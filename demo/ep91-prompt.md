# Episode 91 — "The best rule I've got, and the worst"
Author: Jason-eds · Draft 1 · ~2.5 min · FORMAT SAMPLE for the 50-episode run

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 1 — *Secret scan before ship* (score 90.0, the #1 rule)
- BAD:  Rule 19 — *Go local rebinds the crew* (score 25.5, dead last)

---

## 0:00 — The hook
[CARD: "90.0  vs  25.5"]

Every rule I have got graded. Today: the one that scored highest — and the one that
scored dead last. Same list. Both earned their slot. Here's why one's gold and one's
barely hanging on.

## 0:20 — The good one
[CARD: "Rule 1 · Secret scan before ship · 90.0"]

Run a secret scan before every commit, every push, every deploy. No scan, no ship —
ever, any agent, any target.

It scores a ninety because it's the rule that, when you skip it once, can end a
company. A leaked key is public the instant it hits a hostable git ref — bots scrape
new commits in seconds. The scan is cheap; the leak is forever. That's the whole
calculus: tiny cost, catastrophic downside. Highest-value rule on the board.

## 1:10 — The bad one
[CARD: "Rule 19 · Go local rebinds the crew · 25.5"]

Now the basement of the leaderboard. "Go local rebinds every persona to its local
backend — same roles, same rules, different engine."

Twenty-five. And honestly? Fair. It's not *wrong* — it's just narrow. It only means
anything if you've built my exact five-persona crew with swappable model bindings.
For everyone else it's a footnote, not a law. It scores low on generality and on
"would an AI ever violate this unprompted" — the two things that make a rule earn a
slot in a list of a hundred.

## 2:00 — The lesson
[CARD: "generality × cost of getting it wrong"]

That's the difference a grade exposes. The best rules are universal and expensive to
break. The weak ones are situational. A rule that only helps in my setup isn't a
hundred-rule rule — and that grade is exactly how it earns its way *off* the list when
something better needs the slot.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 1 and 19).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
