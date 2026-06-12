Status: In Progress

# PLAN — Agent assignments: B+ (87) → 95 publish bar

Eddie's directive (2026-06-12): distribute the remaining book work across the
crew via the handoff protocol (`plans/HANDOFF_<recipient>.md`). Floor-fix
(v1.3.5) addressed Edith's worst findings; per her report the book should now
sit near the 90 working bar. This plan carries it to 95.

## Assignment matrix

| Seat | Brief | Backlog items | Handoff |
|---|---|---|---|
| **Claudius** (architecture) | Axiom sets + pseudo-proof flowchart specs per chapter; **Security chapter outline** (rootless/SELinux/least-privilege philosophy → "see it in action in Bard"); capstone architecture sections once PLAN_capstone-bardpro is signed (note: "Bard," Pro dropped) | F6, F10, F7 | HANDOFF_Claudius.md |
| **Claude** (backend) | Crew-installation appendix: copy-pasteable persona/harness configs for Claude Code, OpenCode, local stacks | F8 | HANDOFF_Claude.md |
| **Claudina** (frontend/production) | Visual production: ComfyUI plate specs (6 prompts), EPUB device QA, diagram-cramping proof check, cover spec | B6 (proof check), art swap | HANDOFF_Claudina.md |
| **Linda** (marketing) | KDP listing: title/subtitle metadata, categories, keywords, back-cover copy from the frustration map; launch sequencing | GTM | HANDOFF_Linda.md |
| **Iris** (editorial) | Line pass: B6 remainder (decoration diagrams cut-or-earn, hallucinated-API incident named in Rule 50), F9 newbie on-ramp design | B6, F9 | HANDOFF_Iris.md |
| **Edith** (assessor) | Re-grade gates: after wave 1 (target ≥90 confirmed), after capstone + F8 (target ≥93), publish gate (≥95). No edits, ever. | grade gates | (commissioned per gate, no standing brief) |
| **Jason** (PM) | Coordination, commits, scope containment, this plan's status | — | — |
| **Eddie** (principal) | Trademark email; author read-through at trim size; ComfyUI renders (6 plates + crew); sign-offs: axioms (F6), capstone claims (F7), on-ramp form (F9) | — | — |

## Sequencing

- **Wave 1 (parallel, independent):** Iris line pass · Claude F8 appendix ·
  Claudius F6 axioms · Claudina production briefs · Linda GTM brief.
  No file overlap: Iris owns ch01–ch05 prose touches this wave; Claude owns a
  NEW appendix section in 99-back-matter.md (coordinate the single file with
  Iris via Jason — Iris does not touch back matter this wave); Claudius
  delivers specs as plan docs (no manuscript edits); Claudina and Linda
  deliver briefs (no manuscript edits).
- **Gate:** Edith re-grade → confirm ≥90.
- **Wave 2:** Security chapter (F10) + capstone chapter drafts (Claudius
  outlines + Jason-coordinated drafting, Eddie voice pass) · F6 flowcharts
  rendered into chapter closers · plate swap when Eddie's renders land.
- **Gate:** Edith re-grade → ≥93; Eddie read-through.
- **Wave 3:** polish from both gates' findings; trademark answer resolves the
  cover; Edith publish gate ≥95. Nothing publishes below 95.

## Standing constraints (all seats)

- The Reddit test (RUBRIC.md): no overclaim, pseudo-proofs stay pseudo.
- Audience fit is the heaviest weight: plain language, terms taught before
  used.
- Book↔RULES.md drift is a bug. Rule bodies change only with a bug/feature
  entry behind them.
- One purpose per commit; Jason commits, agents never do.

Author: Jason
