# Episode 124 — "Burn the secret vs. write it down"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 53 — *Never copy a secret anywhere* (score 59.5)
- BAD:  Rule 94 — *File bugs/features on sight* (score 50.5)

---

## 0:00 — The hook
[CARD: "59.5  vs  50.5"]

Two rules about handling information the second you touch it. One says *destroy it, never
copy it.* The other says *capture it, never lose it.* Both graded — and there's nine points
between them. Here's what that gap is made of.

## 0:20 — The good one
[CARD: "Rule 53 · Never copy a secret anywhere · 59.5"]

"Never copy a discovered secret anywhere — not into chat, not a scratch file, not
'temporarily.' One exception: during leak response, surface it verbatim — SHA, file, exact
string — to its owner, who must identify which credential to kill."

It scores in the high fifties because it's pure security with almost no cost. The pertinence
is direct — the moment an agent finds a key, the dangerous instinct is to paste it somewhere
to "deal with it." This rule kills that instinct cold. It's architecturally simple: one
prohibition, one named exception, no machinery. And it generalizes — every project, every
agent, every language has secrets that must not get a second copy. The one thing capping its
score is enforceability: a scanner can catch a committed secret, but "don't paste it in chat"
leans on the agent doing the right thing. Strong rule, hard to mechanically verify.

## 1:10 — The bad one
[CARD: "Rule 94 · File bugs/features on sight · 50.5"]

"Track every bug and every requested feature in `bugs.md`/`features.md` the moment it's
observed — even if fixed the same turn. Open questions are filed inline with the entry;
filing never blocks on answers."

Fifty and a half. Not a bad rule — a *specific* one. The principle is sound: capture things
before they evaporate. But it's prescriptive about *my* mechanism — two named files at the
repo root, a particular inline-question convention. That drags down generality, because plenty
of teams track in an issue tracker, not markdown. It's also weak on enforceability — nothing
fails the build when you forget to log a bug — and lighter on the dimension that lifts the top
rules: getting this wrong is annoying, not catastrophic. A dropped bug entry costs you memory.
A copied secret costs you the key. That's the nine points.

## 2:00 — The lesson
[CARD: "stakes × universality"]

Both rules are about handling something the instant you see it. The difference the grade
exposes is *what's at risk* and *how widely it applies.* The secret rule guards against ruin
and works everywhere. The tracking rule guards against forgetfulness and ties itself to my
filenames. Same good instinct — capture or kill on sight — but stakes and universality are
what separate a high rule from a middling one.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 53 and 94).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
