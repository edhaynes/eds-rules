#!/usr/bin/env python3
"""Assemble ep95: owl splash + "in plain English" lower-thirds over the solo
screen-share recording. No speaker map, no RVM blur (source is a screen-share,
not a talking-head). Single ffmpeg pass, bounded output.

Usage: assemble.py <source.mp4> <out.mp4>

Card timings come from the Gemini meeting transcript's section timestamps
(the same "term-first-mentioned" approach ep94 used), in SOURCE time — the splash
is concatenated in front afterwards, so these are unshifted.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
SRC = sys.argv[1]
OUT = sys.argv[2]
SPLASH_DUR = 5.0
FADE = 0.4

# (slide key, start_seconds, duration) — first spoken mention per the transcript.
# 100-rules/axiom intro 00:00, anonymizer 01:39, squawkbox/latency 02:44,
# hierarchy+hallucination+SIL 03:41, parameters+distillation+CDN 05:53.
CARDS = [
    ("llm",           12,  6),
    ("anonymizer",    99,  6),
    ("latency",       164, 6),
    ("hallucination", 221, 6),
    ("sil",           233, 6),
    ("parameters",    350, 6),
    ("distillation",  360, 6),
    ("cdn",           370, 5),
]

dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
    "format=duration", "-of", "default=nokey=1:noprint_wrappers=1", SRC]).strip())

inp = ["-loop", "1", "-t", str(SPLASH_DUR), "-i", os.path.join(A, "splash.png"),
       "-i", SRC,
       "-f", "lavfi", "-t", str(SPLASH_DUR), "-i", "anullsrc=r=48000:cl=stereo"]
for key, _, _ in CARDS:
    inp += ["-loop", "1", "-i", os.path.join(A, f"slide_{key}.png")]

fc = []
prev = "1:v"
for n, (key, st, d) in enumerate(CARDS):
    end = st + d
    si = 3 + n
    fc.append(f"[{si}:v]format=rgba,fade=in:st={st}:d={FADE}:alpha=1,"
              f"fade=out:st={end - FADE}:d={FADE}:alpha=1[s{n}]")
    fc.append(f"[{prev}][s{n}]overlay=enable='between(t,{st},{end})':eof_action=pass[v{n}]")
    prev = f"v{n}"
fc.append(f"[{prev}]fps=24,format=yuv420p,fade=in:st=0:d=0.4,setpts=PTS-STARTPTS[body]")
fc.append("[0:v]scale=1920:1080,fps=24,format=yuv420p,fade=in:st=0:d=0.5,setpts=PTS-STARTPTS[op]")
fc.append("[op][2:a][body][1:a]concat=n=2:v=1:a=1[v][a]")

cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats", *inp,
       "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
       "-t", f"{SPLASH_DUR + dur:.3f}",
       "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT]
subprocess.run(cmd, check=True)
out_dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
    "format=duration", "-of", "default=nokey=1:noprint_wrappers=1", OUT]).strip().decode()
print(f"wrote {OUT} ({float(out_dur):.0f}s)")
