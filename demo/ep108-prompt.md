# Episode 108 — "Scan the whole rope, not just the end"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 55 — *Scan the range; not the tip* (score 63.5)
- BAD:  Rule 50 — *Show progress; cache default* (score 45.5)

---

## 0:00 — The hook
[CARD: "63.5  vs  45.5"]

Every rule I have got graded. Today: one rule about security that knows exactly where
people get burned — and one about user experience that's good advice but soft as a
law. Same list, eighteen points apart. Here's what those points are made of.

## 0:20 — The good one
[CARD: "Rule 55 · Scan the range; not the tip · 63.5"]

"Before pushing, scan the entire push range, not just the tip — an intermediate commit
can carry the leak."

Sixty-three and a half. It scores high because it's pertinent and it's security, and
it closes a hole most people don't even know is open. You scan the latest commit, it's
clean, you push — and three commits back somebody dropped a key that's now riding along
in the history. The tip lies. The range tells the truth. It's cheap to enforce — one
flag on the scan command — and it generalizes to any repo, any team, any agent. The
only reason it isn't a ninety is it's a refinement of a bigger rule, not a headline on
its own.

## 1:10 — The bad one
[CARD: "Rule 50 · Show progress; cache default · 45.5"]

Now the softer end. "Show progress on unavoidably slow operations and say why; cached
paths are the default, expensive paths are explicit and rare."

Forty-five and a half. And it's not wrong — it's genuinely good UX advice. The problem
is it's two rules wearing one coat: a progress-bar rule and a caching-strategy rule,
stapled together. Neither half is easy to enforce — there's no scan, no gate, no green
or red. An AI won't violate it the way it'll violate a secret leak; it just quietly
ships something slightly worse. Pertinent? Sure. Security? None. Architecturally
simple? It's actually two ideas. That's why it lands mid-table — it's a preference
dressed as a law.

## 2:00 — The lesson
[CARD: "a law you can check beats a wish you can't"]

That's the gap the grade exposes. The good rule names a specific failure and gives you
a way to catch it — scan the range, find the leak. The weak one names a good habit but
hands you nothing to enforce it with. Rules that gate beat rules that hope. If you
can't write the check, you've written advice, not a rule.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 55 and 50).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
