# Episode 114 — "Name the number, name the default"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 26 — *No magic numbers* (score 61.5)
- BAD:  Rule 24 — *Local default; not hardcoded* (score 47.0)

---

## 0:00 — The hook
[CARD: "61.5  vs  47.0"]

Two rules about not hardcoding things. Both feel like the same lesson. But one scored
a sixty-one and the other a forty-seven. Same idea, fifteen points apart — and the gap
tells you exactly what makes a rule worth keeping.

## 0:20 — The good one
[CARD: "Rule 26 · No magic numbers · 61.5"]

No magic numbers — named constants or config entries only.

It scores in the sixties because it's universal and it's checkable. Every language,
every codebase, every developer hits this — a bare `30` or `0.85` buried in the logic
that nobody can explain six months later. Naming it costs one line and pays you back
every time someone reads the code. It scores high on pertinence and generality because
it applies everywhere, and high on enforceability because a linter can flag a literal
the moment it lands. Cheap to follow, easy to verify, helps every project. That's a
real rule.

## 1:10 — The bad one
[CARD: "Rule 24 · Local default; not hardcoded · 47.0"]

Now the one that came up short. "Use X locally" means configurable with X as the
default, never hardcoded.

Forty-seven. And the diagnosis is honest: it's the right instinct wearing a confusing
costume. The core idea — wire the default through config, don't bake it in — is good.
But the rule is phrased around a specific habit of mine, "use X locally," instead of a
general principle. That hurts it on generality: a reader who never says "go local"
isn't sure it's talking to them. And it overlaps the cleaner config rules already on
the list, so it pulls duplicate weight. It's also softer to enforce — there's no linter
that catches "you made the default rigid instead of swappable." Good idea, narrow
framing, fuzzy enforcement. That's how you land in the forties.

## 2:00 — The lesson
[CARD: "a principle beats a habit"]

That's the spread. Rule 26 states a principle anyone can apply and a machine can check.
Rule 24 states *my* habit and hopes you generalize it. Same family — don't hardcode —
but the one phrased as a universal law graded higher than the one phrased as a personal
preference. When you write a rule, name the principle, not your routine.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 26 and 24).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
