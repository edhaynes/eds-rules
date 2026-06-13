#!/usr/bin/env bash
# clean-audio.sh — dialed-in voice cleanup for the episode recordings.
# high-pass (rumble) -> FFT denoise (bed hiss) -> noise gate (kills pauses so
# normalization can't pump them up) -> loudness-normalize to -16 LUFS, then
# silence the opening lead-in and fade in.
#
# NOTE: this handles steady bed noise + amplified-pause noise. It does NOT
# remove door slams that land *on top of* speech — that's a Descript "Studio
# Sound" / iZotope RX job (see demo/PLAN notes). For the 100-episode cadence,
# standardizing the audio pass in Descript is the recommendation.
#
# Usage: ./clean-audio.sh <in.m4a> <out.m4a> [lead_silence_secs]
set -euo pipefail
IN="${1:?usage: clean-audio.sh <in> <out> [lead_secs]}"
OUT="${2:?usage: clean-audio.sh <in> <out> [lead_secs]}"
LEAD="${3:-2.5}"   # seconds of opening to silence before speech
FADE="1.0"

command -v ffmpeg >/dev/null 2>&1 || { echo "ffmpeg not found." >&2; exit 1; }

ffmpeg -y -i "$IN" -af \
"highpass=f=85,\
afftdn=nr=10:nf=-25:tn=1,\
agate=threshold=0.03:range=0.0015:ratio=9:attack=8:release=250:knee=3,\
loudnorm=I=-16:TP=-1.5:LRA=11,\
volume=enable='lt(t,${LEAD})':volume=0,\
afade=t=in:st=${LEAD}:d=${FADE}" \
-c:a aac -b:a 192k "$OUT"

echo "cleaned -> $OUT"
