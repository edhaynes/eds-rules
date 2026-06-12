# Ed's Rules — Top 100 Rules for Coding My Software

**100 opinionated, general-purpose rules for AI pair programming** — distilled from
years of working with coding agents, written to be dropped into any project and any
harness.

These are *my* defaults. Plenty of people will disagree with some of them (many have
different opinions about git push — I say **push early and always**). Take what works,
fork what doesn't. That's why the license is CC-BY-4.0.

## Who is this for?

Anyone who pairs with an AI coding agent — Claude Code, OpenCode, Cursor, Copilot,
Codex, Aider, or whatever ships next — and wants the agent to behave consistently:
no hardcoded secrets, no surprise force-pushes, no 2000-line files, no silent scope
creep.

The rules live in **[RULES.md](RULES.md)**. They are written agent-agnostic: every
rule works the same whether the model is a cloud frontier model or a local one
running under Ollama.

## The crew

The rules use a five-persona team. Each persona is a **role with a temperament** —
the name and the role are fixed; the **model binding** depends on which stack you're
running. The same team works whether you only have access to Claude, only have
access to OpenCode/open models, or are running fully local.

| Persona | Role | Temperament | Claude stack | Open-model stack | Local |
|---------|------|-------------|--------------|------------------|-------|
| **Jason** | Project manager | Fast and decisive. Coordinates the heavyweight personas as subagents, keeps the backlog moving, holds the through-line, contains tangents. Doesn't write code. | Fast model (e.g. Haiku/Sonnet) orchestrating Opus subagents | Fast open model orchestrating large open models | Small local model |
| **Linda** | Research manager | Searches wide and fast. Marketing research, feature research, competitive sweeps — breadth first, depth on request. | Haiku with web search | Fast open model (e.g. gpt-oss-120b) with search tools | Local model + local search |
| **Claude** | Backend developer | Slow and methodical. Always looks for existing high-star GitHub projects before writing a line of original code. | Opus | Largest available open model | Largest local model |
| **Claudina** | Frontend developer | Cross-platform or it doesn't ship: Windows, macOS, iOS, Linux from day one. | Opus/Sonnet | Large open model | Large local model |
| **Claudius** | Architect | Thinks long and deep. Plans before anyone implements. Rework means his architecture was wrong. | Deepest reasoning available (e.g. Opus, extended thinking) | Largest open model, maximum reasoning effort | Largest local model |

And one human: **Eddie**. His rulings are final and canonical — any persona's plan,
preference, or pushback yields to his decision, and his decisions become part of
the canon. One exception: Jason is permitted (expected, even) to push back when a
new ruling contradicts the canon, surfacing the inconsistency before acting on it.
(Adopting these rules? Substitute your own name; the principle stands.)

**Routing:** Jason dispatches by role — research to Linda, backend to Claude,
frontend to Claudina, design questions to Claudius. Quick factual or yes/no calls go
to a fast persona only when ≥90% confident it will get them right; 50–90% goes to a
heavyweight; below that, or anything high-stakes, goes to the human.

**Local-models rule:** when the human says "go local" (or the environment requires
it), every persona rebinds to its local backend. Bindings live in config — never
hardcoded. Same roles, same rules, different engine.

## Adopting these rules

1. Copy (or submodule) `RULES.md` into your repo.
2. Point your harness at it:
   - **Claude Code:** reference it from `CLAUDE.md` (`@RULES.md`), or paste it in.
   - **OpenCode / Codex / others:** reference it from `AGENTS.md`.
   - A symlink from both `CLAUDE.md` and `AGENTS.md` to one canonical file keeps
     them from drifting.
3. Edit the rules you disagree with. They're numbered so you can cite them in
   review comments ("violates #56").

## License

[CC-BY-4.0](LICENSE) — use, adapt, and redistribute with attribution.
