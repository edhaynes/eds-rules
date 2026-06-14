# Episode 104 — "Catch it loud, or ship it slow"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 78 — *No swallowed exceptions* (score 64.5)
- BAD:  Rule 73 — *Correctness over speed* (score 44.5)

---

## 0:00 — The hook
[CARD: "64.5  vs  44.5"]

Two rules from the same list, twenty points apart. One tells you exactly what to do
and an AI can check it. The other is something I believe in my bones — and it still
landed near the bottom. Same author, same rubric. Here's why.

## 0:20 — The good one
[CARD: "Rule 78 · No swallowed exceptions · 64.5"]

"No bare `except:`/`catch (e)` swallows — catch specific exceptions, rethrow or log
with context."

Sixty-four and a half. It scores high because it's concrete and you can enforce it
with a linter — that's the enforceability and architectural-simplicity win. It's
pertinent everywhere: a swallowed exception is the bug that hides every other bug,
the silent failure that costs you a midnight debugging session because nothing ever
told you it broke. There's a quiet security angle too — a swallowed error is an
auth check that failed open and never said a word. And it's general: every language
with exceptions has this footgun, so the rule travels.

## 1:10 — The bad one
[CARD: "Rule 73 · Correctness over speed · 44.5"]

Now the one I'd defend in a bar fight. "Correctness over speed: the delay to reach
full coverage and verified behavior is acceptable and expected."

Forty-four and a half. And I get it. The problem isn't that it's wrong — it's that
it's a *value*, not an instruction. There's nothing to enforce. No linter flags
"you went too fast," no test catches "you traded correctness for velocity." It's a
priority I hold, not a check an AI can run. It also reads as personal — it's me
telling the crew which side to err on, which makes it feel narrow even though the
principle is universal. Concrete rules grade well; philosophies grade soft.

## 2:00 — The lesson
[CARD: "a check beats a creed"]

That's the gap a grade exposes. Rule 78 is a creed *and* a check — believe it, and a
machine can prove you kept it. Rule 73 is just the creed. Both matter. But on a list
of a hundred, the rules that earn their slot are the ones you can verify, not just
the ones you can preach.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 78 and 73).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
