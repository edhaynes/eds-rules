#!/usr/bin/env python3
"""Assemble ep94: owl splash + explainer lower-thirds over the (already-blurred,
solo) recording. No speaker map, no RVM. Single ffmpeg pass, bounded output.

Usage: assemble.py <source.mp4> <out.mp4>
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
SRC = sys.argv[1]
OUT = sys.argv[2]
SPLASH_DUR = 5.0
FADE = 0.4

# (slide key, start_seconds, duration) — from transcript term detection
CARDS = [
    ("axiom",    87.8,  6),
    ("powell",   102.3, 6),
    ("failfast", 110.3, 6),
    ("api",      190.1, 6),
    ("fleet",    219.6, 4),
    ("stack",    224.4, 6),
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
