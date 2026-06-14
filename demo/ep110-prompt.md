# Episode 110 — "The gate the robot trips, and the taste it can't fake"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 58 — *Pre-push rescan + tests* (score 63.0)
- BAD:  Rule 32 — *OO + SOLID where it earns* (score 46.0)

---

## 0:00 — The hook
[CARD: "63.0  vs  46.0"]

Every rule I have got graded. Today's pair is closer than usual — sixty-three against
forty-six. One tells a machine exactly what to do at a hard line. The other asks it to
have good taste. Watch which one the grade rewards.

## 0:20 — The good one
[CARD: "Rule 58 · Pre-push rescan + tests · 63.0"]

"Pre-push hooks rescan and run the tests."

Sixty-three, and it earns it on enforceability. This isn't advice — it's a gate. The
hook fires on every push, scans for secrets again, runs the suite, and refuses to let
broken or leaky code leave your machine. There's no judgment call, no "did I remember
to" — the machine remembers for you. It scores well on security and cost-effectiveness
because it catches the two cheapest-to-prevent, most-expensive-to-fix failures right at
the boundary. Where it loses points is generality: not every repo can run a full suite
on every push, so it's a strong rule, not a perfect one.

## 1:10 — The bad one
[CARD: "Rule 32 · OO + SOLID where it earns · 46.0"]

Now the softer one. "Default to object-oriented design with clear, single
responsibilities; prefer composition, use inheritance sparingly, and apply SOLID —
especially Single Responsibility and Dependency Inversion — where it earns its keep."

Forty-six. And it's not wrong — I believe every word of it. The problem is that phrase,
"where it earns its keep." That's a taste call, and taste doesn't enforce. A hook can
check for a leaked key; nothing can check whether you applied Single Responsibility
*wisely*. It scores low on enforceability and architectural simplicity because it's
really six principles wearing one number, and each one is a matter of degree, not a
yes/no. Good engineering — bad rule. Those aren't the same thing.

## 2:00 — The lesson
[CARD: "enforceable beats wise"]

That's the gap a grade exposes. A rule a machine can trip over is worth more on this
list than a rule a machine has to be wise to follow. SOLID is genuinely good practice —
it just can't be a line item the way a pre-push hook can. The best rules in a hundred
are the ones you can't accidentally skip. Wisdom belongs in the work; the list is for
the gates.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 58 and 32).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
