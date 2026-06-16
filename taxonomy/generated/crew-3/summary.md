# Compose summary

Crew: **cloud-native distributed app (multi-platform)** — 3 seats, total rule budget **221**.

- Active rules across layers: **50**
- Team-resident (memorized) union: **50**
- Paged tail (context-injected on demand): **0**
- Axiom core: **24** rules

## Per seat
| Seat | Model | Budget | Resident | Paged |
|------|-------|-------:|---------:|------:|
| Jason | qwen2.5-coder:7b | 7 | 7 | 35 |
| Claude | qwen2.5-14b | 14 | 14 | 33 |
| Claudius | claude-opus | 200 | 50 | 0 |

## Safety: is every axiom resident in *some* seat?
- **YES** — all axioms are memorized somewhere in the crew.

## Guy's test — how small can the crew get?
- The axiom core is **24** rules → needs **24** resident slots (≈24B of summed budget) to hold every axiom in-weights.
- Small models only (≤20B) sum to **21B** → **short of 24**: a frontier seat (or fewer axioms) is required to hold the whole core resident without paging.
- Lever: trimming the axiom core to ≤ small-model budget (21B here) is what lets a frontier-free crew stay safe.

## Capacity dial
- Team-resident capacity = Σ(per-model budgets). Harder project → add seats → more resident, less paging. Easier project → drop a seat.
