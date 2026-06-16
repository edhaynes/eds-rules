#!/usr/bin/env python3
"""Whisper transcription with word-level timestamps (runs on Gladius GPU).

Outputs words.json: {"words": [{"w": str, "start": float, "end": float}, ...]}
Used to place explainer cards at the first mention of each glossary term.
Usage: transcribe.py <media> <out.json> [model]
"""
import json, sys
import whisper

media, out = sys.argv[1], sys.argv[2]
model_name = sys.argv[3] if len(sys.argv) > 3 else "large-v3"

model = whisper.load_model(model_name, download_root="/srv/models/whisper")
r = model.transcribe(media, word_timestamps=True, language="en", fp16=True)

words = []
for seg in r["segments"]:
    for w in seg.get("words", []):
        words.append({"w": w["word"].strip(), "start": round(w["start"], 3),
                      "end": round(w["end"], 3)})
json.dump({"text": r["text"], "words": words}, open(out, "w"), indent=0)
print(f"done {out}  ({len(words)} words)")
