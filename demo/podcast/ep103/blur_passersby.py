#!/usr/bin/env python3
"""Cover passersby faces with original critters; leave the host (Eddie) untouched.

Pipeline:
  1. YOLO-track every person across the clip (stable track IDs).
  2. Per frame, the HOST is the largest box whose height >= HOST_MIN_H * frame_h
     (the close-up subject). Determined per-frame so a tracker ID-switch on the
     host doesn't accidentally uncover/cover him.
  3. Every OTHER tracked person gets a creature PNG (assigned by track_id, so a
     given passerby keeps the same critter), scaled to their box and placed over
     the head, alpha-composited.
  4. Write a video-only mp4; audio is muxed back in by the assemble step.

Host detection is geometric (size/position), not identity — robust for a single
close-mic host with distant background foot-traffic.

Usage: blur_passersby.py <source.mov> <out.mp4> [--cap SECONDS] [--device mps|cpu]
"""
from __future__ import annotations
import argparse
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO

HERE = Path(__file__).resolve().parent
CREATURES_DIR = HERE / "assets" / "creatures"
CREATURE_FILES = ["creature_1_owl.png", "creature_2_moose.png",
                  "creature_3_frog.png", "creature_4_rabbit.png"]

HOST_MIN_H = 0.45      # a box taller than this fraction of frame height can be host
MIN_PERSON_AREA = 600  # ignore detection noise smaller than this (px^2)
HEAD_SCALE = 1.35      # creature width as a multiple of person-box width
HEAD_Y = 0.10          # head-center as a fraction of box height down from the top
CONF = 0.40         # a touch stricter than default to suppress non-person noise


def load_creatures():
    out = []
    for f in CREATURE_FILES:
        img = cv2.imread(str(CREATURES_DIR / f), cv2.IMREAD_UNCHANGED)
        if img is None or img.shape[2] != 4:
            raise SystemExit(f"creature missing/needs alpha: {f}")
        out.append(img)
    return out


def overlay_rgba(frame, png, cx, cy, target_w):
    """Alpha-composite png centered at (cx, cy), scaled to target_w, clipped to frame."""
    h0, w0 = png.shape[:2]
    tw = max(8, int(target_w))
    th = max(8, int(tw * h0 / w0))
    rs = cv2.resize(png, (tw, th), interpolation=cv2.INTER_AREA)
    x0, y0 = int(cx - tw / 2), int(cy - th / 2)
    fx0, fy0 = max(0, x0), max(0, y0)
    fx1, fy1 = min(frame.shape[1], x0 + tw), min(frame.shape[0], y0 + th)
    if fx1 <= fx0 or fy1 <= fy0:
        return
    crop = rs[fy0 - y0:fy1 - y0, fx0 - x0:fx1 - x0]
    alpha = crop[:, :, 3:4].astype(np.float32) / 255.0
    roi = frame[fy0:fy1, fx0:fx1]
    roi[:] = (crop[:, :, :3].astype(np.float32) * alpha +
              roi.astype(np.float32) * (1 - alpha)).astype(np.uint8)


def run(source, out, cap=None, device="mps"):
    creatures = load_creatures()
    cv = cv2.VideoCapture(str(source))
    fps = cv.get(cv2.CAP_PROP_FPS) or 30.0
    W = int(cv.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(cv.get(cv2.CAP_PROP_FRAME_HEIGHT))
    max_frames = int(cap * fps) if cap else None

    model = YOLO("yolo11n.pt")
    writer = cv2.VideoWriter(str(out), cv2.VideoWriter_fourcc(*"mp4v"), fps, (W, H))

    n, covered = 0, 0
    for res in model.track(source=str(source), classes=[0], conf=CONF, persist=True,
                           stream=True, tracker="bytetrack.yaml", device=device,
                           verbose=False):
        if max_frames and n >= max_frames:
            break
        frame = res.orig_img.copy()
        boxes = []
        for b in res.boxes:
            x1, y1, x2, y2 = b.xyxy[0].tolist()
            area = (x2 - x1) * (y2 - y1)
            if area < MIN_PERSON_AREA:
                continue
            tid = int(b.id[0]) if b.id is not None else -1
            boxes.append((area, x1, y1, x2, y2, tid))

        # host = largest box tall enough to be the close-up subject
        host = None
        for box in sorted(boxes, key=lambda z: -z[0]):
            if (box[4] - box[2]) >= HOST_MIN_H * H:
                host = box
                break

        for area, x1, y1, x2, y2, tid in boxes:
            if host is not None and (area, x1, y1, x2, y2, tid) == host:
                continue
            bw = x2 - x1
            cx = (x1 + x2) / 2
            cy = y1 + HEAD_Y * (y2 - y1)
            png = creatures[tid % len(creatures)] if tid >= 0 else creatures[0]
            overlay_rgba(frame, png, cx, cy, bw * HEAD_SCALE)
            covered += 1

        writer.write(frame)
        n += 1
        if n % 300 == 0:
            print(f"  {n} frames, {covered} creature-overlays so far")

    cv.release()
    writer.release()
    print(f"wrote {out}  ({n} frames @ {fps:.0f}fps, {covered} total overlays)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("out")
    ap.add_argument("--cap", type=float, default=None, help="only process first N seconds")
    ap.add_argument("--device", default="mps")
    a = ap.parse_args()
    run(a.source, a.out, a.cap, a.device)
