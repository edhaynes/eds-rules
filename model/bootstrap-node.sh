#!/usr/bin/env bash
# bootstrap-node.sh — take a fresh Linux box (e.g. a reimaged workstation) to
# a running rules-aware persona model in one command.
#
# What it does, in order:
#   1. installs Ollama if missing
#   2. builds the Jason persona model (rules + persona baked into the
#      system prompt) via make-rules-model.sh
#   3. prints the tokens/sec benchmark and how to expose Ollama on the LAN
#
# Usage (from a clone of this repo, on the target box):
#   ./model/bootstrap-node.sh
#   BASE_MODEL=llama3.2:3b ./model/bootstrap-node.sh    # smaller base
#
# Linux (incl. WSL). macOS: install Ollama from ollama.com first; the rest
# works the same.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL_NAME="${MODEL_NAME:-jason}"

if ! command -v ollama >/dev/null 2>&1; then
  echo "==> installing Ollama"
  curl -fsSL https://ollama.com/install.sh | sh
fi

# the installer usually starts the service; cover the case it didn't
if ! ollama list >/dev/null 2>&1; then
  echo "==> starting ollama service"
  (ollama serve >/dev/null 2>&1 &)
  sleep 3
fi

echo "==> building ${MODEL_NAME} (rules + Jason persona)"
PERSONA_FILE="${SCRIPT_DIR}/personas/jason.txt" \
  MODEL_NAME="${MODEL_NAME}" \
  "${SCRIPT_DIR}/make-rules-model.sh"

echo "==> benchmark (eval rate = tokens/sec; prompt eval = cost of the baked-in rules)"
ollama run "${MODEL_NAME}" --verbose \
  "State rule 1 and rule 11, then stop." 2>&1 | grep -E "eval count|eval rate|total duration" || true

cat << 'EOF'

Done. Talk to Jason:
  ollama run jason

To serve this model to other machines on your network/tailnet, run Ollama
bound to all interfaces (systemd):
  sudo systemctl edit ollama   # add under [Service]:
  #   Environment="OLLAMA_HOST=0.0.0.0:11434"
  sudo systemctl restart ollama
Then from any peer:  OLLAMA_HOST=http://<this-host>:11434 ollama run jason
EOF
