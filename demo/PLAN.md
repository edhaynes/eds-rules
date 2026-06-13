# Status: In Progress — 2026-06-13

# Demo video plan — "Seeing is believing"

Tracks the narrated demo-video work and every decision/parked idea from the
2026-06-13 session, so the through-line survives the burst of tangents.

## Locked deliverable
A **60–90s narrated teaser** of the rules-as-a-model demo.
- **Format:** Eddie records his own full-screen terminal; ElevenLabs voiceover
  added in post; assembled to MP4 by `make-demo-video.sh`.
- **Thesis:** one variable — same Llama 3.1 8B, with the rules vs. without.
- **Tagline:** "Seeing is believing" (Eddie, 2026-06-13).
- **Voice:** ElevenLabs (key in Eddie's `~/.zshrc`, read from env by the script).

## Decisions (this session)
| # | Decision | Status |
|---|---|---|
| 1 | Demo subject = the rules-as-a-model (Way 3 prompt-baked), built & smoke-tested | Done — `model/make-rules-model.sh` |
| 2 | Teaser now; training deep-dive is a separate later segment | Locked |
| 3 | Comparison axis A — isolate the rules: vanilla-Llama vs rules-Llama | **Works today** |
| 4 | Comparison axis B — "small trained beats big": rules-Llama vs vanilla Claude | **Blocked** (see below) |
| 5 | Cost & power savings punchline | Done — `cost-power-savings.md` |
| 6 | Ship the pipeline as repo scripts | Done — `ask-vanilla.sh`, `make-demo-video.sh` |

## Files in this dir
- `narration.txt` — the voiceover script (ElevenLabs input).
- `teaser-runsheet.md` — exact on-camera command sequence + pacing.
- `ask-vanilla.sh` — query a rules-free model (BACKEND=llama default, claude optional).
- `make-demo-video.sh` — ElevenLabs VO + ffmpeg mux → MP4.
- `cost-power-savings.md` — the cost/power estimate with explicit assumptions.

## Blockers
- **Valid `ANTHROPIC_API_KEY`** for any Claude-side comparison (axis B, and the
  Claude half of axis A). The key in Eddie's env (len 46) fails Anthropic auth
  (`invalid x-api-key`) — likely a Claude Code OAuth/subscription token, not an
  `sk-ant-…` Messages-API key. `ask-vanilla.sh BACKEND=claude` is wired and ready
  the moment a real key is exported. Llama-vs-Llama is unblocked and is the more
  rigorous one-variable cut anyway.

## Shelved / parked
- **Training deep-dive (Way 2):** epoch training + reverse-rule-lookup story.
  Source = real artifacts on **Gladius**, which is **unreachable** (Eddie, 2026-06-13)
  — shelved. Will not fabricate epoch logs/loss curves; resume when Gladius is back.
- **"Properly trained beats big Claude"** truthful claim needs the fine-tuned model
  (Gladius) — also gated on the above.

## Honesty guardrails (carry into any cut)
- Llama-8B vs frontier-Claude is **not** apples-to-apples on general capability; the
  claim is narrow: *on knowing/enforcing Eddie's rules*, a small trained model wins on
  cost + locality.
- Prompt-baked (Way 3) is shaky on exact rule numbers — lead with violation detection
  and semantic recall, not number attribution.
- Cost/power numbers are volume-dependent; state the assumption.
