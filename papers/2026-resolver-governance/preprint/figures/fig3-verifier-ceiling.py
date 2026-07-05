#!/usr/bin/env python3
"""
fig3-verifier-ceiling.py — Figure 3 of the V2 governance preprint.

THE VERIFIER'S CEILING. A part-to-whole bar of all 236 seeded-defect concerns, split by
HOW their grounding can be checked. It is an integrity-positive figure: it depicts a
LIMITATION honestly, so a reader cannot over-read §8's verifier as "the verifier checks
the grounding" — today it mechanizes only the externally-checkable, explicitly-cited slice
(~7%); most concerns still rest on expert (LLM, Path-B) coding, and the ceiling is a
DATA-LOSS artifact (the per-case briefings weren't persisted), not a tooling gap. Supports §8 / §10.2.

DESIGN DISCIPLINE (Minard, the data-graphics reviewer):
  * Reproducible artifact — the two load-bearing buckets are read from FROZEN data, not
    typed in:  total concerns + the ungrounded count from
        ../../../seeded-defect-2026-06-26/v2-run/codings.json
    and the machine-verified (external-canon) count from
        ../../../seeded-defect-2026-06-26/patha-run/concerns-full.json
  * The middle split (in-briefing: blocked-on-briefings vs. prose-grounded) CANNOT be machine-
    derived for this corpus — the per-case briefings weren't persisted — so it is taken from
    the §10.2 hand-map and LABELLED approximate (≈). Exact vs. approximate is marked on
    the figure; we do not manufacture precision the data can't support.
  * Honest part-to-whole — shares sum to the real n=236; no truncation, no rounding that
    would make the machine-verified slice look bigger than 7%.

Usage:   python3 figures/fig3-verifier-ceiling.py
Output:  figures/fig3-verifier-ceiling.svg
"""

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
SD = os.path.join(HERE, "..", "..", "..", "seeded-defect-2026-06-26")
OUT = os.path.join(HERE, "fig3-verifier-ceiling.svg")

plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "Palatino", "DejaVu Serif"]


def main():
    # --- frozen anchors --------------------------------------------------------------
    codings = json.load(open(os.path.join(SD, "v2-run", "codings.json")))
    total = sum(len(rv["concerns"]) for case in codings for rv in case["reviews"])
    ungrounded = sum(1 for case in codings for rv in case["reviews"]
                     for c in rv["concerns"] if c.get("grounding") == "UNGROUNDED")
    external = len(json.load(open(os.path.join(SD, "patha-run", "concerns-full.json"))))

    # --- §10.2 hand-map for the in-briefing middle (briefings not persisted -> not machine-derivable) ---
    inbrief_blocked = round(total * 0.19)                     # ~19%, §10.2
    prose_grounded = total - external - ungrounded - inbrief_blocked   # remainder, ~57%

    segs = [
        # name, n, color, textcolor, exactness, meaning
        ("Machine-verified today", external, "#2e7d5b", "white", "exact",
         "external-canon artifact (CWE / RFC / DOI) resolved against a public registry — no model, no domain expert"),
        ("Blocked on un-persisted briefings", inbrief_blocked, "#c98a1b", "white", "≈ §10.2",
         "cites an in-briefing fact-id; the resolver exists, but the per-case briefings were never saved (a data loss)"),
        ("Needs briefings + a claim→fact mapper", prose_grounded, "#d9c7a3", "#4a3b1a", "≈ §10.2",
         "grounded by reading the briefing with no citation token — needs the briefings + a claim→fact mapper"),
        ("Ungrounded — no artifact", ungrounded, "#9aa0a6", "white", "exact",
         "the verifier concurs: there is nothing to check"),
    ]
    assert sum(s[1] for s in segs) == total, "segments must sum to total"

    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    BAR_Y, BAR_H = 0.60, 0.16
    left = 0.0
    centers = []
    for name, n, color, tcol, exact, meaning in segs:
        w = n / total
        ax.add_patch(Rectangle((left, BAR_Y), w, BAR_H, facecolor=color,
                               edgecolor="white", linewidth=1.2))
        cx = left + w / 2
        centers.append((cx, w, color))
        # percent inside the segment; shrink the font for narrow segments rather than
        # floating it above (a leader into the group-bracket label collides)
        pct = f"{100*n/total:.0f}%"
        fs = 12 if w >= 0.11 else 9.5
        ax.text(cx, BAR_Y + BAR_H/2, pct, ha="center", va="center",
                color=tcol, fontsize=fs, fontweight="bold")
        left += w

    # --- group brackets above the bar ------------------------------------------------
    def bracket(x0, x1, y, label, color):
        ax.plot([x0, x0, x1, x1], [y-0.022, y, y, y-0.022], color=color, lw=1.1)
        ax.text((x0+x1)/2, y+0.012, label, ha="center", va="bottom", fontsize=9.5,
                color=color, fontstyle="italic")

    w0 = segs[0][1]/total
    w_mid = (segs[1][1]+segs[2][1])/total
    bracket(0, w0, 0.86, "machine-verified today", "#256b4e")
    bracket(w0, w0+w_mid, 0.86, "still expert-coded (Path-B) — blocked by un-persisted briefings", "#9a6a12")
    bracket(w0+w_mid, 1.0, 0.86, "ungrounded", "#6a6e73")

    # --- key below the bar -----------------------------------------------------------
    ky = 0.40
    for name, n, color, tcol, exact, meaning in segs:
        ax.add_patch(Rectangle((0.0, ky-0.018), 0.022, 0.036, facecolor=color, edgecolor="none"))
        ax.text(0.032, ky, f"{name}", ha="left", va="center", fontsize=10.5, fontweight="bold",
                color="#1a1a1a")
        ax.text(0.032, ky-0.052, f"{100*n/total:.0f}% · n={n} · {exact}", ha="left", va="center",
                fontsize=9, color=color)
        ax.text(0.34, ky-0.013, meaning, ha="left", va="center", fontsize=9.3, color="#555")
        ky -= 0.105

    # --- title / subtitle / caveat ---------------------------------------------------
    fig.suptitle("A computer can double-check only 7% of the objections on its own today",
                 x=0.035, y=0.965, ha="left", fontsize=13.5, fontweight="bold", color="#1a1a1a")
    fig.text(0.035, 0.895,
             f"All {total} seeded-defect concerns, by how their grounding can be checked. The ceiling is a "
             "data-loss artifact — the per-case briefings",
             ha="left", fontsize=9.6, color="#444")
    fig.text(0.035, 0.862, "weren't persisted — not a tooling gap (the in-briefing resolver exists). §8 / §10.2.",
             ha="left", fontsize=9.6, color="#444")

    fig.text(0.035, 0.045,
             f"Exact (frozen): machine-verified {external} and ungrounded {ungrounded} are counted directly; "
             "the in-briefing split (≈19% / ≈57%) is the §10.2 hand-map.",
             ha="left", fontsize=8.5, fontstyle="italic", color="#8a2f2f")
    fig.text(0.035, 0.018,
             "Directional, LLM-coded. Source: pilots/seeded-defect-2026-06-26/v2-run/codings.json + patha-run/concerns-full.json.",
             ha="left", fontsize=8.5, fontstyle="italic", color="#8a2f2f")

    plt.subplots_adjust(left=0.03, right=0.98, top=0.83, bottom=0.10)
    fig.savefig(OUT, format="svg")
    plt.close(fig)
    print(f"[fig3] wrote {os.path.relpath(OUT)}")
    print(f"[fig3] frozen anchors: total={total}, machine-verified(external)={external} "
          f"({100*external/total:.1f}%), ungrounded={ungrounded} ({100*ungrounded/total:.1f}%)")
    print(f"[fig3] §10.2 hand-map middle: blocked≈{inbrief_blocked} ({100*inbrief_blocked/total:.0f}%), "
          f"prose-grounded≈{prose_grounded} ({100*prose_grounded/total:.0f}%)")


if __name__ == "__main__":
    main()
