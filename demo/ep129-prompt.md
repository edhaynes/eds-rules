# Episode 129 — "Scan what you didn't write, ship what stays up"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 57 — *Scan files you didn't write* (score 58.0)
- BAD:  Rule 48 — *Health endpoints + SIGTERM* (score 51.5)

---

## 0:00 — The hook
[CARD: "58.0  vs  51.5"]

Every rule I have got graded. Today: two from the middle of the pack, six points apart.
One guards a door most people forget exists; the other is solid advice that just doesn't
apply everywhere. Same neighborhood on the board, two different reasons they sit there.

## 0:20 — The good one
[CARD: "Rule 57 · Scan files you didn't write · 58.0"]

Before `git add` of any file you didn't author, scan it for secret-shaped strings (key
prefixes, JWTs, private-key blocks, long base64 blobs).

Fifty-eight, and it earns it on security and pertinence. The trap this closes is the one
nobody watches: it's easy to remember to scrub your *own* secrets — it's the file another
agent dropped in, or the config you pasted from somewhere, that ships the leaked key. The
check is cheap and it's a clean named pattern, so it's enforceable in a hook. Where it
gives up points is generality and simplicity — it's one specific moment in one workflow,
a precondition on `git add`, not a universal law. Real value, narrow window.

## 1:10 — The bad one
[CARD: "Rule 48 · Health endpoints + SIGTERM · 51.5"]

Now the lower one. "Services expose health/readiness endpoints and shut down gracefully
on SIGTERM."

Fifty-one and a half. And it's not wrong — it's *good* engineering. It scores lower
because it only means anything if you're running a long-lived service behind an
orchestrator. No service, no SIGTERM to catch, no readiness probe to answer — so it's
silent for a CLI, a script, a library, a batch job. That's a generality hit. And it leans
on judgment: "graceful" isn't a pattern a hook can grep for, so enforceability drops too.
Sound rule, smaller blast radius.

## 2:00 — The lesson
[CARD: "applies everywhere × catches what you'd miss"]

That's what the grade exposes. Both rules are correct — the gap is reach and what they
catch. The scan guards a blind spot you'd actually walk into; the health rule is great
advice that just sleeps until you're running a server. A rule climbs the list when it
applies broadly *and* catches the thing you'd otherwise miss — and that's exactly the
axis these six points measure.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 57 and 48).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
