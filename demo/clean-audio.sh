#!/usr/bin/env bash
# clean-audio.sh — gentle voice cleanup for the episode recordings.
# high-pass (rumble) -> FFT denoise (bed hiss) -> loudness-normalize to -16
# LUFS, then silence the opening lead-in and fade in.
#
# NOTE: the noise gate was removed (2026-06-13, "too aggressive" — it clipped
# speech tails). This is a light touch: bed-noise reduction + consistent gain.
# It does NOT remove door slams over speech, and won't fully kill faint noise
# amplified in long pauses — those are a Descript "Studio Sound" / iZotope RX
# job. For the 100-episode cadence, standardizing the audio pass in Descript
# is the recommendation.
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
loudnorm=I=-16:TP=-1.5:LRA=11,\
volume=enable='lt(t,${LEAD})':volume=0,\
afade=t=in:st=${LEAD}:d=${FADE}" \
-c:a aac -b:a 192k "$OUT"

echo "cleaned -> $OUT"
