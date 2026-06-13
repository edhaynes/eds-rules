#!/usr/bin/env python3
"""Polish-rounds experiment: how many MORE meaty rules can rubric-driven review
find, and when do returns diminish?

Eddie's hypothesis: two more polish rounds yield meaty results, tapering by
round 5. Each round = a review pass that surfaces the best NEW gap not already
covered, graded on the recalibrated rule-quality rubric (quality/RUBRIC.md,
full 0-10 range, 50 = keep/cut bar). Candidates are listed in discovery order
(best gaps found first), binned into rounds. Stdlib only; renders an SVG taper.

This is one informed pass (Jason), not an independent multi-agent run — the
grades are judgment, transparent and editable. Re-run after editing a tuple.
"""
from pathlib import Path

WEIGHTS = (0.30, 0.15, 0.20, 0.15, 0.10, 0.10)  # matches quality/grade_rules.py
BAR = 50.0

# round -> list of (name, pertinence, security, cost, arch, enforce, generality)
ROUNDS = {
    1: [("UTC everywhere; no naive datetimes",        6, 3, 7, 5, 6, 8),
        ("Least privilege for creds/IAM/DB users",     5, 8, 6, 4, 3, 8)],
    2: [("Timeouts + retries + circuit breakers",      6, 4, 6, 5, 4, 8),
        ("Latency/determinism + live progress [Eddie]",6, 2, 6, 5, 4, 8)],
    3: [("Migrations: forward-only, reversible, tested",5, 4, 6, 5, 4, 7),
        ("Observability: metrics + tracing + alerts",   5, 2, 6, 5, 4, 8)],
    4: [("Independent review of AI output pre-merge",   6, 3, 5, 4, 3, 8),
        ("PII minimization; redact PII in logs",        4, 6, 6, 4, 3, 7)],
    5: [("Safe-by-default perms (no 0777 / 0.0.0.0)",   4, 6, 5, 4, 5, 7),
        ("Concurrency / race-safety discipline",        5, 3, 5, 6, 2, 7)],
    6: [("Reproducible / deterministic builds",         4, 4, 5, 5, 5, 7),
        ("Rate limiting / quotas / cost controls",      4, 5, 5, 4, 4, 7)],
    7: [("Backups + a tested restore (DR)",             4, 5, 5, 3, 3, 7),
        ("Accessibility (a11y) for any UI",             4, 2, 5, 4, 5, 6)],
    8: [("Cache-invalidation discipline",               4, 2, 5, 4, 3, 6),
        ("Canary / feature-flag rollout",               3, 3, 5, 4, 3, 7)],
    9: [("API versioning / deprecation policy",         3, 2, 5, 4, 3, 6),
        ("Runbooks / on-call operational docs",         3, 1, 5, 3, 2, 6)],
    10:[("License / SPDX headers",                      2, 1, 4, 3, 6, 6),
        ("i18n / localization readiness",               2, 1, 4, 4, 4, 5),
        ("Commit emoji / style conventions",            2, 1, 4, 3, 5, 5)],
}


def composite(scores):
    return round(sum(s * w for s, w in zip(scores, WEIGHTS)) * 10, 1)


def analyse():
    rows = []
    for rnd, cands in ROUNDS.items():
        for name, *sc in cands:
            rows.append({"round": rnd, "name": name, "q": composite(sc)})
    best = {r: max(x["q"] for x in rows if x["round"] == r) for r in ROUNDS}
    return rows, best


def write_csv(rows, path):
    out = ["round,candidate,quality,above_bar"]
    for r in rows:
        out.append(f'{r["round"]},{r["name"].replace(",", ";")},{r["q"]},{int(r["q"]>=BAR)}')
    path.write_text("\n".join(out) + "\n")


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(rows, best, path):
    W, H = 900, 540
    L, R, T, B = 70, 240, 70, 60
    pw, ph = W - L - R, H - T - B
    qmax = 70

    def X(rnd):
        return L + pw * (rnd - 1) / (len(ROUNDS) - 1)

    def Y(q):
        return T + ph * (1 - q / qmax)

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'font-family="Helvetica,Arial,sans-serif" font-size="12">']
    s.append(f'<rect width="{W}" height="{H}" fill="#fff"/>')
    s.append(f'<text x="{L}" y="34" font-size="20" font-weight="bold" fill="#1a1a1a">'
             f'Polish rounds — do new rules keep coming?</text>')
    s.append(f'<text x="{L}" y="52" font-size="12" fill="#666">'
             f'Best candidate quality per review round (recalibrated rubric, 0-100). '
             f'Dashed = 50 keep/cut bar.</text>')
    # axes
    for q in (0, 25, 50, 75 if qmax > 75 else qmax):
        if q > qmax:
            continue
        y = Y(q)
        s.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="#eee"/>')
        s.append(f'<text x="{L-8}" y="{y+4:.1f}" text-anchor="end" font-size="10" fill="#999">{q}</text>')
    yb = Y(BAR)
    s.append(f'<line x1="{L}" y1="{yb:.1f}" x2="{W-R}" y2="{yb:.1f}" '
             f'stroke="#c0392b" stroke-width="1.6" stroke-dasharray="5,3"/>')
    s.append(f'<text x="{W-R+6}" y="{yb+4:.1f}" font-size="11" fill="#c0392b" font-weight="bold">50 keep/cut</text>')
    # all candidate dots
    for r in rows:
        col = "#16a085" if r["q"] >= BAR else "#c0392b"
        s.append(f'<circle cx="{X(r["round"]):.1f}" cy="{Y(r["q"]):.1f}" r="3.2" '
                 f'fill="{col}" opacity="0.55"/>')
    # best-per-round line
    pts = " ".join(f'{X(r):.1f},{Y(best[r]):.1f}' for r in sorted(best))
    s.append(f'<polyline points="{pts}" fill="none" stroke="#2c3e50" stroke-width="2"/>')
    for r in sorted(best):
        s.append(f'<circle cx="{X(r):.1f}" cy="{Y(best[r]):.1f}" r="4.5" fill="#2c3e50"/>')
        s.append(f'<text x="{X(r):.1f}" y="{Y(best[r])-9:.1f}" text-anchor="middle" '
                 f'font-size="10" fill="#2c3e50">{best[r]:.0f}</text>')
        s.append(f'<text x="{X(r):.1f}" y="{H-B+18:.1f}" text-anchor="middle" '
                 f'font-size="11" fill="#444">R{r}</text>')
    s.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-14}" text-anchor="middle" font-size="12" '
             f'fill="#444">polish round</text>')
    # callout: where it crosses the bar
    cross = next(r for r in sorted(best) if best[r] < BAR)
    s.append(f'<text x="{X(cross):.1f}" y="{Y(best[cross])+22:.1f}" text-anchor="middle" '
             f'font-size="10" fill="#c0392b">taper crosses bar</text>')
    # legend of best candidate names per round (right gutter)
    lx, ly = W - R + 6, T + 6
    s.append(f'<text x="{lx}" y="{ly}" font-size="10" font-weight="bold" fill="#333">best find each round</text>')
    for i, r in enumerate(sorted(best)):
        name = next(x["name"] for x in rows if x["round"] == r and x["q"] == best[r])
        col = "#16a085" if best[r] >= BAR else "#c0392b"
        s.append(f'<text x="{lx}" y="{ly+16+i*15}" font-size="9" fill="{col}">'
                 f'R{r} {best[r]:.0f} {esc(name[:30])}</text>')
    s.append('</svg>')
    path.write_text("\n".join(s) + "\n")


def main():
    here = Path(__file__).resolve().parent
    rows, best = analyse()
    write_csv(rows, here / "polish-candidates.csv")
    render_svg(rows, best, here / "polish-taper.svg")
    above = [r for r in rows if r["q"] >= BAR]
    print("best candidate per round:", {r: best[r] for r in sorted(best)})
    print(f"above-bar candidates found total: {len(above)} / {len(rows)}")
    for r in above:
        print(f"  R{r['round']}  {r['q']:.1f}  {r['name']}")
    cross = next(r for r in sorted(best) if best[r] < BAR)
    print(f"taper crosses the 50 bar at round {cross}")
    print(f"wrote polish-candidates.csv and polish-taper.svg")


if __name__ == "__main__":
    main()
