# Changelog

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/).

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
