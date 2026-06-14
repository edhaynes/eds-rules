# Episode 111 — "Hermetic tests, and a 'nice if reasonable' default"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 77 — *No network in unit tests* (score 63.0)
- BAD:  Rule 25 — *Zero-setup local defaults* (score 46.0)

---

## 0:00 — The hook
[CARD: "63.0  vs  46.0"]

Every rule I have got graded. Today: one rule that keeps my test suite honest, and one
that sounds great until you ask who's actually going to enforce it. Same list, seventeen
points apart. Here's what those seventeen points are made of.

## 0:20 — The good one
[CARD: "Rule 77 · No network in unit tests · 63.0"]

77. No network calls in unit tests — fakes, mocks, and fixtures.

Sixty-three because it's the rule that decides whether your suite is a test or a coin
flip. A unit test that hits the network isn't testing your code — it's testing your code,
plus somebody's API, plus DNS, plus the WiFi at the cafe. It fails for reasons that have
nothing to do with you, so people start ignoring red. It scores high on pertinence —
every project with tests has this exact temptation — and on architectural simplicity:
the moment you have to mock the network, you're forced to put a seam there, and that seam
makes the whole design cleaner. It's also dead easy to enforce: ban the socket in the
test runner and the violations announce themselves. Cheap to keep, expensive to skip.

## 1:10 — The bad one
[CARD: "Rule 25 · Zero-setup local defaults · 46.0"]

Now the soft middle of the board. Rule twenty-five:

25. Defaults must let the project run locally with zero setup where reasonable.

Forty-six. And honestly? Fair. I love this rule — clone, run, it works, no config
scavenger hunt. But look at the wording: "where reasonable." That's an escape hatch you
could drive a truck through. A rule an AI can satisfy by deciding it wasn't reasonable
isn't really a rule — it's a preference with good intentions. It scores low on
enforceability, because there's no green-or-red signal for "did you make setup zero." And
it leans on my taste for what counts as a sane default, which drops it on generality.
Great north star, weak law.

## 2:00 — The lesson
[CARD: "a law needs a tripwire"]

That's the seventeen points right there. Rule 77 has a tripwire — open a socket, the test
fails, you got caught. Rule 25 has a vibe. The best rules don't just tell you the right
thing; they make the wrong thing trip an alarm. If you can't write the check that catches
the violation, you haven't written a rule yet — you've written advice.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 77 and 25).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
