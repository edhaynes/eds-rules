Status: Not Implemented

# PLAN — Capstone chapter: "Pulling It Together" (F7, Bard zero-trust architecture)

Author-date: 2026-06-12. Scopes features.md F7 (absorbs F3 zero-trust; absorbs the
Squawk Box half of F4). Source repo inspected read-only at
`~/projects/VibeLLamaPhonograph/bardLLMPro/` (v1.5.2) and
`~/projects/claudeTalk/` (Squahk, v0.6.x TestFlight). Eddie's question: *where are
we now, and where would we like to be to publish?*

---

## 1. Where we are now — honest inventory

The chapter's entire credibility rides on the RUBRIC.md Reddit test: a technical
crowd sniffs out a fraud in two seconds. So the inventory below is split with the
same `[shipped]` / `[design-only]` discipline the repo itself uses in
`docs/SECURITY_AND_INTEGRATION.md` ("Honesty contract: every claim is marked
shipped or roadmap; when in doubt it under-claims"). The chapter inherits that
convention verbatim.

### Shipped — exists in code, tested, in CI (v1.0.0 → v1.5.2)

| Claim | Evidence in repo |
|---|---|
| TLS-default fabric: Router + Registry + UBI-9 Podman agent (llama.cpp or echo behind a swappable `InferenceEngine`) | `router/`, `registry/`, `agent/`, `agent/Containerfile` (multi-stage, non-root, default-deny demo flags); CHANGELOG v1.0.0 |
| Per-hop JWT, zero network-location trust — every hop (client→router, router→agent, agent→registry, broker link) verifies the token on its own merits | hop table in `docs/SECURITY_AND_INTEGRATION.md §1`; `common/auth.py` `TokenVerifier` seam |
| Frozen wire contracts, contract-first | `contracts/` (JSON Schema + 4 OpenAPI files + broker-link schema); contract tests pin code to the files |
| One config layer, fail-fast | `common/config.py` — sole `os.environ` reader; missing/short `BARDPRO_JWT_SECRET` is a startup crash (min 32 bytes since v1.5.2, found by live pentest, bug #58) |
| Broker transport ("LokNet"): outbound-only WebSocket, Router as single public front door, Registry needs no public bind | v1.1.0–v1.2.1; real-socket mesh-free smoke (`scripts/smoke_broker.py`) runs in CI |
| 100% line+branch coverage, enforced | `pyproject.toml` `--cov-branch --cov-fail-under=100` IS the CI gate; **257 tests collected at v1.5.2** (160 at the v1.0.0 MVP tag; README's "208" is stale — see gaps) |
| CI: lint + tests on ubuntu+macos, gitleaks over full history, multi-arch agent-image builds | `.github/workflows/bardpro-ci.yml` (since v0.13.0) |
| Adversarial pentest as a CI regression suite (~23 attacks held defended) | `tests/test_security_pentest.py` (v1.5.2); independent audit doc `docs/SECURITY_AUDIT.md` (v1.4.2) |
| ADR discipline | docs/adr/ numbered 0001–0015 (14 files present; ADR-0012 console-stack is referenced in CHANGELOG but not in `docs/adr/` — resolve the count before printing it) |
| Keep-a-Changelog at every bump; README regenerated from scratch, every claim code-verified | `CHANGELOG.md` (35+ entries in 3 days); v0.13.2 entry documents the regeneration discipline |
| Cloud Run deploy recipe — **authored, not executed** | v1.3.0: Containerfile.cloud + parameterized deploy script, `bash -n`/shellcheck clean, never run. Chapter must say "authored, not executed" if mentioned |

### Design-only — direction, not built. The chapter MUST label these roadmap.

| Item | Reality |
|---|---|
| TRUST_MODEL.md v3 (per-entity hybrid-PQ hardware keys, MLS workgroups with per-epoch re-key, HPKE envelopes, encryption-at-rest, bridging) | First line of the file: *"Status: Not Implemented — deferred to v3 (Run); direction only, not an MVP commitment."* `trust/` contains **stubs** coded to `contracts/trust.schema.yaml`, not wired into the data path. The PQ verifier does not exist — only the `TokenVerifier` seam does. |
| "Zero trust of the overlay itself" (Eddie's *like Tailscale, but Tailscale isn't inside the boundary* positioning) | **Partially true today, fully true only in v3.** Shipped: per-hop authentication means a Tailscale/LAN packet earns nothing — that is real and demonstrable. Not shipped: E2EE past relays, per-entity identity, workgroup authorization. The honest sentence is "the overlay is treated as untrusted transport *for authentication* today; the full least-disclosure model is the v3 design." |
| Plugin SDK / plugin platform | v2 direction (root features #66 Hub plugin platform, #68 plugin catalog incl. SSH/SCP). **No SDK code exists, no seam in the codebase is named "plugin."** What exists is the de-facto plugin contract: frozen wire contracts + JWT + the swappable `TokenVerifier`/`InferenceEngine` seams. |
| Squawk Box as a Bard plugin | The app exists and ships (claudeTalk repo; product name **"Squahk"**, v0.6.x on TestFlight; E2EE rooms are called "Squahk Boxes"). It already speaks JWT + `POST /v1/message` against the live contract as the **v1 example client** (ADR-0011). It is integrated as a *client*, not via a plugin SDK — because the SDK doesn't exist. |
| Profile B (enterprise console, strict onboarding), ssh CLI tab, remote spawn, Valkey control plane, mesh | All v2 per ROADMAP.md; some have ADRs (0004, 0007, 0008, 0010), none have product code beyond the parked Flutter/console scaffolds. |

### One naming discrepancy to surface now

Eddie's ruling names the plugin **"Squawk Box"**; the shipping product is
**"Squahk"** (App Store identity `com.edhaynes.squahk`), and "Squahk Boxes" are
the E2EE rooms inside it. The book can use whichever name Eddie wants — but book
and app should not disagree in public. **Decision needed from Eddie:** chapter
says "Squawk Box" and the app renames, or the chapter uses the app's real name.

---

## 2. Where we need to be to publish the chapter

Eddie's claim for the chapter: *"90%+ rubric quality out of the box, functionally
correct throughout; the only gaps were mandatory MVP features I forgot to spec."*

### What substantiates it today

- **100% line+branch coverage enforced from v0.2.1 onward** — not aspirational,
  the CI gate fails under 100%. 160 tests at MVP, 257 at v1.5.2.
- **Contract-first**: contracts frozen before lanes started; contract tests pin
  the code; v1 changes were additive-only.
- **The v1.2.1 receipt** (quote it in the chapter): *"No real bug surfaced under
  real sockets vs TestClient. The slice-1/2 broker code behaved exactly as
  designed end-to-end."* That is "functionally correct out of the box," in the
  project's own changelog, written before this book chapter existed.
- **The bug ledger matches the claim's shape**: #51 (UBI9 aarch64
  libcurl-minimal conflict — platform/environment, caught by the
  verify-on-real-hardware rule), #53 (plain-HTTP gate — post-demo *hardening
  nobody specced*), #54 (broker link-hijack — found by a deliberately
  commissioned audit), #58 (JWT min length — found by a live pentest). Delivered
  features did not come back broken; the findings were unspecced requirements
  surfaced by the inspection discipline itself. That's the Powell-rule lesson
  the chapter draws.
- **ADRs + CHANGELOG + regenerated READMEs** give the chapter citable receipts
  for every decision it narrates.

### What would be dishonest to imply — and the gaps to close

| # | Gap | Why it matters | Effort |
|---|---|---|---|
| G1 | **No RUBRIC.md / recorded rubric grade exists in bardLLMPro.** "90%+ on the rubric" currently has no graded artifact behind it — the Reddit test fails on the chapter's headline claim. | Either (a) write the project rubric and have Edith grade v1.5.2 cold, citing the score, or (b) rephrase the claim as what's provable: 100% enforced coverage, zero delivered-feature regressions, audit/pentest findings all in unspecced territory. Recommend (a) — it's the book's own medicine. | ~½ sprint (rubric + cold grade) |
| G2 | **Squawk Box is a client, not a plugin; the plugin SDK has no code and no named seam.** | Saying "the first plugin" overclaims. Fix: a short **plugin-contract doc sprint** in bardLLMPro that names the seam (frozen contracts + JWT + verifier/engine interfaces) as the v1 plugin contract, with Squawk Box as integration #1 against it — then the chapter's sentence is true: "the plugin contract is the frozen API; the SDK that wraps it is v2." SSH / remote-desktop plugins are catalog **roadmap**, presented as such. | ~1 sprint (docs + contract naming, no code), OR pure honest-labeling in the chapter at zero repo cost |
| G3 | **Stale numbers.** README says 208 tests; tree collects 257; F7's own entry says 160. Version, test count, ADR count (0012 file question) must be frozen-and-verified on the day the chapter is drafted. | One verification pass, quoted with the version it was measured at ("at v1.5.2: 257 tests, 100% line+branch enforced"). | hours |
| G4 | **Security-audit Critical (Maude relay no-auth/plaintext, E2EE paper-only) is a live finding on Eddie's personal infrastructure.** | The chapter must not publish an unfixed vulnerability of a running personal system. Print only findings fixed at press time (#54, #58 — both fixed, both great scars) or generalize. | gating rule, no repo work |
| G5 | **TRUST_MODEL v3 / PQ / MLS are direction.** | Presented as "where the design goes," never as capability. The chapter reuses the [shipped]/[roadmap] tagging inline. | writing discipline only |

Minimum bar to publish: G1 resolved (graded rubric or reworded claim), G2 resolved
(either path), G3 done, G4 enforced. G2's doc sprint is the only bardLLMPro work
worth doing for the book's sake; everything else is chapter-side honesty.

---

## 3. Proposed chapter outline — "Pulling It Together" (`book/ch06.md`)

Posture (Eddie 2026-06-12): a **personal reference architecture**, explicit YMMV
disclaimer mirroring the Red Hat disclaimer — provided as is, do your own
research, not a commercial project. Target **5–7k words**, 9 sections. Rule
references resolve against post-F5 `RULES.md` numbering (F5 is implemented, so
numbers are stable; cite by number + name at draft time).

1. **The claim and the scoreboard.** What got built in how many days, by the
   rules in this book: the fabric, the numbers (tests, coverage gate, CI,
   ADRs), and the precise claim — everything specified shipped correct; the
   gaps were the spec's. Sets the [shipped]/[roadmap] tagging contract with the
   reader. *(Exercises: quality bar / rubric rules; voice & honesty.)*
2. **Freeze the seams first.** Contract-first as the thing that let parallel
   agents build without colliding: `contracts/` before lanes, fakes before
   features, additive-only changes. *(API/contract-first, plan-sizing /
   sprint rules.)*
3. **One config layer or nothing.** `common/config.py` as the only
   `os.environ` reader; fail-fast on the missing secret; "no insecure
   default" as a config decision. *(Ch. 2 configuration rules: one layer,
   validate at startup, no silent fallback, no magic numbers.)*
4. **Trust nothing by location.** The per-hop JWT table; a LAN packet earns
   nothing; cleartext is a fail-fast opt-in that still logs a WARNING.
   *(Ch. 4 trust-boundary and secret-hygiene rules.)*
5. **The overlay is not inside the boundary.** The Tailscale comparison done
   honestly: the mesh is transport, never authorization — and the broker link
   (outbound-only 443, single public front door, private Registry) removes
   even the *need* for the overlay. Today's shipped authn vs the v3
   least-disclosure design, labeled. *(Swappable interfaces; trust-boundary
   rules; honest-labeling discipline.)*
6. **Prove it or it didn't happen.** 100% line+branch as the CI gate, no
   network in unit tests, the real-socket smoke, and the pentest suite as a
   *regression* suite — attacks that stay defended forever. The v1.2.1
   "no real bug under real sockets" receipt. *(Ch. 4 testing rules; green
   before commit; healthy before handover.)*
7. **The institution remembers.** ADRs that supersede rather than edit;
   Keep-a-Changelog at every bump; READMEs regenerated from scratch with every
   claim code-verified; the SECURITY doc's honesty contract. *(Ch. 5 memory
   rules: ADRs, MEMORY.md, README regeneration, plan tracking.)*
8. **Designed for plugins: Squawk Box first.** The plugin contract is the
   frozen API + JWT + the verifier/engine seams; Squawk Box (the walkie-talkie
   app) integrates against it as plugin #1 — push-to-talk to your own fleet —
   and the catalog (SSH, remote desktop, …) is roadmap that the same seam
   already accommodates. *(Swappable-backend, dependency-injection,
   research-before-building rules.)*
9. **The residual failure mode is the spec.** The bug ledger walked honestly:
   #51, #53, #54, #58 — what each would have cost without the rules, and why
   every one landed in unspecced territory. The machine nails what's
   specified; the Powell rule and sprint sizing exist to fix the human. Close
   with where the design goes (v3 trust model, labeled direction) and the
   YMMV disclaimer. *(Powell rule, sprint-sizing, file-everything tracking
   rules.)*

**B&W diagram candidates (pick 3 of 4; existing Mermaid→grayscale pipeline):**
- D1 — Fabric architecture: client → Router → Registry → Agent (container),
  engines behind the seam. (Replaces a page of prose.)
- D2 — Trust-boundary map: the four hops, a JWT-verify checkpoint drawn at
  each arrowhead; the LAN/overlay drawn *outside* the boundary, dashed.
- D3 — Plugin seam: one frozen contract on the left; Squawk Box (solid box),
  SSH / remote desktop (dashed boxes, labeled roadmap) on the right.
- D4 — Crawl/walk/run rings: shipped core, v2 shapes, v3 trust fabric —
  the shipped-vs-roadmap labeling made visual.

**Structural impact (from F7):** new `book/ch06.md`; `build.py` SOURCES list;
`OUTLINE.md` product/structure rows; front-matter "How to read this book"
sentence; back matter untouched (capstone carries no numbered rules, Appendix D
unaffected). Sequence after F6 if F6 lands first is NOT required — the capstone
cites rule numbers already stable post-F5.

---

## 4. Privacy / generalization checklist (public commercial book)

Found in the source docs; none of it ships in the chapter as-is:

- **Hostnames / hardware inventory:** `gx10`, `GB10`, "Mac M5 Max",
  `frogstation`, `gladius` → "a laptop and an ARM GPU workstation." No node
  tables from `ONE_PAGER.md`/`RUNBOOK.md`.
- **Tailnet / overlay specifics:** tailnet node names, "Tailscale owns :8443 on
  the Mac TS IP, so the demo router runs on :9443" → keep the *scar* (the
  overlay owned the port; config rule saved the demo), drop the topology.
  "Tailscale" as nominative comparison is fine; our tailnet's shape is not.
- **Port numbers:** 8443/8444/8081/9443/5173/8080 appear as defaults — fine as
  *example* config values, never as "this is my live infrastructure" facts.
- **Key material / secrets plumbing:** `BARDPRO_TLS_CERT_PATH`/`KEY_PATH`
  examples generalized; Secret Manager secret names and gcloud project/region
  values never quoted (the deploy script already refuses to hardcode PROJECT —
  say so, show nothing). ElevenLabs key rotation (bug #57) only as "a vendor
  API key," if at all.
- **People / outreach:** the Chris Wright demo, `docs/outreach/`, "Red Hat CTO"
  framing — excluded entirely. The book's Red Hat disclaimer already walks
  that line; the chapter must not imply Red Hat saw or blessed any of this.
- **Identifiers:** `com.edhaynes.squahk`, `jason_relay` / `JASON_*` env
  prefixes, `github.com/edhaynes/...` repo paths, persona names inside product
  internals → generalized or omitted.
- **Commercial positioning:** ADR-0015 pricing ($19.99/yr Hub, break-even
  math), POSITIONING.md business model — omitted; the chapter's stated posture
  is *personal reference architecture, not a commercial project*.
- **Live vulnerabilities:** per G4, no unfixed audit finding on running
  personal infrastructure appears in print.

A grep sweep against this list is a named publish gate (below).

---

## 5. Publish gates

1. **Claims verified against repo state on draft day** — version, test count,
   coverage gate, ADR file count (resolve the ADR-0012 question), each quoted
   with the version measured. Any number the repo can't show, the chapter
   can't print.
2. **G1 resolved**: bardLLMPro RUBRIC.md exists and Edith has graded it cold
   (preferred), or the headline claim is reworded to the provable form.
3. **G2 resolved**: plugin-contract naming doc landed in bardLLMPro, or the
   chapter uses the "contract today, SDK v2" honest framing.
4. **Naming ruling from Eddie**: Squawk Box vs Squahk, book and app agree.
5. **Shipped-vs-roadmap audit**: every architectural claim in the draft tagged
   and checked against §1 of this plan (the Reddit test, applied mechanically).
6. **Privacy sweep**: grep the draft against the §4 checklist; zero hits.
7. **Diagrams render B&W clean** through the existing pipeline at 7"×10".
8. **Eddie read-through and sign-off** on posture (YMMV disclaimer present,
   no commercial framing).
9. **Edith cold grade ≥90** for the chapter (rubric protocol: a failing
   chapter caps the book); book publishes only at 95+.

---

Author: Claudius
