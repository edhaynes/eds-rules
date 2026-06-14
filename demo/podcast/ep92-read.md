# Episode 92 — read script (clean teleprompter, ~5–7 min)

GOOD: Rule 2 — Never hardcode a secret (82.0) · BAD: Rule 18 — Linda searches wide (30.0)
[YOUR STORY] = riff in your own words; that's where the time comes from.

---

Episode ninety-two.

Every rule I've got, I had graded — cold, against a rubric. Today's the number-two
rule on the whole board, up against number ninety-nine. The best secret rule I have,
and one that's basically just me talking to myself.

The good one first. Rule two: never hardcode a secret. No API key, no token, no
password, no private endpoint typed into your source code. And if you find one already
sitting in the codebase — stop, flag it, and never propagate it. Not even for a minute.

It scores an eighty-two. Almost as high as the scan rule, and for the same reason: the
downside is catastrophic and the cost of obeying is nothing. The day you type a key into
a string literal, that key is one commit away from public — forever. There's no "I'll
pull it out later." Later is too late. Bots scrape new commits in seconds, and once it's
touched a hostable git ref, you assume it's copied for good. You don't un-leak a secret.
You rotate it and you live with the scare.

[YOUR STORY — a hardcoded secret you found or nearly shipped. The "temporary" key that
lived forever. The yaml file nobody inspected.]

Here's the part that matters double in the AI era. An AI agent is a champion propagator.
It reads your codebase for patterns and reproduces what it sees. One hardcoded key
becomes the template for the next five files the agent writes. It isn't malicious — it's
consistent, which is worse. A person might feel a twinge copying a credential. The agent
feels nothing. So for an agent the rule is absolute: find a secret, stop, surface it to
the human, touch nothing.

And obeying it is mechanical, which is the point. Secrets arrive through environment
variables, mounted files, or a secrets manager. The repo carries a dot-env-example that
documents what's needed — and nothing else. The real value never lives in the code. Not
in a string, not in a comment, not "just while I test it."

That's the gold. Now the basement.

Rule eighteen: Linda searches wide. Linda's my research persona — fast, web-capable,
sweeps broad: marketing, competitors, features. Breadth first, depth on request.

It scores a thirty. Second from the bottom. And honestly? Fair. It's not wrong — it's
narrow. It only means anything if you've built my exact five-persona crew. For everybody
else, "Linda searches wide" isn't a law. It's a footnote about how one guy organized his
AI team.

[YOUR STORY — why you built the crew. What Linda actually saves you. The moment a
persona earned its keep.]

And that's a diagnosis, not a takedown. A rule scores low on my rubric for two specific
reasons. One: generality — does it apply to anybody but me. Two: would an AI ever break
it unprompted. Linda fails both. Claude is never going to wake up and violate "Linda
searches wide" — it's not a rule you can break, it's a description of a workflow. So it
sits at the bottom. And it should.

Here's the contrast — the whole reason you grade your own rules. The best ones are
universal and expensive to break: hardcoding a secret can end a company, and it'll do it
to anybody. The weak ones are situational — they only help inside my exact setup. Same
list. Both earned a slot at some point. But the grade tells you which one belongs on
*your* list, and which one is just mine.

That's the difference a number exposes that an opinion hides. Eighty-two means: do this,
no matter who you are. Thirty means: this is a personal quirk — your mileage may vary.

That's episode ninety-two. Tomorrow — zero hardcoded values, against who gets the final
word on the team. See you then.
