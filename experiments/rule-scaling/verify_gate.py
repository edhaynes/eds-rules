#!/usr/bin/env python3
"""Verify gate — the system component that earns the 90%.

The size law says a cheap model can't hold the full rule set, and the good-enough
bar says it doesn't have to. The gate is what makes that true: a cheap-tier model
does the work, a fast verifier scores it against the task's rule slice, and:

    pass  (>= threshold) -> ship it, cheap.
    fail  (<  threshold) -> escalate to T3 (Opus) and ship that instead.

The cheap model only has to be good enough OFTEN enough — the gate catches the
misses and the escalation rate is the cost. System quality comes from the pipeline,
not from a perfect small model.

Config (all env-overridable, no hardcoded values):
    CHEAP      cheap-tier model         (default qwen2.5-coder:14b)
    T3         escalation target        (default claude-opus-4-8)
    THRESHOLD  gate pass mark, 0-100    (default 80)
    SLICE_N    top-N rules in the slice (default 14 — Jason's 1-per-B budget)
    JUDGE      verifier model           (default openai/gpt-oss-120b on Groq)
"""
import json
import os
import statistics
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = [l.strip() for l in open(os.path.join(HERE, "rules.txt")) if l.strip()]
ASSIGNMENT = open(os.path.join(HERE, "ASSIGNMENT.md")).read()

CHEAP = os.environ.get("CHEAP", "qwen2.5-coder:14b")
T3 = os.environ.get("T3", "claude-opus-4-8")
JUDGE = os.environ.get("JUDGE", "openai/gpt-oss-120b")
THRESHOLD = float(os.environ.get("THRESHOLD", "80"))
SLICE_N = int(os.environ.get("SLICE_N", "14"))
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
RETRIES = int(os.environ.get("RETRIES", "4"))
UA = "curl/8.7.1"   # Groq's Cloudflare 1010-blocks the default urllib UA


def _post(url, body, headers, timeout):
    last = None
    for _ in range(RETRIES):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
            return json.load(urllib.request.urlopen(req, timeout=timeout))
        except (urllib.error.URLError, ConnectionResetError, TimeoutError) as e:
            last = e
    raise last


def chat(model, messages):
    """Run a chat completion on Ollama (local) or the Anthropic API (claude*)."""
    if model.startswith("claude"):
        sysmsg = next((m["content"] for m in messages if m["role"] == "system"), "")
        conv = [m for m in messages if m["role"] != "system"]
        d = _post("https://api.anthropic.com/v1/messages",
                  {"model": model, "max_tokens": 8000, "system": sysmsg, "messages": conv},
                  {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
                   "content-type": "application/json", "user-agent": UA}, 600)
        return "".join(b.get("text", "") for b in d.get("content", []))
    d = _post(OLLAMA_URL,
              {"model": model, "messages": messages, "stream": False,
               "options": {"temperature": 0.3, "num_ctx": 8192}},
              {"content-type": "application/json"}, 1800)
    return d["message"]["content"]


def do_work(model, task, rule_slice):
    """A model does the assignment under its rule slice, then one polish round."""
    sysprompt = ("You are an expert engineer. Follow ALL of these rules in everything "
                 "you produce:\n" + "\n".join(f"{i+1}. {r}" for i, r in enumerate(rule_slice)))
    msgs = [{"role": "system", "content": sysprompt}, {"role": "user", "content": task}]
    impl = chat(model, msgs)
    msgs += [{"role": "assistant", "content": impl},
             {"role": "user", "content": "Do ONE polish round: clean up, remove dead code, "
              "finalize, make the version visible. Output the final files."}]
    return impl + "\n\n=== POLISH ===\n" + chat(model, msgs)


class VerifyGate:
    """Scores produced work against a rule slice and rules pass/escalate."""

    def __init__(self, rule_slice, threshold=THRESHOLD, judge=JUDGE):
        self._slice = rule_slice
        self._threshold = threshold
        self._judge = judge

    def _score_rule(self, rule, work):
        """0-100 adherence for one rule, or None if the rule doesn't apply (excluded)."""
        sysmsg = ("You are a strict senior engineer. Score 0-100 how well the produced "
                  "work follows ONE rule (0 = clearly violates, 100 = fully follows). If "
                  "the rule is a process a static set of files cannot demonstrate, or does "
                  "not apply, respond \"NA\" (excluded). Judge only the files produced.")
        user = (f"RULE:\n{rule}\n\nWORK PRODUCED:\n{work[:14000]}\n\nReply with JSON only: "
                '{"score": <integer 0-100, or the string "NA">}')
        d = _post("https://api.groq.com/openai/v1/chat/completions",
                  {"model": self._judge, "temperature": 0,
                   "response_format": {"type": "json_object"},
                   "messages": [{"role": "system", "content": sysmsg},
                                {"role": "user", "content": user}]},
                  {"authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
                   "content-type": "application/json", "user-agent": UA}, 120)
        try:
            sc = json.loads(d["choices"][0]["message"]["content"])["score"]
            if isinstance(sc, str) and sc.strip().upper().startswith("NA"):
                return None
            return max(0, min(100, int(sc)))
        except (KeyError, ValueError, json.JSONDecodeError):
            return None

    def assess(self, work):
        """Return (mean_score, per_rule_scores, passed)."""
        scores = [self._score_rule(r, work) for r in self._slice]
        applied = [s for s in scores if s is not None]
        mean = statistics.mean(applied) if applied else float("nan")
        return mean, scores, (mean == mean and mean >= self._threshold)


def run_with_gate(task, slice_n=SLICE_N, cheap=CHEAP, t3=T3, threshold=THRESHOLD):
    """Route a task through cheap -> verify -> escalate-if-needed. Returns the decision."""
    rule_slice = RULES[:slice_n]
    gate = VerifyGate(rule_slice, threshold)

    cheap_work = do_work(cheap, task, rule_slice)
    cheap_score, _, passed = gate.assess(cheap_work)
    if passed:
        return {"served_by": cheap, "tier": "cheap", "score": round(cheap_score, 1),
                "escalated": False, "cheap_score": round(cheap_score, 1), "work": cheap_work}

    t3_work = do_work(t3, task, rule_slice)
    t3_score, _, _ = gate.assess(t3_work)
    return {"served_by": t3, "tier": "T3", "score": round(t3_score, 1), "escalated": True,
            "cheap_score": round(cheap_score, 1), "work": t3_work}


def main():
    print(f"verify gate · cheap={CHEAP} · T3={T3} · threshold={THRESHOLD} · slice=top-{SLICE_N}\n")
    r = run_with_gate(ASSIGNMENT)
    verdict = "ESCALATED to T3" if r["escalated"] else "shipped CHEAP"
    print(f"cheap ({CHEAP}) scored {r['cheap_score']}  ->  {verdict}")
    print(f"final: served by {r['served_by']} at {r['score']} (threshold {THRESHOLD})")
    if r["escalated"]:
        print("  (cheap output was below the bar; the gate caught it and bounced it up.)")
    else:
        print("  (cheap output cleared the bar; T3 never touched — that's the cost win.)")


if __name__ == "__main__":
    main()
