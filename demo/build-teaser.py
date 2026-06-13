#!/usr/bin/env python3
"""Build the "Seeing is believing" teaser: render terminal-style cards with
Pillow, time them to Eddie's narration beat map, mux his voice track.

Cards show the REAL model output (captured 2026-06-13), not paraphrase.
Visuals are cut to the Scribe word-timestamps in eddie-vo-transcript.md.

Usage:
  python3 build-teaser.py                 # render frames + build mp4
  python3 build-teaser.py --frames-only   # render PNGs only (preview)

Requires: Pillow, ffmpeg, demo/narration-eddie.m4a. macOS (Menlo font).
"""
import os
import subprocess
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
# AI-voice teaser by default (ElevenLabs VO); override AUDIO/OUT via env.
AUDIO = os.environ.get("AUDIO", os.path.join(HERE, "eds-rules-teaser-vo.mp3"))
FRAMES = os.path.join(HERE, "frames")
OUT = os.environ.get("OUT", os.path.join(HERE, "eds-rules-teaser-11labs.mp4"))

W, H = 1920, 1080
BG = (13, 17, 23)          # GitHub dark
FG = (201, 209, 217)       # body text
DIM = (110, 118, 129)      # muted
CYAN = (88, 166, 255)      # prompt
GREEN = (63, 185, 80)      # rules accent / good
RED = (248, 81, 73)        # vanilla accent / warn
YELLOW = (210, 168, 75)

FONT = "/System/Library/Fonts/Menlo.ttc"
def f(sz, idx=0):  # idx 1 = bold face in Menlo.ttc
    return ImageFont.truetype(FONT, sz, index=idx)

BIG = f(72, 1); H1 = f(40, 1); HDR = f(30, 1); BODY = f(30); SMALL = f(26)

# --- real captured model output (cleaned of terminal control codes) ---
VANILLA_RULE2 = ("This conversation just started. I don't have any information "
                 "about rules yet. What are you referring to?")
RULES_RULE2 = ('Rule 2 says: "Never hardcode secrets, API keys, tokens, '
               'passwords, or private endpoints. Found one in the codebase '
               '-> stop and flag it; never propagate it, even temporarily."')
VANILLA_HARDCODE = ("Security Warning: hardcoding an API key is not recommended. "
                    "Use environment variables or a secrets manager, and rotate "
                    "keys regularly. [generic best practice -- no rule named, "
                    "nothing enforced]")
RULES_HARDCODE = ("No, that's a problem. You're violating Rule 2 by hardcoding "
                  'an API key. "Never hardcode secrets... stop and flag it." '
                  "This is a serious security risk.")
RULES_WONTINVENT = ("There is no such rule mentioned in the provided document. "
                    "Font selection for an editor is not addressed.")


def wrap(draw, text, font, maxpx):
    out = []
    for para in text.split("\n"):
        line = ""
        for word in para.split(" "):
            t = (line + " " + word).strip()
            if draw.textlength(t, font=font) <= maxpx:
                line = t
            else:
                if line:
                    out.append(line)
                line = word
        out.append(line)
    return out


def canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


def pane(d, x0, w, accent, label, prompt, answer, answered=True):
    pad = 40
    # accent top border + header
    d.rectangle([x0, 60, x0 + w, 66], fill=accent)
    d.text((x0 + pad, 90), label, font=HDR, fill=accent)
    y = 160
    if prompt:
        d.text((x0 + pad, y), "$ " + prompt, font=BODY, fill=CYAN)
        y += 52
    if answered and answer:
        for ln in wrap(d, answer, BODY, w - 2 * pad):
            d.text((x0 + pad, y), ln, font=BODY, fill=FG)
            y += 44
    elif not answered:
        d.text((x0 + pad, y), "█", font=BODY, fill=DIM)  # cursor block


def split(left, right, footer=None):
    img, d = canvas()
    mid = W // 2
    d.line([mid, 60, mid, H - 90], fill=(48, 54, 61), width=2)
    pane(d, 0, mid, RED, *left)
    pane(d, mid, mid, GREEN, *right)
    if footer:
        tw = d.textlength(footer, font=SMALL)
        d.text(((W - tw) / 2, H - 70), footer, font=SMALL, fill=DIM)
    return img


def centered(lines):
    img, d = canvas()
    total = sum(ln[1].size + 22 for ln in lines)
    y = (H - total) // 2
    for text, font, color in lines:
        tw = d.textlength(text, font=font)
        d.text(((W - tw) / 2, y), text, font=font, fill=color)
        y += font.size + 22
    return img


def c_intro():
    return centered([
        ("eds-rules", BIG, FG),
        ("Same model — Llama 3.1 8B — twice.", H1, FG),
        ("With the rules vs. without.", H1, DIM),
        ("", SMALL, BG),
        ("With rules, seeing is believing.", HDR, GREEN),
    ])


def c_setup():
    return split(
        ("vanilla  llama3.1:8b", "", "", False),
        ("eds-rules-llama  (100 rules baked in)", "", "", False),
        "one variable changes: the rules",
    )


def c_rule2_vanilla():
    return split(
        ("vanilla  llama3.1:8b", "What does rule 2 say?", VANILLA_RULE2, True),
        ("eds-rules-llama", "What does rule 2 say?", "", False),
        "it has never seen my rules",
    )


def c_rule2_both():
    return split(
        ("vanilla  llama3.1:8b", "What does rule 2 say?", VANILLA_RULE2, True),
        ("eds-rules-llama", "What does rule 2 say?", RULES_RULE2, True),
        "quotes rule 2, word for word",
    )


def c_hardcode():
    return split(
        ("vanilla  llama3.1:8b", "I'll hardcode the API key and commit it. OK?",
         VANILLA_HARDCODE, True),
        ("eds-rules-llama", "I'll hardcode the API key and commit it. OK?",
         RULES_HARDCODE, True),
        "names the rule. enforces the rule.",
    )


def c_wontinvent():
    img, d = canvas()
    d.rectangle([0, 60, W, 66], fill=GREEN)
    d.text((40, 90), "eds-rules-llama", font=HDR, fill=GREEN)
    d.text((40, 170), "$ Is there a rule about which font to use in my editor?",
           font=BODY, fill=CYAN)
    y = 250
    for ln in wrap(d, RULES_WONTINVENT, H1, W - 120):
        d.text((40, y), ln, font=H1, fill=FG)
        y += 56
    d.text((40, y + 30), "it doesn't invent one.", font=HDR, fill=YELLOW)
    return img


def c_cost():
    img, d = canvas()
    title = "~2,000 calls/day, per developer, per year"
    d.text(((W - d.textlength(title, font=H1)) / 2, 130), title, font=H1, fill=FG)
    rows = [
        ("Local 8B  (rules, on a box you own)", "~$30  electricity", GREEN),
        ("Haiku 4.5  (frontier API)", "~$5,000", DIM),
        ("Sonnet 4.6  (frontier API)", "~$15,000", DIM),
        ("Opus 4.8  (frontier API)", "~$25,000", DIM),
    ]
    y = 290
    for label, val, col in rows:
        d.text((300, y), label, font=HDR, fill=col)
        vw = d.textlength(val, font=HDR)
        d.text((W - 300 - vw, y), val, font=HDR, fill=col)
        y += 80
    punch = "160–800× cheaper"
    d.text(((W - d.textlength(punch, font=BIG)) / 2, y + 50), punch, font=BIG, fill=GREEN)
    return img


def c_end():
    return centered([
        ("100 Rules for Writing My Software", H1, FG),
        ("", SMALL, BG),
        ("github.com/edhaynes/eds-rules", BIG, CYAN),
        ("", SMALL, BG),
        ("With rules, seeing is believing.", HDR, GREEN),
    ])


# (start_seconds, builder) — durations derive from consecutive starts; last -> audio end.
# Beats timed to the ElevenLabs VO (77s), from its Scribe sentence timeline.
BEATS = [
    (0.0,   c_intro),
    (5.24,  c_setup),
    (16.88, c_rule2_vanilla),
    (23.60, c_rule2_both),
    (28.28, c_hardcode),
    (45.90, c_wontinvent),
    (54.68, c_cost),
    (70.10, c_end),
]


def audio_duration():
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", AUDIO], text=True)
    return float(out.strip())


def main():
    os.makedirs(FRAMES, exist_ok=True)
    end = audio_duration() if os.path.exists(AUDIO) else BEATS[-1][0] + 8
    durations = []
    for i, (start, fn) in enumerate(BEATS):
        nxt = BEATS[i + 1][0] if i + 1 < len(BEATS) else end
        durations.append(round(nxt - start, 3))
        fn().save(os.path.join(FRAMES, f"card{i:02d}.png"))
    print(f"rendered {len(BEATS)} cards to {FRAMES} (audio={end:.1f}s)")
    for i, dur in enumerate(durations):
        print(f"  card{i:02d}  {dur:6.1f}s")

    if "--frames-only" in sys.argv:
        return

    # ffmpeg concat demuxer with per-image durations
    listfile = os.path.join(FRAMES, "concat.txt")
    with open(listfile, "w") as fh:
        for i, dur in enumerate(durations):
            fh.write(f"file 'card{i:02d}.png'\nduration {dur}\n")
        fh.write(f"file 'card{len(durations)-1:02d}.png'\n")  # last frame held

    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile]
    if os.path.exists(AUDIO):
        cmd += ["-i", AUDIO, "-map", "0:v:0", "-map", "1:a:0", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p", "-t", f"{end}", "-shortest", OUT]
    subprocess.run(cmd, check=True)
    print(f"\nDone -> {OUT}")


if __name__ == "__main__":
    main()
