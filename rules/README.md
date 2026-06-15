# Drop-in rules kit

[`RULES.md`](RULES.md) in this folder is the 100 rules as a single,
AI-ingestible Markdown file — the same canonical text published at the repo root,
copied here so you can drop the whole `rules/` folder into any project. The rules
are written as **standing instructions for an AI coding agent**: secret hygiene,
config-over-hardcoding, cross-platform discipline, the testing bar, versioning,
and operating a fleet of cheap models as a system.

> `rules/RULES.md` is a **synced copy** of the root `RULES.md`. Edit the root
> file, not this one — a pre-commit hook (`rules/sync.py`) regenerates this copy
> and refuses to commit if the two drift.

---

## Claude Code

Claude Code reads a `CLAUDE.md` at the project root on every session and follows
its `@`-imports. Point it at the rules:

1. Copy the rules file into your project:
   ```sh
   mkdir -p rules
   curl -fsSL \
     https://raw.githubusercontent.com/edhaynes/eds-rules/main/rules/RULES.md \
     -o rules/RULES.md
   ```
2. Add one line to your `CLAUDE.md` (create it if absent):
   ```markdown
   @rules/RULES.md
   ```

That's it — the 100 rules load into context at the start of every Claude Code
session. (You can also paste the file's contents directly into `CLAUDE.md` if you
prefer one file over an import.)

## OpenCode / Codex / Cursor / Aider / others

These harnesses read an `AGENTS.md` (or an equivalent project-rules file)
instead of `CLAUDE.md`. Same idea:

1. Copy `rules/RULES.md` into the project (as above).
2. Reference it from `AGENTS.md`:
   ```markdown
   # Project rules
   See rules/RULES.md — the 100 standing rules. They are non-negotiable defaults;
   if a rule should be broken for a specific change, say so first and get sign-off.
   ```
   If your harness does not support imports, paste the contents of `rules/RULES.md`
   directly into `AGENTS.md`.

## One file, both harnesses (no drift)

If a project uses more than one harness, keep a single source and symlink the
harness entry points to it so they can't drift apart:

```sh
# macOS / Linux
ln -sf rules/RULES.md CLAUDE.md
ln -sf rules/RULES.md AGENTS.md
```

```powershell
# Windows (PowerShell, as admin or with Developer Mode on)
New-Item -ItemType SymbolicLink -Path CLAUDE.md -Target rules\RULES.md
New-Item -ItemType SymbolicLink -Path AGENTS.md -Target rules\RULES.md
```

If symlinks aren't an option on your platform, a one-line `@rules/RULES.md`
import (Claude Code) plus a one-line reference (AGENTS.md) achieves the same
single-source result.

---

## How to use them well

- **Tighten, never loosen.** A project's own `CLAUDE.md`/`AGENTS.md` may add
  stricter rules on top of these, but must not relax them. Number-cite in review:
  "this violates rule 9."
- **Slice the rules to the model (rules 94–96).** A small local model reliably
  holds about one rule per billion parameters. Don't hand an 8B model all 100 —
  give each seat the subset its job needs (the hard rules plus the rules for its
  task), and keep the cheap-tier context bounded. The frontier model can hold the
  whole set.
- **Edit what you disagree with.** These are *opinionated* defaults under
  CC-BY-4.0. Fork the file and make them yours; the numbering is there so reviews
  can reference specific rules.

Canonical source and the full book (*100 Rules for Writing My Software: The Red
Hat Way*): <https://github.com/edhaynes/eds-rules>.
