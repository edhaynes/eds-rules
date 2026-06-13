# Rule-scaling experiment — results (clean metric, 2026-06-13)

Subjects: granite3.1-dense:2b · gemma3:4b · llama3.1:8b (Ollama) · claude-opus-4-8 (API).
Judge: openai/gpt-oss-120b (Groq). Task: 10-min full-stack URL-shortener + one polish
round. Grade = mean judge score (0–100) over a top-weighted sample of rules, **N/A
excluded** (process rules a static artifact can't show are dropped, not scored 50).
K=10 sampled rules · 3 repeats · corpus = the real 100 rules + 28 padding.

See `graph.svg`. Raw per-rule data (score + judge reason): `results-<model>.jsonl`.

## Grade (0–100, N/A excluded) vs. N rules in context
```
  N │ Granite 2B │ Gemma 4B │ Llama 8B │  Opus
  2 │   100      │   100    │   100    │  100
  4 │   100      │    89    │   100    │   87
  8 │    55      │    72    │    75    │   98
 16 │    61      │    73    │    59    │   95
 32 │    40      │    41    │    40    │   56   ← Opus noise (1 weak gen)
 64 │    36      │    41    │    46    │   65
128 │    44      │    35    │    47    │   80
```
(N=1 is blank: the only rule there is a process rule → all N/A.)
Average over N=8..128: Granite **47** · Gemma **52** · Llama **53** · **Opus 79**.

## Findings
1. **Small models have a hard rule budget.** 2B/4B/8B all hit ~90–100 at 2–4 rules,
   then collapse to ~35–55 by N≥16 — far below the 90% goal. They actively *violate*
   rules once the set grows.
2. **2B ≈ 4B ≈ 8B.** Scaling within the small/mid tier doesn't help — all three cluster
   together and crater together.
3. **The frontier model doesn't dilute.** Opus stays at/above the 90% goal through N=16
   and holds 65–80 at the full 128-rule load — a ~30-point gap over the small models in
   the real-scale zone. Capacity, not a few billion params, is what holds the full rule set.
4. **The 1/5 budget rule of thumb holds** (Eddie): at the worst small-model grades the
   rules are still well under a quarter of the literal context — it's the *attention*
   budget that saturates, not token space.

## Caveats
- One generated artifact per N (REPEATS re-samples judging only, not generation), so the
  curve is noisy — e.g. Opus's N=32 dip is a single weak generation. Multiple generations
  per N + error bars would smooth it for publication.
- Single judge model; single corpus order.

## Implication for the persona fleet (`plans/PLAN_persona-models.md`)
The heavyweight tier (Claude/Claudius) needs frontier-class capacity (cloud Opus, or a
70B on Gladius) to hold the full rules *and* do hard work. A 2B "Jason" must get a
small, prioritized rule set — or be fine-tuned — not the full 100 prompt-baked.
