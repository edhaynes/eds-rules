# Changelog

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/).

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
