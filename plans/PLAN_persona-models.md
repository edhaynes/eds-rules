Status: In Progress — 2026-06-13 (3-tier fleet design; awaiting Eddie sign-off, then hand S1/S3 to Claude)
Author: Jason-eds (architectural decider) with Claudius-eds

# Model fleet — a 3-tier, route-by-task design

## The thesis (Eddie, 2026-06-13)
Three model tiers, bound by **task class, not by persona**. The goal: **90% of all task
volume completes in the first two (cheap, local) tiers; only the hardest ~10% escalates
to the expensive frontier tier.** That is the cost-and-power thesis — reserve the
1T-class model for the 10% that genuinely needs it; everything routine runs on a 2B or
8B that costs ~nothing and runs on hardware we own.

## The sizing law (Eddie, 2026-06-14): one rule per billion params
Rule of thumb: **a model reliably holds ~1 rule per billion parameters at the 90% bar.**
2B → ~2, 8B → ~8, 14B → ~14, 16B → ~16; the full consolidated ~70 needs a ~70B; 100 → ~100B.
This is the unifying law behind the fleet — and it *retrodicts the size ladder*: 64 rules
needs ~64B, our biggest local was 34B, so every local model flatlined at ~35 and only Opus
(»64B) could even approach 64. **The local "64 @ 90%" chimera was arithmetic.** Consequences:
- **Design each seat to ≤ (its billions) rules.** Jason on a 14B → tune for the **top 14**.
- **Fine-tuning raises the effective count** — rules baked into weights don't spend the
  attention budget — which is what lets a tuned model punch above its billions, and is why
  the cheap tiers can exist at all.
- **The full set lives only on a »70B** (cloud Opus, or a 70B on Gladius) — which is exactly
  why T3 is frontier and the cheap tiers MUST be sliced.

## The three tiers

| Tier | Size | Task class | Examples | Rule budget | Where |
|---|---|---|---|---|---|
| **T1 — grunt** | ~2B | mechanical / tool-calling | `git push`, `ls`, `cat`, `repo_search`, file moves, status checks | **tiny** — only the hard rules that touch the act (secret-scan-before-push, no-hardcode, push discipline, cross-platform paths) | local, anywhere (Mac / iPhone / iPad) |
| **T2 — worker** | ~8B | bounded knowledge work | market & competitor research, writing + running Python tests, dead-code passes, doc edits | **small** — the slice for the job (testing rules for the test seat; GTM/research for Linda) | local, 16GB box |
| **T3 — big guns** | 16B → 1T++ | open-ended hard reasoning | architecture, novel code, tricky merges, multi-file refactors, plan authoring | **full** — holds the whole consolidated set | cloud Opus++ (Gladius is down — "hearing problems"); a 70B local when Gladius returns |

## Why this is the right shape (the evidence)
The rule-scaling experiment (`experiments/rule-scaling`) is the proof: 2B/8B/16B-class
models hold ~8 rules well, then rule-following craters past ~16; only frontier capacity
holds the full set (Opus ~79 avg vs ~50 for the small tier in the real-scale zone). A
small model is **not** failing at *capability* on a mechanical task — it fails when the
task is buried under rules it can't hold. **The move that makes the 90% goal reachable
is to give each tier only the rules its task class needs** — a rule *slice*, not the
full 100. That is the central design decision.

## Achievable goals (2026-06-14 — reset against the size-ladder data)
The size ladder killed the old target: **no runnable model holds 64 prompt-baked rules at
90%** (ceiling = Opus 71, unstable; local size flat at ~35). So we stop chasing that and
set goals we can actually hit. The reframe: **success is each *seat* following its own
*slice* at ≥90% — not any model following all 100.** Nobody holds the full set; that's the
design, not a miss.

| Goal | Target | Basis in the data |
|---|---|---|
| **G1 — T1 grunt budget** | a 2B holds its slice of **≤5 rules** (≤8 if fine-tuned) at ≥90% | small models score ~90–100 only at N≤4; crater past ~8 |
| **G2 — T2 worker budget** | a **fine-tuned 8B** holds **≤10 rules** at ≥90% | fine-tune gave +20% (44 vs 36 at N=64); strong at small N |
| **G3 — T3 budget** | Opus holds **≤16 rules** at ≥90% | measured: Opus 95 @ N=16, degrades past it |
| **G4 — every slice fits its tier** | each per-seat slice ≤ its tier's budget; union == canon | slicing + consolidation (100→~70) make slices fit |
| **G5 — fleet cost goal** | **≥90% of task *volume*** resolved in T1+T2 | most real work is mechanical/bounded → few rules apply |
| **G6 — the proving milestone** | fine-tuned 8B clears **≥90% on its ≤8 slice** (the slice test) | single go/no-go for the cheap-tier thesis |

**Explicitly dropped:** any one model holding 64 prompt-baked rules at 90% — measured
unreachable, off the roadmap. The win comes from *fine-tune + slice*, not bigger models.

## The enablers (these unlock the achievable goals above)
1. **Global rule consolidation (F19 — the deep merge pass).** Shrink the canonical 100
   to a tighter set; fewer rules everywhere raises every tier's ceiling. Cluster
   analysis is done — see **Merge map** below (~100 → ~70, *no rule loosened*).
2. **Per-tier rule slices (the real lever).** Each tier/seat loads only its relevant
   rules. T1 (git push) does not need the testing or architecture rules; the T2 test
   seat does not need the deploy-cadence rules. Slicing keeps every tier inside its
   ~8-rule budget **without dropping any rule from the canon** — the canon is the
   union; each seat sees a view.
3. *(optional boost)* **Fine-tune T1/T2 on their slice** so the rules are ingrained, not
   prompt-budgeted — freeing context for the actual task. Stable rules → fine-tune is
   the right tool (see Training levers).

## Routing & escalation (how a task finds its tier, and the 90% metric)
- A **router** classifies each incoming task → tier (mechanical / bounded-knowledge /
  open-ended). The cheapest tier that can plausibly do it goes first.
- **Escalate on failure or low confidence:** T1 → T2 → T3. A task a tier can't satisfy
  (fails its own check, or low self-confidence) bumps up a tier.
- **The 90% metric IS the success criterion:** over a representative task corpus,
  *fraction of tasks completed correctly without reaching T3 ≥ 90%*. We measure and
  report this — it's the whole point of the fleet.

## Persona → tier (roles bind to tiers by task)
Personas are role+rules contracts; the model is whatever tier the *task* lands in.
- **Jason (PM / merges):** **Qwen2.5-Coder-14B, fine-tuned for the top 14 rules** (1-per-B
  law) + decision drills + merge exemplars; dispatches his mechanical sub-ops (git push,
  status) down to **T1**. Apache-2.0, ARM-native, ~9GB Q4.
- **Claude (backend), Claudius (architect):** **T3 — Opus++.** Hard code and
  architecture are base-capacity problems; only frontier holds the full rules *and*
  does the work.
- **Brutus (tester):** **T2** — 8B running the suite; speed > size.
- **Linda (research / GTM):** **T2** — fast web-capable (Groq GPT-OSS-120B).
- **Claudina (frontend):** **T2 → T3** — code model + RAG over current framework docs.

## Training levers (the decision that actually matters)
Four levers, most people reach for the wrong one:
1. **Base-model choice** — biggest lever for *capability*. A code-specialized model
   beats a general one at code. Pick the base by the seat's domain first.
2. **Prompt-bake (system prompt)** — persona + the rule *slice*. Every seat gets this.
   Free, immediate, no GPU.
3. **Fine-tune / QLoRA** — for **stable** behavior you want *ingrained*: the rules,
   decision style, house code-style. NOT for knowledge that changes.
4. **RAG** — for **large, changing** knowledge: framework docs, library APIs, the repo's
   own ADRs.
> **The correction:** don't fine-tune a model to "know React + Vite" — framework
> knowledge is large and changes; fine-tuning bakes in stale docs. RAG over current
> docs wins. Fine-tune for *your house style and the rules*, not the framework.

So: **base model for capability, RAG for changing knowledge, fine-tune for the rules and
your style, prompt for the persona.**

## Merge map (F19 input — cluster analysis, ~100 → ~70, no loosening)
Each cluster *combines* overlapping rules into one sharper rule; coverage is preserved,
wording tightened. Proposed savings by section (needs Eddie's sign-off before editing
the canonical `RULES.md`):

| Section | Now | → | Merge moves |
|---|---|---|---|
| Secret hygiene (1, 2, 51–60) | 12 | ~5 | 54/55/56/57 → one "scan at every boundary"; 51/58/59 → "hooks + gitignore from day one, rescan on push"; 52/53/60 → "leak response: rotate first, never copy, document the gap"; keep 2 (no hardcode), keep 3 (distrust input) |
| Versioning (61–68) | 8 | ~4 | 61/64/68 → tag discipline (immutable, fetch-before-tag, push-by-name); 62/63 → semver forward-only, one canonical place; 65/67 → build number + display; keep 66 (changelog) |
| Config (20–27) | 8 | ~4 | 20/26 → no hardcoded values / magic numbers; 23/24 → one config layer, X-as-default; 21/22 → validate at startup, never silent fallback; 25/27 → local-zero-setup + `.env.example` |
| Size & complexity (34–38) | 5 | ~2 | 34/37/38 → size limits (files, functions, nesting); 35 → fold into OO/SRP (32); 36 → fold into one-purpose-per-commit (8) |
| Cross-platform (11, 39–43) | 6 | ~3 | 11/40/41/43 → cross-platform primitives + headless/script-everything; 39/42 → target platforms + arches + CI |
| Testing (69–77) | 9 | ~6 | 72/74 → 100% coverage incl. down=stop-fix; 70/71 → contract-first + failing-first; keep 69/73/75/76/77 |
| Architecture (28–33) | 6 | ~4 | 31/32/33 → OO + DI + SOLID + one-class-per-file; keep 28/29/30 |
| Hygiene (87–91) | 5 | ~3 | 88/89/90 → cleanup (dead code, post-stable sweep, no commented code); keep 87/91 |
| Errors (78–82) | 5 | ~4 | 78/82 → exception + cleanup discipline; keep 79/80/81 |
| Dependencies (83–86) | 4 | ~3 | 83/84 → pin+lockfile + vuln audit; keep 85/86 |
| Docs/memory (92–97) | 6 | ~5 | 93/96 → persist decisions / ADRs; keep 92/94/95/97 |
| Hard rules + crew + working (4–10, 12–19, 98–100) | — | — | mostly distinct; **one move:** 15's sizing clause + 98 → one sharp rule (below) |

**The sizing rule (Eddie, 2026-06-13 — "another rule").** Consolidate the sprint-sizing
clause of 15 with 98 into one rule that states all three properties the current pair only
imply between them: *Chunk every task into **bite-size, parallel-capable** units, each
sized so the AI hits **≥90% quality first try**; anything with >10% first-try-failure risk
or that can't run independently of its siblings gets split further.* This is the law the
whole fleet rides on — it's why the tiers work (small chunks fit a small tier's budget) and
why the crew parallelizes. Merging 15+98 frees the slot it needs; **count stays 100.**

Net: ~30 merged → **~70 rules**, none loosened — room to *add* sharper rules (like the
sizing rule above) without growing the count. (The 2 further passes Eddie expects can
squeeze the crew + docs sections; this first pass takes the structural overlap.)

## Sprints (sized so the implementer nails each first try ≥90%)
- **S1 — Rule slices (doc-only, mechanical).** Author per-tier/per-seat slice files
  (`slices/t1-grunt.md`, `slices/t2-test.md`, `slices/t2-research.md`, `slices/t3-full.md`).
  *Acceptance:* each slice ≤ its tier's rule budget; a check script asserts the union of
  all slices == the canon (no rule dropped). **Unblocked — Claude's first sprint.**
- **S2 — Deep merge pass (F19).** Apply the Merge map to `RULES.md`. *Depends on Eddie's
  sign-off on the map.* *Acceptance:* count → ~70, no rule loosened, count-discipline
  note updated, slices regenerated from the new canon.
- **S3 — Router skeleton.** `route(task) -> tier` — rules-based v1 (intent/keyword →
  tier). *Acceptance:* a labeled set of sample tasks routes correctly ≥90%. **Unblocked.**
- **S4 — T1 bring-up.** 2B + grunt slice + tool-calling for `git`/`ls`/`cat`/`repo_search`.
  *Acceptance:* runs the 4 ops obeying the slice (secret-scan gate fires before push) on
  a fixture repo.
- **S5 — T2 bring-up.** 8B + test slice: writes & runs a pytest suite to green on a
  fixture; + research seat (Groq) for Linda.
- **S6 — T3 binding.** Cloud Opus++ for big-guns tasks; full consolidated rules.
- **S7 — Escalation + 90% harness.** T1→T2→T3 escalation on failure; a corpus of N
  representative tasks; measure % completed without reaching T3; target **≥90%**. Reuses
  the `experiments/rule-scaling` harness pattern.

## Tiers → hardware (the dependency)
- **T1 (≤2-3B):** Mac / iPhone / iPad — anywhere.
- **T2 (7-8B Q4):** the RTX 5080 16GB box, or a Mac.
- **T3 (16B → 1T++):** cloud Opus++ now (**Gladius down**); a 70B local when Gladius
  (`gx10`, 128GB) is reachable again.
- **QLoRA training:** ≤8B comfortable on 16GB; a 14B fine-tune wants Gladius.

## Open questions (Powell — I need these to lock the plan)
1. **The 90% corpus.** What task mix counts toward the metric? I can draft it from real
   session work (mostly git/file ops + tests + research, occasional architecture) — or
   you specify the mix. *Recommend: I draft, you adjust.*
2. **Jason's exact base.** ✅ RESOLVED — Qwen2.5-Coder-14B, fine-tune for the top 14 rules
   (1-per-B). Pulling + baselining now; tune is the proving run (target ≥90% @ 14).
3. **Slice-first or fine-tune-first** for T1/T2? *Recommend slice-first* — cheaper,
   faster to prove the 90% number; fine-tune as the boost once slices prove out.
4. **Router: rules-based or LLM-classifier?** *Recommend rules-based v1*, LLM later.

## First hand-off to Claude (once you sign off)
S1 (rule slices) and S3 (router skeleton) are both unblocked, mechanical, and
independently verifiable — exactly the shape that lands first-try. S2 (the merge pass)
waits on your sign-off of the Merge map above. I hold S6/S7 (escalation + the 90%
measurement) until the tiers exist.
