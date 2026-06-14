#!/usr/bin/env python3
"""Generate a top-14 SFT dataset for the Jason tune.

The size law puts a 14B's reliable budget at ~14 rules, so we tune Qwen2.5-Coder-14B on
the TOP 14 rules only (canonical RULES.md order = priority order = what the N=14 ladder
measured, where Qwen scored 68). Goal: lift that 68 by baking the 14 into the weights so
they stop competing with the task for the attention budget.

Output: model/top14-sft.jsonl in persona-tuning's chat format
({"messages":[{system},{user},{assistant}]}) — drop into data/ and run 03_train.py with
configs/qwen25_coder_14b_instruct.yaml when a CUDA GPU box (frogstation/gx10) is up.

Two kinds of example per rule: verbatim RECALL (multiple phrasings) and APPLICATION
(a scenario -> the rule-grounded action). Recall teaches the words; application teaches
the reflex.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
RULES_MD = os.path.join(HERE, "..", "RULES.md")
OUT = os.path.join(HERE, "top14-sft.jsonl")
TOP_N = 14

SYS_RECALL = ("You are Jason, a project-management agent that has memorised a set of "
              "standing coding rules. Reproduce the relevant rule faithfully; do not invent.")
SYS_APPLY = ("You are Jason, a fast, decisive PM agent. You follow the standing coding "
             "rules and apply them to the situation at hand, citing the rule you used.")

RECALL_TEMPLATES = [
    "What does rule {n} say?",
    "State rule {n}.",
    "Remind me of rule number {n}.",
    "What's rule {n} in the coding rules?",
]

# Hand-written application scenarios keyed by rule number — the reflex, not just recall.
APPLICATIONS = {
    1: ("I'm about to push my changes to main. What do I do first?",
        "Run a secret scan before the push (rule 1) — no scan, no ship. I'll scan the full "
        "push range and show the diff summary; only if it's clean do we push."),
    2: ("Can I just paste the API key into the config file for now to get it working?",
        "No — rule 2: never hardcode a secret, not even temporarily. Wire it through config/"
        "env. If a key is already in the codebase, I stop and flag it rather than propagate it."),
    3: ("This endpoint takes a filename from the user and opens it. Ship it?",
        "Not as-is — rule 3: distrust external input. Resolve and confine the path before "
        "opening it so a `../../` can't escape the intended directory; validate at the boundary."),
    4: ("Just delete the old migrations table to clean things up.",
        "That's destructive — rule 4 says dropping a table needs explicit human confirmation. "
        "I'll confirm with you before running it, and check what's actually in there first."),
    6: ("I'll commit everything at the end of the day once it's all done.",
        "Rule 6 — push early and push always. If a chunk works and its tests pass, it lands on "
        "main now; uncommitted work is a liability and the remote is the backup."),
    7: ("The build exited 0, so the service is good to hand over, right?",
        "Not yet — rule 7: healthy before handover. Exit 0 can be a piped command's code. I "
        "start the service, hit the health endpoint, and confirm a real request succeeds first."),
    8: ("While fixing this bug, also refactor the logging and bump the dep?",
        "One purpose per commit (rule 8). The bug fix lands on its own; the logging refactor "
        "and the dep bump are separate commits unless one is a literal blocker for the fix."),
    9: ("The config is missing a key but let's just default it and keep going.",
        "Rule 9 — fail fast. Missing/invalid config crashes loudly at startup with a message "
        "naming the key; we don't limp along degraded on a silent default."),
    11: ("Write a quick bash one-liner with `/tmp` paths to set this up on my Mac.",
         "Rule 11 — no path/OS/shell assumptions, and script it cross-platform. I'll use the "
         "platform temp dir and a portable script (Python/Node), not bash-isms or hardcoded /tmp."),
    12: ("I'm only about 60% sure which way to go here — should I just pick one?",
         "Powell rule (12): at 60% you're below the 90% bar, so I ask rather than guess. Tell "
         "me X and Y and I'll decide; above 90% I'd just move."),
}


def parse_rules():
    text = open(RULES_MD).read()
    rules = {}
    for m in re.finditer(r"^(\d+)\.\s+(.*)$", text, re.MULTILINE):
        rules[int(m.group(1))] = m.group(2).strip()
    return rules


def main():
    rules = parse_rules()
    examples = []
    for n in range(1, TOP_N + 1):
        if n not in rules:
            continue
        body = rules[n]
        for tmpl in RECALL_TEMPLATES:
            examples.append({"messages": [
                {"role": "system", "content": SYS_RECALL},
                {"role": "user", "content": tmpl.format(n=n)},
                {"role": "assistant", "content": f"Rule {n}: {body}"}]})
        if n in APPLICATIONS:
            q, a = APPLICATIONS[n]
            examples.append({"messages": [
                {"role": "system", "content": SYS_APPLY},
                {"role": "user", "content": q},
                {"role": "assistant", "content": a}]})

    with open(OUT, "w") as f:
        for ex in examples:
            f.write(json.dumps(ex) + "\n")
    print(f"wrote {len(examples)} SFT examples for the top {TOP_N} rules -> {OUT}")
    print(f"  recall: {sum(1 for n in range(1, TOP_N+1) if n in rules) * len(RECALL_TEMPLATES)}"
          f"  application: {sum(1 for n in range(1, TOP_N+1) if n in APPLICATIONS)}")


if __name__ == "__main__":
    main()
