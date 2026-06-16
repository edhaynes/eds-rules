# Layered ruleset + composer (branch: rules-taxonomy)

Replaces the flat 100 with a **small axiom core + composable preference layers**,
and treats rules as a **cache hierarchy**: each model holds a resident working set
sized by the sizing law (~1 rule/billion params); the rest is paged into context on
demand. See `../plans/PLAN_rules-taxonomy.md` for the full rationale.

## Files
- `rules.yaml` — **single source of truth.** Axiom core + preference layers
  (`personal`, `project`, `bardllm`, `employer`), each rule with a `priority`
  (drives resident selection) and `triggers` (drive paging).
- `crew-*.yaml` — a crew: seats with model bindings, param budgets, layers drawn,
  and focus tags. `crew-3.yaml` = the Guy branch (Claudius/Claude/Linda).
  `crew-bardllm.yaml` = the bard-llm project.
- `compose.py` — generates, per crew, into `generated/<crew>/`:
  - `axioms.md`, `layers/*.md` — readable docs from the registry
  - `seats/<name>.md` — each seat's resident slice + paged tail
  - `summary.md` — capacity, axiom-coverage safety check, **Guy's test**

## Run
```
python3 compose.py rules.yaml crew-3.yaml
python3 compose.py rules.yaml crew-bardllm.yaml
```

## Current numbers
- Axiom core: **24** (target: trim to ≤22 so a frontier-free 8B+14B crew can hold
  the whole core in-weights — see Guy's test in any summary.md).
- cloud-native crew-3 active rules: **52**; bard-llm: **49**.
- Requires: PyYAML.
