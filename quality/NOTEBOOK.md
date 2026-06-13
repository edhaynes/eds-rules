# Lab Notebook — grading and polishing the 100 rules

A running log of the 2026-06-13 investigation into the *quality* of the rules
themselves (not the prose). Kept for a final report. Newest findings appended.

## Premise

We added three rules (input-security, idempotency, latency budget), then asked:
how good is each rule, where are the gaps, and how many polish rounds keep
finding meaty new rules before returns diminish? Eddie's standing quality bar:
solid A− software, and for an individual rule, **5/10 (=50/100) is the keep/cut
line — a rule should be above average to earn a slot.**

## Entry 1 — the 3-rule swap (commit f4b3ccd)

Net-neutral at 100. Added by importance: **#3 input-security**, **#47
idempotency**, **#76 latency budget**. Retired by consolidation: LF line-endings,
standalone SOLID, the dependency-disclosure duplicate. (Book sync still pending —
B12.)

## Entry 2 — why the three gaps existed (quality/why-these-gaps.md)

Eddie corrected two of three root causes, which tightened the finding:
- **Input-security** — the only *true* blind spot. Cause: sole consumer → the
  trust boundary collapses (you self-regulate your own input). Monkey testing
  found robustness bugs, not adversarial ones (random input never lands on
  `'; DROP TABLE`). Background contributor: a confidentiality/crypto security
  tradition, not app-sec.
- **Idempotency** — NOT a blind spot. Eddie preaches it (Ansible's defining
  attribute, already earmarked for the planned Ansible chapter). It was missing
  as a *discrete rule* because it was tacit + implied-by-Ansible.
- **Latency budget** — missed because it's so internalized he'd never violate
  it; you don't write rules for mistakes you never make. The trap: agents don't
  inherit the reflex.
- **Through-line:** one real blind spot; the other two are *tacit mastery never
  externalized for a non-expert AI executor.*

## Entry 3 — the rubric and first grading

Six dimensions, pertinence weighted .30 (quality/RUBRIC.md). First pass: mean
60.3, range 38–90. **Flawed** — see Entry 4.

## Entry 4 — Eddie catches central-tendency bias (commit d94f119)

Observation: "we're still delivering meaty rules at the bottom; I expected a much
higher falloff — are we grading correctly?" Correct. Dimensions had clustered in
4–8; nothing could fall far. Recalibrated to the **full 0–10 range** (a
niche/never-violated rule may score 1–2). New distribution: **mean 55, range
25.5–90, and 33 rules below the 50 bar.** Floor is now go-local (25.5), Linda
(30), five-roles (33.5) — honest. The graph gained the 50 keep/cut line.

## Entry 5 — importance ≠ rubric-quality (the Powell divergence)

Eddie ranks the **Powell rule (90% then decide) #1**; the rubric ranks
**secret-scan #1** and puts Powell mid-pack (~60). Not a contradiction — two
different questions. Eddie ranks by *foundational-ness* (Powell is the decision
OS every rule runs through — the architect's keystone view). The rubric ranks by
*operational leverage* (irreversible × frequent × enforceable). Powell is
unenforceable (you can't CI-gate "did you reach 90% before deciding"), so it
scores mid despite being the most important rule. **The rubric has no
"load-bearing / foundational" axis** — it measures a rule as an individual
enforceable directive, not as the frame others hang on. Both lenses are kept:
the book orders by importance; the graph scores by quality.

## Entry 6 — Eddie's new rule, and consolidation as polish

Proposed: *latency & determinism always considered; when busy, show live
progress and surface warnings/errors as they happen.* Grades **52.5 → rank
58/101, above the bar.** Notably it **consolidates two below-bar rules** —
#50 "show progress" (45.5) and #76 "latency budget" (45.5) — into one above-bar
rule. That is the polish dynamic itself: merge weak siblings into one strong rule.

## Entry 7 — the polish experiment (experiments/polish-rounds/)

10 review rounds, each surfacing the best *new* gap, graded on the recalibrated
rubric. Result (best candidate per round): **58, 55.5, 51.5, 49.5, 49, 47.5, 44,
40, 37, 32.** The taper **crosses the 50 bar at round 4** — slightly earlier than
Eddie's "taper by 5," directionally right. Deeper finding: **only 5 above-bar new
rules exist to be found** (UTC/time, least-privilege, timeouts+retries, Eddie's
latency rule, migrations). Everything after — observability, review-gate, PII,
concurrency, backups, a11y, canary… — grades 42–49.5, real but below the bar.

## Entry 8 — the headline: 100 is not sustainable at a 50 floor

Putting Entry 4 + Entry 7 together:
- 33 existing rules sit below the 50 bar.
- Polish can only refill ~5 above-bar replacements.
- Therefore a rules doc with a hard 50-quality floor is **~70–73 rules, not 100.**
The "100" was padded with ~30 below-average (niche/hygiene/crew) rules. The
honest choices: (a) a leaner ~70-rule set, every rule above the bar; or (b) keep
"100" as a brand and accept a sub-bar tail. Decision pending with Eddie.

## Open threads

- Cut depth: which of the 33 sub-bar rules go (Eddie: keep Podman/UBI by
  conviction; discard most others).
- Refill: adopt the ~5 above-bar polish finds (UTC, least-privilege, timeouts,
  Eddie's latency rule, migrations)?
- Book sweep (B12) still pending the cut/refill outcome — better to sweep once.
