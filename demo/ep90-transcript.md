# Episode 90 — transcript
_Transcribed from the recording (ElevenLabs Scribe, 2026-06-13). Lightly raw — speech-to-text artifacts (e.g. "Tackling General Dynamics" = TACLANE, General Dynamics) not corrected._

Ed's 100 Rules, Episode 90.
I know you're saying, "This is the second episode, Ed," but 90 is a number I keep coming back to.
It's my class number.
I went to the United States Naval Academy, class of 1990.
It's a right angle, so, uh, important in geometry.
And it's a rule that in my 100 Rules, uh, 90, the 90 Rule comes first.
It's, uh, Colin Powell's, uh, Rule of 90.
Um, I was there when Admiral William Crowe handed the chairmanship of the Joint Chiefs of Staff to General Colin Powell, and I was in a, uh, I was in the stands, not in a parade.
As a senior, I got to get out of the parade and sit in the stands.
And little did I know that, um, the next 35 years of my life I'd be building around working, that something that Powell had already wrote down.
I hadn't heard of it at that time.
Um, his version was the 40 to 70 Rule.
Gather 40 to 70% of the information, then trust your gut.
Wait for 100 and you've waited too long.
Um, in software there's, uh, less room for error, so I made it the 90% Rule, uh, in honor of my class.
Basically, I tell my AI project managers that if they have a 90% degree of certainty that they know what I would answer to their question, that they just continue on.
And because I've given them 100 very opinionated, uh, rules, they, it knows exactly how I would think on 90% of the stuff, so, uh, hardly ever asks me for questions, which is something that annoys people about AI.
So, the second thing, uh, I'll say is this, like on Sesame Street, this is brought to you by the letter C.
And, um, why am I qualified to do this?
Uh, when I went to Red Hat, it was like I had gone from high school baseball to the pros, and suddenly everyone was a lot smarter than me.
And one thing I was never good at was, uh, algorithms, so I made a C in algorithms.
It was probably the only computer science class I didn't make an A in.
I just struggled with algorithms, I struggled with the tedium of doing the math, and just the hard work it took to do algorithms.
Um, the second C is that I was a C programmer initially.
When I worked for the defense industry, I did one of the first, uh, uh, top secret, um, rated encryptors for the internet.
It was called Tackling General Dynamics in the '90s.
In the '90s.
And, uh, so C programmer.
I was never good at C++.
I did not understand...
I am a word thinker, not a visual thinker.
And that is why I'm unusually good at writing LLM prompts.
Um, LLMs think exactly like I think.
And I know other people like this.
Um, um, one of my kids is like this too.
Steve, on the other hand, is a visual thinker.
Uh, reason I'm collaborating with him is his slides always look fantastic, so that's gets you...
a picture's worth a thousand words, right?
All right.
So the third C is Claude.
Uh, I started using Claude just a few months ago, and Claude makes up for my two deficits.
Claude is fantastic at algorithms, knows...
he's been trained on all the best ones and can pick the right one and implement it correctly almost 100% of the time.
Um, the other thing is object-oriented.
Uh, AI is great at organizing things and understanding relationships, and that's object-oriented.
And I found my architectures became much more powerful when I used AI to help.
It starts off with my scattered, uh, fragments of words architecture and then organize it into something elegant that has the object-oriented, things like polymorphism and everything.
So, um, so we talked about 90, we talked about the three Cs, which is C in algorithms, uh, C programmer in Claude.
Now I'm more like a Python programmer.
Python's pretty neat.
Um, why, why does AI code as a C, uh, average programmer?
Um, the reason is that it was trained on average code.
Every- everyone tried to train with as much stuff as possible.
So any GitHub repo done by a first-year computer science student who copied someone else's bad code and then tried to change it by hardcoding a few things, I mean, that's, uh, 95% of what it's being trained on.
So, um, now there are some models I'd like to investigate.
I think IBM Granite models was done on a very curated, uh, set of I, I would hope, quality code.
And, uh, one of my next projects is to program a 2 billion parameter tiny Granite model to be my project manager by training it with my, uh, 100 Rules.
Should take about half an hour on my, my MacBook.
Um, so why, why 100 Rules?
Uh, starts with the Rule of 90, but the core ideas are simple.
The rules are standing law, and they sit in front of the model on every request.
The agent, um, doesn't negotiate them.
You scan for secrets before every commit.
No scan, no ship.
You never hardcode a secret.
You never delete files.
You don't rewrite history.
You clean up after yourself.
You delete dead code.
When you change an architectural decision, you update and re-version all your documents.
You always increment your version number when you publish.
You always have it visible on the front end so you know what you're dealing with.
Um, push to main early and often.
This is one that people fought me on, but here's the thing.
AI can do merges correctly 95% of the time, so there's no downside to just pushing every piece of work you do to main.
And then if something gets messed up, I-I haven't seen it happen yet, honestly.
Um, so push to main, uh, early and always is what I say.
Uh, and so what I did with my 100 rules, I also created five personas.
So I have a team of AI agents.
It's not just Claude.
I have Jason.
He's the project manager.
He doesn't need to code.
He just organizes.
Claudius, which is the architect.
This is the smartest, longest-running model you have, um, almost always in the cloud.
Um, Claude is the backend developer.
He's careful.
And like me, he always tries to reuse open source projects when possible with lots of GitHub stars.
Uh, Linda does research and go-to-market.
Uh, Linda is based on someone I knew in high school that was very smart and, um, wore glasses and looked like a librarian and was as smart as a librarian.
Um, and, uh, what's neat is a small model trained on the rules makes a perfectly good Ja- Jason, and he manages those expensive models so you can get away with having a $20 a month Claude subscription, only use $20 worth of electricity, not drown the planet in greenhouse gases, right?
So the plan, and I think I can pull this off, and I think most videos are gonna be more like three to five minutes, not this should be around 10 minutes, one rule a day for 100 days.
So me and Steve, maybe we can take turns, give each other a day off, or maybe we all join together.
We'll have special guests from Red Hat or coworkers, and, um, I want to prove to you that each of these rules work.
Not a formal proof, but we'll do like a pseudo-proof of why I think this rule works.
So it's on github.com, edhaynes, that's H-A-Y-N-E-S, /edsrules.
Uh, so y- you can take what you like and fork what you don't like, and I'd really be interested if people, say, you've got...
O- Out of 100, there must be 10 rules that are missing.
I'm interested in wha...
I've ordered them one to 100 and wh- how important I think they are.
I would like someone to find something in the top 20.
I would be really amazed.
Okay, so the last thing is sort of a funny story.
I'm from the Naval Academy Class of 1990, and about six months ago, one of my classmates posted on Facebook, he said, "Why does Nancy Mace have our class crest in her background on this press conference?" And this has happened a few times (laughs) .
We have no idea.
So if the internet knows...
I'm not accusing her of anything.
I think probably it's a colleague's office, but I don't know of any classmates that are Class of '90.
So maybe...
Did Class of '90 ever gift a congressman our class crest?
That would have been a while back.
So I don't know what it's still doing there.
So, um, anyway, if anyone knows, uh, drop a like in the comments, and as always, this is my first podcast, but I- I've heard this a million times.
Subscribe, hit the like button, forward to your friends, make comments, you know, feed the algorithm.
So anyway, but we don't have any ads right now, so um, enjoy.
Enjoy the free video.
Um, and with that, I will drop off.
Have a great day and talk to you tomorrow.
