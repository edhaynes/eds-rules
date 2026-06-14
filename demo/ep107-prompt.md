# Episode 107 — "Scan everything vs. budget everything"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 54 — *Scan the whole artifact* (score 63.5)
- BAD:  Rule 76 — *Latency budget; gated like cov.* (score 45.5)

---

## 0:00 — The hook
[CARD: "63.5  vs  45.5"]

Every rule I have got graded. Today two rules about being thorough — one about what you
scan before you ship, one about what you measure before you ship. Same instinct, two very
different grades. Here's why one's solid and one's still proving itself.

## 0:20 — The good one
[CARD: "Rule 54 · Scan the whole artifact · 63.5"]

"Before deploying, scan the full artifact: image build context, manifests, env bindings,
the lot — not just the files changed since last deploy."

It scores a sixty-three because it closes a gap the obvious version of the rule leaves
wide open. Everybody knows to scan their diff. Almost nobody scans the *whole* thing — and
a leaked key doesn't care which commit introduced it. The secret you're shipping might have
been sitting in a manifest for months. It's pertinent to every deploy, it's a pure security
win, and it's dead simple to state: scan all of it, every time. Where it loses a few points
is enforceability — "the full artifact" is a judgment call, and the cost goes up the bigger
your build context gets. But the principle is universal, and the downside of skipping it is
the same catastrophic leak the diff-scan was supposed to prevent. Solid rule.

## 1:10 — The bad one
[CARD: "Rule 76 · Latency budget; gated like cov. · 45.5"]

Now the weaker one. "Declare a latency and throughput budget, then gate regressions against
it the way you gate coverage. Determinism and latency are features: measure them, set the
ceiling explicitly, and fail the build when a change blows past it — a silent slowdown is a
defect that ships."

Forty-five. And I'll be honest about why. The *idea* is right — a silent slowdown really is
a defect, and I believe that. But as a rule it's hard to enforce and it's not universal.
Coverage gating works because coverage is one stable number; latency isn't. It moves with
the machine, the load, the cache, the day. Pin a hard ceiling and you get flaky builds that
fail for reasons nobody touched. Plenty of perfectly good software has no latency budget at
all — a CLI, a batch job, a doc site doesn't need one. So it scores low on generality and on
enforceability: great advice for systems where determinism is the product, a footnote for
everything else. Right call, narrow scope.

## 2:00 — The lesson
[CARD: "a good principle isn't always a good gate"]

That's the gap the grades expose. Both rules say "be thorough" — but Rule 54 is a thing you
can actually *do the same way every time*, and Rule 76 is a thing you have to tune per
project or it turns into noise. The best rules are easy to enforce and apply everywhere. A
principle you believe in still has to survive being made into a gate — and "fail the build
on latency" is a harder gate to get right than "scan all the files." That difficulty is the
whole forty-five-versus-sixty-three.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 54 and 76).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
