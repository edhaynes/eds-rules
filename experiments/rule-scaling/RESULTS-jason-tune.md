# Does fine-tuning lift the cheap tier? — NO (recall data is a net loss) · 2026-06-14

Tuned **Qwen2.5-Coder-14B** with QLoRA on the v0.3.1 recall/refuse dataset (1610
examples, 3 epochs) on gx10, exported to GGUF, served, and evaluated against the base
on the same hardware and harness.

## Training looked great
- eval loss **0.059**, token accuracy **97.6%** — the model memorised the rules' recall-
  and-refuse format cold. (That low a loss is itself an overfit flag.)

## In-task, it was a net loss
| metric | tuned jason-qwen14b | base qwen2.5-coder:14b |
|---|---|---|
| rule-following @ N=14 (3 gens) | **50.5 ± 1.5** | **57.5 ± 9.2** |
| coding pass@1 (HumanEval, 20) | **85%** | **95%** |
| rule recall (training eval) | 97.6% | — |

The tune **recites rules perfectly but does the actual job worse** — it follows rules
slightly *worse* while coding (50.5 vs 57.5) and codes *worse* (85% vs 95%). It also
collapsed the model's variance (±1.5 vs ±9.2): rigid, deterministic recitation behaviour.

## Findings
1. **Recall-style fine-tuning does not teach in-task rule application — it teaches
   reciting.** Knowing "what is rule N" verbatim is not the same skill as obeying rule N
   while writing code, and training the former slightly suppresses the latter.
2. **Overfitting traded capability for memorisation.** 3 epochs to loss 0.059 cost ~10
   points of coding ability. Fewer epochs, lower LR, and regularisation would be needed
   just to *not lose ground*.
3. **The architecture, not model-tuning, is what delivers the 90%.** This session's real
   wins were the *system* — slice the rules to the seat, verify, escalate the residual
   (rules 95/97/99). Fine-tuning the cheap tier on recall data is a dead end.
4. **Always GENS≥3.** The base swings 46→69 across generations (±9.2); the earlier "68"
   was a lucky single run. Single-gen comparisons are noise.

## If fine-tuning is pursued further
- Train on **application/reasoning data** — examples of obeying rules *while doing the
  task* — not Q&A recall.
- Regularise hard (1 epoch, low LR, early stop on an *in-task* eval, not a recall eval).
- Gate every tune on the in-task eval (rule-following @N + coding pass@1), never on
  training loss — training loss said "great," in-task said "worse."
