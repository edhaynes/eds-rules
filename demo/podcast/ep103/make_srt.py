#!/usr/bin/env python3
"""Build closed-caption sidecars (.srt + .vtt) from a Whisper transcript.

Prefers the higher-accuracy small.en transcript; falls back to the base one.
Sentence-ish segments straight from Whisper, lightly cleaned. Hand-fix any
remaining mishears in the .srt before publish — airport audio is noisy.

Run: python3 make_srt.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
SRC = WORK / "transcript-small.json"
if not SRC.exists():
    SRC = WORK / "transcript.json"


def ts(t, sep):
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def main():
    segs = json.load(open(SRC))["segments"]
    srt, vtt = [], ["WEBVTT", ""]
    for i, s in enumerate(segs, 1):
        text = s["text"].strip()
        if not text:
            continue
        srt.append(f"{i}\n{ts(s['start'], ',')} --> {ts(s['end'], ',')}\n{text}\n")
        vtt.append(f"{ts(s['start'], '.')} --> {ts(s['end'], '.')}\n{text}\n")
    (HERE / "ep103.srt").write_text("\n".join(srt))
    (HERE / "ep103.vtt").write_text("\n".join(vtt))
    print(f"wrote ep103.srt + ep103.vtt ({len(segs)} cues) from {SRC.name}")


if __name__ == "__main__":
    main()
