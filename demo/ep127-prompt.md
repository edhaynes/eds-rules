# Episode 127 — "Plan it tight, or just keep climbing"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 98 — *Plan first; size for 90%* (score 59.0)
- BAD:  Rule 62 — *Versions only move forward* (score 50.5)

---

## 0:00 — The hook
[CARD: "59.0  vs  50.5"]

Two rules, nine points apart. One tells you how to set up the work so the AI actually
lands it. The other tells you how to number what you ship. Both made the list — but
only one of them earns its keep on every project I touch. Here's the gap.

## 0:20 — The good one
[CARD: "Rule 98 · Plan first; size for 90% · 59.0"]

"Plan first for non-trivial work: state the approach and the files to be touched before
editing. Size the work so the AI nails it first try 90% of the time — any step with more
than a 10% chance of first-try failure gets broken into smaller, mechanical,
independently-verifiable sub-steps. Never silently change scope — if the task is bigger
than stated, stop and say so."

Fifty-nine, and the engine behind it is generality — a nine. This rule doesn't care
what you're building. Any task, any language, any AI, any human: plan before you touch
files, and chunk the work small enough that it lands first try. That's why it scores
high on pertinence too — it's the single biggest lever on whether a session produces
working code or a pile of rework. Cost-effectiveness is a seven because the plan is
cheap and the rework it prevents is not. Where it gives back points is enforceability —
a three. "Size it for 90%" is judgment, not a check you can fail in a hook. You can't
automate good scoping. But a rule this universal earns its slot even with a soft edge.

## 1:10 — The bad one
[CARD: "Rule 62 · Versions only move forward · 50.5"]

Now the one that scored lower. "Bump on every release; versions only move forward. Roll
back by rolling forward to a new patch."

Fifty and a half. And it's not wrong — I stand by it. Monotonic versions, no re-tagging,
roll back by rolling forward: that's sound discipline, and it's actually enforceable, a
six, you really can block a backwards bump. Where it loses is pertinence and generality.
It's a four on pertinence because it's a convention, not a safety rail — break it and
nothing burns, you just confuse a deploy. And it leans on my specific scheme: auto-bump
on release, the odd/even cadence, the tagging flow. Strip my setup away and "versions
go forward" is something most teams already get for free from their tooling. It's a good
habit that's mostly already solved — and a rule that's already solved doesn't fight for
its slot.

## 2:00 — The lesson
[CARD: "shapes the work  vs  labels the work"]

That's the split a grade exposes. Rule 98 changes how every piece of work gets *done* —
that's why it scores. Rule 62 changes how the work gets *numbered* after the fact —
useful, enforceable, but downstream of where the value is. The rules that earn the top
of the list shape the work itself. The ones near the bottom are good manners around the
edges.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 98 and 62).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Rule 98: pertinence 7, security 2, cost-eff 7, arch-simpl 6, enforce 3, generality 9 → 59.0.
- Rule 62: pertinence 4, security 3, cost-eff 7, arch-simpl 4, enforce 6, generality 8 → 50.5.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
