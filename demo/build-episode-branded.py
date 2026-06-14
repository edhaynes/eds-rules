#!/usr/bin/env python3
"""Assemble an "Ed's 100 Rules" episode MP4 from audio + the script's [CARD] cues,
in the bard-marketing brand (black/Red Hat red/white, Arial, the Bard owl).

Pipeline stage: audio (your recording OR the clone) -> branded card video -> MP4,
ready for the YouTube upload+schedule stage.

Usage:
  python3 build-episode-branded.py --ep 92 --audio podcast/ep92.wav [--out podcast/ep92.mp4]
Cards: title -> each [CARD: "..."] from podcast/ep<N>.md -> outro, timed evenly
across the audio (a later pass can sync to the script's section timecodes).
Requires: Pillow, ffmpeg.
"""
import argparse, os, re, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OWL = os.path.expanduser("~/projects/bard-marketing/logos/bard-owl-square.png")

W, H = 1920, 1080
BLACK = (16, 16, 16); RED = (238, 0, 0); WHITE = (255, 255, 255)
GRAY = (191, 191, 191); DIM = (128, 128, 128)
ARIAL = "/System/Library/Fonts/Supplemental/Arial%s.ttf"


def font(sz, bold=True):
    p = ARIAL % (" Bold" if bold else "")
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def wrap(d, text, fnt, maxpx):
    out, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxpx: line = t
        else: out.append(line); line = w
    if line: out.append(line)
    return out


def header(img, d, ep):
    if os.path.exists(OWL):
        owl = Image.open(OWL).convert("RGBA").resize((96, 96)); img.paste(owl, (60, 50), owl)
    d.text((176, 56), "ED'S 100 RULES", font=font(46), fill=WHITE)
    d.text((176, 108), "the rule-quality series", font=font(26, False), fill=DIM)
    tag = f"EP {ep}"; l, t, r, b = d.textbbox((0, 0), tag, font=font(46))
    d.text((W - 60 - (r - l), 60), tag, font=font(46), fill=RED)


def card(ep, lines):
    """lines = list of (text, size, color)."""
    img = Image.new("RGB", (W, H), BLACK); d = ImageDraw.Draw(img)
    header(img, d, ep)
    rendered = []
    for text, size, color in lines:
        for ln in wrap(d, text, font(size), W - 320):
            rendered.append((ln, font(size), color))
    total = sum(f.size + 26 for _, f, _ in rendered)
    y = (H - total) // 2 + 40
    for ln, fnt, color in rendered:
        w = d.textlength(ln, font=fnt); d.text(((W - w) / 2, y), ln, font=fnt, fill=color)
        y += fnt.size + 26
    # red baseline accent
    d.rectangle([0, H - 8, W, H], fill=RED)
    return img


def parse_cards(ep):
    md = os.path.join(HERE, "podcast", f"ep{ep}.md")
    title = ""
    cues = []
    for line in open(md, encoding="utf-8"):
        if line.startswith("# Episode") and not title:
            title = line.split("—", 1)[-1].strip().strip('"')
        m = re.search(r'\[CARD:\s*"?(.+?)"?\s*\]', line)
        if m and m.group(1) not in ("…", "..."):
            cues.append(m.group(1))
    return title, cues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ep", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--out")
    a = ap.parse_args()
    audio = a.audio if os.path.isabs(a.audio) else os.path.join(HERE, a.audio)
    out = a.out or os.path.join(HERE, "podcast", f"ep{a.ep}.mp4")
    title, cues = parse_cards(a.ep)

    frames = [card(a.ep, [("Ed's 100 Rules", 64, GRAY), (title, 88, WHITE)])]
    for c in cues:
        # color scores/vs red, rest white
        parts = [(c, 78, RED if re.search(r'\bvs\b|\d{2}\.\d', c) else WHITE)]
        frames.append(card(a.ep, parts))
    frames.append(card(a.ep, [("Ed's 100 Rules", 56, GRAY), ("Same list. Different grades.", 64, WHITE)]))

    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", audio]).strip())
    per = dur / len(frames)

    tmp = tempfile.mkdtemp()
    listf = os.path.join(tmp, "list.txt")
    with open(listf, "w") as lf:
        for i, fr in enumerate(frames):
            p = os.path.join(tmp, f"f{i:02d}.png"); fr.save(p)
            lf.write(f"file '{p}'\nduration {per:.3f}\n")
        lf.write(f"file '{os.path.join(tmp, f'f{len(frames)-1:02d}.png')}'\n")

    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listf, "-i", audio,
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{dur:.3f}", out],
        check=True, capture_output=True)
    print(f"wrote {out}  ({len(frames)} cards over {dur:.0f}s)")


if __name__ == "__main__":
    main()
