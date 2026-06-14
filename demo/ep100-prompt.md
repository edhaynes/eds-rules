# Episode 100 — "Crash on bad config vs size a sprint just right"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 22 — *Validate config at startup* (score 66.5)
- BAD:  Rule 15 — *Jason sprints sized for 90%* (score 43.5)

---

## 0:00 — The hook
[CARD: "66.5  vs  43.5"]

Every rule I have got graded. Today: a solid, do-this-everywhere rule — against one
that's good advice but can't carry its weight on a hundred-rule list. Twenty-three
points apart, both mine. Here's what the grade saw that I didn't.

## 0:20 — The good one
[CARD: "Rule 22 · Validate config at startup · 66.5"]

Validate config at startup and fail with a message naming the missing or invalid key.

It scores in the high sixties because it's pertinent to basically every program that
reads config, and it's cheap to do — check the values once at boot, crash loud if
they're wrong. Architecturally it's clean: one validation gate instead of scattered
"is this set?" checks limping through the codebase. Enforceable, too — you either fail
fast with a named key or you don't. Where it loses a few points is generality and
security: it's universal-ish but not catastrophic to skip the way a secret scan is. A
strong rule, just not a top-of-the-board one.

## 1:10 — The bad one
[CARD: "Rule 15 · Jason sprints sized for 90% · 43.5"]

Now the back of the pack. "Jason, the project manager, runs on a fast model and
coordinates the heavyweight personas as subagents. He holds the through-line, contains
tangents, and chunks the work into independent, clearly defined sprints — each sized so
the AI nails it first go 90% of the time, and independent so the personas can run them
in parallel. He does not write code."

Forty-three. And it's fair. The *sprint-sizing* idea inside it is genuinely good —
small, independent chunks the AI can nail first try is real wisdom. But it scores low
because it's persona-specific: it describes my crew, my Jason, my parallel-subagent
setup. Strip that out and you've got "size your work well," which is generality, sure,
but also vague — hard to enforce, no clear pass/fail. It mixes a universal lesson with
a private org chart, and the org chart drags the grade down.

## 2:00 — The lesson
[CARD: "a rule the machine can check beats one only your team understands"]

That's the gap a grade exposes. The good rule has a sharp edge — name the bad key,
crash, done. You can test it. The weak one is half timeless craft, half my staffing
diagram, and the craft half is too soft to enforce. Best rules are specific about the
behavior and general about the setting. Get that backwards and even good advice scores
in the forties.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 22 and 15).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
