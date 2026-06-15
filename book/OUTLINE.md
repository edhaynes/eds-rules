# Book Outline — *100 Rules for Writing My Software: The Red Hat Way*

Status: In Progress — draft re-synced to consolidated RULES.md 2026-06-15 (6 chapters + front/back matter); build pipeline live (`book/build.py` → EPUB + 7"×10" PDF); remaining: author read-through of the re-sync, rubric cold grade (RUBRIC.md), trademark answer before cover is final

> **Restructured 2026-06-11 (Eddie):** 5 chapters × 20 rules (was 10 × 10).
> Chapters build on one another, most fundamental first; each opens with a
> synopsis of the fundamentals it stands on. The chapter specs below the
> Product table describe the original 10-chapter cut and are retained for the
> rule-grouping rationale; the live structure is the 5-chapter arc:
>
> 1. **First Principles** (book rules 1–22) — hard rules + the crew → `ch01.md`
> 2. **Design** (23–40) — configuration + architecture → `ch02.md`
> 3. **Build** (41–61) — cross-platform & deployment + errors/observability/dependencies → `ch03.md`
> 4. **Protect and Prove** (62–75) — secret hygiene + testing & the quality bar → `ch04.md`
> 5. **Ship and Remember** (76–92) — versioning & release + hygiene/memory/process → `ch05.md`
> 6. **Operating an AI Fleet** (93–100) — making cheap models good as a system → `ch06.md`
>
> **Re-synced 2026-06-15** to the consolidated `RULES.md` (overlaps merged, ~9
> new non-fleet rules added, new fleet chapter): the book moved from 5×20 to
> **6 chapters summing to 100** (22/18/21/14/17/8). Per-chapter rule counts are
> no longer uniform; see Appendix D for the book↔RULES.md mapping. Spec:
> `plans/PLAN_book-resync.md`.
>
> Front matter: `00-front-matter.md` (title/disclaimer, foreword, how to read,
> meet the crew). Back matter: `99-back-matter.md` (appendices A–E incl. the
> book↔RULES.md mapping, glossary).

## Product

| Attribute | Value |
|---|---|
| Title | **100 Rules for Writing My Software** |
| Subtitle | **The Red Hat Way** |
| Kindle price | **$9.99** (raised from $4.99, 2026-06-12) |
| Softcover price | **$19.99** (raised from $9.99, 2026-06-12 — priced against the technical-nonfiction comp set) |
| Interior | **Black and white** (KDP standard B&W, cream or white paper) |
| Trim | **7" × 10"** (raised from 6"×9", 2026-06-12 — technical-book comp set; KDP B&W print cost is per page, so the bigger trim prints *cheaper*: ~125 pp vs 166) |
| Structure | **5 chapters × 20 rules = 100 rules** (restructured from 10×10) |
| Art | Lots of diagrams — 2–4 per chapter, all designed for B&W |
| License note | Book text © author; the underlying rules repo stays CC-BY-4.0 |

**Disclaimer (front matter, verbatim intent):** These rules are called "the Red
Hat way" but are **not sanctioned or verified by Red Hat**. The author is a Red
Hat architect; this book is personal work, unaffiliated with and not endorsed by
Red Hat. Everything is provided as is, with no promises. Your mileage may vary —
do your own research.

**B&W diagram constraint:** no color-coded legends. Distinguish elements with
line styles (solid/dashed/dotted), shapes, hatching, and labels. Mermaid sources
live in `book/diagrams/`, rendered to grayscale SVG/PNG at build time.

## Front matter

1. Title page + disclaimer (above)
2. Foreword — *why these rules exist*: years of actual development experience,
   plus the realization that AI changed the economics: messy things like merges
   are now done extremely well by machines, so push early and always; sprints
   can be tailored so the AI nails them first go 90% of the time.
3. How to read this book — rules are numbered 1–100 straight through; each rule
   gets a statement, the *why* (usually a scar), and a diagram where one earns
   its place. Steal what works; fork what doesn't.
4. Meet the crew — one-page introduction to the five personas + Eddie
   (full treatment in Chapter 2).

## The ten chapters

Each chapter: a one-page opener (the war story or principle that motivates it),
ten rules, a closing one-page "chapter card" (the ten rules restated as a
checklist — also doubles as a printable poster).

Rule numbers below reference `RULES.md`; the book renumbers them 1–100 in
chapter order. A mapping table goes in Appendix D.

### Ch. 1 — The Ten Commandments (hard rules)
RULES.md 1–10. The never-violates: secret scans, no hardcoded secrets, no
destruction without confirmation, push early and always, green before commit,
one purpose per commit, fail fast, autonomy bounded by version control.
**Diagrams:** trust-boundary map (what counts as "crossing" — remote, registry,
cluster, host); the commit→push→deploy gate flowchart; "uncommitted work is a
liability" timeline.

### Ch. 2 — The Crew (personas, routing, decisions)
RULES.md 11–18, 98, 100. Jason, Linda, Claude, Claudina, Claudius, Eddie;
harness-portable bindings; go-local; the Powell rule; sprint sizing for 90%
first-try success; no flattery.
**Diagrams:** org chart; Powell-rule decision tree (certainty → act/ask);
parallel sprint lanes (independent chunks across personas); model-binding
matrix (Claude stack / open stack / local).

### Ch. 3 — Configuration Over Hardcoding
RULES.md 19–26, 45, 46. One config layer, .env.example, validate at startup,
no silent fallbacks, no magic numbers, on-prem↔cloud by config only, storage
behind an adapter.
**Diagrams:** config precedence stack (env → .env → file → flags); "go local"
rebinding; the storage-adapter seam.

### Ch. 4 — Architecture
RULES.md 27–34, 37, 38. OO with clear responsibilities, swappable interfaces,
dependency injection, SOLID where it earns its keep, research before building,
file-size ceilings, no god classes, mechanical refactor commits.
**Diagrams:** swappable-backend interface (one contract, N providers);
DI vs. globals contrast; the 500/800/1000-line file gauge.

### Ch. 5 — Cross-Platform and Deployment
RULES.md 39–44, 47–50. macOS/Linux/Windows, arm64+x86_64, path libraries,
no shell-isms, LF endings; Podman + RHEL UBI + OpenShift (the chapter that
earns the subtitle — and the "write your own rules" invitation); health
endpoints; pre-deploy gates never disabled.
**Diagrams:** platform × arch support matrix; container lifecycle (build →
gate → deploy → SIGTERM); rootless-daemonless vs. root-daemon contrast.

### Ch. 6 — Secret Hygiene
RULES.md 51–60. Hooks before first commit, scan everything you didn't author,
scan the push range not the tip, scan the full deploy artifact, rotate first
clean later, never copy a discovered secret.
**Diagrams:** the leak lifecycle (add → commit → push → burned forever, with
the ~90-day object-retention tail); rotation-protocol sequence diagram;
scan-gate placement map (add / commit / push / deploy).

### Ch. 7 — Versioning and Release
RULES.md 61–68, 92, 96. SemVer from one canonical place, immutable tags,
fetch-before-tag, unique monotonic build numbers, version visible everywhere,
changelog in the bump commit, post-release cleanup sweep, plan status hygiene.
**Diagrams:** version flow (commit → bump → tag → changelog); tag-immutability
timeline (why moved tags break pins); build-number generation
(`git rev-list --count HEAD`).

### Ch. 8 — Testing and the Quality Bar
RULES.md 69–76, 35, 36. Contract first, failing-test first, 100% line *and*
branch coverage, correctness over speed, no network in unit tests, you get
what you inspect — and the rubric: 90% solid A− working bar, polish to 95%,
publish at 95%+. Small functions and shallow nesting live here because a
complexity budget is what makes 100% branch coverage tractable.
**Diagrams:** contract-first TDD loop; coverage funnel (line → branch →
asserted); the rubric gauge (90 → 95 → publish); nesting-depth ladder.

### Ch. 9 — Errors, Observability, Dependencies
RULES.md 77–86. No swallowed exceptions, logger never print, structured logs,
loud in dev graceful in prod, context managers, AI errors surfaced to users;
pinned versions, lockfiles, stdlib-plus-one, vuln audits, local virtualenvs.
**Diagrams:** error-propagation ladder (dev vs. prod paths); logging pipeline;
dependency vetting funnel (need → candidates → license/ARM/maintenance → pin).

### Ch. 10 — Hygiene, Memory, Process
RULES.md 87–91, 93–95, 97, 99. Dependency disclosure, dead-code passes, no
commented-out code, no orphan TODOs, README regenerated not patched, ADRs
immutable, every bug and feature filed on observation, decisions persisted in
the same commit, errors quoted verbatim, diffs not prose.
**Diagrams:** the dead-code sweep cycle; decision flow (chat → ADR/memory →
same commit); bug/feature entry state machine (Open → In Progress → Completed).

## Back matter

- **Appendix A** — drop-in pre-commit config (gitleaks + hygiene hooks)
- **Appendix B** — minimum `.gitignore` for secrets
- **Appendix C** — adopting the rules per harness (Claude Code / OpenCode /
  others; CLAUDE.md vs AGENTS.md; the symlink trick)
- **Appendix D** — RULES.md ↔ book-chapter rule-number mapping table
- **Glossary** — the crew, the Powell rule, the quality bar, trust boundary
- **Index of rules** — one line each, by book number

## Production notes

- Manuscript in Markdown, one file per chapter (`book/ch01.md` …
  `book/ch10.md`), built to EPUB (Kindle) and print PDF (KDP) with pandoc.
- Diagrams: Mermaid → SVG → grayscale; verify every diagram reads correctly
  printed B&W at 6"×9" before accepting it.
- Word-count target: 25–35k (250–350 words/rule average keeps the softcover in
  the cheap-to-print range at $9.99).
- The repo's `RULES.md` stays the canonical short form; the book elaborates,
  it never contradicts. Rule text drift between book and repo is a bug.
