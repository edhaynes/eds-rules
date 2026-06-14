# Episode 128 — "The one you can hand to a stranger, and the one you have to argue"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 27 — *Ship the .env.example* (score 58.0)
- BAD:  Rule 38 — *Shallow nesting* (score 51.0)

---

## 0:00 — The hook
[CARD: "58.0  vs  51.0"]

Two rules, seven points apart. One tells you to hand the next person a map. The other
tells you to stop burying your code three layers deep. Both are good advice — but only
one of them holds up the second you try to enforce it.

## 0:20 — The good one
[CARD: "Rule 27 · Ship the .env.example · 58.0"]

Ship a `.env.example` documenting every required variable; gitignore the real `.env`.

Fifty-eight, and it earns it on almost every dimension. Pertinence: every project with
config needs this, full stop. Security: it's the rule that lets you commit *what* you
need without ever committing the *values* — the example file is the inventory, the real
`.env` stays out of git. Cost-effectiveness is the killer — it's one file, written
once, and it saves every future contributor from guessing which six variables make the
thing boot. Architecturally it's trivial, and it's enforceable: the file either exists
and lists the keys, or it doesn't. Where it loses a few points is generality — it
assumes a `.env`-style config layer, which not every stack uses. But when it applies,
it's pure profit.

## 1:10 — The bad one
[CARD: "Rule 38 · Shallow nesting · 51.0"]

Now the softer half. "More than ~3 levels of nesting → extract."

Fifty-one. And it's *right* — deep nesting is where bugs hide and readers give up. So
why does it score lower? Because it's advice dressed as a law. That "~3" is a feel, not
a line — sometimes four levels is the honest shape of the problem, and a forced extract
makes it worse. It's hard to enforce cleanly: a linter can count braces, but it can't
tell you whether the extraction actually helped. And it overlaps with a half-dozen other
"keep it readable" rules, so it carries less weight on its own. Good instinct, fuzzy
edge — that's a fifty-one.

## 2:00 — The lesson
[CARD: "a checkable fact beats a good feeling"]

That's the gap the grade exposes. The strong rule is a thing you can *verify* — the file
exists or it doesn't. The weak rule is a thing you have to *judge* — three levels or
four, extract or leave it. Both make better software. But a rule you can check on its own
earns its slot; a rule you have to argue every time is really a guideline wearing a
number.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 27 and 38).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
