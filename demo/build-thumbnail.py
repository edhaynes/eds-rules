#!/usr/bin/env python3
"""Render the YouTube/README thumbnail for the teaser — a high-contrast,
few-words, curiosity-driven card built to catch clicks.

Usage: python3 build-thumbnail.py   ->  demo/teaser-thumb.png (1280x720)
Requires: Pillow. macOS (Menlo font).
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "teaser-thumb.png")

W, H = 1280, 720
BG = (13, 17, 23)
FG = (240, 246, 252)
DIM = (139, 148, 158)
GREEN = (63, 185, 80)
RED = (248, 81, 73)

FONT = "/System/Library/Fonts/Menlo.ttc"
def f(sz, bold=True):
    return ImageFont.truetype(FONT, sz, index=1 if bold else 0)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# faint split wash: red left, green right
mid = W // 2
left = Image.new("RGB", (mid, H), (28, 18, 18)); img.paste(left, (0, 0))
right = Image.new("RGB", (W - mid, H), (16, 28, 18)); img.paste(right, (mid, 0))
d.line([mid, 0, mid, H], fill=(48, 54, 61), width=3)


def center(text, font, y, color, cx=W // 2):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=color)


# top kicker
center("SAME 8B MODEL — TWICE", f(40), 70, DIM)

# the hook: no rules (red) vs my rules (green)
center("no rules", f(96), 200, RED, cx=mid // 2)
center("my rules", f(96), 200, GREEN, cx=mid + mid // 2)
center("vs", f(54), 215, FG)

# proof line under each side
center('"no idea what', f(34), 360, DIM, cx=mid // 2)
center('rule 2 is"', f(34), 400, DIM, cx=mid // 2)
center("quotes the rule,", f(34), 360, FG, cx=mid + mid // 2)
center("catches the leak", f(34), 400, FG, cx=mid + mid // 2)

# payoff strip
d.rectangle([0, 500, W, 506], fill=GREEN)
center("seeing is believing", f(64), 540, GREEN)
center("github.com/edhaynes/eds-rules", f(30), 640, DIM)

# play triangle badge, bottom-right
bx, by, r = W - 110, H - 110, 46
d.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0), outline=FG, width=4)
d.polygon([(bx - 16, by - 24), (bx - 16, by + 24), (bx + 28, by)], fill=FG)

img.save(OUT)
print(f"wrote {OUT} ({W}x{H})")
