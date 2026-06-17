#!/bin/bash
# gcp-cost-audit — monthly, READ-ONLY GCP cost inventory + cleanup recommendations.
#
# NEVER deletes anything. It inventories every billing-enabled project, estimates
# Artifact Registry storage cost, flags the usual offenders (min-instances > 0,
# big/stale image repos, build-cruft buckets, any always-on Compute/SQL/GKE/IP/LB),
# diffs Artifact Registry storage against last month, and writes a dated report.
# Cleanup is proposed as ready-to-run gcloud commands for a human to approve.
#
# Installed via launchd (see README.md). Runs as the logged-in user so it reuses
# the existing gcloud auth in ~/.config/gcloud.
set -uo pipefail

export PATH="/opt/homebrew/share/google-cloud-sdk/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
export CLOUDSDK_CONFIG="${CLOUDSDK_CONFIG:-$HOME/.config/gcloud}"
export CLOUDSDK_CORE_DISABLE_PROMPTS=1

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORTS="$HERE/reports"
mkdir -p "$REPORTS"
STAMP="$(date +%Y-%m-%d)"
OUT="$REPORTS/$STAMP.md"
REGION="${GCP_AUDIT_REGION:-us-central1}"
GBPRICE="0.10"   # USD per GB/month, Artifact Registry standard tier (approx)

# Match only genuine "API not enabled / no access" signatures — NOT the word
# "disabled" that legitimately appears in resource JSON (e.g. SCANNING_DISABLED).
off() { echo "$1" | grep -qiE "has not been used in project|SERVICE_DISABLED|is disabled\. Enable it|not enabled on project|PERMISSION_DENIED|Billing must be enabled|must be set to a valid project"; }

CLEAN="$(mktemp)"        # accumulates cleanup recommendations
total_ar_bytes=0

{
echo "# GCP cost audit — $STAMP"
echo
echo "_Read-only inventory; nothing was modified. The cleanup list at the bottom is"
echo "recommendations only — review and run them yourself._"
echo
echo "bardtek.com DNS is managed in the registrar UI (Squarespace/Google Domains), not Cloud DNS."
echo

for p in $(gcloud projects list --format="value(projectId)" 2>/dev/null); do
  billing=$(gcloud billing projects describe "$p" --format="value(billingEnabled)" 2>/dev/null)
  if [ "$billing" != "True" ]; then
    echo "## $p — billing disabled (cannot incur cost) — skipped"; echo; continue
  fi
  echo "## $p"

  # ---- Cloud Run (+ min-instances) ----
  run=$(gcloud run services list --project="$p" --quiet \
        --format="value(metadata.name,region)" 2>&1)
  if off "$run"; then echo "- Cloud Run: API off"
  elif [ -z "$run" ]; then echo "- Cloud Run: none"
  else
    echo "- Cloud Run services:"
    echo "$run" | while IFS=$'\t' read -r name rg; do
      [ -z "$name" ] && continue
      rg="${rg:-$REGION}"
      mn=$(gcloud run services describe "$name" --project="$p" --region="$rg" --quiet \
           --format="value(spec.template.metadata.annotations['autoscaling.knative.dev/minScale'])" 2>/dev/null)
      mn="${mn:-0}"
      echo "    - $name ($rg) min-instances=$mn"
      if [ "$mn" != "0" ]; then
        echo "FLAG [$p] Cloud Run '$name' has min-instances=$mn (idles at cost). Zero it:" >> "$CLEAN"
        echo "    gcloud run services update $name --project=$p --region=$rg --min-instances=0" >> "$CLEAN"
      fi
    done
  fi

  # ---- Artifact Registry (sizes + cost) ----
  arjson=$(gcloud artifacts repositories list --project="$p" --quiet --format=json 2>&1)
  if off "$arjson"; then echo "- Artifact Registry: API off"
  else
    sums=$(echo "$arjson" | python3 -c '
import sys, json
raw = sys.stdin.read()
i = raw.find("[")                       # skip gcloud "Listing items..." preamble before the JSON
try: d = json.loads(raw[i:]) if i >= 0 else []
except Exception: d = []
tot = 0
for r in d:
    b = int(r.get("sizeBytes", 0) or 0); tot += b
    name = r.get("name","").split("/")[-1]
    print(f"REPO\t{name}\t{b}")
print(f"TOT\t{tot}")
' 2>/dev/null)
    pbytes=0
    echo "- Artifact Registry repos:"
    while IFS=$'\t' read -r tag a b; do
      case "$tag" in
        REPO)
          gb=$(python3 -c "print(f'{$b/1e9:.2f}')")
          echo "    - $a : ${gb} GB"
          if python3 -c "import sys; sys.exit(0 if $b>5e9 else 1)"; then
            echo "FLAG [$p] AR repo '$a' is ${gb} GB (>5 GB). Prune old versions or delete:" >> "$CLEAN"
            echo "    gcloud artifacts repositories delete $a --project=$p --location=$REGION   # or set a cleanup policy" >> "$CLEAN"
          fi
          case "$a" in
            *cloud-run-source-deploy*|*cloudbuild*)
              echo "FLAG [$p] AR repo '$a' is build-cache cruft (${gb} GB) — safe to prune stale versions." >> "$CLEAN" ;;
          esac
          ;;
        TOT) pbytes="$a" ;;   # "TOT<TAB>bytes" — value is field 2
      esac
    done <<< "$sums"
    total_ar_bytes=$(python3 -c "print(int($total_ar_bytes)+int($pbytes))")
    pgb=$(python3 -c "print(f'{$pbytes/1e9:.2f}')")
    echo "    project AR total: ${pgb} GB"
  fi

  # ---- Cloud Storage buckets ----
  bk=$(gcloud storage buckets list --project="$p" --quiet --format="value(name)" 2>&1)
  if off "$bk"; then echo "- Buckets: API off"
  elif [ -z "$bk" ]; then echo "- Buckets: none"
  else
    echo "- Buckets:"
    for b in $bk; do
      sz=$(gcloud storage du -s "gs://$b" 2>/dev/null | awk '{print $1}')
      sz="${sz:-0}"
      gb=$(python3 -c "print(f'{$sz/1e9:.2f}')")
      echo "    - gs://$b : ${gb} GB"
      case "$b" in
        *_cloudbuild|run-sources-*)
          echo "FLAG [$p] bucket 'gs://$b' is build-source cruft (${gb} GB) — safe to empty." >> "$CLEAN" ;;
      esac
    done
  fi

  # ---- Always-on (expensive) resources ----
  for kind in \
    "VMs|compute instances list|name,zone,machineType.basename(),status" \
    "Cloud SQL|sql instances list|name,databaseVersion,settings.tier,state" \
    "GKE|container clusters list|name,location,currentNodeCount" \
    "Static IPs|compute addresses list|name,address,status" \
    "Load balancers|compute forwarding-rules list|name,IPAddress"; do
    label="${kind%%|*}"; rest="${kind#*|}"; cmd="${rest%%|*}"; fmt="${rest#*|}"
    out=$(gcloud $cmd --project="$p" --quiet --format="value($fmt)" 2>&1)
    if off "$out"; then :   # API off => none of that resource
    elif [ -n "$out" ]; then
      echo "- $label PRESENT:"; echo "$out" | sed 's/^/    /'
      echo "FLAG [$p] $label present — these bill even when idle. Review/delete in console or gcloud." >> "$CLEAN"
    fi
  done
  echo
done

# ---- Totals + month-over-month ----
tot_gb=$(python3 -c "print(f'{$total_ar_bytes/1e9:.2f}')")
tot_cost=$(python3 -c "print(f'{$total_ar_bytes/1e9*$GBPRICE:.2f}')")
echo "## Totals"
echo "- Artifact Registry across all projects: **${tot_gb} GB** ≈ **\$${tot_cost}/mo** (at \$$GBPRICE/GB/mo)"

prev=$(ls -1 "$REPORTS"/*.md 2>/dev/null | grep -v "/$STAMP.md\$" | tail -1)
if [ -n "$prev" ]; then
  pg=$(grep -oE "TOTAL_AR_GB: [0-9.]+" "$prev" | awk '{print $2}' | tail -1)
  if [ -n "$pg" ]; then
    delta=$(python3 -c "print(f'{$tot_gb-$pg:+.2f}')")
    echo "- vs last report ($(basename "$prev" .md)): ${pg} GB → ${tot_gb} GB (**${delta} GB**)"
  fi
fi
echo "<!-- TOTAL_AR_GB: $tot_gb -->"
echo

echo "## Cleanup recommendations (review, then run yourself — nothing was deleted)"
if [ -s "$CLEAN" ]; then echo; echo '```'; cat "$CLEAN"; echo '```'
else echo; echo "_No flags this month — clean._"; fi
echo

echo "## Bottom line"
top=$(grep -m1 "^FLAG" "$CLEAN" 2>/dev/null | sed 's/^FLAG //')
echo "- Est. spend driver: **${tot_gb} GB** Artifact Registry ≈ **\$${tot_cost}/mo**."
echo "- Top cleanup opportunity: ${top:-none — nothing flagged}."
} > "$OUT"

rm -f "$CLEAN"
echo "Wrote $OUT"
