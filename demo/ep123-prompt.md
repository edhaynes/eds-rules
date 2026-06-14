# Episode 123 — "A boring rule beats a smart one"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 40 — *Path library + LF endings* (score 60.0)
- BAD:  Rule 35 — *No god classes* (score 49.5)

---

## 0:00 — The hook
[CARD: "60.0  vs  49.5"]

Two rules off the same list. One's a dull little plumbing rule about file paths. The
other sounds like real engineering wisdom — don't build god classes. And yet the
boring one outscores the smart one. Here's why.

## 0:20 — The good one
[CARD: "Rule 40 · Path library + LF endings · 60.0"]

Use the language's path library — never string-concatenate paths or hardcode
separators — and enforce LF line endings via `.gitattributes`.

Sixty. Not glamorous, but it earns it. It's *pertinent* — every project touches the
filesystem, so it bites constantly. It's dead cheap and dead simple: use the tool
that's already in your stdlib, add one config file. And it's mechanically
*enforceable* — a linter or `.gitattributes` either passes or it doesn't, no judgment
call. Most of all it's *general*: Mac, Linux, Windows, every language with a path
module. A rule that applies everywhere and a machine can check is exactly what a
hundred-rule list wants.

## 1:10 — The bad one
[CARD: "Rule 35 · No god classes · 49.5"]

Now the one that sounds smarter. "No god classes: more than ~7–10 public methods means
a collaborator is missing."

Forty-nine and a half. And it's not wrong — god classes *are* a smell. But look at
that "~7–10." It's a heuristic, not a line. Where rule 40 a linter passes or fails,
this one's a judgment call every time — a legit class can have twelve methods, and a
bloated one can hide behind six. Low *enforceability*, because there's no clean test.
And it's narrower than it reads: it only really fires on object-oriented code, so its
*generality* takes a hit too. Good advice — just softer and harder to pin down than
its score-mate.

## 2:00 — The lesson
[CARD: "checkable beats clever"]

That's the gap the grade exposes. The rule that wins isn't the wiser-sounding one —
it's the one a machine can enforce and that fires everywhere. "No god classes" is a
principle you have to *apply*; "use the path library" is a rule you can *check*. On a
list meant to run unattended, checkable beats clever every time.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 40 and 35).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
