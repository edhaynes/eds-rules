# Sandbox A/B — process & inference topology

Two independent, equally-isolated Podman containers run in parallel. Same shape
(UBI9 + Node, fresh HOME with no host rules, only the one repo mounted, launched
as the host user via `--userns=keep-id`). The ONLY difference is the brain:
the **control** thinks with a frontier model and **no rules**; the **guy** crew
thinks with local rules-sliced models.

```
                                  macOS host (Apple silicon)
┌──────────────────────────────────────────────────────────────────────────────────┐
│                                                                                    │
│   ./run-bench.sh control                         ./run-bench.sh guy                │
│         │ podman run                                   │ podman run               │
│         │ --userns=keep-id --user $(id -u)             │ --userns=keep-id …        │
│         │ -e ANTHROPIC_API_KEY                          │ -e LITELLM_MASTER_KEY    │
│ ────────┼───────────────────────────────────────────────┼──────────  Podman VM ───│
│         ▼                                               ▼          (libkrun)       │
│  ╔════════════════════════╗                      ╔════════════════════════╗       │
│  ║  CONTROL  sandbox      ║                      ║  GUY  sandbox          ║       │
│  ║  UBI9 + node20         ║                      ║  UBI9 + node20         ║       │
│  ║  HOME=/sandbox-home    ║  ← no CLAUDE.md,     ║  HOME=/sandbox-home    ║       │
│  ║  /work = claude/       ║    no shared-rules   ║  /work = test_guy/     ║       │
│  ║                        ║  ← only this repo    ║                        ║       │
│  ║   claude -p  (RULELESS)║    mounted           ║   opencode run         ║       │
│  ║        │               ║                      ║    ├─ jason   (default)║       │
│  ╚════════│═══════════════╝                      ║    ├─ claude  (sub)    ║       │
│           │                                      ║    └─ claudius (sub)   ║       │
│           │                                      ╚═════│════════│════════╝       │
│           │ HTTPS                                      │        │  host.containers │
│           ▼                                            │        │   .internal       │
│     ☁  Anthropic API                                   ▼        ▼                  │
│        (frontier, no rules)                  Ollama :11434    LiteLLM :4000        │
│                                              jason:guy1.0     gpt-oss-120b ─► Groq │
│                                              claude:guy1.0    (Claudius frontier)  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

## Reading it
- **Two parallel containers**, never touching each other or the host filesystem
  beyond their one mounted repo. Each runs as *you* (uid mapped) so it can write
  its repo and use `--dangerously-skip-permissions` safely (the container is the jail).
- **Control brain** = Anthropic's cloud frontier model, started with zero rules
  (clean HOME → no `~/.claude/CLAUDE.md`). Tokens/duration captured from
  `claude --output-format json` → `bench/control-*/metrics.json`.
- **Guy brain** = local, on the host: Jason (default) + Claude on Ollama
  (`*:guy1.0`, rules baked in), Claudius on the host LiteLLM proxy → Groq. The
  container reaches all host services at `host.containers.internal`.
- **Inference always leaves the container** — control to the cloud, guy to host
  Ollama/LiteLLM. The container is just the isolated harness + workspace.

Same prompt (`PROMPT.txt`), same task (`ASSIGNMENT.md`), same rubric — so the
result delta is attributable to *rules + crew vs none*, nothing else.
