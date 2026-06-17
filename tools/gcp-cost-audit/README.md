# gcp-cost-audit

Monthly, **read-only** GCP cost audit. Inventories every billing-enabled project,
estimates Artifact Registry storage cost, flags the usual cost offenders, diffs
storage month-over-month, and writes a dated report to `reports/`. It **never
deletes anything** — the cleanup section is ready-to-run `gcloud` commands for you
to review and run yourself.

What it flags: Cloud Run services with `min-instances > 0`, Artifact Registry repos
over 5 GB and any `cloud-run-source-deploy`/`*_cloudbuild` build-cache repos,
`*_cloudbuild`/`run-sources-*` cruft buckets, and any always-on Compute VM / Cloud
SQL / GKE / reserved static IP / load balancer.

## Run it manually
```
bash tools/gcp-cost-audit/audit.sh
open tools/gcp-cost-audit/reports/$(date +%Y-%m-%d).md
```

## Install the monthly schedule (launchd — runs as you, reuses your gcloud auth)
```
cp tools/gcp-cost-audit/com.edhaynes.gcp-cost-audit.plist ~/Library/LaunchAgents/
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.edhaynes.gcp-cost-audit.plist
launchctl enable gui/$(id -u)/com.edhaynes.gcp-cost-audit
```
Runs the **1st of every month at 09:00 local**. If the Mac is asleep/off at that
moment, launchd runs it at the next wake. Reports land in `reports/` (gitignored).

## Uninstall
```
launchctl bootout gui/$(id -u)/com.edhaynes.gcp-cost-audit
rm ~/Library/LaunchAgents/com.edhaynes.gcp-cost-audit.plist
```

## Notes
- Requires the local gcloud SDK authed (`gcloud auth list`). The script pins the
  Homebrew SDK path and `CLOUDSDK_CONFIG=~/.config/gcloud` so launchd's minimal env
  still finds auth.
- `reports/` is gitignored (the script + plist are versioned; the monthly outputs
  are not, to keep git clean).
- The "pricing cap" itself is a **GCP Billing Budget** (set separately in the
  billing console / `gcloud billing budgets`), which alerts by email 24/7 and does
  not depend on this job.
