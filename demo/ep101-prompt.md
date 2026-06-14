# Episode 101 — "Gates that never blink, and rules carved in stone"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 46 — *Pre-deploy gates never off* (score 66.5)
- BAD:  Rule 96 — *ADRs are immutable* (score 44.0)

---

## 0:00 — The hook
[CARD: "66.5  vs  44.0"]

Every rule I have got graded. Today: one that guards the door on every deploy — and
one that asks you to carve your decisions in stone and never touch them again. Both
made the list. Only one of them earns its keep everywhere. Here's the split.

## 0:20 — The good one
[CARD: "Rule 46 · Pre-deploy gates never off · 66.5"]

Pre-deploy gates — smoke test, vulnerability scan, secret scan — are never disabled by
default. Escape hatches are explicit, one-off, and logged.

It scores in the sixties because it's the rule that keeps a bad build from reaching
production. The gates are cheap to run and brutal to skip — a missed scan or a broken
smoke test is exactly the thing that bites you at deploy time, the worst possible
moment. It's strong on security and on cost-effectiveness: small standing cost, big
downside avoided. The "explicit, one-off, logged" clause is what makes it
enforceable — you can override, but you can't override *quietly*. It loses a few
points on architectural simplicity, because a real gate setup is plumbing you have to
build and maintain, not a one-liner. But it's general — every project that ships
anything has a deploy step worth guarding.

## 1:10 — The bad one
[CARD: "Rule 96 · ADRs are immutable · 44.0"]

Now the soft middle of the board. "Non-obvious decisions go in numbered ADRs —
immutable after acceptance; a later ADR supersedes, never edits."

Forty-four. And it's not wrong — it's a genuinely good discipline. It just scores
narrow. The whole rule only means anything if you've already bought into ADRs as a
practice, and plenty of solid teams never write one. So it leans low on generality.
It's also hard to enforce: nothing stops someone editing an accepted ADR in place
except habit and a code review that happens to care — there's no scan, no gate, no
loud failure when it's broken. Compare it to Rule 46, where the override is logged.
Here, a quiet edit leaves no trace. Good practice, weak as a *law*.

## 2:00 — The lesson
[CARD: "enforceable × general"]

That's what the grade exposes. The strong rule has teeth — it runs on every deploy and
it screams when you skip it. The weak one is a good habit that depends on everyone
choosing to keep it. A rule earns a slot when it's both broadly useful *and* hard to
violate without noticing. Discipline you have to remember isn't as safe as a gate that
won't let you through.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 46 and 96).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
