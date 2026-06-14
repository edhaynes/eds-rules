# Episode 95 — "Crash on purpose, or chase a chip"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 9 — *Fail fast* (score 72.5)
- BAD:  Rule 42 — *Both arches; flag no-ARM* (score 39.5)

---

## 0:00 — The hook
[CARD: "72.5  vs  39.5"]

Two rules, same list, graded against the same rubric. One tells you to crash on
purpose. The other tells you to babysit a CPU architecture. One's a near-universal
law; the other's half a law on a good day. Here's why the gap.

## 0:20 — The good one
[CARD: "Rule 9 · Fail fast · 72.5"]

"Fail fast: invalid config, missing dependencies, or unreachable backends crash loudly
at startup with a clear message — never limp along degraded."

Seventy-two and a half, and it earns it. It's pertinent to basically every program
that reads config or talks to a backend — that's most of them. It's cheap: a check at
startup costs nothing and saves you the worst kind of bug, the silent half-working one
that fails three hours later in production with no clue why. Architecturally it's
simple — a guard at the door, not a system. And it's general: it doesn't care what
language, what stack, what my crew looks like. The only reason it isn't a ninety is
enforceability — an AI can technically write degraded fallback code without realizing
it broke the rule. But on value, this one's gold.

## 1:10 — The bad one
[CARD: "Rule 42 · Both arches; flag no-ARM · 39.5"]

Now the soft end of the board. "Target arm64 and x86_64; flag any dependency without
native ARM builds and document the workaround."

Thirty-nine and a half. Not wrong — just narrow. This only bites if you actually ship
to both arm64 and x86_64, and if your dependency graph has a stubborn x86-only package
in it. For a lot of projects that's never. It also leans on my world specifically — I
run an ARM compute box, so a no-ARM dependency has no home here. That's a real constraint
*for me*. As a hundred-rule law it scores low on generality, and it's hard to enforce —
"document the workaround" is advice, not a gate an AI either passes or fails. It's a
good checklist item. It's a weak commandment.

## 2:00 — The lesson
[CARD: "a law beats a checklist"]

That's the split a grade makes obvious. Fail-fast is a law — it applies everywhere and
breaking it costs you. Both-arches is a checklist item — it applies sometimes, to
people in my exact situation, and breaking it costs you a build flag. Both belong in a
project. Only one belongs near the top of a list of a hundred.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 9 and 42).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
