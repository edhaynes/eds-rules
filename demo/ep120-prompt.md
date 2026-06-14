# Episode 120 — "One commit, one job — and a rule that's just good manners"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 8 — *One purpose per commit* (score 60.0)
- BAD:  Rule 67 — *Show the version everywhere* (score 49.0)

---

## 0:00 — The hook
[CARD: "60.0  vs  49.0"]

Two rules I actually believe in — one scores a sixty, one barely clears the high
forties. Both are good advice. Only one of them earns a slot in a list of a hundred.
Here's the eleven-point gap, and what it tells you about what makes a rule worth
writing down.

## 0:20 — The good one
[CARD: "Rule 8 · One purpose per commit · 60.0"]

One purpose per commit, one purpose per deploy. No "while I'm in there" fixes.

Sixty, and it earns it on enforceability and generality. This rule applies to every
project, every language, every team — there's no setup where "make this commit do one
thing" stops being true. It scores well on architectural simplicity too: it's not a
tool, it's a discipline, so there's nothing to build and nothing to maintain. And it's
cost-effective in the way that matters — a clean one-purpose commit is the difference
between reverting a bug in ten seconds and bisecting through a tangle of unrelated
changes for an hour. Where it loses a few points is security and raw pertinence: it
won't save you from a leaked key, and it's good hygiene rather than a catastrophe-
stopper. Solid, universal, cheap to follow. That's a sixty.

## 1:10 — The bad one
[CARD: "Rule 67 · Show the version everywhere · 49.0"]

Now the one that comes up short. "Display the version everywhere it matters: splash
screen, `--version`, `/health`."

Forty-nine. And it's not wrong — it's just thin. It's genuinely useful: when something
breaks in production, the first question is always "which version is this," and a
visible version string answers it instantly. But it scores low on generality and
pertinence because it's narrow — it only matters for shipped, versioned, deployed
software with a splash screen or a health endpoint. A library, a script, a one-off
tool? The rule's got nothing to say. And on enforceability it's soft: an AI will never
*violate* this unprompted the way it'll bundle five fixes into one commit. It's a
checklist item, not a guardrail. Good practice — just not a hundred-rule practice.

## 2:00 — The lesson
[CARD: "discipline beats checklist"]

That's the gap a grade exposes. Rule 8 is a discipline — it shapes how you work on
everything you touch. Rule 67 is a checklist item — handy when it applies, silent when
it doesn't. The best rules change your behavior across the whole board. The weaker ones
just remind you to tick a box. Both are good advice; only one is structural — and that's
exactly the line a grade draws.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 8 and 67).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
