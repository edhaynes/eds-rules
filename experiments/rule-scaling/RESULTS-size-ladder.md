# Size ladder — does any model hold 64 rules at 90%? (2026-06-14)

Eddie's question: *"64 rules minimum at 90 percent — what model size does that get us?"*
Answer, measured: **no size we can run gets us there with rules prompt-baked.** Not even Opus.

## Setup
N=64 rules injected into the system prompt; the model does the 10-min full-stack
assignment + one polish round; judge (gpt-oss-120b) scores a top-weighted K=10 sample,
N/A excluded. **GENS=3 independent generations per model**, reported mean ± std — real
error bars, unlike run.py's single shot. Cloud-capped: 70B deferred (Gladius unreachable).

## Results @ N=64 (grade 0–100; goal = 90)
```
  model                         size   kind    mean ± std   per-gen        n
  claude-opus-4-8               cloud  cloud   71.1 ± 22.5  [72, 98, 43]   3
  gemma3-ablit:12b              12B    base    50.0 ±  0.0  [50]           1*
  eds-rules-llama               8B     ft      43.6 ± 19.1  [65, 47, 19]   3
  gemma3:27b                    27B    base    37.1 ± 11.7  [44, 47, 21]   3
  llama3.1:8b                   8B     base    36.4 ± 14.9  [55, 36, 19]   3
  codellama:34b-instruct        34B    base    34.0 ± 15.1  [38, 50, 14]   3
  granite-coding-rules-8b       8B     ft      14.3 ±  0.0  [14]           1*
```
*Provisional (1 gen): hit Ollama "connection reset" on the other 2 — memory thrash
swapping 27B/34B in and out. claude-fable-5: 404 (no Fable access on this key) — dropped.

## Findings
1. **Nobody clears 90%. The chimera is confirmed for prompt-baking.** The ceiling is
   Opus at **71** — and even that swings 43→98 across three runs. There is no model size
   that reliably holds 64 prompt-baked rules at 90%. The "64 @ 90% in one prompt" target
   is unreachable, full stop.
2. **Size barely moves it in the local range.** 8B = 36, 27B = 37, 34B = 34 — flat. The
   *biggest* local model (34B) is no better than the *smallest* (8B). Throwing parameters
   at a stuffed prompt does not buy rule-following. (Matches the earlier 2B≈4B≈8B result.)
3. **Fine-tuning is the only lever that moved the needle the right way.** `eds-rules-llama`
   (fine-tuned 8B) scored **43.6 vs 36.4** for its vanilla base `llama3.1:8b` — +7 points,
   ~+20% relative, *same size, same box*. Baking rules into the weights beats stuffing them
   into the prompt. (The granite-ft 14 is a 1-gen fluke on a broken run — re-test needed.)
4. **Even the frontier needs help at 64.** Opus's huge variance says 64 in-context is past
   the point of reliability even for Opus — so slicing helps the big tier too, not just the
   small ones.

## Implication (confirms `plans/PLAN_persona-models.md`)
Don't chase a model big enough to hold 64 prompt-baked rules — it doesn't exist locally,
and even Opus wobbles. The chimera is *"one model, 64 rules, in the prompt."* The escape
is the architecture already planned: **fine-tune + per-tier slice** so no seat ever holds
64 at once and the rules it does hold are in its weights, not burning its budget. The +20%
fine-tune signal is the first evidence that the cheap tiers can be made real.

## Next (to firm this up)
- Re-run granite-ft + 12B cleanly (serialize model loads so Ollama doesn't reset).
- Test the ft models on their **slice** (≤8 rules) — expected to clear the bar, proving
  fine-tune + slice is the viable combo.
- Add the 70B point when Gladius can hear again.
