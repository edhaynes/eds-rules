# Rule-Quality Rubric

A way to grade how *good* each of the 100 rules is — not how important it ranks
(that's the per-chapter importance order), but its quality as a rule: does it
prevent real damage, is it cheap to follow, does it keep the architecture simple,
can you actually enforce it?

Distinct from the root `RUBRIC.md` (which grades the book's *prose*). This grades
the *rules themselves*, on engineering merit.

## Dimensions

Each rule scores 0–10 on six dimensions:

| Dim | Weight | Question | 10 looks like | 0 looks like |
|---|--:|---|---|---|
| **Pertinence** | 0.30 | How often would Claude, left to its own devices, violate this — and how badly does that hurt? `P(violate) × severity`. | Claude breaks it constantly and the cost is catastrophic (leaks a secret, force-pushes). | Claude essentially never does it, or the cost is trivial. |
| **Security** | 0.15 | Does following it prevent a security failure? | Directly stops a breach or leak. | No security bearing at all. |
| **Cost-effectiveness** | 0.20 | Value returned per unit of friction to follow it. | Cheap to do, huge payoff (run a scanner; ship `.env.example`). | Heavy ongoing tax for marginal gain. |
| **Architectural simplicity** | 0.15 | Does obeying it make the system *simpler* and cleaner? | Directly reduces coupling/complexity (DI, one config layer, small functions). | Adds ceremony or scaffolding. |
| **Enforceability** | 0.10 | Can a hook/CI/linter check it, or is it a judgment call? | Binary and machine-checkable (coverage %, secret scan, lockfile). | Pure philosophy, unmeasurable. |
| **Generality** | 0.10 | Does it apply across projects, stacks, and teams? | Universal (fail fast, validate config). | Niche or opinionated to one stack/crew (Podman-only, persona-specific). |

## Compositing

```
quality(0–100) = ( 0.30·Pertinence + 0.15·Security + 0.20·CostEff
                 + 0.15·ArchSimpl + 0.10·Enforce + 0.10·Generality ) × 10
```

Pertinence is weighted heaviest because the whole point of the document is to
stop the expensive mistakes an unsupervised agent makes by default — a rule that
prevents a frequent, costly failure is doing the most work.

## Reading the scores

These are deliberately **not** all 90+. A rule can be canonical and still score
in the 50s if it's an unenforceable philosophy (rule 28, "architecture beats
language") or opinionated to one stack (rule 49, Podman/UBI/OpenShift). A low
score is not "delete this" — it's "this earns its slot on conviction, not on
broad cheap-to-enforce leverage." The bar-anchor lines at 90/95 mirror the
project's own "solid A−" quality target.

Grades are one informed engineering judgment (Jason), not gospel — the script
that holds them is the single source; edit a tuple and re-render.
