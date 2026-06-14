# Episode 115 — "Run it five times, or run it once"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 47 — *Idempotent; safe to re-run* (score 61.5)
- BAD:  Rule 45 — *Same code on-prem or cloud* (score 47.5)

---

## 0:00 — The hook
[CARD: "61.5  vs  47.5"]

Two rules about making software behave the same way twice. One scored a sixty-one,
one scored a forty-seven. They sound like cousins — but one is a hard law for any
system, and the other only really lands if you build the way I build. Here's the gap.

## 0:20 — The good one
[CARD: "Rule 47 · Idempotent; safe to re-run · 61.5"]

"Make every operation idempotent and safe to re-run. Deploys, migrations, and setup
scripts must converge to the same state run once or five times, and resume cleanly
after an interruption — a half-finished run is the normal case, not the exception.
Gate on the real end-state, never on a partial artifact that merely looks 'done.'"

It scores in the sixties because it's the rule that saves you on the worst day. Things
get interrupted — a network blip, a killed pipeline, a deploy that dies halfway. If
your script can't be run again safely, that half-finished run becomes a manual cleanup
job at the worst possible moment. Idempotency makes "just run it again" the answer to
almost everything. It's pertinent to deploys, migrations, setup — universal stuff. It's
cheap to design in and brutal to retrofit. And it's enforceable: you can test it by
running the thing twice and checking the state. High generality, low cost, real teeth.

## 1:10 — The bad one
[CARD: "Rule 45 · Same code on-prem or cloud · 47.5"]

Now the lower end. "The same code runs on-prem or in the cloud with only config
changes — never source changes."

Forty-seven. It's a good principle — I believe it — but the grade is honest about
what it is. It's narrower than it looks. It only earns its keep if you actually ship
to *both* on-prem and cloud; plenty of teams run one or the other and this rule never
fires for them. That's generality docked. And it's hard to enforce — there's no clean
test for "this would still work elsewhere with just config," so you find out you broke
it only when you try to move. Pertinent and architecturally sound, but situational and
slippery to check. That's how you land in the forties.

## 2:00 — The lesson
[CARD: "universal + testable beats sound + situational"]

That's the split the grade exposes. Both rules are correct. But one applies to nearly
every operation you'll ever automate and you can prove you followed it — and the other
is a genuinely good idea that only some shops need and nobody can easily verify.
Universal and testable beats sound and situational, every time. That's why one's in
the sixties and one's fighting for its slot.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 47 and 45).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
