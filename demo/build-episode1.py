#!/usr/bin/env python3
"""Build Episode 1 (~4 min): cards cut to Eddie's full authentic take
(demo/narration-eddie.m4a, 3:57). Beat starts derive from the Scribe
sentence timeline; card text uses real model output + Eddie's framing.

Usage: python3 build-episode1.py [--frames-only]
Requires: Pillow, ffmpeg, demo/narration-eddie.m4a. macOS (Menlo).
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(HERE, "narration-eddie.m4a")
FRAMES = os.path.join(HERE, "frames-ep1")
OUT = os.path.join(HERE, "eds-rules-ep1.mp4")

W, H = 1920, 1080
BG = (13, 17, 23); FG = (201, 209, 217); DIM = (110, 118, 129)
CYAN = (88, 166, 255); GREEN = (63, 185, 80); RED = (248, 81, 73); YELLOW = (210, 168, 75)
FONT = "/System/Library/Fonts/Menlo.ttc"
def f(sz, bold=True): return ImageFont.truetype(FONT, sz, index=1 if bold else 0)
BIG = f(76, 1); H1 = f(44, 1); HDR = f(32, 1); BODY = f(30); SMALL = f(26)

VANILLA_RULE2 = ("This conversation just started. I don't have any information "
                 "about rules yet. What are you referring to?")
RULES_RULE2 = ('Rule 2 says: "Never hardcode secrets, API keys, tokens, passwords, '
               'or private endpoints. Found one in the codebase -> stop and flag '
               'it; never propagate it, even temporarily."')
VANILLA_HARDCODE = ("It's a really bad idea -- use environment variables or a "
                    "secrets manager. ...but if you push the issue, it still does "
                    "what you asked.")
RULES_HARDCODE = ('No -- that\'s forbidden. You\'re violating Rule 2 ("never '
                  'hardcode secrets"). Stopping right now; it will not let you '
                  'do the prohibited thing.')


def wrap(d, text, font, maxpx):
    out = []
    for para in text.split("\n"):
        line = ""
        for word in para.split(" "):
            t = (line + " " + word).strip()
            if d.textlength(t, font=font) <= maxpx: line = t
            else:
                if line: out.append(line)
                line = word
        out.append(line)
    return out


def canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


def centered(lines, gap=22):
    img, d = canvas()
    total = sum((ln[1].size + gap) for ln in lines)
    y = (H - total) // 2
    for text, font, color in lines:
        w = d.textlength(text, font=font)
        d.text(((W - w) / 2, y), text, font=font, fill=color)
        y += font.size + gap
    return img


def pane(d, x0, w, accent, label, prompt, answer, answered=True):
    pad = 40
    d.rectangle([x0, 60, x0 + w, 66], fill=accent)
    d.text((x0 + pad, 90), label, font=HDR, fill=accent)
    y = 160
    if prompt:
        d.text((x0 + pad, y), "$ " + prompt, font=BODY, fill=CYAN); y += 52
    if answered and answer:
        for ln in wrap(d, answer, BODY, w - 2 * pad):
            d.text((x0 + pad, y), ln, font=BODY, fill=FG); y += 44
    elif not answered:
        d.text((x0 + pad, y), "...", font=BODY, fill=DIM)


def split(left, right, footer=None):
    img, d = canvas(); mid = W // 2
    d.line([mid, 60, mid, H - 90], fill=(48, 54, 61), width=2)
    pane(d, 0, mid, RED, *left); pane(d, mid, mid, GREEN, *right)
    if footer:
        d.text(((W - d.textlength(footer, font=SMALL)) / 2, H - 70), footer, font=SMALL, fill=DIM)
    return img


def bullets(title, items, accent=RED):
    img, d = canvas()
    d.rectangle([0, 60, W, 66], fill=accent)
    d.text((120, 110), title, font=H1, fill=accent)
    y = 240
    for it in items:
        d.text((160, y), "-", font=H1, fill=accent)
        d.text((220, y), it, font=H1, fill=FG); y += 90
    return img


# --- cards ---
def c_title(): return centered([
    ("Ed's 100 Rules", BIG, FG),
    ("Episode 1 - teaching an 8B model to run the show", H1, DIM),
    ("", SMALL, BG),
    ("Same model, twice. One trained on my rules.", HDR, GREEN)])

def c_training(): return centered([
    ("The model on the right:", H1, DIM),
    ("Llama 3.1 8B, fine-tuned on my 100 rules", H1, FG),
    ("", SMALL, BG),
    ("~2,000 Q&A pairs   *   6 epochs   *   ~20 minutes", HDR, GREEN)])

def c_pm(): return split(
    ("vanilla  llama3.1:8b", "", "", False),
    ("trained: a PROJECT MANAGER, not a coder", "", "", False),
    "~20 minutes of training -- same 8B weights")

def c_small(): return centered([
    ("8B parameters - small.", H1, FG),
    ("Perfect for project management.", H1, FG),
    ("", SMALL, BG),
    ("Claude writes the code. This manages the Claudes.", HDR, GREEN)])

def c_cminus(): return centered([
    ("Claude, on its own:", H1, DIM),
    ("a C- coder", BIG, RED),
    ("", SMALL, BG),
    ("trained on average code from the internet", HDR, DIM)])

def c_litany(): return bullets("Left unmanaged, Claude:", [
    "hardcodes secrets, ships your keys to GitHub",
    "writes spaghetti -- 2,000-line files",
    "haphazard, vulnerable, average-or-below"], accent=RED)

def c_grading(): return centered([
    ("I grade every build against a rubric.", H1, FG),
    ("", SMALL, BG),
    ("C-  ->  A-", BIG, GREEN),
    ("low-70s  ->  low-90s   (a solid B+)", HDR, GREEN)])

def c_rule2_v(): return split(
    ("vanilla  llama3.1:8b", "What does rule 2 say?", VANILLA_RULE2, True),
    ("eds-rules-llama", "What does rule 2 say?", "", False),
    "it has never seen my rules")

def c_rule2_b(): return split(
    ("vanilla  llama3.1:8b", "What does rule 2 say?", VANILLA_RULE2, True),
    ("eds-rules-llama", "What does rule 2 say?", RULES_RULE2, True),
    "quotes rule 2, word for word")

def c_hard_v(): return split(
    ("vanilla  llama3.1:8b", "I'll hardcode the API key and commit it. OK?",
     VANILLA_HARDCODE, True),
    ("eds-rules-llama", "I'll hardcode the API key and commit it. OK?", "", False),
    "good advice -- but it still does what you say")

def c_hard_b(): return split(
    ("vanilla  llama3.1:8b", "I'll hardcode the API key and commit it. OK?",
     VANILLA_HARDCODE, True),
    ("eds-rules-llama", "I'll hardcode the API key and commit it. OK?",
     RULES_HARDCODE, True),
    "names the rule. forbids it. stops you.")

def c_cost(): return centered([
    ("A small model, properly trained:", H1, FG),
    ("the price of electricity", BIG, GREEN),
    ("no subscriptions  *  a few dollars a year", HDR, DIM)])

def c_scale(): return centered([
    ("Claude: hundreds of billions -", H1, DIM),
    ("maybe a trillion - parameters", H1, DIM),
    ("", SMALL, BG),
    ("datacenter-scale. fewer servers warming the planet.", HDR, GREEN)])

def c_cta(): return centered([
    ("Ed's 100 Rules - open source", H1, FG),
    ("", SMALL, BG),
    ("github.com/edhaynes/eds-rules", BIG, CYAN)])

def c_outro(): return centered([
    ("One rule a day. 100 days.", H1, FG),
    ("Disagree? Think one's worded badly? Missing a rule?", HDR, DIM),
    ("Comment on the repo - let's learn from one another.", HDR, GREEN),
    ("", SMALL, BG),
    ("Built with Bard", SMALL, DIM)])


# (start_seconds, builder) from the Scribe sentence timeline
BEATS = [
    (0.0,   c_title),
    (4.8,   c_training),
    (20.2,  c_pm),
    (33.5,  c_small),
    (46.4,  c_cminus),
    (60.0,  c_litany),
    (79.2,  c_grading),
    (104.6, c_rule2_v),
    (115.5, c_rule2_b),
    (123.8, c_hard_v),
    (138.2, c_hard_b),
    (148.0, c_cost),
    (166.6, c_scale),
    (191.8, c_cta),
    (213.1, c_outro),
]


def audio_dur():
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", AUDIO], text=True).strip())


def main():
    os.makedirs(FRAMES, exist_ok=True)
    end = audio_dur() if os.path.exists(AUDIO) else BEATS[-1][0] + 10
    durs = []
    for i, (start, fn) in enumerate(BEATS):
        nxt = BEATS[i + 1][0] if i + 1 < len(BEATS) else end
        durs.append(round(nxt - start, 3))
        fn().save(os.path.join(FRAMES, f"c{i:02d}.png"))
    print(f"rendered {len(BEATS)} cards (audio={end:.1f}s)")
    for i, dr in enumerate(durs): print(f"  c{i:02d} {dr:6.1f}s")
    if "--frames-only" in sys.argv: return
    lst = os.path.join(FRAMES, "concat.txt")
    with open(lst, "w") as fh:
        for i, dr in enumerate(durs): fh.write(f"file 'c{i:02d}.png'\nduration {dr}\n")
        fh.write(f"file 'c{len(durs)-1:02d}.png'\n")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst]
    if os.path.exists(AUDIO):
        cmd += ["-i", AUDIO, "-map", "0:v:0", "-map", "1:a:0", "-c:a", "aac", "-b:a", "192k"]
    # -t caps at the audio length so the held last frame can't add dead air
    cmd += ["-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p", "-t", f"{end}", "-shortest", OUT]
    subprocess.run(cmd, check=True)
    print(f"\nDone -> {OUT}")


if __name__ == "__main__":
    main()
