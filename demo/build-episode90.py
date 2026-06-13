#!/usr/bin/env python3
"""Episode 90 (~10:24) in Steve's "Black_Template" format: black bg, Arial,
Red Hat red accents, Red Hat logo (toggle), disclaimer on the title card.
Cards timed to the Scribe sentence timeline of demo/narration-ep90.m4a.

Usage:  python3 build-episode90.py [--frames-only]
Env:    LOGO=redhat (default) | eds        (which brand mark to stamp)
Requires: Pillow, ffmpeg, demo/narration-ep90.m4a, demo/assets/redhat-logo-white.png
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.environ.get("AUDIO", os.path.join(HERE, "narration-ep90.m4a"))
FRAMES = os.path.join(HERE, "frames-ep90")
OUT = os.environ.get("OUT", os.path.join(HERE, "eds-rules-ep90.mp4"))
LOGO_MODE = os.environ.get("LOGO", "redhat")
RH_LOGO = os.path.join(HERE, "assets", "redhat-logo-white.png")

W, H = 1920, 1080
BG = (16, 16, 16)            # near-black (template lt2)
RED = (238, 0, 0)            # accent1
RED2 = (204, 0, 0)
WHITE = (255, 255, 255)
GRAY = (191, 191, 191)       # accent5
DGRAY = (128, 128, 128)      # accent6

def arial(sz, bold=False):
    p = ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
         else "/System/Library/Fonts/Supplemental/Arial.ttf")
    return ImageFont.truetype(p, sz)

BIG = arial(132, True); H1 = arial(56, True); HDR = arial(40, True)
BODY = arial(38); SMALL = arial(28)

_logo = None
def logo():
    global _logo
    if _logo is None and LOGO_MODE == "redhat" and os.path.exists(RH_LOGO):
        im = Image.open(RH_LOGO).convert("RGBA")
        scale = 132 / im.width
        _logo = im.resize((132, max(1, int(im.height * scale))))
    return _logo


def base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    lg = logo()
    if lg is not None:
        img.paste(lg, (W - lg.width - 70, 64), lg)
    else:  # eds text mark
        d.text((W - 360, 70), "ED'S 100 RULES", font=SMALL, fill=GRAY)
    return img, d


def wrap(d, text, font, maxpx):
    out = []
    for para in text.split("\n"):
        line = ""
        for word in para.split(" "):
            t = (line + " " + word).strip()
            if d.textlength(t, font=font) <= maxpx:
                line = t
            else:
                if line: out.append(line)
                line = word
        out.append(line)
    return out


def centered(lines, gap=24):
    img, d = base()
    total = sum(ln[1].size + gap for ln in lines)
    y = (H - total) // 2
    for text, font, color in lines:
        for ln in (wrap(d, text, font, W - 240) or [""]):
            w = d.textlength(ln, font=font)
            d.text(((W - w) / 2, y), ln, font=font, fill=color)
            y += font.size + gap
    return img


def heading(title, items, accent=RED):
    img, d = base()
    d.rectangle([120, 150, 300, 162], fill=accent)
    d.text((120, 188), title, font=H1, fill=WHITE)
    y = 320
    for it in items:
        d.text((140, y + 6), "—", font=HDR, fill=accent)
        for i, ln in enumerate(wrap(d, it, HDR, W - 420)):
            d.text((210, y), ln, font=HDR, fill=WHITE if i == 0 else GRAY)
            y += 56
        y += 26
    return img


# ---- cards ----
def c_title():
    img = centered([
        ("ED'S 100 RULES", H1, GRAY),
        ("Episode 90", BIG, WHITE),
        ("Brought to you by the number 90 and the letter C", HDR, RED),
    ])
    d = ImageDraw.Draw(img)
    disc = "Personal technology blog — opinions expressed are my own and not those of Red Hat."
    w = d.textlength(disc, font=SMALL)
    d.text(((W - w) / 2, H - 80), disc, font=SMALL, fill=DGRAY)
    return img

def c_ninety(): return centered([
    ("Ninety.", BIG, WHITE),
    ("my class number — USNA 1990", HDR, GRAY),
    ("a right angle  ·  the rule that comes first", HDR, RED)])

def c_powell(): return centered([
    ("I was in the stands as a senior", H1, WHITE),
    ("when Admiral William Crowe handed the Joint Chiefs", HDR, GRAY),
    ("to General Colin Powell.", HDR, GRAY)])

def c_rule90(): return centered([
    ("Powell's rule: 40–70%", H1, GRAY),
    ("gather 40–70% of the info, then trust your gut", HDR, GRAY),
    ("In software there's less room for error —", HDR, WHITE),
    ("so I made it 90%, in honor of my class.", H1, RED)])

def c_rule90_applied(): return centered([
    ("The 90% rule", H1, WHITE),
    ("At 90% certainty of what I'd say, the AI just continues.", HDR, GRAY),
    ("100 opinionated rules = it knows how I think.", HDR, RED)])

def c_letterC(): return centered([
    ("Brought to you by the letter", H1, GRAY),
    ("C", BIG, RED),
    ("Red Hat was high-school baseball → the pros.", HDR, GRAY)])

def c_c1(): return centered([
    ("The first C", HDR, RED),
    ("a C in algorithms", H1, WHITE),
    ("the only CS class I didn't ace — I'm no theorist", HDR, GRAY)])

def c_c2(): return centered([
    ("The second C", HDR, RED),
    ("a C programmer", H1, WHITE),
    ("TACLANE, General Dynamics, the '90s — the first", HDR, GRAY),
    ("Top-Secret-rated internet encryptor. Never loved C++.", HDR, GRAY)])

def c_wordthinker(): return centered([
    ("I'm a word thinker, not a visual one —", H1, WHITE),
    ("which is exactly why I'm good at LLM prompts.", HDR, RED),
    ("(Steve's the visual thinker. His slides look fantastic.)", HDR, GRAY)])

def c_c3(): return centered([
    ("The third C", HDR, RED),
    ("Claude", BIG, WHITE),
    ("covers my two deficits: algorithms, and OO design.", HDR, GRAY)])

def c_oo(): return centered([
    ("AI organizes relationships — that's object-oriented.", H1, WHITE),
    ("It turns my scattered word-fragments of architecture", HDR, GRAY),
    ("into something elegant. Polymorphism and all.", HDR, RED)])

def c_recap(): return centered([
    ("90, and the three C's:", H1, WHITE),
    ("C in algorithms · C programmer · Claude", HDR, RED),
    ("(these days I'm more of a Python programmer.)", HDR, GRAY)])

def c_whycavg(): return centered([
    ("Why does AI code like a C-average programmer?", H1, WHITE),
    ("It was trained on average code —", HDR, GRAY),
    ("first-year repos, copied and hardcoded. ~95% of it.", HDR, RED)])

def c_granite(): return centered([
    ("Next project:", HDR, RED),
    ("train a 2B IBM Granite model as my PM", H1, WHITE),
    ("on the 100 rules — ~30 minutes on a MacBook.", HDR, GRAY)])

def c_rules(): return heading("The rules are standing law", [
    "Scan for secrets before every commit — no scan, no ship",
    "Never hardcode a secret. Never delete files. Never rewrite history.",
    "Clean up after yourself; delete dead code",
    "Re-version the docs when a decision changes; version always visible"])

def c_pushmain(): return centered([
    ("Push to main — early and often.", H1, WHITE),
    ("People fight me on this. But AI does merges right ~95%", HDR, GRAY),
    ("of the time — so there's no reason to hoard local work.", HDR, RED)])

def c_personas1(): return heading("Five personas, not just Claude", [
    "Jason — project manager. Doesn't code; he organizes.",
    "Claudius — the architect. Smartest, longest-running model; in the cloud."])

def c_personas2(): return heading("The crew, continued", [
    "Claude — backend. Careful; reuses high-star open source first.",
    "Linda — research & go-to-market. (Sharp as a librarian, looks it too.)"])

def c_cost(): return centered([
    ("A small model, trained on the rules, makes a fine Jason —", H1, WHITE),
    ("and he manages the expensive models.", HDR, GRAY),
    ("$20/mo Claude + $20 of electricity. Don't cook the planet.", HDR, RED)])

def c_plan(): return centered([
    ("One rule a day. 100 days.", BIG, WHITE),
    ("Me and Steve trading off, guests from Red Hat,", HDR, GRAY),
    ("and a pseudo-proof for why each rule works.", HDR, RED)])

def c_cta(): return centered([
    ("github.com/edhaynes/eds-rules", H1, RED),
    ("Take what you like, fork what you don't.", HDR, GRAY),
    ("Find a rule I'm missing — or one that belongs in the top 20.", HDR, WHITE)])

def c_mace(): return centered([
    ("A funny one to close.", H1, WHITE),
    ("A classmate asked: why is our USNA Class-of-'90 crest", HDR, GRAY),
    ("behind a congresswoman on TV? No idea — probably a", HDR, GRAY),
    ("colleague's office. Not accusing anyone. Small world.", HDR, RED)])

def c_signoff(): return centered([
    ("My first podcast.", H1, WHITE),
    ("Subscribe, like, comment, send it to a friend.", HDR, GRAY),
    ("No ads — enjoy the free video.", HDR, RED),
    ("See you tomorrow, for rule one.", HDR, WHITE)])


BEATS = [
    (0.0, c_title), (21.58, c_ninety), (36.92, c_powell), (64.86, c_rule90),
    (83.64, c_rule90_applied), (114.26, c_letterC), (136.18, c_c1),
    (157.38, c_c2), (180.60, c_wordthinker), (210.08, c_c3), (242.12, c_oo),
    (261.88, c_recap), (279.88, c_whycavg), (311.72, c_granite),
    (345.10, c_rules), (387.27, c_pushmain), (420.15, c_personas1),
    (447.31, c_personas2), (474.67, c_cost), (500.31, c_plan),
    (529.78, c_cta), (558.35, c_mace), (593.91, c_signoff),
]


def audio_dur():
    return float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", AUDIO], text=True).strip())


def main():
    os.makedirs(FRAMES, exist_ok=True)
    end = audio_dur() if os.path.exists(AUDIO) else BEATS[-1][0] + 20
    durs = []
    for i, (start, fn) in enumerate(BEATS):
        nxt = BEATS[i + 1][0] if i + 1 < len(BEATS) else end
        durs.append(round(nxt - start, 3))
        fn().save(os.path.join(FRAMES, f"c{i:02d}.png"))
    print(f"rendered {len(BEATS)} cards (audio={end:.0f}s, LOGO={LOGO_MODE})")
    if "--frames-only" in sys.argv:
        return
    lst = os.path.join(FRAMES, "concat.txt")
    with open(lst, "w") as fh:
        for i, dr in enumerate(durs):
            fh.write(f"file 'c{i:02d}.png'\nduration {dr}\n")
        fh.write(f"file 'c{len(durs)-1:02d}.png'\n")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst]
    if os.path.exists(AUDIO):
        cmd += ["-i", AUDIO, "-map", "0:v:0", "-map", "1:a:0", "-c:a", "aac", "-b:a", "192k"]
    cmd += ["-c:v", "libx264", "-r", "30", "-pix_fmt", "yuv420p", "-t", f"{end}", "-shortest", OUT]
    subprocess.run(cmd, check=True)
    print(f"\nDone -> {OUT}")


if __name__ == "__main__":
    main()
