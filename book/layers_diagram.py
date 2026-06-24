#!/usr/bin/env python3
"""Render the layered-ruleset funnel (the '3-pager' diagram) in B&W for the book.

Inverted pyramid: widest/darkest at top = most general (the axiom core every seat
carries), tapering down to the narrowest/lightest = most specific (employer). Slice
width is proportional to rule count. Counts come from taxonomy/rules.yaml.

    python3 book/layers_diagram.py   ->  book/art/the-layers.png
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# layer: (name, count, one-line scope, grayscale fill)
LAYERS = [
    ("Axiom core",          24, "universal — carried by every seat",        (24, 24, 24)),
    ("Personal / architect",18, "the crew, the stack, engineering style",   (88, 88, 88)),
    ("Project",              5, "what this codebase is being built to be",   (140, 140, 140)),
    ("Employer",             3, "the shop's house standard (e.g. Red Hat)",  (190, 190, 190)),
]

S = 3                                   # supersample for crisp print
W, H = 1700 * S, 760 * S
PAD = 40 * S
CX = 470 * S                            # funnel centre
TOPW = 760 * S                          # widest slice (axiom)
SLICE_H = 150 * S
GAP = 10 * S

FONTS = Path("/System/Library/Fonts")
SUPP = FONTS / "Supplemental"


def f(name, size):
    for base in (SUPP, FONTS):
        p = base / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    serif = lambda s: f("Georgia Bold.ttf", s)
    serif_r = lambda s: f("Georgia.ttf", s)
    mono = lambda s: f("Courier New Bold.ttf", s)

    scale = TOPW / max(c for _, c, _, _ in LAYERS)
    widths = [c * scale for _, c, _, _ in LAYERS]

    # general/specific axis markers
    d.text((PAD, PAD), "GENERAL", font=mono(26 * S), fill=(0, 0, 0))
    d.text((PAD, PAD + 30 * S), "▲", font=mono(26 * S), fill=(0, 0, 0))
    d.text((PAD, H - PAD - 56 * S), "▼", font=mono(26 * S), fill=(0, 0, 0))
    d.text((PAD, H - PAD - 26 * S), "SPECIFIC", font=mono(26 * S), fill=(0, 0, 0))

    y = PAD + 20 * S
    label_x = CX + TOPW / 2 + 50 * S
    for i, (name, c, desc, fill) in enumerate(LAYERS):
        top = widths[i]
        bot = widths[i + 1] if i + 1 < len(LAYERS) else widths[i] * 0.5
        tl, tr = CX - top / 2, CX + top / 2
        bl, br = CX - bot / 2, CX + bot / 2
        d.polygon([(tl, y), (tr, y), (br, y + SLICE_H), (bl, y + SLICE_H)],
                  fill=fill, outline=(0, 0, 0), width=2 * S)
        # count, centred, contrast by fill brightness
        txtcol = "white" if sum(fill) / 3 < 130 else (0, 0, 0)
        cf = serif(46 * S)
        cw = d.textlength(str(c), font=cf)
        d.text((CX - cw / 2, y + SLICE_H / 2 - 32 * S), str(c), font=cf, fill=txtcol)
        # leader line + side label
        midy = y + SLICE_H / 2
        d.line([(tr + 8 * S, midy), (label_x - 16 * S, midy)], fill=(120, 120, 120), width=2 * S)
        d.text((label_x, midy - 30 * S), name, font=serif(30 * S), fill=(0, 0, 0))
        d.text((label_x, midy + 6 * S), desc, font=serif_r(24 * S), fill=(90, 90, 90))
        y += SLICE_H + GAP

    out = Path("book/art/the-layers.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    img.resize((W // S, H // S), Image.LANCZOS).save(out, dpi=(300, 300))
    print(f"wrote {out} ({W // S}x{H // S})")


if __name__ == "__main__":
    main()
