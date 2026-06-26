#!/usr/bin/env python3
"""Assemble the Vulcan / QNX certified-AI demo MP4 from the maestro VO + the [CARD] cues.

Vulcan brand (matches the pitch deck: deep navy + gold + white), not the Ed's-100-Rules brand.
Pipeline: VO audio + podcast/epVULCAN.md [CARD:] cues -> branded card video -> MP4.

Usage:
  python3 build-vulcan-video.py --audio podcast/vulcan_vo.mp3 --out podcast/vulcan-qnx-branded.mp4
Requires: Pillow, ffmpeg.
"""
import argparse
import os
import re
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
NAVY = (10, 22, 40)        # deep navy background (pitch-deck #0b2545 family)
GOLD = (200, 162, 58)      # accent (#c8a23a)
WHITE = (245, 245, 245)
DIM = (120, 140, 160)
ARIAL = "/System/Library/Fonts/Supplemental/Arial%s.ttf"


def font(sz, bold=True):
    p = ARIAL % (" Bold" if bold else "")
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()


def wrap(d, text, fnt, maxpx):
    out, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxpx:
            line = t
        else:
            out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def header(d):
    d.text((60, 56), "VULCAN", font=font(46), fill=WHITE)
    d.text((60, 108), "certified, provable AI", font=font(26, False), fill=DIM)
    tag = "QNX"
    lft, top, rgt, bot = d.textbbox((0, 0), tag, font=font(46))
    d.text((W - 60 - (rgt - lft), 60), tag, font=font(46), fill=GOLD)


def card(lines):
    """lines = list of (text, size, color)."""
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    header(d)
    rendered = []
    for text, size, color in lines:
        for ln in wrap(d, text, font(size), W - 320):
            rendered.append((ln, font(size), color))
    total = sum(f.size + 26 for _, f, _ in rendered)
    y = (H - total) // 2 + 40
    for ln, fnt, color in rendered:
        w = d.textlength(ln, font=fnt)
        d.text(((W - w) / 2, y), ln, font=fnt, fill=color)
        y += fnt.size + 26
    d.rectangle([0, H - 8, W, H], fill=GOLD)  # gold baseline accent
    return img


def parse_cues(md):
    cues = []
    for line in open(md, encoding="utf-8"):
        m = re.search(r'\[CARD:\s*"?(.+?)"?\s*\]', line)
        if m and m.group(1) not in ("…", "..."):
            cues.append(m.group(1))
    return cues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True)
    ap.add_argument("--cues", default=os.path.join(HERE, "podcast", "epVULCAN.md"))
    ap.add_argument("--out", default=os.path.join(HERE, "podcast", "vulcan-qnx-branded.mp4"))
    a = ap.parse_args()
    audio = a.audio if os.path.isabs(a.audio) else os.path.join(HERE, a.audio)
    cues = parse_cues(a.cues)

    bio = card([
        ("Ed Haynes", 80, GOLD),
        ("First Top Secret-certified encryptor — TACLANE", 42, WHITE),
        ("First certified IPv6 stack — Nortel", 42, WHITE),
        ("Wind River Innovation Award", 42, WHITE),
        ("3x Red Hat Summit speaker", 42, WHITE),
        ("Positive Train Control — Alstom", 42, WHITE),
    ])
    frames = [bio, card([("VULCAN", 96, WHITE), ("Certified AI for QNX", 64, GOLD)])]
    for c in cues:
        color = GOLD if re.search(r'\bvs\b|\d{2,3}%|million|two answers', c) else WHITE
        frames.append(card([(c, 78, color)]))
    frames.append(card([("Prove. Or refuse.", 72, GOLD)]))
    frames.append(card([
        ("TACLANE — first Top-Secret-certified encryptor", 38, WHITE),
        ("Nortel — first certified IPv6 stack", 38, WHITE),
        ("Wind River — Titanium, carrier-grade", 38, WHITE),
        ("Alstom x Red Hat — safety-critical rail", 38, WHITE),
        ("QNX x Vulcan — ?", 48, GOLD),
    ]))
    frames.append(card([
        ("Every line above shipped.", 52, WHITE),
        ("The next press release is yours.", 66, GOLD),
        ("What does your quote say?", 52, WHITE),
    ]))

    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", audio]).strip())
    per = dur / len(frames)

    tmp = tempfile.mkdtemp()
    listf = os.path.join(tmp, "list.txt")
    with open(listf, "w") as lf:
        for i, fr in enumerate(frames):
            p = os.path.join(tmp, f"f{i:02d}.png")
            fr.save(p)
            lf.write(f"file '{p}'\nduration {per:.3f}\n")
        lf.write(f"file '{os.path.join(tmp, f'f{len(frames)-1:02d}.png')}'\n")

    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listf, "-i", audio,
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-t", f"{dur:.3f}", a.out],
        check=True, capture_output=True)
    print(f"wrote {a.out}  ({len(frames)} cards over {dur:.0f}s)")


if __name__ == "__main__":
    main()
