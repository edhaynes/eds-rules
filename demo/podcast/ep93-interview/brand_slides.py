#!/usr/bin/env python3
"""Brand assets for Ep 93 (the Guy Turgeon interview), in the "Ed's 100 Rules"
look: black #101010, Red Hat red #EE0000, Arial, the Bard owl.

Produces:
  - opening.png            full-screen title card (1920x1080)
  - slide_<key>.png        lower-third explainer cards (RGBA, transparent) that
                           flash in when a jargon term is spoken.

Term copy lives in GLOSSARY below; edit there. Used by build_proof.sh / the
full assembler. Requires Pillow.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OWL = os.path.expanduser("~/projects/eds-rules/demo/assets/bard-owl-square.png")
OUT = os.path.join(HERE, "assets")

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
        if d.textlength(t, font=fnt) <= maxpx:
            line = t
        else:
            out.append(line); line = w
    if line:
        out.append(line)
    return out


def header(img, d):
    if os.path.exists(OWL):
        owl = Image.open(OWL).convert("RGBA").resize((96, 96))
        img.paste(owl, (60, 50), owl)
    d.text((176, 56), "ED'S 100 RULES", font=font(46), fill=WHITE)
    d.text((176, 108), "the rule-quality series", font=font(26, False), fill=DIM)
    tag = "EP 93"
    l, t, r, b = d.textbbox((0, 0), tag, font=font(46))
    d.text((W - 60 - (r - l), 60), tag, font=font(46), fill=RED)


def opening(title_lines):
    """title_lines = list of (text, size, color)."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    header(img, d)
    rendered = []
    for text, size, color in title_lines:
        for ln in wrap(d, text, font(size), W - 320):
            rendered.append((ln, font(size), color))
    total = sum(f.size + 26 for _, f, _ in rendered)
    y = (H - total) // 2 + 30
    for ln, fnt, color in rendered:
        w = d.textlength(ln, font=fnt)
        d.text(((W - w) / 2, y), ln, font=fnt, fill=color)
        y += fnt.size + 26
    d.rectangle([0, H - 8, W, H], fill=RED)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "opening.png")
    img.save(p)
    print("wrote", p)


def lower_third(key, term, definition, kicker="EXPLAINER"):
    """Transparent RGBA lower-third card (explainer or disclaimer)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # panel geometry
    x0, x1 = 90, W - 90
    y0, y1 = 812, 1012
    panel = Image.new("RGBA", (x1 - x0, y1 - y0), (16, 16, 16, 224))
    img.paste(panel, (x0, y0), panel)
    d.rectangle([x0, y0, x0 + 12, y1], fill=RED)          # red accent bar
    d.rectangle([x0, y1, x1, y1 + 6], fill=RED)           # red baseline
    # kicker
    d.text((x0 + 48, y0 + 26), kicker, font=font(26), fill=RED)
    # term
    d.text((x0 + 48, y0 + 58), term, font=font(60), fill=WHITE)
    # definition (wrap)
    fnt = font(34, False)
    yy = y0 + 132
    for ln in wrap(d, definition, fnt, (x1 - x0) - 96):
        d.text((x0 + 48, yy), ln, font=fnt, fill=GRAY)
        yy += fnt.size + 8
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f"slide_{key}.png")
    img.save(p)
    print("wrote", p)


# --- DRAFT copy — Ed approves before the full render -----------------------
GLOSSARY = {
    "90rule":   ("The 90% Rule",
                 "Gather about 90% of what you need to decide, then decide. "
                 "Below that, ask one more question; above it, stop researching and move."),
    "apifirst": ("API-First",
                 "Design and freeze the interface contract before writing code. "
                 "The API becomes the single source of truth everything else serves."),
    "attacksurface": ("Attack Surface",
                 "Every point where an attacker could try to get in. "
                 "Less code and fewer entry points means a smaller surface to defend."),
    "vxworks":  ("VxWorks",
                 "A real-time operating system (RTOS) for embedded devices — "
                 "historically one large process with full memory access, prized for determinism."),
    "ubi":      ("UBI",
                 "Red Hat Universal Base Image — the hardened, freely redistributable "
                 "container base image this project uses by default."),
    "podman":   ("Podman",
                 "Red Hat's daemonless, rootless container engine — "
                 "a drop-in Docker alternative with a smaller attack surface."),
}

OPENING = [
    ("EPISODE 93", 56, GRAY),
    ("In Conversation with", 64, WHITE),
    ("Guy Turgeon", 110, WHITE),
    ("Grading the 100 Rules", 44, RED),
]

def ed_card_bg():
    """Branded background for Ed's audiogram: header + name + baseline, with the
    centre band (y 280-840) left empty for the owl + its audio waveform."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    header(img, d)
    name, sub = "ED HAYNES", "Grading the 100 Rules"
    f1, f2 = font(56), font(34, False)
    w1 = d.textlength(name, font=f1)
    d.text(((W - w1) / 2, 858), name, font=f1, fill=WHITE)
    w2 = d.textlength(sub, font=f2)
    d.text(((W - w2) / 2, 924), sub, font=f2, fill=RED)
    d.rectangle([0, H - 8, W, H], fill=RED)
    p = os.path.join(OUT, "ed_card_bg.png")
    img.save(p)
    print("wrote", p)


if __name__ == "__main__":
    opening(OPENING)
    for k, (term, defn) in GLOSSARY.items():
        lower_third(k, term, defn)
    ed_card_bg()
