# Episode 132 — "Keep it small vs the key you can't take back"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 37 — *Small functions; few params* (score 57.5)
- BAD:  Rule 52 — *A touched secret is burned* (score 52.0)

---

## 0:00 — The hook
[CARD: "57.5  vs  52.0"]

Two rules, five and a half points apart, both from the middle of my list. One tells you
how to shape a function. The other tells you what to do when you've already lost a
secret. Close scores — but they're weak for completely different reasons, and that's the
lesson.

## 0:20 — The good one
[CARD: "Rule 37 · Small functions; few params · 57.5"]

Functions target ≤50 lines and ≤5 parameters — refactor instead of stretching.

Fifty-seven. Solidly above the middle, and it earns it on simplicity and generality:
this is true in every language, every codebase, every decade. A short function with few
parameters is easier to read, test, and reason about — that's architectural simplicity
baked straight into a rule. It's pertinent everywhere and costs nothing to follow. Where
it loses points is enforceability and security — the numbers are a bit arbitrary, a
linter can nag but can't really make you obey, and it has nothing to do with keeping you
safe. Good rule, not a great one.

## 1:10 — The bad one
[CARD: "Rule 52 · A touched secret is burned · 52.0"]

Now five points down. "A secret that ever touched a commit is burned. Rotate first,
clean history second — pushed objects outlive deletion."

Fifty-two. And it stings, because this one is *dead right* — I've watched a key go
public seconds after a commit. So why's it middling? Because it's not really a rule you
*follow*, it's a procedure you run *after* you've already broken a different rule. It's
narrow — it only fires in the cleanup of a leak — and an AI can't proactively obey it
the way it can obey "scan before you push." Low on generality, hard to enforce up front.
The content is gold; the *shape* of it scores like a footnote.

## 2:00 — The lesson
[CARD: "a rule you follow beats a rule you invoke"]

That's what the grade exposes. Rule 37 is mediocre because it's soft — easy to ignore,
nothing at stake. Rule 52 is mediocre because it's reactive — it's the right move only
once you're already cleaning up a mess. The best rules sit in front of the mistake and
apply everywhere. Be useful before the damage, not just after it.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 37 and 52).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
