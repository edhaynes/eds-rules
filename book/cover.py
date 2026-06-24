#!/usr/bin/env python3
"""Generate KDP-ready covers for the rules book.

Two artifacts, both at 300 DPI:
  * ebook  — front-only, 1600x2560 (KDP Kindle ideal 1.6:1)         -> dist/cover-ebook.png
  * wrap   — full paperback wrap (back + spine + front) sized from   -> dist/cover-wrap.png / .pdf
             the interior page count.

Design is purely typographic (no SVG rasteriser on this box, and the Red Hat
fedora is a separate trademark we deliberately avoid). Title stays "The Red Hat
Way" per Eddie; the AI-agents hook rides as a cover tagline + back-cover copy so
the browse thumbnail signals the audience without changing the title.

Spine math is KDP's: white paper, black-and-white interior = 0.002252 in/page.
Run:  python3 book/cover.py --pages 167
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ── KDP geometry (inches) ────────────────────────────────────────────────────
DPI = 300
TRIM_W, TRIM_H = 7.0, 10.0
BLEED = 0.125
SAFE = 0.25                      # keep live text this far inside the trim
PAGE_THICKNESS = 0.002252        # KDP white paper, B&W interior, in/page

# ── palette ──────────────────────────────────────────────────────────────────
INK = (21, 23, 28)               # near-black charcoal background
PAPER = (244, 242, 238)          # warm off-white
RED = (204, 0, 0)                # Red Hat red, our accent
RED_BRIGHT = (238, 0, 0)
MUTE = (150, 154, 162)           # muted gray for kickers / fine print

FONTS = Path("/System/Library/Fonts")
SUPP = FONTS / "Supplemental"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    """Load a system font by filename, falling back to the default."""
    for base in (SUPP, FONTS):
        p = base / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def serif(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    return font("Georgia Bold.ttf" if bold else "Georgia.ttf", size)


def mono(size: int) -> ImageFont.FreeTypeFont:
    return font("Courier New Bold.ttf", size)


def tracked(draw, xy, text, fnt, fill, tracking=0, anchor_center=None):
    """Draw letter-spaced text. anchor_center=width centres the run."""
    if anchor_center is not None:
        total = sum(draw.textlength(c, font=fnt) + tracking for c in text) - tracking
        x = (anchor_center - total) / 2
        y = xy[1]
    else:
        x, y = xy
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + tracking


def wrap_text(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ── front cover (shared by ebook + wrap-front) ───────────────────────────────
def draw_front(img: Image.Image, ox: int, oy: int, w: int, h: int):
    """Render the front-cover composition into img at offset (ox, oy)."""
    d = ImageDraw.Draw(img)
    cx = ox + w // 2
    s = w / 1600.0                                  # scale factor off the ebook size

    # top red rule
    d.rectangle([ox, oy, ox + w, oy + int(26 * s)], fill=RED)

    # kicker — the discoverability tagline (audience signal, not the title)
    tracked(d, (0, oy + int(150 * s)),
            "A FIELD MANUAL FOR DIRECTING AI CODING AGENTS",
            mono(int(30 * s)), MUTE, tracking=int(2 * s), anchor_center=ox * 2 + w if ox else w)

    # "100" — the brand numeral, oversized
    f100 = serif(int(560 * s))
    n = "100"
    nw = d.textlength(n, font=f100)
    d.text((cx - nw / 2, oy + int(300 * s)), n, font=f100, fill=RED)

    # RULES
    fr = serif(int(250 * s))
    rw = d.textlength("RULES", font=fr)
    d.text((cx - rw / 2, oy + int(890 * s)), "RULES", font=fr, fill=PAPER)

    # FOR WRITING MY SOFTWARE
    fsub = serif(int(96 * s), bold=True)
    for i, line in enumerate(("FOR WRITING", "MY SOFTWARE")):
        lw = d.textlength(line, font=fsub)
        d.text((cx - lw / 2, oy + int((1200 + i * 110) * s)), line, font=fsub, fill=PAPER)

    # divider + subtitle
    dy = oy + int(1490 * s)
    d.line([cx - int(180 * s), dy, cx + int(180 * s), dy], fill=RED, width=max(1, int(4 * s)))
    tracked(d, (0, oy + int(1530 * s)), "THE RED HAT WAY",
            mono(int(54 * s)), RED_BRIGHT, tracking=int(10 * s),
            anchor_center=ox * 2 + w if ox else w)

    # faint rule-number ledger down the lower third (technical texture)
    led = mono(int(26 * s))
    ty = oy + int(1720 * s)
    cols = ["  1  scan before you ship", " 23  if it can change, it's config",
            " 62  hooks before the first commit", " 68  contract first",
            " 70  100% branch coverage", "100  verify, then escalate"]
    for i, line in enumerate(cols):
        d.text((ox + int(150 * s), ty + i * int(46 * s)), line, font=led,
                fill=(60, 63, 70))

    # author
    fa = mono(int(60 * s))
    aw = d.textlength("ED  HAYNES", font=fa)
    d.text((cx - aw / 2, oy + h - int(180 * s)), "ED  HAYNES", font=fa, fill=PAPER)

    # bottom red rule
    d.rectangle([ox, oy + h - int(26 * s), ox + w, oy + h], fill=RED)


def build_ebook(out: Path):
    w, h = 1600, 2560
    img = Image.new("RGB", (w, h), INK)
    draw_front(img, 0, 0, w, h)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, dpi=(DPI, DPI))
    print(f"ebook  -> {out}  ({w}x{h})")


def build_wrap(out_png: Path, pages: int):
    spine_in = pages * PAGE_THICKNESS
    full_w_in = 2 * BLEED + 2 * TRIM_W + spine_in
    full_h_in = 2 * BLEED + TRIM_H
    # Round the canvas UP so the file meets-or-exceeds KDP's expected size; a
    # sub-pixel round-down (14.690 vs expected 14.691) trips KDP's size check.
    W, H = math.ceil(full_w_in * DPI), math.ceil(full_h_in * DPI)
    spine = round(spine_in * DPI)
    trim = round(TRIM_W * DPI)
    bleed = round(BLEED * DPI)

    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)

    back_x0 = 0
    spine_x0 = bleed + trim
    front_x0 = spine_x0 + spine

    # ── front (right panel) ──
    draw_front(img, front_x0, 0, trim + bleed, H)

    # ── spine ──
    d.rectangle([spine_x0, 0, front_x0, H], fill=INK)
    d.line([spine_x0 + 6, 0, spine_x0 + 6, H], fill=RED, width=4)
    d.line([front_x0 - 6, 0, front_x0 - 6, H], fill=RED, width=4)
    if spine >= 100:                                  # room for spine text
        spine_img = Image.new("RGB", (H, spine), INK)
        sd = ImageDraw.Draw(spine_img)
        sf = serif(int(spine * 0.42))
        txt = "100 RULES FOR WRITING MY SOFTWARE          ED HAYNES"
        tw = sd.textlength(txt, font=sf)
        sd.text(((H - tw) / 2, spine * 0.28), txt, font=sf, fill=PAPER)
        img.paste(spine_img.rotate(90, expand=True), (spine_x0, 0))

    # ── back (left panel) ──
    bx = back_x0 + bleed + int(SAFE * DPI)
    by = bleed + int(SAFE * DPI)
    inner_w = trim - 2 * int(SAFE * DPI)
    d.rectangle([back_x0, 0, back_x0 + int(26 * (trim / 1600.0) * DPI / DPI) + 20, H], fill=INK)
    d.rectangle([back_x0, 0, back_x0 + 26, H], fill=RED)

    head = serif(64)
    d.text((bx, by), "The hundred, in seven chapters.", font=head, fill=PAPER)
    by += 110

    blurb = (
        "Forty-seven years of software discipline, rewritten for the age of AI "
        "coding agents. One hundred numbered rules — the lines you never cross, "
        "the gates that hold when memory doesn't, and the crew of five AI roles "
        "that run them. Distilled from defense networking, embedded real-time "
        "systems, and enterprise open source; sharpened against the one thing "
        "that changed everything, which is that the patience to reach 100% "
        "coverage is no longer human patience."
    )
    bf = serif(40, bold=False)
    for line in wrap_text(d, blurb, bf, inner_w):
        d.text((bx, by), line, font=bf, fill=PAPER)
        by += 56
    by += 40

    bullets = [
        "Get 90% of the information, then decide — the Powell rule.",
        "Scan before every commit, push, and deploy. No scan, no ship.",
        "Push early and always: AI killed the merge-pain excuse.",
        "Contract first, then 100% line and branch coverage.",
        "A small axiom core every model carries; the rest paged on demand.",
    ]
    bbf = serif(38, bold=False)
    for b in bullets:
        d.text((bx, by), "—", font=serif(38), fill=RED)
        for j, line in enumerate(wrap_text(d, b, bbf, inner_w - 60)):
            d.text((bx + 60, by), line, font=bbf, fill=PAPER)
            by += 50
        by += 14

    # companion line
    by = H - bleed - int(SAFE * DPI) - 230
    cf = mono(34)
    for line in ("Companion repo (CC-BY-4.0):  github.com/edhaynes/eds-rules",
                 "The 100 Rules podcast + a side-by-side model demo.",
                 "Built with Bard — local LLMs on iPhone, iPad, and Mac."):
        d.text((bx, by), line, font=cf, fill=MUTE)
        by += 48

    # No barcode placeholder: KDP overlays the ISBN barcode automatically at
    # print time, so the back cover stays clean.

    out_png.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_png, dpi=(DPI, DPI))
    img.save(out_png.with_suffix(".pdf"), "PDF", resolution=DPI)
    print(f"wrap   -> {out_png}  ({W}x{H}px, {full_w_in:.3f}x{full_h_in:.3f}in, "
          f"spine {spine_in:.3f}in @ {pages}pp)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=167,
                    help="interior page count (drives spine width)")
    ap.add_argument("--out", type=Path, default=Path("dist"))
    args = ap.parse_args()
    build_ebook(args.out / "cover-ebook.png")
    build_wrap(args.out / "cover-wrap.png", args.pages)


if __name__ == "__main__":
    main()
