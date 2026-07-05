#!/usr/bin/env python3
"""
fig5-gate-null.py — Figure 5 of the governance preprint (§6.4): the gate's
pre-committed output-quality null, and *why* it happens.

WHAT THE FIGURE ARGUES
  Iterating a challenge to agreement (R2, the both-must-agree gate — SPARRING's
  named distinctive niche, §2) leaves NO FEWER net material flaws in the final
  output than a single challenge-and-fix (R1): the pre-committed null (R2-R1 ~ 0).
  The mechanism is the point, and a stacked bar makes it legible: each condition's
  net-flaws-remaining bar is split into
      (originals still remaining)  +  (NEW flaws the revision introduced).
  The adversarial challenge is a better *detector* — it removes ~87% of the
  producer's original blind-spot flaws (the dark segment collapses from 3.875 to
  ~0.5) — but revising *under adversarial pressure* seeds ~2 NEW flaws (the amber
  segment grows), while a quiet self-revision (R1') seeds only ~1.25. The detection
  win and the churn cost cancel, so the totals (bar lengths) barely move — and the
  effort-matched self-revision control quietly wins. Lower is better.

DESIGN DISCIPLINE (Minard)
  * Reproducible artifact — every NET total is read from the frozen, committed
        ../../../resolver-iteration-2026-06-29/analysis/results-aggregate.json
    (means_net_flaws_remaining) and asserted against the hardcoded values. The
    (original-remaining + new-introduced) SPLIT is transcribed from that pilot's
    results.md table (§ "Net material flaws remaining") because the aggregate JSON
    stores only the net totals, not the split — so the split carries an explicit
    source comment and an assert that each split sums to the JSON-backed net.
  * Honest length encoding — zero-based common x-axis (net flaws 0..~4.2), no
    truncation; bar LENGTH (Cleveland rank 2) reads the net DV directly, and the
    near-equal R1/R2 bar lengths ARE the null, shown honestly, not narrated away.
  * Uncertainty must be visible — the caveat rides on the figure: directional,
    n=8, model-established ground truth (>=2-of-3 panel), no significance test,
    absolute new-flaw levels are upper bounds (fresh-panel baseline). A null must
    not be dressed as a clean finding, and a null must not be visually inflated
    into a "difference" — the honest read here is "these bars are the same length."

Usage:   python3 figures/fig5-gate-null.py
Output:  figures/fig5-gate-null.svg
"""

import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "sparring-v2-fig5-gate-null"  # deterministic ids
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
AGG = os.path.join(HERE, "..", "..", "..", "resolver-iteration-2026-06-29",
                   "analysis", "results-aggregate.json")
OUT = os.path.join(HERE, "fig5-gate-null.svg")

plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "Palatino", "DejaVu Serif"]

# --- Palette (house muted set, from fig4) -----------------------------------
C_ORIG = "#46707d"   # desaturated teal-blue: producer's ORIGINAL blind-spot flaws still remaining
C_NEW  = "#9a6a1f"   # amber: NEW flaws the revision introduced (the churn cost)
C_ANCHOR = "#8a8f94" # grey: the ship-as-is anchor line
INK   = "#1a1a1a"
BODY  = "#444444"
CAVEAT = "#8a2f2f"

# --- Data --------------------------------------------------------------------
# key -> (row label line 1, row label line 2, original-remaining, new-introduced)
# NET totals are asserted against results-aggregate.json below.
# SPLIT is transcribed from resolver-iteration-2026-06-29/results.md, table
# "Net material flaws remaining (the pre-registered DV ...)". The aggregate JSON
# stores only the net totals; the original/new split lives in results.md.
ROWS = [
    ("R0.anchor",  "Ship as-is",                 "anchor — no revision",          3.875, 0.000),
    ("R1prime",    "Self-revise ×2",        "no challenger (effort-matched)",     1.000, 1.250),
    ("R1.same",    "Single challenge",           "same-vendor",                        0.500, 2.125),
    ("R2.same",    "Iterate to agreement",       "same-vendor  (the gate)",            0.625, 2.000),
    ("R1.cross",   "Single challenge",           "cross-vendor",                       0.500, 2.625),
    ("R2.cross",   "Iterate to agreement",       "cross-vendor  (the gate)",           0.750, 2.250),
]

# JSON key mapping for the net-total cross-check
JSON_KEY = {
    "R0.anchor": "R0", "R1prime": "R1prime",
    "R1.same": "R1.same", "R2.same": "R2.same",
    "R1.cross": "R1.cross", "R2.cross": "R2.cross",
}


def fmt(v):
    """Exact means (each is k/8); trim trailing zeros, keep them honest."""
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return s if s else "0"


def main():
    agg = json.load(open(AGG))
    means = agg["means_net_flaws_remaining"]

    # Integrity guards: every net total ties to the frozen JSON, every split sums to net.
    for key, _, _, orig, new in ROWS:
        net = orig + new
        jkey = JSON_KEY[key]
        assert abs(net - means[jkey]) < 1e-9, (
            f"{key}: split {orig}+{new}={net} != JSON net {means[jkey]}")
    ANCHOR = means["R0"]  # 3.875 — the ship-as-is denominator/anchor

    n = len(ROWS)
    # Native canvas kept near the paper's text-column width so the DOCX build (which
    # fits each figure to the column) barely downscales it — that is what keeps the
    # on-figure text legible in Word. The dense detail that used to sit in the
    # subtitle/caveat lines lives in the caption; the figure carries only the takeaway.
    fig, ax = plt.subplots(figsize=(7.6, 5.6))

    # rows top->bottom, with a visual gap between the two controls and the
    # challenged block. Build y positions directly (top row highest).
    ys, y, GAP = [], 0.0, 0.65
    for i in range(n):
        if i == 2:
            y += GAP           # air between the two controls and the challenged block
        ys.append(-y)
        y += 1.0
    top = max(ys)
    bot = min(ys)

    BAR_H = 0.60

    for (key, l1, l2, orig, new), yy in zip(ROWS, ys):
        net = orig + new
        ax.add_patch(Rectangle((0, yy - BAR_H/2), orig, BAR_H,
                               facecolor=C_ORIG, edgecolor="white", linewidth=1.2))
        ax.add_patch(Rectangle((orig, yy - BAR_H/2), new, BAR_H,
                               facecolor=C_NEW, edgecolor="white", linewidth=1.2))
        if orig >= 0.42:
            ax.text(orig/2, yy, fmt(orig), ha="center", va="center",
                    color="white", fontsize=11, fontweight="bold")
        if new >= 0.42:
            ax.text(orig + new/2, yy, fmt(new), ha="center", va="center",
                    color="white", fontsize=11, fontweight="bold")
        # net total at bar end (skip R0: its total IS the anchor line/label)
        if key != "R0.anchor":
            ax.text(net + 0.07, yy, f"{fmt(net)} net", ha="left", va="center",
                    color=INK, fontsize=11.5, fontweight="bold")
        # row label (two lines) to the left of zero
        ax.text(-0.10, yy + 0.15, l1, ha="right", va="center",
                color=INK, fontsize=12, fontweight="bold")
        ax.text(-0.10, yy - 0.18, l2, ha="right", va="center",
                color=BODY, fontsize=9.6)

    # --- the ship-as-is anchor reference line (the "do nothing" baseline) ---
    ax.plot([ANCHOR, ANCHOR], [bot - 0.5, top + 0.40],
            color=C_ANCHOR, lw=1.1, ls=(0, (4, 3)), zorder=0)
    ax.text(ANCHOR - 0.06, top + 0.52, f"ship-as-is anchor = {fmt(ANCHOR)}",
            ha="right", va="center", color=C_ANCHOR, fontsize=9.6, fontstyle="italic")

    # winner note on the self-revision control (in the clear band below its bar)
    ax.text(0.0, ys[1] - 0.55,
            "↑ lowest net — the effort-matched self-revision control (R1′) quietly wins",
            ha="left", va="center", color="#2e5d34", fontsize=9.4, fontstyle="italic")

    # --- the null brackets: R1<->R2 within each vendor arm ------------------
    def null_bracket(y_hi, y_lo, label):
        bx = 4.55                # right of the anchor line and all bar-end labels
        ax.plot([bx, bx + 0.10, bx + 0.10, bx],
                [y_hi, y_hi, y_lo, y_lo], color="#333", lw=1.0)
        ax.text(bx + 0.17, (y_hi + y_lo)/2, label, ha="left", va="center",
                color="#333", fontsize=9.5, fontstyle="italic")

    null_bracket(ys[2], ys[3], "R2 − R1 = +0.00\n(the null)")
    null_bracket(ys[4], ys[5], "R2 − R1 = −0.125\n(the null)")

    # axes cosmetics -- honest zero-based scale
    ax.set_xlim(-2.15, 6.6)
    ax.set_ylim(bot - 1.05, top + 0.80)
    ax.set_yticks([])
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_bounds(0, 4)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.tick_params(axis="x", labelsize=10.5, colors=BODY, length=3)
    ax.set_xlabel("Net material flaws remaining per output  (lower is better)",
                  fontsize=11.5, color=INK)

    # --- legend (two-segment key), one line under the axis ------------------
    ly = bot - 0.85
    ax.add_patch(Rectangle((-0.02, ly - 0.10), 0.17, 0.20, facecolor=C_ORIG, edgecolor="none"))
    ax.text(0.22, ly, "originals still remaining",
            ha="left", va="center", fontsize=9.8, color=INK)
    ax.add_patch(Rectangle((2.80, ly - 0.10), 0.17, 0.20, facecolor=C_NEW, edgecolor="none"))
    ax.text(3.04, ly, "new flaws introduced",
            ha="left", va="center", fontsize=9.8, color=INK)

    # --- titles (takeaway only; the split/caveat detail lives in the caption) ---
    fig.text(0.012, 0.960,
             "Iterating to agreement buys no cleaner answer than a single challenge",
             ha="left", fontsize=13.5, fontweight="bold", color=INK)
    fig.text(0.012, 0.918,
             "— it removes blind spots, but revising adds new flaws, and the two cancel (R2 vs R1 = the null; §6.4)",
             ha="left", fontsize=10.5, color=BODY)

    plt.subplots_adjust(left=0.185, right=0.99, top=0.86, bottom=0.13)
    fig.savefig(OUT, format="svg", metadata={"Date": None})
    plt.close(fig)

    # --- echo plotted values for diffing ------------------------------------
    print(f"[fig5] wrote {os.path.relpath(OUT)}")
    print(f"[fig5] anchor (ship-as-is) net = {ANCHOR}")
    for key, l1, l2, orig, new in ROWS:
        print(f"        {key:11s} orig={orig:<5} + new={new:<5} = net {orig+new:<5} "
              f"(JSON {means[JSON_KEY[key]]})")


if __name__ == "__main__":
    main()
