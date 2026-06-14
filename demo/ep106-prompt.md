# Episode 106 — "The backup habit, and the chore nobody does"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 6 — *Push early; push always* (score 63.5)
- BAD:  Rule 97 — *Regenerate the README* (score 45.5)

---

## 0:00 — The hook
[CARD: "63.5  vs  45.5"]

Two rules off the same list, eighteen points apart. One is a safety habit you can run
on autopilot. The other is good advice that almost nobody actually enforces. Watch how
the grade tells them apart.

## 0:20 — The good one
[CARD: "Rule 6 · Push early; push always · 63.5"]

Push early and push always: working code lands on main frequently. Uncommitted,
unpushed work is a liability — the remote is the backup. The classic excuse not to
(merge pain) is gone: AI handles messy merges extremely well.

A sixty-three because it's universal and cheap, and it kills a real, recurring loss:
work that only exists on one disk is one wiped laptop away from gone. The reason people
hoarded local commits — merge hell — is the one thing AI genuinely erased. So the cost
of doing the right thing dropped to near zero while the downside of skipping it stayed
exactly as bad. It scores well on pertinence and cost-effectiveness, and it's dead
simple to enforce: push at the end of every unit of work, no judgment call required.
Where it loses points is security and architectural weight — it's a discipline, not a
gate. Good habit, not a wall.

## 1:10 — The bad one
[CARD: "Rule 97 · Regenerate the README · 45.5"]

Now the softer one. "After every major change, regenerate the README from scratch
rather than patching it. It answers, in order: what/who for, quick start, configuration
table, how to test, architecture, deployment, troubleshooting."

Forty-five. And it's not bad advice — a regenerated README beats a patched one that's
drifted three features behind reality. The problem is enforceability. "Major change" is
a judgment call, "from scratch" is a preference, and nothing fails if you skip it — no
test goes red, no deploy halts. A rule you can quietly ignore with zero consequence
scores low no matter how sensible it reads. It also leans prescriptive: that exact
seven-section order is my taste, not a law, which costs it on generality. Sound
guidance, weak as an enforceable rule.

## 2:00 — The lesson
[CARD: "a rule needs teeth, not just sense"]

That's the gap the grade exposes. Both rules are good advice. But Rule 6 has a clean
trigger and a real cost for skipping it, so it runs itself. Rule 97 depends on you
choosing to do the right thing every time — and "depends on discipline" is exactly the
kind of rule an AI, or a tired human, lets slide. The best rules don't ask for good
intentions. They have teeth.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 6 and 97).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
