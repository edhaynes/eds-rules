# Episode 140 — "Loud failures, dead comments"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 81 — *AI errors surface; no fake tool* (score 56.0)
- BAD:  Rule 91 — *No commented-out code* (score 55.5)

---

## 0:00 — The hook
[CARD: "56.0  vs  55.5"]

Half a point apart on the rubric, and they teach opposite lessons. One is about what
your software does when things go wrong. The other is about what your *codebase*
looks like when things go right. Same grade, almost — and yet one of these earns its
slot and the other is hanging on by a thread.

## 0:20 — The good one
[CARD: "Rule 81 · AI errors surface; no fake tool · 56.0"]

AI/LLM errors surface to the user as friendly messages — never a silent failure, never a raw stack trace. And agents only call tools that actually exist in their tool list: a hallucinated tool name wastes tokens and stalls the session — fall back to shell or file primitives, or ask for the tool to be wired in, never fabricate one.

It scores in the mid-fifties because it's two real, modern failure modes bolted
together. On pertinence it's dead-on for anything with an LLM in the loop: silent
failures and invented tool names are exactly how these systems rot in production. The
cost-effectiveness is high — a friendly error message is nearly free, and a fabricated
tool call burns tokens and stalls the whole session. Where it loses points is
architectural simplicity and generality: it's two rules in one sentence, and it only
bites if you're building agentic AI. Enforceability is middling — "never fabricate a
tool" is hard to lint for. Solid, specific, current — but not universal.

## 1:10 — The bad one
[CARD: "Rule 91 · No commented-out code · 55.5"]

Now the one right below it. "No commented-out code — git history is the archive."

Fifty-five and a half. And honestly? Fair. It's *right* — dead code in comments is
clutter, git already keeps the history, nobody reads the graveyard. But look at the
grade: it scores well on cost-effectiveness and enforceability — a linter can flag a
commented-out block, it's cheap to fix — and yet it sits near the floor. Why? Low
stakes and low security weight. Nothing catastrophic happens if a comment block
lingers. It's hygiene, not a guardrail. It's the kind of rule a tidy human follows by
habit and an AI rarely violates unprompted — which is exactly what makes it a
footnote, not a law.

## 2:00 — The lesson
[CARD: "stakes, not just correctness"]

That's what the half-point gap exposes. Both rules are *correct*. The difference is
what it costs you to break them. Rule 81 is about software that fails loud instead of
lying to you — break it and a user is staring at a frozen spinner or a stack trace.
Rule 91 is about tidiness — break it and your diff is a little uglier. A rubric
doesn't reward being right. It rewards mattering when you're wrong.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 81; rule 91 short title "No commented-out code").
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
