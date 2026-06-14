# Ed's 100 Rules — series episode map

Author: Jason-eds · 2026-06-13

Source of order: `quality/grades.csv` composite score (the rule-quality rubric, F19).

**Format:** 50 episodes (Ep91–140), each pairs one top-scoring rule with one
bottom-scoring rule so the heavy hitters spread across the whole run instead of
front-loading. Ep90 is the existing intro. Guest-speaker episodes are a later
expansion beyond the 50. Pairing rule: rank *k* from the top with rank *k* from
the bottom (Ep91 = best + worst).


## The 50 episodes (good rule × bad rule)

| Ep | GOOD (score) | BAD (score) | The contrast angle |
|---|---|---|---|
| 91 | #1 Secret scan before ship (90.0) | #19 Go local rebinds the crew (25.5) | _tbd_ |
| 92 | #2 Never hardcode a secret (82.0) | #18 Linda searches wide (30.0) | _tbd_ |
| 93 | #20 Zero hardcoded values (74.0) | #13 Five roles; human is final (33.5) | _tbd_ |
| 94 | #51 Hooks before first commit (73.5) | #14 Claudius plans deep (37.5) | _tbd_ |
| 95 | #9 Fail fast (72.5) | #42 Both arches; flag no-ARM (39.5) | _tbd_ |
| 96 | #3 Distrust every external input (72.0) | #83 Structured logs past a script (40.0) | _tbd_ |
| 97 | #4 Destruction needs a human (71.5) | #90 Cleanup sweep after release (41.5) | _tbd_ |
| 98 | #59 Gitignore keys from day one (71.0) | #95 Plans carry a live Status (42.5) | _tbd_ |
| 99 | #84 Pin it and lock it (67.5) | #33 One non-trivial class per file (42.5) | _tbd_ |
| 100 | #22 Validate config at startup (66.5) | #15 Jason sprints sized for 90% (43.5) | _tbd_ |
| 101 | #46 Pre-deploy gates never off (66.5) | #96 ADRs are immutable (44.0) | _tbd_ |
| 102 | #56 Inspect config-file diffs (65.5) | #68 Push tags by name (44.0) | _tbd_ |
| 103 | #70 Tests with logic; regress first (65.0) | #36 Size refactors are own commits (44.0) | _tbd_ |
| 104 | #78 No swallowed exceptions (64.5) | #73 Correctness over speed (44.5) | _tbd_ |
| 105 | #7 Green commit; healthy handover (64.0) | #49 Podman / UBI / OpenShift (45.0) | _tbd_ |
| 106 | #6 Push early; push always (63.5) | #97 Regenerate the README (45.5) | _tbd_ |
| 107 | #54 Scan the whole artifact (63.5) | #76 Latency budget; gated like cov. (45.5) | _tbd_ |
| 108 | #55 Scan the range; not the tip (63.5) | #50 Show progress; cache default (45.5) | _tbd_ |
| 109 | #5 Autonomy bounded by VC (63.0) | #39 Three platforms; two in CI (46.0) | _tbd_ |
| 110 | #58 Pre-push rescan + tests (63.0) | #32 OO + SOLID where it earns (46.0) | _tbd_ |
| 111 | #77 No network in unit tests (63.0) | #25 Zero-setup local defaults (46.0) | _tbd_ |
| 112 | #88 Lint + format every commit (62.5) | #65 Unique build number (46.5) | _tbd_ |
| 113 | #23 One config layer; one order (61.5) | #43 No shell-isms; orchestrate (47.0) | _tbd_ |
| 114 | #26 No magic numbers (61.5) | #24 Local default; not hardcoded (47.0) | _tbd_ |
| 115 | #47 Idempotent; safe to re-run (61.5) | #45 Same code on-prem or cloud (47.5) | _tbd_ |
| 116 | #75 Full regression; with numbers (61.5) | #28 Architecture beats language (47.5) | _tbd_ |
| 117 | #11 No path/OS assumptions; script (61.0) | #92 No orphan TODOs (48.0) | _tbd_ |
| 118 | #12 Powell rule: 90% then decide (60.5) | #17 Claudina: cross-platform day one (48.0) | _tbd_ |
| 119 | #85 Audit for vulnerabilities (60.5) | #60 After a leak; fix the hook (48.5) | _tbd_ |
| 120 | #8 One purpose per commit (60.0) | #67 Show the version everywhere (49.0) | _tbd_ |
| 121 | #21 Never silently fall back (60.0) | #64 Fetch tags before tagging (49.0) | _tbd_ |
| 122 | #31 DI over globals (60.0) | #99 No flattery; no yes-manning (49.5) | _tbd_ |
| 123 | #40 Path library + LF endings (60.0) | #35 No god classes (49.5) | _tbd_ |
| 124 | #53 Never copy a secret anywhere (59.5) | #94 File bugs/features on sight (50.5) | _tbd_ |
| 125 | #80 A logger; never print (59.5) | #74 Coverage never goes down (50.5) | _tbd_ |
| 126 | #82 Cleanup is structural (59.0) | #66 Changelog rides the bump (50.5) | _tbd_ |
| 127 | #98 Plan first; size for 90% (59.0) | #62 Versions only move forward (50.5) | _tbd_ |
| 128 | #27 Ship the .env.example (58.0) | #38 Shallow nesting (51.0) | _tbd_ |
| 129 | #57 Scan files you didn't write (58.0) | #48 Health endpoints + SIGTERM (51.5) | _tbd_ |
| 130 | #86 Stdlib plus one; not five (58.0) | #44 Storage goes through adapter (51.5) | _tbd_ |
| 131 | #30 Search open source first (57.5) | #71 Contract first; code second (52.0) | _tbd_ |
| 132 | #37 Small functions; few params (57.5) | #52 A touched secret is burned (52.0) | _tbd_ |
| 133 | #41 No hardcoded temp/home/drive (57.5) | #72 100% line + branch coverage (52.5) | _tbd_ |
| 134 | #79 Loud dev; graceful prod (57.5) | #61 Tags are immutable (53.0) | _tbd_ |
| 135 | #89 Dead-code pass after features (57.5) | #16 Claude searches before building (53.0) | _tbd_ |
| 136 | #10 Disclose every dependency (56.5) | #93 Persist decisions same commit (53.5) | _tbd_ |
| 137 | #63 SemVer; one canonical home (56.5) | #100 Verbatim errors; diffs; asks (54.0) | _tbd_ |
| 138 | #34 Files small; never >1000 lines (56.0) | #87 Project-local virtualenv (54.5) | _tbd_ |
| 139 | #69 Inspect; grade to a rubric (56.0) | #29 Swappable interface per axis (55.0) | _tbd_ |
| 140 | #81 AI errors surface; no fake tool (56.0) | #91 No commented-out code (55.5) | _tbd_ |

## Full rule leaderboard (the score-ranked order)

| Rank | # | Rule | Section | Score |
|---|---|---|---|---|
| 1 | 1 | Secret scan before ship | hard | 90.0 |
| 2 | 2 | Never hardcode a secret | hard | 82.0 |
| 3 | 20 | Zero hardcoded values | config | 74.0 |
| 4 | 51 | Hooks before first commit | secret | 73.5 |
| 5 | 9 | Fail fast | hard | 72.5 |
| 6 | 3 | Distrust every external input | hard | 72.0 |
| 7 | 4 | Destruction needs a human | hard | 71.5 |
| 8 | 59 | Gitignore keys from day one | secret | 71.0 |
| 9 | 84 | Pin it and lock it | deps | 67.5 |
| 10 | 22 | Validate config at startup | config | 66.5 |
| 11 | 46 | Pre-deploy gates never off | deploy | 66.5 |
| 12 | 56 | Inspect config-file diffs | secret | 65.5 |
| 13 | 70 | Tests with logic; regress first | test | 65.0 |
| 14 | 78 | No swallowed exceptions | errors | 64.5 |
| 15 | 7 | Green commit; healthy handover | hard | 64.0 |
| 16 | 6 | Push early; push always | hard | 63.5 |
| 17 | 54 | Scan the whole artifact | secret | 63.5 |
| 18 | 55 | Scan the range; not the tip | secret | 63.5 |
| 19 | 5 | Autonomy bounded by VC | hard | 63.0 |
| 20 | 58 | Pre-push rescan + tests | secret | 63.0 |
| 21 | 77 | No network in unit tests | test | 63.0 |
| 22 | 88 | Lint + format every commit | hygiene | 62.5 |
| 23 | 23 | One config layer; one order | config | 61.5 |
| 24 | 26 | No magic numbers | config | 61.5 |
| 25 | 47 | Idempotent; safe to re-run | deploy | 61.5 |
| 26 | 75 | Full regression; with numbers | test | 61.5 |
| 27 | 11 | No path/OS assumptions; script | hard | 61.0 |
| 28 | 12 | Powell rule: 90% then decide | crew | 60.5 |
| 29 | 85 | Audit for vulnerabilities | deps | 60.5 |
| 30 | 8 | One purpose per commit | hard | 60.0 |
| 31 | 21 | Never silently fall back | config | 60.0 |
| 32 | 31 | DI over globals | arch | 60.0 |
| 33 | 40 | Path library + LF endings | xplat | 60.0 |
| 34 | 53 | Never copy a secret anywhere | secret | 59.5 |
| 35 | 80 | A logger; never print | errors | 59.5 |
| 36 | 82 | Cleanup is structural | errors | 59.0 |
| 37 | 98 | Plan first; size for 90% | working | 59.0 |
| 38 | 27 | Ship the .env.example | config | 58.0 |
| 39 | 57 | Scan files you didn't write | secret | 58.0 |
| 40 | 86 | Stdlib plus one; not five | deps | 58.0 |
| 41 | 30 | Search open source first | arch | 57.5 |
| 42 | 37 | Small functions; few params | size | 57.5 |
| 43 | 41 | No hardcoded temp/home/drive | xplat | 57.5 |
| 44 | 79 | Loud dev; graceful prod | errors | 57.5 |
| 45 | 89 | Dead-code pass after features | hygiene | 57.5 |
| 46 | 10 | Disclose every dependency | hard | 56.5 |
| 47 | 63 | SemVer; one canonical home | version | 56.5 |
| 48 | 34 | Files small; never >1000 lines | size | 56.0 |
| 49 | 69 | Inspect; grade to a rubric | test | 56.0 |
| 50 | 81 | AI errors surface; no fake tool | errors | 56.0 |
| 51 | 91 | No commented-out code | hygiene | 55.5 |
| 52 | 29 | Swappable interface per axis | arch | 55.0 |
| 53 | 87 | Project-local virtualenv | deps | 54.5 |
| 54 | 100 | Verbatim errors; diffs; asks | working | 54.0 |
| 55 | 93 | Persist decisions same commit | docs | 53.5 |
| 56 | 16 | Claude searches before building | crew | 53.0 |
| 57 | 61 | Tags are immutable | version | 53.0 |
| 58 | 72 | 100% line + branch coverage | test | 52.5 |
| 59 | 52 | A touched secret is burned | secret | 52.0 |
| 60 | 71 | Contract first; code second | test | 52.0 |
| 61 | 44 | Storage goes through adapter | deploy | 51.5 |
| 62 | 48 | Health endpoints + SIGTERM | deploy | 51.5 |
| 63 | 38 | Shallow nesting | size | 51.0 |
| 64 | 62 | Versions only move forward | version | 50.5 |
| 65 | 66 | Changelog rides the bump | version | 50.5 |
| 66 | 74 | Coverage never goes down | test | 50.5 |
| 67 | 94 | File bugs/features on sight | docs | 50.5 |
| 68 | 35 | No god classes | size | 49.5 |
| 69 | 99 | No flattery; no yes-manning | working | 49.5 |
| 70 | 64 | Fetch tags before tagging | version | 49.0 |
| 71 | 67 | Show the version everywhere | version | 49.0 |
| 72 | 60 | After a leak; fix the hook | secret | 48.5 |
| 73 | 17 | Claudina: cross-platform day one | crew | 48.0 |
| 74 | 92 | No orphan TODOs | hygiene | 48.0 |
| 75 | 28 | Architecture beats language | arch | 47.5 |
| 76 | 45 | Same code on-prem or cloud | deploy | 47.5 |
| 77 | 24 | Local default; not hardcoded | config | 47.0 |
| 78 | 43 | No shell-isms; orchestrate | xplat | 47.0 |
| 79 | 65 | Unique build number | version | 46.5 |
| 80 | 25 | Zero-setup local defaults | config | 46.0 |
| 81 | 32 | OO + SOLID where it earns | arch | 46.0 |
| 82 | 39 | Three platforms; two in CI | xplat | 46.0 |
| 83 | 50 | Show progress; cache default | deploy | 45.5 |
| 84 | 76 | Latency budget; gated like cov. | test | 45.5 |
| 85 | 97 | Regenerate the README | docs | 45.5 |
| 86 | 49 | Podman / UBI / OpenShift | deploy | 45.0 |
| 87 | 73 | Correctness over speed | test | 44.5 |
| 88 | 36 | Size refactors are own commits | size | 44.0 |
| 89 | 68 | Push tags by name | version | 44.0 |
| 90 | 96 | ADRs are immutable | docs | 44.0 |
| 91 | 15 | Jason sprints sized for 90% | crew | 43.5 |
| 92 | 33 | One non-trivial class per file | arch | 42.5 |
| 93 | 95 | Plans carry a live Status | docs | 42.5 |
| 94 | 90 | Cleanup sweep after release | hygiene | 41.5 |
| 95 | 83 | Structured logs past a script | errors | 40.0 |
| 96 | 42 | Both arches; flag no-ARM | xplat | 39.5 |
| 97 | 14 | Claudius plans deep | crew | 37.5 |
| 98 | 13 | Five roles; human is final | crew | 33.5 |
| 99 | 18 | Linda searches wide | crew | 30.0 |
| 100 | 19 | Go local rebinds the crew | crew | 25.5 |
