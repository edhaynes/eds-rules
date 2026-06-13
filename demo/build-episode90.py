#!/usr/bin/env python3
"""Episode 90 (re-record, ~11:17) in Steve's "Black Template" format with
visuals. Black bg, Arial, Red Hat red, RH logo (LOGO=redhat|eds), disclaimer
on the title. Cards timed to the Scribe timeline of demo/narration-ep90b.m4a.
Five drawn/cropped visuals: 90° diagram, the 40-70/90 scale, model-size bars,
the crew org chart, and the cropped USNA crest from the Fox frame.

Usage:  python3 build-episode90.py [--frames-only]
Env:    LOGO=redhat|eds   AUDIO=<file>   OUT=<file>
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.environ.get("AUDIO", os.path.join(HERE, "narration-ep90b-clean.m4a"))
FRAMES = os.path.join(HERE, "frames-ep90")
OUT = os.environ.get("OUT", os.path.join(HERE, "eds-rules-ep90.mp4"))
LOGO_MODE = os.environ.get("LOGO", "redhat")
RH_LOGO = os.path.join(HERE, "assets", "redhat-logo-white.png")
CREST = os.path.join(HERE, "assets", "mace-crest.png")

W, H = 1920, 1080
BG = (16, 16, 16); RED = (238, 0, 0); RED2 = (204, 0, 0)
WHITE = (255, 255, 255); GRAY = (191, 191, 191); DGRAY = (110, 110, 110)
BAND = (60, 60, 60)

def arial(sz, bold=False):
    return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial%s.ttf"
                              % (" Bold" if bold else ""), sz)
BIG = arial(120, True); H1 = arial(54, True); HDR = arial(38, True)
BODY = arial(36); SMALL = arial(27)

_logo = None
def logo():
    global _logo
    if _logo is None and LOGO_MODE == "redhat" and os.path.exists(RH_LOGO):
        im = Image.open(RH_LOGO).convert("RGBA")
        _logo = im.resize((128, int(im.height * 128 / im.width)))
    return _logo

def base():
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    lg = logo()
    if lg is not None: img.paste(lg, (W - lg.width - 70, 60), lg)
    else: d.text((W - 360, 66), "ED'S 100 RULES", font=SMALL, fill=GRAY)
    return img, d

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

def centered(lines, gap=24):
    img, d = base()
    total = sum(ln[1].size + gap for ln in lines)
    y = (H - total) // 2
    for text, font, color in lines:
        for ln in (wrap(d, text, font, W - 240) or [""]):
            w = d.textlength(ln, font=font)
            d.text(((W - w) / 2, y), ln, font=font, fill=color); y += font.size + gap
    return img

def topline(d, lines, y0=170):
    y = y0
    for text, font, color in lines:
        for ln in wrap(d, text, font, W - 240):
            w = d.textlength(ln, font=font)
            d.text(((W - w) / 2, y), ln, font=font, fill=color); y += font.size + 12
        y += 8
    return y

def heading(title, items):
    img, d = base()
    d.rectangle([120, 150, 300, 162], fill=RED)
    d.text((120, 188), title, font=H1, fill=WHITE)
    y = 320
    for it in items:
        d.text((140, y + 4), "—", font=HDR, fill=RED)
        for i, ln in enumerate(wrap(d, it, HDR, W - 420)):
            d.text((210, y), ln, font=HDR, fill=WHITE if i == 0 else GRAY); y += 54
        y += 26
    return img

# ---------- visuals ----------
def v_right_angle(img, d):
    ox, oy, L = W // 2 - 170, 900, 330
    d.line([(ox, oy), (ox + L, oy)], fill=RED, width=9)
    d.line([(ox, oy), (ox, oy - L)], fill=RED, width=9)
    s = 52; d.rectangle([ox, oy - s, ox + s, oy], outline=WHITE, width=4)
    d.text((ox + 90, oy - 96), "90°", font=H1, fill=WHITE)

def v_scale(img, d):
    x0, x1, y, h = 360, 1560, 800, 40
    px = lambda v: x0 + (x1 - x0) * v / 100
    d.rectangle([px(40), y, px(70), y + h], fill=BAND)
    d.rectangle([x0, y, x1, y + h], outline=DGRAY, width=3)
    for v in (0, 40, 70, 100):
        d.text((px(v) - 12, y + h + 18), str(v), font=SMALL, fill=GRAY)
    d.text(((px(40) + px(70)) / 2 - 110, y - 56), "Powell: 40–70", font=SMALL, fill=GRAY)
    d.line([(px(90), y - 34), (px(90), y + h + 34)], fill=RED, width=7)
    d.text((px(90) - 24, y - 96), "90", font=HDR, fill=RED)

def _box(d, cx, cy, w, h, name, role):
    d.rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], outline=RED, width=4)
    nw = d.textlength(name, font=HDR); d.text((cx - nw / 2, cy - h / 2 + 18), name, font=HDR, fill=WHITE)
    rw = d.textlength(role, font=SMALL); d.text((cx - rw / 2, cy + 4), role, font=SMALL, fill=GRAY)

def v_orgchart(img, d):
    top = (W // 2, 500)
    _box(d, top[0], top[1], 360, 110, "Jason", "architect / lead")
    row = [("Claude", "back end · C"), ("Claudina", "front end · C++"),
           ("Brutus", "tests · Python"), ("Linda", "research · Groq")]
    n = len(row); span = 1640; x0 = (W - span) / 2; cy = 820
    for i, (nm, rl) in enumerate(row):
        cx = x0 + span * (i + 0.5) / n
        d.line([(top[0], top[1] + 55), (cx, cy - 55)], fill=DGRAY, width=3)
        _box(d, cx, cy, 360, 110, nm, rl)

def v_sizebars(img, d):
    x0 = 360; d.text((x0, 560), "Ed's PM model  ·  ~2B params  ·  runs on an iPhone", font=SMALL, fill=GRAY)
    d.rectangle([x0, 600, x0 + 150, 670], fill=RED)
    d.text((x0, 730), "frontier model  ·  ~1 trillion params  ·  datacenter", font=SMALL, fill=GRAY)
    d.rectangle([x0, 770, x0 + 1200, 840], fill=BAND)
    d.text((x0, 900), "~500× smaller  ·  $20/mo to the dime  ·  sips power", font=HDR, fill=RED)

def v_crest(img, d):
    if not os.path.exists(CREST): return
    c = Image.open(CREST).convert("RGB")
    scale = 470 / c.height; c = c.resize((int(c.width * scale), 470))
    x = (W - c.width) // 2; y = 470
    d.rectangle([x - 6, y - 6, x + c.width + 6, y + c.height + 6], outline=DGRAY, width=3)
    img.paste(c, (x, y))

def visual_card(heads, draw_fn):
    img, d = base(); topline(d, heads); draw_fn(img, d); return img

# ---------- cards ----------
def c_title():
    img = centered([("ED'S 100 RULES", H1, GRAY), ("Episode 90", BIG, WHITE),
                    ("Brought to you by the number 90 and the letter C", HDR, RED)])
    d = ImageDraw.Draw(img)
    disc = "Personal technology blog — opinions expressed are my own and not those of Red Hat."
    d.text(((W - d.textlength(disc, font=SMALL)) / 2, H - 80), disc, font=SMALL, fill=DGRAY)
    return img

def c_ninety(): return visual_card(
    [("Ninety.", BIG, WHITE), ("my class number — USNA 1990 · the rule that comes first", HDR, RED)], v_right_angle)
def c_powell(): return centered([
    ("Admiral Crowe handed the Joint Chiefs to Colin Powell.", H1, WHITE),
    ("I was in the stands — a hot day, glad not to be marching.", HDR, GRAY)])
def c_rule90(): return visual_card([
    ("Powell's 40–70  →  my 90%", H1, WHITE),
    ("gather 40–70%, trust your gut — I tightened it: software has less", HDR, GRAY),
    ("room for error (high-availability, embedded, safety-critical)", HDR, GRAY)], v_scale)
def c_rule90_applied(): return centered([
    ("At 90% sure of what I'd say, the PM just continues.", H1, WHITE),
    ('"Code for an hour. No questions unless you drop below 90%."', HDR, RED),
    ("100 specific, opinionated rules — so it never interrupts.", HDR, GRAY)])
def c_smallmodel(): return visual_card([
    ("A small model, trained on the rules —", H1, WHITE),
    ("runs on my iPhone, iPad, MacBook, and out-manages Claude", HDR, GRAY)], v_sizebars)
def c_letterC(): return centered([
    ("Brought to you by the number 90 —", H1, WHITE),
    ("— and the letter C.", H1, RED), ("(yes, like Sesame Street.)", HDR, GRAY)])
def c_c1(): return centered([
    ("The first C: a C in algorithms.", H1, WHITE),
    ("the only class I didn't ace — advanced math, visual thinking.", HDR, GRAY),
    ("I'm a word and logic thinker — which is exactly why I'm good at prompts.", HDR, RED)])
def c_thinkers(): return centered([
    ("Two kinds of programmer.", H1, WHITE),
    ("Visual thinkers build the GUIs and front ends — their stuff looks great", HDR, GRAY),
    ("(Steve Connors' slides). I'm the device-driver, C-and-assembly guy.", HDR, GRAY)])
def c_c2(): return centered([
    ("The second C: a C programmer.", H1, WHITE),
    ("General Dynamics, Boston — TACLANE, the first Top-Secret-certified", HDR, GRAY),
    ("internet encryptor. 35 years in the field. ~33 people. Billions.", HDR, GRAY)])
def c_jason(): return centered([
    ("Why is my architect bot named Jason?", H1, WHITE),
    ("Jason was my real architect on TACLANE — one of the best I've known.", HDR, GRAY),
    ("On time, under budget. (Like making the Sox and winning the Series as a rookie.)", HDR, RED)])
def c_c3(): return centered([
    ("The third C: Claude.", H1, WHITE),
    ("started in February — under six months. Covers my two deficits:", HDR, GRAY),
    ("turns device-driver-C-hacker thoughts into clean OO, on the right algorithms.", HDR, RED)])
def c_claude_caveat(): return centered([
    ("Honestly? Claude's raw coding is just okay.", H1, WHITE),
    ("But its algorithm implementation and object-oriented analysis", HDR, GRAY),
    ("are excellent — that's the part I lean on.", HDR, RED)])
def c_approach(): return heading("How the 100 rules run a build", [
    "Object-oriented first: turn my mess of thoughts into a clean design",
    "Freeze the API",
    "Then ungate three agents in parallel: front end, back end, and tests — 100% coverage"])
def c_recap(): return centered([
    ("So: the rule of 90, and the three C's.", H1, WHITE),
    ("Algorithms  ·  C programmer  ·  Claude", HDR, RED)])
def c_team1(): return visual_card([("The crew", H1, WHITE)], v_orgchart)
def c_team2(): return centered([
    ("Brutus — the tester.", H1, WHITE),
    ("Python, 100% coverage. Runs on the basement gaming PC (RTX 5080, 16GB) —", HDR, GRAY),
    ("too small for big models, but blazing on small ones and the whole test suite.", HDR, GRAY)])
def c_team3(): return centered([
    ("Linda — research.", H1, WHITE),
    ("wired to Groq's GPT-OSS-120B via opencode wrappers Claude wrote.", HDR, GRAY),
    ("Searches wide and fast — ingest a lot, process it quickly.", HDR, RED)])
def c_plan(): return centered([
    ("Keeping this to about ten minutes —", H1, WHITE),
    ("one more, and it's a funny one.", HDR, GRAY)])
def c_mace(): return visual_card([
    ("A small-world puzzle", H1, WHITE),
    ("my USNA Class-of-'90 crest — behind Rep. Nancy Mace (The Citadel)", HDR, RED)], v_crest)
def c_bonus(): return centered([
    ("Bonus points in the comments:", H1, WHITE),
    ("tell me why our Class-of-'90 crest is on her wall. 990 of us are puzzled.", HDR, GRAY),
    ("No politics — just a technology podcast.", HDR, RED)])
def c_teaser(): return centered([
    ("Coming up:", H1, WHITE),
    ("real architecture examples, and learning to do GUIs properly.", HDR, GRAY),
    ("Claude taught me GUIs; I taught him good coding. Talk tomorrow.", HDR, RED)])

BEATS = [
    (0.0, c_title), (30.42, c_ninety), (45.86, c_powell), (61.90, c_rule90),
    (101.05, c_rule90_applied), (132.56, c_smallmodel), (179.58, c_letterC),
    (189.70, c_c1), (227.11, c_thinkers), (249.52, c_c2), (274.42, c_jason),
    (317.52, c_c3), (353.50, c_claude_caveat), (364.52, c_approach),
    (412.72, c_recap), (425.27, c_team1), (438.69, c_team2), (473.82, c_team3),
    (533.14, c_plan), (542.00, c_mace), (597.71, c_bonus), (632.18, c_teaser),
]

def audio_dur():
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries",
        "format=duration","-of","default=noprint_wrappers=1:nokey=1", AUDIO], text=True).strip())

def main():
    os.makedirs(FRAMES, exist_ok=True)
    end = audio_dur() if os.path.exists(AUDIO) else BEATS[-1][0] + 30
    durs = []
    for i, (start, fn) in enumerate(BEATS):
        nxt = BEATS[i + 1][0] if i + 1 < len(BEATS) else end
        durs.append(round(nxt - start, 3)); fn().save(os.path.join(FRAMES, f"c{i:02d}.png"))
    print(f"rendered {len(BEATS)} cards (audio={end:.0f}s, LOGO={LOGO_MODE})")
    if "--frames-only" in sys.argv: return
    lst = os.path.join(FRAMES, "concat.txt")
    with open(lst, "w") as fh:
        for i, dr in enumerate(durs): fh.write(f"file 'c{i:02d}.png'\nduration {dr}\n")
        fh.write(f"file 'c{len(durs)-1:02d}.png'\n")
    cmd = ["ffmpeg","-y","-f","concat","-safe","0","-i",lst]
    if os.path.exists(AUDIO):
        cmd += ["-i",AUDIO,"-map","0:v:0","-map","1:a:0","-c:a","aac","-b:a","192k"]
    cmd += ["-c:v","libx264","-r","30","-pix_fmt","yuv420p","-t",f"{end}","-shortest",OUT]
    subprocess.run(cmd, check=True); print(f"\nDone -> {OUT}")

if __name__ == "__main__":
    main()
