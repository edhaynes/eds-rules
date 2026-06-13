#!/usr/bin/env python3
"""Rule-scaling experiment — does a small model's rule-following decay as the
rule count grows?

For N in 1,2,4,...,128: feed the top-N rules into the SUBJECT model (Granite 2B),
have it do a fixed ~10-minute full-stack assignment plus one polish round, then
grade how much of the produced work obeys a top-weighted random sample of the
N rules. Grade = mean judge score (0-100). The curve of grade vs N is the result.

  SUBJECT:  granite3.1-dense:2b   (Ollama, local)
  JUDGE:    openai/gpt-oss-120b   (Groq API, GROQ_API_KEY from env)

Usage:  python3 run.py            # full sweep
        NS=1,2,4,8 python3 run.py # custom sweep (pilot)
Writes results.jsonl + prints the curve.
"""
import json, os, random, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = [l.strip() for l in open(os.path.join(HERE, "rules.txt")) if l.strip()]
ASSIGN = open(os.path.join(HERE, "ASSIGNMENT.md")).read()
SUBJECT = os.environ.get("SUBJECT", "granite3.1-dense:2b")
JUDGE = os.environ.get("JUDGE", "openai/gpt-oss-120b")
NS = [int(x) for x in os.environ.get("NS", "1,2,4,8,16,32,64,128").split(",")]
K = int(os.environ.get("K", "10"))          # rules sampled per grade
REPEATS = int(os.environ.get("REPEATS", "1"))
SEED = 90                                    # reproducible
GROQ_KEY = os.environ["GROQ_API_KEY"]


def ollama_chat(messages):
    if SUBJECT.startswith("claude"):                       # Anthropic API subject (frontier control)
        sysmsg = next((m["content"] for m in messages if m["role"] == "system"), "")
        conv = [m for m in messages if m["role"] != "system"]
        body = {"model": SUBJECT, "max_tokens": 8000, "system": sysmsg, "messages": conv}
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
            data=json.dumps(body).encode(),
            headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
                     "content-type": "application/json", "user-agent": "curl/8.7.1"})
        d = json.load(urllib.request.urlopen(req, timeout=300))
        return "".join(b.get("text", "") for b in d.get("content", []))
    body = {"model": SUBJECT, "messages": messages, "stream": False,
            "options": {"temperature": 0.2, "num_ctx": 8192}}
    req = urllib.request.Request("http://localhost:11434/api/chat",
        data=json.dumps(body).encode(), headers={"content-type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=900))["message"]["content"]


def judge(rule, work):
    """Return (score 0-100, reason) or (None, reason) for NOT APPLICABLE (excluded)."""
    sysmsg = ("You are a strict senior engineer. Score 0-100 how well the produced "
              "work follows ONE rule (0 = clearly violates, 100 = fully follows). "
              "If the rule is a development *process* (committing, secret-scanning, "
              "pushing, code review, deploy gates) that a static set of files cannot "
              "demonstrate, or it otherwise does not apply, respond \"NA\" instead "
              "(NA is excluded from the grade, not scored). Judge only the files "
              "actually produced, not intentions.")
    user = (f"RULE:\n{rule}\n\nASSIGNMENT:\n{ASSIGN[:1200]}\n\nWORK PRODUCED:\n"
            f"{work[:14000]}\n\nReply with JSON only: "
            '{"score": <integer 0-100, or the string "NA">, "reason": "<one sentence>"}')
    body = {"model": JUDGE, "temperature": 0, "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": sysmsg},
                         {"role": "user", "content": user}]}
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"authorization": f"Bearer {GROQ_KEY}", "content-type": "application/json",
                 "user-agent": "curl/8.7.1"})   # Groq's Cloudflare 1010-blocks the default urllib UA
    txt = json.load(urllib.request.urlopen(req, timeout=120))["choices"][0]["message"]["content"]
    try:
        j = json.loads(txt); sc = j["score"]; why = j.get("reason", "")
        if isinstance(sc, str) and sc.strip().upper().startswith("NA"):
            return None, why
        return max(0, min(100, int(sc))), why
    except Exception:
        return None, "parse-fail"


def weighted_sample(n, k, rng):
    """k distinct rule indices from 0..n-1, weight ∝ 1/(rank) — top-weighted."""
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


def run():
    safe = SUBJECT.replace("/", "_").replace(":", "-")
    out = open(os.path.join(HERE, f"results-{safe}.jsonl"), "w")   # per-model raw data (no clobber)
    print(f"subject={SUBJECT} judge={JUDGE} K={K} repeats={REPEATS}\n")
    print(f"{'N':>4}  {'grade':>6}  sampled-rule scores")
    for N in NS:
        sysprompt = ("You are an expert engineer. Follow ALL of these rules in "
                     "everything you produce:\n" +
                     "\n".join(f"{i+1}. {RULES[i]}" for i in range(N)))
        msgs = [{"role": "system", "content": sysprompt},
                {"role": "user", "content": ASSIGN}]
        impl = ollama_chat(msgs)
        msgs += [{"role": "assistant", "content": impl},
                 {"role": "user", "content": "Do ONE polish round: clean up, remove "
                  "dead code, finalize, and make the version visible. Output the final files."}]
        final = ollama_chat(msgs)
        work = impl + "\n\n=== POLISH ROUND ===\n" + final
        reps, na_counts = [], []
        for rep in range(REPEATS):
            rng = random.Random(SEED + N * 1000 + rep)
            sampled = weighted_sample(N, K, rng)
            judged = [judge(RULES[i], work) for i in sampled]
            vals = [s for s, _ in judged if s is not None]    # N/A excluded from the grade
            na = sum(1 for s, _ in judged if s is None)
            reps.append(sum(vals) / len(vals) if vals else float("nan"))
            na_counts.append(na)
            out.write(json.dumps({"N": N, "rep": rep, "sampled": sampled, "na": na,
                "scores": [s for s, _ in judged],
                "reasons": [{"rule": RULES[i][:70], "score": s, "why": r}
                            for i, (s, r) in zip(sampled, judged)],
                "grade": reps[-1]}) + "\n"); out.flush()
        good = [x for x in reps if x == x]        # drop nan (all-N/A reps)
        grade = sum(good) / len(good) if good else float("nan")
        na_avg = sum(na_counts) / len(na_counts)
        ftoks = len(sysprompt) // 4
        print(f"{N:>4}  {grade:6.1f}  ~{ftoks:>5}tok  na/rep={na_avg:.1f}  {[round(x) for x in good]}")
        with open(os.path.join(HERE, "summary.tsv"), "a") as sm:
            sm.write(f"{SUBJECT}\t{N}\t{grade:.1f}\t{ftoks}\t{na_avg:.1f}\n")
    out.close()
    print("\nwrote results.jsonl")


if __name__ == "__main__":
    run()
