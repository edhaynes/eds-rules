#!/usr/bin/env bash
# run-bench.sh — run one A/B side headless in its sandbox, with precise wall-clock
# timing and token capture. Bench metadata is written OUTSIDE the repo (host
# ~/test_projects/bench/) so it never pollutes the build artifacts.
#
#   run-bench.sh control     # ruleless Claude Code; clean token report via --output-format json
#   run-bench.sh guy         # OpenCode crew (token capture is best-effort for local models)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:?usage: run-bench.sh control|guycc|guy}"
TS="$(python3 -c 'import datetime;print(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))')"
OUT="$HOME/test_projects/bench/${MODE}-${TS}"; mkdir -p "$OUT"

stamp() { python3 -c 'import datetime,time;n=datetime.datetime.now(datetime.timezone.utc);print(n.isoformat(), repr(time.time()))'; }

JASON_MODEL=""   # set for the cloud "Jason coordinator" candidate arms (native Anthropic API)
case "$MODE" in
  control) REPO="$HOME/test_projects/claude" ;;       # ruleless Claude Code + frontier Anthropic
  guycc)   REPO="$HOME/test_projects/claude_guy" ;;    # apples-to-apples: Claude Code harness + guy's local model
  guy)     REPO="$HOME/test_projects/test_guy" ;;      # OpenCode crew + guy's local models
  haiku)   REPO="$HOME/test_projects/claude_haiku";  JASON_MODEL="claude-haiku-4-5"  ;;  # Jason candidate: fast/cheap coordinator
  sonnet)  REPO="$HOME/test_projects/claude_sonnet"; JASON_MODEL="claude-sonnet-4-6" ;;  # Jason candidate: reasoning coordinator
  *) echo "usage: run-bench.sh control|guycc|guy|haiku|sonnet" >&2; exit 1 ;;
esac
PROMPT="$(cat "$REPO/PROMPT.txt")"

read -r START_ISO START_EPOCH <<<"$(stamp)"
echo "[$START_ISO] starting $MODE run -> $OUT"

# run as the host user (not container-root): lets the agent use skip-permissions
# AND own the mounted repo (rootless podman uid-mapping).
UID_MAP=(--userns=keep-id --user "$(id -u):$(id -g)")
if [ "$MODE" = control ]; then
  : "${ANTHROPIC_API_KEY:?set ANTHROPIC_API_KEY}"
  podman run --rm "${UID_MAP[@]}" -v "$REPO:/work:Z" -e ANTHROPIC_API_KEY eds-sandbox-control \
    -p "$PROMPT" --dangerously-skip-permissions --output-format json \
    > "$OUT/result.json" 2> "$OUT/stderr.log" || echo "(claude exited non-zero — see stderr.log)"
elif [ -n "$JASON_MODEL" ]; then
  # Jason-coordinator candidate: same ruleless Claude Code harness + native Anthropic
  # API, pinned to a specific cloud model. Only the model differs from control.
  : "${ANTHROPIC_API_KEY:?set ANTHROPIC_API_KEY}"
  podman run --rm "${UID_MAP[@]}" -v "$REPO:/work:Z" -e ANTHROPIC_API_KEY \
    -e ANTHROPIC_MODEL="$JASON_MODEL" \
    -e ANTHROPIC_SMALL_FAST_MODEL="$JASON_MODEL" \
    eds-sandbox-control \
    -p "$PROMPT" --dangerously-skip-permissions --output-format json \
    > "$OUT/result.json" 2> "$OUT/stderr.log" || echo "(claude/$MODE exited non-zero — see stderr.log)"
elif [ "$MODE" = guycc ]; then
  # Same ruleless Claude Code harness as control, but pointed at guy's local model
  # (claude:guy1.0) via the host LiteLLM Anthropic endpoint. Only the model differs
  # from control — the harness, sandbox, task, and rubric are identical.
  : "${LITELLM_MASTER_KEY:?set LITELLM_MASTER_KEY}"
  podman run --rm "${UID_MAP[@]}" -v "$REPO:/work:Z" \
    -e ANTHROPIC_BASE_URL=http://host.containers.internal:4000 \
    -e ANTHROPIC_AUTH_TOKEN="$LITELLM_MASTER_KEY" \
    -e ANTHROPIC_MODEL=claude-guy \
    -e ANTHROPIC_SMALL_FAST_MODEL=claude-guy \
    -e MAX_THINKING_TOKENS=0 \
    -e CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    eds-sandbox-control \
    -p "$PROMPT" --dangerously-skip-permissions --output-format json \
    > "$OUT/result.json" 2> "$OUT/stderr.log" || echo "(claude+guy exited non-zero — see stderr.log)"
else
  mkdir -p "$OUT/ochome"   # persist OpenCode session data on the host for token capture
  podman run --rm "${UID_MAP[@]}" -v "$REPO:/work:Z" -v "$OUT/ochome:/sandbox-home:Z" \
    -e LITELLM_MASTER_KEY eds-sandbox-guy \
    run --agent jason "$PROMPT" > "$OUT/result.txt" 2> "$OUT/stderr.log" || echo "(opencode exited non-zero)"
fi

read -r END_ISO END_EPOCH <<<"$(stamp)"
WALL="$(python3 -c "print(round(${END_EPOCH}-${START_EPOCH},3))")"

# pull tokens/duration/cost from claude's JSON if present
python3 - "$OUT" "$START_ISO" "$END_ISO" "$WALL" "$MODE" <<'PY'
import json, os, sys
out, start, end, wall, mode = sys.argv[1:6]
m = {"mode": mode, "start_utc": start, "end_utc": end, "wall_seconds": float(wall)}
rj = os.path.join(out, "result.json")
if os.path.exists(rj):
    try:
        d = json.load(open(rj))
        u = d.get("usage", {})
        m.update({
            "claude_duration_ms": d.get("duration_ms"),
            "claude_api_ms": d.get("duration_api_ms"),
            "num_turns": d.get("num_turns"),
            "total_cost_usd": d.get("total_cost_usd"),
            "input_tokens": u.get("input_tokens"),
            "output_tokens": u.get("output_tokens"),
            "cache_read_input_tokens": u.get("cache_read_input_tokens"),
            "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
            "is_error": d.get("is_error"),
        })
    except Exception as e:
        m["parse_error"] = str(e)
json.dump(m, open(os.path.join(out, "metrics.json"), "w"), indent=2)
print(json.dumps(m, indent=2))
PY
echo "[$END_ISO] done in ${WALL}s — metrics: $OUT/metrics.json"
