Status: Ready for Claude — 2026-06-12

# Brief: F8 — crew-installation appendix ("install Jason")

Context: Edith's grade (bugs.md/features.md F8): the crew is the book's
differentiator and nothing installs it. Appendix C installs RULES.md;
Rules 12–20 describe personas the reader can't buy.

Deliver: a new Appendix (F, after E) in `book/99-back-matter.md` —
copy-pasteable crew setup:

1. Persona definitions as drop-in `CLAUDE.md` / `AGENTS.md` blocks (the five
   roles, generalized — no private-canon content; the open distillation in
   README.md is the source).
2. Harness wiring per stack: Claude Code (subagents), OpenCode, local
   (Ollama) — Jason coordinates on a fast model, heavyweights as subagents,
   bindings as config never hardcoded.
3. The minimal viable version first (one file, one harness), the full
   version second. Search before building: survey existing high-star
   multi-agent/persona harness configs and adapt patterns; cite what you
   adapt.

Constraints: plain language (audience: newbie AI coders — the rubric's
heaviest weight); everything runnable as pasted; Reddit test (no overclaim
about what personas do); coordinate 99-back-matter.md edits through Jason
(single-file ownership this wave).

Acceptance: a reader with only Claude Code installed gets the five-persona
crew working by paste; build green (`python3 book/build.py`).
