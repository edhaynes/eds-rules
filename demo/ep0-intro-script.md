# Episode 0 — "Why I gave my AI 100 rules"
Author: Jason-eds · Draft 1 · ~10 min (~1,400 words at a relaxed pace)

Delivery: Eddie, first person, conversational — same register as Episode 1, just
tighter. Pause at each blank line; those are the card cuts. `[CARD: …]` and
`[B-ROLL: …]` are production cues, **not read aloud**. Spell the URL the way you
did in Ep 1 (it transcribes clean and helps viewers).

---

## 0:00 — Cold open / the hook
[CARD: black → "Ed's 100 Rules" title]

Here's something that should worry you if you let an AI write your code.

Out of the box, a coding model is a C-minus engineer. It was trained on the
average of all the code on the internet — and most code on the internet is
average or worse. So it hardcodes your secret keys. It writes two-thousand-line
files. It force-pushes over your history. It ships the spaghetti and tells you
it's done.

[CARD: split — "C- by default" / "A- with rules"]

I spent a weekend writing it a hundred rules. The same model, with those rules
in front of it, goes from a C-minus to a solid A-minus. I'm going to show you
exactly how — and you're going to be able to do it yourself, on a laptop, for
the price of electricity.

## 0:45 — Who's talking
[B-ROLL: old hardware — mainframe, TRS-80; then TACLANE]

Quick bit about why I get to have opinions about this.

I've been writing software for forty-seven years. I started around ten or
eleven, on university mainframes and a TRS-80 Color Computer. I'm not a hobbyist
who discovered AI last year.

I wrote the first TCP/IP stack inside the TACLANE — General Dynamics, about a
thirty-person team. It was the first network encryptor certified to carry
Top Secret traffic, and thirty years later it's still in production and has sold
into the billions. I built the first certified IPv6 stack at Nortel. I did
real-time and determinism at Wind River, and open source the right way at
Red Hat — which is why you'll hear me say Podman, not Docker, and UBI, not Alpine.

[CARD: "C — but with an object-oriented architecture"]

Here's the lesson that runs under all hundred rules: TACLANE was written in C,
for speed — but it had an object-oriented *architecture*. Every directory had
one header. Every function's job was obvious from its name. Every change to the
device went through range-checks and locks. **Architecture matters more than the
language or the framework.** That's the whole game.

## 2:00 — The problem these rules solve
[CARD: a wall of red flags — "hardcoded key", "2,000-line file", "force-push", "no tests"]

So when AI showed up, I was thrilled and frustrated in the same breath. The
upside is real — these tools are fast, and they're tireless. But the default
output is exactly the spaghetti I spent a career training out of human juniors.

It guesses at file paths. It assumes you're on a Mac. It invents a dependency
with no ARM build and doesn't mention it. It catches an exception and swallows
it silently. It hardcodes "localhost" in eleven places. And it is *relentlessly*
agreeable — it'll tell you a bad idea is a great idea because you seem to want to
hear that.

[CARD: "half this document exists out of frustration"]

Half of this rules document exists because of that frustration. The other half
is the thirty years of discipline that made TACLANE work, written down so a
machine can follow it.

## 3:30 — The big idea
[CARD: "Rules = standing law the agent can't talk its way out of"]

The core idea is simple. The rules are standing law. They sit in front of the
model on every single request, and the agent does not get to negotiate them.

A few examples of what that buys you. **Scan for secrets before every commit —
no scan, no ship.** **Never hardcode a secret; if you find one, stop and flag
it.** **Never delete files, drop a table, or rewrite history without me saying
so out loud.** **Push to main early and often** — and yes, people fight me on
that one, but the messy merges that used to make us hoard local work are exactly
what AI is great at now, so the old reason to wait is gone.

[CARD: "Powell rule: get to 90%, then decide"]

And the rule that governs all the others — I call it the Powell rule. Get to
about ninety percent of what you'd need to make a decision, then *make the
decision*. Below ninety percent, ask a question. Above it, stop gathering and
move. It keeps the agent from both charging off blind and stalling forever.

## 5:00 — Meet the crew
[CARD: the org chart — Jason, Claudius, Claude, Claudina, Linda]

Now, the part people find strange at first, and then can't work without. The
rules run a *team* — five personas, each a role with a temperament. They're not
five models; they're five seats, and you bind whatever model you've got to each
seat.

[CARD: "Jason — Project Manager"]

The one at the keyboard most is Jason — the project manager. Jason is fast and
decisive: he scopes the work into small sprints, runs the heavy thinkers as
subagents, holds the through-line, and does *not* write production code. Jason
is named after a real person — the lead architect on TACLANE. At least
twenty-five of these hundred rules are really his.

[CARD: Claudius / Claude / Claudina / Linda, one line each]

Then there's Claudius — the architect, thinks long and deep, plans before anyone
writes a line. Claude — the backend dev, slow and careful, who searches for a
high-quality open-source solution before writing anything original. Claudina —
frontend, who won't ship unless it runs on Windows, Mac, iOS, and Linux. And
Linda — research and go-to-market, fast and wide, the one who tells me who this
is even for.

[CARD: "a small model can be the manager"]

And here's the twist that makes it cheap: the *manager* doesn't have to be huge.
An eight-billion-parameter model, trained on the rules, makes a perfectly good
Jason. He manages the expensive models so you don't have to.

## 7:00 — What the rules actually are
[CARD: the rule categories]

So what's actually in the hundred? They're grouped. There are hard rules you
never break — secrets, destructive actions, version control. There's a whole
section that says **zero hardcoded values** — every host, port, model name, and
timeout flows through one config layer with a sane local default. There's
testing: define the contract first, then write tests against it, and hit a
hundred percent line *and* branch coverage. Cross-platform, every time. Small
files, small functions, no god classes.

[CARD: "100 — a hard cap"]

And the number is a hard cap. A hundred. Not because a hundred is magic, but
because the cap forces consolidation — every time I want to add one, I have to
earn it by merging or cutting another. Rules documents that only grow become
documents nobody reads.

## 8:30 — The plan, and the ask
[CARD: "one rule a day · 100 days"]

Here's what I'm going to do. One rule a day, for a hundred days. Each one short —
what the rule is, why it's there, and the scar that taught it to me. By the end
we'll have walked the whole hundred together.

[CARD: the local-model demo still / "seeing is believing"]

And I'm not going to just assert that this works. I trained a local model on
these rules — you'll see it catch a hardcoded key and quote the exact rule it
breaks, while the vanilla model shrugs. With rules, seeing is believing.

[CARD: github.com/edhaynes/eds-rules · CC-BY · "Built with Bard"]

It's all open source — Ed's 100 Rules, on github.com/edhaynes — that's
H-A-Y-N-E-S — slash eds-rules. The license is CC-BY, so take what works and fork
what doesn't. Plenty of you will disagree with some of these, and I want that:
comment on the repo, tell me where I'm wrong, tell me which rule belongs in the
top hundred that I missed. I've been doing this forty-seven years and I'm still
learning.

So — let's start at rule one tomorrow. Thanks a lot, and I'll see you then.

[CARD: end — "Episode 1 → Rule 1" · subscribe]

---

### Pacing / production notes
- ~1,400 words ≈ 9–10 min at a relaxed pace; if it runs long, the bio (0:45) and
  the rules-categories (7:00) are the safe trims.
- 14 card cues marked — same `build-episode1.py` pipeline (Scribe → beat map →
  render → mux) builds it once you record.
- Claims are all from your own bio; confirm the TACLANE team size / "billions"
  framing before publish if you want to be conservative.
