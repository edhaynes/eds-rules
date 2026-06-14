# Episode 96 — "Guard the door, or just take notes"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 3 — *Distrust every external input* (score 72.0)
- BAD:  Rule 83 — *Structured logs past a script* (score 40.0)

---

## 0:00 — The hook
[CARD: "72.0  vs  40.0"]

Two rules from the same list. One scored a seventy-two, one scored a forty. One stops
attackers from owning your box. The other tells you how to format your log lines. Both
earned a slot — here's why the gap is this wide.

## 0:20 — The good one
[CARD: "Rule 3 · Distrust every external input · 72.0"]

Distrust every external input. Validate and constrain it at the boundary; parameterize
queries and commands, resolve and confine paths, never interpolate untrusted data into
SQL, a shell, HTML, or a deserializer. Secret hygiene guards what leaks out — this
guards what gets in.

It scores a seventy-two because it's the front door. Nearly every serious breach you've
ever read about traces back to trusting something you shouldn't have — an injection, a
path traversal, a deserializer fed a payload. It's broadly pertinent, it's the heart of
security, and it generalizes to every language and every project that touches the
outside world. Where it gives up points is enforceability and simplicity — "validate at
the boundary" is a discipline, not a checkbox a scanner can run for you. Still, the
downside of getting it wrong is total, and that's what keeps it near the top.

## 1:10 — The bad one
[CARD: "Rule 83 · Structured logs past a script · 40.0"]

Now down the leaderboard. "Use a logger, never `print`, in shipped code; log level
configurable, and structured — JSON — once the project outgrows a script."

A forty. And honestly? Fair. It's good advice — I stand by it — it's just *small*. It's
real engineering hygiene, but it's a quality-of-life rule, not a load-bearing one.
Nobody gets breached because their logs weren't JSON. It scores low on security and on
pertinence because the cost of skipping it is mild — a harder debugging session, not a
catastrophe — and the "once the project outgrows a script" qualifier makes it situational
by its own wording. It's a B-grade habit pretending it belongs next to the front-door
rules.

## 2:00 — The lesson
[CARD: "stakes, not effort"]

That's what the grade exposes: a rule's worth is measured by what happens when you break
it, not by how often you do it. Guarding the door is worth a seventy-two because the
cost of leaving it open is everything. Tidy logs are worth a forty because the cost is a
slower afternoon. Both are right. Only one of them can sink you.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 3; the structured-logging clause of rule
  80, which the rubric grades as entry 83 "Structured logs past a script").
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
