Status: Partial — Remaining: map full old-100 → layers; frontier-free crew demo; sync RULES.md/STATE. (book synced 2026-06-16 — new Chapter 7 "From a Hundred Rules to an Axiom Core" + Appendix F, on main.) (branch: rules-taxonomy, 2026-06-16)
Author: Jason-eds

## Decisions (Eddie, 2026-06-16)
- Output form: **composer + layer files** (built: `taxonomy/`).
- Scope: axiom core + layers + the **3-crew worked example** (Claudius/Claude/Linda).
- Axiom core: **keep at 24, no trim.** A frontier seat (Opus) is required to hold the
  whole core resident; the crew includes one, so axioms are covered. (Guy's test
  still noted: a *frontier-free* 8B+14B crew would need the core ≤22 — not pursued.)

# Re-taxonomize the rules: a small axiom core + composable preference layers

## The shift
Drop the fixed "100." The flat list graded on one universal scale put role/project
rules at the bottom of `grades.csv` (crew 33.5, go-local 25.5, Podman/UBI 45.0) —
not because they're weak but because they're **mis-scoped**: a role rule graded as
an axiom always loses on `generality`.

New model: **~20–30 immutable axioms** form the universal core; **everything else is
a fill-in layer** — personal/architect prefs, project prefs, employer prefs. Count
is no longer fixed. This is the canon's own governance hierarchy made literal
(town→library→bookshelf→book; constraints only tighten downward, never loosen).

Supersedes the prior "keep 100 as the brand, flag don't cut" decision (STATE.md).

## Why the structure exists: a rule memory budget (the real driver)
This isn't filing — it's fitting a memory budget. An 8B model can't hold 100 rules
(sizing law, rule 94: ~1 rule/B params). So treat the ruleset as a **cache
hierarchy**:
- **Resident working set, per seat** — each model "memorizes" (in weights via the
  persona fine-tune, or always-in-system-prompt) a slice sized to its budget:
  Jason 8B ≈ 8, mid 14B ≈ 14, Claudius Opus ≈ the axioms + a large slice.
- **Team-resident union ≈ 60 rules** held across the 3 seats with no single seat
  holding all (rule 95: a view of the canon per seat; union = canon).
- **Retrieved tail** — every other rule lives in the canon and is **paged into the
  context window on demand** when a task touches it (about to deploy → inject the
  deploy rules; untrusted input → inject input-validation). Cheap because it's
  just-in-time, bounded by the tier's context ceiling (rule 96).
This is why axioms must be *few*: the resident budget is tiny, so the always-on core
has to be the smallest set that must never be missed; everything else is paged.

**Crew size is the capacity dial.** Team-resident capacity = Σ(per-model rule
budgets). More complex project → add members → more rules held resident → less
paging. The composer reports this and scales both ways:
- **Guy's test (minimize):** the smallest crew (fewest params/seats) whose summed
  budget still covers the *required-resident* set (axioms + must-hold project rules).
  Answers "how small can it get and still be safe?"
- **Scale up:** add seats for harder projects; capacity grows, paging shrinks.

## The layers (by scope)

**AXIOMS (~20–30, immutable, universal).** What almost no serious engineer disputes:
safety, security, decision discipline, the quality stance. Proposed set below.

**PERSONAL / ARCHITECT PREFS.** The operator's opinions and crew:
- Engineering style: OO + SOLID, file/function size limits, one-class-per-file,
  config layering, dependency philosophy, logging style. (These are *opinions* —
  many disagree — so prefs, not axioms.)
- The crew: roles, team size, **model bindings**, rule-slices per the sizing law.
  Eddie = 5 personas; a 3-crew starter example:
  | Role | Job | Model | Rule budget (≈1/B params, rule 94) |
  |------|-----|-------|-------------------------------------|
  | Jason | PM / coordinator | Llama 8B | ~8 |
  | Claudius | Architect | Claude Opus | full canon |
  | (mid) | Python test-dev / easy coding | 14B | ~14 |
  - Binding is config per stack, never hardcoded (rule 14/20).
- The stack: **Podman, UBI, Ansible, OpenShift**; rootless + SELinux enforcing.
- Fleet operation: the sizing/slicing laws (current 93–100).

**PROJECT PREFS.** What's being built — here:
- Cloud-native distributed app; **OpenShift-first, portable to GCloud**.
- **Multi-platform target set: Windows, Linux, macOS, iOS** (the cross-platform
  *principle* is craft/axiom; the *target set* is the project's choice).
- Deployment, distributed-systems rules (trace IDs, timeouts/retries/circuit-
  breakers), migrations, idempotency.

**EMPLOYER PREFS.** Org-level constraints (compliance, approved vendors/regions,
review gates). Placeholder layer — fill per engagement.

## Testbed & connectivity (cross-cuts personal/project infra)
Short section on the testbed and a **connectivity rubric**:
- Substrate: remote compute/host over **SSH**, provisioned by **Ansible**, reached
  headlessly (rule 12: no display, script everything).
- Connectivity rubric — prove reachable+ready before use, graded not vibed: SSH up,
  Ansible ping/play converges, health/readiness endpoint green, a representative
  request succeeds. Ties rule 8 (healthy before handover) + 47 (health endpoints).

## Proposed AXIOM core (~24; from RULES.md — for Eddie to ratify)
Security & safety: 2 secret-scan, 3 no-hardcoded-secrets, 4 distrust-input (+ bounds/
range/overflow checking, folded in), 5 destruction-needs-human, 13 least-privilege,
51 secret-hooks, 52/53 burned-secret-rotate.
Discipline: 1 Powell-90%, 6 autonomy=version-control, 7 push-early, 8 green/healthy,
9 one-purpose-per-commit, 10 fail-fast, 11 disclose-dependencies.
Quality: 62 inspect+grade-to-rubric, 63 tests+regression-first, 64 contract-first,
66 correctness>speed.
Working w/ humans: 90 plan-first, 91 no-flattery, 92 verbatim-errors/diffs/assumptions.
Borderline (axiom vs craft-pref — Eddie calls it): 65 100%-coverage, 12 no-OS-
assumptions/script-everything, 21 zero-hardcoded-values.

Everything not in the axiom core drops to a prefs layer.

## Open decisions (need Eddie)
1. **Output form** (recommend c): (a) one re-sectioned RULES.md; (b) separate files
   per layer; (c) `axioms.md` + `layers/{personal,project,employer}.md` + a small
   **composer** that emits a per-seat ruleset (axioms + selected prefs, sized to the
   model's rule budget). (c) is the branch's real payoff and matches rules 95–96.
2. **Axiom set** — ratify / adjust the ~24 above; decide the borderline three.
3. **This branch's scope** — taxonomy + axiom core + the layer files, *and* ship the
   3-crew worked example (model bindings + slices) as the reference personal layer?

## Done when
Axioms ratified; every old rule mapped to a layer or cut; composer (if chosen)
emits a valid per-seat slice; grades/book/STATE re-synced; branch reviewed.
