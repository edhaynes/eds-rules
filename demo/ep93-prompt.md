# Episode 93 — "Config beats a cast of characters"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 20 — *Zero hardcoded values* (score 74.0)
- BAD:  Rule 13 — *Five roles; human is final* (score 33.5)

---

## 0:00 — The hook
[CARD: "74.0  vs  33.5"]

Two rules off the same list. One tells you to stop wiring numbers into your code. The
other describes the cast of characters running my shop. One travels to anybody's
project; the other barely leaves mine. The grade saw the difference — here's why.

## 0:20 — The good one
[CARD: "Rule 20 · Zero hardcoded values · 74.0"]

"Zero hardcoded values for anything that could plausibly change: hosts, ports, model
names, paths, timeouts, retry counts, feature flags, prompts."

It scores a seventy-four because it's pure architecture, and it pays off everywhere. On
pertinence it's a bullseye — hardcoding is the single most common thing that makes code
impossible to move, test, or deploy somewhere new. It's cheap: pull the value into
config, done, and you never pay for it again. Architectural simplicity actually goes
*up* when you follow it — one config layer instead of magic numbers scattered across
forty files. And it's general — Python, Go, a shell script, a frontend, doesn't matter.
The only thing keeping it off the very top is enforceability: a linter can flag some of
it, but "could plausibly change" still takes judgment. Strong rule, broad reach.

## 1:10 — The bad one
[CARD: "Rule 13 · Five roles; human is final · 33.5"]

Now the low end. "The crew is five fixed roles plus one human — Eddie. Eddie's rulings
are final and canonical: any persona's plan, preference, or pushback yields to his
decision, and his decisions become part of the canon. One exception: Jason is permitted
— expected — to push back when a new ruling contradicts the canon, surfacing the
inconsistency before acting on it. The model behind each role is a config binding per
stack, never hardcoded."

Thirty-three. And that's honest. It's not a bad idea — a clear chain of command and a
human with the final word is genuinely useful. But as a *rule on a hundred-rule list*,
it's narrow. It describes my specific crew: five named roles, one named human, one named
persona who gets to argue back. Strip the names out and what's left — "have a final
decision-maker" — is true but thin. It scores low on generality because almost none of
it transfers, and low on enforceability because there's nothing for a tool to check.
It's a setup, not a law.

## 2:00 — The lesson
[CARD: "transferable architecture > local org chart"]

That's the split a grade exposes. Rule 20 is about how code is *built*, so it works in
anyone's hands. Rule 13 is about how *my* shop is run, so it mostly works in mine. The
rules that earn a permanent slot describe the structure, not the staff — and when a
better structural rule comes along, the org-chart rule is the first to give up its seat.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 20 and 13).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
