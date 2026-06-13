# Why these three rules were missing — a reflection

On 2026-06-13 three rules were added to close gaps in the 100: **input-security**
(rule 3), **idempotency** (rule 47), and a **latency/performance budget** (rule 76).
Eddie asked the right question: *why did I miss these — do they just not occur, or
is it something to focus on?* They aren't random omissions; they map onto a 47-year
career, and each has a different cause.

## ① Input-security — a real blind spot. Focus here.

**Eddie's own diagnosis (the primary cause):** *"I'm the main consumer of my own
software, so I self-regulate my prompt."* When you are the only user, the trust
boundary **collapses** — every input is your input, trusted by definition, so the
rule never bites. It reappears the moment a *second* user, or a file/URL/API payload
from anywhere, touches the system. Pertinence therefore scales with how many
not-you inputs reach the code: low for a personal tool today, high the instant it
ships to someone else or meets the open internet. (That's why it grades 79 — real,
but below the secret rules — rather than 90+.)

**The testing gap he named:** he *did* do monkey testing — good instinct toward
robustness — but monkey/fuzz testing throws *random* input and finds crashes, not
attacks. An attacker isn't random; they craft `'; DROP TABLE`, `../../etc/passwd`,
`$(rm -rf)`, and random input essentially never lands on those exact strings. Monkey
testing proves *robustness*, not *security*. The rigorous version is adversarial:
injection test cases, a security-aware fuzz corpus, or the rule-3 disciplines up
front (parameterize, confine paths) so the bug class can't exist.

**Contributing factor (background):** the author's security tradition is
**confidentiality** — TACLANE, Nortel, network encryptors: protect the key, encrypt
the channel, don't let the secret escape (hence ten leakage rules). The
injection/untrusted-input model is the **web/multi-tenant app-sec** tradition
(OWASP), never the home turf; in defense/embedded, inputs arrive from a known peer
over a fixed protocol behind a defined boundary — the encryptor *is* the boundary.

**Occurs constantly once exposed** (top web-vuln class; agents introduce it by
default). Action: internalize "the attacker controls the input," and test for
malice, not just chaos.

## ② Idempotency — NOT a blind spot. Tacit mastery, never written down.

**Eddie's correction:** *"I preach idempotency up and down — a key attribute of
Ansible."* Right. This was never an ignorance gap. Idempotency is *the* defining
property of Ansible (declarative, converge-to-desired-state, safe to re-run), and
this repo already earmarks an Ansible/Day-2 chapter (F12) where idempotency is the
philosophical anchor. So why was it missing as a *rule*? Same reason as the
performance budget below: a principle known so cold — and already slated to arrive
*via Ansible* — that it never got pulled out as its own discrete, agent-facing line.
Making it rule 47 lifts it from "implied by Ansible" to an explicit gate **every**
operation must meet, Ansible in the stack or not — it wasn't, in the voicelab setup
script that tripped on it the same day. **Occurrence: you'd never violate it; your
agents will, at deploy/migration/script boundaries, unless it's an explicit gate.**

## ③ Performance budget — missed because you'd never violate it.

Determinism and latency are the author's *core* values (Wind River, on-prem
efficiency). No rule existed because the value is so internalized it never got
written down — you author rules for the mistakes that actually happen, and you'd
never ship sloppy latency. The trap: **agents don't inherit your reflexes.** Claude,
left alone, writes the O(n²) loop and never checks the clock. Graded lowest of the
three (51.5) because for *you* its pertinence is near-zero — but for your *executors*
it isn't. Action: externalize tacit expertise into enforced gates.

## The through-line

Only **one** of the three was a true blind spot — **input-security** — and even
that for a rational reason (sole consumer, collapsed trust boundary). The other two
were never gaps in the author's *knowledge*: idempotency he preaches (Ansible), and
latency/determinism is his life's work. They were missing as **rules** because of a
subtler trap — **tacit mastery you never have to write down for yourself.** You
author rules for the mistakes that actually happen to *you*; you'd never violate
these, so they stayed implicit.

The catch: **a non-expert AI executor doesn't inherit a 47-year reflex.** Claude,
left alone, writes the unbatched query, skips the re-run check, interpolates the
untrusted string — not from malice, from having none of the instinct. So the real
lesson isn't "you have blind spots" (you mostly don't); it's *externalize the
expertise that lives in your hands into explicit, enforced gates*, because the agent
era moved the typing to someone who can't feel when a rule is being broken.
