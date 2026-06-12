# Back Matter

## Appendix A — Drop-in pre-commit config

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks: [{ id: gitleaks }]
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks: [{ id: detect-secrets, args: ["--baseline", ".secrets.baseline"] }]
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: detect-private-key
      - id: end-of-file-fixer
      - id: trailing-whitespace
  # add language-specific linters/formatters below
```

## Appendix B — Minimum `.gitignore` for secrets

```
.env
.env.*
!.env.example
*.pem
*.key
*.pfx
*.p12
*.crt
id_rsa*
credentials.json
service-account*.json
.aws/
.azure/
.gcp/
*.sqlite
*.db
```

## Appendix C — Adopting the rules per harness

The canonical short form of all one hundred rules lives in the companion
repository (`RULES.md` at github.com/edhaynes/eds-rules, CC-BY-4.0).

1. Copy (or submodule) `RULES.md` into your repo.
2. Point your harness at it:
   - **Claude Code:** reference it from `CLAUDE.md` with an `@RULES.md` import.
   - **OpenCode / Codex / others:** reference it from `AGENTS.md`.
   - A symlink from both `CLAUDE.md` and `AGENTS.md` to one canonical file
     keeps them from drifting.
3. Project-specific files may tighten the rules; they must never loosen them.
4. Edit what you disagree with — the rules are numbered so reviews can cite
   them ("violates rule 56").

## Appendix D — Book number ↔ repository `RULES.md` mapping

The repository groups the rules by topic; the book orders them pedagogically.
Same one hundred rules, two orderings.

| Book rules | RULES.md rules | Topic |
|---|---|---|
| 1–10 | 1–10 | Hard rules |
| 11–18 | 11–18 | The crew |
| 19 | 98 | Plan first, sprint sizing |
| 20 | 100 | No flattery |
| 21–28 | 19–26 | Configuration |
| 29–30 | 45–46 | Config-driven deployment, storage adapter |
| 31–38 | 27–34 | Architecture, file size |
| 39–40 | 37–38 | God classes, mechanical refactors |
| 41–46 | 39–44 | Cross-platform |
| 47–50 | 47–50 | Containers, health, deploy gates |
| 51–60 | 77–86 | Errors, observability, dependencies |
| 61–70 | 51–60 | Secret hygiene |
| 71–78 | 69–76 | Testing, quality bar |
| 79–80 | 35–36 | Function size, nesting (complexity budget) |
| 81–88 | 61–68 | Versioning, tags, build numbers |
| 89 | 92 | Post-release cleanup |
| 90 | 96 | Plan status tracking |
| 91–95 | 87–91 | Dependency disclosure, dead code, lint |
| 96–98 | 93–95 | README, ADRs, bug/feature ledgers |
| 99 | 97 | Decisions persisted same-commit |
| 100 | 99 | Verbatim errors, diffs not prose |

## Glossary

- **The crew** — five fixed AI roles (Jason, Linda, Claude, Claudina,
  Claudius) plus one human; model bindings are configuration, never canon.
- **The Powell rule** — get 90% of the information you need to make a
  decision, then make the decision; below 90% certainty, ask the human more
  questions. Never guess ahead; never stall gathering past 90%.
- **The quality bar** — every project keeps a rubric grading the software;
  90% (solid A−) is the working bar, polish takes it to 95%, nothing
  publishes below 95%.
- **Trust boundary** — anything beyond the local working tree: the remote
  repo, a registry, a cluster, a host you don't own. Everything that crosses
  one gets scanned.
- **Go local** — the standing instruction that rebinds every persona to a
  local model backend; same roles, same rules, different engine.
- **Chapter card** — the twenty-rule checklist closing each chapter.
