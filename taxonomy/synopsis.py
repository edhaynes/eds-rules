#!/usr/bin/env python3
"""Generate a one/two-page synopsis (HTML) of the layered ruleset from rules.yaml.
Render to PDF with headless Chrome. Single source of truth = rules.yaml.

Usage: synopsis.py  ->  generated/synopsis.html
"""
import os, html
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
reg = yaml.safe_load(open(os.path.join(HERE, "rules.yaml")))
OWL = os.path.join(HERE, "..", "demo", "assets", "bard-owl-square.png")

AX = reg["axioms"]
LAYERS = reg["layers"]
CREW = yaml.safe_load(open(os.path.join(HERE, "crew-3.yaml")))

# axiom thematic groups (presentation only)
GROUPS = [
    ("Safety & security", ["AX-SCAN", "AX-NOSECRET", "AX-INPUT", "AX-DESTROY",
                            "AX-LEASTPRIV", "AX-HOOKS", "AX-BURNED"]),
    ("Architecture", ["AX-NOHARD", "AX-FAILFAST", "AX-CONTRACT", "AX-HEADLESS"]),
    ("Engineering discipline", ["AX-POWELL", "AX-AUTOVC", "AX-PUSH", "AX-GREEN",
                                "AX-ONEPURP", "AX-DEPDISC", "AX-PLAN"]),
    ("Quality", ["AX-GRADE", "AX-REGRESS", "AX-CORRECT", "AX-COVER"]),
    ("Working with humans / agents", ["AX-NOFLAT", "AX-VERBATIM"]),
]
byid = {r["id"]: r for r in AX}

LAYER_BLURB = {
    "personal": "Architect's opinions, the crew, the stack, fleet operation. YMMV — fork freely.",
    "project": "What's being built (generic cloud-native, multi-platform).",
    "bardinfra": "Concrete sample app — bard-infra, the fleet/infra project (owns the testbed).",
    "employer": "Org-level constraints. Placeholder — fill per engagement.",
}

e = html.escape


def axiom_groups():
    out = []
    for name, ids in GROUPS:
        items = "".join(
            f"<li><b>{e(byid[i]['title'])}</b> <span class=t>{e(byid[i]['text'])}</span></li>"
            for i in ids if i in byid)
        out.append(f"<h3>{e(name)} <span class=n>({len([i for i in ids if i in byid])})</span></h3><ul>{items}</ul>")
    return "".join(out)


def crew_rows():
    out = []
    for s in CREW["seats"]:
        b = s["params_b"]
        budget = "full" if b >= 100 else f"~{b}"
        out.append(f"<tr><td>{e(s['name'])}</td><td>{e(s['role'])}</td>"
                   f"<td>{e(s['model'])}</td><td>{budget}</td></tr>")
    return "".join(out)


def layer_block(key):
    rules = LAYERS.get(key, [])
    items = "".join(f"<li><b>{e(r['title'])}</b></li>" for r in sorted(rules, key=lambda r: -r["priority"]))
    return (f"<h3>{e(key.capitalize())} layer <span class=n>({len(rules)})</span></h3>"
            f"<p class=blurb>{e(LAYER_BLURB.get(key, ''))}</p><ul class=compact>{items}</ul>")


NAX = len(AX)
NPERS = len(LAYERS.get("personal", []))
NPROJ = len(LAYERS.get("project", []))
NINFRA = len(LAYERS.get("bardinfra", []))
NEMP = len(LAYERS.get("employer", []))

def pyramid_svg():
    """Inverted pyramid: widest = most general (axioms), tapering to most specific.
    Slice width is proportional to rule count."""
    layers = [("Axioms", NAX, "universal — every seat", "#161616"),
              ("Personal / architect", NPERS, "crew, stack, engineering style", "#7a1414"),
              ("Project", NPROJ, "what's being built (or bard-infra: %d)" % NINFRA, "#c01818"),
              ("Employer", NEMP, "org constraints", "#EE0000")]
    cx, y, h, gap, maxw = 300, 26, 70, 5, 470
    scale = maxw / max(c for _, c, _, _ in layers)
    widths = [c * scale for _, c, _, _ in layers]
    parts = []
    for i, (name, c, desc, color) in enumerate(layers):
        top = widths[i]
        bot = widths[i + 1] if i + 1 < len(layers) else widths[i] * 0.45
        tl, tr, bl, br = cx - top / 2, cx + top / 2, cx - bot / 2, cx + bot / 2
        ly = y + h / 2
        parts.append(f'<polygon points="{tl:.0f},{y} {tr:.0f},{y} {br:.0f},{y+h} {bl:.0f},{y+h}" fill="{color}"/>')
        parts.append(f'<text x="{cx}" y="{ly+6:.0f}" text-anchor="middle" fill="#fff" font-weight="700" font-size="18">{c}</text>')
        parts.append(f'<line x1="{tr:.0f}" y1="{ly:.0f}" x2="556" y2="{ly:.0f}" stroke="#ccc" stroke-width="1"/>')
        parts.append(f'<text x="562" y="{ly-2:.0f}" fill="#161616" font-size="13" font-weight="700">{name}</text>')
        parts.append(f'<text x="562" y="{ly+14:.0f}" fill="#777" font-size="11">{desc}</text>')
        y += h + gap
    return (f'<svg viewBox="0 0 820 {y+6}" width="100%" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Helvetica,Arial">'
            f'<text x="10" y="40" fill="#EE0000" font-size="11" font-weight="700">GENERAL ▲</text>'
            f'<text x="8" y="{y-8}" fill="#EE0000" font-size="11" font-weight="700">SPECIFIC ▼</text>'
            + "".join(parts) + '</svg>')


owl_uri = ""
if os.path.exists(OWL):
    import base64
    owl_uri = "data:image/png;base64," + base64.b64encode(open(OWL, "rb").read()).decode()

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>
@page {{ size: letter; margin: 14mm; }}
* {{ box-sizing: border-box; }}
body {{ font: 10.5pt/1.45 -apple-system, Helvetica, Arial, sans-serif; color: #161616; }}
header {{ display:flex; align-items:center; gap:14px; border-bottom:3px solid #EE0000; padding-bottom:10px; margin-bottom:14px; }}
header img {{ width:54px; height:54px; }}
header .w {{ font-weight:700; font-size:20pt; letter-spacing:.5px; }}
header .s {{ color:#808080; font-size:10pt; }}
header .tag {{ margin-left:auto; color:#EE0000; font-weight:700; font-size:12pt; }}
h2 {{ color:#EE0000; font-size:13pt; margin:16px 0 6px; border-bottom:1px solid #ddd; padding-bottom:3px; }}
h3 {{ font-size:11pt; margin:10px 0 4px; }}
.n {{ color:#808080; font-weight:400; font-size:9pt; }}
ul {{ margin:4px 0 8px; padding-left:18px; }}
li {{ margin:2px 0; }}
.t {{ color:#444; font-weight:400; }}
.blurb {{ color:#666; font-style:italic; margin:2px 0 4px; }}
ul.compact {{ columns:2; column-gap:24px; }}
ul.compact li {{ break-inside:avoid; }}
.lead {{ background:#f6f6f6; border-left:4px solid #EE0000; padding:8px 12px; margin:8px 0 14px; }}
table {{ border-collapse:collapse; width:100%; font-size:9.5pt; margin:6px 0; }}
th,td {{ border:1px solid #ddd; padding:4px 8px; text-align:left; }}
th {{ background:#161616; color:#fff; }}
.cols {{ display:flex; gap:24px; }} .cols>div {{ flex:1; }}
footer {{ margin-top:16px; border-top:1px solid #ddd; padding-top:6px; color:#808080; font-size:8.5pt; }}
</style></head><body>
<header>
  {'<img src="'+owl_uri+'">' if owl_uri else ''}
  <div><div class=w>ED'S RULES — LAYERED EDITION</div><div class=s>synopsis · axiom core + composable preference layers</div></div>
  <div class=tag>DRAFT · branch rules-taxonomy</div>
</header>

<div class=lead><b>The shift.</b> The flat 100 becomes a small <b>immutable axiom core ({len(AX)})</b>
plus <b>composable preference layers</b> — personal/architect, project, employer. The
count is no longer fixed; mis-scoped rules (a role rule graded as an axiom) stop being
"low quality" and move to the layer they belong to.</div>

<div class=lead><b>Why: rules are a cache hierarchy.</b> No small model holds 100 rules
(sizing law: ~1 rule per billion parameters). Each seat holds a <b>resident</b> working
set sized to its budget; the rest is <b>paged</b> into context on demand. The crew's
resident union is its memorized canon — so the axioms must be <i>few</i>.</div>

<h2>The shape — an inverted pyramid (slice width = rule count)</h2>
<p class=blurb>Most general / axiomatic at the top (widest); most app- and person-specific at the bottom (narrowest). Rules get fewer as they get more specific.</p>
{pyramid_svg()}

<h2>The axiom core — {len(AX)} immutable, universal rules</h2>
{axiom_groups()}

<h2>Preference layers</h2>
{layer_block('personal')}
<div class=cols><div>{layer_block('project')}</div><div>{layer_block('bardinfra')}</div></div>
{layer_block('employer')}

<h2>The crew &amp; the composer</h2>
<p>Each project picks layers and a crew; <code>compose.py</code> emits a per-seat slice
sized to the model's rule budget, plus the paged tail. Worked 3-crew (the "Guy" branch):</p>
<table>
<tr><th>Seat</th><th>Role</th><th>Model</th><th>Budget</th></tr>
{crew_rows()}
</table>
<p><b>Worked numbers:</b> cloud-native project = <b>{NAX+NPERS+NPROJ+NEMP}</b> active rules
({NAX} axioms + {NPERS} personal + {NPROJ} project + {NEMP} employer); bard-infra =
<b>{NAX+NPERS+NINFRA}</b> ({NAX} axioms + {NPERS} personal + {NINFRA} bard-infra). <b>Guy's test:</b>
the {NAX}-axiom core needs ~{NAX}B of summed budget to be fully resident; a frontier-free
8B+14B crew (22B) is just short — a frontier seat (Opus) covers it, which this crew has.</p>

<footer>Generated from taxonomy/rules.yaml · github.com/edhaynes/eds-rules · CC-BY-4.0 ·
Decision (2026-06-16): axiom core kept at {len(AX)}, no trim.</footer>
</body></html>"""

out = os.path.join(HERE, "generated", "synopsis.html")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w").write(HTML)
print(out)
