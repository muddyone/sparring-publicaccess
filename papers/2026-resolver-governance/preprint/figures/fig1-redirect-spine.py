#!/usr/bin/env python3
"""
fig1-redirect-spine.py — generate Figure 1 of the V2 governance preprint.

THE REDIRECT SPINE. A Cleveland dot plot of judge-vs-human agreement (Spearman ρ)
per rubric criterion, GROUPED by whether the process evidence stayed visible after
the format-symmetric blinding. The paper's central claim (§5.1) is that agreement
held exactly where the blind left evidence visible (C1) and collapsed where it
stripped it (C2, C3). This figure lets a reader see that pattern at a glance instead
of reconstructing it from the §4.1 table plus the §5.1 prose.

DESIGN DISCIPLINE (Minard, the data-graphics reviewer):
  * Reproducible artifact — reads the frozen results, no hand-typed numbers:
        ../analysis/primary-results.json  ->  gate_primary_unaided
  * Encoding fit (Cleveland) — position on a common scale, the most accurately read
    encoding for quantity; criterion on the category axis.
  * Graphical integrity — honest [-1, +1] ρ axis; the pass/fail thresholds DIFFER by
    criterion tier (high-stakes vs. inference-heavy), so they are drawn PER ROW rather
    than as one global band that would misrepresent the inference-heavy criteria.
  * Uncertainty must be visible (the project's cardinal rule) — each ρ rests on only
    n=4 paired points; that, the 6-rater reference, and the fact that the pattern is
    directional-not-clean (C4, partly visible, also fails) are stated ON the figure.
  * Honesty about the undefined cell — C5a has no ρ (judges scored a flat 6/7); it is
    shown as an explicit INDETERMINATE row, never dropped or faked to a position.

  Zero non-stdlib dependencies (no matplotlib / numpy). Output is a standalone SVG that
  embeds natively in the pandoc HTML build (the canonical clean artifact). For the
  xelatex PDF build, an SVG needs rsvg-convert installed; see figures/README.md.

Usage:   python3 figures/fig1-redirect-spine.py
Output:  figures/fig1-redirect-spine.svg
"""

import json
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "..", "analysis", "primary-results.json")
OUT = os.path.join(HERE, "fig1-redirect-spine.svg")

# --- criterion metadata: code, short label, evidence-visibility group, tier ----------
# Visibility (§5.1): does the criterion's evidence survive flattening both answers to
# the same four-section shape?  visible = leaves a fingerprint in the finished text;
# partial = partly visible; stripped = the adversarial trace is gone.
# Tier (§3.4): high-stakes {C1,C2,C5a,C5b} pass>=0.70 / fail<0.40;
#              inference-heavy {C3,C4}     pass>=0.50 / fail<0.20.
# Rows are ordered by the INDEPENDENT variable (visibility), not sorted by outcome —
# sorting by ρ would be circular. Within that, the outcome is left to fall where it does.
CRITERIA = [
    # key,  code,  label,                          group,      tier
    ("c1",  "C1",  "Verifiable-artifact citation",  "visible",  "high"),
    ("c5a", "C5a", "Factual accuracy vs. briefing",  "visible",  "high"),
    ("c5b", "C5b", "Engagement with source",         "partial",  "high"),
    ("c4",  "C4",  "Calibrated confidence",          "partial",  "low"),
    ("c2",  "C2",  "Substantive vs. theatrical",     "stripped", "high"),
    ("c3",  "C3",  "Missed real concerns",           "stripped", "low"),
]

THRESHOLDS = {"high": {"pass": 0.70, "fail": 0.40}, "low": {"pass": 0.50, "fail": 0.20}}

GROUPS = {
    "visible":  ("Evidence visible after blinding",   "#1f6f8b", "circle"),
    "partial":  ("Partly visible",                    "#c98a1b", "square"),
    "stripped": ("Evidence stripped by blinding",     "#9b2d2d", "triangle"),
}

VERDICT_COLOR = {
    "PASS": "#2e7d5b", "FAIL": "#b5483d",
    "BORDERLINE": "#c98a1b", "INDETERMINATE": "#777777",
}

# --- canvas geometry ------------------------------------------------------------------
W, H = 980, 612
ML, MR, MT, MB = 300, 196, 128, 120          # margins; left holds labels, right ρ+verdict
LEFT = 48                                      # full-bleed left edge for title/caption/legend/footer
PX0, PX1 = ML, W - MR                          # plot x-range (ρ = -1 .. +1)
PLOT_W = PX1 - PX0
ROW_H = 46
GROUP_GAP = 26
Y_START = MT + 36
SERIF = "'TeX Gyre Pagella', Palatino, 'Palatino Linotype', Georgia, serif"


def xmap(r):
    """ρ in [-1, +1] -> pixel x (position on a common scale: Cleveland's most-accurate encoding)."""
    return PX0 + (r + 1.0) / 2.0 * PLOT_W


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def main():
    with open(RESULTS) as fh:
        data = json.load(fh)
    block = data["gate_primary_unaided"]
    rho = block["per_criterion_rho"]
    klass = block["per_criterion_class"]
    n_raters = block["n_raters"]
    agg = block["gate"]["aggregate"]

    svg = []
    svg.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="{SERIF}">'
    )
    svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')

    # --- title + subtitle ------------------------------------------------------------
    svg.append(
        f'<text x="{LEFT}" y="40" font-size="18" font-weight="bold" fill="#1a1a1a">'
        'AI judges and people agreed where the evidence stayed visible — and split where it was hidden</text>'
    )
    svg.append(
        f'<text x="{LEFT}" y="66" font-size="13" fill="#444">'
        f'Judge–human rank agreement (Spearman ρ) by rubric criterion, grouped by whether the '
        'process evidence</text>'
    )
    svg.append(
        f'<text x="{LEFT}" y="84" font-size="13" fill="#444">'
        f'stayed visible after both answers were flattened to the same shape. '
        f'Reference: {n_raters} unaided raters. Gate: <tspan font-weight="bold">{esc(agg)}</tspan>.</text>'
    )

    # --- ρ axis (top of plot) --------------------------------------------------------
    axis_y = MT
    svg.append(f'<line x1="{PX0}" y1="{axis_y}" x2="{PX1}" y2="{axis_y}" stroke="#888" stroke-width="1"/>')
    for tick in (-1.0, -0.5, 0.0, 0.5, 1.0):
        tx = xmap(tick)
        svg.append(f'<line x1="{tx:.1f}" y1="{axis_y-4}" x2="{tx:.1f}" y2="{axis_y}" stroke="#888"/>')
        svg.append(
            f'<text x="{tx:.1f}" y="{axis_y-8}" font-size="11" fill="#666" text-anchor="middle">'
            f'{tick:+.1f}</text>'.replace("+0.0", "0.0")
        )
    svg.append(
        f'<text x="{(PX0+PX1)/2:.0f}" y="{MT-30}" font-size="11.5" fill="#666" text-anchor="middle" '
        'font-style="italic">Spearman ρ  (−1 = ranked oppositely · 0 = unrelated · +1 = same order)</text>'
    )

    # --- zero reference line (full height of the rows) -------------------------------
    rows_bottom = Y_START + len(CRITERIA) * ROW_H + 2 * GROUP_GAP
    zx = xmap(0.0)
    svg.append(f'<line x1="{zx:.1f}" y1="{axis_y}" x2="{zx:.1f}" y2="{rows_bottom:.0f}" '
               'stroke="#cccccc" stroke-width="1" stroke-dasharray="2,3"/>')

    # --- rows ------------------------------------------------------------------------
    y = Y_START
    prev_group = None
    for key, code, label, group, tier in CRITERIA:
        if group != prev_group:
            y += GROUP_GAP
            gname, gcolor, _ = GROUPS[group]
            svg.append(f'<line x1="{LEFT}" y1="{y-22:.0f}" x2="{PX1}" y2="{y-22:.0f}" stroke="#e6e6e6"/>')
            svg.append(
                f'<text x="{LEFT}" y="{y-9:.0f}" font-size="11.5" font-weight="bold" '
                f'fill="{gcolor}" letter-spacing="0.3">{esc(gname.upper())}</text>'
            )
            prev_group = group

        cy = y
        thr = THRESHOLDS[tier]
        gname, gcolor, shape = GROUPS[group]

        # faint travel guide
        svg.append(f'<line x1="{PX0}" y1="{cy:.1f}" x2="{PX1}" y2="{cy:.1f}" stroke="#f2f2f2" stroke-width="1"/>')

        # per-row pass/fail threshold ticks (drawn per row because tiers differ)
        for thr_val, col in ((thr["pass"], VERDICT_COLOR["PASS"]), (thr["fail"], VERDICT_COLOR["FAIL"])):
            tx = xmap(thr_val)
            svg.append(f'<line x1="{tx:.1f}" y1="{cy-14:.1f}" x2="{tx:.1f}" y2="{cy+14:.1f}" '
                       f'stroke="{col}" stroke-width="1.4" opacity="0.55"/>')

        # left label
        svg.append(
            f'<text x="{ML-26}" y="{cy+5:.1f}" font-size="13.5" fill="#1a1a1a" text-anchor="end">'
            f'<tspan font-weight="bold">{code}</tspan>  {esc(label)}</text>'
        )

        r = rho[key]["rho"]
        npts = rho[key]["n"]
        verdict = klass[key]["class"]
        vcol = VERDICT_COLOR[verdict]

        if r is None:
            # INDETERMINATE — no position is honest. Mark it, do not invent a point.
            svg.append(
                f'<text x="{PX0+6:.1f}" y="{cy+5:.1f}" font-size="12" fill="#777" font-style="italic">'
                'ρ undefined — judges scored a flat 6/7 (no variance to rank)</text>'
            )
        else:
            dx = xmap(r)
            if shape == "circle":
                svg.append(f'<circle cx="{dx:.1f}" cy="{cy:.1f}" r="7" fill="{gcolor}" '
                           'stroke="#ffffff" stroke-width="1"/>')
            elif shape == "square":
                svg.append(f'<rect x="{dx-6.5:.1f}" y="{cy-6.5:.1f}" width="13" height="13" '
                           f'fill="{gcolor}" stroke="#ffffff" stroke-width="1"/>')
            else:  # triangle
                svg.append(
                    f'<polygon points="{dx:.1f},{cy-7.8:.1f} {dx-7.2:.1f},{cy+6:.1f} {dx+7.2:.1f},{cy+6:.1f}" '
                    f'fill="{gcolor}" stroke="#ffffff" stroke-width="1"/>'
                )

        # right: ρ value + verdict + n
        rho_txt = "n/a" if r is None else f"{r:+.2f}".replace("+", " ")
        svg.append(
            f'<text x="{PX1+14}" y="{cy+1:.1f}" font-size="13" fill="#1a1a1a">'
            f'<tspan font-weight="bold">ρ = {rho_txt}</tspan></text>'
        )
        svg.append(
            f'<text x="{PX1+14}" y="{cy+16:.1f}" font-size="10.5" fill="{vcol}">'
            f'{verdict} · n={npts}</text>'
        )

        y += ROW_H

    # --- legend ----------------------------------------------------------------------
    ly = rows_bottom + 30
    lx = LEFT
    svg.append(f'<text x="{lx}" y="{ly}" font-size="11.5" font-weight="bold" fill="#444">Visibility group</text>')
    seg = lx + 110
    for group in ("visible", "partial", "stripped"):
        gname, gcolor, shape = GROUPS[group]
        if shape == "circle":
            svg.append(f'<circle cx="{seg}" cy="{ly-4}" r="6" fill="{gcolor}"/>')
        elif shape == "square":
            svg.append(f'<rect x="{seg-6}" y="{ly-10}" width="12" height="12" fill="{gcolor}"/>')
        else:
            svg.append(f'<polygon points="{seg},{ly-11} {seg-6.5},{ly+2} {seg+6.5},{ly+2}" fill="{gcolor}"/>')
        svg.append(f'<text x="{seg+12}" y="{ly}" font-size="11.5" fill="#444">{esc(gname)}</text>')
        seg += 22 + len(gname) * 6.7

    ly2 = ly + 22
    svg.append(
        f'<line x1="{lx+2}" y1="{ly2-10}" x2="{lx+2}" y2="{ly2+4}" stroke="{VERDICT_COLOR["PASS"]}" '
        'stroke-width="1.6" opacity="0.7"/>'
        f'<text x="{lx+10}" y="{ly2}" font-size="11" fill="#555">pass threshold</text>'
        f'<line x1="{lx+118}" y1="{ly2-10}" x2="{lx+118}" y2="{ly2+4}" stroke="{VERDICT_COLOR["FAIL"]}" '
        'stroke-width="1.6" opacity="0.7"/>'
        f'<text x="{lx+126}" y="{ly2}" font-size="11" fill="#555">fail threshold '
        '(both vary by criterion tier: high-stakes 0.70/0.40, inference-heavy 0.50/0.20)</text>'
    )

    # --- caveat footer (the cardinal integrity rule, on the figure) ------------------
    fy = ly2 + 26
    svg.append(
        f'<text x="{lx}" y="{fy}" font-size="11" fill="#8a2f2f" font-style="italic">'
        'Directional, small-n: each ρ is computed on only n=4 paired points — small-sample rank '
        'correlations are highly unstable (§4.5).</text>'
    )
    svg.append(
        f'<text x="{lx}" y="{fy+16}" font-size="11" fill="#8a2f2f" font-style="italic">'
        'The pattern is directional, not clean: C4 (partly visible) also fails. '
        'Source: analysis/primary-results.json · gate_primary_unaided.</text>'
    )

    svg.append("</svg>")
    out = "\n".join(svg)

    # self-check: the SVG must be well-formed XML before we write it.
    try:
        ET.fromstring(out)
    except ET.ParseError as e:
        print(f"[fig1] ERROR: generated SVG is not well-formed XML: {e}", file=sys.stderr)
        sys.exit(1)

    with open(OUT, "w") as fh:
        fh.write(out)
    print(f"[fig1] wrote {os.path.relpath(OUT)}  ({len(out)} bytes, well-formed)")
    # echo the data actually plotted, so a reviewer can diff figure against frozen source
    print("[fig1] plotted from gate_primary_unaided:")
    for key, code, label, group, tier in CRITERIA:
        r = rho[key]["rho"]
        print(f"        {code:4s} {group:8s} {tier:4s}  rho={('undef' if r is None else f'{r:+.4f}')}"
              f"  -> {klass[key]['class']}")


if __name__ == "__main__":
    main()
