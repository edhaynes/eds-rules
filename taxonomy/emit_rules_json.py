#!/usr/bin/env python3
"""Emit the layered ruleset as rules.json for the Rules Browser app (seed data).

Flattens the registry into one array, each rule tagged with its layer and section,
so the app can list, search, and filter/group by layer (axiom/personal/project/...).

Usage: emit_rules_json.py [rules.yaml] [out.json]
"""
import json, os, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "rules.yaml")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "generated", "rules.json")

reg = yaml.safe_load(open(SRC))
rules = []
for r in reg["axioms"]:
    rules.append({"id": r["id"], "title": r["title"], "text": r["text"],
                  "layer": "axiom", "priority": r["priority"], "triggers": r.get("triggers", [])})
for layer, items in reg.get("layers", {}).items():
    for r in items:
        rules.append({"id": r["id"], "title": r["title"], "text": r["text"],
                      "layer": layer, "priority": r["priority"], "triggers": r.get("triggers", [])})

layers = ["axiom"] + list(reg.get("layers", {}).keys())
doc = {"generatedFrom": "taxonomy/rules.yaml", "count": len(rules),
       "layers": layers, "rules": rules}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(doc, open(OUT, "w"), indent=2)
print(f"wrote {OUT} ({len(rules)} rules across {len(layers)} layers)")
