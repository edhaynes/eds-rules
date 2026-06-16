# STATE — eds-rules

*Living project summary. **Ingested at session start; regenerated after each
commit.** Hard cap **1024 words** (currently ~800). When over cap, prune detail to
ADRs / MEMORY / the notebook — STATE is a summary that points, never a log.*

Last updated: 2026-06-13. **Note 2026-06-16:** book is now **7 chapters**
(`book/ch01–07`) — ch06 "Operating an AI Fleet", and new ch07 "From a Hundred
Rules to an Axiom Core" integrates Guy's taxonomy ("Guy's scalpel": axiom core +
paged preference layers, cache hierarchy, Guy's test) + Appendix F. Adds no
rules; count stays 100. CHANGELOG 1.4.6. STATE below predates ch06/ch07 and is
due a fuller regen.

## What this is
"100 Rules for Writing My Software: The Red Hat Way" — an opinionated, capped-at-
100 rule set for AI coding agents, published as a repo (`RULES.md`, CC-BY-4.0)
**and** a book (`book/ch01–05`). Distilled from Eddie's ~47-year career; the
"Jason" persona is the architect of General Dynamics' TACLANE encryptor (~25 rules
are really Jason's). Repo: github.com/edhaynes/eds-rules.

## Current status
- Version ~1.4.x — **even-minor = stable cycle → confirm before push/deploy.**
- `RULES.md`: 100 rules. Two changesets pending book-sync: (1) 3-in/3-out swap
  (in: input-security #3, idempotency #47, latency-budget #76; out: LF, SOLID,
  dep-disclosure dup; commit f4b3ccd); (2) **STATE rule #92 inserted** (this
  process), structured-logging folded into #80 to free the slot.
- Book (5 chapters × 20, importance-ordered per PLAN_rule-weighting): **NOT yet
  synced to the 3-swap → see B12.**
- Teaser demo video live (8B Llama with-rules vs without). Persona-model training
  (`model/`) works as proof of concept.

## Active focus — the rule-quality study (`quality/`)
- Rubric (6 dims, pertinence-weighted; `quality/RUBRIC.md`); graded all 100
  (`grade_rules.py` → `grades.csv` + `rule-quality.svg/png`). Recalibrated to full
  0–10 range after Eddie caught central-tendency bias: mean 55, range 25.5–90,
  **33 rules below the 50 keep/cut bar.**
- Polish experiment (`experiments/polish-rounds/`): rubric-driven review tapers —
  above-bar finds exhausted by round 3; only ~5 quality new rules exist. So a
  50-floored doc is ~70–73 rules; "100" carries ~30 below-average rules.
- **Decision: keep 100 as the brand, flag don't cut.** Weak rules that earn slots
  on conviction/framework = "mulligan" rules, openly labeled YMMV (crew, Podman/
  UBI/OpenShift "hardcoded to Eddie"). Triage in `quality/sub-bar-triage.md`:
  ~20 REWRITE (consolidate up), ~13 MULLIGAN, ~0 discard.
- Lab notebook `quality/NOTEBOOK.md` (13 entries) — report through-line: a verbal
  thinker predicts LLM process-dynamics (3-round epochs) by introspecting his own
  refinement loop.

## Open threads / unfinished
- **B12 (top, in progress): sync the book** to both RULES.md changesets.
  Prepped + de-risked: plan (`PLAN_book-sync.md`), 4 essays drafted
  (`book-sync-drafts.md`, awaiting Eddie's `[ANECDOTE]` fills + voice), mapping
  frozen + **bijection-verified** (`book-sync-mapping.py`; chapters 21/19/19/21/20;
  retire SOLID/structured-logs/line-endings/say-what-you-install, insert
  input-sec/idempotency/latency/state). **Remaining = the application** (insert 4,
  fold 4, renumber ~95 headings + 5 cards + Appendix D + ~239 cross-refs) — must
  land in ONE consistent pass (global renumber; partial = broken). Until done,
  RULES.md↔book drift is the known bug.
- Eddie's latency/determinism+live-progress rule (grades 52.5, consolidates
  #50+#76) — available as an optional net-neutral swap.
- **STATE process:** rule #92 added; per-repo `STATE.md` live (1024-word cap,
  regen each commit); `~/projects/state.h` index (1–3 sentences/repo) being set
  up. Ship criterion (Eddie): ship when no new candidate cracks the top 20 — the
  STATE rule (67) may be the last in; next-best find (UTC, 58) is below the line.
- Book feature chapters open: security (F10), HA (F11), lifecycle/Day-2 (F12),
  capstone/Bard (F7). Plans: agent-assignments (87→95 bar), demo video (awaiting
  Eddie's recording; axis-B blocked on ANTHROPIC_API_KEY), persona-models
  (awaiting hardware/sign-off).

## Gotchas a fresh agent must know
- **Cap is sacred: exactly 100 rules.** A new rule enters only by consolidating/
  retiring another. "Exactly 20/chapter" is softer (flexed to 19–21).
- **Concurrent sessions push to this repo** (other agents commit `experiments/`,
  `demo/`). `git fetch`/check origin before assuming HEAD; stage only your own
  files (don't touch `experiments/rule-scaling/summary.tsv`).
- **Pre-commit eof-fixer** rewrites generated SVGs lacking a trailing newline and
  aborts the commit — generators must emit `\n` at EOF.
- Secret-scan (gitleaks) every commit; hooks installed.
- No matplotlib — graphs are hand-built SVG → PNG via headless Chrome.
- Personas: Jason (PM, default voice), Claudius (arch), Claude (backend), Claudina
  (frontend), Linda (research), Iris/Edith (editorial), Gladius (gx10 compute,
  often unreachable).

## Repo map
`book/` manuscript + build · `demo/` video (teaser live) · `model/` persona-model
training · `experiments/` rule-scaling, polish-rounds · `quality/` rubric/grades/
notebook/triage · `plans/` PLAN_*/HANDOFF_* · `dist/` · `test/`
