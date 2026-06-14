# Episode 105 — "Proof it works vs my favorite tools"
Author: Jason-eds · Draft 1 · ~2.5 min

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Each episode pairs the day's **good rule** (top of the leaderboard) with a **bad rule**
(bottom) — the contrast is the hook.

- GOOD: Rule 7 — *Green commit; healthy handover* (score 64.0)
- BAD:  Rule 49 — *Podman / UBI / OpenShift* (score 45.0)

---

## 0:00 — The hook
[CARD: "64.0  vs  45.0"]

Two rules graded on the same rubric. One scored a sixty-four, one scored a forty-five.
The good one is about proving your work actually runs before you call it done. The
weak one is about which container tools I happen to prefer. That gap — between proof
and preference — is the whole episode.

## 0:20 — The good one
[CARD: "Rule 7 · Green commit; healthy handover · 64.0"]

Green before commit, healthy before handover: never commit while tests fail, and never
present a service as done without verifying it is up, healthy, and answering a real
request.

It scores in the sixties because it kills the most common lie in software: "it works."
A passing build that nobody ran. A green exit code that was really a piped command's
exit code. The rule forces a real signal — tests actually green, the service actually
up, a real request actually answered — before anything moves forward. It's strong on
pertinence and enforceability: you can check it mechanically, and it applies to every
project that ships anything. Where it loses a few points is generality — "healthy
handover" leans toward service work, less so a pure library — and architectural reach;
it's discipline more than design. Still, high-value, hard to argue with.

## 1:10 — The bad one
[CARD: "Rule 49 · Podman / UBI / OpenShift · 45.0"]

Now the weaker one. "Container-friendly by default: config from env or mounted files,
logs to stdout, no assumed persistent disk. The container stack is Podman, Red Hat UBI
base images, and OpenShift — rootless and daemonless beats a root daemon. Tough luck;
if you prefer Ubuntu, Arch Linux, and Docker's insecure daemon, write your own rules —
the license lets you."

Forty-five. And here's the honest read: this rule is two rules wearing one coat. The
first half — config from env, logs to stdout, no assumed disk — is solid, universal,
twelve-factor container hygiene that scores well anywhere. The second half names my
specific stack: Podman, UBI, OpenShift. That part is preference, not principle. It's
defensible — rootless and daemonless genuinely is a better security posture — but it's
opinionated and shop-specific, and the rubric reads that as low generality and low
enforceability. An AI can't really "violate" your tool preference. So a great first
half gets dragged down by a second half that's a config binding dressed as a law.

## 2:00 — The lesson
[CARD: "principle vs preference"]

That's what the grade exposes. A rule that demands *proof* — show me it runs — is
universal and enforceable, and it scores. A rule that demands a *brand* — use my tools
— is taste, and taste doesn't generalize. The fix isn't to delete it; it's to split
it: keep the portable hygiene as the rule, and move the tool choice to where config
belongs. Proof earns a slot on a hundred-rule list. Preference earns a footnote.

---

### Notes
- GOOD/BAD text = verbatim from RULES.md (rules 7 and 49).
- Scores from `quality/grades.csv`. Rubric dimensions: pertinence, security,
  cost-effectiveness, architectural simplicity, enforceability, generality.
- Tone: honest, no false drama — a weak rule isn't trashed, it's diagnosed.
