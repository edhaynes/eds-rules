# Ep 93 — Guy Turgeon interview: post-production pipeline

Turns the raw Google Meet recording (`Guy_Ed … Recording.mp4`, speaker-view, 1080p24,
~30 min) into an upload-ready episode:

1. **Opening card** — branded title screen ("Ed's 100 Rules", EP 93).
2. **Explainer cards** — a lower-third flashes in at the first spoken mention of each
   jargon term (the 90% rule, API-first, attack surface, VxWorks, UBI, Podman).
3. **Background blur** — only on *Ed's* segments (Guy's feed is already Meet-blurred and
   is left untouched). Robust Video Matting keeps Ed sharp, blurs the room.
4. **Lighting fix** — a colour grade on Ed's segments (cuts the warm cast, lifts the face).

The recording is *speaker-view*: one stream that cuts to whoever is talking, captioned
bottom-left. So the work is gated by a speaker map — blur/grade apply only where the
caption says "Ed Haynes".

## Compute split

- **Gladius (gx10)** — GPU work: RVM background blur (`rvm_blur.py`) and Whisper
  transcription (`transcribe.py`), both on the ComfyUI venv (torch + cu130, GB10).
- **Local (mac)** — speaker map (`speaker_map_ocr.py`, caption OCR via tesseract),
  brand assets (`brand_slides.py`), and final assembly (`assemble.py`).

## Steps

```
# 1. brand assets (opening + explainer lower-thirds)
python3 brand_slides.py

# 2. speaker map: Ed vs Guy, via caption OCR  -> work/segments.json
python3 speaker_map_ocr.py "<source.mp4>" work/segments.json

# 3. on Gladius: background blur (full video) + word-timestamp transcript
scp rvm_blur.py transcribe.py gladius:/srv/models/ep93/
ssh gladius '… rvm_blur.py source.mp4 full_blur.mp4'      # -> full_blur.mp4
ssh gladius '… transcribe.py source.mp4 words.json large-v3'  # -> words.json
scp gladius:/srv/models/ep93/{full_blur.mp4,words.json} work/

# 4. assemble: blur/grade Ed windows + flash cards + opening + audio
python3 assemble.py "<source.mp4>" work/ep93-final.mp4
```

## Tuning knobs

| Where | Knob | Default |
|---|---|---|
| `rvm_blur.py` | gaussian kernel / sigma / downsample | 61 / 16 / 0.25 |
| `assemble.py` | `GRADE` (colour) | grade "B" (warm-cut + face lift) |
| `assemble.py` | `SLIDE_DUR` / `FADE` | 6.0s / 0.4s |
| `brand_slides.py` | `GLOSSARY`, `OPENING` | term copy + title |

Heavy/regenerable media lives under `work/` (gitignored). Tools and brand PNGs are tracked.
RVM is GPL-3.0, used here as an offline tool (not shipped). Whisper is MIT.
