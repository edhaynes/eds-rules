# Episode 138 — "A wall every language hits vs a habit one language needs"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 34 — *Files small; never >1000 lines* (score 56.0)
- BAD:  Rule 87 — *Project-local virtualenv* (score 54.5)

---

## 0:00 — The hook
[CARD: "56.0  vs  54.5"]

Two rules, a point and a half apart on the board, and they teach completely different
lessons. One is a guardrail every language on earth runs into. The other is a good
habit that only matters if you write Python. Same neighborhood on the leaderboard —
very different reasons for landing there.

## 0:20 — The good one
[CARD: "Rule 34 · Files small; never >1000 lines · 56.0"]

Source files target ≤500 lines, never exceed 1000; past 800, actively refactor.

Fifty-six, and it earns it on generality more than anything. This rule doesn't care
what stack you're on — Python, Go, Rust, TypeScript, C — a thousand-line file is a
god-file in any of them, and a god-file is where bugs hide and reviews go to die.
It scores well on architectural simplicity because the rule *is* the simplification:
hit the ceiling, something's doing too much, pull it apart. It's pertinent because
file bloat is the single most common way AI-written code rots — generate, append,
append, append. Where it loses points is enforceability and the cost-of-getting-it-
wrong: a big file is a smell, not a catastrophe, and "actively refactor" is a judgment
call, not a hard gate. Good rule. Not a save-the-company rule.

## 1:10 — The bad one
[CARD: "Rule 87 · Project-local virtualenv · 54.5"]

Now the one just below it. "Python work always uses a project-local virtualenv —
never install into the system Python."

Fifty-four and a half. And it's not wrong — it's just *narrow*. This is solid Python
hygiene; polluting the system interpreter is a real way to wreck a machine. But look
at the dimensions: generality takes the hit, because the rule only exists for one
language. Go, Rust, Node — they isolate differently or not at all, and this rule has
nothing to say to them. It's also a habit, not a tripwire — there's no clean
"the AI definitely violated this" signal the way a leaked key gives you. Pertinent
inside its lane, low-stakes outside it. That combination — useful but stack-specific
and soft to enforce — is exactly what parks a rule mid-table.

## 2:00 — The lesson
[CARD: "universal guardrail  >  good local habit"]

That's the gap a grade exposes. A rule that holds in every language and catches the
most common failure mode beats a rule that's genuinely correct but only speaks to one
ecosystem. Both are worth following. Only one of them is worth a slot in a list meant
to apply to *all* my software — and the half-point between them is the whole argument.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 34; and the virtualenv rule, "Python
  work always uses a project-local virtualenv — never install into the system Python.").
- Scores from `quality/grades.csv` (ranked rows: Rule 34 = 56.0, Rule 87
  "Project-local virtualenv" = 54.5). Note: grades.csv ranks by composite, so its
  `num` is a leaderboard index — the virtualenv rule's verbatim line in RULES.md is
  numbered 86.
- Rubric dimensions: pertinence, security, cost-effectiveness, architectural
  simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
