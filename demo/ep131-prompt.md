# Episode 131 — "Don't reinvent it; do define it first"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 30 — *Search open source first* (score 57.5)
- BAD:  Rule 71 — *Contract first; code second* (score 52.0)

---

## 0:00 — The hook
[CARD: "57.5  vs  52.0"]

Two rules from the middle of the pack today, separated by five and a half points. One
tells you to go *find* what already exists before you write a line. The other tells you
to *define* the thing precisely before you build it. Both are good advice — here's why
the grader liked one more.

## 0:20 — The good one
[CARD: "Rule 30 · Search open source first · 57.5"]

Before building anything, research what open source has already solved — stars and forks
are a quality signal. Check the codebase for something to adapt before inventing.

It scores in the high fifties because it's universal and it's cheap. Every project,
every language, every stack — the question "has someone already solved this?" always
pays. It scores well on pertinence and cost-effectiveness: the search costs minutes, the
code you don't write costs nothing to maintain. And it leans on architectural simplicity
— a vetted, high-star dependency is usually a cleaner seam than the thing you'd have
hand-rolled. Where it loses points is enforceability: no tool can prove you *looked*. But
as a default instinct, it's one of the most generally useful rules on the board.

## 1:10 — The bad one
[CARD: "Rule 71 · Contract first; code second · 52.0"]

Now the one just below it. "Contract first: define and freeze the API or interface, write
the tests against the contract, then implement. Never the reverse."

Fifty-two. And it's a *good* discipline — I stand behind it. So why the dip? Two reasons.
It's narrower than it looks: "freeze the contract first" is gold for an API or a service
boundary, but most of the code anyone writes isn't crossing a contract — it's internal,
exploratory, where freezing too early is its own mistake. So generality takes a hit. And
it's hard to enforce: you can check that tests exist, but you can't check that the
contract came *first*, in that order. Pertinence is high, the order discipline is real —
but "never the reverse" is more aspiration than something a tool can hold you to.

## 2:00 — The lesson
[CARD: "always-useful beats sometimes-right"]

That's the gap a grade exposes. "Search first" wins anywhere, every time, for cents.
"Contract first" is sharper advice — but only at the boundaries, and only if you actually
keep the order. The broadly-useful, cheap-to-follow rule edges out the precise one that
applies in fewer places and can't be checked. Both belong on the list; one just earns
its slot a little more easily.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 30 and 71).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
