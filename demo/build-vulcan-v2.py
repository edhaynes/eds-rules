#!/usr/bin/env python3
"""Vulcan × QNX pitch video v2 — Bard-branded, per-slide maestro TTS (true timing).

Each slide gets its own narration chunk (ElevenLabs maestro), so the slide shows for exactly its
spoken duration. Accomplishments + real press-release claims up front; auto-first; CAR▸CANbus▸QNX
[Vulcan+LogicOS] integration diagram; summary close. ELEVEN_API_KEY read from env, never hardcoded.

Usage:  ELEVEN_API_KEY=... python3 build-vulcan-v2.py
"""
import json
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import hashlib

HERE = Path(__file__).resolve().parent
OUT = HERE / "podcast" / "vulcan-qnx-v2.mp4"
OWL = HERE / "assets" / "vulcan-owl-gold.png"      # gold owl from bardtek.com
QNX_LOGO = HERE / "assets" / "qnx-logo.png"        # official QNX white logo (Wikimedia)
CACHE = HERE / "assets" / ".tts_cache"             # per-line TTS cache (don't re-spend credits)
VOICE_ID = "xnE7vmHjTg1xy0WXwuIX"            # maestro (confirmed)
TTS_MODEL = "eleven_multilingual_v2"
API_KEY = os.environ.get("ELEVEN_API_KEY") or os.environ.get("ELEVENLABS_API_KEY")

W, H = 1920, 1080
NAVY = (10, 22, 40)
GOLD = (200, 162, 58)
WHITE = (245, 245, 245)
DIM = (120, 140, 160)
STEEL = (40, 64, 100)
RED = (212, 72, 56)
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


def base():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    if OWL.exists():
        owl = Image.open(OWL).convert("RGBA")
        owl.thumbnail((128, 128))                      # a little bigger, aspect preserved
        img.paste(owl, (56, 36), owl)
    d.text((196, 56), "BARD", font=font(54), fill=GOLD)
    d.text((198, 120), "certified, provable AI", font=font(22, False), fill=DIM)
    if QNX_LOGO.exists():
        q = Image.open(QNX_LOGO).convert("RGBA")
        q.thumbnail((230, 92))                         # official QNX logo, top-right
        img.paste(q, (W - 60 - q.width, 60), q)
    nda = "CONFIDENTIAL — NDA REQUIRED"
    d.text(((W - d.textlength(nda, font=font(20))) / 2, H - 46), nda, font=font(20), fill=DIM)
    d.rectangle([0, H - 8, W, H], fill=GOLD)
    return img, d


def center(d, lines):
    rendered = []
    for text, size, color in lines:
        for ln in wrap(d, text, font(size), W - 360):
            rendered.append((ln, font(size), color))
    total = sum(f.size + 24 for _, f, _ in rendered)
    y = (H - total) // 2 + 30
    for ln, fnt, color in rendered:
        w = d.textlength(ln, font=fnt)
        d.text(((W - w) / 2, y), ln, font=fnt, fill=color)
        y += fnt.size + 24


def card_text(big, sub=None):
    img, d = base()
    lines = [(big, 84, WHITE)] + ([(sub, 46, GOLD)] if sub else [])
    center(d, lines)
    return img


def card_bio():
    img, d = base()
    center(d, [("Ed Haynes", 96, GOLD),
               ("47 years building systems that cannot fail", 44, WHITE),
               ("author, “Ed’s 100 Rules”", 34, DIM)])
    return img


def card_trail():
    img, d = base()
    rows = [
        'TACLANE — first Top-Secret-certified encryptor',
        'Nortel — "first to pass IPv6 Phase II validation"',
        'Wind River Titanium — "industry\'s first commercial Carrier Grade NFVI"',
        'Alstom / Red Hat — safety-critical rail',
    ]
    center(d, [("A trail of press releases", 52, GOLD)] + [(r, 36, WHITE) for r in rows])
    return img


def _box(d, x, y, w, h, label, fill, outline, fsize=34, tcolor=WHITE):
    d.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=fill, outline=outline, width=3)
    tw = d.textlength(label, font=font(fsize))
    d.text((x + (w - tw) / 2, y + (h - fsize) / 2 - 4), label, font=font(fsize), fill=tcolor)


def card_diagram():
    img, d = base()
    d.text((W / 2 - d.textlength("Where it runs", font=font(48)) / 2, 210),
           "Where it runs", font=font(48), fill=GOLD)
    cy = 560
    _box(d, 150, cy - 70, 300, 140, "CAR / ECUs", STEEL, GOLD)
    # CAN bus arrow
    d.line([460, cy, 690, cy], fill=GOLD, width=6)
    d.polygon([(690, cy - 12), (714, cy), (690, cy + 12)], fill=GOLD)
    d.text((470, cy - 56), "CAN bus", font=font(30), fill=DIM)
    # QNX box containing the certified-AI layer
    qx, qw = 730, 1040
    d.rounded_rectangle([qx, cy - 200, qx + qw, cy + 200], radius=22, outline=GOLD, width=4)
    d.text((qx + 28, cy - 192), "QNX  (RTOS, safety-certified)", font=font(34), fill=WHITE)
    d.text((qx + 28, cy - 150), "certified-AI layer:", font=font(28, False), fill=DIM)
    _box(d, qx + 60, cy - 90, 420, 150, "Vulcan", NAVY, GOLD, 56, GOLD)
    _box(d, qx + 540, cy - 90, 420, 150, "LogicOS", NAVY, GOLD, 56, GOLD)
    d.text((qx + 60, cy + 90), "provable · deterministic · 1M params · certifiable",
           font=font(28, False), fill=DIM)
    return img


def _car(d, x, y):
    """A small car icon: body + cabin + wheels, steel/gold."""
    d.rounded_rectangle([x, y + 34, x + 300, y + 96], radius=18, fill=STEEL, outline=GOLD, width=3)
    d.line([(x + 78, y + 36), (x + 116, y), (x + 196, y), (x + 232, y + 36)], fill=GOLD, width=3)
    d.ellipse([x + 54, y + 84, x + 100, y + 130], fill=NAVY, outline=GOLD, width=4)
    d.ellipse([x + 200, y + 84, x + 246, y + 130], fill=NAVY, outline=GOLD, width=4)
    d.text((x + (300 - d.textlength("vehicle", font=font(26))) / 2, y + 52), "vehicle",
           font=font(26), fill=WHITE)


def card_scenario():
    img, d = base()
    title = "In the vehicle — one core, two jobs"
    d.text(((W - d.textlength(title, font=font(46))) / 2, 184), title, font=font(46), fill=GOLD)
    _car(d, 150, 470)
    d.line([470, 560, 612, 560], fill=GOLD, width=5)
    d.polygon([(612, 548), (636, 560), (612, 572)], fill=GOLD)
    d.text((480, 506), "CAN bus", font=font(26), fill=DIM)
    qx, qy, qw, qh = 660, 360, 1130, 420
    d.rounded_rectangle([qx, qy, qx + qw, qy + qh], radius=20, outline=GOLD, width=4)
    d.text((qx + 28, qy + 16), "QNX  ·  time- & space-partitioned", font=font(30), fill=WHITE)
    d.rounded_rectangle([qx + 40, qy + 74, qx + qw - 40, qy + 200], radius=14, outline=RED, width=3)
    d.text((qx + 64, qy + 90), "BRAKE CONTROL", font=font(40), fill=RED)
    d.text((qx + 64, qy + 144), "ASIL-D · safety-critical · hard real-time",
           font=font(28, False), fill=DIM)
    d.rounded_rectangle([qx + 40, qy + 224, qx + qw - 40, qy + 350], radius=14,
                        outline=STEEL, width=3)
    d.text((qx + 64, qy + 240), "HUD", font=font(40), fill=WHITE)
    d.text((qx + 64, qy + 294), "firmware updating...", font=font(28, False), fill=DIM)
    badge = "Vulcan: admitted — proven safe"
    d.text((qx + qw - 40 - d.textlength(badge, font=font(28)), qy + 250), badge,
           font=font(28), fill=GOLD)
    return img


def card_panicstop():
    img, d = base()
    center(d, [("PANIC STOP", 120, RED),
               ("...while the HUD firmware is updating", 40, DIM),
               ("", 14, DIM),
               ("Brakes respond — deterministically.", 52, WHITE),
               ("Freedom from interference.  PROVEN.", 46, GOLD)])
    return img


def card_summary():
    img, d = base()
    rows = ["TACLANE", "Nortel IPv6", "Wind River Titanium", "Alstom / Red Hat"]
    center(d, [(" →  ".join(rows), 40, WHITE),
               ("QNX × Vulcan  —  ?", 56, GOLD),
               ("QNX certifies the OS.  Vulcan certifies the AI.", 40, WHITE)])
    return img


def card_finale():
    img, d = base()
    center(d, [("The next press release is yours.", 74, GOLD),
               ("What does your quote say?", 56, WHITE),
               ("", 20, DIM),
               ("bardtek.com   ·   “Ed’s 100 Rules” on Amazon", 32, DIM)])
    return img


SLIDES = [
    (card_bio, "I'm Ed Haynes. For forty-seven years I've built the systems that cannot fail, and "
               "left a trail of press releases doing it."),
    (card_trail, "The first Top-Secret-certified encryptor. The first certified IPv6 stack. Wind "
                 "River's first carrier-grade platform. Safety-critical rail with Alstom and Red "
                 "Hat. First, certified, shipped, every time."),
    (lambda: card_text("Certified AI for QNX"),
     "Now, the next one. Certified, provable AI, built for QNX."),
    (lambda: card_text("“Probably” is not certified."),
     "In automotive, in industrial, in medical, probably is not a word you get to use. A two "
     "billion parameter model can tell you code looks safe. It cannot prove it."),
    (lambda: card_text("Prove. Or refuse."),
     "Vulcan proves it. A function bound for a safety-critical partition: no dynamic memory, no "
     "unbounded loops, no recursion. Admitted, or refused, naming the exact rule."),
    (lambda: card_text("Same code. Two answers."),
     "The two billion parameter model? Sometimes it catches the violation. Sometimes it misses. "
     "Ask twice, get two answers. It cannot name the rule, because it never reasoned about rules."),
    (card_diagram,
     "This runs where it matters. On the bus, inside QNX, on the safety-critical core. Vulcan and "
     "Logic O S, the certified-AI layer. One million parameters. Deterministic to the bit. Small "
     "enough to audit, and to certify."),
    (card_scenario,
     "Picture it in the vehicle. The driver slams on the brakes — and at that exact moment, the "
     "heads-up display is taking a firmware update. Two tasks, one core. On most systems, that is "
     "a race."),
    (card_panicstop,
     "With Vulcan, it is not a race. The update was admitted to its partition only after Vulcan "
     "proved it cannot allocate memory, cannot loop unbounded, cannot steal a microsecond from the "
     "brakes. So the panic stop completes — deterministically — while the heads-up display updates. "
     "Freedom from interference. Proven."),
    (lambda: card_text("You can certify the prover."),
     "You cannot put a black box through I S O twenty-six-two-six-two. But a proof, and a proover "
     "small enough to verify, that you can certify."),
    (card_summary,
     "QNX certifies the operating system. Vulcan certifies the intelligence on top. Every line on "
     "this list shipped."),
    (card_finale,
     "So... the next press release is yours. What does your quote say?"),
]


def tts(text, path):
    CACHE.mkdir(parents=True, exist_ok=True)
    key = hashlib.md5((VOICE_ID + "|" + TTS_MODEL + "|" + text).encode()).hexdigest()
    cached = CACHE / f"{key}.mp3"
    if cached.exists():
        path.write_bytes(cached.read_bytes())
        return
    body = json.dumps({"text": text, "model_id": TTS_MODEL,
                       "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}", data=body,
        headers={"xi-api-key": API_KEY, "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    cached.write_bytes(data)
    path.write_bytes(data)


def dur(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", str(path)]).strip())


def main():
    if not API_KEY:
        raise SystemExit("ELEVEN_API_KEY not set")
    tmp = Path(tempfile.mkdtemp())
    listf, concat = tmp / "list.txt", tmp / "audio.txt"
    total = 0.0
    with open(listf, "w") as lf, open(concat, "w") as af:
        for i, (render, narration) in enumerate(SLIDES):
            png = tmp / f"s{i:02d}.png"
            render().save(png)
            mp3 = tmp / f"s{i:02d}.mp3"
            tts(narration, mp3)
            tail = 1.8 if i == len(SLIDES) - 1 else 0.35  # hold the finale; small tail elsewhere
            d = dur(mp3) + tail
            total += d
            lf.write(f"file '{png}'\nduration {d:.3f}\n")
            af.write(f"file '{mp3}'\n")
            print(f"  slide {i}: {d:.1f}s", flush=True)
        lf.write(f"file '{tmp / f's{len(SLIDES)-1:02d}.png'}'\n")
    full_audio = tmp / "vo.mp3"
    # Re-encode the concatenated audio (stream-copy of MP3s only plays the first segment).
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat,
                    "-c:a", "libmp3lame", "-b:a", "192k", str(full_audio)],
                   check=True, capture_output=True)
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listf), "-i", str(full_audio),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", str(OUT)],
        check=True, capture_output=True)
    print(f"wrote {OUT}  ({len(SLIDES)} slides, ~{total:.0f}s)")


if __name__ == "__main__":
    main()
