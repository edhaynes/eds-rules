#!/usr/bin/env python3
"""Real coding benchmark — HumanEval, test-graded (not judge-graded).

Tests the fleet's coding thesis: a cheap model ("Jason", Qwen) nails the chunks it
can, and only the hard residual needs Opus ("the real coding"). Each problem is a
function spec + hidden unit tests; we generate the function, run the ACTUAL tests in
a subprocess, and score pass@1 — objective, no LLM judge.

Output buckets the problems three ways so Jason's decomposition target is visible:
  - cheap solves        -> Jason's domain (the chunks worth keeping cheap)
  - only T3 solves       -> the hard 10% (real coding -> escalate)
  - neither solves       -> needs decomposition into smaller chunks

Config (env): MODELS (default qwen2.5-coder:14b,claude-opus-4-8) · N problems
(default 40) · TIMEOUT secs per test (default 12) · SEED.

SAFETY: executes model-generated code in a subprocess with a hard timeout in a temp
dir. HumanEval problems are benign algorithmic functions; this is the standard way
the benchmark is run. Do not point it at untrusted problem sets without a sandbox.
"""
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = [json.loads(l) for l in open(os.path.join(HERE, "HumanEval.jsonl")) if l.strip()]
MODELS = os.environ.get("MODELS", "qwen2.5-coder:14b,claude-opus-4-8").split(",")
N = int(os.environ.get("N", "40"))
TIMEOUT = int(os.environ.get("TIMEOUT", "12"))
SEED = int(os.environ.get("SEED", "90"))
RETRIES = int(os.environ.get("RETRIES", "4"))
UA = "curl/8.7.1"
FENCE = re.compile(r"```(?:python)?\s*(.*?)```", re.DOTALL)


def _post(url, body, headers, timeout):
    last = None
    for _ in range(RETRIES):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
            return json.load(urllib.request.urlopen(req, timeout=timeout))
        except (urllib.error.URLError, ConnectionResetError, TimeoutError) as e:
            last = e
    raise last


def generate(model, prompt):
    instr = ("Complete this Python function. Output ONLY the full function as a single "
             "Python code block — signature, body, and any imports it needs. No prose.\n\n" + prompt)
    if model.startswith("claude"):
        d = _post("https://api.anthropic.com/v1/messages",
                  {"model": model, "max_tokens": 1500,
                   "messages": [{"role": "user", "content": instr}]},
                  {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
                   "content-type": "application/json", "user-agent": UA}, 180)
        txt = "".join(b.get("text", "") for b in d.get("content", []))
    else:
        d = _post("http://localhost:11434/api/chat",
                  {"model": model, "stream": False, "options": {"temperature": 0.1, "num_ctx": 4096},
                   "messages": [{"role": "user", "content": instr}]},
                  {"content-type": "application/json"}, 600)
        txt = d["message"]["content"]
    m = FENCE.search(txt)
    return (m.group(1) if m else txt).strip()


def passes(code, problem):
    """Run the problem's real unit tests against generated code. True iff exit 0."""
    program = f"{code}\n\n{problem['test']}\n\ncheck({problem['entry_point']})\n"
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, dir=tempfile.gettempdir()) as f:
        f.write(program)
        path = f.name
    try:
        r = subprocess.run([sys.executable, path], capture_output=True, timeout=TIMEOUT)
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    finally:
        os.unlink(path)


def run():
    rng = random.Random(SEED)
    subset = rng.sample(PROBLEMS, min(N, len(PROBLEMS)))
    out = open(os.path.join(HERE, "coding-bench-results.jsonl"), "w")
    results = {m: {} for m in MODELS}
    print(f"HumanEval · {len(subset)} problems · models={MODELS} · timeout={TIMEOUT}s\n")
    for i, p in enumerate(subset):
        line = f"{i+1:>3}/{len(subset)} {p['task_id']:<14}"
        for m in MODELS:
            try:
                code = generate(m, p["prompt"])
                ok = passes(code, p)
            except Exception as e:
                ok = False
                out.write(json.dumps({"model": m, "task": p["task_id"], "error": str(e)[:150]}) + "\n")
            results[m][p["task_id"]] = ok
            out.write(json.dumps({"model": m, "task": p["task_id"], "passed": ok}) + "\n")
            out.flush()
            line += f"  {m.split('/')[-1][:18]}={'P' if ok else '.'}"
        print(line)
    out.close()

    print("\n=== pass@1 ===")
    for m in MODELS:
        n_pass = sum(results[m].values())
        print(f"  {m:<28} {n_pass}/{len(subset)}  ({100*n_pass/len(subset):.0f}%)")

    if len(MODELS) >= 2:
        cheap, t3 = MODELS[0], MODELS[-1]
        tasks = [p["task_id"] for p in subset]
        cheap_only = [t for t in tasks if results[cheap][t] and not results[t3][t]]
        t3_only = [t for t in tasks if results[t3][t] and not results[cheap][t]]
        neither = [t for t in tasks if not results[cheap][t] and not results[t3][t]]
        both = [t for t in tasks if results[cheap][t] and results[t3][t]]
        print(f"\n=== the split (cheap={cheap} vs T3={t3}) ===")
        print(f"  both solve (cheap's domain): {len(both)}")
        print(f"  only T3 (the hard 10%):      {len(t3_only)}  {t3_only}")
        print(f"  cheap-only (T3 flaked):      {len(cheap_only)}  {cheap_only}")
        print(f"  neither (needs decompose):   {len(neither)}  {neither}")
        with open(os.path.join(HERE, "coding-bench-summary.txt"), "w") as s:
            s.write(f"HumanEval {len(subset)} problems\n")
            for m in MODELS:
                np = sum(results[m].values())
                s.write(f"{m}\t{np}/{len(subset)}\t{100*np/len(subset):.0f}%\n")
            s.write(f"both={len(both)} t3_only={len(t3_only)} cheap_only={len(cheap_only)} neither={len(neither)}\n")
    print("\nwrote coding-bench-results.jsonl + coding-bench-summary.txt")


if __name__ == "__main__":
    run()
