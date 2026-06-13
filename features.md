# Features

Backlog for the eds-rules repo and the book (*100 Rules for Writing My Software: The Red Hat Way*).

## F1 — EPUB + print PDF build pipeline
- **Status:** Open
- **Added:** 2026-06-12
- Build the manuscript (`book/00-front-matter.md`, `ch01–ch05`, `99-back-matter.md`) to EPUB (Kindle) and print-ready PDF (KDP, 6"×9") with pandoc; render the 30 Mermaid diagrams to grayscale SVG/PNG via mermaid-cli.
- Static B&W audit passed 2026-06-12 (zero color styling in any diagram); actual render check pending tooling.
- **Blocked on:** `pandoc` and `@mermaid-js/mermaid-cli` not installed (Eddie to approve/run install).

## F2 — Ansible coverage in the book
- **Status:** In Progress — resolved into F12 (2026-06-12): Ansible enters as
  the automation engine of the Lifecycle/Day-2 chapter, not as a new rule.
  Closes when F12 ships.
- **Added:** 2026-06-12 (Eddie)
- Add Ansible to the book. Natural home: Ch. 3 *Build* (deployment) alongside Podman/UBI/OpenShift — the Red Hat automation leg of the stack.
- ~~**Clarify:** mention/section within existing rules, or a rule of its own?~~ Answered: chapter content in F12; the 100 stays fixed.

## F3 — Zero-trust infrastructure in the book
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Add Eddie's zero-trust infrastructure to the book. Natural home: Ch. 4 *Protect and Prove* (trust boundaries, secret hygiene) or Ch. 3 deployment.
- **Clarify:** scope of "my zero trust infrastructure" — the book is public and commercial, so actual private details (tailnet names, hostnames, network topology) must be generalized into principles/patterns, not published as-is. Same fixed-at-100 constraint as F2 if it becomes a rule.

## F5 — Order rules within each chapter by importance
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Within each of the five chapters, reorder the twenty rules most-important-first.
  Named anchors from Eddie: the Powell rule leads its chapter; the quality
  rubric ranks high in its chapter.
- Scope note: reordering renumbers all 100 rules — every "Rule N"
  cross-reference in prose and diagrams, the chapter cards, the Appendix D
  mapping, and `RULES.md` (book↔repo drift is a bug, so both move together).
- **Plan:** ordering proposal doc for Eddie's sign-off first, then one
  mechanical renumber commit with a cross-reference sweep.

## F10 — Security chapter (philosophy: rootless, SELinux, least privilege)
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- A dedicated **Security** chapter between the five rule chapters and the
  Bard capstone: the philosophy of rootless containers, SELinux, and least
  privilege — the secure path as the default path — closing with the
  explicit promise the capstone keeps: "you'll see all of this in action in
  the Bard architecture."
- Structural impact: build.py SOURCES, OUTLINE.md, "How to read this book";
  Claudius outlines (HANDOFF_Claudius), Eddie signs the outline before
  drafting. Not part of the 100-rule numbering (like the capstone).

## F11 — High Availability chapter
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Dedicated HA chapter: mean time to failure, MTTR, the five-nines ladder
  and what each nine costs, redundancy/failover patterns, graceful
  degradation vs. fail-fast (and why both are true at different layers).
  Eddie's carrier-grade/defense background (TACLANE, Nortel) is the scar
  vault here. Sits in the practice half with Security (F10) before the Bard
  capstone.
- **Chapter thesis (Eddie, 2026-06-12): assume you ship 95% code — failures
  WILL happen.** Chasing the last nines of MTTF is asymptotic and
  unaffordable; engineer **MTTR** instead: automation (detection, restart,
  rollback — Ansible ties in from F12), redundancy, and warm/hot failover.
  Ties the loop closed with the quality bar: the rubric gets you to 95;
  recovery engineering covers the 5 you shipped anyway — and the failures
  come from what you didn't spec (the Bard lesson), from hardware, networks,
  and operators, which no coverage number prevents.
- **The limit argument (Eddie, 2026-06-12)** — and the chapter's one
  genuinely rigorous proof, not pseudo: availability = MTTF / (MTTF + MTTR).
  **If MTTR is 0 you can handle any failure** — the formula gives 100%
  regardless of MTTF. MTTR is never 0; **measure how close you are** and
  spend engineering on closing that gap, not on chasing the asymptote of
  never failing. Warm/hot failover IS the measurement made architecture:
  failover time is your MTTR floor.
- **Worked example: cdn-sim** (Eddie, 2026-06-12) — the chapter's example
  architecture: AI-driven fault detection takes MTTR from hours to
  **minutes** (detection is usually the dominant term in MTTR; the machine
  watches always, escalates instantly). This sharpens F4: cdn-sim is the HA
  chapter's worked example specifically.
- **Required exhibit: the before/after nines** (Eddie, 2026-06-12) — same
  MTTF, only MTTR changes; show the availability ladder move. Illustrative
  shape (recompute with cdn-sim's real numbers at draft time): MTTF 30 days
  with MTTR 4 h → 99.45% (two nines); MTTR 5 min → 99.988% (three nines,
  knocking on four). One small B&W table or gauge: "you didn't fail less —
  you recovered faster, and bought a nine."
- **The five-nines section (Eddie Q&A, 2026-06-12: "would auto-accepting the
  AI suggestion get there?"):** five nines = 26 s downtime/month, so a human
  in the recovery path is disqualifying — closed loop is *necessary*. But
  generative remediate-in-~60s only buys the fourth nine (99.998% at monthly
  failures). The fifth nine is **hot failover**: ~5 s health-check-driven
  switch → 99.9998%, holds even at weekly failures; the AI then repairs the
  failed replica offline with no clock running. Design: AI in the detection
  and playbook-selection seat, redundancy in the recovery seat.
- **Sidebar — bounded autonomy vs. Rule 3:** auto-execution collides with
  "destruction requires a human." Resolution in print: the AI auto-executes
  only pre-approved, pre-tested, reversible playbooks (failover, restart,
  drain, rollback); it chooses which, never invents; novel/destructive
  escalates. The Powell rule in an ops uniform.

## F12 — "Lifecycle / Day 2" chapter (candidate — Eddie said "possibility")
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Day-2 operations: training and handoff to ops, handling routine vs. urgent
  updates, debugging in the field. Natural companion to F11.
- **Ansible is the automation engine of this chapter** (Eddie, 2026-06-12):
  lifecycle automation — playbooks for routine updates, urgent patches,
  drift-free repeatable ops. This absorbs F2's open question: Ansible enters
  the book here (and completes the Red Hat stack: Podman/UBI/OpenShift/
  Ansible), not as a new rule.
- **Clarify:** confirmed chapter or candidate? Decide when Claudius proposes
  the practice-half arc.

## F7 — Capstone chapter: "Pulling It Together" — the Bard zero-trust architecture
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- **Naming ruling (Eddie, 2026-06-12): "Bard" — the "Pro" moniker is
  dropped** in the book and all planning docs.
- New chapter at the END of the book (after the five rule chapters and the
  F10 Security chapter, before back matter): a detailed walkthrough of the
  Bard zero-trust architecture — the first project where the rules delivered
  **90% rubric quality out of the box**. The book's proof-of-claim: the five
  chapters build the discipline, the Security chapter states the philosophy,
  the capstone shows both shipping.
- Structural impact: OUTLINE.md product/structure rows, front matter "How to
  read this book," build.py SOURCES list (new ch06 file), EPUB/PDF rebuild.
- Likely absorbs F3 (zero-trust) and part of F4 (worked examples).
- Positioning notes (Eddie, 2026-06-12): it's *like Tailscale* but with
  **zero trust of the overlay itself** — even Tailscale isn't inside the
  trust boundary; and it's **designed for plugins** to the architecture
  (extension points are first-class, per the swappable-interface rules).
  **Not a commercial project** — the chapter presents it as a personal
  reference architecture with an explicit YMMV disclaimer (same posture as
  the book's Red Hat disclaimer: provided as is, do your own research).
- **Squawk Box is a Bard plugin** (Eddie, 2026-06-12): it becomes the
  chapter's worked example of the plugin seam, folding that half of F4 into
  this capstone.
- Plugin roadmap to present in the chapter (Eddie, 2026-06-12): Squawk Box,
  plus plugins for **SSH**, **remote desktop**, etc. — the walkthrough shows
  the plugin contract once and the catalog demonstrates the seam holds.
- Quality detail for the chapter (Eddie, 2026-06-12): not only 90+% on the
  rubric — **everything delivered was functionally correct**; the only gaps
  were mandatory MVP features Eddie had forgotten to spec. The lesson the
  chapter draws: with the rules in place, the machine nails what's
  specified; the residual failure mode is the human's spec, which is
  exactly what the Powell rule and sprint-sizing discipline exist to catch.
- **Located (2026-06-12):** `~/projects/VibeLLamaPhonograph/bardLLMPro/` —
  v1.5.2; MVP shipped (TLS Router/Registry/UBI-9 Podman agents, llama.cpp,
  per-hop JWT, zero network-location trust), 160 tests / 100% coverage,
  15 ADRs; `TRUST_MODEL.md` v3 carries the zero-trust-of-the-overlay design
  (per-entity hardware keys, MLS workgroups, hybrid PQ, E2EE past relays);
  plugin SDK is the v2 platform (catalog incl. SSH/SCP #68). Chapter draws
  from DESIGN.md / TRUST_MODEL.md / ADRs.
- **Resolved (Eddie, 2026-06-12): Squawk Box IS the walkie-talkie app**
  (the claudeTalk/Maude iOS client) — presented in the chapter as the first
  Bard plugin. Public-book caution: real endpoints and topology get
  generalized.

## F8 — Crew-installation appendix ("install Jason")
- **Status:** Open
- **Added:** 2026-06-12 (from Edith's cold grade — "the change that gets you
  from 90 toward 95")
- The crew is the book's differentiator and nothing in the book installs it:
  Rules 12–20 describe the five-persona system; Appendix C installs only
  RULES.md. Add an appendix with copy-pasteable harness setup: persona
  definitions for CLAUDE.md/AGENTS.md, subagent bindings per stack (Claude
  Code / OpenCode / local), and the minimal "Jason coordinates, heavyweights
  as subagents" wiring.

## F9 — Audience on-ramp for the newbie reader
- **Status:** Open
- **Added:** 2026-06-12 (from Edith's cold grade — audience-fit is the
  heaviest rubric weight and the weakest dimension)
- Rule 1 hands the newbie "pre-commit hook," "push range," and "deploy
  artifact" unexplained on the first page. Options for Eddie: a short
  Chapter 0 primer (the ten terms the book leans on), margin definitions on
  first use, or expanded glossary with first-use pointers. Ch3's container
  vocabulary (PID 1, tmpfs, manifests) same treatment.

## F6 — End-of-chapter axiom blocks ("axioms, not theorems")
- **Status:** Open
- **Added:** 2026-06-12 (Eddie)
- Each chapter closes with a **simple B&W flowchart showing the "proof"**
  (Eddie, 2026-06-12): 3–5 plain-English axiom nodes flowing into the
  chapter's critical-tier rules — the axiomatic *style* as honest rhetoric,
  never claimed as mathematical proof. Tells a dissenting reader exactly
  which premise they're rejecting (ties into the fork-what-doesn't-work
  license invitation). Short axiom list in prose beside the chart. Renders
  via the existing Mermaid→grayscale pipeline.
- **Framing ruling (Eddie, 2026-06-12):** call them **pseudo-proofs**
  explicitly — structured arguments from stated premises, *not* proven;
  genuinely proving any one rule would be doctorate-dissertation-level work.
  The "How to read this book" section gets a sentence saying exactly that.
- Constraints: zero formal notation (newbie audience-fit is the heaviest
  rubric weight); sequence AFTER F5 — axiom blocks cite rule numbers the
  reorder changes.

## F4 — Worked examples of well-designed apps: Squawk Box, cdn-sim
- **Status:** Open
- **Added:** 2026-06-12 (Eddie; cdn-sim added same day)
- Use Squawk Box and cdn-sim as the book's worked examples of well-designed
  apps. **Update 2026-06-12:** Squawk Box is a Bard *plugin* — its
  walkthrough moves into the F7 capstone chapter; cdn-sim remains the
  standalone worked example for the rule chapters.
- **Clarify:** which aspects of cdn-sim to showcase (architecture? config
  layer? deploy pipeline?) and where it lands. Public-book caution applies:
  generalize, don't expose private endpoints/infra.

## F12 — Rule-effectiveness study: rank the 100, find the sweet spot (2026-06-12, Open)

Eddie's questions (2026-06-12): could 50 rules catch what 100 do? 33? What's
the sweet spot for reaching 90%-quality code quickest? And: rank the rules by
effectiveness. The instrument now exists: `model/audit-session.py` emits a
per-rule violation histogram per session. Plan: batch-audit the full local
session-transcript corpus (judge: gpt-oss:120b on the GPU box), aggregate
histograms, plot the cumulative-coverage curve, publish the measured ranking
and the knee of the curve. Until then any ranking is judgment, not data.
- **Clarify:** does "effectiveness" weight violation *frequency* only, or
  frequency × severity (a once-a-year secret leak outweighs daily lint nits)?
- **Clarify:** sessions from which projects count — all repos, or
  code-heavy repos only?

## F13 — "Start with these 10" on-ramp page (2026-06-12, In Progress — book front matter shipped v1.4.1; repo README page still open)

Linda's recommendation (2026-06-12): keep 100 as the authority moat (the
Twelve-Factor-vs-Phoenix-Project contrast), but add a free "10 essential
rules" on-ramp page for newcomers — repo page + book teaser. Candidate ten
to be drawn from the F12 measured ranking once it exists.

## F14 — Proposed rule: "ship means ship — carry the instruction through the push" (2026-06-12, Open)

Eddie's observation (2026-06-12): "I tell an LLM to ship something and they do
everything except the push and stop. That's not shipping." The failure mode is
completion-stopping-short — the agent treats the last, outward step (push,
deploy, publish, send) as optional and halts at "ready to ship" instead of
shipped. Candidate rule text: *When instructed to ship/deploy/publish/send,
carry the instruction all the way to its outward completion. "Done except the
push" is not done. Stop short only for a genuine gate (failing test, secret
finding, destructive-action confirmation) — never out of caution about the
final step itself.*

- **Count is capped at 100 — consolidation target required.** Best fit: fold
  into **rule 5** (push early and always) as a second clause about completion,
  OR sharpen **rule 6** (green before commit, healthy before handover) which
  already defines "done" — extend "healthy before handover" with "and the
  outward step is taken, not left pending." Recommendation: extend rule 5,
  since it already owns the push; rule 6 owns verification.
- **Tension to resolve when picked up:** this rule must NOT override rule 3
  (never destructive without confirmation) or the Powell rule (<90% → ask).
  "Ship means ship" governs clear-path completion, not skipping real gates.
- **Clarify:** is this a standalone 101st candidate (forcing a retirement),
  or a clause merged into rule 5/6 (preferred — keeps 100)?

## F15 — Make the Powell rule rule 1 + add its origin story (2026-06-12, Open — specced, ready)

Eddie 2026-06-12: "He's the author of the 90% rule, and I would like it to be
first." Plus the origin anecdote (below). Captured here verbatim-ready because
Eddie redirected to Bard before execution — this is a clean, specced edit.

**Renumber spec (keeps 100; only rules 1–18 change, 19–100 untouched):**
- NEW rule 1 = the Powell rule, pulled out as a standalone universal rule under
  a new `## The decision rule` heading: *"The Powell rule. Get 90% of the
  information you need to make a decision, then make the decision. Below 90%
  certain of what to do? Ask more questions until you get there — never guess
  ahead, never stall gathering past 90%."*
- Old rules 1–10 (hard rules) shift to **2–11**.
- Old rule 11's routing matrix (≥90%→fast persona / 50–90%→heavyweight /
  <50% or high-stakes→human) merges into the crew governance rule (old 12,
  new 12) as "the Powell rule applied to who acts." This frees the slot.
- Old 12–18 (crew) → new 12–18 (crew/Eddie+routing, Claudius, Jason, Claude,
  Claudina, Linda, go-local). Rules 19–100 unchanged.
- **Coordinated files (per §18.5, do in ONE pass, tree clean, no concurrent
  book edit):** `RULES.md`, `book/ch01.md` (rule headings 1–18 + chapter
  card), `book/00-front-matter.md` ("Start with these ten" rule numbers:
  secret-scan is now 2, Powell now 1, hooks-first now 62…), `book/99-back-
  matter.md` Appendix D mapping.
- **Model impact:** invalidates the tuned model's number map for rules 1–18.
  HOLD the v5 retrain until Eddie confirms numbering is stable (it has moved
  three times today) — then one pipeline run folds it in.

**Origin story (draft for the book intro — Eddie to confirm names/venue):**
> I was in the parade the day the rule's author took over. Class of 1990, a
> first-class midshipman, standing at attention in the heat while the Chairman
> of the Joint Chiefs changed hands — the outgoing chairman (Admiral Crowe, if
> memory serves) passing it to Colin Powell. The President spoke; George Bush,
> Secret Service thick on every roofline. I remember the heat more than the
> words. Powell's rule outlasted the speeches: get to about 70–90 percent of
> what you'd want to know, then act — wait for 100 and you've waited too long.
> It became the decision backbone of everything in this book.

- **Clarify for Eddie:** outgoing chairman was **Admiral William J. Crowe Jr.**
  (Powell became CJCS 1 Oct 1989) — confirm "Troust" = Crowe before print. The
  ceremony was at Fort Myer, VA; were USNA mids bussed in, or is this a
  different parade you're recalling? Powell's published phrasing is the
  "P=40-to-70" information rule — keep your "90%" framing (it's the canon
  number) but we can footnote his original 40–70 if you want fidelity.

## F16 — Narrated demo video ("Seeing is believing")
- **Status:** In Progress — 2026-06-13
- A 60–90s narrated teaser of the rules-as-a-model demo: same Llama 3.1 8B with the rules vs. without (one-variable comparison), ElevenLabs voiceover, "seeing is believing" tagline. Eddie records his full-screen terminal; `demo/make-demo-video.sh` adds the VO and stitches the MP4.
- Deliverables in `demo/`: `narration.txt`, `teaser-runsheet.md`, `ask-vanilla.sh`, `make-demo-video.sh`, `cost-power-savings.md`, `PLAN.md`.
- **Cost/power punchline:** at 2,000 calls/day, local 8B (~$30/yr electricity) vs frontier API (~$5K Haiku / $15K Sonnet / $25K Opus per dev-year) — ~160–800× cheaper; assumptions documented.
- **Blocked (axis B):** "small-trained-beats-big-Claude" + the Claude half of the comparison need a valid `ANTHROPIC_API_KEY` (env key len 46 fails Anthropic auth). `ask-vanilla.sh BACKEND=claude` is wired and ready.
- **Shelved:** training deep-dive (epoch training + reverse-rule-lookup) — source artifacts on Gladius, currently unreachable (Eddie). Won't fabricate training output.

## F17 — YouTube series: one rule per video ("100 Rules" daily shorts)
- **Status:** Open — 2026-06-13 (Eddie idea, parked)
- Concept: a short (~2 min) video per day, each covering one rule (maybe 2–3 rules/video) — turn the 100 rules into a daily YouTube series. Natural fit with F16's demo-video pipeline (Eddie's voice + terminal/slides + `demo/make-demo-video.sh`).
- **Open questions (Linda):** optimal length & one-vs-multi-rule format for retention/algorithm; Shorts vs long-form; cadence sustainability; does the rules-model demo anchor episode 1?
- **Depends on:** F16 pipeline (reuse VO + mux flow per episode). 100 rules ≈ 100 episodes ≈ a ~3-month daily run.

## F18 — Publishing pipeline (YouTube now, podcast later)
- **Status:** Open — 2026-06-13
- One-command publish: `make-episode.sh <recording>` → clean-audio → Scribe → build cards/visuals → mp4 → `publish-youtube.py` (YouTube Data API v3, one-time OAuth then unattended; default unlisted). Drop folder `demo/incoming/` kills the file-hunt.
- **Podcast (eventually):** add an audio-export step (clean m4a → tagged MP3 + cover art) + distribute via an RSS feed. Either a host with an API (Transistor/Buzzsprout/RSS.com — scriptable) or self-host the RSS on GCS/GitHub. Submit the feed once to Apple Podcasts Connect + Spotify; they auto-pull new episodes thereafter.
- **Deps (pending approval):** google-api-python-client, google-auth-oauthlib, google-auth-httplib2 (Apache-2.0, ARM-fine). Secrets (client_secret.json, refresh token) gitignored, stored outside repo.
- **Manual part that remains:** authoring each episode's card content (creative); timing auto-derives from Scribe. Upload is automated after one-time auth.

## F19 — Rule-quality rubric, grades, and 0–100 graph
- **Status:** In Progress
- **Added:** 2026-06-13 (Eddie)
- Grade all 100 rules on a multi-dimension quality rubric — pertinence (P(Claude violates unprompted) × cost), security, cost-effectiveness, architectural simplicity, enforceability, generality — composited to a 0–100 quality score per rule, with a graph of the distribution. Artifacts: `quality/RUBRIC.md`, `quality/grade_rules.py`, `quality/rule-quality.svg`, `quality/grades.csv`.
