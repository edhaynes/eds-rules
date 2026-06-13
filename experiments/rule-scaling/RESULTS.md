# Rule-scaling experiment — results (run 1, 2026-06-13)

Subject: granite3.1-dense:2b (rules prompt-baked) · Judge: openai/gpt-oss-120b ·
Task: 10-min full-stack URL-shortener + one polish round · K=10 top-weighted
sample · 3 repeats · corpus = real 100 rules + 28 padding.

## The curve — grade (0–100) vs. N rules in context
```
  N=1    50.0   (only rule 1, a process rule → N/A baseline)
  N=2    75.0   ┐ peak — a 2B nails a handful
  N=4    75.0   ┘
  N=8    56.2
  N=16   52.7
  N=32   47.2
  N=64   43.7   ← worst
  N=128  49.8   (noise; per-rep 56/40/54)
```
165 judgments: 36 clear violations (≤25), 37 clean follows (≥90), 90 N/A (≈50).

## Finding
**A 2B model has a finite rule budget.** It follows ~2–8 prompt-baked rules
cleanly; adherence then degrades as the rule count climbs — roughly halving the
"win" by N≈64. The judge's reasons at high N are concrete: drops the tests,
hardcodes ports/paths, assumes a Unix shell, adds undeclared dependencies,
ships buggy code. Piling on more rules makes it obey *fewer*.

## Caveats (honest)
- One generation per N (stochastic); grades are noisy (N=128 bump is within noise).
- Many top rules are *process* rules scored N/A (50), compressing absolute grades
  toward the middle — the **shape** (peak at 2–4, decline) is the signal, not the level.
- Single judge model; single corpus order.

## Highest-value follow-ups
1. **Fine-tune vs prompt-bake** — retrain Granite 2B on the rules (Way 2) and rerun.
   Does ingraining the rules raise the budget / flatten the decline? This directly
   tests the "train Jason" plan (PLAN_persona-models).
2. **Medium tier** — same sweep on Llama 3.1 8B; does the bigger model hold more rules?
3. **Fixed code-testable rule set** — grade the same N artifact-observable rules at
   every N for clean apples-to-apples.
4. More generations per N + error bars for a publishable curve.
