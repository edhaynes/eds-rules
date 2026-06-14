Status: In Progress — 2026-06-13

# PLAN — Book sync (B12): bring the book to RULES.md (two changesets)

Sync `book/ch0*.md` + cards + Appendix D + cross-refs to the two RULES.md
changes shipped 2026-06-13: the 3-in/3-out swap (1.4.3) and the STATE-rule
insert + structured-logging fold (1.4.4). Decision (Eddie): **flex chapters to
19–21**, do NOT keep rigid 20. Count stays 100.

## Net change (4 in, 4 out)

**New essays to write** (in the book voice, STYLE.md):
1. **Input-security** → Ch1 (First Principles), early — beside the secret rules
   (after "Never hardcode a secret"). The other half of security: malicious input.
2. **Idempotency** → Ch3 (Build), in the deploy/gates cluster.
3. **Latency/determinism budget** → Ch4 (Protect and Prove), in the testing cluster.
4. **STATE / project memory** → Ch5 (Ship and Remember), memory cluster — high in
   the chapter (grades 67).

**Essays to retire** (content folds into a sibling, no discipline lost):
- **LF line endings** (book ~R60, Ch3) → folded into the path-library rule.
- **SOLID** (book ~R38, Ch2) → folded into the OO-design rule.
- **Dependency-disclosure dup** (book ~R100, Ch5) → folded into the hard
  dependency rule.
- **Structured logging** (book ~R59, Ch3) → folded into the logger rule.

## Chapter deltas (→ flex sizes)

| Ch | Adds | Removes | Net | New size |
|----|------|---------|----:|---------:|
| 1 First Principles | input-security | — | +1 | 21 |
| 2 Design | — | SOLID | −1 | 19 |
| 3 Build | idempotency | LF, structured-logging | −1 | 19 |
| 4 Protect & Prove | latency budget | — | +1 | 21 |
| 5 Ship & Remember | STATE | dep-disclosure dup | 0 | 20 |

Total 21+19+19+21+20 = 100. Book numbers stay contiguous 1–100; the
cumulative offset at each point drives the renumber.

## Steps (commit per logical unit)

1. **Draft the 4 new essays** (parallel) — voice + structure of an existing rule
   essay; technical/argument paragraphs written, personal war-stories left as
   `[ANECDOTE: ...]` placeholders for Eddie/Iris (the author writes his own
   history). [in progress]
2. **Freeze the mapping** — DONE + verified: `plans/book-sync-mapping.py`
   (bijection on 1–100 asserts OK; chapters 21/19/19/21/20). Retirements fold:
   SOLID(old38)→30, structured-logs(old59)→50, line-endings(old60)→52,
   say-what-you-install(old100)→10. Inserts: input-sec→3, idempotency→47,
   latency→77, state→84.
3. **Per chapter (ch01–05):** insert new essay(s) at importance position; remove
   retired essay(s), folding their clause into the sibling rule's bold statement +
   a sentence; renumber `## Rule N:` headings; reorder + renumber the chapter card.
4. **Appendix D** (`book/99-back-matter.md`): regenerate the book↔RULES.md mapping
   table; re-sort the rule index.
5. **Cross-reference sweep:** `grep -nE '\b[Rr]ules? [0-9]'` across `book/*.md` +
   `RULES.md`; resolve each to the new number; rewrite opener prose that narrates
   contiguous runs (Ch3 "movements", Ch4 framing).
6. **Mermaid:** Ch4 scan-gate map edge labels cite rule numbers — update.

## Regression checks (all green before the closing commit)

- `grep -h '^## Rule' book/ch0*.md` → exactly 1–100 in order (21/19/19/21/20 per file).
- Each chapter card: N entries matching that chapter's headings in order.
- Appendix D: both columns are permutations of 1–100; spot-checks agree.
- Every `[Rr]ule N` reference resolves to the intended rule.
- Book↔repo: each rule's `RULES.md` one-liner and the book's bold statement match.
- EPUB/PDF build green (blocked on pandoc + mermaid-cli per F1 — structural checks
  stand in until tooling lands).
