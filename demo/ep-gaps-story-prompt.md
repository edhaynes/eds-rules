# Episode (story) — "The stuff I missed"
Author: Jason-eds · Draft 1 · ~7 min (target 5–10) · narrative, not a rule pairing

Delivery: Eddie, first person. Blank lines = card cuts. `[CARD: …]` = production cue.
Grounded in `quality/why-these-gaps.md` + `quality/sub-bar-triage.md` — no [FILL] gaps.
Placement: a longer reflective episode; works as a mid-series "behind the rules" break.

---

## 0:00 — I graded my own rules
[CARD: "100 rules · graded"]

I did something uncomfortable. I took my hundred rules — the ones I'd built up over a
forty-seven-year career — and I graded them. Every one, on a rubric. Pertinence,
security, cost, simplicity, enforceability, generality.

And the interesting part wasn't the winners. The secret-scanning rule scored a ninety,
fine, no surprise. The interesting part was the holes. The stuff that wasn't on the
list at all. Because the gaps in a rulebook tell you more about the author than the
rules do.

[CARD: "three things were missing"]

Three things were just… missing. Input security. Idempotency. A performance budget.
And when I asked myself *why* I missed each one, I got three different answers — and
only one of them was the answer I expected.

## 1:00 — The one real blind spot
[CARD: "① input security"]

Input security. Distrusting the data coming into your system — the injected SQL, the
`../../` path, the untrusted string you drop into a shell. That one was a genuine blind
spot, and I had to sit with why.

Here's the honest reason: **I'm the only user of my own software.** When you're the
sole consumer, the trust boundary collapses. Every input is *my* input, so it's trusted
by definition, so the rule never bites. It only wakes up the moment a second person —
or a file, a URL, an API payload from anywhere — touches the system.

[CARD: "confidentiality ≠ input-trust"]

There's a deeper reason too, and it's about where I come from. My security tradition is
*confidentiality* — TACLANE, Nortel, network encryptors. Protect the key. Encrypt the
channel. Don't let the secret escape. That's why I have ten rules about leaks. But the
*injection* model — the attacker controls the input — that's the web, multi-tenant,
app-sec world. Never my home turf. In defense and embedded, the input arrives from a
known peer, over a fixed protocol, behind a defined boundary. The encryptor *is* the
boundary.

[CARD: "monkey testing finds chaos, not malice"]

And one more thing I had to admit. I *did* test inputs — I did monkey testing, throwing
random garbage at it. Good instinct. But random isn't an attacker. Random input
essentially never types `'; DROP TABLE` or `$(rm -rf)` — an attacker types exactly
that, on purpose. Monkey testing proves your code is *robust*. It does not prove it's
*secure*. Those are different words. I'd been hearing them as the same one.

## 3:20 — The two that weren't blind spots at all
[CARD: "② idempotency  ③ latency"]

Now the other two. And this is where it got interesting, because they were *not*
ignorance.

Idempotency — make every operation safe to run twice. I preach that. Up and down. It's
the whole soul of Ansible: declarative, converge to the desired state, re-run it five
times and get the same result. I don't need to be taught idempotency.

Latency and a performance budget? That's my *life's work*. Wind River. Real-time
operating systems, where a late millisecond is a defect. On-prem determinism is the
thing I value most. I would never, ever ship a sloppy O(n-squared) loop and not feel it.

[CARD: "so why were they missing?"]

So if I know both cold — why weren't they rules?

## 4:40 — The trap: tacit mastery
[CARD: "you write rules for the mistakes you make"]

Here's the trap, and I think it's the most useful thing the whole exercise taught me.

**You write rules for the mistakes that actually happen to you.** You don't write down
the thing you'd never get wrong. Idempotency and latency were missing not because I
didn't know them — because I knew them so deeply they'd gone *tacit*. They lived in my
hands, not on the page. Mastery you never have to articulate to yourself.

For forty-seven years, that was completely fine. The expert and the typist were the same
person. If it lived in my hands, it got into the code.

## 5:40 — The catch: the typist changed
[CARD: "the agent doesn't inherit your reflexes"]

And then the AI era moved the typing to someone else. To Claude. To an executor that
has *none* of my instinct.

[CARD: "no malice — no instinct"]

Left alone, the agent writes the unbatched query. It skips the re-run check and the
setup script blows up the second time. It interpolates the untrusted string straight
into the command. Not out of malice — out of having no reflex to violate. It can't
*feel* when a rule is breaking, because it never spent forty-seven years building the
feeling.

That's the catch. All that tacit mastery — the stuff so internalized I never wrote it
down — became invisible exactly when it stopped being in my hands and started being in
the hands of something that can't sense it.

## 6:30 — The lesson
[CARD: "externalize the reflex into a gate"]

So the real job of a rulebook in the AI era isn't to capture your *blind spots*. I
barely had any — only one of the three. The job is to **externalize the expertise that
lives in your hands into explicit, enforced gates.** Take the thing you'd never get
wrong, and write it down anyway — as a rule, a test, a CI check — because the person at
the keyboard now can't feel it the way you can.

[CARD: "mulligans, honestly labeled"]

And grading honestly cuts the other way too. Some of my rules aren't universal law —
they're personal quirks I keep on conviction. My five-persona crew. Podman over Docker.
"No flattery." I call those *mulligans* now — admitted do-overs, your-mileage-may-vary —
and I label them as quirks instead of pretending they're physics. There's still a
handful I owe the list, too: UTC everywhere, least privilege, timeouts and retries,
migrations. The work's not done.

But that's the headline. I didn't have many blind spots. I had a lifetime of reflexes I
never had to say out loud — and a new collaborator who needs every one of them spelled
out. Write down what your hands already know. That's the stuff you miss.

---

### Notes
- Sources: `quality/why-these-gaps.md` (the three gaps + through-line), `quality/sub-bar-triage.md`
  (mulligans, the 5 still-to-add finds). Bio facts (TACLANE, Nortel, Wind River, sole
  consumer, Ansible, monkey testing) are from the canon + gap doc — none invented.
- Apolitical, no copyrighted IP. Tone: reflective, honest, a little self-critical — earns trust.
- Trim levers if you need 5 min: cut the mulligan coda (6:55→end) and tighten §3:20.
- Confirm: "47 years," "only user of my own software," and the monkey-testing admission are
  yours to stand behind on the mic — all drawn from the gap doc, but it's your voice.
