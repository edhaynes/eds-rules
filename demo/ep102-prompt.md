# Episode 102 — "The diff you read, and the flag you forgot"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 56 — *Inspect config-file diffs* (score 65.5)
- BAD:  Rule 68 — *Push tags by name* (score 44.0)

---

## 0:00 — The hook
[CARD: "65.5  vs  44.0"]

Every rule I have got graded. Today: a habit that catches the leak nobody looks for —
and a one-liner that's right, but barely earns its slot. Same list. One's a discipline,
one's a footnote. Here's the gap a grade exposes.

## 0:20 — The good one
[CARD: "Rule 56 · Inspect config-file diffs · 65.5"]

Before committing, inspect the staged diff of every config-shaped file (yaml, json,
toml, env, anything under infra/deploy dirs) — leaks hide best in "harmless" config.

Sixty-five and a half, and it earns every point. It's high on pertinence and security:
a leaked key almost never lands in your application code — it lands in a values.yaml, an
env file, a Terraform var that nobody reads because it "looks like config." Cost-
effectiveness is great — reading a diff is free, the leak is forever. It's general:
every project has config files, every agent stages them. Architecturally it's just a
habit, no machinery. The one thing holding it back from the top tier is enforceability —
"inspect" is a human verb. You can scan, but "actually look at it" is hard to automate.
That's the only ceiling on it.

## 1:10 — The bad one
[CARD: "Rule 68 · Push tags by name · 44.0"]

Now down the board. "Push tags by name, never `--tags` reflexively."

Forty-four. And it's not wrong — it's just narrow. The reason it exists is real: a
mistyped or rewritten local tag can clobber a tag on the remote that something depends
on, and `git push --tags` fires every one of them at once. But look at the dimensions.
Generality's low — most projects barely use tags, and the ones that do don't trip on
this often. It's a single git mechanic, not a principle. And the cost of getting it
wrong is recoverable in a way a leaked secret never is. It's a good habit hiding inside
a bigger rule about treating tags as immutable — on its own, it's a footnote, not a law.

## 2:00 — The lesson
[CARD: "a habit that scales vs a habit that's local"]

That's the split a grade exposes. The strong rule applies to every file in every repo
and guards against the worst thing that can happen. The weak one guards against a narrow
slip in one tool, recoverable, in projects that even use the feature. Both are good
advice. Only one is a hundred-rule rule — and the grade is how the other earns its way
*off* the list when something more universal needs the slot.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 56 and 68).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
