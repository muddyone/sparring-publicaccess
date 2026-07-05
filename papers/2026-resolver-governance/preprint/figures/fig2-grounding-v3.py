#!/usr/bin/env python3
"""
fig2-grounding-v3.py — the v3 grounding figure for §7.2 (RE-CUT as a Cleveland dot plot).

SUPERSEDES the earlier 2-D "theater map" scatter of the same name. That scatter spent a
whole perceptual axis (legitimacy/precision = 100/100/50) on a near-degenerate dimension
that was silent on the load-bearing S-vs-T comparison, and its quadrant scaffolding +
"15% strawman ghost" annotation kept alive the theater-knockout frame that §7.2 RETIRED as
a strawman artifact. The honest v3 story is a magnitude comparison of one number —
GROUNDING RATE — so it is drawn as a dot plot: position on a common 0-100 scale, the
encoding the eye reads most accurately for quantity (Cleveland). Precision rides along as a
secondary annotation; it is not given its own axis because on the load-bearing S-vs-T
contrast it is identical (100/100) and carries no information there.

The argument (§7.2): the DURABLE result is S's wide, precision-free lead over a raw single
pass (B); the edge over a realistic *competent* skeptic (T) is marginal (~13 pts, n=12).

DESIGN DISCIPLINE (Minard): earn the ink (one honest comparison, no quadrant ornament);
honest 0-100 axis; uncertainty ON the figure (n, directional/no-sig-test, machine-verified
grounding vs. LLM-coded legitimacy/precision). Reproducible: fixed svg.hashsalt + no embedded
date, so re-runs are byte-identical.

Source: ../../../seeded-defect-2026-06-26/v3-run/aggregate.json (Path-A judged).
Usage:  python3 figures/fig2-grounding-v3.py   ->  figures/fig2-grounding-v3.svg
"""

import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "sparring-v3-fig2-dot"   # deterministic element ids
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
AGG = os.path.join(HERE, "..", "..", "..", "seeded-defect-2026-06-26", "v3-run", "aggregate.json")
OUT = os.path.join(HERE, "fig2-grounding-v3.svg")
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "Palatino", "DejaVu Serif"]
plt.rcParams["svg.fonttype"] = "none"

# condition -> (display label, color, marker). Rows ordered top->bottom by grounding (S,T,B).
COND = {
    "S": ("S - SPARRING ceremony",          "#1f6f4a", "o"),
    "T": ("T - realistic competent skeptic", "#c98a1b", "s"),
    "B": ("B - raw single pass",            "#9b2d2d", "^"),
}
ORDER = ["S", "T", "B"]   # top to bottom


def main():
    doc = json.load(open(AGG))
    agg = doc["aggregate"]
    case_count = doc["case_count"]
    total = sum(agg[c]["concerns"] for c in "BST")

    fig, ax = plt.subplots(figsize=(9.4, 4.8))
    ys = {c: i for i, c in enumerate(reversed(ORDER))}  # B=0,T=1,S=2 -> S plots on top

    for c in ORDER:
        label, color, marker = COND[c]
        g = agg[c]["grounding_rate"]; p = agg[c]["precision"]; n = agg[c]["concerns"]
        y = ys[c]
        # faint full-width guide so the eye can read position on the common scale
        ax.plot([0, 100], [y, y], color="#f0f0f0", lw=1, zorder=1)
        ax.scatter([g], [y], s=330, c=color, marker=marker, edgecolors="white",
                   linewidths=1.5, zorder=5)
        # grounding value just right of the dot
        ax.annotate(f"{g:.0f}%", (g, y), textcoords="offset points", xytext=(13, 0),
                    ha="left", va="center", fontsize=12, fontweight="bold", color=color, zorder=6)
        # condition label + precision (secondary) at the left gutter
        ax.annotate(label, (0, y), textcoords="offset points", xytext=(-12, 6),
                    ha="right", va="center", fontsize=11, color=color, zorder=6)
        ax.annotate(f"precision {p:.0f}% · n={n}", (0, y), textcoords="offset points",
                    xytext=(-12, -9), ha="right", va="center", fontsize=8.6,
                    fontstyle="italic", color="#777", zorder=6)

    # --- the two load-bearing comparisons, annotated on the figure ---
    yS, yT, yB = ys["S"], ys["T"], ys["B"]
    gS = agg["S"]["grounding_rate"]; gT = agg["T"]["grounding_rate"]; gB = agg["B"]["grounding_rate"]

    # marginal S-T edge: bracket between the two dots near the top
    ymid = (yS + yT) / 2
    ax.annotate("", xy=(gS, ymid), xytext=(gT, ymid),
                arrowprops=dict(arrowstyle="<->", color="#888", lw=1.0))
    ax.text((gS + gT) / 2, ymid + 0.13,
            f"S - T ≈ {gS-gT:.0f} pts  (marginal; n={case_count}, no sig. test)",
            ha="center", va="bottom", fontsize=8.6, fontstyle="italic", color="#666")

    # durable S-B win: low bracket spanning the wide gap
    ax.annotate("", xy=(gS, yB - 0.34), xytext=(gB, yB - 0.34),
                arrowprops=dict(arrowstyle="<->", color="#256b4e", lw=1.1))
    ax.text((gS + gB) / 2, yB - 0.50,
            f"S - B = {gS-gB:.0f} pts  - the durable win, at no precision cost (S 100% vs B 50%)",
            ha="center", va="top", fontsize=8.8, fontstyle="italic", color="#256b4e")

    ax.set_xlim(0, 100)
    ax.set_ylim(-0.95, 2.6)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9, color="#666")
    ax.set_xlabel("Grounding rate - share of a condition's concerns backed by a checkable, machine-verified artifact",
                  fontsize=10, color="#333")
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#bbb")
    ax.tick_params(length=0)

    fig.suptitle("SPARRING's critique is grounded - the durable win is over a raw single pass, "
                 "not over a competent skeptic",
                 x=0.5, y=0.975, fontsize=12.0, fontweight="bold", color="#1a1a1a")
    ax.set_title("v3 seeded-defect pilot. Each condition placed by its grounding rate on a common scale. S leads a raw\n"
                 "pass (B) by a wide margin at no precision cost; its edge over a competent skeptic (T) is marginal.",
                 fontsize=8.8, color="#444", pad=10)

    fig.text(0.5, 0.055,
             "Grounding is machine-verified (existence model-free vs. public registries / the saved briefing; "
             "correct-application cross-vendor, Claude+OpenAI - §8).",
             ha="center", fontsize=7.6, fontstyle="italic", color="#8a2f2f")
    fig.text(0.5, 0.030,
             "Precision/legitimacy is LLM-coded and awaits the domain-expert audit. Directional: "
             f"n={case_count} cases / {total} concerns, no significance test. Source: v3-run/aggregate.json.",
             ha="center", fontsize=7.6, fontstyle="italic", color="#8a2f2f")

    plt.subplots_adjust(left=0.27, right=0.93, top=0.80, bottom=0.21)
    fig.savefig(OUT, format="svg", metadata={"Date": None})
    plt.close(fig)
    print(f"[fig2-v3 dotplot] wrote {os.path.relpath(OUT)}")
    for c in ORDER:
        a = agg[c]
        print(f"   {c}: grounding={a['grounding_rate']:.1f}%  precision={a['precision']:.1f}%  n={a['concerns']}")
    print(f"   S-T = {gS-gT:.1f} pts ; S-B = {gS-gB:.1f} pts")


if __name__ == "__main__":
    main()
