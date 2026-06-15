Status: Implemented, 2026-06-15 — 6 chapters (22/18/21/14/17/8=100), Appendix D remapped, EPUB+PDF build clean

# PLAN — Re-sync the book to the current `RULES.md`

The canon (`RULES.md`) was consolidated 2026-06-14 (commits `f4b3ccd`, `c7c66fc`,
`7b7a5fa`): overlaps merged, ~9 new non-fleet rules added, and a new
*Operating an AI fleet* chapter (rules 93–100). Count held at 100. The book
(`book/ch01–ch05.md`) still teaches the pre-consolidation set. OUTLINE.md is
explicit: "Rule text drift between book and repo is a bug." This plan re-syncs.

**Decision (Eddie, 2026-06-15):** add a 6th book chapter for the fleet rules;
full content sync now, executed as parallel per-chapter subagents.

## Voice / format (every chapter, every rule)

- Heading `## Rule N: Title`, then a **bold one-line statement** that matches the
  canon's wording, then a *why* — a scar from real experience, 120–320 words —
  and an optional small table/diagram + italic caption "where one earns its place."
- Each chapter ends with `### Chapter N card`: a numbered checklist, one terse
  line per rule (`N. **Title** — gist.`).
- Match the surrounding prose: no flattery, scar-driven, plain. New rules read
  like neighbours, not like a different author.
- Fix every internal cross-reference (`Rule NN`, `Chapter N`, "rule nn") to the
  NEW numbering. Update the chapter opener if it cites rule ranges/counts.

## New global numbering (book order → canon #)

The book keeps its pedagogical order; only content the canon merged/added moves.

### Ch.1 — First Principles → rules 1–22  (file `book/ch01.md`)
| New | Title | Canon | Action |
|--|--|--|--|
| 1 | No scan, no ship | 1 | keep, renumber |
| 2 | Never hardcode a secret | 2 | keep |
| 3 | Distrust every external input | 3 | **NEW** |
| 4 | Destruction requires a human | 4 | keep (was Rule 3) |
| 5 | No recoverable history, no autonomy | 5 | keep (was 4) |
| 6 | Push early and push always | 6 | keep (was 5) |
| 7 | Green before commit, healthy before handover | 7 | keep (was 6) |
| 8 | One purpose per commit | 8 | reword (was 7): add "a size or mechanical refactor is its own commit so the diff stays reviewable" |
| 9 | Fail fast | 9 | keep (was 8) |
| 10 | No anonymous dependencies | 10 | reword (was 9): name, purpose, license, **maintenance status**, and platform support |
| 11 | Assume no path, OS, or shell — and no head | 11 | keep (was 10) |
| 12 | Least privilege by default | 12 | **NEW** |
| 13 | The Powell rule — 90% and decide | 13 | keep (was 11) |
| 14 | Five roles, one human, zero hardcoded models | 14 | keep (was 12) |
| 15 | Plan first | 90 | reword (was Rule 13 "Plan first, size for 90%"): **drop** the sprint-sizing detail — that now lives in Ch.6 Rule 93. Keep: state the approach and files before editing; never silently change scope. |
| 16 | Claudius plans, or it's rework | 15 | keep (was 14) |
| 17 | Jason holds the through-line | 16 | keep (was 15) |
| 18 | Claude searches before he builds | 17 | keep (was 16) |
| 19 | Claudina ships everywhere | 18 | keep (was 17) |
| 20 | Linda searches wide | 19 | keep (was 18) |
| 21 | No flattery | 91 | keep (was 19) |
| 22 | Go local | 20 | keep (was 20) |

**NEW Rule 3 — canon text:** "Distrust every external input. Validate and
constrain it at the boundary; parameterize queries and commands, resolve and
confine paths, never interpolate untrusted data into SQL, a shell, HTML, or a
deserializer. Secret hygiene guards what leaks out — this guards what gets in."
Scar: an injection / path-traversal / unsafe-deserialization incident.

**NEW Rule 12 — canon text:** "Least privilege by default. Every credential,
token, service account, and role gets the narrowest scope that works — no
wildcard permissions, no shared admin keys; expire and rotate by default, and
grant more only when something actually fails for lack of it." Scar: a
wildcard/admin token blast radius.

### Ch.2 — Design → rules 23–40  (file `book/ch02.md`)
Order = current minus two merged rules. (was Rule → New)
| New | Title | Canon | Action |
|--|--|--|--|
| 23 | If it can change, it's config | 21 | reword (was 21): **absorb** old Rule 34 "No magic numbers" — "…and no magic numbers: named constants or config entries only." |
| 24 | Architecture beats language | 28 | keep (was 22) |
| 25 | Every vendor axis gets an interface | 29 | keep (was 23) |
| 26 | Search before you build | 30 | keep (was 24) |
| 27 | Collaborators come through the front door | 31 | keep (was 25) |
| 28 | No silent fallbacks | 22 | keep (was 26) |
| 29 | Validate at startup, name the key | 23 | keep (was 27) |
| 30 | One config layer, one precedence order | 24 | keep (was 28) |
| 31 | Objects with one job each | 32 | reword (was 29): **absorb** old Rule 38 "SOLID where it earns its keep" — "…apply SOLID, especially SRP and Dependency Inversion, where it earns its keep." |
| 32 | Storage goes through the adapter | 43 | keep (was 30) |
| 33 | On-prem and cloud are config values | 44 | keep (was 31) |
| 34 | "Use X locally" means default, not destiny | 25 | keep (was 32) |
| 35 | Zero-setup defaults | 26 | keep (was 33) |
| 36 | The file-size gauge | 34 | reword (was 36): **absorb** function-size (≤50 lines/≤5 params) and nesting (extract past ~3 levels) — the content of old Ch.4 Rules 79 & 80, which are deleted there. |
| 37 | No god classes | 35 | keep (was 37) |
| 38 | One non-trivial class per file | 33 | keep (was 39) |
| 39 | Ship the `.env.example` | 27 | keep (was 35) |
| 40 | Refactors are mechanical commits | 36 | keep (was 40) |
DELETE standalone old Rule 34 (magic numbers) and old Rule 38 (SOLID) — folded above.

### Ch.3 — Build → rules 41–61  (file `book/ch03.md`)
| New | Title | Canon | Action |
|--|--|--|--|
| 41 | Gates never disabled by default | 45 | keep (was 41) |
| 42 | Catch specific, never swallow | 71 | reword (was 42): **absorb** old Rule 56 "Cleanup is structural" — "Resource cleanup uses context managers / defer / using." |
| 43 | Pin it and lock it | 77 | reword (was 43): **absorb** old Rule 44 audit — "…run a vulnerability audit periodically and on every new dependency." |
| 44 | Health endpoints and graceful SIGTERM | 47 | keep (was 45) |
| 45 | Container-friendly by default — Podman, UBI, OpenShift | 48 | **reword** (was 46): rootless, **SELinux enforcing**, smallest capability set; no `--privileged`, no unjustified caps, non-root user, read-only root fs where feasible; "least privilege beats convenience." Keep the "write your own rules" invitation (soften the old "tough luck" tone per canon). |
| 46 | Make it idempotent | 46 | **NEW** |
| 47 | Loud in dev, graceful in prod, diagnosable always | 72 | keep (was 47) |
| 48 | Three platforms, two in CI | 37 | keep (was 48) |
| 49 | A logger, never print | 73 | reword (was 49): **absorb** old Rule 59 structured logs — "…structured (JSON) once it outgrows a script." |
| 50 | AI errors surface; agents don't invent tools | 74 | keep (was 50) |
| 51 | Path libraries, never string glue | 38 | reword (was 51): **absorb** old Rule 60 LF endings — "…and enforce LF via `.gitattributes`." |
| 52 | Stdlib plus one good dependency | 78 | keep (was 52) |
| 53 | No hardcoded temp, home, or drive letters | 39 | keep (was 53) |
| 54 | Both architectures, flagged exceptions | 40 | keep (was 54) |
| 55 | No shell-isms — orchestrate in Python or Node | 41 | keep (was 55) |
| 56 | Time is UTC until it's displayed | 42 | **NEW** |
| 57 | Project-local virtualenvs, always | 79 | keep (was 57) |
| 58 | Show progress; cached by default, expensive by exception | 49 | keep (was 58) |
| 59 | Every remote call has a timeout and a way out | 75 | **NEW** |
| 60 | One request, one trace ID | 76 | **NEW** |
| 61 | Migrations go down as well as up | 50 | **NEW** |
DELETE old Rules 44, 56, 59, 60 (folded above).
**NEW canon texts:** R46 (46), R56=UTC (42), R59=timeout/retry/circuit-breaker (75),
R60=correlation/trace ID (76), R61=reversible+idempotent migrations (50). Use the
exact canon wording for the bold statement; author the scars.

### Ch.4 — Protect and Prove → rules 62–75  (file `book/ch04.md`)
| New | Title | Canon | Action |
|--|--|--|--|
| 62 | Hooks before the first commit | 51 | reword (was 61): **absorb** old Rule 72 (pre-push rescan+tests) and old Rule 75 (`.gitignore` day one) — canon 51 now states both. |
| 63 | Rotate first, clean history second | 52 | keep (was 62) |
| 64 | Never copy a secret anywhere | 53 | keep (was 63) |
| 65 | Scan every boundary before you cross it | 54 | reword (was 65 "Scan the whole artifact"): **absorb** old Rules 66 (push range), 70 (harmless config), 71 (files you didn't author) — canon 54 is the single scan-everywhere rule. |
| 66 | You get what you inspect — and it gets a grade | 62 | keep (was 64) |
| 67 | No test, no ship | 63 | keep (was 67) |
| 68 | Contract first, code second | 64 | keep (was 68) |
| 69 | 100% — lines and branches | 65 | keep (was 69) |
| 70 | Correctness over speed | 66 | keep (was 73) |
| 71 | Coverage never goes down | 67 | keep (was 74) |
| 72 | Full regression, every feature, with the numbers | 68 | keep (was 77) |
| 73 | Set a latency budget and gate it | 69 | **NEW** |
| 74 | No network in unit tests | 70 | keep (was 78) |
| 75 | Fix the hook that missed it | 55 | keep (was 76) |
DELETE old Rules 66, 70, 71, 72, 75 (folded into 62/65); old Rules 79 & 80
(function size, nesting) move to Ch.2 Rule 36 — delete here.
**NEW Rule 73 — canon text (69):** "Declare a latency and throughput budget,
then gate regressions against it the way you gate coverage. Determinism and
latency are features: set the ceiling explicitly and fail the build when a
change blows past it — a silent slowdown is a defect that ships." Scar: a silent
regression that shipped.

### Ch.5 — Ship and Remember → rules 76–92  (file `book/ch05.md`)
| New | Title | Canon | Action |
|--|--|--|--|
| 76 | Tags are carved in stone | 56 | reword (was 81): **absorb** old Rule 86 (fetch before tag) and old Rule 93 (push tags by name) — canon 56 states all three. |
| 77 | Versions only move forward | 57 | keep (was 82) |
| 78 | Persist decisions in the same commit | 86 | reword (was 83): **absorb** old Rule 91 (ADRs immutable) — canon 86 states both. |
| 79 | One version, one home | 58 | keep (was 84) |
| 80 | File it the moment you see it | 87 | keep (was 85) |
| 81 | Every build wears a serial number | 59 | keep (was 87) |
| 82 | Verbatim errors, diffs not prose, assumptions out loud | 92 | keep (was 88) |
| 83 | The changelog rides in the bump commit | 60 | keep (was 89) |
| 84 | Plans tell you their own status | 88 | keep (was 90) |
| 85 | The version answers the door | 61 | keep (was 92) |
| 86 | Lint and format every commit | 80 | keep (was 94) |
| 87 | Sweep the dead code | 81 | keep (was 95) |
| 88 | After the release, take out the trash | 82 | keep (was 96) |
| 89 | Regenerate the README | 89 | keep (was 97) |
| 90 | No commented-out code | 83 | keep (was 98) |
| 91 | No orphan TODOs | 84 | keep (was 99) |
| 92 | A living state file so a cold agent can start | 85 | **NEW** |
DELETE old Rules 86 (fetch→folded into 76), 91 (ADR→folded into 78), 93
(push-tags→folded into 76), 100 (dependency disclosure — now redundant with
Ch.1 Rule 10, which states maintenance status; remove the standalone).
**NEW Rule 92 — canon text (85):** "Maintain a living state file so a memoryless
agent can start cold: a per-repo `STATE.md` (≤1024 words) ingested at session
start and regenerated at the end of every commit, plus a one-line-per-repo index
at the projects root. It points to the ADRs and trackers — never a log; when it
overflows, prune detail outward." Scar: a memoryless agent restarting blind.

### Ch.6 — Operating an AI Fleet → rules 93–100  (NEW file `book/ch06.md`)
All eight are NEW prose. Canon text is authoritative for the bold statement.
| New | Canon | Statement source |
|--|--|--|
| 93 | 93 | Chunk into bite-size parallel-capable units, each sized for ≥90% first-try; split anything >10% fail-risk or non-independent. |
| 94 | 94 | The sizing law: ~1 rule per billion params at the 90% bar (2B→~2, 8B→~8, 14B→~14). |
| 95 | 95 | Slice the rules to the seat — a *view* of the canon, not the whole book. |
| 96 | 96 | Context ceiling by tier: little model ≤~8k, frontier safe to ~128k. |
| 97 | 97 | Good enough at the model, 90% at the system — quality lives in the pipeline. |
| 98 | 98 | Match the work to the model — smallest tier that clears it, escalate the residual. |
| 99 | 99 | Verify, then escalate — gate cheap output, bounce failures up a tier. |
| 100 | 100 | Externalize the reflex — the senior's tacit instinct becomes an explicit rule/test/gate. |
Ch.6 needs: `# Chapter 6 — Operating an AI Fleet`, a one-page opener (the
through-line: the rules so far make ONE agent good; this chapter makes a *fleet*
of cheap agents good as a system — the experiments in this repo are the receipts),
the 8 rules with scars, and a `### Chapter 6 card`. A black-and-white diagram of
the verify-then-escalate pipeline (cheap tier → verify gate → escalate residual)
earns its place. No chapter-divider plate required (build skips it if
`art/chapter-6.svg` is absent).

## Coordinator (Jason) owns these — not the subagents
- `book/00-front-matter.md`: "How to read" chapter list + ranges (1–22, 23–40,
  41–61, 62–75, 76–92, 93–100), the "six chapters" count, and "Start with these
  ten" rule numbers (re-map: scan=1, never-hardcode=2, destruction=4, push=6,
  green=7, one-purpose=8, fail-fast=9, Powell=13, config=23, hooks=62).
- `book/99-back-matter.md`: **Appendix D** fully rebuilt from subagent-reported
  (new#→canon#) lists. Keep the Companion-media section already added.
- `book/build.py`: add `ch06.md` to `SOURCES`.
- `book/OUTLINE.md`: note the 6-chapter structure + this re-sync.
- Rebuild EPUB+PDF, verify, open PDF.

## Done when
Book teaches exactly the current 100 canon rules, 6 chapters, Appendix D correct,
EPUB+PDF build clean, no stale rule numbers in cross-references.
