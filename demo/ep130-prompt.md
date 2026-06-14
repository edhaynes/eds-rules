# Episode 130 — "One good dependency beats five clever seams"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 86 — *Stdlib plus one; not five* (score 58.0)
- BAD:  Rule 44 — *Storage goes through adapter* (score 51.5)

---

## 0:00 — The hook
[CARD: "58.0  vs  51.5"]

Two rules, both about keeping a codebase clean. One tells you how to pick a
dependency; the other tells you how to hide your storage. Six points apart on the
grade — and that gap is the whole lesson about when discipline pays and when it's
just ceremony.

## 0:20 — The good one
[CARD: "Rule 86 · Stdlib plus one; not five · 58.0"]

Prefer stdlib plus one well-maintained dependency over five small ones.

Fifty-eight, and it earns it on cost-effectiveness and architectural simplicity.
Every dependency you add is a supply-chain door, a license to audit, an ARM build
to pray for, a thing that breaks at 2am. The rule is pure subtraction: lean on the
standard library that already shipped tested, and when you do reach outside, reach
once for something maintained instead of five times for npm confetti. It's general —
applies to any language with a stdlib and a package manager — and it's pertinent,
because the default LLM move is to bolt on a micro-library for every line. Where it
gives up points is enforceability: "well-maintained" is judgment, not a check you
can fail in CI. You can't lint taste.

## 1:10 — The bad one
[CARD: "Rule 44 · Storage goes through adapter · 51.5"]

Now the one that scored lower. "Storage goes through an adapter: no
`open(\"./data/...\")` outside it, no hardcoded buckets, regions, or account IDs."

Fifty-one and a half. And it's not wrong — it's the right instinct, swappable
storage behind an interface, local FS in dev, a bucket in the cloud. The trouble is
generality and architectural simplicity both take a hit. It's prescriptive in a way
that only fully pays off once you actually run on two storage backends; for a project
that's SQLite-and-done, the adapter is a layer of indirection you wrote for a future
that never arrives. And the second half — no hardcoded buckets, regions, account IDs —
is really the no-hardcoding rule wearing a storage costume, so it's part doctrine,
part overlap. Good advice, narrower reach. That's a fifty-one.

## 2:00 — The lesson
[CARD: "subtract by default; abstract when it pays"]

That's the six points. The strong rule makes the codebase smaller — fewer deps,
less surface, less to break. The weaker one makes it bigger on the bet you'll need
the flexibility later. Both are about cleanliness, but subtraction is universal and
the right kind of abstraction is situational. Reach for one good thing before five
small ones — and build the seam only when something on the other side of it is
actually moving.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rule 86 "Stdlib plus one; not five" =
  "Prefer stdlib plus one well-maintained dependency over five small ones"; rule 44).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
