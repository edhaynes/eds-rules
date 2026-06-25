#!/usr/bin/env python3
"""Render lower-third chyrons for ep103 (title + distilled bullet).

Each chyron is a full-frame 1280x720 RGBA PNG with only the lower third painted
(rest transparent), so the assemble step overlays it at (0,0) with a fade — same
idiom as ep93's explainer slides. Palette matches the book cover (book/cover.py).

Writes chyron_NN.png + chyrons.json (start/dur for the assemble step).
Run: python3 make_chyrons.py
"""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "assets" / "chyrons"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
INK = (21, 23, 28)
PAPER = (244, 242, 238)
RED = (204, 0, 0)
MUTE = (170, 174, 182)

FONTS = Path("/System/Library/Fonts")
SUPP = FONTS / "Supplemental"


def font(name, size):
    for base in (SUPP, FONTS):
        p = base / name
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


# (start_seconds, TITLE, bullet) — approved 2026-06-25
CHYRONS = [
    (20,  "THE 1-PARAMETER LLM",      "A Reddit gag — a model whose only job is to gush about one thing"),
    (47,  "THE 0-PARAMETER MODEL",    "An echo — returns the token you send. true gives true, false gives false"),
    (78,  "STILL HAS A PURPOSE",      "Collapse a pipeline's result to true or false, emit it as one token"),
    (104, "SCALING 10x EACH STEP",    "0, then 1, then ten times bigger each step — up to 500M parameters"),
    (120, "LOGIC BEFORE MATH",        "Boolean logic first, then math, then the Socratic dialogues (Plato)"),
    (143, "A MORAL COMPASS",          "Trained on the New Testament — minus the genealogies"),
    (160, "PROVABLE BY CONSTRUCTION", "Early versions verified mathematically correct by an outside mathematician"),
    (177, "PROVABLE vs UNPROVABLE",   '"Adam is 6 ft 10" can be proven;  "Adam is a jerk" cannot'),
    (216, "TINY = FAST",              "Intrusion detection in 14 microseconds vs Llama-8B at 253 ms — similar results"),
    (255, "LOGIC IN THE TEXT",        'The 500B model analyzes the "render unto Caesar" dilemma — a framing error'),
    (286, "THE FIRST AXIOM",          "true = true. You have to start somewhere — faith or scientific method, same logic"),
    (364, "RECORDED AT DEN",          "Passersby blurred by request"),
]
DUR = 7.0   # seconds each chyron holds


def fit(draw, text, name, size, max_w):
    """Shrink font until text fits max_w."""
    while size > 18:
        f = font(name, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(name, 18)


def render(idx, title, bullet):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    band_h = 150
    y0 = H - band_h - 40
    # translucent charcoal band
    band = Image.new("RGBA", (W, band_h), (*INK, 232))
    img.alpha_composite(band, (0, y0))
    # red accent bar on the left
    d.rectangle([60, y0 + 24, 70, y0 + band_h - 24], fill=RED)
    tx = 92
    tf = fit(d, title, "Georgia Bold.ttf", 52, W - tx - 80)
    d.text((tx, y0 + 26), title, font=tf, fill=PAPER)
    bf = fit(d, bullet, "Georgia.ttf", 34, W - tx - 80)
    d.text((tx, y0 + 92), bullet, font=bf, fill=MUTE)
    img.save(OUT / f"chyron_{idx:02d}.png")


def main():
    meta = []
    for i, (start, title, bullet) in enumerate(CHYRONS, 1):
        render(i, title, bullet)
        meta.append({"idx": i, "start": start, "dur": DUR,
                     "png": f"chyron_{i:02d}.png", "title": title})
    json.dump(meta, open(OUT / "chyrons.json", "w"), indent=2)
    print(f"wrote {len(CHYRONS)} chyrons + chyrons.json to {OUT}")


if __name__ == "__main__":
    main()
