# Episode 125 — "A logger you'll thank yourself for, and a ratchet that slips"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 80 — *A logger; never print* (score 59.5)
- BAD:  Rule 74 — *Coverage never goes down* (score 50.5)

---

## 0:00 — The hook
[CARD: "59.5  vs  50.5"]

Two rules from the same list, nine points apart. One tells you to stop printing and
start logging. The other tells you your test coverage can never slip. Both sound
sensible. Here's why one earns its slot clean and the other only just hangs on.

## 0:20 — The good one
[CARD: "Rule 80 · A logger; never print · 59.5"]

Use a logger, never `print`, in shipped code; log level configurable, and structured (JSON) once the project outgrows a script.

It scores a fifty-nine because it's universal and it's cheap. Every language has a
logger, every project ships logs, and the day you're debugging something live, a
`print` you can't switch off or filter is useless — a logger with a level and a JSON
shape is the difference between grep-able answers and noise. Architecturally it's
simple: one sink, one config knob. It scores well on pertinence and generality
because it bites on every project, and well on cost-effectiveness because the fix is
trivial and the payoff is every incident you'll ever debug. Where it gives up points
is enforceability — a linter can flag `print`, but "structured once it outgrows a
script" is a judgment call, not a gate.

## 1:10 — The bad one
[CARD: "Rule 74 · Coverage never goes down · 50.5"]

Now the one that slips. "Coverage going down is a stop-and-fix, not a 'justify it.'"

Fifty and a half. And honestly? Fair. The intent is gold — a coverage ratchet keeps
a suite from quietly rotting. But the rule as written is a fragment of a bigger one,
and that costs it. It only means something if you've already got coverage measured,
a target set, and CI wired to fail on a drop — without that scaffolding it's an
aspiration, not a law. It scores soft on enforceability, because "stop-and-fix"
depends entirely on tooling someone else has to stand up first, and soft on
architectural simplicity, because a hard "never down" ratchet fights you on the day
you legitimately delete tested code. It's not wrong — it's just narrower and more
situational than its eighty-percent neighbour.

## 2:00 — The lesson
[CARD: "a rule has to bite on its own"]

That's the gap a grade exposes. The strong rule works the moment you read it — swap
`print` for a logger, done. The weaker one needs a whole rig standing behind it
before it does anything, and it punishes the honest case where coverage *should*
move. The best rules carry their own teeth. The ones that lean on setup you haven't
built yet earn the lower score — and that's exactly how the list keeps the ones that
pull their weight.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 80 and 74).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
