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

## ② Idempotency — the world moved, more than a blind spot.

Idempotency is a *distributed-systems / unattended-ops* concern: retries,
at-least-once delivery, resumable jobs, declarative reconciliation. In RTOS/embedded
you **controlled execution** — a function runs once, deterministically. "The process
dies halfway and is re-run" is a cloud/CI/**agent** reality. It bit the voicelab
setup script the same day — and bit because the *agent* fire-and-retries.
**Medium-occurrence but rising fast**, precisely because of how AI agents work.

## ③ Performance budget — missed because you'd never violate it.

Determinism and latency are the author's *core* values (Wind River, on-prem
efficiency). No rule existed because the value is so internalized it never got
written down — you author rules for the mistakes that actually happen, and you'd
never ship sloppy latency. The trap: **agents don't inherit your reflexes.** Claude,
left alone, writes the O(n²) loop and never checks the clock. Graded lowest of the
three (51.5) because for *you* its pertinence is near-zero — but for your *executors*
it isn't. Action: externalize tacit expertise into enforced gates.

## The through-line

All three sit in the gap between the author's mental model — *deterministic
execution, a trusted boundary, a single expert operator* — and the new reality:
*untrusted input, unattended retrying agents, and a non-expert AI doing the typing.*
The rules are excellent at the disciplines the author practices; the gaps are
exactly where the agent era introduces failure modes the prior decades never had to
defend, because the machine, the network edge, and the execution were all under one
expert's control.
