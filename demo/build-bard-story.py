#!/usr/bin/env python3
"""Bard — the whole story, investor cut (3–5 min, per-slide maestro TTS).

One unified narrative across the three layers of the stack:
  bard-infra  — WHERE it runs : a zero-trust fabric of the compute you already own.
  logicOS     — HOW  it runs  : a scheduler that is a decision procedure; proven, deterministic.
  Vulcan      — WHAT it decides: provable AI; prove-or-refuse; names the rule; ~1M params, certifiable.

Thesis: "computing you can prove and own" — the antithesis of probabilistic, rented, black-box cloud.
Reuses the v2 machinery (navy+gold Bard brand, ElevenLabs maestro per-slide TTS with on-disk cache,
ffmpeg concat). ELEVEN_API_KEY read from env, never hardcoded. Claims grounded in the repos — no
overclaim (logicOS = behavioral/scheduling guarantees, NOT a WCET/timing bound).

Usage:  ELEVEN_API_KEY=... python3 build-bard-story.py
Requires: Pillow, ffmpeg/ffprobe.
"""
import hashlib
import json
import os
import subprocess
import tempfile
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw

# Reuse the v2 brand primitives verbatim so the look matches the shipped Vulcan×QNX cut.
import importlib.util

_V2 = Path(__file__).resolve().parent / "build-vulcan-v2.py"
_spec = importlib.util.spec_from_file_location("vulcan_v2", _V2)
v2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(v2)

# Brand constants / helpers pulled from v2 (single source of truth for the look).
W, H = v2.W, v2.H
NAVY, GOLD, WHITE, DIM, STEEL, RED = v2.NAVY, v2.GOLD, v2.WHITE, v2.DIM, v2.STEEL, v2.RED
font, wrap, center, card_text, _box = v2.font, v2.wrap, v2.center, v2.card_text, v2._box

HERE = Path(__file__).resolve().parent
OUT = HERE / "podcast" / "bard-story.mp4"
OWL = HERE / "assets" / "vulcan-owl-gold.png"
CACHE = HERE / "assets" / ".tts_cache"
VOICE_ID = "xnE7vmHjTg1xy0WXwuIX"            # maestro (confirmed)
TTS_MODEL = "eleven_multilingual_v2"
API_KEY = os.environ.get("ELEVEN_API_KEY") or os.environ.get("ELEVENLABS_API_KEY")


def base():
    """Bard-branded base card — owl + BARD wordmark, gold rule, confidential footer.

    Unlike the v2 cut this is a general investor pitch, not the QNX audition, so the QNX logo
    and every QNX/BlackBerry name are dropped — traction is framed as a generic safety-RTOS vendor.
    """
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    if OWL.exists():
        owl = Image.open(OWL).convert("RGBA")
        owl.thumbnail((128, 128))
        img.paste(owl, (56, 36), owl)
    d.text((196, 56), "BARD", font=font(54), fill=GOLD)
    d.text((198, 120), "computing you can prove and own", font=font(22, False), fill=DIM)
    nda = "CONFIDENTIAL — NDA REQUIRED"
    d.text(((W - d.textlength(nda, font=font(20))) / 2, H - 46), nda, font=font(20), fill=DIM)
    d.rectangle([0, H - 8, W, H], fill=GOLD)
    return img, d


# v2.center / v2.card_text call v2.base() (the QNX-branded one). Re-point them at ours so every
# card carries the Bard-story header instead of the QNX-pitch header.
v2.base = base


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


def _layer(d, x, y, w, h, name, role, tag, accent=GOLD):
    d.rounded_rectangle([x, y, x + w, y + h], radius=18, fill=NAVY, outline=accent, width=4)
    d.text((x + 36, y + 22), name, font=font(50), fill=accent)
    d.text((x + 36, y + 86), role, font=font(28, False), fill=WHITE)
    tw = d.textlength(tag, font=font(26, False))
    d.text((x + w - 36 - tw, y + (h - 26) / 2), tag, font=font(26, False), fill=DIM)


def card_stack():
    img, d = base()
    title = "One stack. Proven top to bottom. Yours."
    d.text(((W - d.textlength(title, font=font(46))) / 2, 196), title, font=font(46), fill=GOLD)
    x, w, h, gap = 460, 1000, 150, 30
    y = 320
    _layer(d, x, y, w, h, "Vulcan", "what it decides — provable AI", "prove · or refuse")
    _layer(d, x, y + (h + gap), w, h, "logicOS", "how it runs — deterministic scheduler",
           "no inversion · no starvation")
    _layer(d, x, y + 2 * (h + gap), w, h, "bard-infra", "where it runs — your zero-trust fabric",
           "nothing leaves your network")
    return img


def card_bardinfra():
    img, d = base()
    center(d, [("bard-infra", 92, GOLD),
               ("Pool the compute you already own", 46, WHITE),
               ("into one fleet — a desktop, a GPU box, a laptop.", 38, WHITE),
               ("", 12, DIM),
               ("Zero-trust. Self-hosted. Nothing leaves your network.", 40, GOLD),
               ("Shipping today — the LLM is one plugin, not the product.", 32, DIM)])
    return img


def card_logicos():
    img, d = base()
    center(d, [("logicOS", 92, GOLD),
               ("The scheduler as a decision procedure", 46, WHITE),
               ("Given the runqueue, which task runs next — provably.", 38, WHITE),
               ("", 12, DIM),
               ("No task starves. No priority inversion. Deterministic.", 40, GOLD),
               ("We sell the guarantee, not the speed.", 32, DIM)])
    return img


def card_vulcan():
    img, d = base()
    center(d, [("Vulcan", 92, GOLD),
               ("Prove. Or refuse.", 50, WHITE),
               ("It names the exact rule it enforced —", 38, WHITE),
               ("no recursion, no unbounded loop, no dynamic memory.", 38, WHITE),
               ("", 12, DIM),
               ("~1M parameters. Small enough to audit, and to certify.", 40, GOLD)])
    return img


def card_proveguess():
    img, d = base()
    cw = 760
    lx, rx, ty, bh = 150, W - 150 - cw, 360, 360
    d.rounded_rectangle([lx, ty, lx + cw, ty + bh], radius=18, outline=GOLD, width=4)
    d.text((lx + 40, ty + 28), "VULCAN", font=font(54), fill=GOLD)
    for i, t in enumerate(["100%, deterministic", "names the rule",
                           "~1M params — auditable", "runs on the critical core"]):
        d.text((lx + 40, ty + 120 + i * 56), "• " + t, font=font(34, False), fill=WHITE)
    d.rounded_rectangle([rx, ty, rx + cw, ty + bh], radius=18, outline=DIM, width=3)
    d.text((rx + 40, ty + 28), "2B-param model", font=font(54), fill=DIM)
    for i, t in enumerate(["ask twice, two answers", "cites nothing",
                           "2 billion params — opaque", "cannot be certified"]):
        d.text((rx + 40, ty + 120 + i * 56), "• " + t, font=font(34, False), fill=DIM)
    head = "Same code. Two answers — or one proof."
    d.text(((W - d.textlength(head, font=font(44))) / 2, 232), head, font=font(44), fill=GOLD)
    return img


def card_panicstop():
    img, d = base()
    center(d, [("PANIC STOP", 120, RED),
               ("...while the HUD firmware is updating", 40, DIM),
               ("", 14, DIM),
               ("Brakes respond — deterministically.", 52, WHITE),
               ("Freedom from interference.  PROVEN.", 46, GOLD)])
    return img


def card_traction():
    img, d = base()
    rows = [
        "Certified CAN-bus detector runs on a safety-certified RTOS target",
        "Tier-one safety-RTOS vendor in active conversation",
        "Proofs independently validated by a mathematician",
        "bard-infra shipping · Vulcan + logicOS demonstrable today",
    ]
    center(d, [("Where it stands", 52, GOLD)] + [("• " + r, 34, WHITE) for r in rows])
    return img


def card_market():
    img, d = base()
    center(d, [("The wedge", 56, GOLD),
               ("Markets that cannot use “probably”:", 42, WHITE),
               ("", 8, DIM),
               ("avionics — DO-178C · ARINC 653", 36, WHITE),
               ("automotive — ISO 26262 · ASIL-D", 36, WHITE),
               ("medical — IEC 62304", 36, WHITE),
               ("industrial & defense — IEC 61508", 36, WHITE),
               ("", 8, DIM),
               ("plus privacy-critical — your data, your fleet, your network", 36, GOLD)])
    return img


def card_finale():
    img, d = base()
    center(d, [("Computing you can prove and own.", 72, GOLD),
               ("From the home fabric to the safety-critical core.", 48, WHITE),
               ("", 20, DIM),
               ("bardtek.com   ·   “Ed’s 100 Rules” on Amazon", 32, DIM)])
    return img


SLIDES = [
    (lambda: card_text("We made computers fast.",
                       "We forgot to make them trustworthy."),
     "For seventy years we made computers faster. Somewhere along the way we stopped asking whether "
     "we could trust them — or even whether we still owned them."),
    (card_bio, "I'm Ed Haynes. For forty-seven years I've built the systems that cannot fail, and "
               "left a trail of press releases doing it."),
    (card_trail, "The first Top-Secret-certified encryptor. The first certified IPv6 stack. Wind "
                 "River's first carrier-grade platform. Safety-critical rail with Alstom and Red "
                 "Hat. First, certified, shipped — every time."),
    (lambda: card_text("Computing you can prove and own."),
     "So this is what we're building. Computing you can prove, and computing you own. The opposite "
     "of a rented, probabilistic black box in someone else's cloud. One conviction, three layers."),
    (card_stack,
     "One stack, proven from the bottom up. Bard-infra — where it runs. Logic O S — how it runs. "
     "And Vulcan — what it decides. Each layer earns the trust the layer above it depends on."),
    (card_bardinfra,
     "Start at the bottom. Bard-infra pools the compute you already own — a desktop, a G P U box, a "
     "laptop — into one fleet you control. Zero-trust, self-hosted, and nothing ever leaves your "
     "network. It ships today, and the language model is just one plugin on it, not the product."),
    (card_logicos,
     "On top of that runs logic O S. Its scheduler isn't a heuristic — it's a decision procedure "
     "that answers one question provably: given everything waiting, which task runs next? No task "
     "starves. No priority inversion. Deterministic to the bit. We sell the guarantee, not the speed."),
    (card_vulcan,
     "And at the top sits Vulcan — the part everyone else leaves to chance. Vulcan proves, or it "
     "refuses, and it names the exact rule it enforced: no recursion, no unbounded loop, no dynamic "
     "memory. One million parameters — small enough to audit, and small enough to certify."),
    (card_proveguess,
     "Here's why that matters. A two-billion-parameter model can tell you code looks safe. Ask it "
     "twice and you may get two answers, and it can't tell you which rule it checked — because it "
     "never reasoned about rules. Vulcan gives you one proof, every time, and names it."),
    (card_panicstop,
     "Put the whole stack in a car. The driver slams the brakes — and at that exact instant the "
     "heads-up display is taking a firmware update. Two tasks, one core. Vulcan admitted that update "
     "only after proving it cannot steal a microsecond from the brakes. So the panic stop completes, "
     "deterministically, while the display updates. Freedom from interference — proven."),
    (card_traction,
     "This isn't a deck. Bard-infra is shipping. Vulcan and logic O S run today. The certified "
     "detector already runs on a safety-certified R T O S target, a tier-one vendor is in active "
     "conversation, and the proofs have been independently validated by a mathematician."),
    (card_market,
     "And it points at the markets that are never allowed to say probably. In avionics, that means "
     "D O one-seventy-eight C, and ARINC six-fifty-three. In automotive, I S O twenty-six-two-six-two. "
     "In medical, in industrial, in defense — the same demand: prove it. And then there's the "
     "privacy-critical world — your data, your fleet, your network. Provable where it must be "
     "proven; owned where it must be owned."),
    (card_finale,
     "Computing you can prove and own — from the home fabric all the way to the safety-critical "
     "core. That's the company. Let's talk about building it together."),
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
            tail = 1.8 if i == len(SLIDES) - 1 else 0.4
            d = dur(mp3) + tail
            total += d
            lf.write(f"file '{png}'\nduration {d:.3f}\n")
            af.write(f"file '{mp3}'\n")
            print(f"  slide {i}: {d:.1f}s", flush=True)
        lf.write(f"file '{tmp / f's{len(SLIDES)-1:02d}.png'}'\n")
    full_audio = tmp / "vo.mp3"
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat,
                    "-c:a", "libmp3lame", "-b:a", "192k", str(full_audio)],
                   check=True, capture_output=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # Force CONSTANT frame rate (-vsync cfr) + faststart. The concat image demuxer's per-slide
    # `duration` directives yield a variable-frame-rate file that ffmpeg reads fine but QuickTime
    # mishandles — it stops the audio at the first VFR timestamp discontinuity (~18s). CFR fixes it.
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listf), "-i", str(full_audio),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-vsync", "cfr", "-g", "60",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-movflags", "+faststart", "-shortest", str(OUT)],
        check=True, capture_output=True)
    print(f"wrote {OUT}  ({len(SLIDES)} slides, ~{total:.0f}s)")


if __name__ == "__main__":
    main()
