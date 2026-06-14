# Episode 135 — "Clean up first, or search first?"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 89 — *Dead-code pass after features* (score 57.5)
- BAD:  Rule 16 — *Claude searches before building* (score 53.0)

---

## 0:00 — The hook
[CARD: "57.5  vs  53.0"]

Two rules, four and a half points apart, and they pull in opposite directions. One
says clean the house before you build a new room. The other says go shopping before
you build anything at all. Both made the list — only one earned its grade.

## 0:20 — The good one
[CARD: "Rule 89 · Dead-code pass after features · 57.5"]

After a stable release, the first task is a cleanup sweep — before any new feature.

It scores in the high fifties because it's pertinent and it's enforceable. Right after
you ship, the cruft is at its peak — dead branches, half-finished experiments, files
nobody owns anymore — and you've got the one moment where touching them is safe,
because the release is already out the door. The cost is near zero: you're not
building, you're deleting. Architecturally it keeps the codebase honest, and it's easy
to enforce — it's a checklist item, not a judgment call. Where it loses points is
security, which it barely touches, and generality — "stable release" is a cadence not
every shop runs. Solid, useful, a little situational.

## 1:10 — The bad one
[CARD: "Rule 16 · Claude searches before building · 53.0"]

Now the one just below it. "Claude, the backend developer, is slow and methodical.
Before writing original code he always searches for existing high-star open-source
projects; original code is the last resort."

Fifty-three. And the instinct behind it is dead right — don't reinvent what a
ten-thousand-star library already does. But look at how it's written. It names a
persona, *Claude the backend developer*, which means it only fires if you've built my
crew. Strip the name and what's left — "search before you build" — is good advice but
soft: there's no clean done-signal, no way to check whether the search actually
happened. It scores low on enforceability and low on generality for exactly that
reason. Good principle, wrapped in a rule that's hard to hold anyone to.

## 2:00 — The lesson
[CARD: "a principle isn't a rule until you can check it"]

That's the gap the grade exposes. The cleanup rule wins because it's a thing you can
*verify happened*. The search rule lags because it's an attitude dressed as a law —
right in spirit, fuzzy in practice, and tangled up in one persona's name. Same
distance on the board, opposite lessons: write the rule so you can tell when it was
broken, and don't bind a universal idea to a setup only you have.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 89 and 16).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
