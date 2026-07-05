#!/usr/bin/env python3
"""
fig4-coverage-v3.py — Figure 4 of the governance preprint (§8): the verifier's coverage in v3.

REPLACES the superseded fig3-verifier-ceiling (v2). The v2 figure depicted a ~7%-only
machine-verifiable "ceiling" that was a DATA-LOSS artifact (per-case briefings never saved).
v3 persists every briefing, so the ceiling is closed: a part-to-whole of all 99 v3 concerns
by HOW their grounding is resolved shows the large majority are machine-checkable now. The
residual limitation is no longer *coverage* but *legitimacy* (is a flagged concern real),
which the verifier does not touch -> domain-expert audit.

DESIGN DISCIPLINE (Minard):
  * Reproducible artifact - EVERY number is read from the frozen, committed
        ../../../seeded-defect-2026-06-26/v3-run/coverage.json
    (derived by that pilot's committed derive_coverage.py from the canonical case-file
    codings). Nothing is hand-typed; an assert guards the part-to-whole sum.
  * Honest part-to-whole - shares sum to the real n=99; honest 0-100, no truncation.
  * Uncertainty must be visible - existence is model-free, correct-application is cross-vendor,
    but legitimacy stays expert-pending; directional, synthetic, n=99/12 - all on the figure.

Usage:   python3 figures/fig4-coverage-v3.py
Output:  figures/fig4-coverage-v3.svg
"""

import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "sparring-v3-fig4-coverage"  # deterministic element ids
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
COV = os.path.join(HERE, "..", "..", "..", "seeded-defect-2026-06-26", "v3-run", "coverage.json")
OUT = os.path.join(HERE, "fig4-coverage-v3.svg")
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "Palatino", "DejaVu Serif"]


def main():
    cov = json.load(open(COV))
    total = cov["n_concerns"]
    cat = cov["by_category"]
    ib = cov["in_briefing_breakdown"]
    machine = cov["machine_checkable"]
    external = cat["external-registry"]
    inbrief = cat["in-briefing"]
    noart = cat["no-artifact"]
    ib_exp = ib["in-briefing-explicit"]
    ib_map = ib["in-briefing-mapper"]

    # ordered segments, left->right: in-briefing (explicit, then mapper), external, no-artifact
    segs = [
        ("In-briefing - explicit #/section id", ib_exp, "#2e7d5b", "white",
         "cites an explicit briefing fact-id; resolved against the saved briefing - no model"),
        ("In-briefing - mapper-recovered", ib_map, "#7bb89a", "#173b2c",
         "no citation token, but the claim->fact mapper links it to a saved briefing fact"),
        ("External registry (CWE / RFC / DOI)", external, "#c98a1b", "white",
         "resolved against a public registry (MITRE / IETF / Crossref) - no model, no domain expert"),
        ("No citable artifact", noart, "#9aa0a6", "white",
         "the verifier concurs: there is nothing to check"),
    ]
    assert sum(s[1] for s in segs) == total, "segments must sum to n_concerns"
    assert (ib_exp + ib_map) == inbrief, "in-briefing breakdown must sum to category"
    assert (external + inbrief) == machine, "machine-checkable must be external + in-briefing"

    fig, ax = plt.subplots(figsize=(9.8, 4.6))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    BAR_Y, BAR_H = 0.58, 0.17
    left = 0.0
    for name, n, color, tcol, meaning in segs:
        w = n / total
        ax.add_patch(Rectangle((left, BAR_Y), w, BAR_H, facecolor=color,
                               edgecolor="white", linewidth=1.3))
        pct = f"{100*n/total:.0f}%"
        fs = 12 if w >= 0.10 else 9.0
        # tiny segments (no-artifact 7%) keep the % but shrink font
        ax.text(left + w/2, BAR_Y + BAR_H/2, pct, ha="center", va="center",
                color=tcol, fontsize=fs, fontweight="bold")
        left += w

    # group brackets: machine-checkable (everything but no-artifact) vs not
    def bracket(x0, x1, y, label, color):
        ax.plot([x0, x0, x1, x1], [y-0.024, y, y, y-0.024], color=color, lw=1.1)
        ax.text((x0+x1)/2, y+0.014, label, ha="center", va="bottom", fontsize=9.5,
                color=color, fontstyle="italic")

    w_machine = machine / total
    bracket(0.0, w_machine, 0.86, f"machine-checkable today - {machine} of {total}", "#256b4e")
    bracket(w_machine, 1.0, 0.86, "nothing to check", "#6a6e73")

    # key below the bar
    ky = 0.40
    for name, n, color, tcol, meaning in segs:
        ax.add_patch(Rectangle((0.0, ky-0.018), 0.022, 0.036, facecolor=color, edgecolor="none"))
        ax.text(0.032, ky, name, ha="left", va="center", fontsize=10.5, fontweight="bold", color="#1a1a1a")
        ax.text(0.032, ky-0.050, f"{100*n/total:.0f}% · n={n}", ha="left", va="center", fontsize=9, color=color)
        ax.text(0.34, ky-0.013, meaning, ha="left", va="center", fontsize=9.2, color="#555")
        ky -= 0.107

    fig.suptitle(f"A computer can independently check the grounding of {machine} of {total} objections in v3",
                 x=0.035, y=0.965, ha="left", fontsize=13.3, fontweight="bold", color="#1a1a1a")
    fig.text(0.035, 0.895,
             f"All {total} v3 seeded-defect concerns, by how their grounding is resolved. v3 persists every "
             "briefing, so the in-briefing majority is now",
             ha="left", fontsize=9.5, color="#444")
    fig.text(0.035, 0.862,
             "machine-checkable - closing the v2 corpus's ~7%-only ceiling, which was a data-loss artifact, "
             "not a tooling gap. §8 / §10.2.",
             ha="left", fontsize=9.5, color="#444")

    fig.text(0.035, 0.045,
             "Existence is model-free; correct-application is cross-vendor (Claude+OpenAI). The residual limit is "
             "now LEGITIMACY (is a concern real) - not coverage - which",
             ha="left", fontsize=8.4, fontstyle="italic", color="#8a2f2f")
    fig.text(0.035, 0.018,
             "routes to the domain-expert audit, not the verifier. Directional, synthetic; n=99 concerns / 12 cases. "
             "Source: v3-run/coverage.json (derived from case-file codings).",
             ha="left", fontsize=8.4, fontstyle="italic", color="#8a2f2f")

    plt.subplots_adjust(left=0.03, right=0.98, top=0.83, bottom=0.10)
    fig.savefig(OUT, format="svg", metadata={"Date": None})
    plt.close(fig)
    print(f"[fig4] wrote {os.path.relpath(OUT)}")
    print(f"[fig4] frozen: total={total}, machine-checkable={machine} ({100*machine/total:.1f}%)")
    for name, n, *_ in segs:
        print(f"        {name:38s} n={n} ({100*n/total:.1f}%)")


if __name__ == "__main__":
    main()
