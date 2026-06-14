# Episode 122 — "Wire it in vs talk straight"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 31 — *DI over globals* (score 60.0)
- BAD:  Rule 99 — *No flattery; no yes-manning* (score 49.5)

---

## 0:00 — The hook
[CARD: "60.0  vs  49.5"]

Every rule I have got graded. Today: a solid one about how you build your code — and a
softer one about how the AI talks to you. Eleven points apart. One's structural, one's
behavioral, and the gap tells you which kind of rule actually holds.

## 0:20 — The good one
[CARD: "Rule 31 · DI over globals · 60.0"]

"Dependency injection over module-level globals and singletons — collaborators arrive
via the constructor."

It scores a sixty because it's pertinent to almost any codebase and it pays off in
every dimension that matters. Pass your collaborators in and the whole thing gets
cheaper: you can swap the real backend for a fake in a test, you can point local at one
thing and cloud at another, and nothing reaches out and grabs a hidden global. That's
architectural simplicity you can feel — the seams are visible, the wiring is explicit.
It's enforceable, too: a reviewer can spot a module-level singleton at a glance. Broad,
cheap to follow, expensive to skip. That's a real rule.

## 1:10 — The bad one
[CARD: "Rule 99 · No flattery; no yes-manning · 49.5"]

Now the softer one. "No flattery, no yes-manning. Agree only when it carries
information, disagree plainly when the evidence warrants, and defend your reasoning
before capitulating."

Forty-nine and a half. And honestly? Fair. I stand by it — I don't want an AI that
tells me I'm brilliant before it tells me I'm wrong. But it's hard to grade and harder
to enforce. There's no scanner for sycophancy, no test that fails when the model
flatters you. It scores lower on enforceability and on objectivity, because "agree only
when it carries information" is a judgment call every single time, not a checkable
contract. It's also a touch persona-specific — it's about how I want to be talked to,
not about how the software behaves. Good guidance, weak law.

## 2:00 — The lesson
[CARD: "structural rules outscore behavioral ones"]

That's the split a grade exposes. A rule you can wire into the architecture and check at
review time beats a rule about tone every time — not because tone doesn't matter, but
because you can't enforce a vibe. The best rules leave a mark in the code. The soft ones
live in the prompt and hope for the best.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 31 and 99).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
