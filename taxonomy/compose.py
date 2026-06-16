#!/usr/bin/env python3
"""Compose a layered ruleset into per-seat slices sized to each model's budget.

Single source of truth = rules.yaml (axiom core + preference layers). Given a crew
config, emit:
  - generated/axioms.md + generated/layers/*.md   (readable docs from the registry)
  - generated/seats/<name>.md                       (resident slice + paged tail)
  - generated/summary.md                            (capacity, coverage, Guy's test)

The model: rules are a cache hierarchy. Each seat holds a RESIDENT working set sized
by the sizing law (~1 rule / billion params, rule P-FLEET); everything else is PAGED
into context on a trigger. The team-resident union is the crew's "memorized" canon.

Usage: compose.py [rules.yaml] [crew.yaml]
"""
import os, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
RULES = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "rules.yaml")
CREW = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "crew-3.yaml")
OUT = os.path.join(HERE, "generated", os.path.splitext(os.path.basename(CREW))[0])


def load():
    reg = yaml.safe_load(open(RULES))
    crew = yaml.safe_load(open(CREW))
    pools = {"axiom": reg["axioms"]}
    for name, rules in reg.get("layers", {}).items():
        pools[name] = rules
    return reg, crew, pools


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(text)


def doc(title, rules, blurb=""):
    out = [f"# {title}", ""]
    if blurb:
        out += [blurb, ""]
    for r in sorted(rules, key=lambda r: -r["priority"]):
        out.append(f"- **{r['title']}** (`{r['id']}`, prio {r['priority']}) — {r['text']}")
    return "\n".join(out) + "\n"


def candidates(seat, pools):
    """Rules a seat can draw, scored: focus-match first, then priority."""
    focus = set(seat.get("focus", []))
    cand = []
    for layer in seat["draws"]:
        for r in pools.get(layer, []):
            match = len(set(r.get("triggers", [])) & focus) > 0 or "always" in r.get("triggers", [])
            cand.append((1 if match else 0, r["priority"], layer, r))
    cand.sort(key=lambda t: (-t[0], -t[1]))
    return cand


def main():
    reg, crew, pools = load()
    active = crew["project"]["active_layers"]

    # 1) readable layer docs from the registry
    write(os.path.join(OUT, "axioms.md"),
          doc("Axioms — immutable, universal core", pools["axiom"],
              "Every seat. Few by design: the resident budget is tiny, so the "
              "always-on core is the smallest set that must never be missed."))
    for layer, rules in reg.get("layers", {}).items():
        write(os.path.join(OUT, "layers", f"{layer}.md"),
              doc(f"{layer.capitalize()} layer", rules))

    # 2) per-seat slices
    active_ids = {r["id"] for L in active for r in pools.get(L, [])}
    team_resident = set()
    seat_reports = []
    for seat in crew["seats"]:
        budget = seat["params_b"]
        cand = candidates(seat, pools)
        resident = cand[:budget]
        resident_ids = {r["id"] for _, _, _, r in resident}
        team_resident |= resident_ids
        # paged = active rules this seat draws but doesn't hold resident
        drawable = [r for L in seat["draws"] for r in pools.get(L, [])]
        paged = [r for r in drawable if r["id"] not in resident_ids]
        lines = [f"# {seat['name']} — {seat['role']}", "",
                 f"Model `{seat['model']}` · ~{budget}B → rule budget **{budget}** "
                 f"(sizing law). Draws: {', '.join(seat['draws'])}.", "",
                 f"## Resident ({len(resident)}) — held in weights / always in prompt"]
        for _, _, layer, r in resident:
            lines.append(f"- [{layer}] **{r['title']}** (`{r['id']}`)")
        lines += ["", f"## Paged ({len(paged)}) — injected on trigger"]
        for r in sorted(paged, key=lambda r: -r["priority"])[:60]:
            lines.append(f"- **{r['title']}** (`{r['id']}`) ← triggers: {', '.join(r.get('triggers', []))}")
        write(os.path.join(OUT, "seats", f"{seat['name'].lower()}.md"), "\n".join(lines) + "\n")
        seat_reports.append((seat, len(resident), len(paged)))

    # 3) capacity + coverage + Guy's test
    axiom_ids = {r["id"] for r in pools["axiom"]}
    axioms_covered = axiom_ids <= team_resident
    missing_axioms = sorted(axiom_ids - team_resident)
    total_budget = sum(s["params_b"] for s in crew["seats"])
    small_budget = sum(s["params_b"] for s in crew["seats"] if s["params_b"] <= 20)
    n_axioms = len(axiom_ids)

    s = ["# Compose summary", "",
         f"Crew: **{crew['project']['name']}** — {len(crew['seats'])} seats, "
         f"total rule budget **{total_budget}**.", "",
         f"- Active rules across layers: **{len(active_ids)}**",
         f"- Team-resident (memorized) union: **{len(team_resident)}**",
         f"- Paged tail (context-injected on demand): **{len(active_ids) - len(team_resident)}**",
         f"- Axiom core: **{n_axioms}** rules", "",
         "## Per seat",
         "| Seat | Model | Budget | Resident | Paged |",
         "|------|-------|-------:|---------:|------:|"]
    for seat, res, pg in seat_reports:
        s.append(f"| {seat['name']} | {seat['model']} | {seat['params_b']} | {res} | {pg} |")
    s += ["",
          "## Safety: is every axiom resident in *some* seat?",
          f"- **{'YES' if axioms_covered else 'NO'}** — "
          + ("all axioms are memorized somewhere in the crew."
             if axioms_covered else f"missing: {', '.join(missing_axioms)} (paged-only — risky).")]
    s += ["",
          "## Guy's test — how small can the crew get?",
          f"- The axiom core is **{n_axioms}** rules → needs **{n_axioms}** resident "
          f"slots (≈{n_axioms}B of summed budget) to hold every axiom in-weights.",
          f"- Small models only (≤20B) sum to **{small_budget}B** "
          + (f"→ **short of {n_axioms}**: a frontier seat (or fewer axioms) is required "
             "to hold the whole core resident without paging."
             if small_budget < n_axioms else
             f"→ **covers the {n_axioms} axioms** without a frontier model."),
          f"- Lever: trimming the axiom core to ≤ small-model budget "
          f"({small_budget}B here) is what lets a frontier-free crew stay safe.",
          "",
          "## Capacity dial",
          "- Team-resident capacity = Σ(per-model budgets). Harder project → add seats "
          "→ more resident, less paging. Easier project → drop a seat."]
    write(os.path.join(OUT, "summary.md"), "\n".join(s) + "\n")

    emit_slices(crew, pools)

    print(f"composed: {len(active_ids)} active rules, {len(team_resident)} team-resident, "
          f"axioms covered={axioms_covered}. See {OUT}/summary.md")


def emit_slices(crew, pools):
    """Per-seat full-text rule slice for baking into a model's system prompt:
    all axioms (universal) + the seat's role rules from its non-axiom draws.
    Small seats (<=20B) cap the role rules to the highest-priority dozen."""
    for seat in crew["seats"]:
        cap = 12 if seat["params_b"] <= 20 else 999
        lines = [f"# Ed's Rules — {seat['name']}'s slice ({seat['role']})", "",
                 "## Axioms — universal, always apply", ""]
        for r in sorted(pools["axiom"], key=lambda r: -r["priority"]):
            lines.append(f"- **{r['title']}** — {r['text']}")
        role = []
        for layer in seat["draws"]:
            if layer == "axiom":
                continue
            role += pools.get(layer, [])
        role = sorted(role, key=lambda r: -r["priority"])[:cap]
        if role:
            lines += ["", f"## {seat['name']}'s rules", ""]
            for r in role:
                lines.append(f"- **{r['title']}** — {r['text']}")
        write(os.path.join(OUT, "slices", f"{seat['name'].lower()}.rules.md"), "\n".join(lines) + "\n")
    print(f"  slices: {', '.join(s['name'].lower() for s in crew['seats'])} -> {OUT}/slices/")


if __name__ == "__main__":
    main()
