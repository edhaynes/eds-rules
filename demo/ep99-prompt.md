# Episode 99 — "The rule that audits itself, and the one that's just taste"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 84 — *Pin it and lock it* (score 67.5)
- BAD:  Rule 33 — *One non-trivial class per file* (score 42.5)

---

## 0:00 — The hook
[CARD: "67.5  vs  42.5"]

Same list, same rubric, two rules twenty-five points apart. One protects you from a
supply chain you don't control. The other is a layout preference dressed up as a law.
Here's why the grader split them.

## 0:20 — The good one
[CARD: "Rule 84 · Pin it and lock it · 67.5"]

"Run a vulnerability audit periodically and on every new dependency."

Sixty-seven and a half — and it's the highest generality score on this episode, a nine.
Every project on earth pulls in dependencies, and every one of those dependencies is
code you didn't write and can't fully vouch for. Auditing on every new dep and on a
schedule is cheap, it's scriptable, and it catches the thing that hurts most: a known
CVE you shipped without knowing. It scores well on cost-effectiveness and enforceability
because the whole check is one command in a hook — easy to wire, hard to skip by
accident. It's not a perfect ten on pertinence or security on its own, because an audit
is a tripwire, not a fix — but as a standing habit it earns its slot anywhere.

## 1:10 — The bad one
[CARD: "Rule 33 · One non-trivial class per file · 42.5"]

Now the lower end. "One non-trivial class per file; small helpers and DTOs may share."

Forty-two and a half. And look — it's not bad advice. It's just soft. The security
score is a one, because nothing about file layout protects anything; a vulnerability
does not care how you organized your classes. Pertinence is a three because it's a style
guideline, the kind of thing a good engineer already does by instinct. And enforceability
drags too — "non-trivial" is a judgment call, "may share" is an exception baked right in,
so a linter can't cleanly hold the line. It's a reasonable convention. It's just not a
load-bearing rule, and the grade says so.

## 2:00 — The lesson
[CARD: "protects you  vs  pleases you"]

That's the split a grade exposes. The strong rule defends you against something real and
expensive — a CVE you'd otherwise ship blind. The weak one makes the code tidier, and
tidy is nice, but tidy isn't protection. When a rule's whole value is taste, it scores
like taste. The hundred best rules earn their place by what they stop, not by how clean
they make the diff look.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 84 and 33).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
