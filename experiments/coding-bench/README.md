# Coding benchmark — HumanEval, test-graded

Real coding capability (not rule-following): generate the function, run the actual
unit tests, score pass@1. Tests the fleet thesis — cheap "Jason" (Qwen) nails the
chunks it can; only the hard residual ("real coding") needs Opus.

## Fetch the dataset (gitignored — MIT, openai/human-eval)
```
curl -sL "https://github.com/openai/human-eval/raw/master/data/HumanEval.jsonl.gz" \
  -o HumanEval.jsonl.gz && gunzip -kf HumanEval.jsonl.gz
```

## Run (needs GROQ/ANTHROPIC keys in env for cloud models; Ollama for locals)
```
MODELS="qwen2.5-coder:14b,claude-opus-4-8" N=40 python3 coding_bench.py
```
Output: pass@1 per model + the split (both / only-T3 / cheap-only / neither).

SAFETY: runs model-generated code in a subprocess with a hard timeout. HumanEval is
benign; do not point this at untrusted problem sets without a real sandbox.
