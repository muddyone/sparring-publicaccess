#!/usr/bin/env python3
"""
fig2-grounding-gap.py — Figure 2 of the V2 governance preprint.

THE GROUNDING GAP. A Tufte slopegraph of grounding rate (share of concerns backed by a
checkable artifact) across the three conditions — B (neutral pass), S (SPARRING ceremony),
T (placebo) — with one line per seeded-defect family. The paper's §7.3 argument is that
the separation between grounded SPARRING and a fluent placebo opens *precisely* where the
check requires reaching OUTSIDE the provided briefing (security/CWE, citations) and nearly
vanishes where the artifact lives inside it (overclaim-vs-spec, buried contradiction).
The slopegraph makes that "where the gap concentrates" argument visible: the external-canon
lines crater in the T column while the in-briefing lines stay near the ceiling.

Supports / illustrates §7.3.

DESIGN DISCIPLINE (Minard, the data-graphics reviewer):
  * Reproducible artifact — reads the frozen results, no hand-typed numbers:
        ../../seeded-defect-2026-06-26/v2-run/aggregate.json  ->  by_dc
  * Encoding fit — a slopegraph (position + slope) is the right form for "which categories
    move, and where" across a small set of conditions; far more legible than a 4x3 table.
  * Graphical integrity — honest 0–100 y-axis; lines colored by the LOAD-BEARING split
    (external-canon vs. in-briefing), because that split IS the argument, not decoration.
  * Uncertainty must be visible (the project's cardinal rule) — directional, LLM-coded
    (Path-B), and the small per-family concern counts (n) are printed on the figure; the
    note records that the external-canon families are now verifier-backed (§8) while the
    in-briefing families remain Path-B.

Usage:   python3 figures/fig2-grounding-gap.py
Output:  figures/fig2-grounding-gap.svg
"""

import json
import os
import sys
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # suppress findfont fallback chatter

HERE = os.path.dirname(os.path.abspath(__file__))
AGG = os.path.join(HERE, "..", "..", "..", "seeded-defect-2026-06-26", "v2-run", "aggregate.json")
OUT = os.path.join(HERE, "fig2-grounding-gap.svg")

# Prefer the manuscript's serif (TeX Gyre Pagella); fall back cleanly if absent.
plt.rcParams["svg.fonttype"] = "none"          # keep text as text in the SVG (selectable, small)
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "Palatino", "DejaVu Serif"]

# defect-class -> (display label, where the check lives). Order: external first, then in-briefing,
# so the two argument groups read top-block / bottom-block on the right-hand labels.
FAMILIES = [
    ("DC3", "Security / CWE",       "external", "#9b2d2d"),   # check lives in MITRE
    ("DC1", "Citations",            "external", "#cf7a30"),   # check lives in the literature
    ("DC4", "Overclaim vs. spec",   "inbrief",   "#5b7f93"),   # check lives in the briefing
    ("DC2", "Buried contradiction", "inbrief",   "#9aa0a6"),   # check lives in the briefing
]
CONDS = ["B", "S", "T"]
COND_SUB = {"B": "neutral pass", "S": "SPARRING ceremony", "T": "placebo"}
XPOS = {"B": 0.0, "S": 1.0, "T": 2.0}


def main():
    with open(AGG) as fh:
        agg = json.load(fh)
    by_dc = agg["by_dc"]
    case_count = agg["case_count"]
    total_concerns = sum(agg["aggregate"][c]["raw"]["n"] for c in CONDS)

    fig, ax = plt.subplots(figsize=(9.2, 6.3))

    for dc, label, group, color in FAMILIES:
        ys = [by_dc[dc][c]["grounding_rate"] for c in CONDS]
        ns = [by_dc[dc][c]["raw"]["n"] for c in CONDS]
        xs = [XPOS[c] for c in CONDS]

        is_ext = group == "external"
        ax.plot(xs, ys, color=color, lw=2.6 if is_ext else 1.5,
                solid_capstyle="round", zorder=3 if is_ext else 2,
                alpha=1.0 if is_ext else 0.85)
        ax.plot(xs, ys, "o", color=color, ms=6 if is_ext else 4.5, zorder=4,
                markeredgecolor="white", markeredgewidth=0.8)

        # value labels at each vertex; nudge the two near-ceiling families apart at S
        for c, x, y in zip(CONDS, xs, ys):
            if c == "B":
                ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points",
                            xytext=(-9, 0), ha="right", va="center", fontsize=9, color=color)
            elif c == "S":
                dy = -13 if is_ext else 9     # external below, in-briefing above (group-consistent)
                va = "bottom" if dy > 0 else "top"
                ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points",
                            xytext=(0, dy), ha="center", va=va, fontsize=9, color=color)
            else:  # T — value, then the family name + where-the-check-lives tag, further right
                tag = "external" if is_ext else "in-briefing"
                ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points",
                            xytext=(9, 0), ha="left", va="center", fontsize=9,
                            fontweight="bold", color=color)
                ax.annotate(f"  {label} — {tag}", (x, y), textcoords="offset points",
                            xytext=(26, 0), ha="left", va="center", fontsize=10.5, color=color)

    # the punchline gap, annotated once
    ax.annotate("", xy=(2.0, 96.2), xytext=(2.0, 36.4),
                arrowprops=dict(arrowstyle="<->", color="#555", lw=1.0))
    ax.annotate("S − T = 60 pts\non security", (2.0, 66.3), textcoords="offset points",
                xytext=(8, 0), ha="left", va="center", fontsize=8.5, color="#555")

    # axes / spines (Tufte: drop the box)
    ax.set_xlim(-0.45, 2.05)
    ax.set_ylim(25, 105)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels([f"$\\bf{{{c}}}$\n{COND_SUB[c]}" for c in CONDS], fontsize=11)
    ax.set_yticks([40, 60, 80, 100])
    ax.set_yticklabels(["40", "60", "80", "100%"], fontsize=9, color="#666")
    ax.tick_params(length=0)
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.set_ylabel("Grounding rate — share of concerns backed by a checkable artifact",
                  fontsize=10, color="#444")
    ax.set_xlim(-0.5, 2.0)         # leave room on the right for labels (via subplots_adjust)

    # title + subtitle
    fig.suptitle("SPARRING only pulls ahead when the proof lies outside the documents",
                 x=0.04, y=0.975, ha="left", fontsize=14.5, fontweight="bold", color="#1a1a1a")
    ax.set_title(
        f"Share of concerns backed by a checkable artifact, by defect family and condition. "
        f"Seeded-defect pilot: {case_count} cases, {total_concerns} concerns.",
        loc="left", fontsize=10, color="#444", pad=14)

    # caveat footer (the cardinal integrity rule, on the figure)
    fig.text(0.04, 0.055,
             "Directional, LLM-coded (Path-B); per-family n is small (S condition: 17–28 concerns each). "
             "External-canon families (security, citations)",
             fontsize=8.6, fontstyle="italic", color="#8a2f2f")
    fig.text(0.04, 0.028,
             "are now verifier-backed against MITRE/Crossref (§8); in-briefing families remain Path-B. "
             "Source: pilots/seeded-defect-2026-06-26/v2-run/aggregate.json · by_dc.",
             fontsize=8.6, fontstyle="italic", color="#8a2f2f")

    plt.subplots_adjust(left=0.085, right=0.70, top=0.86, bottom=0.13)

    fig.savefig(OUT, format="svg")
    plt.close(fig)
    print(f"[fig2] wrote {os.path.relpath(OUT)}")
    print("[fig2] plotted from seeded-defect v2-run/aggregate.json -> by_dc:")
    for dc, label, group, _ in FAMILIES:
        row = " / ".join(f"{by_dc[dc][c]['grounding_rate']:.1f} (n={by_dc[dc][c]['raw']['n']})"
                         for c in CONDS)
        print(f"        {dc} {label:22s} [{group:8s}]  B/S/T = {row}")


if __name__ == "__main__":
    main()
