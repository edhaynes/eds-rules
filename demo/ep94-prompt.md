# Episode 94 — "The gate everyone respects, and the one only my crew obeys"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 51 — *Hooks before first commit* (score 73.5)
- BAD:  Rule 14 — *Claudius plans deep* (score 37.5)

---

## 0:00 — The hook
[CARD: "73.5  vs  37.5"]

Every rule I have got graded. Today: a rule that puts a guardrail in place before you
can hurt yourself — against a rule that's really just a job description. Same list,
twice the spread in the score. Here's what the grade is telling us.

## 0:20 — The good one
[CARD: "Rule 51 · Hooks before first commit · 73.5"]

Pre-commit hooks with secret scanning — gitleaks plus detect-secrets — are mandatory
in every repo, installed before the first commit, not after.

Seventy-three and a half. Notice the word *before*. A scan you run by hand is a scan
you forget under pressure; a hook runs whether you remember or not. That's why it
scores so high on security and enforceability — it doesn't trust discipline, it
removes the chance to skip. It's broadly pertinent because every repo has the same
exposure, and it's general — works for one dev or a team of fifty, any language, any
stack. The one place it loses points is architectural simplicity: a hook is a moving
part you have to install and maintain in every repo. Small price for a gate that can't
be talked out of doing its job.

## 1:10 — The bad one
[CARD: "Rule 14 · Claudius plans deep · 37.5"]

Now lower down the board. "Claudius, the architect, thinks long and deep. He plans
before anyone implements; if architecture needs rework, his plan was wrong."

Thirty-seven. And the diagnosis is honest: this isn't a rule, it's a role. The good
instinct inside it — plan before you build — is real. But it's wrapped around a named
persona on my specific crew, so its generality collapses; it means nothing to anyone
who hasn't built my exact team. It scores near the floor on security and on
enforceability, because there's nothing here to check. No gate, no scan, no green-light
condition. "Plan deeply" is advice you can nod at and ignore, and no tool will ever
catch you. A rule earns its slot by being enforceable and universal — this one is
neither.

## 2:00 — The lesson
[CARD: "a gate beats a good intention"]

That's the contrast a grade exposes. The strong rule installs something that acts
without you. The weak one describes how someone ought to behave and hopes. Good
intentions don't survive a deadline; a hook does. When you write a rule, ask whether a
machine could enforce it — if the answer is no, you've written a value, not a law, and
the leaderboard will say so.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 51 and 14).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Rule 51 dims: pertinence 7, security 9, cost-eff 8, arch-simpl 4, enforce 8,
  generality 9 → 73.5. Rule 14 dims: pertinence 4, security 1, cost-eff 5,
  arch-simpl 6, enforce 1, generality 4 → 37.5.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
