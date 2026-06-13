ED'S 100 RULES — EPISODE 0 — reading script (~10 min)
Read straight through. (Parenthetical headers are signposts — don't read them.)
Pause at the blank lines. Natural pace; ~10 min.

----------------------------------------------------------------------

(90 — cold open)

Ninety. It's a number I keep coming back to, and it's no accident.

It's my class number — United States Naval Academy, Class of 1990.

It's a right angle. Ninety degrees is what makes a corner true — the thing every square structure, every sound building, every honest joint is measured against. Off by a few degrees and the whole thing racks out of true. Good code is the same. Good architecture is the same.

And it's the rule that governs all my other rules: the ninety-percent rule. Get to about ninety percent of what you'd need to make a decision — then make the decision. Below that, ask a question. Above it, stop gathering and move. It's the cure for both charging off half-blind and for stalling forever waiting to be certain.

Here's the part I didn't appreciate at the time. As a midshipman, I was there when Admiral William Crowe handed the Chairmanship of the Joint Chiefs of Staff to General Colin Powell. Little did I know I'd spend the next thirty-five years building my whole way of working around something Powell wrote down. His version was the forty-to-seventy rule — gather forty to seventy percent of the information, then trust your gut; wait for a hundred and you've waited too long. I've pushed it tighter for working with AI, where a wrong guess is cheap to catch — I call mine ninety percent — but it's his idea, and I've never found a better one.

(The three C's — who's talking)

Let me be honest about how I'm qualified to do this. It comes down to three C's.

The first: I was a C student in algorithms. The elegant proofs were never how my brain worked. I was a hacker — I got the thing running.

The second: I spent my career in C, the language, and for years I was bad at object-oriented design. My code worked and it shipped, but "clean" was not the word anyone used for it.

And yet — that C student, that hacker, wrote the first TCP/IP stack in the first encryptor ever certified to carry Top Secret traffic. Because shipping real systems isn't about the grade in algorithms. It's about judgment, and scars, and knowing what actually breaks at three in the morning.

The third C is Claude. Claude covers my first two — it's better at algorithms than I ever was, and it writes cleaner object-oriented code than I do on my best day. A brilliant, tireless junior engineer.

But Claude has never been paged at three a.m. It hasn't shipped an embedded system that has to run ten years without a reboot, or had a security certification ride on its code, or designed for high availability where downtime isn't an inconvenience — it's mission failure. That's my half: the practical experience, the embedded discipline, the security instinct you only earn the hard way.

Alone, I'm a C student who got lucky with judgment. Alone, Claude is an A-plus intern with no scars. Neither one ships A-minus software by itself. Together — with a hundred rules as the contract between us — we do. That's the whole project.

(The problem)

Because here's what an AI does by default. It was trained on the average of all the code on the internet, and most of that is average or worse. So it hardcodes your secret keys. It writes two-thousand-line files. It guesses at paths, assumes you're on a Mac, invents a dependency with no ARM build and doesn't mention it, swallows errors silently. And it is relentlessly agreeable — it'll call a bad idea a great idea because you seem to want to hear that. Half of these rules exist out of that frustration. The other half is thirty years of discipline, written down so a machine can follow it.

(The big idea — and the rules)

The core idea is simple. The rules are standing law. They sit in front of the model on every request, and the agent does not get to negotiate them. Scan for secrets before every commit — no scan, no ship. Never hardcode a secret. Never delete files or rewrite history without me saying so out loud. Define the contract first, then test against it — a hundred percent coverage, branches included. Push to main early and often — people fight me on that one, but the messy merges that used to make us hoard local work are exactly what AI is great at now. And the number is a hard cap: a hundred. The cap forces consolidation — to add a rule, I have to earn it by cutting another.

(The crew)

The rules run a team — five personas, each a role with a temperament, and you bind whatever model you've got to each seat. Jason, the project manager — fast, decisive, scopes the work, holds the line, doesn't write code; he's named after the lead architect on that encryptor. Claudius, the architect, thinks long and deep. Claude, the backend developer — careful, and reuses great open source before writing anything new. Claudina, frontend, who won't ship unless it runs on every platform. And Linda, research and go-to-market, who tells me who this is even for. And here's the twist that makes it cheap: the manager doesn't have to be huge. A small model, trained on the rules, makes a perfectly good Jason — and he manages the expensive models for you.

(The plan — and the proof)

So here's the plan. One rule a day, for a hundred days. Each one short — what it is, why it's there, and the scar that taught it to me. And I won't just assert that it works. I trained a local model on these rules, and you'll watch it catch a hardcoded key and quote the exact rule it breaks, while the vanilla model just shrugs. With rules, seeing is believing. It's all open source — Ed's 100 Rules, github.com/edhaynes — that's H-A-Y-N-E-S — slash eds-rules. The license is CC-BY, so take what works and fork what doesn't. Comment on the repo, tell me where I'm wrong, tell me which rule I missed. Forty-seven years in, and I'm still learning.

(The crest — a small-world closer)

One last thing, and it's genuinely strange. That's my class crest — Naval Academy, Class of 1990, our motto Vidimus, Venimus, Vicimus: we saw, we came, we conquered. And there it is, framed on the wall, behind a congresswoman from South Carolina doing a TV hit. She's The Citadel, Class of 1999 — a fine institution. Wrong school. And wrong decade. How did my class crest end up on her wall? I have no idea, and I'm not accusing anyone of anything — probably a gift to some congressman whose office she borrowed. I'm just one of nine hundred-odd of us who did a hard double-take. If you know the story, drop it in the comments. Small world.

So — rule one, tomorrow. Thanks a lot, and I'll see you then.
