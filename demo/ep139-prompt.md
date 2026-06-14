# Episode 139 — "The rule that grades the others, and the one that needs a use case"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 69 — *Inspect; grade to a rubric* (score 56.0)
- BAD:  Rule 29 — *Swappable interface per axis* (score 55.0)

---

## 0:00 — The hook
[CARD: "56.0  vs  55.0"]

A point apart on the board, but they teach opposite lessons. One rule decides whether
every other rule is being followed. The other is a good idea waiting for a situation to
matter in. Here's why one outranks the other.

## 0:20 — The good one
[CARD: "Rule 69 · Inspect; grade to a rubric · 56.0"]

You get what you inspect: test-driven, not test-after — and graded. Every project keeps
a rubric that scores how good the software actually is. The goal is solid A− software:
90% on the rubric is the working bar, polish takes it to 95%, and nothing publishes
below 95%.

It scores well because it's the rule that makes quality measurable instead of a
feeling. Pertinence is high — it applies to every project, every language, every stack.
Cost-effectiveness is the killer feature: a rubric is cheap to write and it catches
slow quality drift before it ships. Enforceability is concrete — there's a number, you
hit the bar or you don't. And generality is wide: "decide what good means, then measure
against it" is a discipline anyone can adopt. The only thing keeping it off the very top
is that the bar itself is a judgment call, but the rule still earns its slot.

## 1:10 — The bad one
[CARD: "Rule 29 · Swappable interface per axis · 55.0"]

A point behind it: "Anything with a local-vs-cloud or vendor axis goes behind a
swappable interface: LLM provider, storage, database, vector store, cache, queue, auth,
logging sinks."

Fifty-five. And it's solid architecture — I stand by it. So why not higher? It's
prescriptive about a *shape* rather than a *risk*. The list of axes is specific to the
kind of system I build — swap the LLM, swap the storage — and for a project that has no
vendor axis it's just overhead. Pushed too literally it costs you on architectural
simplicity: every interface is an abstraction you have to maintain, and not every axis
earns one. It loses points on generality and on cost-effectiveness — the value depends
entirely on whether you'll actually swap the backend, and a lot of code never does.

## 2:00 — The lesson
[CARD: "measure quality vs predict the future"]

That's the gap. The good rule tells you how to *know* if your work is good — useful on
day one of any project. The architecture rule tells you to prepare for a change that
*might* come. One pays off immediately and everywhere; the other pays off only if you
guessed the future right. A grade rewards the rule that helps you now.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 69 and 29).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
