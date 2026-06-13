#!/usr/bin/env python3
"""Grade all 100 rules on the quality rubric (see RUBRIC.md) and render a graph.

Stdlib only — no matplotlib, no third-party deps. Outputs:
  quality/grades.csv         raw scores + composite, one row per rule
  quality/rule-quality.svg   horizontal bar chart, sorted by composite

Each rule is scored 0-10 on six dimensions; the weighted composite is 0-100.
Edit a row and re-run to re-grade. Weights live in WEIGHTS.
"""
from pathlib import Path

# dim order: pertinence, security, cost_eff, arch_simpl, enforce, generality
WEIGHTS = (0.30, 0.15, 0.20, 0.15, 0.10, 0.10)
DIMS = ("pertinence", "security", "cost_eff", "arch_simpl", "enforce", "generality")

# section key -> (display label, colour)
SECTIONS = {
    "hard":    ("Hard rules",        "#c0392b"),
    "crew":    ("The crew",          "#8e44ad"),
    "config":  ("Configuration",     "#2980b9"),
    "arch":    ("Architecture",      "#16a085"),
    "size":    ("Size & complexity", "#27ae60"),
    "xplat":   ("Cross-platform",    "#f39c12"),
    "deploy":  ("Deployment",        "#d35400"),
    "secret":  ("Secret hygiene",    "#e74c3c"),
    "version": ("Versioning",        "#7f8c8d"),
    "test":    ("Testing",           "#2c3e50"),
    "errors":  ("Errors & observ.",  "#34495e"),
    "deps":    ("Dependencies",      "#9b59b6"),
    "hygiene": ("Hygiene",           "#1abc9c"),
    "docs":    ("Docs & memory",     "#3498db"),
    "working": ("Working together",  "#e67e22"),
}

# (num, section, short title, pertinence, security, cost_eff, arch, enforce, generality)
# Recalibrated 2026-06-13 to use the FULL 0-10 range (Eddie: kill the central-
# tendency bias; a niche/never-violated rule must be free to score 1-2). 50 is
# the keep/cut bar — below it, a rule earns its slot on conviction, not leverage.
RULES = [
    (1,  "hard", "Secret scan before ship",        10, 10, 10, 4, 10,  9),
    (2,  "hard", "Never hardcode a secret",          9, 10,  9, 4,  6, 10),
    (3,  "hard", "Distrust every external input",    7,  9,  8, 5,  5,  9),
    (4,  "hard", "Destruction needs a human",        7,  8,  9, 3,  6, 10),
    (5,  "hard", "Autonomy bounded by VC",           6,  6,  8, 4,  7,  7),
    (6,  "hard", "Push early, push always",          7,  4,  8, 3,  8,  8),
    (7,  "hard", "Green commit, healthy handover",   7,  3,  7, 5,  8,  9),
    (8,  "hard", "One purpose per commit",           6,  2,  8, 6,  5,  9),
    (9,  "hard", "Fail fast",                        7,  5,  8, 8,  6, 10),
    (10, "hard", "Disclose every dependency",        5,  5,  7, 4,  5,  9),
    (11, "hard", "No path/OS assumptions; script",   7,  3,  7, 5,  6,  8),
    (12, "crew", "Powell rule: 90% then decide",     8,  2,  8, 5,  2,  8),
    (13, "crew", "Five roles, human is final",       4,  1,  5, 4,  1,  3),
    (14, "crew", "Claudius plans deep",              4,  1,  5, 6,  1,  4),
    (15, "crew", "Jason sprints sized for 90%",      5,  1,  6, 6,  2,  4),
    (16, "crew", "Claude searches before building",  6,  2,  7, 6,  2,  7),
    (17, "crew", "Claudina: cross-platform day one", 5,  3,  6, 5,  3,  6),
    (18, "crew", "Linda searches wide",              3,  1,  5, 3,  1,  4),
    (19, "crew", "Go local rebinds the crew",        2,  1,  4, 4,  2,  2),
    (20, "config", "Zero hardcoded values",          8,  4,  8, 8,  6, 10),
    (21, "config", "Never silently fall back",       5,  5,  7, 7,  5,  8),
    (22, "config", "Validate config at startup",     6,  4,  8, 7,  7,  9),
    (23, "config", "One config layer, one order",    6,  3,  7, 8,  5,  8),
    (24, "config", "Local default, not hardcoded",   4,  2,  6, 6,  4,  7),
    (25, "config", "Zero-setup local defaults",      4,  1,  7, 5,  4,  7),
    (26, "config", "No magic numbers",               6,  2,  7, 7,  7,  9),
    (27, "config", "Ship the .env.example",          5,  3,  8, 5,  7,  8),
    (28, "arch", "Architecture beats language",      4,  1,  6, 8,  1,  9),
    (29, "arch", "Swappable interface per axis",     5,  4,  6, 8,  3,  7),
    (30, "arch", "Search open source first",         6,  2,  8, 7,  2,  8),
    (31, "arch", "DI over globals",                  5,  3,  7, 9,  5,  8),
    (32, "arch", "OO + SOLID where it earns",        4,  1,  6, 7,  3,  7),
    (33, "arch", "One non-trivial class per file",   3,  1,  5, 6,  6,  7),
    (34, "size", "Files small, never >1000 lines",   5,  1,  6, 7,  9,  8),
    (35, "size", "No god classes",                   4,  1,  6, 8,  4,  8),
    (36, "size", "Size refactors are own commits",   4,  1,  6, 5,  3,  8),
    (37, "size", "Small functions, few params",      5,  1,  6, 8,  9,  8),
    (38, "size", "Shallow nesting",                  4,  1,  6, 7,  7,  8),
    (39, "xplat", "Three platforms, two in CI",      4,  2,  6, 4,  6,  7),
    (40, "xplat", "Path library + LF endings",       6,  2,  7, 6,  8,  8),
    (41, "xplat", "No hardcoded temp/home/drive",    5,  3,  7, 6,  7,  8),
    (42, "xplat", "Both arches, flag no-ARM",        4,  1,  5, 4,  4,  6),
    (43, "xplat", "No shell-isms; orchestrate",      4,  2,  6, 6,  4,  7),
    (44, "deploy", "Storage goes through adapter",   4,  3,  6, 8,  4,  7),
    (45, "deploy", "Same code on-prem or cloud",     4,  2,  6, 7,  3,  7),
    (46, "deploy", "Pre-deploy gates never off",     6,  8,  7, 5,  7,  8),
    (47, "deploy", "Idempotent, safe to re-run",     6,  4,  7, 7,  5,  8),
    (48, "deploy", "Health endpoints + SIGTERM",     4,  3,  6, 6,  7,  7),
    (49, "deploy", "Podman / UBI / OpenShift",       4,  4,  5, 6,  6,  2),
    (50, "deploy", "Show progress; cache default",   4,  1,  6, 6,  3,  8),
    (51, "secret", "Hooks before first commit",      7,  9,  8, 4,  8,  9),
    (52, "secret", "A touched secret is burned",     4,  9,  6, 3,  2,  8),
    (53, "secret", "Never copy a secret anywhere",   5,  9,  7, 4,  3,  8),
    (54, "secret", "Scan the whole artifact",        5,  9,  7, 4,  7,  8),
    (55, "secret", "Scan the range, not the tip",    5,  9,  7, 4,  7,  8),
    (56, "secret", "Inspect config-file diffs",      6,  9,  7, 4,  6,  8),
    (57, "secret", "Scan files you didn't write",    5,  8,  6, 4,  5,  8),
    (58, "secret", "Pre-push rescan + tests",        5,  8,  7, 4,  8,  8),
    (59, "secret", "Gitignore keys from day one",    6,  8,  9, 4,  8,  9),
    (60, "secret", "After a leak, fix the hook",     3,  7,  6, 4,  3,  8),
    (61, "version", "Tags are immutable",            4,  4,  7, 4,  7,  8),
    (62, "version", "Versions only move forward",    4,  3,  7, 4,  6,  8),
    (63, "version", "SemVer, one canonical home",    5,  2,  7, 7,  6,  8),
    (64, "version", "Fetch tags before tagging",     4,  3,  7, 3,  7,  7),
    (65, "version", "Unique build number",           4,  1,  6, 4,  8,  7),
    (66, "version", "Changelog rides the bump",      5,  1,  7, 4,  6,  8),
    (67, "version", "Show the version everywhere",   4,  2,  7, 4,  6,  8),
    (68, "version", "Push tags by name",             3,  3,  6, 3,  7,  7),
    (69, "test", "Inspect, grade to a rubric",       6,  2,  7, 6,  4,  8),
    (70, "test", "Tests with logic, regress first",  7,  4,  7, 6,  6,  9),
    (71, "test", "Contract first, code second",      5,  3,  5, 7,  4,  8),
    (72, "test", "100% line + branch coverage",      5,  4,  4, 5,  9,  7),
    (73, "test", "Correctness over speed",           4,  2,  6, 5,  2,  8),
    (74, "test", "Coverage never goes down",         4,  2,  6, 5,  8,  8),
    (75, "test", "Full regression, with numbers",    6,  4,  7, 5,  7,  9),
    (76, "test", "Latency budget, gated like cov.",  4,  2,  5, 5,  6,  7),
    (77, "test", "No network in unit tests",         6,  3,  7, 7,  7,  9),
    (78, "errors", "No swallowed exceptions",        6,  4,  7, 7,  7,  9),
    (79, "errors", "Loud dev, graceful prod",        5,  4,  7, 7,  3,  9),
    (80, "errors", "A logger, never print",          6,  2,  7, 5,  8,  9),
    (81, "errors", "AI errors surface; no fake tool",6,  3,  7, 5,  4,  8),
    (82, "errors", "Cleanup is structural",          5,  3,  7, 7,  6,  9),
    (83, "errors", "Structured logs past a script",  3,  1,  6, 5,  3,  7),
    (84, "deps", "Pin it and lock it",               6,  6,  8, 5,  8,  9),
    (85, "deps", "Audit for vulnerabilities",        5,  7,  7, 4,  7,  8),
    (86, "deps", "Stdlib plus one, not five",        5,  4,  7, 8,  3,  8),
    (87, "deps", "Project-local virtualenv",         5,  4,  7, 5,  7,  5),
    (88, "hygiene", "Lint + format every commit",    6,  2,  8, 5,  9,  9),
    (89, "hygiene", "Dead-code pass after features", 5,  2,  7, 7,  7,  8),
    (90, "hygiene", "Cleanup sweep after release",   3,  1,  6, 6,  3,  7),
    (91, "hygiene", "No commented-out code",         5,  2,  7, 5,  8,  8),
    (92, "hygiene", "No orphan TODOs",               4,  2,  6, 4,  7,  8),
    (93, "docs", "Persist decisions same commit",    6,  2,  7, 5,  3,  8),
    (94, "docs", "File bugs/features on sight",      6,  1,  7, 4,  3,  8),
    (95, "docs", "Plans carry a live Status",        4,  1,  6, 4,  5,  6),
    (96, "docs", "ADRs are immutable",               4,  1,  6, 5,  4,  7),
    (97, "docs", "Regenerate the README",            5,  1,  6, 4,  3,  8),
    (98, "working", "Plan first, size for 90%",      7,  2,  7, 6,  3,  9),
    (99, "working", "No flattery, no yes-manning",   6,  1,  7, 4,  2,  8),
    (100,"working", "Verbatim errors, diffs, asks",  6,  2,  7, 4,  4,  9),
]


def composite(scores):
    return round(sum(s * w for s, w in zip(scores, WEIGHTS)) * 10, 1)


def graded():
    rows = []
    for num, sect, short, *scores in RULES:
        rows.append({"num": num, "section": sect, "short": short,
                     "scores": scores, "composite": composite(scores)})
    return rows


def write_csv(rows, path):
    header = ["num", "section", "short_title", *DIMS, "composite"]
    lines = [",".join(header)]
    for r in rows:
        title = r["short"].replace(",", ";")
        lines.append(",".join(str(x) for x in
                     [r["num"], r["section"], title, *r["scores"], r["composite"]]))
    path.write_text("\n".join(lines) + "\n")


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(rows, path):
    rows = sorted(rows, key=lambda r: r["composite"], reverse=True)
    bar_h, gap = 13, 4
    row_h = bar_h + gap
    left, right = 290, 70          # label gutter, score gutter
    top, bottom = 96, 40
    plot_w = 620
    width = left + plot_w + right
    height = top + len(rows) * row_h + bottom

    def x(score):
        return left + plot_w * score / 100.0

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
         f'font-family="Helvetica,Arial,sans-serif" font-size="11">']
    s.append(f'<rect width="{width}" height="{height}" fill="#ffffff"/>')
    s.append(f'<text x="{left}" y="34" font-size="22" font-weight="bold" fill="#1a1a1a">'
             f'100 Rules — Quality Score</text>')
    s.append(f'<text x="{left}" y="54" font-size="12" fill="#666">'
             f'Weighted rubric (pertinence·.30 security·.15 cost·.20 simplicity·.15 '
             f'enforce·.10 generality·.10), 0–100. Sorted best→worst.</text>')

    # gridlines + axis labels
    for g in (0, 25, 50, 75, 100):
        gx = x(g)
        s.append(f'<line x1="{gx:.1f}" y1="{top-6}" x2="{gx:.1f}" y2="{height-bottom+4}" '
                 f'stroke="#e8e8e8"/>')
        s.append(f'<text x="{gx:.1f}" y="{top-12}" font-size="10" fill="#999" '
                 f'text-anchor="middle">{g}</text>')
    # 50 = Eddie's keep/cut bar (5/10 = above average). Below it, reconsider the rule.
    gx = x(50)
    s.append(f'<line x1="{gx:.1f}" y1="{top-6}" x2="{gx:.1f}" y2="{height-bottom+4}" '
             f'stroke="#c0392b" stroke-width="1.6" stroke-dasharray="5,3"/>')
    s.append(f'<text x="{gx:.1f}" y="{height-bottom+18}" font-size="10" fill="#c0392b" '
             f'text-anchor="middle" font-weight="bold">50 — keep/cut bar</text>')

    for i, r in enumerate(rows):
        y = top + i * row_h
        col = SECTIONS[r["section"]][1]
        bw = x(r["composite"]) - left
        label = esc(f'{r["num"]:>3}. {r["short"]}')
        s.append(f'<text x="{left-8}" y="{y+bar_h-2}" text-anchor="end" fill="#333">{label}</text>')
        s.append(f'<rect x="{left}" y="{y}" width="{bw:.1f}" height="{bar_h}" '
                 f'fill="{col}" rx="1.5"/>')
        s.append(f'<text x="{x(r["composite"])+6:.1f}" y="{y+bar_h-2}" fill="#333" '
                 f'font-size="10">{r["composite"]:.0f}</text>')

    # legend — bottom-right, where the low-scoring bars leave whitespace
    lx = left + plot_w * 0.60
    ly = top + len(rows) * row_h - 15 * len(SECTIONS) - 10
    s.append(f'<rect x="{lx-10}" y="{ly-22}" width="200" height="{15*len(SECTIONS)+30}" '
             f'fill="#ffffff" stroke="#ddd" rx="4"/>')
    s.append(f'<text x="{lx}" y="{ly-6}" font-size="11" font-weight="bold" fill="#333">Section</text>')
    for j, (key, (lab, col)) in enumerate(SECTIONS.items()):
        ey = ly + 6 + j * 15
        s.append(f'<rect x="{lx}" y="{ey}" width="11" height="11" fill="{col}" rx="1.5"/>')
        s.append(f'<text x="{lx+16}" y="{ey+9}" font-size="10" fill="#444">{esc(lab)}</text>')

    s.append('</svg>')
    path.write_text("\n".join(s) + "\n")


def summary(rows):
    rows_sorted = sorted(rows, key=lambda r: r["composite"], reverse=True)
    avg = sum(r["composite"] for r in rows) / len(rows)
    print(f"mean quality: {avg:.1f}   "
          f"max {rows_sorted[0]['composite']} (#{rows_sorted[0]['num']})   "
          f"min {rows_sorted[-1]['composite']} (#{rows_sorted[-1]['num']})")
    print("\nTop 8:")
    for r in rows_sorted[:8]:
        print(f"  {r['composite']:5.1f}  {r['num']:>3}. {r['short']}")
    print("\nBottom 8:")
    for r in rows_sorted[-8:]:
        print(f"  {r['composite']:5.1f}  {r['num']:>3}. {r['short']}")
    print("\nBy section (avg):")
    for key, (lab, _) in SECTIONS.items():
        vals = [r["composite"] for r in rows if r["section"] == key]
        print(f"  {sum(vals)/len(vals):5.1f}  {lab} ({len(vals)})")
    below = [r for r in rows_sorted if r["composite"] < 50.0]
    print(f"\nBELOW THE 50 KEEP/CUT BAR ({len(below)} rules):")
    for r in below:
        print(f"  {r['composite']:5.1f}  {r['num']:>3}. {r['short']}")


def main():
    here = Path(__file__).resolve().parent
    rows = graded()
    assert len(rows) == 100, f"expected 100 rules, got {len(rows)}"
    write_csv(rows, here / "grades.csv")
    render_svg(rows, here / "rule-quality.svg")
    summary(rows)
    print(f"\nwrote {here/'grades.csv'} and {here/'rule-quality.svg'}")


if __name__ == "__main__":
    main()
