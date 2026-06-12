# Bugs

Known bugs for the eds-rules repo and the book manuscript.

## B1 — Post-F5 narrative seams (body sentences strained by the reorder)
- **Status:** Open
- **Observed:** 2026-06-12, during the F5 importance reorder (body text was
  frozen by instruction; these sentences now read against the new order)
- Ch. 2, new Rule 30 tail: "That's the configuration half of this chapter in
  one sentence" — still numerically true but the halves now interleave.
- Ch. 2, new Rule 31 opening: "This rule is where the previous eight stop
  being hygiene" — its eight predecessors are no longer the config-hygiene
  run the sentence described.
- Ch. 1 transition paragraph: lists the second half as "five fixed roles,
  one human, and the decision doctrine that binds them" — accurate, but the
  doctrine now *leads*; one-clause polish available.
- Fix in a single editorial pass after the F5 commits land (needs Eddie/Iris
  judgment — body text, not mechanical).

## B2 — Powell rule misdefined in Ch3 + Ch5 synopses (Edith, cold grade 2026-06-12)
- **Status:** In Progress (floor-fix sprint, 2026-06-12)
- Ch3 synopsis: "the Powell rule: you break it, you own it"; Ch5 synopsis:
  "the Powell rule holds: you touched it, you own it." That is the Pottery
  Barn rule — a different Powell doctrine. The flagship rule is *get 90% of
  the information, then decide*. Worst defect in the book; both openers.

## B3 — Rule 46 ignores rootless Docker (Reddit-test exposure)
- **Status:** In Progress (floor-fix sprint, 2026-06-12)
- "Docker's insecure daemon" argues against Docker's classic architecture as
  if it were the only one; rootless mode has shipped since 20.10 (2020).
  Fix: acknowledge it and state why Podman still wins (rootless by
  construction vs. opt-in).

## B4 — RULES.md drift: repo rule 53 vs book Rules 62–63
- **Status:** In Progress (floor-fix sprint, 2026-06-12)
- Repo says "never copy a secret anywhere," full stop; the book correctly
  carves the verbatim-disclosure-to-owner exception. Repo short form is
  incomplete — drift is a bug.

## B5 — Appendix E overclaims the open-weights tune
- **Status:** In Progress (floor-fix sprint, 2026-06-12)
- "A weekend and a good dataset" / robustness "High" overstates what LoRA
  can instill (agentic process discipline is not a weekend). Soften to honest
  ranges; the Reddit test applies.

## B6 — Minor grade findings (one pass, low severity)
- **Status:** Open
- Ch3 synopsis claims function-size limits already established (they are
  Ch4, Rule 79). Rule 64 gauge + Rule 69 funnel diagrams are decoration —
  cut or earn. Rule 13 sprint-lanes diagram may be cramped at trim — check
  in printed proof. Frustration #1 (hallucinated *library* APIs, not just
  tools) never named where the arriving reader looks — add the named
  incident to Rule 50's body or Ch2 search-first.
