# Sub-bar triage — the 33 rules below the 50 keep/cut bar

Worksheet for Eddie's campaign: get every rule to ≥50 by **rewriting** (broaden
or consolidate weak siblings into one stronger rule) or **discarding** — and for
the genuine personal quirks that will never clear a *universal* leverage bar,
**label them "mulligan" rules** (admitted do-overs, YMMV) rather than pretend.

Three verdicts:
- **REWRITE** — weak only because it's narrow or duplicative; broaden it or merge
  it with a sibling to clear 50. (Consolidation frees slots → refill with the 5
  above-bar polish finds, keeping the count at 100 with a higher floor.)
- **MULLIGAN** — earns its slot on conviction, framework, or philosophy, not
  leverage. Keep, but label it openly as a personal quirk (YMMV).
- **DISCARD** — genuine deadweight; nothing redeems it.

| # | Rule | Score | Verdict | Note |
|--:|---|--:|---|---|
| 13 | Five roles, human is final | 33.5 | MULLIGAN | The crew framework — the core personal quirk of this doc. |
| 14 | Claudius plans deep | 37.5 | MULLIGAN | Persona quirk. |
| 15 | Jason sprints sized for 90% | 43.5 | MULLIGAN | Persona quirk. |
| 17 | Claudina: cross-platform day one | 48.0 | MULLIGAN | Persona quirk (cross-platform itself is covered by #11). |
| 18 | Linda searches wide | 30.0 | MULLIGAN | Persona quirk. |
| 19 | Go local rebinds the crew | 25.5 | MULLIGAN | Local-model quirk — lowest-leverage rule; pure preference. |
| 49 | Podman / UBI / OpenShift | 45.0 | MULLIGAN | Eddie keeps by conviction; the rule itself already says "write your own if you prefer Ubuntu." Archetypal mulligan. |
| 28 | Architecture beats language | 47.5 | MULLIGAN | The unenforceable thesis; foundational philosophy, YMMV. |
| 32 | OO + SOLID where it earns | 46.0 | MULLIGAN | Design philosophy/preference. |
| 73 | Correctness over speed | 44.5 | MULLIGAN | Values statement; or fold into the coverage rules (72–75). |
| 99 | No flattery, no yes-manning | 49.5 | MULLIGAN | Personal working-relationship preference. |
| 42 | Both arches, flag no-ARM | 39.5 | MULLIGAN | Eddie's ARM/Gladius concern; niche — or fold into cross-platform. |
| 33 | One non-trivial class per file | 42.5 | MULLIGAN | Style preference; or fold into the size rules. |
| 50 | Show progress; cache default | 45.5 | REWRITE | Merge with #76 into Eddie's "latency/determinism + live progress" rule (graded 52.5). |
| 76 | Latency budget, gated like cov. | 45.5 | REWRITE | Same merge → one above-bar rule. Frees a slot. |
| 64 | Fetch tags before tagging | 49.0 | REWRITE | Consolidate with #61 "tags are immutable; verify remote first." |
| 67 | Show the version everywhere | 49.0 | REWRITE | Consolidate version *display* with build-number (#65). |
| 65 | Unique build number | 46.5 | REWRITE | Consolidate with #67. |
| 68 | Push tags by name | 44.0 | REWRITE | Mechanical sub-rule; fold into #61. |
| 24 | Local default, not hardcoded | 47.0 | REWRITE | Fold into the config rules (#20–23). |
| 25 | Zero-setup local defaults | 46.0 | REWRITE | Fold into config (#20/#24). |
| 45 | Same code on-prem or cloud | 47.5 | REWRITE | Fold into config/portability. |
| 43 | No shell-isms; orchestrate | 47.0 | REWRITE | Broaden + fold into #11 "script everything, cross-platform." |
| 39 | Three platforms, two in CI | 46.0 | REWRITE | Fold into cross-platform (#11/#40). |
| 83 | Structured logs past a script | 40.0 | REWRITE | Fold into the logger rule (#80). |
| 36 | Size refactors are own commits | 44.0 | REWRITE | Fold into one-purpose-per-commit (#8). |
| 35 | No god classes | 49.5 | REWRITE | Broaden ("a god class is a missing collaborator") or fold into size rules. |
| 60 | After a leak, fix the hook | 48.5 | REWRITE | Fold into the post-leak protocol (#52). |
| 96 | ADRs are immutable | 44.0 | REWRITE | Fold into decision-persistence (#93). |
| 95 | Plans carry a live Status | 42.5 | REWRITE | Fold into bug/feature tracking (#94). |
| 90 | Cleanup sweep after release | 41.5 | REWRITE | Fold into dead-code/hygiene (#89). |
| 97 | Regenerate the README | 45.5 | REWRITE | Broaden to "docs are regenerated, not patched." |
| 92 | No orphan TODOs | 48.0 | REWRITE | Fold into hygiene; or broaden the tracker-link discipline. |

**Tally:** ~13 MULLIGAN (label + keep), ~20 REWRITE (most via consolidation),
0 hard DISCARD yet — almost everything is either salvageable or an honest quirk.

**Count mechanics:** consolidation merges ~20 weak rules into ~10 stronger ones,
freeing ~10 slots. Refill with the 5 above-bar polish finds (UTC, least-privilege,
timeouts/retries, the latency merge, migrations) + room for more as Eddie rewrites.
Net: stays at 100, floor rises, mulligans stay openly labeled. Every non-mulligan
rule ≥50; mulligans flagged YMMV.
