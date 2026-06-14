# Episode 117 — "Runs anywhere vs. a note nobody reads"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 11 — *No path/OS assumptions; script* (score 61.0)
- BAD:  Rule 92 — *No orphan TODOs* (score 48.0)

---

## 0:00 — The hook
[CARD: "61.0  vs  48.0"]

Every rule I have got graded. Today two from the middle of the pack — one solid, one
soft. One makes your code run on a machine you've never seen. The other is a tidiness
note. Watch the gap open up once you grade them honestly.

## 0:20 — The good one
[CARD: "Rule 11 · No path/OS assumptions; script · 61.0"]

Here's the rule, word for word:

"Never assume a path, OS, or shell — use cross-platform primitives. Assume everything
is headless: every tool runs with no display and nobody at a prompt. Script
everything — a manual procedure dies with the next reimage; a script is a `git clone`
away."

It scores a sixty-one, and most of that comes from generality and pertinence. An AI
hardcodes a slash, assumes bash, assumes a `/tmp` — constantly, unprompted — and the
code works on its machine and dies on mine. This rule catches that class of bug across
every language and every project, so it's broad and it's relevant. The "script
everything" half is the real payoff: a manual fix is gone the next reimage, but a
script survives. Where it loses points is security — it's a portability rule, not a
safety rule — and architectural simplicity, because it's actually three ideas bolted
together: no assumptions, headless, scriptable. Strong rule, slightly overloaded.

## 1:10 — The bad one
[CARD: "Rule 92 · No orphan TODOs · 48.0"]

Now the softer one. Word for word:

"No TODO without a tracker link; otherwise it's a dated FIXME with an owner."

Forty-eight. Not wrong — just thin. It's a hygiene rule, and hygiene rules grade low on
the things that matter most for a hundred-rule list. Pertinence is a four: a stray TODO
never breaks a build or leaks a key, it just sits there. Security is a two, because it
guards nothing. And enforceability is shaky — a grep can flag the word `TODO`, but it
can't tell a real tracker link from a fake one, so the rule leans on discipline more
than tooling. It scores well on generality, sure, every codebase has TODOs. But "broad
and harmless" is exactly the profile of a rule that's easy to write and easy to ignore.

## 2:00 — The lesson
[CARD: "cost of breaking it"]

That's what the grade exposes. Both rules are general — both apply everywhere. The
difference is what happens when you break them. Skip rule eleven and your code won't
run on the next box. Skip rule ninety-two and you've got a slightly messier file. The
strong rule prevents a failure; the weak one prevents clutter. When you're ranking a
hundred rules, "what does it cost me to ignore this?" is the question that sorts them.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (the rules titled "No path/OS assumptions;
  script" and "No orphan TODOs").
- Scores from `quality/grades.csv` (11 → 61.0; 92 → 48.0). Rubric dimensions:
  pertinence, security, cost-effectiveness, architectural simplicity, enforceability,
  generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
