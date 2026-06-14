# Episode 134 — "Crash early, fail gentle — and the rule that's just good manners"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 79 — *Loud dev; graceful prod* (score 57.5)
- BAD:  Rule 61 — *Tags are immutable* (score 53.0)

---

## 0:00 — The hook
[CARD: "57.5  vs  53.0"]

Every rule I have got graded. Today: a solid one about how your code should fail — and
one that's correct but barely earns its slot. Four and a half points apart. Both about
respecting the past, but only one of them changes how you write code tomorrow.

## 0:20 — The good one
[CARD: "Rule 79 · Loud dev; graceful prod · 57.5"]

Fail loudly in dev, gracefully in prod, diagnosably always.

It scores a fifty-seven because it captures a real tension in one line. In dev you
want the thing to blow up — loud, immediate, in your face — so you fix it now. In prod
you want it to degrade like an adult, not dump a stack trace at a user. But *always*
you keep enough context to diagnose. That's pertinent to literally every backend
anyone writes, it's architecturally simple, and it generalizes across every language
and runtime. Where it loses points is enforceability — "diagnosably" is judgment, not
a check you can fail in CI. Still, broad and right.

## 1:10 — The bad one
[CARD: "Rule 61 · Tags are immutable · 53.0"]

Now the one that scored lower. "Tags are immutable: never move, delete, or reuse a
pushed tag."

Fifty-three. And it's not wrong — it's just narrow. It's true, it matters, and the day
it bites you it really bites: someone pinned a container to `v1.2.0` and you moved the
tag underneath them. But it only applies in one corner — version tags in git — and
mostly it's already enforced for you by tooling and good habits. It scores fine on
pertinence and cost-of-getting-it-wrong, but it's low on generality and it barely
needs to be *said* to an AI that would rarely retag unprompted. It reads more like
good manners than a load-bearing law.

## 2:00 — The lesson
[CARD: "a rule about how you build > a rule about what not to touch"]

That's the gap the grade exposes. Rule 79 shapes every error path you'll ever write.
Rule 61 just tells you to leave one thing alone. Both are correct — but the one that
changes your behavior across the whole codebase outranks the one that protects a single
corner. Universal-and-shapes-your-work beats narrow-and-true, every time.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 79 and 61).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
