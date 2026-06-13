Status: Not Implemented — design draft 2026-06-13 (awaiting Eddie sign-off + hardware/cloud answers)
Author: Jason-eds (architectural decider) with Claudius-eds

# Persona model fleet — base model + training approach per persona

Goal: a trained/bound local-first model per persona, tiered by task. This doc
decides, for each persona, (a) the base model + size tier and (b) the *training
approach* — which is the decision that actually matters.

## The principle (read this first — it drives every row)

There are four levers, and most people reach for the wrong one:

1. **Base-model choice** — biggest lever for *capability*. A code-specialized
   model beats a general model at code, full stop. Pick the base by the
   persona's domain before considering any training.
2. **Prompt-bake (system prompt / Way 3)** — the persona, temperament, and the
   100 rules synopsis. *Every* persona gets this. Free, immediate, no GPU.
3. **Fine-tune / QLoRA (Way 2)** — for **stable** behavior you want *ingrained*:
   the rules, decision style, house code-style. NOT for knowledge that changes.
4. **RAG (retrieve at inference)** — for **large, changing** knowledge:
   framework docs (React/Vite), library APIs, the repo's own ADRs.

> **The correction (pushing back on the Claudina instinct):** *don't fine-tune a
> model to "know React + Vite."* Framework knowledge is large and changes every
> few months — fine-tuning bakes in **stale** docs, costs a retrain per version,
> and an 8B still writes mediocre JSX. **RAG over the current docs beats it on
> every axis.** Fine-tune for *your house component style*, not for the framework.

So: **base model for capability, RAG for changing knowledge, fine-tune for the
rules and your style, prompt for the persona.**

## The matrix

| Persona | Role | Tier — base model | Training approach |
|---|---|---|---|
| **Jason** | PM / coordinator | small — **Granite 2B** (fallback Llama 3.1 8B) | **QLoRA** on the 100 rules + decision drills ("given X, what would Eddie decide?") + the Powell-90% behavior. Rules are stable → fine-tune is right. Proven (`jason:latest`). |
| **Claudius** | architect / deep reasoning | heavyweight — **biggest reasoning model available** (cloud Opus, or on Gladius a 70B / reasoning model: QwQ-32B, DeepSeek-R1-distill) | **No fine-tune.** Architecture quality is base reasoning capacity, not Eddie-specific data. Prompt-bake rules + ADR style; **RAG over `docs/adr/`, `plans/`, `CLAUDE.md`** so it reasons in-context with the canon. |
| **Claude** | backend dev | heavyweight — **Qwen2.5-Coder-14B** (~9GB at Q4, fits a 16GB card) — a *code* model, not a generic 12B | Strong code base + prompt-bake rules (tests, config-over-hardcode, OSS-reuse-first) + **RAG over library/API docs**. Optional QLoRA only to ingrain the rules. |
| **Claudina** | frontend | medium — **Qwen2.5-Coder-7B/14B** (a code model; *not* generic Llama 8B) | **RAG over current React/Vite/Tailwind + your component library** + frontend-rules prompt + cross-platform constraint. Fine-tune *only* a small adapter on **your house component patterns**, never the framework. |
| **Brutus** | tester (Python) | small-med — **Qwen2.5-Coder-7B** (16GB card, fast; runs the suite) | Prompt-bake the testing rules (contract-first, 100% line+branch, no network in unit tests) + few-shot. Optional QLoRA on the testing discipline. Speed > size here. |
| **Linda** | research / GTM | cloud — **Groq GPT-OSS-120B** (fast, web-capable) | **None.** Her value is breadth + speed + live web, not ingrained knowledge. Stock + GTM-brief prompt + web/search tools. |

## Tiers → hardware (the dependency)
- **small (≤2-3B):** Mac / iPhone / iPad — Jason, runs anywhere.
- **medium (7-14B Q4):** the RTX 5080 16GB box ("Brutus") or a Mac — Claude, Claudina, Brutus.
- **heavyweight (32-70B+):** **only Gladius** (128GB) — Claudius local, or cloud.
- **QLoRA training:** comfortable for ≤8B on 16GB; a 14B fine-tune wants Gladius.

## Build recipes (reusable)
- **Fine-tuned persona** (Jason, optional others): extend `model/make-rules-model.sh`
  + the Way-2 dataset generators (per-rule drills + persona-specific pairs) → QLoRA → GGUF → Ollama. One `make-persona-model.sh PERSONA=jason`.
- **RAG persona** (Claudius, Claude, Claudina): a doc-index build (embed the
  framework docs / repo docs) + a retrieval wrapper in the persona's runtime. No GPU training.
- **Prompt-only** (Linda, baseline for all): `PERSONA_FILE=` system-prompt bake (exists).

## Open questions (these refine the heavyweight rows — Powell: I need these to lock them)
1. **Is Gladius coming back?** It's the only box that trains a 14B or runs a 32-70B.
   While it's shelved, the heavyweight tier (Claudius local, a 14B Claude fine-tune)
   is blocked — those personas stay cloud or capped at what the 16GB box runs.
2. **Local-only or hybrid?** Should Claudius/Claude be fully local, or is it fine for
   the *heavyweights* to stay cloud (Opus) while the trained-local fleet is Jason +
   Brutus + Claudina + Claude-backend? This decides whether I design a local 32-70B
   or just bind those seats to cloud.
3. **Brutus vs Gladius / canon:** Ep90 uses Brutus (RTX 5080); the persona canon marks
   Brutus decommissioned (→ Gladius). Confirm the real tester box before I target it.

## Recommended first chunk (if approved)
Start where it's proven and unblocked: **Jason on Granite 2B** (QLoRA, the Ep90 plan)
+ **Brutus/Claudina/Claude as Qwen-Coder + RAG** on the 16GB box. Defer Claudius's
heavyweight until the Gladius/cloud question is answered.
