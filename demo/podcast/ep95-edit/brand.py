#!/usr/bin/env python3
"""Ep95 brand assets: Bard-owl splash screen + lower-third "in plain English"
explainer cards for non-technical viewers. Brand: black #101010, Red Hat red
#EE0000, Arial, the owl. Mirrors ep94-edit/brand.py; only the episode metadata
and the glossary (the actual jargon spoken in ep95) differ. Requires Pillow.

Episode 95 — "The Virtue of the Small": dropping the flat 100-rules framing for a
small axiom core, small local models, and knowledge distillation.
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


def ctr(d, y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def splash(title, subtitle):
    """Big-owl splash screen."""
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    if os.path.exists(OWL):
        owl = Image.open(OWL).convert("RGBA").resize((300, 300))
        img.paste(owl, ((W - 300) // 2, 210), owl)
    ctr(d, 540, "ED'S RULES", font(72), WHITE)
    ctr(d, 626, "100 Rules for Writing My Software", font(30, False), DIM)
    ctr(d, 712, "EPISODE 95", font(40), RED)
    ctr(d, 778, title, font(56), WHITE)
    if subtitle:
        ctr(d, 852, subtitle, font(32, False), GRAY)
    d.rectangle([0, H - 8, W, H], fill=RED)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "splash.png")
    img.save(p)
    print("wrote", p)


def lower_third(key, term, definition):
    """Transparent RGBA lower-third explainer card for non-technical viewers."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x0, x1 = 90, W - 90
    y0, y1 = 812, 1012
    panel = Image.new("RGBA", (x1 - x0, y1 - y0), (16, 16, 16, 224))
    img.paste(panel, (x0, y0), panel)
    d.rectangle([x0, y0, x0 + 12, y1], fill=RED)
    d.rectangle([x0, y1, x1, y1 + 6], fill=RED)
    d.text((x0 + 48, y0 + 26), "IN PLAIN ENGLISH", font=font(26), fill=RED)
    d.text((x0 + 48, y0 + 58), term, font=font(60), fill=WHITE)
    fnt = font(34, False)
    yy = y0 + 132
    for ln in wrap(d, definition, fnt, (x1 - x0) - 96):
        d.text((x0 + 48, yy), ln, font=fnt, fill=GRAY)
        yy += fnt.size + 8
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, f"slide_{key}.png")
    img.save(p)
    print("wrote", p)


# plain-English explainers for non-technical viewers (term, gloss), keyed to the
# first spoken mention of each term in the recording (see assemble.py CARDS).
GLOSSARY = {
    "llm":          ("LLM", "Large Language Model — the kind of AI (like ChatGPT) that reads and writes text by predicting the next word."),
    "anonymizer":   ("Voice Anonymizer", "A tool that disguises a speaker's voice, so a guest can talk on a recording without being identified."),
    "latency":      ("Latency", "The delay between doing something and seeing the result. 'Low latency' means it feels instant."),
    "hallucination":("AI Hallucination", "When an AI confidently makes something up — stating false information as if it were fact."),
    "sil":          ("SIL Certification", "Safety Integrity Level — an industrial safety rating for systems where a failure could hurt people."),
    "parameters":   ("Parameters", "The internal 'dials' a model learns. More parameters (2 billion vs. a trillion) = more it can hold in mind."),
    "distillation": ("Knowledge Distillation", "Teaching a smaller, cheaper model to copy a big model's answers — most of the smarts, a fraction of the size."),
    "cdn":          ("CDN", "Content Delivery Network — servers that keep copies of content close to users so pages load fast."),
}

TITLE = "The Virtue of the Small"
SUBTITLE = "Fewer rules, smaller models, a sharper core"

if __name__ == "__main__":
    splash(TITLE, SUBTITLE)
    for k, (term, defn) in GLOSSARY.items():
        lower_third(k, term, defn)
