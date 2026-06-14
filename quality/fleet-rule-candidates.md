# AI-fleet rule candidates (2026-06-14)

A coherent new chapter emerging from the rule-scaling + coding-bench work: **rules for
running a multi-model AI dev fleet.** Candidates for `RULES.md`, entering via slots freed
by the merge pass (F20) so the count stays 100. Each is evidence-backed by `experiments/`.

1. **The sizing law — ~1 rule per billion params.** A model reliably holds ~1 rule/B at
   the 90% bar (2B→2, 8B→8, 14B→14). Never ask a model to hold more rules than it has
   billions of parameters. *Evidence: size ladder — 64 rules @ 90% needs ~64B; every local
   model (≤34B) flatlined at ~35.*

2. **Slice the rules to the seat.** Give each model/task only the rules its job needs — a
   *view* of the canon, not the whole book. The canon is the union of all slices; no seat
   holds all of it. *Evidence: Qwen-14B codes at 90% but follows 14 rules at 68% — the
   bottleneck is rule-load, not capability. Free the coder of the rule-load and its ability
   shows through.*

3. **Context ceiling by tier.** A little model never deals with more than **~8k context**
   (they go bonkers past ~8–10k); a frontier model is safe to **~128k**. Bound every
   cheap-tier task to ≤8k — slice the input, not just the rules. *Evidence: Eddie's field
   observation across many small-model runs.*

4. **Bite-size, parallel-capable, ≥90% chunks.** Chunk every task into bite-size,
   parallel-capable units, each sized for ≥90% quality first try; >10% first-try-failure
   risk or not independently runnable → split further. *(Lands by merging rules 15 + 98.)*

5. **Good enough at the model, 90% at the system.** A cheap model only has to be good
   enough to try first; the 90% bar belongs to the *system* — cheap model + verify gate +
   escalate-the-residual — not to each tier. *Evidence: verify gate + the coding split
   (cheap does 90%, the hard 10% escalates).*

These cohere into one "operate the fleet" chapter. The unifying idea: **match the work to
the model — size, rules, and context all scale together — and let the system, not any one
model, carry the quality bar.**
