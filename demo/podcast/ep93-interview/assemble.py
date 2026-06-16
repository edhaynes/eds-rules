#!/usr/bin/env python3
"""Assemble the final Ep93 video — single pass.

Inputs:
  source.mp4      original Meet recording (Guy frames + the audio track)
  segments.json   [start,end,"ed"|"guy"] speaker map (caption OCR)
  words.json      Whisper word timestamps (for explainer placement)
  assets/         opening card, ed_card_bg, owl, explainer lower-thirds

One ffmpeg pass:
  1. build Ed's owl audiogram layer inline (card + owl + voice waveform)
  2. show that layer only during *Ed* windows; Guy's video stays untouched
  3. flash each approved explainer card at the term's first spoken mention
  4. prepend the opening card; keep original audio (delayed by the opening)

Usage: assemble.py <source.mp4> <out.mp4> [cap_seconds]
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "assets")
W = os.path.join(HERE, "work")
SOURCE = sys.argv[1]
OUT = sys.argv[2]
CAP = float(sys.argv[3]) if len(sys.argv) > 3 else None  # smoke-test a short window

OPEN_DUR = 5.0
SLIDE_DUR = 6.0
FADE = 0.4
PRESET = "veryfast"
WAVE = "showwaves=s=1100x280:mode=p2p:rate=24:colors=0xFF4030:scale=cbrt"

TERMS = [
    ("90rule",        ["90 percent rule", "ninety percent rule", "90 rule"]),
    ("apifirst",      ["api first"]),
    ("attacksurface", ["attack surface"]),
    ("vxworks",       ["vxworks", "vx works"]),
    ("ubi",           ["universal base image", " ubi "]),
    ("podman",        ["podman", "pod man"]),
]


def ed_windows():
    segs = json.load(open(os.path.join(W, "segments.json")))["segments"]
    wins = [(a, b) for a, b, c in segs if c == "ed"]
    if CAP:
        wins = [(a, min(b, CAP)) for a, b in wins if a < CAP]
    return wins


def term_hits():
    words = json.load(open(os.path.join(W, "words.json")))["words"]
    s, idx = "", []
    for x in words:
        tok = x["w"].lower().replace("%", " percent").replace("-", " ")
        tok = re.sub(r"[^a-z0-9 ]", "", tok) + " "
        s += tok
        idx += [x["start"]] * len(tok)
    s = re.sub(r" +", " ", s)
    hits = []
    for key, variants in TERMS:
        best = None
        for ph in variants:
            p = s.find(ph)
            if p != -1 and (best is None or idx[p] < best):
                best = idx[p]
        if best is not None and (not CAP or best < CAP - 8):
            hits.append((key, round(best, 2)))
            print(f"  term '{key}' @ {best:.1f}s")
        elif best is None:
            print(f"  term '{key}' not spoken — skipped")
    return sorted(hits, key=lambda h: h[1])


def build():
    ed = ed_windows()
    hits = term_hits()
    ed_expr = "+".join(f"between(t,{a},{b})" for a, b in ed) or "0"

    src_in = (["-t", str(CAP)] if CAP else []) + ["-i", SOURCE]
    inputs = ["-loop", "1", "-t", str(OPEN_DUR), "-i", os.path.join(A, "opening.png"),
              *src_in,
              "-loop", "1", "-framerate", "24", "-i", os.path.join(A, "ed_card_bg.png"),
              "-loop", "1", "-framerate", "24", "-i", os.path.join(A, "owl.png"),
              "-f", "lavfi", "-t", str(OPEN_DUR), "-i", "anullsrc=r=48000:cl=stereo"]
    base_n = 5  # opening=0, source=1, card=2, owl=3, silence=4, slides=5..
    for key, _ in hits:
        inputs += ["-loop", "1", "-i", os.path.join(A, f"slide_{key}.png")]

    fc = [
        "[1:a]asplit=2[aw][ao]",
        f"[aw]aformat=channel_layouts=mono,{WAVE}[wave]",
        "[2:v][wave]overlay=(W-w)/2:580[c1]",
        "[3:v]scale=340:340[owl]",
        "[c1][owl]overlay=(W-w)/2:250[edlayer]",
        # shortest=1 + eof_action=pass: bound the body to the source length,
        # otherwise the looped card/owl streams make overlay run forever.
        f"[1:v][edlayer]overlay=enable='{ed_expr}':shortest=1:eof_action=pass[base]",
    ]
    prev = "base"
    for n, (key, t) in enumerate(hits):
        end = t + SLIDE_DUR
        fc.append(f"[{base_n + n}:v]format=rgba,fade=in:st={t}:d={FADE}:alpha=1,"
                  f"fade=out:st={end - FADE}:d={FADE}:alpha=1[s{n}]")
        fc.append(f"[{prev}][s{n}]overlay=enable='between(t,{t},{end})':eof_action=pass[v{n}]")
        prev = f"v{n}"
    fc += [
        f"[{prev}]fps=24,format=yuv420p,fade=in:st=0:d=0.4,setpts=PTS-STARTPTS[body]",
        "[0:v]scale=1920:1080,fps=24,format=yuv420p,fade=in:st=0:d=0.5,setpts=PTS-STARTPTS[op]",
        "[op][4:a][body][ao]concat=n=2:v=1:a=1[v][a]",
    ]

    # hard output duration cap (belt-and-braces against unbounded looped inputs)
    src_dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nokey=1:noprint_wrappers=1", SOURCE]).strip())
    total = OPEN_DUR + (CAP if CAP else src_dur)

    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-stats", *inputs,
           "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
           "-t", f"{total:.3f}",
           "-c:v", "libx264", "-crf", "19", "-preset", PRESET, "-pix_fmt", "yuv420p",
           "-threads", "0", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", OUT]
    print(f"rendering{' (CAP=' + str(CAP) + 's)' if CAP else ''}...")
    subprocess.run(cmd, check=True)
    dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nokey=1:noprint_wrappers=1", OUT]).strip().decode()
    print(f"wrote {OUT}  ({float(dur):.0f}s)")


if __name__ == "__main__":
    build()
