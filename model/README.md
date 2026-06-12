# Run the 100 rules as a model

Two ways to get a Llama that knows these rules — matching the foreword's
"three ways to bend a model" (the first, training from scratch, is for labs).

The end goal, in priority order:

1. **Violation detection** — show it an action or a diff, it names the rule
   being broken and quotes it.
2. **Attribution** (text/situation → rule number) — the skill violation
   detection is built on.
3. **Verbatim recall** (number → rule text) — table stakes.

## Way 3 (start here): bake the rules into a system prompt

Anything that runs Ollama can do this in about two minutes — no GPU, no
training:

```bash
cd model
./make-rules-model.sh
ollama run eds-rules-llama
```

The script pulls `llama3.1:8b` (~5 GB), writes a Modelfile whose system
prompt carries the full `RULES.md` plus a recall / attribution / violation-
detection job description, pins `temperature 0` (Ollama's 0.8 default
paraphrases rules the model knows cold), and creates the model. Variables:
`BASE_MODEL`, `MODEL_NAME`, `RULES_FILE` — point `RULES_FILE` at your own
fork's rules and the same script builds *your* rules model.

Honest trade-offs, measured on the script's own smoke tests: violation
detection works out of the box (it caught "I'll hardcode the API key and
commit it" and quoted the right rule), but **number attribution is shaky** —
asked for rule 5, the prompt-baked 8B answered with rule 4's text. An 8B
reading a 100-rule prompt miscounts; precise number↔rule mapping is exactly
what fine-tuning fixes (way 2 measured 10/10). The rules also ride along as
~4k prompt tokens on every request, and very long sessions dilute
instruction-following — which is why the rules lean on hooks and gates that
hold even when the model drifts.

## Way 2: fine-tune the rules into the weights (the recipe we ran)

We QLoRA-tuned `Llama-3.1-8B-Instruct` on this exact corpus (2026-06-12, on
a single DGX Spark-class unified-memory box). Recipe that survived contact
with reality:

- **One rule = one chunk.** Split the 100 numbered rules into per-rule
  training targets, not section-sized blobs.
- **Dataset ≈ 1,550 pairs** from four generators: LLM-written lookup
  questions (questions only — answers are always the verbatim rule text,
  never LLM output), fixed recite phrasings, cloze (mask-and-restore), and
  **deterministic number drills** — five "What does rule N say?" variants
  plus reverse text→number drills per rule. The drills are the load-bearing
  part: without them the model recalls text perfectly while mismapping
  numbers.
- **QLoRA r=16/α=32, 3 epochs, lr 2e-4, 4-bit base, ~26 min** on a GB10.
- **Gate on open-ended recall, not loss.** Token accuracy ≈95% looked
  identical on runs that passed and failed recall. The gate that means
  something: sample rules, ask cold "What does rule N say?", check verbatim
  containment.
- **Serve-side**: bake the training-time system prompt into the Modelfile
  and pin `temperature 0` — both silently degrade recall if forgotten.

Measured (10-rule sample, greedy): **forward recall 10/10 verbatim;
reverse text→number 6/10**. Reverse mapping and violation detection are the
active frontier — the next dataset revision adds violation-scenario
training pairs (described action → "this violates rule N: …"), since
noticing broken rules is the model's actual job, not recitation parlor
tricks.

Base weights note: Meta's Llama 3.1 license requires derivative weights to
keep "Llama" in the name; the ungated `unsloth/Meta-Llama-3.1-8B-Instruct`
mirror avoids the HF token dance. Tooling: Hugging Face PEFT/TRL or any
QLoRA harness; export GGUF q4_k_m via llama.cpp and `ollama create`.
(See also the book's Appendix E.)

## The miss loop: violations as training data

A violation that sneaks past the model is a bug, and bug fixes ship with a
regression test (rule 71). The loop:

1. **File it** — every missed violation goes in a ledger (date, the exact
   statement that slipped past, a distinctive snippet of the rule that
   should have fired). Snippets, not numbers: numbers move when the rules
   are reordered; text survives.
2. **Train on it** — ledger entries convert mechanically into grounded
   training pairs ("Stop — that violates rule N. <verbatim rule>") for the
   next fine-tune.
3. **Gate on it forever** — every past miss is replayed against every new
   model version; one regression fails the gate. The ledger only grows.

## Audit your sessions

`audit-session.py` (stdlib-only, any Ollama judge) scans an AI-coding-session
transcript — Claude Code `.jsonl` or plain text — against the rules and
emits `findings.yaml`: violations in the ledger schema above, **proposed new
rules** for frictions the 100 don't cover (each must name a consolidation
candidate — the count is fixed), and a per-rule violation histogram.

```bash
python3 model/audit-session.py \
    --log ~/.claude/projects/<project>/<session>.jsonl \
    --model llama3.1:8b
```

Run it over enough sessions and the histogram answers the question every
rules document should fear: *which rules actually catch things, and how many
do you really need?* The cumulative-coverage curve from real audits — not
opinion — is how this list earns its 100 slots or loses them.

## Which way should you pick?

| | Way 3 (prompt) | Way 2 (fine-tune) |
|---|---|---|
| Time | 2 minutes | an afternoon |
| Hardware | anything running Ollama | one capable GPU / unified-memory box |
| Robustness | dilutes over long sessions | survives long sessions |
| Your own rules | `RULES_FILE=...` | regenerate dataset, retrain |
| Updates when rules change | re-run script (seconds) | retrain (~1 hour) |

Start with way 3 today; graduate to way 2 when drift annoys you.
