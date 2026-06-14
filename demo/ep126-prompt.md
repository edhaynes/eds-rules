# Episode 126 — "Cleanup that can't be forgotten vs. paperwork that can"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 82 — *Cleanup is structural* (score 59.0)
- BAD:  Rule 66 — *Changelog rides the bump* (score 50.5)

---

## 0:00 — The hook
[CARD: "59.0  vs  50.5"]

Two rules, nine points apart on the grade sheet, and both about not forgetting things.
One makes forgetting impossible. The other just asks you, nicely, to remember. Watch
which one wins.

## 0:20 — The good one
[CARD: "Rule 82 · Cleanup is structural · 59.0"]

Here it is, word for word: "Resource cleanup uses context managers / `defer` / `using`
— no close-and-hope."

Fifty-nine. It scores well because it's pertinent everywhere and it's structural — it
ties cleanup to the *scope*, not to your discipline. A file handle, a lock, a socket, a
transaction: with `with` or `defer` or `using`, the release happens when the block
exits, even when an exception blows through the middle. That's the architectural
simplicity points — you delete the entire class of "forgot to close it on the error
path" leaks instead of patching them one by one. It's general across every language
that has the construct, and it leans on the language to enforce it rather than on a
reviewer's eyeballs. The reason it isn't a ninety: it's a leak, not a breach — getting
it wrong costs you a slow degrade, not a dead company.

## 1:10 — The bad one
[CARD: "Rule 66 · Changelog rides the bump · 50.5"]

Now the one that lands lower. Word for word: "Maintain a changelog in the same commit
as the version bump."

Fifty point five. And it's not a bad idea — I follow it. It's just weaker as a *rule*.
It's pure process hygiene: nothing breaks if you skip it. No leak, no crash, no
corrupt state — just a changelog that drifts out of sync, which you fix later with
mild annoyance. That's low on cost-of-getting-it-wrong. It's also soft on
enforceability — "same commit" is a convention a human has to honor, and there's no
language construct holding the line the way `with` holds it for Rule 82. And it's a
notch narrower in generality: it only matters once you're cutting versioned releases
with a changelog at all. Useful, real, worth keeping — just not load-bearing.

## 2:00 — The lesson
[CARD: "structure beats discipline"]

That's the gap the grade exposes. The strong rule moves the work into the structure of
the code, where the language enforces it and you literally can't forget. The weak rule
leaves the work on a human's to-do list. Both are good advice — but a rule you can't
forget will always outscore a rule you're merely supposed to remember.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 82 and 66).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
