Status: Ready for Claudius — 2026-06-12

# Brief: F6 axioms · F10 Security chapter outline · F7 capstone architecture

Context: PLAN_agent-assignments.md (the program), RUBRIC.md (the bar and the
Reddit test), Edith's grade findings in bugs.md B6.

1. **F6 — axiom sets (per features.md F6):** for each of the five rule
   chapters, 3–5 plain-English axioms and the axiom→critical-rule trace,
   delivered as a spec (Mermaid flowchart source per chapter, B&W
   constraints) in `plans/DESIGN_axioms.md`. Pseudo-proofs, explicitly:
   "axioms, not theorems." Zero formal notation. Eddie signs before any
   manuscript edit.
2. **F10/F11/F12 — the practice-half arc (one design, not piecemeal):**
   Eddie has ruled Security (F10: rootless, SELinux, least privilege) and
   High Availability (F11: MTTF, MTTR, the five-nines ladder) as chapters,
   with Lifecycle/Day-2 (F12: ops handoff, routine vs. urgent updates, field
   debugging, Ansible as the automation engine) a strong candidate. These
   plus the Bard capstone form the book's practice half — design the WHOLE
   arc in `plans/DESIGN_practice-half.md`: chapter order, what each promises
   and the capstone delivers, word budgets, diagram candidates, and a
   recommendation on F12 (in or out). Note the shape: these mirror the Bard
   Technical Solutions pillars — say so if it strengthens the framing, skip
   it if it reads as an ad.
3. **F7 — capstone:** PLAN_capstone-bardpro.md (scoping in flight) — own its
   architecture sections after Eddie signs. **Naming: "Bard," Pro dropped.**

Acceptance: specs decisive enough that drafting is mechanical; shipped vs.
design-only labeled with brutal clarity; no manuscript edits this wave.
