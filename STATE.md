# STATE — eds-rules

*Living project summary. **Ingested at session start; regenerated after each
commit.** Hard cap **1024 words** (currently ~750). When over cap, prune detail to
ADRs / MEMORY / the notebook — STATE is a summary that points, never a log.*

Last updated: 2026-06-23.

## What this is
"100 Rules for Writing My Software: The Red Hat Way" — an opinionated, capped-at-
100 rule set for AI coding agents, published as a repo (`RULES.md`, CC-BY-4.0)
**and** a book (`book/ch01–07` → EPUB + 7"×10" print PDF). Distilled from Eddie's
~47-year career; the "Jason" persona is the architect of General Dynamics'
TACLANE encryptor (~25 rules are really Jason's). Repo:
github.com/edhaynes/eds-rules.

## Current status
- Version **1.4.6** (CHANGELOG). **Even-minor = stable cycle → confirm before
  push/deploy.** No tag since v1.4.1; tags are immutable, promotion is manual.
- `RULES.md`: **100 rules** (cap is sacred). The book tracks it pedagogically;
  Appendix D holds the book↔RULES.md mapping. The historical book-sync bug (B12)
  is no longer the active blocker — the book was re-synced to consolidated
  `RULES.md` (2026-06-15, Powell rule → Rule 1) and rebuilt at 1.4.6.
- **Book = 7 chapters summing to 100, plus a no-rules capstone.** Ch1 First
  Principles · Ch2 Design · Ch3 Build · Ch4 Protect & Prove · Ch5 Ship & Remember
  · Ch6 Operating an AI Fleet (the receipts chapter — sizing law, slicing,
  verify-then-escalate) · **Ch7 From a Hundred Rules to an Axiom Core** (adds no
  rules; reframes the hundred as a cache hierarchy). Built PDF is **165 pp**,
  tracked at `book/eds-rules-book-print.pdf`; EPUB is gitignored in `dist/`.
- Build: `book/build.py [epub|pdf|all]` needs `mmdc`, `pandoc`, `typst` on PATH;
  Mermaid → B&W PNG, pandoc → EPUB and (patched typst) → custom-trim PDF.
- **Amazon KDP prep done (2026-06-23, Eddie):** Kindle + paperback. Copyright page
  added to front matter; `book/cover.py` generates ebook (1600×2560) + paperback
  wrap (spine from page count, barcode keep-out) — covers approved by Eddie;
  `docs/KDP_LISTING.md` is the full listing kit (categories, 7 keywords,
  description, pricing, upload checklist). Title kept "The Red Hat Way" (legal
  cleared); AI-agent discoverability rides in KDP metadata. Plan:
  `plans/PLAN_amazon_kdp.md`. Remaining: epubcheck, KDP-issued ISBN → copyright
  page, imprint name, publish.
- Teaser demo video live (8B Llama with-rules vs without). Persona-model training
  (`model/`) works as proof of concept.

## Active focus — Guy's taxonomy (`taxonomy/`)
- **"Guy's scalpel"** (Guy Turgeon, ep93 interview): drop the flat-100 framing in
  favor of a **small immutable axiom core (~24) + composable preference layers**
  (personal/architect, project, employer), treating rules as a **cache hierarchy**
  — per-seat resident working set (~1 rule/B params), team-resident union = the
  canon, paged tail injected by trigger. `rules.yaml` = source of truth;
  `compose.py` generates per-crew slices/summaries; `crew-*.yaml` define seats.
- **Guy's test**: smallest crew whose summed budget covers the required-resident
  set. 24-axiom core needs ≈24B; a frontier-free 8B+14B pair (21B) is short by 3
  → add a frontier seat or trim core to ≤21. Crew size = capacity dial.
- **Merged to main.** Book half is **done** (Ch7 + Appendix F + glossary, 1.4.6).
  Remaining (plan `PLAN_rules-taxonomy.md`, status Partial): full old-100→layers
  map; frontier-free crew demo; **RULES.md-side sync + a fuller STATE pass**.

## The rule-quality study (`quality/`)
- Rubric (6 dims, pertinence-weighted; `quality/RUBRIC.md`); graded all 100
  (`grade_rules.py` → `grades.csv` + `rule-quality.svg/png`). Recalibrated to full
  0–10 range: mean 55, range 25.5–90, **33 rules below the 50 bar.** The taxonomy
  reframe explains the floor: role/project rules score low because they're
  *mis-scoped* (a preference graded as a universal axiom always loses on
  generality) — the fix is layers, not cuts.
- Polish experiment (`experiments/polish-rounds/`): rubric-driven review tapers;
  above-bar finds exhausted by round 3 (~5 quality new rules exist).
- Lab notebook `quality/NOTEBOOK.md` — a verbal thinker predicts LLM
  process-dynamics (3-round epochs) by introspecting his own refinement loop.

## Open threads / unfinished
- **Taxonomy RULES.md-side sync** (top): the layered model is in the book and
  `taxonomy/`; `RULES.md` itself is still the flat 100. Decide whether/how the
  canon adopts the axiom-core/layer split, and finish STATE regen.
- Eddie's latency/determinism+live-progress rule (grades 52.5) — optional
  net-neutral swap (consolidates #50+#76), not yet applied.
- Book feature chapters still open: security, HA, lifecycle/Day-2, capstone/Bard.
  Plans: demo video (axis-B blocked on `ANTHROPIC_API_KEY`); persona-models
  (awaiting hardware/sign-off).

## Gotchas a fresh agent must know
- **Cap is sacred: exactly 100 rules.** A new rule enters only by consolidating/
  retiring another. Ch7 adds *no* rules by design.
- **Concurrent sessions push to this repo** (other agents commit `experiments/`,
  `demo/`, `tools/`). `git fetch`/check origin before assuming HEAD; **stage only
  your own files** — don't `git add -A`.
- **Pre-commit hooks**: gitleaks/detect-secrets + private-key + large-file +
  eof-fixer (rewrites SVGs lacking trailing `\n` and aborts — generators must emit
  `\n` at EOF) + a "keep `rules/RULES.md` in sync with canonical `RULES.md`" hook.
- No matplotlib — graphs are hand-built SVG → PNG via headless Chrome.
- Book voice: `book/STYLE.md` (Eddie's fiction register; American spelling;
  re-voice delivery, never content). Match ch06 structure for new chapters.
- Personas: Jason (PM, default voice), Claudius (arch), Claude (backend), Claudina
  (frontend), Linda (research), Iris/Edith (editorial), Gladius (gx10 compute,
  often unreachable).

## Repo map
`book/` manuscript + `build.py` (PDF tracked, EPUB in gitignored `dist/`) ·
`taxonomy/` Guy's-scalpel layered ruleset + composer · `demo/` video + podcast ·
`model/` persona-model training + sandbox · `experiments/` rule-scaling,
polish-rounds, coding-bench · `quality/` rubric/grades/notebook/triage ·
`plans/` PLAN_*/HANDOFF_* · `tools/` · `test/`
