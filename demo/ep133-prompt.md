# Episode 133 — "Use the OS, not a guess — and the 100% that isn't"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 41 — *No hardcoded temp/home/drive* (score 57.5)
- BAD:  Rule 72 — *100% line + branch coverage* (score 52.5)

---

## 0:00 — The hook
[CARD: "57.5  vs  52.5"]

Two rules, five points apart. One tells you to stop guessing where the operating
system keeps its files. The other tells you to test every single branch — all of it,
no exceptions. Both sound sensible. Only one earns its slot cleanly. Here's why.

## 0:20 — The good one
[CARD: "Rule 41 · No hardcoded temp/home/drive · 57.5"]

No hardcoded `/tmp`, `~/`, or drive letters — use platform temp/home APIs.

It scores in the high fifties because it's quietly universal. Every language gives you
a real API for the temp directory and the home directory, and the moment you type the
literal path instead, you've shipped a bug that hides until someone runs your code on
a different OS. It's pertinent — it bites in real life. It's cheap — the right call is
one function instead of one string. It's architecturally clean — you're deferring to
the platform instead of pretending you know its layout. And it's general: it applies
to anyone shipping cross-platform anything. The only reason it's not higher is
enforceability — a linter catches the obvious cases, but a creatively wrong path can
still slip through.

## 1:10 — The bad one
[CARD: "Rule 72 · 100% line + branch coverage · 52.5"]

Now the one I have to be honest about. "100% line *and* branch coverage — every branch
exercised and asserted. Yes, 100%; configure the runner to fail under it."

Fifty-two. And I stand behind the discipline — but I get the grade. The problem isn't
that it's wrong, it's that the number is absolute and the world isn't. One hundred
percent is expensive to reach and expensive to hold; the last few percent often buys
you tests that assert nothing real just to color a line green. It scores soft on
cost-effectiveness because the payoff curve flattens hard near the top, and soft on
generality because plenty of solid shops ship at eighty-five and are right to. It
reads less like a universal law and more like *my* bar for code people depend on —
and a personal bar, however good, isn't a hundred-rule rule.

## 2:00 — The lesson
[CARD: "defer to the platform  >  decree a number"]

That's the split a grade exposes. The strong rule says "don't pretend you know what the
OS knows" — humble, cheap, true everywhere. The weak one decrees a number and dares
reality to comply. Rules that defer to something real age well. Rules that legislate an
absolute have to keep defending the absolute — and that's exactly the work a grade makes
visible.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 41 and 72).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
