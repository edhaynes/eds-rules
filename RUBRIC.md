# RUBRIC — *100 Rules for Writing My Software: The Red Hat Way*

Status: First draft, 2026-06-12

The quality bar (rule 76): **90 = working bar (solid A−), polish to 95, publish
only at 95+.** This rubric is how the book is graded against that bar. The
grade is taken cold — the grader reads as a paying reader, not as the author.

---

## 1. Who this book is for

**Primary reader: the newbie AI coder.** Hobbyists, career-switchers, founders,
PMs, and designers who can get an AI agent (Claude Code, Cursor, Copilot) to
produce a working demo — and then watch it collapse. They have little or no
formal engineering background. Their tools are a chat window and hope. They
don't need to be taught to code; they need the **discipline layer** that
47 years of shipping software distills into standing instructions an agent
will actually follow.

**Secondary readers:** experienced developers adopting agents who want a
ready-made ruleset to fork, and team leads looking for agent guardrails they
can drop into a repo.

**The promise of the book:** copy these rules into your repo, and the failure
modes that make AI coding miserable stop happening — not because you got
smarter, but because the agent is now bound by rules that encode the scars.

## 2. What they're frustrated by — and how the book answers

Evidence: Linda's sweep of r/cursor, r/ClaudeAI, HN, and vibe-coding
postmortems, 2026-06-12. Every top-ten frustration maps to chapters in the
draft:

| # | Frustration (typical phrasing) | Where the book answers |
|---|---|---|
| 1 | Hallucinated APIs/tools ("functions that don't exist") | Ch. 1 fail fast; tool-call discipline (rule 82); research-before-building |
| 2 | Lost/overwritten work ("the AI wiped my edits") | Ch. 1 push early and always; autonomy bounded by version control |
| 3 | Leaked API keys ("my key got committed") | Ch. 4 secret hygiene: hooks before first commit, scan gates, rotation protocol |
| 4 | Dependency hell ("it adds the latest of everything") | Ch. 3 pinned versions, lockfiles, dependency disclosure |
| 5 | Broken refactors ("clean diff, app won't start") | Ch. 4 green before commit; regression suite; Ch. 2 mechanical refactor commits |
| 6 | Misleading error handling ("it blames an error that isn't there") | Ch. 3 fail loudly; Ch. 5 quote errors verbatim |
| 7 | File-structure chaos ("duplicate modules everywhere") | Ch. 2 architecture, file-size ceilings, one purpose per file |
| 8 | "Done" but untested ("it swears it's tested; nothing passes") | Ch. 1 healthy before handover; Ch. 4 coverage and the quality bar |
| 9 | Merge-conflict misery | Ch. 1 small focused commits; the foreword's AI-merges-changed-the-economics argument |
| 10 | Works locally, breaks in CI/cloud | Ch. 2 config over hardcoding; Ch. 3 cross-platform primitives, deploy gates |

A revision that weakens any of these answers, or buries one where the
frustrated reader can't find it, is a regression.

## 3. Grading dimensions

Score each 0–100, weight, sum. Letter anchors: 95+ A (publish), 90–94 A−
(working bar), 80–89 B (real gaps), below 80 not presentable.

| Dimension | Weight | What 95+ looks like |
|---|---|---|
| **Audience fit** | 20% | A newbie with no engineering vocabulary can read any rule cold and act on it. Jargon is introduced before it's used or not used. Nothing assumes the reader knows git internals, CI, or containers before the book teaches them. |
| **Actionability** | 20% | Every rule delivers the triad: the statement, the *why* (a real scar), and what to actually do — ideally copy-pasteable. No rule is advice-shaped mush ("be careful with secrets"). |
| **Frustration coverage** | 15% | All ten frustrations in §2 are answered, findable from the table of contents, and the answer would actually have prevented the complained-about incident. |
| **Structural integrity** | 10% | The five chapters build in order; each opener's synopsis genuinely summarizes what the chapter stands on; book text never contradicts `RULES.md` (drift is a bug, filed on sight). |
| **Diagrams** | 10% | Every diagram earns its place, reads correctly printed B&W at 6"×9", and is understood faster than the paragraph it replaces. No color dependence, no decoration. |
| **Voice & honesty** | 10% | Direct, no flattery, no hedging. Scars are real and specific. The Red Hat disclaimer is unambiguous. Claims about what the rules prevent are ones the rules actually deliver. **The Reddit test (Eddie, 2026-06-12): a technical crowd sniffs out a fraud in two seconds — no overclaimed rigor ("proofs" stay pseudo-proofs), no borrowed authority, no credential inflation.** |
| **Production quality** | 10% | EPUB and print PDF build clean; front/back matter complete; Appendix D mapping table exact; no typos a paying reader would catch. |
| **Differentiation** | 5% | Says things the generic "prompt engineering tips" content does not — the personas, the Powell rule, the quality bar, the trust-boundary discipline are presented as the system they are. |

## 4. Grading protocol

- Grade **per chapter** and **whole book**; the book grade is not the average —
  a single failing chapter caps the book at that chapter's grade + 5.
- The grader leads with the bottom line ("this is a B+, here is why it is not
  an A"), gives the **single most damning specific example** per dimension
  (chapter and line), and closes with the **one change** that would move the
  grade most.
- Praise costs one sentence, then move on. The standing question: *would a
  paying reader feel cheated, bored, or condescended to here?*
- A grade below 90 sends the chapter back for revision. Nothing publishes
  below 95.
