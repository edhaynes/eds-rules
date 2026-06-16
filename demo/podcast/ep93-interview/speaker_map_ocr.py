#!/usr/bin/env python3
"""Map the speaker-view timeline into Ed vs Guy segments via caption OCR.

Ground truth = the Meet name caption (bottom-left): "Ed Haynes" / "Guy Turgeon".
We sample at 1 fps, OCR the binarized caption crop, classify, median-smooth, and
emit merged [start, end, "ed"|"guy"] segments.

Usage: speaker_map_ocr.py <source.mp4> <out.json>
Requires: ffmpeg, numpy, Pillow, pytesseract + tesseract.
"""
import json, subprocess, sys
import numpy as np
from PIL import Image
import pytesseract

src, out = sys.argv[1], sys.argv[2]
FPS = 3.0                          # 0.33s resolution — captures real fast switches
CW, CH, SC = 460, 56, 3            # caption crop (bottom-left) then upscale x3
MIN_SEG = 0.4                      # merge sub-0.4s flicker only

proc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", src, "-vf",
     f"fps={FPS},crop={CW}:{CH}:0:ih-{CH},scale=iw*{SC}:ih*{SC},format=gray",
     "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
W, H = CW * SC, CH * SC
fb = W * H


def classify(text):
    t = text.lower()
    if "guy" in t or "turg" in t:
        return "guy"
    if "haynes" in t or "ed " in t or t.strip() == "ed":
        return "ed"
    return None


raw_labels = []
while True:
    raw = proc.stdout.read(fb)
    if len(raw) < fb:
        break
    g = np.frombuffer(raw, np.uint8).reshape(H, W)
    # isolate bright caption text -> black text on white for tesseract
    bw = np.where(g > 175, 0, 255).astype(np.uint8)
    txt = pytesseract.image_to_string(Image.fromarray(bw), config="--psm 7")
    raw_labels.append(classify(txt))
proc.wait()

# carry-forward unknowns
lab = []
last = "ed"
for x in raw_labels:
    if x is None:
        x = last
    last = x
    lab.append(1 if x == "ed" else 0)
lab = np.array(lab)

# despeckle: flip only isolated single samples (OCR noise), keep real switches
sm = lab.copy()
for i in range(1, len(sm) - 1):
    if sm[i] != sm[i - 1] and sm[i] != sm[i + 1]:
        sm[i] = sm[i - 1]

segs = []
cur, start = sm[0], 0
for i in range(1, len(sm)):
    if sm[i] != cur:
        segs.append([start / FPS, i / FPS, "ed" if cur else "guy"])
        cur, start = sm[i], i
segs.append([start / FPS, len(sm) / FPS, "ed" if cur else "guy"])

merged = []
for s in segs:
    if merged and (s[1] - s[0]) < MIN_SEG:
        merged[-1][1] = s[1]
    elif merged and merged[-1][2] == s[2]:
        merged[-1][1] = s[1]
    else:
        merged.append(s)
coalesced = []
for s in merged:
    if coalesced and coalesced[-1][2] == s[2]:
        coalesced[-1][1] = s[1]
    else:
        coalesced.append(s)

ed = sum(s[1] - s[0] for s in coalesced if s[2] == "ed")
guy = sum(s[1] - s[0] for s in coalesced if s[2] == "guy")
json.dump({"segments": [[round(a, 2), round(b, 2), c] for a, b, c in coalesced]},
          open(out, "w"), indent=0)
print(f"done {out}  {len(coalesced)} segments  ed={ed:.0f}s guy={guy:.0f}s")
