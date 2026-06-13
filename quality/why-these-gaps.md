# Why these three rules were missing — a reflection

On 2026-06-13 three rules were added to close gaps in the 100: **input-security**
(rule 3), **idempotency** (rule 47), and a **latency/performance budget** (rule 76).
Eddie asked the right question: *why did I miss these — do they just not occur, or
is it something to focus on?* They aren't random omissions; they map onto a 47-year
career, and each has a different cause.

## ① Input-security — a real blind spot. Focus here.

The doc had ten rules on secret **leakage** and zero on malicious **input**. That
reflects which security tradition formed the author: TACLANE, Nortel, network
encryptors — a world about **confidentiality** (protect the key, encrypt the
channel, don't let the secret escape). The injection/untrusted-input threat model
(SQLi, command injection, XSS, deserialization) is the **web/multi-tenant app-sec**
tradition (OWASP), never the home turf. In defense/embedded, inputs arrive from a
*known peer over a fixed protocol behind a defined trust boundary* — the encryptor
**is** the boundary. In an AI-built web service the input is the open internet.
**Occurs constantly** (top web-vuln class; agents introduce it by default).
Action: internalize "the attacker controls the input."

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
