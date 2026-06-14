# Episode 92 — "The leak that ends you, and the note that's just a note"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 2 — *Never hardcode a secret* (score 82.0)
- BAD:  Rule 18 — *Linda searches wide* (score 30.0)

---

## 0:00 — The hook
[CARD: "82.0  vs  30.0"]

Both of these got graded on the same rubric. One scored an eighty-two — a rule that
protects you whether you run my crew or not. The other scored a thirty. Same list.
Here's what fifty points of difference actually looks like.

## 0:20 — The good one
[CARD: "Rule 2 · Never hardcode a secret · 82.0"]

"Never hardcode secrets, API keys, tokens, passwords, or private endpoints. Found one
in the codebase → stop and flag it; never propagate it, even temporarily."

Eighty-two, and it earns every point. It's pure security and it's pertinent to
literally every codebase ever written — that's where the generality comes from. The
cost-benefit is brutal in your favor: a named constant in a config file costs nothing,
a key baked into source is forever, because once it's in git history it's in every
clone. Architecturally it's simple — secrets live in one place, the config layer, not
sprinkled through the code. And it's enforceable: a scanner can catch a hardcoded key
mechanically. The one thing keeping it off a ninety is that it's the *prevention* rule,
not the *detection* rule — the scan that catches the slip is rule one. This one is the
discipline that means the scan finds nothing.

## 1:10 — The bad one
[CARD: "Rule 18 · Linda searches wide · 30.0"]

Now the bottom of the board. "Linda, the research manager, runs on a fast web-capable
model. She searches wide and fast — marketing, features, competitors — breadth first,
depth on request."

Thirty. And it's not a bad idea — it's just not really a *rule*. It's a role
description for one persona on my specific crew. Pull it out of my setup and there's
nothing to enforce, nothing an AI could violate, no codebase it protects. It scores
low on generality because it only means anything if you've built Linda. Low on
security and architectural simplicity because it isn't about either. It's persona
config dressed as law — useful to me, a footnote to everyone else.

## 2:00 — The lesson
[CARD: "a law protects everyone · a note describes you"]

That's the line a grade draws. The eighty-two protects every codebase on earth and a
scanner can prove it. The thirty describes how one of my people works. Both belong
somewhere — but only one is a hundred-rule rule, and the grade is exactly how the note
earns its way *off* the list when something universal needs the slot.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 2 and 18).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
