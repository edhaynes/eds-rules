# Cost & power: local rules-Llama vs. a frontier API

The teaser's punchline. **Every number below rests on the stated assumptions —
change the assumptions, change the numbers.** Pricing is authoritative (Claude
API reference, cached 2026-06-04); the local figures are electricity only.

## Assumptions (one heavily-AI-assisted developer)
- **Volume:** 2,000 model calls/day, averaging 5,000 input + 1,000 output tokens each.
  → 12M tokens/day → **2.5B input + 0.5B output tokens/year** over 250 working days.
- **Local box:** the 8B runs on hardware you already own (Mac, or the GB10/Gladius).
  Sustained inference ~75 W; assume 8 h/day under load → 0.6 kWh/day → **150 kWh/year**.
- **Electricity:** $0.20/kWh (US average is lower; CA/MA higher — pick your rate).

## Cloud API cost (per developer, per year)
| Model | Input (2.5B × $/M) | Output (0.5B × $/M) | **Total/yr** |
|---|---|---|---|
| Opus 4.8 ($5 / $25) | $12,500 | $12,500 | **$25,000** |
| Sonnet 4.6 ($3 / $15) | $7,500 | $7,500 | **$15,000** |
| Haiku 4.5 ($1 / $5) | $2,500 | $2,500 | **$5,000** |

## Local rules-Llama cost (per year)
- Electricity: 150 kWh × $0.20 = **~$30/year** (8 h/day). Even 24/7 at 75 W ≈ 657 kWh ≈ **~$130/year**.
- Hardware is a one-time, already-owned, sunk cost — not in the annual figure.

## The headline
- **vs Opus 4.8:** ~$25,000 → ~$30  →  **~800× cheaper** (≈80× even at 24/7 power + a hardware amortization).
- **vs Sonnet 4.6:** ~500× cheaper.
- **vs Haiku 4.5:** ~$5,000 → ~$30  →  **~160× cheaper.**
- Conservative teaser claim: *"a few dollars of electricity a year vs. a metered bill in the thousands."* True across all three tiers at this volume.

## Power, honestly
- **Local footprint is fully quantifiable and yours:** ~150 kWh/yr (8 h/day) — about what
  a typical US refrigerator draws in two to three months. It is grid-billed, on-prem, and
  under your control.
- **The cloud alternative's energy is opaque** — Anthropic does not publish datacenter
  energy-per-token, so a direct watt-for-watt comparison would be fabricated. We do **not**
  claim a specific cloud kWh number. The honest framing: the local job's energy is small,
  measurable, and local; the cloud job's energy is someone else's datacenter and shows up
  as a dollar bill, not a meter you read.

## Caveats (say these out loud in any serious version)
- **Not apples-to-apples on capability.** A frontier model is far more *generally* capable
  than an 8B. The claim is narrow and true: **on this specific task — knowing and enforcing
  *your* rules — a small model properly trained wins on cost and locality.** It is not "Llama
  beats Claude at everything."
- The "properly trained" model is the **fine-tuned** one (Way 2), which lives on Gladius
  (currently shelved/unreachable). The model demoable today is the **prompt-baked** one
  (Way 3) — strong on violation detection, shaky on exact rule numbers.
- Volume is the dominant lever. At 50 calls/day instead of 2,000, the API tiers drop to
  ~$125–$625/yr and the multiple shrinks — still local-favorable, but state your real volume.
