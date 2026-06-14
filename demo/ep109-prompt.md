# Episode 109 — "The safety net and the wish list"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 5 — *Autonomy bounded by VC* (score 63.0)
- BAD:  Rule 39 — *Three platforms; two in CI* (score 46.0)

---

## 0:00 — The hook
[CARD: "63.0  vs  46.0"]

Two rules off the same list, seventeen points apart. One sets the exact line where I'll
let an agent run unattended. The other tells me where my code should run. Both are real —
but only one of them earns its keep on every project. Here's the gap.

## 0:20 — The good one
[CARD: "Rule 5 · Autonomy bounded by VC · 63.0"]

"Agent autonomy is bounded by version control: an agent only writes inside a git repo
with a synced remote. No recoverable history, no autonomy."

It scores a sixty-three because it's the rule that makes every *other* risky thing safe.
The moment an agent can write files unattended, the only thing standing between you and a
wiped working tree is recoverable history. Pin autonomy to a synced remote and the worst
case is a `git reset` — not a lost afternoon. It's high on architectural simplicity:
it's one bright line, no exceptions to remember. It's enforceable — you can check for a
remote before you ever grant the keys. And it generalizes to anyone running an agent at
all. The reason it's sixty-three and not ninety is it's a precondition, not a daily
practice — you set it once and it just holds.

## 1:10 — The bad one
[CARD: "Rule 39 · Three platforms; two in CI · 46.0"]

Now the softer one. "Target macOS, Linux, and Windows; CI covers at least two of them."

Forty-six. And it's not wrong — cross-platform matters, and CI catching two of three is
honest about the cost. But look at what drags it down. It's narrow: plenty of code only
ever runs in one place — a Linux container, a single deploy target — and for that work
this rule is just noise. It bakes in a specific number, *two of three*, which reads more
like my preference than a law. And it's weak on enforceability for an agent — it's a goal
you architect toward, not a tripwire that fires the moment someone crosses it. Pertinent
when it's pertinent; a footnote when it isn't.

## 2:00 — The lesson
[CARD: "a line you can check beats a goal you aim at"]

That's what the grade exposes. The strong rule draws a line a machine can verify before
it acts — remote or no remote, autonomy or not. The weak one names a target you steer
toward, with a number that fits my projects more than everyone's. Universal precondition
beats situational aspiration. That's the seventeen points.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 5 and 39).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
