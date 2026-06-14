#!/usr/bin/env python3
"""Size-ladder experiment — answers Eddie's question: "64 rules at 90%, what model
size does that get us?" — and the Path-A-vs-B question: does a *fine-tuned* small
model beat a bigger *prompt-baked* one at holding the full rule set?

Unlike run.py (one generation per N), this does GENS independent generations per
(model, N) and reports mean +/- std — real error bars, so a dip is signal not noise.

  MODELS : the ladder (env-overridable). Ollama locals + claude cloud subjects.
  NS     : rule counts to test (default just 64 — the question).
  GENS   : independent generations per (model, N) for error bars.
  JUDGE  : openai/gpt-oss-120b (Groq), same as run.py.

Usage:
  zsh -ic 'python3 size_ladder.py'                         # full ladder
  MODELS=gemma3-ablit:12b GENS=1 python3 size_ladder.py    # pilot
Writes size-ladder.jsonl (per-gen) + size-ladder-summary.tsv (aggregates).
"""
import json, os, random, statistics, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = [l.strip() for l in open(os.path.join(HERE, "rules.txt")) if l.strip()]
ASSIGN = open(os.path.join(HERE, "ASSIGNMENT.md")).read()
JUDGE = os.environ.get("JUDGE", "openai/gpt-oss-120b")
NS = [int(x) for x in os.environ.get("NS", "64").split(",")]
GENS = int(os.environ.get("GENS", "3"))
K = int(os.environ.get("K", "10"))
TEMP = float(os.environ.get("TEMP", "0.5"))          # >0 so GENS actually diverge
GROQ_KEY = os.environ["GROQ_API_KEY"]

# The ladder. (size, name, kind). kind: 'base' prompt-baked | 'ft' fine-tuned | 'cloud'
DEFAULT_MODELS = [
    ("8B",  "llama3.1:8b",                     "base"),
    ("8Bft","eds-rules-llama:latest",          "ft"),     # Path B: fine-tuned vs its base
    ("8Bft","granite-coding-rules-8b-v0.3.1:latest", "ft"),
    ("12B", "gemma3-ablit:12b",                "base"),
    ("27B", "gemma3:27b",                      "base"),
    ("34B", "codellama:34b-instruct",          "base"),
    ("cloud","claude-opus-4-8",                "cloud"),
    ("cloud","claude-fable-5",                 "cloud"),
]
if os.environ.get("MODELS"):
    DEFAULT_MODELS = [("?", m.strip(), "ft" if "rules" in m else "cloud" if m.startswith("claude") else "base")
                      for m in os.environ["MODELS"].split(",")]


def chat(model, messages):
    if model.startswith("claude"):
        sysmsg = next((m["content"] for m in messages if m["role"] == "system"), "")
        conv = [m for m in messages if m["role"] != "system"]
        body = {"model": model, "max_tokens": 8000, "system": sysmsg, "messages": conv}
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(),
            headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
                     "content-type": "application/json", "user-agent": "curl/8.7.1"})
        d = json.load(urllib.request.urlopen(req, timeout=600))
        return "".join(b.get("text", "") for b in d.get("content", []))
    body = {"model": model, "messages": messages, "stream": False,
            "options": {"temperature": TEMP, "num_ctx": 8192}}
    req = urllib.request.Request("http://localhost:11434/api/chat",
        data=json.dumps(body).encode(), headers={"content-type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=1800))["message"]["content"]


def judge(rule, work):
    sysmsg = ("You are a strict senior engineer. Score 0-100 how well the produced "
              "work follows ONE rule (0 = clearly violates, 100 = fully follows). "
              "If the rule is a development *process* (committing, secret-scanning, "
              "pushing, code review, deploy gates) that a static set of files cannot "
              "demonstrate, or it otherwise does not apply, respond \"NA\" instead "
              "(NA is excluded from the grade). Judge only the files produced.")
    user = (f"RULE:\n{rule}\n\nASSIGNMENT:\n{ASSIGN[:1200]}\n\nWORK PRODUCED:\n"
            f"{work[:14000]}\n\nReply with JSON only: "
            '{"score": <integer 0-100, or the string "NA">, "reason": "<one sentence>"}')
    body = {"model": JUDGE, "temperature": 0, "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": sysmsg}, {"role": "user", "content": user}]}
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"authorization": f"Bearer {GROQ_KEY}", "content-type": "application/json",
                 "user-agent": "curl/8.7.1"})
    txt = json.load(urllib.request.urlopen(req, timeout=120))["choices"][0]["message"]["content"]
    try:
        j = json.loads(txt); sc = j["score"]
        if isinstance(sc, str) and sc.strip().upper().startswith("NA"):
            return None
        return max(0, min(100, int(sc)))
    except Exception:
        return None


def weighted_sample(n, k, rng):
    idx = list(range(n)); chosen = []
    for _ in range(min(k, n)):
        pool = [i for i in idx if i not in chosen]
        w = [1.0 / (i + 1) for i in pool]
        r = rng.random() * sum(w); acc = 0
        for i, wi in zip(pool, w):
            acc += wi
            if acc >= r:
                chosen.append(i); break
    return sorted(chosen)


def grade_one_gen(model, N, gen_idx):
    """One independent generation -> mean judge score over a weighted rule sample."""
    sysprompt = ("You are an expert engineer. Follow ALL of these rules in everything "
                 "you produce:\n" + "\n".join(f"{i+1}. {RULES[i]}" for i in range(N)))
    msgs = [{"role": "system", "content": sysprompt}, {"role": "user", "content": ASSIGN}]
    impl = chat(model, msgs)
    msgs += [{"role": "assistant", "content": impl},
             {"role": "user", "content": "Do ONE polish round: clean up, remove dead "
              "code, finalize, make the version visible. Output the final files."}]
    work = impl + "\n\n=== POLISH ===\n" + chat(model, msgs)
    rng = random.Random(900 + N * 100 + gen_idx)
    sampled = weighted_sample(N, K, rng)
    scores = [judge(RULES[i], work) for i in sampled]
    vals = [s for s in scores if s is not None]
    na = sum(1 for s in scores if s is None)
    return (sum(vals) / len(vals) if vals else None), na


def run():
    out = open(os.path.join(HERE, "size-ladder.jsonl"), "a")
    sm = open(os.path.join(HERE, "size-ladder-summary.tsv"), "a")
    print(f"judge={JUDGE} NS={NS} GENS={GENS} K={K} temp={TEMP}\n")
    print(f"{'model':<38}{'size':>5}{'kind':>6}{'N':>5}{'mean':>7}{'std':>6}  per-gen")
    for size, model, kind in DEFAULT_MODELS:
        for N in NS:
            grades, na_tot = [], 0
            for g in range(GENS):
                try:
                    grade, na = grade_one_gen(model, N, g)
                except Exception as e:
                    out.write(json.dumps({"model": model, "N": N, "gen": g, "error": str(e)[:200]}) + "\n"); out.flush()
                    continue
                if grade is not None:
                    grades.append(grade)
                na_tot += na
                out.write(json.dumps({"model": model, "size": size, "kind": kind, "N": N,
                    "gen": g, "grade": grade, "na": na}) + "\n"); out.flush()
            if grades:
                mean = statistics.mean(grades)
                std = statistics.pstdev(grades) if len(grades) > 1 else 0.0
                pg = [round(x) for x in grades]
            else:
                mean = std = float("nan"); pg = []
            print(f"{model:<38}{size:>5}{kind:>6}{N:>5}{mean:>7.1f}{std:>6.1f}  {pg}")
            sm.write(f"{model}\t{size}\t{kind}\t{N}\t{mean:.1f}\t{std:.1f}\t{len(grades)}\t{na_tot}\n"); sm.flush()
    out.close(); sm.close()
    print("\nwrote size-ladder.jsonl + size-ladder-summary.tsv")


if __name__ == "__main__":
    run()
