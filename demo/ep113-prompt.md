# Episode 113 — "One front door, or a script that only runs on my laptop"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 23 — *One config layer; one order* (score 61.5)
- BAD:  Rule 43 — *No shell-isms; orchestrate* (score 47.0)

---

## 0:00 — The hook
[CARD: "61.5  vs  47.0"]

Two rules about wiring a project together. One tells you where your settings live. One
tells you how to glue your steps together. Same goal — keep the thing portable and sane —
but the grader put fourteen points between them. Here's why.

## 0:20 — The good one
[CARD: "Rule 23 · One config layer; one order · 61.5"]

All config flows through one layer — env vars → `.env` → config file → CLI flags, in
increasing precedence. No environment reads scattered across modules.

Sixty-one because it's pertinent everywhere and dead simple to enforce. Every project has
config; every project eventually has config bleeding into ten different files read ten
different ways, and then nobody can tell why the staging value won. This rule fixes that
with one sentence: one layer, one precedence order, every time. It scores well on
architectural simplicity — a single funnel is the cleanest shape there is — and on
generality, because it's true whether you're writing Python, Go, or a shell script. The
only reason it's not higher: getting config wrong is annoying, not catastrophic. Good
hygiene, not a company-ender.

## 1:10 — The bad one
[CARD: "Rule 43 · No shell-isms; orchestrate · 47.0"]

Now the weaker one. "No shell-isms in cross-platform scripts; orchestrate in Python or
Node, not bash."

Forty-seven. And it's not wrong — bash that assumes a Unix gets you a script that dies the
first time it meets Windows, and I've watched that happen. The problem is enforceability
and scope. "No shell-isms" is fuzzy — where's the line between a clean one-liner and a
shell-ism? A grader can't check that cleanly, and neither can a linter. It also leans on a
preference — "use Python or Node" — that only binds if you've already bought into that
stack. Narrower than it looks, and harder to police than it sounds. Right instinct, soft
edges.

## 2:00 — The lesson
[CARD: "a rule you can check beats a rule you agree with"]

That's the gap. Rule 23 names one shape and one order — you either flow through the layer or
you don't, and anyone can see which. Rule 43 names a vibe. Both want portability; only one
gives you a test for it. The best rules aren't just correct — they're *checkable*. A rule a
machine can enforce earns its slot. A rule you have to argue about, every time, doesn't.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 23 and 43).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
