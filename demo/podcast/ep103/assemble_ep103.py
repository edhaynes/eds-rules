#!/usr/bin/env python3
"""Assemble ep103: blurred video + chyron overlays + cleaned audio + soft CC.

Inputs (all produced by the other ep103 scripts):
  work/ep103-blurred.mp4   passersby covered with critters (blur_passersby.py)
  assets/chyrons/*.png     lower-thirds + chyrons.json timing (make_chyrons.py)
  work/ep103-clean.m4a     cleaned voice track (clean-audio.sh)
  ep103.srt                closed captions (make_srt.py)

One ffmpeg pass: fade each chyron in/out at its timestamp (ep93 idiom), re-encode
to h264, attach the cleaned audio, and mux the .srt as a soft (toggleable) caption
track. Build number = git commit count (coding-rules §8), stamped into metadata.

Usage: assemble_ep103.py [out.mp4]
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE / "work"
CHY = HERE / "assets" / "chyrons"
BLURRED = WORK / "ep103-blurred.mp4"
AUDIO = WORK / "ep103-clean.m4a"
SRT = HERE / "ep103.srt"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "ep103.mp4"
FADE = 0.4


def build_number():
    try:
        return subprocess.check_output(["git", "rev-list", "--count", "HEAD"],
                                       cwd=HERE).decode().strip()
    except subprocess.CalledProcessError:
        return "0"


def main():
    chyrons = json.load(open(CHY / "chyrons.json"))
    total = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", str(BLURRED)]).strip())

    inputs = ["-i", str(BLURRED), "-i", str(AUDIO)]
    for c in chyrons:
        end = c["start"] + c["dur"]
        inputs += ["-loop", "1", "-framerate", "30", "-t", f"{end + 0.5:.1f}",
                   "-i", str(CHY / c["png"])]
    inputs += ["-i", str(SRT)]
    srt_idx = 2 + len(chyrons)

    fc, prev = [], "0:v"
    for n, c in enumerate(chyrons):
        idx = 2 + n
        st, end = c["start"], c["start"] + c["dur"]
        fc.append(f"[{idx}:v]format=rgba,fade=in:st={st}:d={FADE}:alpha=1,"
                  f"fade=out:st={end - FADE}:d={FADE}:alpha=1[c{n}]")
        fc.append(f"[{prev}][c{n}]overlay=enable='between(t,{st},{end})':"
                  f"eof_action=pass[v{n}]")
        prev = f"v{n}"
    fc.append(f"[{prev}]format=yuv420p[vout]")

    bn = build_number()
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats", *inputs,
           "-filter_complex", ";".join(fc),
           "-map", "[vout]", "-map", "1:a", "-map", f"{srt_idx}:s",
           "-t", f"{total:.3f}",
           "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
           "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
           "-metadata", "title=ep103 — Tiny Logic LLMs (Denver Airport)",
           "-metadata", f"comment=eds-rules podcast · build {bn}",
           str(OUT)]
    print(f"assembling ep103 (build {bn}, {len(chyrons)} chyrons)...")
    subprocess.run(cmd, check=True)
    dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nokey=1:noprint_wrappers=1",
        str(OUT)]).strip().decode()
    print(f"wrote {OUT}  ({float(dur):.0f}s, build {bn})")


if __name__ == "__main__":
    main()
