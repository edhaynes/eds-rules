#!/usr/bin/env python3
"""Ep 93 thumbnail — "Quality vs Quantity": Guy Turgeon + a chainsaw cutting
the RULES in half. 1280x720, channel dark-GitHub theme.

Usage: python3 build_thumb_qvq.py
Out:   ep93-quality-vs-quantity-thumb.png
Requires: Pillow. macOS (Impact / Arial Black fonts).
"""
import math
import os

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(HERE, "thumb-src", "guy_1137.jpg")
OUT = os.path.join(HERE, "ep93-quality-vs-quantity-thumb.png")

W, H = 1280, 720
BG = (13, 17, 23)        # GitHub dark
FG = (240, 246, 252)
DIM = (139, 148, 158)
GREEN = (63, 185, 80)
RED = (248, 81, 73)
STEEL = (150, 158, 168)
STEEL_D = (70, 76, 84)
ORANGE = (255, 122, 26)
ORANGE_D = (196, 88, 12)
SAW_YEL = (255, 196, 0)

IMPACT = "/System/Library/Fonts/Supplemental/Impact.ttf"
ARIAL_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"


def impact(sz):
    return ImageFont.truetype(IMPACT, sz)


def black(sz):
    return ImageFont.truetype(ARIAL_BLACK, sz)


# ---------------------------------------------------------------- base canvas
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle vertical wash so the left (graphic) side reads darker than the photo
wash = Image.new("L", (W, 1))
for x in range(W):
    wash.putpixel((x, 0), int(8 + 16 * (x / W)))
wash = wash.resize((W, H))
img = Image.composite(Image.new("RGB", (W, H), (22, 27, 34)), img, wash)
d = ImageDraw.Draw(img)


# ---------------------------------------------------------------- hero (Guy)
PANEL_W = 600


def place_hero():
    im = Image.open(HERO).convert("RGB")
    # crop around the face (cx~1085, eyes~y470 in 1920x1080) at panel aspect
    im = im.crop((648, 36, 1522, 1080))          # 874x1044 ~ 0.837 aspect
    # punch up contrast + saturation + brightness for thumbnail pop
    im = ImageEnhance.Contrast(im).enhance(1.14)
    im = ImageEnhance.Color(im).enhance(1.20)
    im = ImageEnhance.Brightness(im).enhance(1.08)
    im = im.resize((PANEL_W, H), Image.LANCZOS)

    # feather only the far-left edge into the background (keep face crisp)
    mask = Image.new("L", (PANEL_W, H), 255)
    md = ImageDraw.Draw(mask)
    feather = 120
    for x in range(feather):
        md.line([(x, 0), (x, H)], fill=int(255 * (x / feather)))
    img.paste(im, (W - PANEL_W, 0), mask)


place_hero()

# clean near-vertical red divider at the photo seam (left of the face)
seam = W - PANEL_W - 8
d.line([(seam - 26, H), (seam + 26, 0)], fill=(0, 0, 0), width=14)
d.line([(seam - 18, H), (seam + 34, 0)], fill=RED, width=7)


# ---------------------------------------------------------------- chainsaw
def make_chainsaw():
    """Side-profile chainsaw silhouette, bar pointing right. RGBA."""
    cw, ch = 1000, 360
    c = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    p = ImageDraw.Draw(c)

    by = 180                                       # bar centre-line
    bar_x0, bar_x1 = 300, 930
    half = 24                                      # bar half-height
    nose = by                                      # nose centre

    # --- chain: dark race-track band slightly larger than the bar ---
    cgap = 12
    p.rounded_rectangle([bar_x0 - cgap, by - half - cgap,
                         bar_x1 + cgap, by + half + cgap],
                        radius=half + cgap, fill=(33, 37, 44))
    # --- guide bar (steel, rounded nose) ---
    p.rounded_rectangle([bar_x0, by - half, bar_x1, by + half],
                        radius=half, fill=STEEL, outline=STEEL_D, width=3)
    p.rounded_rectangle([bar_x0 + 16, by - 8, bar_x1 - 16, by + 8],
                        radius=8, fill=STEEL_D)          # groove
    # --- chain links: bright cutters spaced along top & bottom edges ---
    step = 30
    x = bar_x0
    while x < bar_x1:
        for ey in (by - half - cgap, by + half + cgap - 10):
            p.rounded_rectangle([x, ey, x + 18, ey + 10], radius=3,
                                fill=(176, 184, 194))
        x += step
    # cutter teeth (angled) on the top edge for a saw read
    x = bar_x0 + 6
    while x < bar_x1 - 20:
        p.polygon([(x, by - half - cgap), (x + 20, by - half - cgap),
                   (x + 4, by - half - cgap - 14)], fill=(120, 128, 138))
        x += step

    # --- engine body (chunky, distinct) ---
    p.rounded_rectangle([70, by - 110, 312, by + 128], radius=38,
                        fill=ORANGE, outline=ORANGE_D, width=7)
    p.rounded_rectangle([250, by - 66, 360, by + 78], radius=18,
                        fill=ORANGE_D)                   # front guard/clutch
    # starter-cord housing
    p.ellipse([98, by - 64, 206, by + 44], fill=ORANGE_D)
    p.ellipse([120, by - 42, 184, by + 22], fill=(28, 31, 37))
    p.ellipse([146, by - 16, 158, by - 4], fill=(176, 184, 194))
    for i in range(5):                               # cooling fins
        fx = 214 + i * 16
        p.rounded_rectangle([fx, by - 84, fx + 7, by - 8], radius=3,
                            fill=ORANGE_D)
    # --- top wrap-around handle (thick, with hand guard) ---
    p.arc([74, by - 196, 336, by - 26], start=196, end=356,
          fill=(26, 29, 35), width=30)
    p.line([(96, by - 150), (300, by - 96)], fill=(26, 29, 35), width=14)
    # --- rear trigger handle (closed loop) ---
    p.arc([6, by - 30, 168, by + 176], start=15, end=300,
          fill=(26, 29, 35), width=30)
    return c


saw = make_chainsaw()
saw = saw.rotate(19, expand=True, resample=Image.BICUBIC)
sw = 830
saw = saw.resize((sw, int(saw.height * sw / saw.width)), Image.LANCZOS)
saw_pos = (10, 250)


# ---------------------------------------------------------------- RULES (cut)
def make_rules_split():
    """Big 'RULES' word, sliced along a jagged diagonal, halves offset."""
    rw, rh = 760, 360
    base = Image.new("RGBA", (rw, rh), (0, 0, 0, 0))
    txt = Image.new("RGBA", (rw, rh), (0, 0, 0, 0))
    td = ImageDraw.Draw(txt)
    font = impact(300)
    word = "RULES"
    tw = td.textlength(word, font=font)
    tx = (rw - tw) / 2
    ty = -36
    # heavy outline + fill
    td.text((tx, ty), word, font=font, fill=(244, 248, 252),
            stroke_width=10, stroke_fill=(9, 12, 16))

    # jagged cut path (diagonal, sloping down-right to match the bar angle)
    import random
    random.seed(11)
    pts = []
    n = 26
    for i in range(n + 1):
        x = rw * i / n
        base_y = 168 + x * 0.235         # diagonal slope (matches saw bar)
        jag = random.uniform(-9, 9)
        pts.append((x, base_y + jag))

    # top mask: region above the jagged line
    top_mask = Image.new("L", (rw, rh), 0)
    tmd = ImageDraw.Draw(top_mask)
    tmd.polygon([(0, 0), (rw, 0)] + list(reversed(pts)), fill=255)
    bot_mask = Image.new("L", (rw, rh), 0)
    bmd = ImageDraw.Draw(bot_mask)
    bmd.polygon([(0, rh), (rw, rh)] + pts, fill=255)

    top = Image.new("RGBA", (rw, rh), (0, 0, 0, 0))
    top.paste(txt, (0, 0), top_mask)
    bot = Image.new("RGBA", (rw, rh), (0, 0, 0, 0))
    bot.paste(txt, (0, 0), bot_mask)

    # composite: small shear so the word still reads — top up-left, bottom drops
    out = Image.new("RGBA", (rw + 40, rh + 64), (0, 0, 0, 0))
    out.alpha_composite(top, (0, 0))
    out.alpha_composite(bot, (22, 46))
    # bright kerf glow traced along the cut
    gd = ImageDraw.Draw(out)
    glow = [(x + 11, y + 23) for x, y in pts]
    gd.line(glow, fill=(255, 214, 90, 230), width=5, joint="curve")
    return out, pts


rules, _ = make_rules_split()
rules_pos = (74, 124)


# ---------------------------------------------------------------- assemble
base = img.convert("RGBA")
base.alpha_composite(rules, rules_pos)
base.alpha_composite(saw, saw_pos)

# sawdust / spark particles flying off the cut
import random
random.seed(3)
pd = ImageDraw.Draw(base)
cx, cy = 470, 360
for _ in range(70):
    ang = random.uniform(-0.5, 0.9)
    dist = random.uniform(30, 260)
    px = cx + math.cos(ang) * dist + random.uniform(-20, 20)
    py = cy + math.sin(ang) * dist - dist * 0.25 + random.uniform(-20, 20)
    r = random.uniform(1.5, 5)
    col = random.choice([ORANGE, SAW_YEL, (210, 180, 140), FG])
    pd.ellipse([px - r, py - r, px + r, py + r], fill=col + (235,))

img = base.convert("RGB")
d = ImageDraw.Draw(img)


def text_c(text, font, cx, y, fill, stroke=0, sc=(0, 0, 0)):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill,
           stroke_width=stroke, stroke_fill=sc)


# top kicker: QUALITY vs QUANTITY
kf = black(46)
d.text((44, 40), "QUALITY", font=kf, fill=GREEN, stroke_width=3,
       stroke_fill=(0, 0, 0))
qw = d.textlength("QUALITY", font=kf)
d.text((44 + qw + 16, 46), "vs", font=black(34), fill=FG)
vw = d.textlength("vs", font=black(34))
d.text((44 + qw + 16 + vw + 16, 40), "QUANTITY", font=kf, fill=RED,
       stroke_width=3, stroke_fill=(0, 0, 0))

# bottom-left channel tag + guest
tagf = black(30)
d.text((44, H - 96), "ED'S 100 RULES", font=tagf, fill=FG,
       stroke_width=2, stroke_fill=(0, 0, 0))
d.text((44, H - 58), "EP 93 · GUY TURGEON", font=black(26), fill=SAW_YEL,
       stroke_width=2, stroke_fill=(0, 0, 0))

img.save(OUT)
print(f"wrote {OUT} ({W}x{H})")
