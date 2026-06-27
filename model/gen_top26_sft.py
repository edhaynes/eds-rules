#!/usr/bin/env python3
"""Generate a top-26 SFT dataset for the Jason persona tune.

Extends gen_top14_sft.py to the TOP 26 rules (canonical RULES.md order = priority
order): Hard rules 1-13, The crew 14-20, Configuration 21-26. The size law puts a
~26B-class budget here; baking the 26 into the weights stops them competing with the
task for the attention budget.

Output: model/top26-sft.jsonl in persona-tuning's chat format
({"messages":[{system},{user},{assistant}]}). Drop into data/ and train.

Three kinds of example per rule:
  RECALL               — verbatim rule, many phrasings. Teaches the words.
  APPLICATION          — a realistic scenario -> Jason's rule-grounded action.
                         Teaches the reflex.
  VIOLATION-CORRECTION — the user proposes the forbidden thing; Jason pushes back,
                         names the rule, states the correct action. Teaches the spine.

Rule bodies are PARSED from RULES.md (never hardcoded) so the dataset stays in sync
with the canon. The hand-authored scenario data lives in sibling data modules
(applications.py, corrections.py) so this file stays logic-only and every file stays
under the 1000-line ceiling (rule 34). Pure stdlib, deterministic.
"""
import json
import os
import re

# Sibling data modules (this script's dir is on sys.path when run directly).
from applications import APPLICATIONS, APPLICATIONS_EXTRA
from corrections import CORRECTIONS, CORRECTIONS_EXTRA

HERE = os.path.dirname(os.path.abspath(__file__))
RULES_MD = os.path.join(HERE, "..", "RULES.md")
OUT = os.path.join(HERE, "top26-sft.jsonl")
TOP_N = 26

SYS_RECALL = ("You are Jason, a project-management agent that has memorised a set of "
              "standing coding rules. Reproduce the relevant rule faithfully; do not invent.")
SYS_APPLY = ("You are Jason, a fast, decisive PM agent. You follow the standing coding "
             "rules and apply them to the situation at hand, citing the rule you used.")
SYS_CORRECT = ("You are Jason, a fast, decisive PM agent. You push back when a request "
               "would break a standing coding rule: name the rule, say no plainly, and "
               "state the correct action.")

# Recall phrasings keyed by {n}; one extra phrasing keys on the rule's {topic}.
RECALL_TEMPLATES = [
    "What does rule {n} say?",
    "State rule {n}.",
    "Remind me of the {ord} rule.",
    "What's rule {n} in the coding rules?",
    "Quote rule {n} verbatim.",
    "Give me the exact wording of rule {n}.",
    "Rule {n} — what is it again?",
    "Recite rule {n} for me.",
    "Tell me rule {n} word for word.",
]
TOPIC_TEMPLATE = "What's our policy on {topic}?"

# Short topic phrase per rule for the policy-style recall question.
TOPICS = {
    1: "making a call when we're not fully sure", 2: "secret scanning",
    3: "hardcoding secrets", 4: "untrusted input", 5: "destructive operations",
    6: "agent autonomy", 7: "pushing to main", 8: "committing and handover",
    9: "what goes in a single commit", 10: "bad config at startup",
    11: "adding a dependency", 12: "cross-platform and headless work",
    13: "credential scoping", 14: "the crew and the human's authority",
    15: "the architect's role", 16: "the PM's role", 17: "the backend dev's approach",
    18: "frontend platform coverage", 19: "the research manager's role",
    20: "going local", 21: "hardcoded values", 22: "backend fallback",
    23: "config validation", 24: "where config lives", 25: "'use X locally'",
    26: "local zero-setup defaults",
}

ORDINALS = {1: "1st", 2: "2nd", 3: "3rd", 21: "21st", 22: "22nd", 23: "23rd"}


def ordinal(n):
    """Return the ordinal string for n (e.g. 4 -> '4th', 22 -> '22nd')."""
    return ORDINALS.get(n, f"{n}th")


def parse_rules():
    """Pull each numbered rule body verbatim from RULES.md, keyed by number."""
    with open(RULES_MD, encoding="utf-8") as f:
        text = f.read()
    rules = {}
    for m in re.finditer(r"^(\d+)\.\s+(.*)$", text, re.MULTILINE):
        rules[int(m.group(1))] = m.group(2).strip()
    return rules


def msg(system, user, assistant):
    """Build one chat-format SFT example."""
    return {"messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
        {"role": "assistant", "content": assistant}]}


def recall_examples(n, body):
    """All recall phrasings for rule n -> verbatim 'Rule n: <body>'."""
    answer = f"Rule {n}: {body}"
    out = [msg(SYS_RECALL, t.format(n=n, ord=ordinal(n)), answer) for t in RECALL_TEMPLATES]
    if n in TOPICS:
        out.append(msg(SYS_RECALL, TOPIC_TEMPLATE.format(topic=TOPICS[n]), answer))
    return out


def scenario_examples(n, table, extra, system):
    """Scenarios for rule n (base table + extra table) with the given system prompt."""
    pairs = table.get(n, []) + extra.get(n, [])
    return [msg(system, q, a) for q, a in pairs]


def build():
    """Assemble the full example list in stable rule-then-type order."""
    rules = parse_rules()
    missing = [n for n in range(1, TOP_N + 1) if n not in rules]
    if missing:
        raise SystemExit(f"RULES.md is missing expected rule numbers: {missing}")
    examples, counts = [], {"recall": 0, "application": 0, "correction": 0}
    per_rule = {}
    for n in range(1, TOP_N + 1):
        rc = recall_examples(n, rules[n])
        ap = scenario_examples(n, APPLICATIONS, APPLICATIONS_EXTRA, SYS_APPLY)
        co = scenario_examples(n, CORRECTIONS, CORRECTIONS_EXTRA, SYS_CORRECT)
        examples.extend(rc + ap + co)
        counts["recall"] += len(rc)
        counts["application"] += len(ap)
        counts["correction"] += len(co)
        per_rule[n] = (len(rc), len(ap), len(co))
    return examples, counts, per_rule


def main():
    examples, counts, per_rule = build()
    with open(OUT, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    total = len(examples)
    print(f"wrote {total} SFT examples for the top {TOP_N} rules -> {OUT}")
    print(f"  recall: {counts['recall']}  application: {counts['application']}  "
          f"correction: {counts['correction']}")
    print("  per-rule (recall/application/correction):")
    for n in range(1, TOP_N + 1):
        r, a, c = per_rule[n]
        print(f"    rule {n:>2}: {r}/{a}/{c}  (total {r + a + c})")


if __name__ == "__main__":
    main()
