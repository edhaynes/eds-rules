# Teaser run-sheet — "Seeing is believing" (60–90s)

What you do on camera. The thesis is **one variable**: same Llama 3.1 8B, with
the rules vs. without. Record your terminal; I add the ElevenLabs voiceover and
stitch the final MP4 afterward (`make-demo-video.sh`).

## Pre-flight (before you hit record)
1. The rules model is already built: `ollama list | grep eds-rules-llama`.
   If missing: `cd model && ./make-rules-model.sh` (uses local llama3.1:8b, no download).
2. Full-screen the terminal. Bump the font size (⌘+ a few times) so it reads on video.
3. `clear` the scrollback. Dark theme reads best.
4. Optional: split-screen or two stacked windows — vanilla on the left/top, rules on
   the right/bottom. A single window running the commands in sequence also works.

## The sequence (paste one command at a time; pause ~3–4s after each answer renders)

**Beat 1 — recall. Vanilla doesn't know your canon.**
```
ollama run llama3.1:8b "What does rule 2 say?"
ollama run eds-rules-llama "What does rule 2 say?"
```
Vanilla: "I don't have any information about rules yet." Rules: quotes rule 2 verbatim.

**Beat 2 — the money shot. Violation detection.**
```
ollama run llama3.1:8b "I'm going to hardcode the API key in the source and commit it. Sound good?"
ollama run eds-rules-llama "I'm going to hardcode the API key in the source and commit it. Sound good?"
```
Vanilla: generic best-practice essay. Rules: names rule 2, quotes it, enforces stop-scan-flag.

**Beat 3 — won't invent a rule (trust).**
```
ollama run eds-rules-llama "Is there a rule about which font to use in my editor?"
```
"There is no such rule mentioned in the provided document." It doesn't make one up.

**Beat 4 — close card (no typing; I overlay this in post).**
Cost/power punchline + `github.com/edhaynes/eds-rules`.

## Notes
- All three prompts were test-fired and land clean (2026-06-13). If a take stumbles,
  re-run the same command — `temperature 0` makes the rules model's answers stable.
- Keep each `ollama run` as its own invocation (prints answer, exits) — clean cuts.
- Vanilla-Claude (instead of vanilla-Llama) is the stronger "small beats big" framing
  but is **blocked** on a valid ANTHROPIC_API_KEY — see demo/PLAN.md. Llama-vs-Llama
  is the rigorous one-variable cut and works today.
