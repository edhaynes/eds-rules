#!/usr/bin/env python3
"""Render summary.tsv (subject<TAB>N<TAB>grade<TAB>ftoks) as a dependency-free
SVG line chart: rule-following grade vs. number of rules in context, one line
per model. Output: graph.svg.
"""
import math, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "summary.tsv")) if l.strip()]
data = collections.OrderedDict()
for subj, N, grade, ftoks in rows:
    data.setdefault(subj, []).append((int(N), float(grade)))
for s in data:
    data[s].sort()

W, H = 1000, 620
L, R, T, B = 90, 240, 70, 80          # margins (R wide for legend)
PW, PH = W - L - R, H - T - B
BG, FG, GRID = "#101010", "#f0f6fc", "#30363d"
COLORS = ["#ee0000", "#58a6ff", "#3fb950", "#d2a84b", "#a371f7"]
NS = [1, 2, 4, 8, 16, 32, 64, 128]

def x(n): return L + (math.log2(n) / 7.0) * PW
def y(g): return T + (1 - g / 100.0) * PH

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
     f'viewBox="0 0 {W} {H}" font-family="Arial,Helvetica,sans-serif">']
s.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
s.append(f'<text x="{L}" y="38" fill="{FG}" font-size="26" font-weight="bold">'
         'Rule-following vs. number of rules in context</text>')
s.append(f'<text x="{L}" y="60" fill="#8b949e" font-size="14">'
         'subject models, rules prompt-baked · judge: GPT-OSS-120B · 10-min full-stack task + polish</text>')
# y grid + labels
for g in range(0, 101, 25):
    yy = y(g)
    s.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{L+PW}" y2="{yy:.1f}" stroke="{GRID}" stroke-width="1"/>')
    s.append(f'<text x="{L-12}" y="{yy+5:.1f}" fill="#8b949e" font-size="13" text-anchor="end">{g}</text>')
s.append(f'<text x="26" y="{T+PH/2:.0f}" fill="{FG}" font-size="15" transform="rotate(-90 26 {T+PH/2:.0f})" text-anchor="middle">grade (0–100)</text>')
# x ticks
for n in NS:
    xx = x(n)
    s.append(f'<line x1="{xx:.1f}" y1="{T+PH}" x2="{xx:.1f}" y2="{T+PH+6}" stroke="#8b949e"/>')
    s.append(f'<text x="{xx:.1f}" y="{T+PH+26}" fill="#8b949e" font-size="13" text-anchor="middle">{n}</text>')
s.append(f'<text x="{L+PW/2:.0f}" y="{H-20}" fill="{FG}" font-size="15" text-anchor="middle">number of rules in the prompt (log scale)</text>')
# lines + points + legend
ly = T + 10
for i, (subj, pts) in enumerate(data.items()):
    c = COLORS[i % len(COLORS)]
    path = " ".join(f"{x(n):.1f},{y(g):.1f}" for n, g in pts)
    s.append(f'<polyline points="{path}" fill="none" stroke="{c}" stroke-width="3"/>')
    for n, g in pts:
        s.append(f'<circle cx="{x(n):.1f}" cy="{y(g):.1f}" r="4.5" fill="{c}"/>')
    s.append(f'<rect x="{L+PW+24}" y="{ly-12}" width="22" height="6" fill="{c}"/>')
    s.append(f'<text x="{L+PW+52}" y="{ly-4}" fill="{FG}" font-size="14">{subj}</text>')
    ly += 28
s.append("</svg>")
open(os.path.join(HERE, "graph.svg"), "w").write("\n".join(s))
print(f"wrote graph.svg  ({len(data)} model(s): {', '.join(data)})")
