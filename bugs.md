# Bugs

Known bugs for the eds-rules repo and the book manuscript.

## B1 — Post-F5 narrative seams (body sentences strained by the reorder)
- **Status:** Completed, 2026-06-12 (pending commit) — all three seams rephrased: Ch2 R30 tail now "configuration thread," Ch2 R31 opener now invokes "the configuration rules" by theme, Ch1 transition leads with the decision doctrine.
- **Observed:** 2026-06-12, during the F5 importance reorder (body text was
  frozen by instruction; these sentences now read against the new order)
- Ch. 2, new Rule 30 tail: "That's the configuration half of this chapter in
  one sentence" — still numerically true but the halves now interleave.
- Ch. 2, new Rule 31 opening: "This rule is where the previous eight stop
  being hygiene" — its eight predecessors are no longer the config-hygiene
  run the sentence described.
- Ch. 1 transition paragraph: lists the second half as "five fixed roles,
  one human, and the decision doctrine that binds them" — accurate, but the
  doctrine now *leads*; one-clause polish available.
- Fix in a single editorial pass after the F5 commits land (needs Eddie/Iris
  judgment — body text, not mechanical).

## B2 — Powell rule misdefined in Ch3 + Ch5 synopses (Edith, cold grade 2026-06-12)
- **Status:** Completed, 2026-06-12 (pending commit) — both synopses now state the real rule: get/gather 90% of the information, then decide; below 90%, ask the human.
- Ch3 synopsis: "the Powell rule: you break it, you own it"; Ch5 synopsis:
  "the Powell rule holds: you touched it, you own it." That is the Pottery
  Barn rule — a different Powell doctrine. The flagship rule is *get 90% of
  the information, then decide*. Worst defect in the book; both openers.

## B3 — Rule 46 ignores rootless Docker (Reddit-test exposure)
- **Status:** Completed, 2026-06-12 (pending commit) — Rule 46 body now acknowledges rootless Docker (20.10, 2020) and holds the line: opt-in retrofit vs. rootless/daemonless by construction; secure path must be the default path.
- "Docker's insecure daemon" argues against Docker's classic architecture as
  if it were the only one; rootless mode has shipped since 20.10 (2020).
  Fix: acknowledge it and state why Podman still wins (rootless by
  construction vs. opt-in).

## B4 — RULES.md drift: repo rule 53 vs book Rules 62–63
- **Status:** Completed, 2026-06-12 (pending commit) — rule 53 now carries the verbatim-disclosure-to-owner exception (SHA, file, exact string, leak response only); repo and book describe the same rule.
- Repo says "never copy a secret anywhere," full stop; the book correctly
  carves the verbatim-disclosure-to-owner exception. Repo short form is
  incomplete — drift is a bug.

## B5 — Appendix E overclaims the open-weights tune
- **Status:** Completed, 2026-06-12 (pending commit) — table row honest (days to weeks / Medium-high, gates still carry process discipline), body paragraph caveats that tuning shapes style and defaults, not procedural discipline.
- "A weekend and a good dataset" / robustness "High" overstates what LoRA
  can instill (agentic process discipline is not a weekend). Soften to honest
  ranges; the Reddit test applies.

## B6 — Minor grade findings (one pass, low severity)
- **Status:** Open — synopsis sub-item Completed, 2026-06-12 (pending commit), in the floor-fix sprint; remaining items below still open.
- ~~Ch3 synopsis claims function-size limits already established (they are
  Ch4, Rule 79).~~ Done 2026-06-12: synopsis now claims only Ch2's file
  ceilings (500/800/1000). Rule 64 gauge + Rule 69 funnel diagrams are decoration —
  cut or earn. Rule 13 sprint-lanes diagram may be cramped at trim — check
  in printed proof. Frustration #1 (hallucinated *library* APIs, not just
  tools) never named where the arriving reader looks — add the named
  incident to Rule 50's body or Ch2 search-first.

## B7 — Invalid Jason Llama8B model name in opencode config
- **Status:** Open — Opencode validation reports `ollama/jason-llama8b` as an invalid model.
- **Observed:** When running Opencode with `opencode.json` (or `project_manager/opencode.json`), the system fails to start due to the unrecognized model name.
- **Fix:** Install the correct model (e.g., `ollama pull jason-llama8b`) or update the config to a valid model name.

## B8 — Tool call validation error for repo_browser.open_file via comment channel
- **Status:** Open — error occurs when attempting to open a file using a tool call that includes a channel tag (`repo_browser.open_file<|channel|>commentary`), which is rejected because the tool is not listed in request.tools.
- **Observed:** The system returns a JSON error:
  ```json
  {"message":"Tool call validation failed: tool call validation failed: attempted to call tool 'repo_browser.open_file<|channel|>commentary' which was not in request.tools","type":"invalid_request_error"}
  ```
- **Fix:** Remove the channel tag and call `repo_browser.open_file` directly, ensuring the tool is included in the request's tools list.

## B9 — Tool call validation error for repo_browser.exec
- **Status:** Open — error occurs when attempting to call the `repo_browser.exec` tool, which is not listed in request.tools.
- **Observed:** The system returns a JSON error:
  ```json
  {"message":"Tool call validation failed: tool call validation failed: attempted to call tool 'repo_browser.exec' which was not in request.tools","type":"invalid_request_error"}
  ```
- **Fix:** Ensure `repo_browser.exec` is included in the request's tools list before calling, or avoid using it if not supported.

## B10 — Failed to parse tool call arguments as JSON
- **Status:** Open — tool call fails when arguments cannot be parsed as valid JSON.
- **Observed:** System returns error:
  ```json
  {"message":"Failed to parse tool call arguments as JSON","type":"invalid_request_error"}
  ```
- **Fix:** Validate and correctly format tool call arguments as proper JSON before invoking the tool; add input validation.

## B11 — Jason model configuration fixed
- **Status:** Completed — the Jason model reference in both `test/opencode.json` and `test/project_manager/opencode.json` has been updated to the installed model name `jason:latest`.
- **Observed:** After the change, Opencode loads without model‑validation errors.
- **Fix:** Updated "model" and "agent.jason.model" fields from `ollama/jason-llama8b` to `jason:latest` in both config files.
