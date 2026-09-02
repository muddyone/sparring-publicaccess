#!/usr/bin/env python3
"""A-v3 (Test B): catch-rate of a producer's OWN would-ship flaws, by condition.
Reads ../results-aggregate.json. Reproducible SVG (fixed hashsalt, no date)."""
import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "catchrate-v3"
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(HERE, "..", "results-aggregate.json")))
cr = res["catch_rate"]; n = res["n_flaws"]
plt.rcParams["font.family"] = "serif"; plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "DejaVu Serif"]
plt.rcParams["svg.fonttype"] = "none"

# order low -> high
conds = [("Produce-and-ship\n(no review — definitional anchor)", 0.0, "#b0a9a0"),
         ("Neutral review\n(fresh eyes)", cr["NEUTRAL"], "#b9912f"),
         ("Self-review\n(producer critiques its OWN work)", cr["SELF"], "#7a7f33"),
         ("SPARRING Challenger\n(fresh + adversarial)", cr["CHAL"], "#256b4e")]
labels = [c[0] for c in conds]; vals = [c[1] for c in conds]; cols = [c[2] for c in conds]

fig, ax = plt.subplots(figsize=(9.6, 5.8))
y = list(range(len(conds)))
ax.barh(y, vals, color=cols, height=0.6, zorder=3)
for i, v in enumerate(vals):
    ax.text(v + 1.5, i, f"{v:.0f}%", va="center", ha="left", fontsize=11, fontweight="bold", color=cols[i])
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9.5)
ax.set_xlim(0, 100); ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9, color="#666")
ax.set_xlabel(f"Share of the producer's own would-ship flaws caught (n={n}, independent audit, blind-coded)", fontsize=10, color="#333")
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.invert_yaxis(); ax.tick_params(length=0)
sv = res["self_vs_chal"]
ax.text(99, 0.55, f"Challenger vs the producer's own self-review:\nthe Challenger caught {sv['chal_only']} flaws self-review missed;\nself-review caught only {sv['self_only']} the Challenger missed",
        ha="right", va="center", fontsize=8.4, fontstyle="italic", color="#256b4e",
        bbox=dict(boxstyle="round,pad=0.4", fc="#eaf3ec", ec="#256b4e", lw=0.6))
fig.suptitle("A challenger recovers 87% of the producer's own material flaws — self-review leaves ~32% unaddressed",
             x=0.5, y=0.965, fontsize=12, fontweight="bold", color="#1a1a1a")
ax.set_title("A-v3 (Test B): an agent produces a recommendation (~4 material flaws/rec, independent audit); we measure how many of its\n"
             "OWN flaws each review recovers. Self-review 68%, a fresh adversarial Challenger 87% — measured against the honest comparator\n"
             "(self-review). The produce-and-ship bar (0) is the definitional anchor: no review, all flaws reach the decision. (Analogue of §6.)",
             fontsize=8.3, color="#444", pad=10)
fig.text(0.5, 0.02, "Single-vendor, n=31 flaws / 8 problems, model-established ground truth; directional pilot, no significance test. "
         "Source: results-aggregate.json.", ha="center", fontsize=7.6, fontstyle="italic", color="#555")
plt.subplots_adjust(left=0.30, right=0.97, top=0.80, bottom=0.13)
fig.savefig(os.path.join(HERE, "catch-rate-v3.svg"), format="svg", metadata={"Date": None})
print("wrote catch-rate-v3.svg")
