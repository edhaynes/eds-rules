# Episode 112 — "The chore that pays vs the one nobody triggers"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 88 — *Lint + format every commit* (score 62.5)
- BAD:  Rule 65 — *Unique build number* (score 46.5)

---

## 0:00 — The hook
[CARD: "62.5  vs  46.5"]

Two housekeeping rules today, and only one of them earns its rent. One runs on every
single commit and keeps the whole codebase honest. The other matters maybe twice a
year — and a machine ships before you ever feel its absence. Same chore drawer, very
different grades.

## 0:20 — The good one
[CARD: "Rule 88 · Lint + format every commit · 62.5"]

Lint and format on every commit; CI stays green.

Sixty-two, and it's a steady performer across the board. It's pertinent because it
fires on *every* commit — not a special occasion, a heartbeat. It's cheap: the
formatter is a one-line hook, the cost is milliseconds, and the payoff is that nobody
ever argues about whitespace or burns a review cycle on style. Architecturally it's as
simple as a rule gets — one tool, one config, runs itself. And it's general: every
language has a linter and a formatter, so this rule travels to any project you'll ever
start. Where it gives back a few points is enforceability — "stays green" is a promise
a tired human can wave through — but wire it into CI and even that gap closes.

## 1:10 — The bad one
[CARD: "Rule 65 · Unique build number · 46.5"]

Now the lower shelf. "Every build gets a unique, monotonically increasing build number
(`git rev-list --count HEAD` works) — stores reject reused ones."

Forty-six. And it's not wrong — it's just narrow, and it barely defends itself. The
tell is right there in the rule: "stores reject reused ones." This earns its keep when
you ship to an app store that enforces it for you. Off that path — a web service, a
CLI, a library — nothing in your day breaks if the number repeats, so pertinence and
generality both sag. It scores its worst on cost-effectiveness and the will-an-AI-ever-
violate-it axis: the machine that generates the build number is exactly the thing that
makes this rule moot, so it almost never gets violated unprompted. Useful when it's
useful. Just not often, and not everywhere.

## 2:00 — The lesson
[CARD: "every commit > twice a year"]

That's the spread a grade makes visible. The strong rule is something you do constantly
and automatically — high frequency, near-zero cost, travels anywhere. The weak one is a
once-in-a-while requirement that the toolchain mostly satisfies on its own. Frequency
times generality is most of the score, and a rule that only bites at the app-store gate
isn't pulling the same weight as one that runs every time you hit save.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 65, and the "Lint and format on every
  commit" rule graded as 88 in `quality/grades.csv`).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
