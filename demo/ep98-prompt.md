# Episode 98 — "Day-one habit beats good-intention paperwork"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 59 — *Gitignore keys from day one* (score 71.0)
- BAD:  Rule 95 — *Plans carry a live Status* (score 42.5)

---

## 0:00 — The hook
[CARD: "71.0  vs  42.5"]

Two rules off my list, both about hygiene. One scored a seventy-one. The other a
forty-two. Same author, same intentions — but one is a habit you set once and never
think about again, and the other is paperwork you have to keep alive. Watch which one
the grade rewards.

## 0:20 — The good one
[CARD: "Rule 59 · Gitignore keys from day one · 71.0"]

`.gitignore` covers `.env*`, keys, certs, and credential files from day one.

Seventy-one. It scores high because it's pertinent to every single repo — there isn't
a project on earth that doesn't have something it shouldn't commit. It's a security
rule, so the downside of skipping it is a leaked credential, and it costs you nothing:
one file, written once, before the first commit. Architecturally it's as simple as a
rule gets — it's just a list of patterns. And "from day one" is the whole trick:
enforce it before there's anything to leak and you never fight history later. Universal,
cheap, set-and-forget. That's a strong rule.

## 1:10 — The bad one
[CARD: "Rule 95 · Plans carry a live Status · 42.5"]

Now the weaker one. "Plans live in a `plans/` directory with a first-line `Status:`
kept current — stale status on shipped work is a process violation."

Forty-two. And it's fair. The idea is right — knowing whether a plan is done or not is
genuinely useful. But look at what drags it down: it's narrow. It only matters if you
keep formal plan docs in a `plans/` folder, which is a personal convention, not a law
of software. And the killer is "kept current." A rule whose value depends on a human
remembering to update a status line every time reality changes is a rule that scores
low on enforceability — nothing catches a stale `Status:` the way a scanner catches a
leaked key. Good intention, hard to enforce, situational. That's a forty-two.

## 2:00 — The lesson
[CARD: "set-once beats keep-current"]

That's the contrast a grade exposes. The best rules you satisfy *once* — write the
gitignore, done forever. The weak ones demand constant upkeep and trust you to never
forget. A rule you can automate or set-and-forget earns its slot; a rule that's really
a chore in disguise is always one busy week away from being ignored. When you write a
rule, ask: do I obey this once, or every single day?

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 59 and 95).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
