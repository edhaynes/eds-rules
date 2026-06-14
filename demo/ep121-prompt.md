# Episode 121 — "Crash loud, or check twice"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 21 — *Never silently fall back* (score 60.0)
- BAD:  Rule 64 — *Fetch tags before tagging* (score 49.0)

---

## 0:00 — The hook
[CARD: "60.0  vs  49.0"]

Both of these rules are about the same instinct — don't trust the thing you can't
see. One earned a sixty by being the kind of rule that saves you from a silent
disaster. The other landed at forty-nine because it's right, but it's small. Same
instinct, two very different grades.

## 0:20 — The good one
[CARD: "Rule 21 · Never silently fall back · 60.0"]

Never silently fall back to a different backend.

It scores a sixty because the failure it prevents is the worst kind: the one you
don't notice. You point at a backend, it's down, and the system quietly swaps to
another one — different data, different behavior, different cost — and never tells
you. That's silent partial failure, and it's worse than a loud crash every time.
This rule is dead pertinent, it's cheap to honor, and it's general: anything with a
local-vs-cloud or vendor-A-vs-vendor-B axis lives or dies by it. The only thing
holding it back from higher is enforceability — "silently" is a judgment call, so a
linter can't fully catch it. But the principle is gold.

## 1:10 — The bad one
[CARD: "Rule 64 · Fetch tags before tagging · 49.0"]

Now the lower half. "Before creating a tag, fetch the remote's tags and compare —
local is not the truth."

Forty-nine. And it's *correct* — I stand by it. Your local clone genuinely is not
the source of truth on what tags exist, and stomping a remote tag breaks anyone
pinned to it. But it's narrow. It only fires at one specific moment — cutting a
release tag — and only bites you if you're tagging by hand across multiple machines.
It scores soft on generality, and on cost-of-getting-it-wrong: a tag collision is
annoying, not catastrophic. It's also the kind of thing a release script does for
you, which means it's more a checklist item than a law.

## 2:00 — The lesson
[CARD: "silent danger beats loud annoyance"]

That's the spread a grade exposes. The rule that stops a *silent* failure beats the
rule that stops a *visible, recoverable* one — because the cost of getting it wrong
is what moves the needle. Both are good advice. But "you'll never notice this until
it's bad" earns a higher slot than "you'll hit an error and fix it." Loud problems
fix themselves. Quiet ones end you.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 21 and 64).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
