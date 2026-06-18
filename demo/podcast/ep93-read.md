# Episode 93 — read script (clean teleprompter, ~5–7 min)

GOOD: Rule 20 — Zero hardcoded values (74.0) · BAD: Rule 13 — Five roles; human is final (33.5)
[YOUR STORY] = riff in your own words; that's where the time comes from.

---

Episode ninety-three.

Every rule I've got, I had graded — cold, against a rubric. Yesterday was the
number-two rule on the board. Today it's the number-three rule, up against the
ninety-eighth. One of them stops your code from rotting the day the world changes
around it. The other is the constitution of my little crew. Same list. Very
different jobs.

The good one first. Rule twenty: zero hardcoded values for anything that could
plausibly change — hosts, ports, model names, paths, timeouts, retry counts,
feature flags, prompts. Pull every one of those out of the code and into config.

It scores a seventy-four. Top of the configuration section, and third on the whole
board. And the reason it sits that high is simple: hardcoding is the single most
common way LLM-written code goes wrong. The AI bakes a port, a model name, a
timeout straight into a function — and now that code only runs in the exact world
it was written in. Move it an inch and it breaks.

[YOUR STORY — the hardcoded value that bit you. The port that was fine until it
wasn't. The model name buried three functions deep that took an afternoon to find.]

Pull every one of those out into config and the same binary runs on my laptop, in a
container, in the cloud — no edit. That's the whole game. That's the difference
between code you *wrote* and code you *own*. Code you wrote runs where you wrote it.
Code you own travels.

And here's why it matters double with an agent at the keyboard. An AI loves a magic
number. It'll inline a timeout because inlining is the shortest path to "it works on
my machine right now." It isn't thinking about the container, or the next deploy, or
the day the endpoint moves. It's optimizing for the demo. So the rule has to be
absolute — zero hardcoded values, full stop — because the agent will never feel the
pain that teaches a human to stop doing it.

Obeying it is mechanical, which is the point. One config layer. Environment
variables, a dot-env-example that documents every knob, sane defaults so the thing
runs locally with no setup. The values live in one place you can read top to bottom.
Nothing important is hiding in a string literal.

That's the gold. Now the basement.

Rule thirteen: five roles, and the human is final. My crew is five fixed personas
plus one human — me. My rulings are final and canonical; any persona's plan,
preference, or pushback yields to the call I make. With one carve-out — Jason's
allowed to push back when a new ruling fights the canon.

It scores a thirty-three and a half. Ninety-eighth out of a hundred. And honestly?
Fair. It's a good governance principle — it's just *mine*. It scores low because
it's about the shape of my team, not about software. Swap your own name in and it
still means something, so it's not pure trivia — but it's organizational, not
technical. It doesn't generalize, and an AI can't really *violate* it the way it
violates a hardcoding rule.

[YOUR STORY — why one human stays final. The decision you'd never hand to a vote of
agents. The time "the human is final" actually saved you.]

And that's a diagnosis, not a takedown. A rule scores low on my rubric for two
specific reasons. One: generality — does it apply to anybody but me. Two: would an
AI ever break it unprompted. Rule thirteen fails both. No agent is going to wake up
and violate "the human gets the final word" — that's not a rule you can break, it's
the frame the whole crew runs inside. So it sits near the bottom. And it should.

Here's the contrast — the whole reason you grade your own rules. Rule twenty makes
your *code* portable: it travels to any machine anybody runs it on. Rule thirteen
makes my *team* coherent, and only my team. A grade isn't a value judgment on the
rule. It's a measure of how far the rule reaches. One reaches everybody. One reaches
my desk.

That's the difference a number exposes that an opinion hides. Seventy-four means: do
this, no matter who you are. Thirty-three means: this is how one guy runs his crew —
borrow it if it fits, ignore it if it doesn't.

That's episode ninety-three. Tomorrow — hooks before your first commit, against how
deep an architect ought to think. See you then.
