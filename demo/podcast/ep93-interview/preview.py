#!/usr/bin/env python3
"""Quick low-res preview of the real pipeline (first N seconds), so the look can
be eyeballed while the full render runs. Writes work/preview.mp4. Separate output
path from assemble.py so it never collides with an in-flight full render.

Usage: preview.py <source.mp4> [seconds]
"""
import os, subprocess, sys
import assemble as Z

SRC = sys.argv[1]
CAP = float(sys.argv[2]) if len(sys.argv) > 2 else 175.0
PV_BODY = os.path.join(Z.W, "preview_body.mp4")
PV = os.path.join(Z.W, "preview.mp4")

ed = Z.ed_windows()
hits = [h for h in Z.term_hits() if h[1] < CAP - 8]
ed_expr = "+".join(f"between(t,{a},{b})" for a, b in ed) or "0"

inp = ["-t", str(CAP), "-i", SRC,
       "-loop", "1", "-framerate", "24", "-i", os.path.join(Z.A, "ed_card_bg.png"),
       "-loop", "1", "-framerate", "24", "-i", os.path.join(Z.A, "owl.png")]
for key, _ in hits:
    inp += ["-loop", "1", "-i", os.path.join(Z.A, f"slide_{key}.png")]

fc = ["[0:a]asplit=2[aw][ao]",
      f"[aw]aformat=channel_layouts=mono,{Z.WAVE}[wave]",
      "[1:v][wave]overlay=(W-w)/2:580[c1]",
      "[2:v]scale=340:340[owl]",
      "[c1][owl]overlay=(W-w)/2:250[edlayer]",
      f"[0:v][edlayer]overlay=enable='{ed_expr}'[base]"]
prev = "base"
for n, (key, t) in enumerate(hits):
    end = t + Z.SLIDE_DUR
    fc.append(f"[{3+n}:v]format=rgba,fade=in:st={t}:d={Z.FADE}:alpha=1,"
              f"fade=out:st={end - Z.FADE}:d={Z.FADE}:alpha=1[s{n}]")
    fc.append(f"[{prev}][s{n}]overlay=enable='between(t,{t},{end})'[v{n}]")
    prev = f"v{n}"
fc.append(f"[{prev}]scale=960:540,format=yuv420p[vbody]")

subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inp,
    "-filter_complex", ";".join(fc), "-map", "[vbody]", "-map", "[ao]",
    "-c:v", "libx264", "-crf", "24", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "128k", PV_BODY], check=True)

subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
    "-loop", "1", "-t", str(Z.OPEN_DUR), "-i", os.path.join(Z.A, "opening.png"),
    "-i", PV_BODY, "-f", "lavfi", "-t", str(Z.OPEN_DUR), "-i", "anullsrc=r=48000:cl=stereo",
    "-filter_complex",
    "[0:v]scale=960:540,fps=24,format=yuv420p,fade=in:st=0:d=0.5,setpts=PTS-STARTPTS[op];"
    "[1:v]fade=in:st=0:d=0.4,setpts=PTS-STARTPTS[bd];"
    "[op][2:a][bd][1:a]concat=n=2:v=1:a=1[v][a]",
    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "24", "-preset", "ultrafast",
    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", PV], check=True)
print("wrote", PV)
