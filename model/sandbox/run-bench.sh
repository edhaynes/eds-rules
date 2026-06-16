#!/usr/bin/env bash
# run-bench.sh — run one A/B side headless in its sandbox, with precise wall-clock
# timing and token capture. Bench metadata is written OUTSIDE the repo (host
# ~/test_projects/bench/) so it never pollutes the build artifacts.
#
#   run-bench.sh control     # ruleless Claude Code; clean token report via --output-format json
#   run-bench.sh guy         # OpenCode crew (token capture is best-effort for local models)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:?usage: run-bench.sh control|guy}"
TS="$(python3 -c 'import datetime;print(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))')"
OUT="$HOME/test_projects/bench/${MODE}-${TS}"; mkdir -p "$OUT"

stamp() { python3 -c 'import datetime,time;n=datetime.datetime.now(datetime.timezone.utc);print(n.isoformat(), repr(time.time()))'; }

REPO="$HOME/test_projects/$([ "$MODE" = control ] && echo claude || echo test_guy)"
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
else
  podman run --rm "${UID_MAP[@]}" -v "$REPO:/work:Z" -e LITELLM_MASTER_KEY eds-sandbox-guy \
    run "$PROMPT" > "$OUT/result.txt" 2> "$OUT/stderr.log" || echo "(opencode exited non-zero)"
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
