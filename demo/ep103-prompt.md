# Episode 103 — "Write the test first, or write the commit alone"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 70 — *Tests with logic; regress first* (score 65.0)
- BAD:  Rule 36 — *Size refactors are own commits* (score 44.0)

---

## 0:00 — The hook
[CARD: "65.0  vs  44.0"]

Two rules about discipline. One tells you how to keep code from breaking; the other
tells you how to keep a diff readable. Both good habits — but the grades say one is a
law and the other is just nice manners. Here's the twenty-one-point gap.

## 0:20 — The good one
[CARD: "Rule 70 · Tests with logic; regress first · 65.0"]

"New logic ships with tests; bug fixes ship with a regression test written
failing-first, before the fix."

Sixty-five, and it earns it. This one's pertinent everywhere — every project, every
language, every team has logic and has bugs. Writing the regression test *first*, so
you watch it fail before you make it pass, is the cheapest insurance there is: you
prove the test actually catches the bug instead of hoping it does. It's
architecturally simple — no framework, no ceremony, just "no new behavior without a
test that pins it." And it's enforceable: coverage gates and CI make it mechanical.
Cost to follow is minutes; cost to skip is the same bug coming back next quarter with
nobody watching. High generality, real teeth.

## 1:10 — The bad one
[CARD: "Rule 36 · Size refactors are own commits · 44.0"]

Now the softer one. "Size refactors are separate, mechanical commits so the diff is
reviewable."

Forty-four. And it's right — I believe it. When you reformat or restructure for size,
do it in its own commit so the reviewer isn't hunting a logic change buried in two
hundred lines of moved braces. Good practice. But look at what drags the grade down:
it's narrow. It only fires when you're specifically doing a *size* refactor, which is
a slice of a slice of the work. It's hard to enforce — there's no gate that knows a
commit "should have been split," it lives entirely on reviewer goodwill. And the
downside of breaking it is mild: a messier diff, not a broken build or a leaked key.
Low cost to violate means low urgency, and a hundred-rule list rewards urgency.

## 2:00 — The lesson
[CARD: "catches bugs > cleans diffs"]

That's the gap. The strong rule protects the *code* — it stops defects cold and a
machine can enforce it. The weak rule protects the *review* — it's courtesy, it
depends on a human remembering, and breaking it costs you a squint, not a fire. Both
belong in a good workflow. Only one belongs near the top of the list.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 70 and 36).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
