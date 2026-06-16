#!/usr/bin/env python3
"""Background blur via Robust Video Matting (RVM), GPU, on Gladius.

Keeps the foreground person exactly as shot and gaussian-blurs only the
background, using RVM's alpha matte:  out = a*src + (1-a)*blur(src).
Streams frames through ffmpeg pipes (no temp PNGs); copies source audio.

Usage:  rvm_blur.py <in.mp4> <out.mp4> [kernel] [sigma] [downsample_ratio]
Runs on the ComfyUI venv (torch+cu130, GB10). RVM repo + weights under
/srv/models/ep93/. RVM is GPL-3.0; used here as an offline tool, not shipped.
"""
import sys, json, subprocess
import numpy as np
import torch
from torchvision.transforms.functional import gaussian_blur

RVM_DIR = "/srv/models/ep93/RobustVideoMatting"
WEIGHTS = "/srv/models/ep93/rvm_mobilenetv3.pth"
sys.path.insert(0, RVM_DIR)
from model import MattingNetwork  # noqa: E402

inp, outp = sys.argv[1], sys.argv[2]
KERNEL = int(sys.argv[3]) if len(sys.argv) > 3 else 61
SIGMA = float(sys.argv[4]) if len(sys.argv) > 4 else 16.0
DS = float(sys.argv[5]) if len(sys.argv) > 5 else 0.25

st = json.loads(subprocess.check_output([
    "ffprobe", "-v", "error", "-select_streams", "v:0",
    "-show_entries", "stream=width,height,r_frame_rate", "-of", "json", inp,
]))["streams"][0]
W, H = st["width"], st["height"]
n, d = st["r_frame_rate"].split("/")
fps = float(n) / float(d)

model = MattingNetwork("mobilenetv3").eval().cuda()
model.load_state_dict(torch.load(WEIGHTS))

dec = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", inp, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
    stdout=subprocess.PIPE)
enc = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
     "-s", f"{W}x{H}", "-r", f"{fps}", "-i", "-", "-i", inp,
     "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-crf", "17",
     "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy", outp],
    stdin=subprocess.PIPE)

fb = W * H * 3
rec = [None] * 4
i = 0
with torch.no_grad():
    while True:
        raw = dec.stdout.read(fb)
        if len(raw) < fb:
            break
        a = np.frombuffer(raw, np.uint8).copy()
        t = torch.from_numpy(a).cuda().float().div(255).view(1, H, W, 3).permute(0, 3, 1, 2)
        fgr, pha, *rec = model(t, *rec, downsample_ratio=DS)
        blurred = gaussian_blur(t, [KERNEL, KERNEL], [SIGMA, SIGMA])
        out = pha * t + (1 - pha) * blurred
        buf = (out.clamp(0, 1) * 255).round().byte().permute(0, 2, 3, 1).contiguous().view(-1).cpu().numpy().tobytes()
        enc.stdin.write(buf)
        i += 1
enc.stdin.close()
enc.wait()
dec.wait()
print(f"done {outp}  ({i} frames {W}x{H}@{fps:.3f})")
