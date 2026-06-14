# Episode 136 — "Name your deps, or lose your decisions"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 10 — *Disclose every dependency* (score 56.5)
- BAD:  Rule 93 — *Persist decisions same commit* (score 53.5)

---

## 0:00 — The hook
[CARD: "56.5  vs  53.5"]

Two rules, three points apart. One tells you what to do before you add a dependency.
The other tells you what to do after you make a decision. Both are good hygiene — but
only one of them is a rule an AI would actually break on its own. That's the gap.

## 0:20 — The good one
[CARD: "Rule 10 · Disclose every dependency · 56.5"]

Never add a dependency without stating its name, purpose, license, maintenance status,
and platform support.

It scores in the mid-fifties because it's pertinent every single time and it catches
real damage cheaply. A dependency is the one line of code where you import someone
else's whole supply chain — license, maintenance, the question of whether it even
builds on your architecture. Stating those five things up front costs a sentence and
heads off the abandoned package, the GPL surprise, the dep with no ARM build that dies
on your box. It's general — it applies to any language, any stack — and it's
enforceable, because "did you name the license?" is a yes-or-no you can check. What
holds it back from the top tier is that it's prevention, not catastrophe: skip it and
you get pain later, not a dead company today.

## 1:10 — The bad one
[CARD: "Rule 93 · Persist decisions same commit · 53.5"]

A hair lower. "When a standing decision is made in chat, persist it — ADR, memory
file, rules doc — in the same commit. Chat history is not memory."

Fifty-three. And it's a *good* habit — I believe in it. So why does it grade below the
dependency rule? Two reasons the rubric exposes. First, enforceability: there's no
machine check for "was a decision made in this conversation?" A linter can verify a
license got named; nothing can verify you captured every call that got made out loud.
It leans on judgment, and rules that lean on judgment grade lower. Second, it's a
little narrow and a little me-specific — it presumes you've got an ADR folder, a
memory file, a rules doc to write into. It's a workflow rule more than a code rule, so
it scores softer on generality. Right idea, harder to pin down.

## 2:00 — The lesson
[CARD: "checkable beats correct"]

That's the three points, right there. Both rules are correct. But the one you can
*check* — name the license, yes or no — outscores the one you can only *intend*. The
best rules don't just tell you the right thing; they leave a mark you can verify after
the fact. Good advice that nobody can audit is still advice. A rule earns its slot when
breaking it leaves evidence.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 10 and 93).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
