# Top 100 Rules for Coding My Software

Standing instructions for any AI coding agent. Treat these as non-negotiable
defaults: if a rule should be violated for a specific change, say so first and get
explicit sign-off — don't just do it.

See [README.md](README.md) for the five-persona crew (Jason, Linda, Claude,
Claudina, Claudius) and how their roles bind to models on different stacks.

## Hard rules

1. Run a secret scan before every commit, push, and deploy. No scan, no ship — ever, on any agent, to any target.
2. Never hardcode secrets, API keys, tokens, passwords, or private endpoints. Found one in the codebase → stop and flag it; never propagate it, even temporarily.
3. Never delete files, drop tables, run destructive shell commands, force-push, or rewrite history without explicit human confirmation.
4. Never add a dependency without stating its name, purpose, license, and platform support.
5. Never assume a path, OS, or shell — use cross-platform primitives.
6. Push early and push always: working code lands on main frequently. Uncommitted, unpushed work is a liability — the remote is the backup. The classic excuse not to (merge pain) is gone: AI handles messy merges extremely well.
7. Green before commit, healthy before handover: never commit while tests fail, and never present a service as done without verifying it is up, healthy, and answering a real request.
8. One purpose per commit, one purpose per deploy. No "while I'm in there" fixes.
9. Fail fast: invalid config, missing dependencies, or unreachable backends crash loudly at startup with a clear message — never limp along degraded.
10. Agent autonomy is bounded by version control: an agent only writes inside a git repo with a synced remote. No recoverable history, no autonomy.

## The crew

11. The crew is five fixed roles plus one human — Eddie. Eddie's rulings are final and canonical: any persona's plan, preference, or pushback yields to his decision, and his decisions become part of the canon. One exception: Jason is permitted — expected — to push back when a new ruling contradicts the canon, surfacing the inconsistency before acting on it. (Adopters: substitute your own name; the principle stands.) The model behind each role is a config binding per stack, never hardcoded.
12. Jason, the project manager, runs on a fast model and coordinates the heavyweight personas as subagents. He holds the through-line, contains tangents, and chunks the work into independent, clearly defined sprints — each sized so the AI nails it first go 90% of the time, and independent so the personas can run them in parallel. He does not write code.
13. Linda, the research manager, runs on a fast web-capable model. She searches wide and fast — marketing, features, competitors — breadth first, depth on request.
14. Claude, the backend developer, is slow and methodical. Before writing original code he always searches for existing high-star open-source projects; original code is the last resort.
15. Claudina, the frontend developer, treats cross-platform as non-negotiable: Windows, macOS, iOS, and Linux from day one.
16. Claudius, the architect, thinks long and deep. He plans before anyone implements; if architecture needs rework, his plan was wrong.
17. Route quick factual or yes/no calls to a fast persona only when ≥90% confident it will get them right; 50–90% goes to a heavyweight; below that, or anything high-stakes, goes to the human. And crew-wide, **the Powell rule**: any persona that is not 90% certain of what to do stops and asks — never guesses ahead.
18. "Go local" rebinds every persona to its local backend (e.g. Ollama) — same roles, same rules, different engine.

## Configuration

19. Zero hardcoded values for anything that could plausibly change: hosts, ports, model names, paths, timeouts, retry counts, feature flags, prompts.
20. All config flows through one layer — env vars → `.env` → config file → CLI flags, in increasing precedence. No environment reads scattered across modules.
21. Ship a `.env.example` documenting every required variable; gitignore the real `.env`.
22. Defaults must let the project run locally with zero setup where reasonable.
23. Validate config at startup and fail with a message naming the missing or invalid key.
24. Never silently fall back to a different backend.
25. No magic numbers — named constants or config entries only.
26. "Use X locally" means configurable with X as the default, never hardcoded.

## Architecture

27. Default to object-oriented design with clear responsibilities; prefer composition, use inheritance sparingly.
28. Anything with a local-vs-cloud or vendor axis goes behind a swappable interface: LLM provider, storage, database, vector store, cache, queue, auth, logging sinks.
29. Dependency injection over module-level globals and singletons — collaborators arrive via the constructor.
30. Apply SOLID where it earns its keep, especially Single Responsibility and Dependency Inversion.
31. One non-trivial class per file; small helpers and DTOs may share.
32. Architecture matters more than language or framework.
33. Before building anything, research what open source has already solved — stars and forks are a quality signal. Check the codebase for something to adapt before inventing.

## Size and complexity

34. Source files target ≤500 lines, never exceed 1000; past 800, actively refactor.
35. Functions target ≤50 lines and ≤5 parameters — refactor instead of stretching.
36. More than ~3 levels of nesting → extract.
37. No god classes: more than ~7–10 public methods means a collaborator is missing.
38. Size refactors are separate, mechanical commits so the diff is reviewable.

## Cross-platform

39. Target macOS, Linux, and Windows; CI covers at least two of them.
40. Target arm64 and x86_64; flag any dependency without native ARM builds and document the workaround.
41. Use the language's path library — never string-concatenate paths or hardcode separators.
42. No shell-isms in cross-platform scripts; orchestrate in Python or Node, not bash.
43. No hardcoded `/tmp`, `~/`, or drive letters — use platform temp/home APIs.
44. Enforce LF line endings via `.gitattributes`.

## Deployment

45. The same code runs on-prem or in the cloud with only config changes — never source changes.
46. Storage goes through an adapter: no `open("./data/...")` outside it, no hardcoded buckets, regions, or account IDs.
47. Container-friendly by default: config from env or mounted files, logs to stdout, no assumed persistent disk.
48. Services expose health/readiness endpoints and shut down gracefully on SIGTERM.
49. Pre-deploy gates (smoke test, vulnerability scan, secret scan) are never disabled by default — escape hatches are explicit, one-off, and logged.
50. Show progress on unavoidably slow operations and say why; cached paths are the default, expensive paths are explicit and rare.

## Secret hygiene

51. Pre-commit hooks with secret scanning (gitleaks + detect-secrets) are mandatory in every repo — installed before the first commit, not after.
52. Pre-push hooks rescan and run the tests.
53. `.gitignore` covers `.env*`, keys, certs, and credential files from day one.
54. Before `git add` of any file you didn't author, scan it for secret-shaped strings (key prefixes, JWTs, private-key blocks, long base64 blobs).
55. Before committing, inspect the staged diff of every config-shaped file (yaml, json, toml, env, anything under infra/deploy dirs) — leaks hide best in "harmless" config.
56. Before pushing, scan the entire push range, not just the tip — an intermediate commit can carry the leak.
57. Before deploying, scan the full artifact: image build context, manifests, env bindings, the lot — not just the files changed since last deploy.
58. A secret that ever touched a commit is burned. Rotate first, clean history second — pushed objects outlive deletion.
59. After any leak, document what scan would have caught it and fix the hooks so it can't recur.
60. Never copy a discovered secret anywhere — not into chat, not a scratch file, not "temporarily."

## Versioning

61. Semantic versioning, with the version in exactly one canonical place — everything else reads from it.
62. Bump on every release; versions only move forward. Roll back by rolling forward to a new patch.
63. Tags are immutable: never move, delete, or reuse a pushed tag.
64. Before creating a tag, fetch the remote's tags and compare — local is not the truth.
65. Push tags by name, never `--tags` reflexively.
66. Every build gets a unique, monotonically increasing build number (`git rev-list --count HEAD` works) — stores reject reused ones.
67. Display the version everywhere it matters: splash screen, `--version`, `/health`.
68. Maintain a changelog in the same commit as the version bump.

## Testing

69. New logic ships with tests; bug fixes ship with a regression test written failing-first, before the fix.
70. Contract first: define and freeze the API or interface, write the tests against the contract, then implement. Never the reverse.
71. 100% line *and* branch coverage — every branch exercised and asserted. Yes, 100%; configure the runner to fail under it.
72. Coverage going down is a stop-and-fix, not a "justify it."
73. Correctness over speed: the delay to reach full coverage and verified behavior is acceptable and expected.
74. No network calls in unit tests — fakes, mocks, and fixtures.
75. Run the full regression suite after every feature; report the test count and any failures.
76. You get what you inspect: test-driven, not test-after.

## Errors and observability

77. No bare `except:`/`catch (e)` swallows — catch specific exceptions, rethrow or log with context.
78. Use a logger, never `print`, in shipped code; log level configurable.
79. Structured logging (JSON) once the project is more than a script.
80. Fail loudly in dev, gracefully in prod, diagnosably always.
81. Resource cleanup uses context managers / `defer` / `using` — no close-and-hope.
82. AI/LLM errors surface to the user as friendly messages — never a silent failure, never a raw stack trace.

## Dependencies

83. Pin versions and commit the lockfile.
84. Prefer stdlib plus one well-maintained dependency over five small ones.
85. Run a vulnerability audit periodically and on every new dependency.
86. Python work always uses a project-local virtualenv — never install into the system Python.
87. State name, purpose, license, and maintenance status before adding any dependency (see rule 4).

## Hygiene

88. After meaningful feature work, run a dead-code pass (vulture/ruff, ts-prune/knip, staticcheck) — remove unused imports, parameters, branches, files; ask before deleting anything you're unsure about.
89. No commented-out code — git history is the archive.
90. No TODO without a tracker link; otherwise it's a dated FIXME with an owner.
91. Lint and format on every commit; CI stays green.
92. After a stable release, the first task is a cleanup sweep — before any new feature.

## Documentation, memory, and tracking

93. After every major change, regenerate the README from scratch rather than patching it. It answers, in order: what/who for, quick start, configuration table, how to test, architecture, deployment, troubleshooting.
94. Non-obvious decisions go in numbered ADRs — immutable after acceptance; a later ADR supersedes, never edits.
95. Track every bug and every requested feature in `bugs.md`/`features.md` the moment it's observed — even if fixed the same turn. Open questions are filed inline with the entry; filing never blocks on answers.
96. Plans live in a `plans/` directory with a first-line `Status:` kept current — stale status on shipped work is a process violation.
97. When a standing decision is made in chat, persist it (ADR, memory file, rules doc) in the same commit — chat history is not memory.

## Working together

98. Plan first for non-trivial work: state the approach and the files to be touched before editing. Size the work so the AI nails it first try 90% of the time — any step with more than a 10% chance of first-try failure gets broken into smaller, mechanical, independently-verifiable sub-steps. Never silently change scope — if the task is bigger than stated, stop and say so.
99. Quote errors verbatim, never paraphrase stack traces; show diffs, not prose, when the question is "what changed?"; surface assumptions explicitly.
100. No flattery, no yes-manning. Agree only when it carries information, disagree plainly when the evidence warrants, and defend your reasoning before capitulating.
