# Hand‑off for Fable / Claude

**Purpose** – Provide concrete, prioritized tasks for the AI agents to improve the book / guide so it meets the expectations of a publishable technical handbook.

---

## 1. Add a narrative introduction
- Create a new chapter `book/ch00-intro.md` that:
  - Opens with a hook (why disciplined AI‑driven development matters today).
  - States the core philosophy: *discipline‑first, AI‑as‑gatekeeper, human‑as‑final arbiter*.
  - References the Powell rule as the decision backbone.
- Update the build pipeline (`book/build.py` or the table of contents) to include this file as the first chapter.

## 2. Expand the “Crew” profiles
- Add a dedicated markdown `book/crew-profiles.md` containing a full profile for each persona (Jason, Linda, Claude, Claudina, Claudius) covering:
  1. **Role & temperament**
  2. **Typical prompts & responsibilities**
  3. **Decision‑making scope**
  4. **Model binding example**
  5. **Example failure mode**
- Reference this file from the “Meet the crew” section (e.g., link from `book/_build/00-front-matter.md`).

## 3. Insert concrete case studies / war stories
- Add a new chapter `book/ch99-case-studies.md` (or embed at the end of each relevant rule) with short, self‑contained stories for the most critical rules:
  - **Rule 1 (Secret scan)** – real leak and remediation timeline.
  - **Rule 2 (Hard‑coded secret)** – token propagation by an AI agent.
  - **Rule 3 (Destructive command)** – accidental `rm -rf` caused by a missing env var.
  - **Rule 9 (Anonymous dependency)** – supply‑chain attack from an unnoticed transitive dep.
  - **Powell rule** – a decision that stalled because the 90 % threshold was never reached.
- Each story must end with a *Lesson* bullet that maps back to the rule.

## 4. Consolidate duplicate rules
- Scan the rule set for overlapping directives (e.g., Rule 4 *Agent autonomy* and the later rule about “never add a dependency without name/purpose/license” that repeats the “state before adding” requirement).
- Merge duplicates into a single rule with numbered sub‑clauses, then renumber subsequent rules to keep the total at 100.
- Update the table of contents and any cross‑references (README, front‑matter, chapter cards).

## 5. Clarify the Powell rule (Rule 11)
- Refine the rule text to explicitly list the decision‑making matrix:
  - **≥ 90 %** → fast persona
  - **50 %‑90 %** → heavyweight persona
  - **< 50 %** or **high‑stakes** → human
- Add a concise checklist (yes/no questions) that agents can use to determine the correct path.
- Provide a concrete example of a “high‑stakes” scenario (e.g., secret rotation, production data migration).

## 6. Reformat all rules for scannability
- Adopt a uniform block for each rule:
  ```
  ## Rule X: <Title>
  **Directive:** <one‑sentence imperative>
  **Rationale:** <why this rule exists, with a short scar story>
  **Guardrail:** <how the rule is enforced – pre‑commit hook, CI check, etc.>
  ```
- Apply this format to every rule file (currently in `RULES.md` and chapter markdowns).
- Ensure each block is no longer than 8 lines to keep it easy to skim.

---

## Acceptance criteria
- The repository builds a PDF that includes the new intro, crew profiles, and case‑study chapters.
- All rule numbers still sum to **100** after consolidation.
- The Powell rule text contains the explicit matrix and checklist.
- Every rule follows the unified formatting template.
- No broken links; the Table of Contents reflects the new files.

*Prepared for the Fable / Claude agents to execute.*
