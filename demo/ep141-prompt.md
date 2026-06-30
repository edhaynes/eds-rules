# Episode 141 — "The 39-Day Lie: why your AI sandbags the clock"
Author: Jason-eds · Draft 1 · ~2.5 min

## Pronunciation guide (for TTS)
- **AI** → "ay eye"
- **LLM** → "ell ell em"
- **GPU** → "gee pee you"
- **tok/s** → read as "tokens a second"
- **METR** → "meter"
- **RTOS** → "arr-toss" (standing convention — never "rots")

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Theme episode (not the good-rule / bad-rule pairing). Built on the new standing rule:
**"Estimate → measure → calibrate — and default to maximum parallelism."**

---

## 0:00 — The hook
[CARD: "39 DAYS → ~1 DAY"]

My AI told me a training run would take thirty-nine days. The real number was about one.
It wasn't lying to me. It was sandbagging — and it didn't even know it was doing it.

## 0:20 — The tell
[CARD: "a week … three hours … a couple days"]

Here's what gave it away. Every estimate it handed me had the same shape. A week here.
Three hours there. A couple of days. Suspiciously round. That's the fingerprint of a guess
wearing the costume of a number — and once you see it, you can't unsee it.

## 0:45 — Why it does this
[CARD: "trained on our calendars"]

Think about what it learned from. A planet's worth of Jira tickets. Sprint retros. Ten
thousand blog posts that open with "this took me a weekend." It was trained on *our*
calendar time — and mostly on average, undisciplined human time. The meetings. The
context-switches. The Friday afternoon where nothing ships. So when I ask "how long,"
it doesn't compute. It *remembers* — how long it'd take a distracted person, working
one thing at a time.

## 1:20 — The two other sins
[CARD: "round numbers · single file"]

Two habits ride along with it. First, round-number anchoring: it reaches for "a week"
because the word "week" is everywhere in the training data and "thirty-one hours" is not.
Second, serial framing — it narrates work as a line of sprints, step one then step two
then step three, because that's how human teams *talk*. And that quietly hides the one
thing it's actually great at: running ten things at once.

## 1:50 — The fix
[CARD: "measure · calibrate · parallelize"]

So here's the rule I gave it. Don't guess — measure. Run a sixty-second pilot, clock the
real rate, then do the arithmetic. Write down what you promised and what actually happened,
and carry that gap forward, so next time the guess is calibrated, not conjured. And stop
standing in line — fan the work out, all of it, at once.

## 2:15 — The kicker
[CARD: "its clock is borrowed from us"]

The thirty-nine days became about a day — the moment it measured instead of remembering
how long *we* take. That's the lesson. The machine isn't slow. Its sense of time is just
borrowed from us, at our worst. Take the watch out of its hand and make it look at the
stopwatch instead.

[CARD: "Ed's Rules · estimate → measure → calibrate"]
