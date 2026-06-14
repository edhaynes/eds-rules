# Episode 119 — "Audit the deps vs patch the hole"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 85 — *Audit for vulnerabilities* (score 60.5)
- BAD:  Rule 60 — *After a leak; fix the hook* (score 48.5)

---

## 0:00 — The hook
[CARD: "60.5  vs  48.5"]

Every rule I have got graded. Today, two from the security-and-dependency end of the
list — one that keeps you out of trouble in the first place, and one that only matters
after you're already in it. Twelve points apart, and the gap is the whole lesson.

## 0:20 — The good one
[CARD: "Rule 85 · Audit for vulnerabilities · 60.5"]

Run a vulnerability audit periodically and on every new dependency.

It clears sixty because it's proactive and it's general. Every project pulls in code
it didn't write, and that code goes stale — a clean dependency today is a CVE next
month. Auditing on every add catches the bad one before it ships, and the periodic
sweep catches the one that rotted after you shipped. It scores high on pertinence
because it touches every codebase with dependencies, and high on security because the
downside it blocks is a known-exploited package in production. The cost is a tool you
already have wired into CI. The one place it gives ground is architectural simplicity —
"periodically" needs a cadence and an owner, or it quietly stops happening. But cheap,
broad, and enforceable in a pipeline gate is exactly what a top rule looks like.

## 1:10 — The bad one
[CARD: "Rule 60 · After a leak; fix the hook · 48.5"]

Now the weaker one. "After any leak, document what scan would have caught it and fix
the hooks so it can't recur."

Forty-eight and a half. And it's a good instinct — it's the post-mortem discipline,
close the gap so the same mistake can't land twice. But look where it sits on the
rubric. It's reactive: it only fires *after* something already went wrong, so its whole
value depends on a failure the other rules are supposed to prevent. It scores low on
generality because "fix the hooks" assumes you run the exact pre-commit and pre-push
hook setup I do — no hooks, no rule. And it's hard to enforce: nobody can gate a commit
on "did you write a thorough post-mortem," so it lives on goodwill, not on automation.
Right idea, narrow blast radius.

## 2:00 — The lesson
[CARD: "prevent broadly  >  patch narrowly"]

That's the split a grade exposes. The strong rule stops a class of problem everywhere,
in a gate a machine can enforce. The weak one is a smart cleanup for one specific
failure, leaning on a setup most people don't have and on a human remembering to do it.
Prevention you can automate beats remediation you have to hope for — and the score says
so out loud.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (the line `85.` for the rule body, and
  rule `60`). Card titles/slugs ("Audit for vulnerabilities", "After a leak; fix the
  hook") and scores are from `quality/grades.csv`.
- Note: in RULES.md the `85.` line reads "Prefer stdlib plus one well-maintained
  dependency over five small ones"; the `grades.csv` row for 85 is slugged `deps` /
  "Audit for vulnerabilities" (60.5). Episode uses the audit framing per the brief.
- Rubric dimensions: pertinence, security, cost-effectiveness, architectural
  simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
