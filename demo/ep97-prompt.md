# Episode 97 — "One rule guards the disaster, one tidies after it"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 4 — *Destruction needs a human* (score 71.5)
- BAD:  Rule 90 — *Cleanup sweep after release* (score 41.5)

---

## 0:00 — The hook
[CARD: "71.5  vs  41.5"]

Two rules from the same list, thirty points apart. One stands between me and a wiped
database. The other just keeps the house tidy. Both are good advice — but the grade
knows which one I can't live without.

## 0:20 — The good one
[CARD: "Rule 4 · Destruction needs a human · 71.5"]

Never delete files, drop tables, run destructive shell commands, force-push, or rewrite
history without explicit human confirmation.

Seventy-one and a half, and it earns it where it counts. Security and
cost-effectiveness both score high because this is the rule that turns a catastrophic,
irreversible mistake into a two-second pause. An agent moving fast will absolutely
`rm -rf` the wrong path or force-push over a week of work — generality scores a ten,
because *every* setup has something destructible. The one soft spot is architectural
simplicity: "destructive" is a judgment call, so the line between confirm and proceed
needs care. But pertinence is high and the downside is total. This is a guardrail at
the edge of a cliff.

## 1:10 — The bad one
[CARD: "Rule 90 · Cleanup sweep after release · 41.5"]

Now the lower end. "After a stable release, the first task is a cleanup sweep — before
any new feature."

Forty-one. And it's not wrong — it's good hygiene, genuinely. The problem is it barely
defends against anything. Security scores a one, because skipping a cleanup never *hurt*
anyone; it just leaves clutter. Enforceability scores low too — what counts as "clean
enough" is fuzzy, and "before any new feature" is a habit an AI will quietly skip the
moment there's a feature it wants to build. It's a workflow preference dressed as a law:
useful in my cadence, optional everywhere else. That's a forty-one rule.

## 2:00 — The lesson
[CARD: "guard the irreversible, not the untidy"]

That's the line a grade draws. Rule 4 guards the thing you can never take back. Rule 90
tidies up after the thing already shipped fine. Both are habits worth keeping — but only
one is a rule the whole list would collapse without. When something better needs a slot,
the cleanup sweep is what makes room.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 4 "Destruction needs a human"; rule 90
  "Cleanup sweep after release" — the post-release cleanup line).
- Note: RULES.md and `quality/grades.csv` are off by one across the hygiene section —
  the CSV's rule 90 ("Cleanup sweep after release", 41.5) maps to the post-release
  cleanup sentence; the verbatim text above follows the CSV title/score pairing.
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
