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
Same one hundred rules, two orderings. (The repository was consolidated
2026-06-14 — overlapping rules merged, freed slots refilled, and a new
*Operating an AI fleet* chapter added; the count held at 100. This table tracks
that numbering.)

| Book rules | RULES.md rules | Topic |
|---|---|---|
| 1–14 | 1–14 | Hard rules, the Powell rule, the five-roles charter |
| 15 | 90 | Plan first |
| 16–20 | 15–19 | The crew — Claudius, Jason, Claude, Claudina, Linda |
| 21 | 91 | No flattery |
| 22 | 20 | Go local |
| 23 | 21 | If it can change, it's config (absorbs magic numbers) |
| 24–27 | 28–31 | Architecture thesis, vendor interfaces, search-first, DI |
| 28–30 | 22–24 | No silent fallbacks, startup validation, one config layer |
| 31 | 32 | Objects with one job (absorbs SOLID) |
| 32–33 | 43–44 | Storage adapter, on-prem/cloud as config |
| 34–35 | 25–26 | "Use X locally", zero-setup defaults |
| 36 | 34 | The size gauge — files, functions, nesting |
| 37 | 35 | No god classes |
| 38 | 33 | One non-trivial class per file |
| 39 | 27 | Ship the `.env.example` |
| 40 | 36 | Mechanical refactor commits |
| 41 | 45 | Deploy gates never disabled |
| 42 | 71 | Catch specific, never swallow (absorbs cleanup) |
| 43 | 77 | Pin and lock (absorbs vulnerability audits) |
| 44–45 | 47–48 | Health endpoints; container stack — Podman/UBI/OpenShift |
| 46 | 46 | Idempotency |
| 47 | 72 | Loud in dev, graceful in prod |
| 48 | 37 | Three platforms, two in CI |
| 49 | 73 | Logger not print (absorbs structured logs) |
| 50 | 74 | AI errors surface; agents don't invent tools |
| 51 | 38 | Path libraries (absorbs LF line endings) |
| 52 | 78 | Stdlib plus one dependency |
| 53–55 | 39–41 | Temp/home/drive, both architectures, no shell-isms |
| 56 | 42 | Time is UTC until it's displayed |
| 57 | 79 | Project-local virtualenvs |
| 58 | 49 | Progress on slow paths |
| 59 | 75 | Remote-call timeout, retry, circuit-breaker |
| 60 | 76 | Correlation/trace ID |
| 61 | 50 | Reversible, idempotent migrations |
| 62–65 | 51–54 | Hooks first, rotate first, never copy a secret, scan every boundary |
| 66 | 62 | The quality rubric (you get what you inspect) |
| 67–69 | 63–65 | Tests ship with logic, contract first, 100% coverage |
| 70–72 | 66–68 | Correctness over speed, coverage ratchet, full regression |
| 73 | 69 | Latency/throughput budget |
| 74 | 70 | No network in unit tests |
| 75 | 55 | Fix the hook that missed it |
| 76 | 56 | Immutable tags (absorbs fetch-before-tag, push by name) |
| 77 | 57 | Versions only move forward |
| 78 | 86 | Persist decisions same-commit (absorbs immutable ADRs) |
| 79 | 58 | One canonical version home |
| 80 | 87 | Bug/feature ledgers |
| 81 | 59 | Build numbers |
| 82 | 92 | Verbatim errors, diffs not prose |
| 83 | 60 | Changelog in the bump commit |
| 84 | 88 | Plan status tracking |
| 85 | 61 | Version displayed everywhere |
| 86–88 | 80–82 | Lint every commit, dead-code sweep, post-release cleanup |
| 89 | 89 | README regeneration |
| 90–91 | 83–84 | No commented-out code, no orphan TODOs |
| 92 | 85 | A living `STATE.md` |
| 93–100 | 93–100 | Operating an AI fleet — sizing law, slicing, context ceilings, verify-then-escalate |

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
