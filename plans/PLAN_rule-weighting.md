Status: Implemented, 2026-06-12

> **Amendment (2026-06-12, Eddie's sign-off via Jason):** Chapter 1 takes the
> middle path on the contested top slot — "No scan, no ship" keeps position 1
> (the opener's irreversibility argument stands), and the Powell rule leads
> the who-decides half at position 11. Hard lines fill 1–10 and crew rules
> 12–20 in the proposed relative order. The frozen mapping incorporating this
> is `plans/F5-mapping.md` (bijection verified). All other chapters execute
> as tabled below.

# PLAN — Rule weighting: order each chapter by importance

Eddie's ruling (2026-06-12): within each chapter, rules are ordered by
importance, most important first. Two anchors named explicitly: the Powell
rule goes **first** in its chapter; the quality-rubric rule ranks **high** in
its chapter. This plan proposes the full ordering for sign-off and specifies
the mechanical renumber that follows.

## What reordering means mechanically

The book numbers its rules 1–100 straight through, twenty per chapter. A
within-chapter reorder therefore changes the book number of nearly every
rule while leaving the chapter ranges intact (Ch 1 = 1–20, Ch 2 = 21–40,
Ch 3 = 41–60, Ch 4 = 61–80, Ch 5 = 81–100). The blast radius:

- **`book/ch01.md` … `ch05.md`** — `## Rule N:` sections physically reordered
  and renumbered; each chapter card (the closing 20-bullet checklist) reordered
  to match.
- **`RULES.md`** — the canonical short form is reordered to match the book's
  new relative order (outline rule: text drift between book and repo is a bug;
  the same holds for order once order carries meaning).
- **Appendix D** (`book/99-back-matter.md`) — the book ↔ `RULES.md` mapping
  table regenerated; the index of rules re-sorted.
- **Cross-references** — prose references ("Rule 17", "Rules 1–10",
  "rules 41 through 46") and Mermaid diagram labels (the Ch 4 scan-gate map
  names Rules 61, 62, 64, 65, 66, 67, 69 in edge labels) must all be swept:
  `grep -nE '\b[Rr]ules? [0-9]'` across `book/*.md` and `RULES.md`.
- **Chapter-opener "movement" prose** — Ch 3's opener narrates contiguous
  topical runs ("rules 41 through 46 is portability"). Importance ordering
  destroys topical contiguity, so those passages need rewriting, not just
  renumbering. Flagged per file below.

Numbers in the tables below are **current** book numbers; after execution,
the proposed position column becomes the new number (plus the chapter base).

## Ranking criteria

1. **Irreversibility** — rules preventing failures that cannot be undone
   (leaked secret, destroyed data, mutated tag, lost decision) rank highest.
2. **Fire rate** — rules exercised many times a day outrank rules exercised
   once a release.
3. **Load-bearing** — rules that other rules' machinery depends on rank above
   rules that merely refine.

Tiers: **Critical** (violation is catastrophic or the rule anchors the
chapter), **High** (daily discipline with real failure cost), **Medium**
(important, recoverable), **Supporting** (hygiene and refinement).

---

## Chapter 1 — First Principles (book 1–20)

Eddie's anchor: the Powell rule leads. It is the decision protocol every
other rule is applied *through* — the crew's operating system. The
irreversible-failure hard rules follow, then the structural hard rules, then
the crew, ordered by how much of the workflow each role's rule carries.

| Pos | Cur # | Rule title | Tier | Rationale |
|----:|------:|---|---|---|
| 1 | 17 | The Powell rule — 90% and decide | Critical | Eddie's anchor; the decision protocol every other rule runs under |
| 2 | 1 | No scan, no ship | Critical | Guards the one mistake typing harder can't undo |
| 3 | 2 | Never hardcode a secret | Critical | Keeps contraband from ever approaching the gate |
| 4 | 3 | Destruction requires a human | Critical | Dropped table / deleted file is irreversible without a human check |
| 5 | 10 | No recoverable history, no autonomy | Critical | The safety net that makes every other agent action reversible |
| 6 | 6 | Push early and push always | Critical | Unpushed work is unrecoverable work; the remote is the backup |
| 7 | 7 | Green before commit, healthy before handover | High | Fires on every commit; broken-by-default state poisons everything downstream |
| 8 | 8 | One purpose per commit | High | Fires on every commit; reviewability and revertability depend on it |
| 9 | 9 | Fail fast | High | Silent degradation costs more than any crash; shapes all error posture |
| 10 | 4 | No anonymous dependencies | High | Each dependency is adopted risk; the gate fires before the damage |
| 11 | 5 | Assume no path, no OS, no shell | Medium | Recoverable, but every baked assumption is a deferred bill (Ch 3 expands) |
| 12 | 11 | Five roles, one human, zero hardcoded models | Medium | Foundation of the crew half; rulings-are-final is the governance keystone |
| 13 | 19 | Plan first, size for 90% | Medium | All sprint work flows through this sizing discipline |
| 14 | 16 | Claudius plans, or it's rework | Medium | Wrong architecture is the costliest crew failure |
| 15 | 12 | Jason holds the through-line | Medium | Scope containment; the coordination layer the juniors hang off |
| 16 | 14 | Claude searches before he builds | Supporting | Original code as last resort — large waste averted, recoverable |
| 17 | 15 | Claudina ships everywhere | Supporting | Cross-platform from day one; enforced again by Ch 3 |
| 18 | 13 | Linda searches wide | Supporting | Breadth-first research profile; informs, doesn't decide |
| 19 | 20 | No flattery | Supporting | Fires every message, but failure is recoverable noise |
| 20 | 18 | Go local | Supporting | A capability that fires rarely; depends on 11's binding clause |

## Chapter 2 — Design (book 21–40)

Architecture decisions are the least reversible in this chapter, but the
config workhorse fires hundreds of times more often — it leads, the thesis
rule and the seam rules follow, the size/refactor gauges close.

| Pos | Cur # | Rule title | Tier | Rationale |
|----:|------:|---|---|---|
| 1 | 21 | If it can change, it's config | Critical | The chapter's workhorse; rules 22–30 all implement it |
| 2 | 36 | Architecture beats language | Critical | The thesis; getting this wrong is the chapter's least reversible failure |
| 3 | 32 | Every vendor axis gets an interface | Critical | The seam that makes everything swappable; on-prem↔cloud rests on it |
| 4 | 37 | Search before you build | Critical | Original code is the last resort; averts the biggest wasted-effort failure |
| 5 | 33 | Collaborators come through the front door | High | DI is the mechanism that makes rule 32's interfaces real and testable |
| 6 | 26 | No silent fallbacks | High | Silent degradation is the worst-to-diagnose production failure |
| 7 | 25 | Validate at startup, name the key | High | Converts config drift into a loud, named, immediate crash |
| 8 | 22 | One config layer, one precedence order | High | Without one layer, rule 21 decays into scattered environment reads |
| 9 | 31 | Objects with one job each | Medium | SRP at every scale; the default shape of new code |
| 10 | 30 | Storage goes through the adapter | Medium | Where the interface principle dies first; migration cost is a quarter, not a sprint |
| 11 | 29 | On-prem and cloud are config values | Medium | Deployment freedom is downstream of rules 21 + 32 |
| 12 | 28 | "Use X locally" means default, not destiny | Medium | The binding clause that keeps "go local" a one-line change |
| 13 | 24 | Zero-setup defaults | Medium | Removes the friction tax on every fresh clone |
| 14 | 27 | No magic numbers | Medium | Daily-fire refinement of rule 21 |
| 15 | 23 | Ship the `.env.example` | Medium | Documentation half of the config layer; cheap, often skipped |
| 16 | 38 | The file-size gauge | Supporting | Hard ceiling against one-line-at-a-time erosion; recoverable |
| 17 | 39 | No god classes | Supporting | Tripwire for a missing collaborator; refactorable |
| 18 | 34 | SOLID where it earns its keep | Supporting | Situational principle application; 31/32/33 already carry the load |
| 19 | 35 | One non-trivial class per file | Supporting | File-boundary honesty; mechanical to restore |
| 20 | 40 | Refactors are mechanical commits | Supporting | Process refinement of rule 8; keeps the gauges enforceable |

## Chapter 3 — Build (book 41–60)

The gates and the failure-visibility rules outrank portability mechanics:
a disabled gate lets irreversible failures through, and a swallowed error is
undiagnosable forever. Portability and dependency hygiene follow by fire
rate; set-once rules close.

| Pos | Cur # | Rule title | Tier | Rationale |
|----:|------:|---|---|---|
| 1 | 49 | Gates never disabled by default | Critical | A silently-off gate re-opens every irreversible failure Ch 1 closed |
| 2 | 51 | Catch specific, never swallow | Critical | An eaten error is a production failure with no witness — ever |
| 3 | 57 | Pin it and lock it | Critical | Unpinned dependencies make builds unreproducible and supply chain unauditable |
| 4 | 59 | Audit for vulnerabilities — on a schedule and at the door | High | A shipped CVE is exposure you can't retroactively remove |
| 5 | 48 | Health endpoints and graceful SIGTERM | High | "Healthy before handover" (hard rule 7) is unverifiable without it |
| 6 | 47 | Container-friendly by default — Podman, UBI, OpenShift | High | The structural deploy posture; the chapter that earns the subtitle |
| 7 | 54 | Loud in dev, graceful in prod, diagnosable always | High | The error-posture contract every handler implements |
| 8 | 41 | Three platforms, two in CI | High | The portability backbone; CI is what keeps it true |
| 9 | 52 | A logger, never print | Medium | Fires daily; the log is the only witness at 3 a.m. |
| 10 | 56 | AI errors surface; agents don't invent tools | Medium | Daily in agent work; silent AI failure misleads the human |
| 11 | 43 | Path libraries, never string glue | Medium | Highest-frequency portability mechanic |
| 12 | 58 | Stdlib plus one good dependency | Medium | Every dependency avoided is failure surface removed |
| 13 | 45 | No hardcoded temp, home, or drive letters | Medium | Dies in the first OpenShift deploy if violated |
| 14 | 42 | Both architectures, flagged exceptions | Medium | ARM-first reality; undocumented exceptions are time bombs |
| 15 | 44 | No shell-isms — orchestrate in Python or Node | Medium | Testable orchestration; bash scripts can't reach Ch 4's coverage bar |
| 16 | 55 | Cleanup is structural, not hopeful | Medium | Context managers prevent slow resource-leak death |
| 17 | 60 | Project-local virtualenvs, always | Supporting | Contains dependency damage to the project |
| 18 | 50 | Show progress; cached by default, expensive by exception | Supporting | Latency honesty; UX, not integrity |
| 19 | 53 | Structured logs once it's more than a script | Supporting | Refinement of rule 52 once scale demands it |
| 20 | 46 | Line endings settled by `.gitattributes` | Supporting | Set once per repo, then never fires again |

## Chapter 4 — Protect and Prove (book 61–80)

The chapter's own opener rules: containment first, because nothing else
matters if the artifact is radioactive. Prevention (hooks) leads, the
post-leak protocol and non-propagation follow — those are the maximum-
irreversibility moments. Eddie's anchor places the rubric rule high: it sits
at 4, ahead of the remaining scan mechanics, because the 90/95 bar governs
whether anything ships at all. Testing structure follows; the complexity
budget closes, as the opener intends.

| Pos | Cur # | Rule title | Tier | Rationale |
|----:|------:|---|---|---|
| 1 | 61 | Hooks Before the First Commit | Critical | Prevention beats response; the gate that makes every later scan automatic |
| 2 | 68 | Rotate First, Clean History Second | Critical | The protocol at the single most irreversible moment in software |
| 3 | 70 | Never Copy a Secret Anywhere | Critical | Propagation multiplies an already-irreversible failure |
| 4 | 78 | You get what you inspect — and it gets a grade | Critical | Eddie's anchor; the 90/95 rubric decides whether anything ships |
| 5 | 67 | Scan the Whole Artifact | Critical | Deploy is the widest trust boundary; the artifact, not the diff |
| 6 | 66 | Scan the Range, Not the Tip | High | An intermediate commit carries the leak past a tip-only scan |
| 7 | 71 | No test, no ship | High | The gate; untested logic is unproven logic |
| 8 | 72 | Contract first, code second | High | The discipline that shapes the entire test suite |
| 9 | 73 | 100% — lines and branches | High | The uninspected branch is the one that comes back from the field |
| 10 | 65 | Leaks Hide in "Harmless" Config | High | The actual leak vector — thirty harmless lines of YAML |
| 11 | 64 | Scan What You Didn't Write | High | Other agents' files are the unaudited input stream |
| 12 | 62 | Rescan on Push, and Bring the Tests | Medium | Second gate; redundancy for the gates above it |
| 13 | 75 | Correctness over speed | Medium | License to take the time the coverage bar requires |
| 14 | 74 | Coverage never goes down | Medium | Ratchet that protects rule 73's achievement |
| 15 | 63 | The .gitignore Knows About Keys on Day One | Medium | Passive defense; set once, saves forever |
| 16 | 69 | Fix the Hook That Missed It | Medium | Turns each leak into a permanent process improvement |
| 17 | 77 | Full regression, every feature, with the numbers | Medium | Recurring proof the suite still proves something |
| 18 | 76 | No network in unit tests | Supporting | Determinism mechanics for the suite |
| 19 | 79 | Small functions | Supporting | The complexity budget that makes 100% branch coverage affordable |
| 20 | 80 | Shallow nesting | Supporting | Same budget, second axis; closes the chapter as the opener intends |

## Chapter 5 — Ship and Remember (book 81–100)

Tag immutability is this chapter's irreversible failure — a moved tag breaks
every consumer's trust permanently. Memory rules rank just behind versioning
integrity: per the opener, written memory is the load-bearing wall for
stateless AI teammates. Hygiene sweeps close.

| Pos | Cur # | Rule title | Tier | Rationale |
|----:|------:|---|---|---|
| 1 | 83 | Tags are carved in stone | Critical | A mutated pushed tag breaks every pin forever; the chapter's one irreversible act |
| 2 | 82 | Versions only move forward | Critical | A reused or regressed version is a lie to every consumer |
| 3 | 99 | Persist decisions in the same commit | Critical | Memory is the load-bearing wall for stateless agents; chat is not memory |
| 4 | 81 | One version, one home | High | Everything else in the chapter reads from this single source |
| 5 | 98 | File it the moment you see it | High | Fires daily; an unfiled bug is a bug forgotten |
| 6 | 84 | Fetch before you tag | High | The check that prevents rule 83 violations before they exist |
| 7 | 86 | Every build wears a serial number | High | "What exactly is running on that box" must have an exact answer |
| 8 | 100 | Verbatim errors, diffs not prose, assumptions out loud | High | Fires every session; paraphrased errors destroy diagnostic signal |
| 9 | 88 | The changelog rides in the bump commit | Medium | Keeps the version and its story from drifting apart |
| 10 | 90 | Plans tell you their own status | Medium | Stale status is a process violation; plans are agent memory too |
| 11 | 97 | ADRs are immutable | Medium | Supersede, never edit — the decision record stays trustworthy |
| 12 | 87 | The version answers the door | Medium | Visibility makes rule 81 verifiable in the field |
| 13 | 85 | Push tags by name | Medium | Mechanical guard against clobbering remote tags |
| 14 | 95 | Lint and format every commit | Medium | Daily-fire baseline hygiene; keeps CI green |
| 15 | 92 | Sweep the dead code | Supporting | Recurring debt control after feature work |
| 16 | 89 | After the release, take out the trash | Supporting | Post-stable cadence; cleanup before new features |
| 17 | 96 | Regenerate the README | Supporting | Regenerated beats patched, but failure is recoverable staleness |
| 18 | 93 | No commented-out code | Supporting | Git history is the archive |
| 19 | 94 | No orphan TODOs | Supporting | Tracker-linked or dated-with-owner; hygiene refinement of rule 98 |
| 20 | 91 | Say what you're installing | Supporting | Restates hard rule 4 at the workflow level; the gate already lives in Ch 1 |

---

## Mechanical steps

Execute only after Eddie signs off on the tables above. One commit per step
where marked; the whole renumber is one logical change but lands as
reviewable units.

1. **Freeze the mapping.** From the tables, generate `old book # → new book #`
   for all 100 rules (new # = chapter base + proposed position). Keep it as a
   working scratch table; it drives every later step and becomes Appendix D's
   regenerated content. Verify it is a bijection on 1–100 before touching any
   file.
2. **`book/ch01.md` … `ch05.md`, one file at a time** (5 commits, or 1 if
   Eddie prefers):
   a. Physically reorder the `## Rule N:` sections into proposed order.
   b. Renumber the headings sequentially within the chapter range.
   c. Reorder and renumber the chapter card (closing checklist) to match.
   d. Rewrite opener prose that narrates contiguous runs — Ch 3's three
      "movements" (41–46 / 47–50 / 51–60) and Ch 4's "containment rules come
      first" framing no longer map to contiguous numbers; rewrite by theme,
      not range, or cite the new numbers explicitly.
   e. Update every in-prose cross-reference in the file via the mapping
      (e.g. ch01 references to Rules 11, 17, 18, 19; ch02 references to
      Rules 21–33 cluster).
   f. Update Mermaid edge labels — the Ch 4 scan-gate placement map names
      Rules 61, 62, 64, 65, 66, 67, 69 inside edge labels and sequence steps.
3. **`RULES.md`**: reorder entries within each topic section so the relative
   order matches the book's new within-chapter order; renumber 1–100. Update
   the internal cross-reference in repo rule 87 ("see rule 4") and any other
   `rule N` mentions to the new numbers.
4. **`book/00-front-matter.md`**: chapter ranges (1–20 … 81–100) are
   unchanged; verify the "how to read" description still holds and no
   specific rule numbers are cited.
5. **`book/99-back-matter.md`**: regenerate the Appendix D mapping table
   from the frozen mapping; re-sort the index of rules by new book number;
   sweep the glossary for rule-number citations.
6. **`book/OUTLINE.md`**: note the reorder under the restructure callout
   (the live structure paragraph) so the outline doesn't contradict the
   manuscript.

### Regression checks (all must pass before the commit that closes the work)

- **Reference resolution:** script (or careful grep pass) extracts every
  `[Rr]ules? N(–M)?` from `book/*.md` and `RULES.md`, resolves each N to the
  `## Rule N:` heading, and a human confirms the surrounding sentence still
  describes that rule. Zero dangling or wrong-target references.
- **Heading sequence:** `grep -h '^## Rule' book/ch0*.md` yields exactly
  1–100 in order, twenty per file.
- **Chapter cards:** each card has exactly 20 entries whose numbers and
  titles match the chapter's headings in order.
- **Diagrams:** `book/build.py` render pass succeeds; visually confirm the
  Ch 4 gate-map labels cite the new numbers and still describe the right gate.
- **Appendix D:** table covers all 100 rules, both columns are permutations
  of 1–100, and spot-checks against the chapter files agree.
- **Book ↔ repo consistency:** for each of the 100 rules, the `RULES.md`
  one-liner and the book's bolded statement describe the same rule under the
  same number (text drift between book and repo is a bug, per OUTLINE.md).
- **Full book build:** EPUB + PDF build green.

## Contestable placements (flagged for Eddie)

- **Ch 1, pos 1:** the Powell rule ahead of "No scan, no ship" follows
  Eddie's anchor verbatim; note it displaces the rule the Ch 1 opener
  currently argues is first "because it guards the only mistake that cannot
  be undone." The opener paragraph will need a sentence acknowledging the
  new order (decision protocol first, then the lines it protects).
- **Ch 4, pos 4 (rubric):** placed inside the containment block. If Eddie
  reads "high in its chapter" as "leads the proof half," it moves to pos 6
  and the scan mechanics close ranks above it.
- **Ch 2, pos 1 vs 2:** config workhorse over the architecture thesis is a
  fire-rate call; reversing them is defensible on irreversibility grounds.
- **Ch 5, pos 8 (rule 100):** verbatim-errors fires constantly but its
  failure is recoverable; it could sit as low as 12 without violating the
  criteria.

Author: Claudius
