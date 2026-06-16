#!/usr/bin/env bash
# Proof cut for Ep93: opening card -> RVM-blurred + colour-graded Ed segment
# with the "90% Rule" explainer lower-third flashing in. Validates the full
# look before the 30-min render. Run after rvm_blur produced work/proof_blur.mp4.
set -euo pipefail
cd "$(dirname "$0")"

GRADE="eq=contrast=1.10:brightness=0.04:saturation=1.07:gamma=1.08:gamma_r=0.97:gamma_b=1.05"

ffmpeg -y -hide_banner -loglevel error \
  -loop 1 -t 4 -i assets/opening.png \
  -i work/proof_blur.mp4 \
  -loop 1 -t 10 -i assets/slide_90rule.png \
  -f lavfi -t 4 -i anullsrc=r=48000:cl=stereo \
  -filter_complex "\
[0:v]scale=1920:1080,fps=24,format=yuv420p,setpts=PTS-STARTPTS[op];\
[2:v]fps=24,format=rgba,fade=in:st=3:d=0.4:alpha=1,fade=out:st=8.6:d=0.4:alpha=1[sl];\
[1:v]${GRADE},fps=24,setpts=PTS-STARTPTS[g];\
[g][sl]overlay=enable='between(t,3,9)',format=yuv420p[mn];\
[op][3:a][mn][1:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 work/proof_cut.mp4
echo "wrote work/proof_cut.mp4"
