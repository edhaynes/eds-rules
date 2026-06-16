# Outreach drafts — Ed's Rules

Ready-to-send copy for the free/earned plays and paid inquiries. Edit the bracketed bits.
Plain text so it pastes clean.

## The hook (reusable one-liner)
> A small local model (Llama 8B) that's read 100 coding rules out-codes a frontier model
> that hasn't — and there's a sizing law behind it: a model reliably holds about one rule
> per billion parameters, so you slice the rules across a crew of small models and page the
> rest into context. Open source, CC-BY, runs on-device.

## Earned coverage — research newsletters (Import AI, Ahead of AI, Davis Summarizes Papers)
Subject: Small-model coding rules + a "1 rule per billion params" sizing law

Hi [name],

I publish "Ed's Rules" — an open-source (CC-BY) rule set for AI coding agents, distilled
from ~47 years of building (first TCP/IP stack in the TACLANE encryptor; first certified
IPv6 stack at Nortel; Wind River; Red Hat). Two results your readers might find worth a line:

1. A local Llama 3.1 8B with the rules in front of it catches a hardcoded key, names the
   exact rule it breaks, and refuses to invent a rule that doesn't exist — the same weights
   without the rules do none of that. 2-min demo: https://youtu.be/rmMGM460FMw
2. A taxonomy that treats rules as a cache hierarchy: a small immutable axiom core plus
   composable preference layers, sliced per model by a ~1-rule-per-billion-parameters
   budget so a 3-model crew "remembers" ~60 rules and pages the rest. Synopsis (PDF):
   https://github.com/edhaynes/eds-rules/releases/download/rules-synopsis-2026-06-16/eds-rules-synopsis.pdf

Repo: github.com/edhaynes/eds-rules. Happy to share data, the rubric, or the training setup.
No ask beyond a look — thought it fit your beat.

— Ed Haynes

## Hugging Face Daily Papers (free, high-leverage)
- Within 14 days of any arXiv post, submit it at huggingface.co/papers (Submit).
- Claim authorship; link the model + a Space running the 8B-with-rules demo.
- Post the demo + sizing-law figure; rally a few early upvotes day-one (timing matters).

## Paid sponsorship inquiry (Practical AI / AlphaSignal / Cooper Press)
Subject: Sponsorship inquiry — Ed's Rules (open-source AI-coding rules)

Hi [name],

Interested in a [single episode ad read / secondary newsletter slot / classified] for
"Ed's Rules," an open-source rule set for AI pair-programming with a local-small-model
angle (8B + rules beats a frontier model with none). Audience fit looks strong with your
[AI-engineering / ML-research / OSS-dev] readers.

Could you send your current rate card and next available slots? Budget is modest and
we're testing one placement before scaling. Demo + repo: youtu.be/rmMGM460FMw ·
github.com/edhaynes/eds-rules

Thanks,
Ed Haynes

## Sequencing (cheapest first)
1. HF Daily Papers submit + the 3 earned-coverage pitches (free).
2. One Open Collective README sponsorship (~$500/mo) on an AI-tooling project.
3. One transparent paid test: Practical AI ($1,200) or Cooper Press classified ($180–250).
4. Scale what moves the GitHub-stars / video-views needle.
