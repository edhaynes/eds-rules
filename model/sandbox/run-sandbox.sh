#!/usr/bin/env bash
# run-sandbox.sh — launch one side of the rules A/B in a UBI/Podman sandbox.
# Both sides are equally isolated (only the test repo mounted, fresh in-container
# HOME with no host rules); the ONLY difference is rules+crew vs none.
#
#   run-sandbox.sh control [args]   # plain Claude Code, ruleless     -> ~/test_projects/claude
#   run-sandbox.sh guy     [args]   # OpenCode + Guy crew (guy1.0)     -> ~/test_projects/test_guy
#
# Inference runs on the HOST: control -> Anthropic API; guy -> host Ollama
# (jason/claude:guy1.0) + host LiteLLM (Claudius) via host.containers.internal.
# Secrets are passed at run time from the host env — never baked into an image.
# The container IS the sandbox, so running the agent with --dangerously-skip-
# permissions inside is safe.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:?usage: run-sandbox.sh control|guy [args...]}"; shift || true

case "$MODE" in
  control)
    : "${ANTHROPIC_API_KEY:?set ANTHROPIC_API_KEY in your env}"
    REPO="$HOME/test_projects/claude"
    podman image exists eds-sandbox-control || \
      podman build -t eds-sandbox-control -f "$HERE/Containerfile.control" "$HERE"
    exec podman run --rm -it -v "$REPO:/work:Z" -e ANTHROPIC_API_KEY \
      eds-sandbox-control "$@"
    ;;
  guy)
    REPO="$HOME/test_projects/test_guy"
    podman image exists eds-sandbox-guy || \
      podman build -t eds-sandbox-guy -f "$HERE/Containerfile.guy" "$HERE"
    # host.containers.internal is provided by podman; LiteLLM key for Claudius's frontier
    exec podman run --rm -it -v "$REPO:/work:Z" -e LITELLM_MASTER_KEY \
      eds-sandbox-guy "$@"
    ;;
  *) echo "usage: run-sandbox.sh control|guy [args...]" >&2; exit 1 ;;
esac
