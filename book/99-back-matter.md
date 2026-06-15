# Back Matter

## Companion media

A two-minute demonstration accompanies these rules: one local Llama 3.1 8B
model, the same weights run twice — vanilla on one side, and with these hundred
rules standing in front of it on the other. The ruled model quotes a rule cold,
catches a hardcoded key and *names the rule it breaks*, and refuses to invent a
rule that does not exist. The "best rule × worst rule" podcast series then walks
the hundred one pair at a time.

- **Watch and listen — the 100 Rules podcast:**
  [youtu.be/rmMGM460FMw](https://youtu.be/rmMGM460FMw)
- **Companion repository (`RULES.md`, CC-BY-4.0):**
  [github.com/edhaynes/eds-rules](https://github.com/edhaynes/eds-rules)

**Built with Bard.** The local models behind the demonstration — and the
on-device inference this book keeps holding up as the cheap, private
alternative to a frontier API — run on **Bard**, *LLM on the Go*: local models
on iPhone, iPad, and Mac.

- **Bard on the App Store:**
  [apps.apple.com/app/bard-llm/id6772813533](https://apps.apple.com/app/bard-llm/id6772813533)

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
   them ("violates rule 55").

## Appendix D — Book number ↔ repository `RULES.md` mapping

The repository groups the rules by topic; the book orders them pedagogically.
Same one hundred rules, two orderings.

| Book rules | RULES.md rules | Topic |
|---|---|---|
| 1–10 | 1–10 | Hard rules |
| 11–12 | 11–12 | The Powell rule, the crew and its governance |
| 13 | 98 | Plan first, sprint sizing |
| 14–18 | 13–17 | The crew (Claudius, Jason, Claude, Claudina, Linda) |
| 19 | 99 | No flattery |
| 20 | 18 | Go local |
| 21 | 19 | If it can change, it's config |
| 22–25 | 27–30 | Architecture thesis, vendor interfaces, search-first, DI |
| 26–28 | 20–22 | No silent fallbacks, startup validation, one config layer |
| 29 | 31 | Objects with one job |
| 30–31 | 45–46 | Storage adapter, on-prem/cloud as config |
| 32–35 | 23–26 | "Use X locally", zero-setup defaults, magic numbers, `.env.example` |
| 36–37 | 34–35 | File-size gauge, god classes |
| 38–39 | 32–33 | SOLID, one class per file |
| 40 | 36 | Mechanical refactor commits |
| 41 | 47 | Deploy gates never disabled |
| 42 | 77 | Catch specific, never swallow |
| 43–44 | 83–84 | Pinned dependencies, vulnerability audits |
| 45–46 | 48–49 | Health endpoints, container-friendly |
| 47 | 78 | Loud in dev, graceful in prod |
| 48 | 39 | Three platforms, two in CI |
| 49–50 | 79–80 | Logger not print, AI errors surface |
| 51 | 40 | Path libraries |
| 52 | 85 | Stdlib plus one dependency |
| 53 | 41 | No hardcoded temp, home, or drive letters |
| 54–55 | 42–43 | Both architectures, no shell-isms |
| 56 | 81 | Structural cleanup (context managers) |
| 57 | 86 | Project-local virtualenvs |
| 58 | 50 | Progress on slow paths |
| 59 | 82 | Structured logs |
| 60 | 44 | Line endings |
| 61–63 | 51–53 | Hooks first, rotate first, never copy a secret |
| 64 | 69 | The quality rubric (you get what you inspect) |
| 65–66 | 54–55 | Scan the artifact, scan the range |
| 67–69 | 70–72 | Tests ship with logic, contract first, 100% coverage |
| 70–72 | 56–58 | "Harmless" config, unauthored files, pre-push rescan |
| 73–74 | 73–74 | Correctness over speed, coverage ratchet |
| 75–76 | 59–60 | `.gitignore` day one, fix the hook |
| 77–78 | 75–76 | Full regression, no network in unit tests |
| 79–80 | 37–38 | Function size, nesting (complexity budget) |
| 81–82 | 61–62 | Immutable tags, versions only forward |
| 83 | 93 | Decisions persisted same-commit |
| 84 | 63 | One canonical version home |
| 85 | 94 | Bug/feature ledgers |
| 86–87 | 64–65 | Fetch before tagging, build numbers |
| 88 | 100 | Verbatim errors, diffs not prose |
| 89 | 66 | Changelog in the bump commit |
| 90 | 95 | Plan status tracking |
| 91 | 96 | Immutable ADRs |
| 92–93 | 67–68 | Version display, push tags by name |
| 94–95 | 88–89 | Lint every commit, dead-code sweeps |
| 96 | 90 | Post-release cleanup |
| 97 | 97 | README regeneration |
| 98–99 | 91–92 | No commented-out code, no orphan TODOs |
| 100 | 87 | Dependency disclosure |

## Appendix E — Bending the model: the three ways to retrain

The foreword names three ways to move a model off its C-grade defaults. In
order of cost:

| Path | Cost | Robustness | Who it's for |
|---|---|---|---|
| Train from scratch | Millions | Highest | Labs, not you |
| Tune open weights | Days to weeks — the dataset is the work | Medium-high — shapes style and defaults; process discipline still needs gates | Anyone with a capable machine |
| Standing rules in the prompt | Free, immediate | Lowest — instructions dilute | Everyone; start here |

**Training from scratch** is listed for completeness. If you have to ask what
it costs, it is the wrong path.

**Tuning open weights** is more approachable than its reputation, with one
honest caveat up front: tuning shapes the model's defaults and style; it does
not install procedural discipline. A tuned model writes in your idiom — it
still won't refuse to commit on a red suite unless a gate stops it. Take a strong
open-weight coding model and fine-tune it with LoRA or QLoRA — techniques
that adjust a small fraction of the model's weights, so the hardware stays
reasonable: a single consumer GPU handles the small-and-mid sizes, and one
large unified-memory machine handles the 70-billion-parameter class. The
established open-source tooling (Hugging Face PEFT, Axolotl, Unsloth) makes
the mechanics a configuration file, not a research project. The hard part —
and the entire point — is the dataset: a few thousand *curated* examples of
your standard (diffs that passed your review, before-and-after refactors,
rules-compliant modules) beat millions of scraped files. Quantity got the
model into this condition; only quality gets it out. Grade the tuned model
against your rubric, not against public benchmarks.

Your starting point matters too. A few less famous model families are trained
on curated, governed corpora rather than the raw scrape — IBM's Granite Code
models are the notable example: Apache-2.0 licensed, trained on
license-filtered data with documented provenance, in over a hundred
programming languages — a pipeline that deduplicates aggressively, scans for
malware, and even redacts keys and passwords from the training data itself.
Secret hygiene all the way down. And InstructLab, the open-source Red Hat/IBM
fine-tuning project, is exactly this appendix's second path packaged for
people who are not researchers: it turns "tune open weights" into a
command-line workflow fed by your own curated examples. A model that begins
license-clean and provenance-tracked has less of the internet's average to
unlearn.

**Standing rules in the prompt** is this book: the hundred rules, dropped
into the file your harness reads on every request (Appendix C shows how, per
harness). It costs nothing and works today, on any model, including the
closed ones you cannot tune. Its weakness is honesty itself: long sessions
dilute instructions, and a model can drift from a rule it read an hour ago.
That is why the rules lean so hard on gates that do not depend on the model's
memory — pre-commit hooks (Appendix A), scans, and tests run whether or not
anyone remembered the rule. Not foolproof is acceptable when the hooks are.

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
