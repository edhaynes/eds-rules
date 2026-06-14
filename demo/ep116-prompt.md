# Episode 116 — "A rule you can count, and a rule you can only nod at"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 75 — *Full regression; with numbers* (score 61.5)
- BAD:  Rule 28 — *Architecture beats language* (score 47.5)

---

## 0:00 — The hook
[CARD: "61.5  vs  47.5"]

Today's pair is a trap. One of these rules sounds boring and one sounds profound — and
the boring one scored higher. That's not an accident. The difference is whether a
machine can tell if you followed it.

## 0:20 — The good one
[CARD: "Rule 75 · Full regression; with numbers · 61.5"]

Run the full regression suite after every feature; report the test count and any failures.

Sixty-one and a half, and the reason is in the second half of that sentence: *report the
count.* "I ran the tests" is a claim. "I ran 412 tests, zero failures" is a fact you can
check. It scores high on generality — every project that ships code has a suite to run —
and high on enforceability, because a number is a thing an agent can be made to produce
and a human can audit. The cost is small, the catch rate is real, and it leaves a paper
trail. That's a working rule.

## 1:10 — The bad one
[CARD: "Rule 28 · Architecture beats language · 47.5"]

Now the one that sounds wiser. "Architecture matters more than language or framework."

Forty-seven and a half. And here's the thing — I *believe* this one. It's true, it's
general, and it scored a nine on simplicity because it's one clean idea. But look at what
it can't do: it scored a *one* on enforceability. There's no check for it. No agent can
run it, no diff can prove it, no commit gate can fail on "your architecture is bad." It's
a value, not a rule — the kind of thing you put on a wall, not in a pipeline. It also
scored a one on security, because it doesn't guard against anything that bites you. It's
wisdom. It's just not actionable wisdom.

## 2:00 — The lesson
[CARD: "a rule you can measure beats a rule you can only admire"]

That's the split a grade exposes. A rule earns its slot when something can *check* it —
a number, a scan, a gate that fails. The profound one-liner that nobody can enforce
drifts to the bottom, no matter how true it is. Truth is necessary. Measurable is what
makes it a rule.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 75 and 28).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Rule 75 (61.5): high on generality (9) and enforceability (7) — a reportable number.
  Rule 28 (47.5): high simplicity (8) and generality (9) but bottomed out on
  enforceability (1) and security (1) — a value, not a checkable rule.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
