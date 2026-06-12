# Features

Backlog for the eds-rules repo and the book (*100 Rules for Writing My Software: The Red Hat Way*).

## F1 — EPUB + print PDF build pipeline
- **Status:** Open
- **Added:** 2026-06-12
- Build the manuscript (`book/00-front-matter.md`, `ch01–ch05`, `99-back-matter.md`) to EPUB (Kindle) and print-ready PDF (KDP, 6"×9") with pandoc; render the 30 Mermaid diagrams to grayscale SVG/PNG via mermaid-cli.
- Static B&W audit passed 2026-06-12 (zero color styling in any diagram); actual render check pending tooling.
- **Blocked on:** `pandoc` and `@mermaid-js/mermaid-cli` not installed (Eddie to approve/run install).

## F2 — Ansible coverage in the book
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Add Ansible to the book. Natural home: Ch. 3 *Build* (deployment) alongside Podman/UBI/OpenShift — the Red Hat automation leg of the stack.
- **Clarify:** mention/section within existing rules, or a rule of its own? The count is fixed at 100 (v1.1.2 policy) — a new rule requires consolidating or deprecating an existing one, never growing the list.

## F3 — Zero-trust infrastructure in the book
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Add Eddie's zero-trust infrastructure to the book. Natural home: Ch. 4 *Protect and Prove* (trust boundaries, secret hygiene) or Ch. 3 deployment.
- **Clarify:** scope of "my zero trust infrastructure" — the book is public and commercial, so actual private details (tailnet names, hostnames, network topology) must be generalized into principles/patterns, not published as-is. Same fixed-at-100 constraint as F2 if it becomes a rule.

## F5 — Order rules within each chapter by importance
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Within each of the five chapters, reorder the twenty rules most-important-first.
  Named anchors from Eddie: the Powell rule leads its chapter; the quality
  rubric ranks high in its chapter.
- Scope note: reordering renumbers all 100 rules — every "Rule N"
  cross-reference in prose and diagrams, the chapter cards, the Appendix D
  mapping, and `RULES.md` (book↔repo drift is a bug, so both move together).
- **Plan:** ordering proposal doc for Eddie's sign-off first, then one
  mechanical renumber commit with a cross-reference sweep.

## F6 — End-of-chapter axiom blocks ("axioms, not theorems")
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Each chapter closes with a **simple B&W flowchart showing the "proof"**
  (Eddie, 2026-06-12): 3–5 plain-English axiom nodes flowing into the
  chapter's critical-tier rules — the axiomatic *style* as honest rhetoric,
  never claimed as mathematical proof. Tells a dissenting reader exactly
  which premise they're rejecting (ties into the fork-what-doesn't-work
  license invitation). Short axiom list in prose beside the chart; one
  disclaimer sentence in "How to read this book." Renders via the existing
  Mermaid→grayscale pipeline.
- Constraints: zero formal notation (newbie audience-fit is the heaviest
  rubric weight); sequence AFTER F5 — axiom blocks cite rule numbers the
  reorder changes.

## F4 — Worked examples of well-designed apps: Squawk Box, cdn-sim
- **Status:** Open
- **Added:** 2026-06-12 (Eddie; cdn-sim added same day)
- Use Squawk Box and cdn-sim as the book's worked examples of well-designed
  apps (Squawk Box possibly illustrating the zero-trust/F3 material).
- **Clarify:** which repo is Squawk Box; which aspects of each to showcase
  (architecture? config layer? deploy pipeline?); where each lands (one
  chapter's worked example vs. a thread through several). Public-book
  caution applies: generalize, don't expose private endpoints/infra.
