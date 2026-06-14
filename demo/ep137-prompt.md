# Episode 137 — "One source of truth, vs. just talk to me straight"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 63 — *SemVer; one canonical home* (score 56.5)
- BAD:  Rule 100 — *Verbatim errors; diffs; asks* (score 54.0)

---

## 0:00 — The hook
[CARD: "56.5  vs  54.0"]

Two rules, two and a half points apart — practically neighbors on the board. But one
is a hard mechanical law a machine can enforce, and the other is mostly me asking to
be talked to like an adult. Watch how that gap shows up in the grade.

## 0:20 — The good one
[CARD: "Rule 63 · SemVer; one canonical home · 56.5"]

"Semantic versioning, with the version in exactly one canonical place — everything else
reads from it."

It scores a mid-fifties because it's genuinely useful and genuinely enforceable, but
it isn't life-or-death. On pertinence it's solid — every project has a version, and
SemVer is the lingua franca, so the rule speaks to everyone. Where it really earns its
points is architectural simplicity: one canonical home means no drift, no "which file
is right," no two-places-out-of-sync bug at release time. And it's enforceable — a
build can read that one source and fail if anything disagrees. It loses points on
security and cost-of-getting-it-wrong: botch your version numbering and you've got a
confusing release, not a breached company. Useful, checkable, low drama.

## 1:10 — The bad one
[CARD: "Rule 100 · Verbatim errors; diffs; asks · 54.0"]

Now the one right below it. "Quote errors verbatim, never paraphrase stack traces;
show diffs, not prose, when the question is 'what changed?'; surface assumptions
explicitly."

Fifty-four. And here's the honest diagnosis: it's three good habits bundled into one
rule, and none of them is mechanically checkable. It's a workflow preference — how I
want an assistant to communicate with me — not a property of the code you can scan
for. Low on enforceability, because nothing fails a build when someone paraphrases a
stack trace. Lighter on generality, too — it reads as me telling my pair-programmer
how to behave, so it's a bit persona-specific. It's not wrong; paraphrased errors and
hand-wavy "I changed some stuff" genuinely waste my time. It just can't be policed the
way the version rule can.

## 2:00 — The lesson
[CARD: "can a machine check it?"]

Two points apart, but they live in different worlds. Rule 63 is a fact about the
codebase — one home for the version, and a build can prove it. Rule 100 is a request
about behavior — quote it straight, show the diff, say your assumptions. Both make the
work better. But the rule a machine can enforce will always grade above the rule that
only works if someone chooses to honor it.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 63 and 100).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
