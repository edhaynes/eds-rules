# Sandboxed rules A/B

A controlled head-to-head: does the rules-sliced 3-agent local crew (**Guy**) match a
frontier model with **no rules** on the same task? Both sides run in equivalent
UBI/Podman sandboxes — only the test repo is mounted, the in-container HOME is fresh
(no host `~/.claude/CLAUDE.md`, no `shared-rules`), so the control is genuinely
ruleless and the **only** variable is rules+crew vs none.

| | Control | Guy crew |
|---|---|---|
| Repo | `~/test_projects/claude` | `~/test_projects/test_guy` |
| Harness | Claude Code | OpenCode (Jason default, Claude + Claudius subagents) |
| Rules | **none** | layered slices, pinned **guy1.0** |
| Inference | Anthropic API | host Ollama `jason/claude:guy1.0` + host LiteLLM (Claudius) |
| Image | `Containerfile.control` | `Containerfile.guy` |

Same `ASSIGNMENT.md` + `RUBRIC.md` + `rules.json` in both. Task: build a React+Vite
Rules Browser to a 90% MVP.

## Run
```bash
# control (ruleless Claude Code)
ANTHROPIC_API_KEY=… ./run-sandbox.sh control

# guy crew (OpenCode, guy1.0)   — needs Ollama up; for Claudius also `proxy.sh start` (LiteLLM)
./run-sandbox.sh guy
```
Pass agent args after the mode (e.g. `./run-sandbox.sh control --dangerously-skip-permissions`).
The container **is** the sandbox, so skip-permissions is safe here.

## Prereqs
- Podman machine running; host **Ollama** serving `jason:guy1.0` + `claude:guy1.0`
  (built by `model/bootstrap-crew.sh`).
- `ANTHROPIC_API_KEY` in env (control). `LITELLM_MASTER_KEY` + LiteLLM proxy on
  `:4000` (Guy's Claudius only).
- Secrets are passed at run time via `-e`; never baked into images or committed.

## Isolation guarantees (verified)
- Fresh `HOME=/sandbox-home` → no host CLAUDE.md / memory / shared-rules reachable.
- Only the one test repo mounted at `/work`. Inference is on the host; the container
  reaches it at `host.containers.internal`.
