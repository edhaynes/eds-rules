#!/usr/bin/env python3
"""Placeholder face-cover critters for ep103 — PROVES THE PIPELINE, not final art.

Four 512x512 RGBA PNGs (transparent bg) matching CREATURES_SPEC.md silhouettes
and palette closely enough to validate the blur/overlay pass. Final art comes
from Gladius ComfyUI (or hand-illustration) and swaps in with the SAME filenames
and format — zero pipeline change.

Run: python3 make_placeholder_creatures.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
OUT = HERE / "assets" / "creatures"
OUT.mkdir(parents=True, exist_ok=True)
S = 512
OUTLINE = (25, 25, 30, 255)
LW = 10


def base(color):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    return img, ImageDraw.Draw(img)


def eyes(d, cx_l, cx_r, cy, r=34):
    for cx in (cx_l, cx_r):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 255), outline=OUTLINE, width=6)
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(25, 25, 30, 255))


def owl():
    img, d = base(None)
    amber = (224, 165, 42, 255)
    d.ellipse([110, 150, 402, 440], fill=amber, outline=OUTLINE, width=LW)          # head
    d.polygon([(140, 175), (190, 95), (220, 185)], fill=amber, outline=OUTLINE)      # ear tufts
    d.polygon([(372, 175), (322, 95), (292, 185)], fill=amber, outline=OUTLINE)
    eyes(d, 215, 297, 270, r=52)                                                     # big spectacled eyes
    d.ellipse([215 - 60, 270 - 60, 215 + 60, 270 + 60], outline=OUTLINE, width=5)
    d.ellipse([297 - 60, 270 - 60, 297 + 60, 270 + 60], outline=OUTLINE, width=5)
    d.polygon([(256, 300), (236, 330), (276, 330)], fill=(240, 150, 40, 255), outline=OUTLINE)  # beak
    img.save(OUT / "creature_1_owl.png")


def moose():
    img, d = base(None)
    choc = (107, 74, 43, 255)
    d.polygon([(150, 150), (40, 60), (120, 110), (60, 30), (170, 120)], fill=choc, outline=OUTLINE)   # antlers L
    d.polygon([(362, 150), (472, 60), (392, 110), (452, 30), (342, 120)], fill=choc, outline=OUTLINE)  # antlers R
    d.ellipse([150, 150, 362, 380], fill=choc, outline=OUTLINE, width=LW)             # head
    d.ellipse([195, 360, 317, 470], fill=(150, 110, 80, 255), outline=OUTLINE, width=LW)  # long snout
    eyes(d, 215, 297, 230)
    img.save(OUT / "creature_2_moose.png")


def frog():
    img, d = base(None)
    green = (95, 168, 68, 255)
    d.ellipse([120, 150, 392, 430], fill=green, outline=OUTLINE, width=LW)            # wide head
    for cx in (185, 327):                                                             # top-mounted bulging eyes
        d.ellipse([cx - 55, 110, cx + 55, 220], fill=green, outline=OUTLINE, width=LW)
        d.ellipse([cx - 30, 130, cx + 30, 190], fill=(255, 255, 255, 255), outline=OUTLINE, width=5)
        d.ellipse([cx - 13, 150, cx + 13, 176], fill=(25, 25, 30, 255))
    d.arc([170, 250, 342, 400], start=10, end=170, fill=OUTLINE, width=10)            # wide grin
    img.save(OUT / "creature_3_frog.png")


def rabbit():
    img, d = base(None)
    grey = (154, 163, 173, 255)
    d.ellipse([150, 175, 240, 360], fill=grey, outline=OUTLINE, width=LW)             # ears
    d.ellipse([272, 175, 362, 360], fill=grey, outline=OUTLINE, width=LW)
    d.ellipse([165, 300, 347, 460], fill=grey, outline=OUTLINE, width=LW)             # head
    eyes(d, 225, 287, 360)
    d.ellipse([245, 395, 267, 415], fill=(230, 120, 140, 255), outline=OUTLINE)       # nose
    d.rectangle([243, 415, 256, 445], fill=(255, 255, 255, 255), outline=OUTLINE, width=4)  # buck teeth
    d.rectangle([256, 415, 269, 445], fill=(255, 255, 255, 255), outline=OUTLINE, width=4)
    img.save(OUT / "creature_4_rabbit.png")


def contact_sheet():
    sheet = Image.new("RGBA", (S * 4, S), (200, 200, 200, 255))
    for i, n in enumerate(["creature_1_owl", "creature_2_moose", "creature_3_frog", "creature_4_rabbit"]):
        sheet.alpha_composite(Image.open(OUT / f"{n}.png"), (i * S, 0))
    sheet.convert("RGB").save(OUT / "contact-sheet.png")


if __name__ == "__main__":
    owl(); moose(); frog(); rabbit(); contact_sheet()
    print(f"wrote 4 placeholder critters + contact-sheet.png to {OUT}")
