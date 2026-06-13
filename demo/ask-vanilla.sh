#!/usr/bin/env bash
# ask-vanilla.sh — query a RULES-FREE model with a prompt, for the demo's
# "with rules vs. without" comparison. Two backends:
#
#   BACKEND=llama   (default) — vanilla llama3.1:8b via Ollama. The rigorous
#                    one-variable comparison: same weights as eds-rules-llama,
#                    no rules system prompt. Works offline, no key.
#   BACKEND=claude  — true vanilla Claude via the Anthropic API, empty system
#                    prompt. Reads ANTHROPIC_API_KEY from the environment;
#                    never prints it, never hardcodes it.
#
# Usage:
#   ./ask-vanilla.sh "What does rule 2 say?"
#   BACKEND=claude ./ask-vanilla.sh "What does rule 2 say?"
#
# Requirements: ollama (llama backend) OR curl + a valid ANTHROPIC_API_KEY
# (claude backend). macOS and Linux.

set -euo pipefail

PROMPT="${1:-}"
if [[ -z "${PROMPT}" ]]; then
  echo "usage: $0 \"<prompt>\"" >&2
  exit 1
fi

BACKEND="${BACKEND:-llama}"
VANILLA_MODEL="${VANILLA_MODEL:-llama3.1:8b}"
CLAUDE_MODEL="${CLAUDE_MODEL:-claude-sonnet-4-6}"

case "${BACKEND}" in
  llama)
    command -v ollama >/dev/null 2>&1 || { echo "ollama not found." >&2; exit 1; }
    exec ollama run "${VANILLA_MODEL}" "${PROMPT}"
    ;;
  claude)
    command -v curl >/dev/null 2>&1 || { echo "curl not found." >&2; exit 1; }
    : "${ANTHROPIC_API_KEY:?ANTHROPIC_API_KEY is not set — export it (it is read from the env, never hardcoded).}"
    # Empty system prompt = rules-free Claude. Body built with python3 for safe JSON.
    body="$(PROMPT="${PROMPT}" CLAUDE_MODEL="${CLAUDE_MODEL}" python3 -c '
import json, os
print(json.dumps({
    "model": os.environ["CLAUDE_MODEL"],
    "max_tokens": 400,
    "system": "",
    "messages": [{"role": "user", "content": os.environ["PROMPT"]}],
}))')"
    curl -s https://api.anthropic.com/v1/messages \
      -H "x-api-key: ${ANTHROPIC_API_KEY}" \
      -H "anthropic-version: 2023-06-01" \
      -H "content-type: application/json" \
      -d "${body}" \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["content"][0]["text"] if "content" in d else json.dumps(d, indent=2))'
    ;;
  *)
    echo "unknown BACKEND=${BACKEND} (use 'llama' or 'claude')" >&2
    exit 1
    ;;
esac
