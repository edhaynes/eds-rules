#!/usr/bin/env bash
# make-demo-video.sh — turn a screen recording into a narrated teaser MP4.
# Generates the voiceover from demo/narration.txt via ElevenLabs, then muxes
# it onto your recording with ffmpeg.
#
# Usage:
#   ./make-demo-video.sh path/to/recording.mov
#   VOICE_ID=<id> ./make-demo-video.sh recording.mov
#   ./make-demo-video.sh --list-voices         # print available voices + IDs
#
# Config (env, all optional except the key):
#   ELEVENLABS_API_KEY   required — read from env, never hardcoded
#   VOICE_ID             ElevenLabs voice id (default: a documented stock voice)
#   TTS_MODEL            ElevenLabs model (default: eleven_multilingual_v2)
#   NARRATION_FILE       default: demo/narration.txt
#   OUT                  default: demo/eds-rules-teaser.mp4
#
# Requirements: curl, ffmpeg (both already present on this machine). macOS/Linux.
# Dependency note (rules §0.4): ElevenLabs is a cloud TTS API (proprietary,
# pay-per-use); no local install or ARM concern. ffmpeg is LGPL/GPL, native ARM.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Key var name varies; accept the common spellings (Eddie's is ELEVEN_API_KEY).
ELEVENLABS_API_KEY="${ELEVENLABS_API_KEY:-${ELEVEN_API_KEY:-${XI_API_KEY:-}}}"
AUDIO="${AUDIO:-}"   # pre-recorded voice track (e.g. Eddie's memo). When set,
                     # use it verbatim and skip ElevenLabs entirely — no key needed.
VOICE_ID="${VOICE_ID:-pNInz6obpgDQGcFmaJgB}"   # stock "Adam" — override to taste
TTS_MODEL="${TTS_MODEL:-eleven_multilingual_v2}"
NARRATION_FILE="${NARRATION_FILE:-${SCRIPT_DIR}/narration.txt}"
OUT="${OUT:-${SCRIPT_DIR}/eds-rules-teaser.mp4}"

command -v curl   >/dev/null 2>&1 || { echo "curl not found."   >&2; exit 1; }
command -v ffmpeg >/dev/null 2>&1 || { echo "ffmpeg not found." >&2; exit 1; }

# --list-voices: fetch the account's voices so you can pick a VOICE_ID.
if [[ "${1:-}" == "--list-voices" ]]; then
  curl -s -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
    https://api.elevenlabs.io/v1/voices \
  | python3 -c 'import json,sys; [print(f"{v[\"voice_id\"]}  {v[\"name\"]}") for v in json.load(sys.stdin).get("voices",[])]'
  exit 0
fi

RECORDING="${1:-}"
if [[ -z "${RECORDING}" || ! -f "${RECORDING}" ]]; then
  echo "usage: $0 <recording.mov|.mp4>   (or --list-voices)" >&2
  exit 1
fi
[[ -f "${NARRATION_FILE}" ]] || { echo "narration not found: ${NARRATION_FILE}" >&2; exit 1; }

WORKDIR="$(mktemp -d)"
trap 'rm -rf "${WORKDIR}"' EXIT
VO="${WORKDIR}/vo.mp3"

if [[ -n "${AUDIO}" ]]; then
  # Use the supplied voice track (Eddie's memo wins the bake-off, 2026-06-13).
  [[ -f "${AUDIO}" ]] || { echo "AUDIO file not found: ${AUDIO}" >&2; exit 1; }
  echo "==> using supplied voice track: $(basename "${AUDIO}") (ElevenLabs skipped)"
  VO="${AUDIO}"
else
  : "${ELEVENLABS_API_KEY:?No ElevenLabs key — export ELEVEN_API_KEY (or ELEVENLABS_API_KEY/XI_API_KEY), or pass AUDIO=<file>. Read from env, never hardcoded.}"
  echo "==> generating voiceover from $(basename "${NARRATION_FILE}") via ElevenLabs (${TTS_MODEL})"
  TEXT="$(cat "${NARRATION_FILE}")"
  req_body="$(TEXT="${TEXT}" TTS_MODEL="${TTS_MODEL}" python3 -c '
import json, os
print(json.dumps({
    "text": os.environ["TEXT"],
    "model_id": os.environ["TTS_MODEL"],
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
}))')"
  http_code="$(curl -s -w '%{http_code}' -o "${VO}" \
    -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
    -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
    -H "content-type: application/json" \
    -d "${req_body}")"
  if [[ "${http_code}" != "200" ]]; then
    echo "ElevenLabs returned HTTP ${http_code}:" >&2
    cat "${VO}" >&2 2>/dev/null || true
    exit 1
  fi
fi

echo "==> muxing voiceover onto $(basename "${RECORDING}") -> $(basename "${OUT}")"
# Replace the recording's audio with the VO. -shortest ends at whichever track
# is shorter; re-encode video to be safe across container/codec combos.
ffmpeg -y -i "${RECORDING}" -i "${VO}" \
  -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k \
  -shortest "${OUT}"

echo
echo "Done -> ${OUT}"
echo "If the VO and the on-screen action drift, re-record to the run-sheet pacing"
echo "or trim the recording; narration timing lives in ${NARRATION_FILE}."
