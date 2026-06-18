# Ep 95 — "The Virtue of the Small"

Produced-video episode (the YouTube track: ep93 = Guy interview, ep94 = Guy's
Scalpel, **ep95 = this**). Distinct from the synthetic `../ep95.md` "best×worst
rule" TTS script, which is a different series that happens to share the number.

Solo Ed Haynes, recorded 2026-06-17 — a screen-share talk over the "Ed's Rules —
Layered Edition" draft. Source: `vok-stbr-iku (2026-06-17 15_37 GMT-4).mp4`
(~9:47, 1080p screen-share with a corner face-cam) + the Gemini meeting notes.

Turns the raw recording into an upload-ready episode:

1. **Opening card** — branded owl splash ("Ed's Rules", EP 95, "The Virtue of the
   Small").
2. **"In plain English" lower-thirds** — a chyron flashes in at the first spoken
   mention of each jargon term, defined for non-technical viewers: LLM, Voice
   Anonymizer, Latency, AI Hallucination, SIL Certification, Parameters, Knowledge
   Distillation, CDN.

No RVM background blur / no speaker map — the source is a screen-share, not a
talking-head, so the ep93 blur/grade stage doesn't apply. Single ffmpeg pass.

## Episode content

- **Dropping the flat "100 rules" framing** — ~49 of the original hundred were
  personal biases / bad experiences with specific tech (Arch, Oracle), not general
  principles. Split general-purpose rules from personal preference.
- **A "martini glass" rule hierarchy** — a small set of personal axioms (≤10),
  then project rules, then employer-mandated ones (e.g. SIL); minimise pet peeves.
- **Rules as model capacity** — a ~2B model holds ~2 rules in mind; trillion-param
  models far more. Overload past capacity → hallucinations. Fewer, sharper rules.
- **CDN simulator + knowledge distillation** — sharing context with a Red Hat
  colleague and "distilling" the recommendation surfaced React + Vite; fixed the GUI.
- **New tooling** — a voice anonymizer (so guests can speak freely) and Squawkbox,
  a low-latency walkie-talkie with real-time speech-to-text.
- **Collaboration + humility** — learn from colleagues; rule suggestions as PRs;
  trim the mutable set toward a dozen.

## Steps

```
# 1. brand assets (owl splash + the eight lower-thirds)
.venv/bin/python brand.py

# 2. assemble: splash + cards over the source, single ffmpeg pass
.venv/bin/python assemble.py "<source.mp4>" work/ep95-final.mp4
```

Card timings (`assemble.py` `CARDS`) come from the Gemini transcript's section
timestamps (the same approach ep94 used), in source time. Term copy lives in
`brand.py` `GLOSSARY`.

## Tuning knobs

| Where | Knob | Default |
|---|---|---|
| `assemble.py` | `CARDS` (key, start_s, dur) | 8 cards, 5–6s each |
| `assemble.py` | `SPLASH_DUR` / `FADE` | 5.0s / 0.4s |
| `brand.py` | `GLOSSARY`, `TITLE`, `SUBTITLE` | term copy + title |

## Thumbnail

`ep95-thumbnail.jpg` (1280×720) — the "Guy + chainsaw" art (cutting the 100 rules
down), relabelled from the ep93 caption to **EP 95 · THE VIRTUE OF THE SMALL**.
Full-res working copy: `work/ep95-thumbnail-full.png`. Source art:
`~/Downloads/ChatGPT Image Jun 16, 2026, 02_40_03 PM.png`.

## YouTube copy

**Title:** The Virtue of the Small — Ed's Rules Ep 95

**Description:**
Why fewer rules and smaller models win. Dropping the flat "100 rules" for a small
immutable axiom core plus composable preference layers — and treating rules as a
cache hierarchy sized to what a model can actually hold. Plus the CDN simulator,
knowledge distillation, and new tooling (voice anonymizer, Squawkbox).
Lower-thirds explain each term in plain English. CC-BY-4.0 ·
github.com/edhaynes/eds-rules

## Publish checklist

- [x] Video assembled → `work/ep95-final.mp4` (9:52, 1080p24)
- [x] Thumbnail → `ep95-thumbnail.jpg` (1280×720)
- [ ] Upload to YouTube (Eddie's login) + set title/description above + thumbnail
- [ ] Add the public URL to `../distribution/REPORT.md §3`
- [ ] (Optional) audio-only cut for the Spotify/Apple feed (`../distribution/podcast.py`)

Heavy/regenerable media lives under `work/` (gitignored). Tools, brand PNGs, and
the JPG thumbnail are tracked. The `.venv/` is local (gitignored).
