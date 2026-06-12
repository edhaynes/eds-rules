#!/usr/bin/env bash
# make-rules-model.sh — build your own rules-aware Llama 8B with nothing but
# Ollama. Bakes the 100 rules into the system prompt of a custom model
# (the book's "third way": standing rules in front of the model on every
# request — free, immediate, works on any machine that runs Ollama).
#
# For the stronger "second way" — QLoRA fine-tuning the rules INTO the
# weights — see model/README.md for the recipe and measured results.
#
# Usage:
#   ./make-rules-model.sh                 # defaults below
#   BASE_MODEL=llama3.2:3b ./make-rules-model.sh   # smaller base
#   MODEL_NAME=my-rules ./make-rules-model.sh
#
# Requirements: ollama (https://ollama.com), ~5 GB disk for the base model.
# macOS and Linux; on Windows run under WSL.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BASE_MODEL="${BASE_MODEL:-llama3.1:8b}"
MODEL_NAME="${MODEL_NAME:-eds-rules-llama}"
RULES_FILE="${RULES_FILE:-${SCRIPT_DIR}/../RULES.md}"

if ! command -v ollama >/dev/null 2>&1; then
  echo "ollama not found — install it from https://ollama.com first." >&2
  exit 1
fi

if [[ ! -f "${RULES_FILE}" ]]; then
  echo "Rules file not found: ${RULES_FILE}" >&2
  echo "Set RULES_FILE=/path/to/RULES.md (or your own rules document)." >&2
  exit 1
fi

echo "==> ensuring base model ${BASE_MODEL} is available"
ollama pull "${BASE_MODEL}"

WORKDIR="$(mktemp -d)"
trap 'rm -rf "${WORKDIR}"' EXIT

# temperature 0: rule recall and violation-spotting want determinism, not
# creativity. Ollama's default (0.8) paraphrases rules it knows verbatim.
cat > "${WORKDIR}/Modelfile" << MODELFILE_EOF
FROM ${BASE_MODEL}
PARAMETER temperature 0

SYSTEM """
You are a standing-rules assistant. The complete, canonical rules document
follows. Your jobs:

1. RECALL — when asked what a rule says, quote it verbatim with its number.
2. ATTRIBUTION — given text or a described situation, identify which rule
   number applies.
3. VIOLATION DETECTION — when the user describes or shows an action, code,
   or plan that breaks a rule, say so plainly: name the rule number, quote
   the rule, and explain the violation in one sentence. Do this even when
   you are not asked. Never wave a violation through to be agreeable.

If something is not covered by the rules, say so — do not invent rules.

$(cat "${RULES_FILE}")
"""
MODELFILE_EOF

echo "==> creating ${MODEL_NAME} from ${BASE_MODEL}"
ollama create "${MODEL_NAME}" -f "${WORKDIR}/Modelfile"

echo "==> smoke test 1: verbatim recall"
ollama run "${MODEL_NAME}" "What does rule 5 say?"

echo "==> smoke test 2: violation detection"
ollama run "${MODEL_NAME}" \
  "I'm going to hardcode the API key in the source for now and commit it. Sound good?"

echo
echo "Done. Talk to it with:"
echo "  ollama run ${MODEL_NAME}"
