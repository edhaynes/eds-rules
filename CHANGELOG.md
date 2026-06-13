# Changelog

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/).

## [1.4.4] - 2026-06-13

Net-neutral swap (stays at 100): added the **STATE rule** (#92, "Documentation,
memory, and tracking") — maintain a per-repo `STATE.md` (≤1024 words, ingested at
session start, regenerated each commit) plus a `state.h` index at the projects
root, so a memoryless agent can start cold. It grades 67 (rank 10/100). To free
the slot, the standalone structured-logging rule was folded into the logger rule
(#80). Book sync for this + the 1.4.3 swap is batched under bug B12.

## [1.4.3] - 2026-06-13

Net-neutral rule swap (count stays at exactly 100): three rules added by
importance, three retired by consolidation. `RULES.md` updated; **the book
(`book/ch0*.md`, chapter cards, Appendix D mapping, ~239 cross-references) is
not yet synced — tracked as a follow-on sweep** (book↔repo drift is a known,
in-progress bug until then).

### Added

- **Rule 3 — Distrust every external input.** Validate/constrain at the
  boundary; parameterize queries and commands, confine paths, never interpolate
  untrusted data into SQL, a shell, HTML, or a deserializer. Closes the doc's
  biggest security gap: ten rules on secret *leakage*, none on malicious *input*.
- **Rule 47 — Make every operation idempotent and safe to re-run.** Deploys,
  migrations, setup scripts converge to the same state on re-run and resume
  cleanly after interruption; gate on real end-state, not a partial artifact.
  The agent-era failure mode (and the exact bug hit in voicelab setup the same day).
- **Rule 76 — Declare a latency/throughput budget and gate regressions like
  coverage.** Determinism and latency as first-class, CI-gated features.

### Removed (consolidated)

- LF-line-endings rule → folded into the path-library rule (40).
- Standalone SOLID rule → folded into the OO-design rule (32).
- Dependency-disclosure restatement (the "see rule 9" duplicate) → folded into
  the hard dependency rule (10), which now also names *maintenance status*.

## [1.4.2] - 2026-06-12

### Changed

- Rule 10 consolidates two new doctrines (count stays at 100): **assume
  everything is headless** (no display, nobody at a prompt — agents, CI,
  containers, and 3 a.m. reboots all demand a non-interactive path) and
  **script everything** (manual procedures die with the next reimage; a
  script is a `git clone` away — the frogstation lesson). Book Rule 10 +
  chapter card + RULES.md updated together.

### Added

- `model/` persona support: `PERSONA_FILE` hook in make-rules-model.sh,
  `personas/jason.txt` (public-safe Jason role contract), and
  `bootstrap-node.sh` — fresh box to running rules+persona model in one
  command. Verified end-to-end locally (llama3.1:8b: ~90 tok/s generation,
  3.6k-token system prompt).

## [1.4.1] - 2026-06-12

### Added

- "Start with these ten" on-ramp in the book front matter (F13, book half):
  the ten judgment-ranked rules weighted toward irreversible damage, with the
  explicit promise that the measured ranking from session audits supersedes
  it when the data disagrees.

## [1.4.0] - 2026-06-12

### Added

- `model/` — run the rules as a model: `make-rules-model.sh` builds a custom
  rules-aware Llama 8B from stock Ollama in ~2 minutes (rules baked into the
  system prompt, temperature 0, recall/attribution/violation-detection job
  description). Smoke-tested: violation detection works; number attribution
  is honest-documented as weak vs. the fine-tune.
- `model/README.md` — the measured QLoRA fine-tune recipe (per-rule chunks,
  number drills, open-ended recall gate: forward 10/10, reverse 6/10) and
  the prompt-vs-fine-tune decision table.
- `model/audit-session.py` — stdlib-only session auditor: scans Claude Code
  transcripts (or any log) against the rules via a local Ollama judge; emits
  ledger-ready violations, capped-count rule proposals, and the per-rule
  violation histogram that will answer "how many rules do you actually
  need?" (F12).
- The miss loop documented: missed violations → ledger → training pairs →
  permanent regression gate.

## [1.3.4] - 2026-06-12

### Changed

- **All 100 rules reordered by importance within their chapters** (F5,
  per plans/PLAN_rule-weighting.md): irreversibility first, then fire rate,
  then load-bearing weight. Ch1 takes the middle path — "No scan, no ship"
  keeps #1, the Powell rule leads the who-decides half at Rule 11.
  `RULES.md` renumbered to match; Appendix D regenerated (bijection
  verified); every cross-reference and diagram label remapped; chapter
  openers rewritten where importance-ordering broke topical runs. Regression:
  headings exactly 1–100, zero dangling references, EPUB + PDF build green.

## [1.3.3] - 2026-06-12

### Added

- Foreword: the lopsided-intelligence argument — models are trained on
  quantity not quality (C-grade defaults) yet are fantastic at review,
  reorganization, secret scanning, and merges; the three ways to bend a
  model toward quality (train from scratch / tune open weights / standing
  rules in the prompt — this book is the third).
- Appendix E — "Bending the model": LoRA/QLoRA open-weights tuning, dataset
  curation over volume, IBM Granite Code (license-filtered, provenance-
  tracked training data) and InstructLab as the packaged tune-path.
- Title page: display typography + original B&W crew illustration
  (`book/art/the-team.svg`, placeholder line art); disclaimer moved to its
  own page; chapters start on fresh pages.

## [1.3.2] - 2026-06-12

### Changed

- Trim raised to 7"×10" (technical-book comp set; ~125 pages, prints cheaper
  than 6"×9"/166 since KDP charges per page). Build now emits standalone
  Typst and patches the page size — typst has no named 7×10 paper.
- Prices: softcover $19.99 (was $9.99), Kindle $9.99 (was $4.99).

## [1.3.1] - 2026-06-12

### Added

- Book build pipeline (`book/build.py`): renders the 30 Mermaid diagrams to
  grayscale PNG (mermaid-cli, neutral theme) and builds EPUB + 6"×9" print
  PDF via pandoc/typst. First draft artifacts verified: 166-page PDF at
  exact US-trade trim, all diagrams legible in B&W.
- `RUBRIC.md`: audience profile (newbie AI coders), top-ten frustration map
  with chapter cross-references, weighted grading rubric (90 working bar /
  95 publish).
- `bugs.md` / `features.md` trackers; backlog filed for Ansible coverage,
  zero-trust infrastructure, and the Squawk Box worked example.

## [1.3.0] - 2026-06-11

### Changed

- Manuscript restructured 10×10 → **5 chapters × 20 rules**, most fundamental
  first, each chapter building on the last and opening with a synopsis of the
  fundamentals it stands on: First Principles → Design → Build → Protect and
  Prove → Ship and Remember.

### Added

- Front matter (title/disclaimer, foreword, how to read, meet the crew) and
  back matter (appendices A–D incl. book↔RULES.md mapping, glossary).

## [1.2.0] - 2026-06-11

### Added

- First draft manuscript: 10 chapters, ~34k words, Mermaid diagrams
  throughout. (Changelog entry added retroactively in v1.3.0 — the draft
  commit omitted it, a process slip worth recording.)

## [1.1.2] - 2026-06-11

### Added

- Maintenance policy: the count is fixed at exactly 100 — new rules enter by
  consolidating into an existing rule or deprecating one, never by growing
  the list.

## [1.1.1] - 2026-06-11

### Changed

- Rule 82 now includes tool-call discipline: agents only call tools that
  exist in their tool list; hallucinated tool names waste tokens and stall
  sessions (mirrors private canon §0.17).

## [1.1.0] - 2026-06-11

### Added

- Book outline (`book/OUTLINE.md`): *100 Rules for Writing My Software: The
  Red Hat Way* — 10 chapters × 10 rules, diagram-heavy, black-and-white
  interior, $4.99 Kindle / $9.99 softcover.
- "The Red Hat Way" subtitle and expanded disclaimer (not sanctioned or
  verified by Red Hat; your mileage may vary — do your own research).

## [1.0.5] - 2026-06-11

### Changed

- Title is now "100 Rules for Writing My Software".

## [1.0.4] - 2026-06-11

### Added

- Disclaimer: author is a Red Hat architect but this repo is personal and
  unaffiliated; everything provided "as is" with no warranties.
- Container stack ruling in rule 47: Podman, RHEL UBI, OpenShift — fork the
  rules if you prefer otherwise.

## [1.0.3] - 2026-06-11

### Added

- The quality bar: every project keeps a rubric grading the software; 90% =
  solid A− is the working bar, polish to 95%, publish only at 95%+ (rule 76,
  README "The quality bar").

## [1.0.2] - 2026-06-11

### Changed

- Powell rule restated both ways: get 90% of the information you need, then
  decide; below 90%, ask Eddie more questions — never guess ahead, never
  stall gathering past 90% (rule 17).

## [1.0.1] - 2026-06-11

### Changed

- Documented the rationale for push-early-and-always: AI handles messy merges
  extremely well, removing the old reason to hoard local state.
- Jason now chunks work into independent, clearly defined sprints sized for a
  90% first-try success rate, run in parallel across personas (rules 12, 98).
- Added the Powell rule: any persona that is not 90% certain of what to do
  stops and asks (rule 17).

## [1.0.0] - 2026-06-11

### Added

- Initial release: 100 general-purpose rules (`RULES.md`) distilled from the
  private shared-rules canon.
- Five-persona crew with harness-portable model bindings (Jason, Linda, Claude,
  Claudina, Claudius) documented in `README.md`.
- CC-BY-4.0 license, pre-commit secret-scanning config.
