#!/usr/bin/env bash
# bootstrap-crew.sh — build "Guy's crew": rules-sliced local Ollama models for the
# 3-agent OpenCode setup. The flat 100 is retired; each agent gets its layered
# slice (axioms + role rules) baked into the model's system prompt.
#
#   Jason   → qwen2.5-coder:7b  (PM / coordinator; OpenCode default agent)
#   Claude  → qwen2.5-coder:14b (builder / test-dev; the heavy tool-loop seat)
#   Claudius→ context injection on a frontier model (NO local build; slice in prompt)
#
# Qwen2.5-Coder (not llama3.1:8b) per Linda's OpenCode tool-calling research
# (2026-06-16); num_ctx 16384 baked by make-rules-model.sh.
#
# Usage: ./model/bootstrap-crew.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TAX="${SCRIPT_DIR}/../taxonomy"
SLICES="${TAX}/generated/crew-3/slices"

command -v ollama >/dev/null || { echo "install Ollama first: https://ollama.com" >&2; exit 1; }
command -v python3 >/dev/null || { echo "python3 required" >&2; exit 1; }

echo "==> composing layered slices from the taxonomy"
python3 "${TAX}/compose.py" "${TAX}/rules.yaml" "${TAX}/crew-3.yaml" >/dev/null
echo "    slices in ${SLICES}/"

build() {  # name base
  echo "==> building '${1}' on ${2} (slice + persona + num_ctx 16384)"
  RULES_FILE="${SLICES}/${1}.rules.md" \
  PERSONA_FILE="${SCRIPT_DIR}/personas/${1}.txt" \
  MODEL_NAME="${1}" BASE_MODEL="${2}" \
  "${SCRIPT_DIR}/make-rules-model.sh" 2>&1 | grep -vE '\[\?(25|2026)' | grep -E 'creating|smoke|Done|rule|—' || true
}

build jason  qwen2.5-coder:7b
build claude  qwen2.5-coder:14b

cat <<EOF

==> Claudius — context injection (no local model)
    Frontier model + his slice in the agent prompt: ${SLICES}/claudius.rules.md

Crew built. Local models: $(ollama list | grep -E '^(jason|claude)\b' | awk '{print $1}' | tr '\n' ' ')
Wire OpenCode per-project: see model/opencode/opencode.json (Jason = default agent).
EOF
