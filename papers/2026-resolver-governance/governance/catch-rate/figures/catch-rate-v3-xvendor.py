#!/usr/bin/env python3
"""A-v3 cross-vendor: catch-rate by condition, Claude-internal vs GPT-5.2-actors/Claude-audit.
Reads ../results-aggregate.json and ../results-aggregate-xvendor.json. Reproducible SVG."""
import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "catchrate-v3-xv"
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ci = json.load(open(os.path.join(HERE, "..", "results-aggregate.json")))["catch_rate"]
xv = json.load(open(os.path.join(HERE, "..", "results-aggregate-xvendor.json")))["catch_rate"]
plt.rcParams["font.family"] = "serif"; plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "DejaVu Serif"]
plt.rcParams["svg.fonttype"] = "none"

conds = [("Produce-and-ship\n(no review — anchor)", 0.0, 0.0), ("Neutral review", ci["NEUTRAL"], xv["NEUTRAL"]),
         ("Self-review", ci["SELF"], xv["SELF"]), ("SPARRING Challenger", ci["CHAL"], xv["CHAL"])]
labels = [c[0] for c in conds]
internal = [c[1] for c in conds]; cross = [c[2] for c in conds]
y = np.arange(len(conds)); h = 0.38

fig, ax = plt.subplots(figsize=(9.8, 5.8))
b1 = ax.barh(y + h/2, internal, h, color="#3b6ea5", zorder=3, label="Claude-internal (Claude produces, reviews & audits)")
b2 = ax.barh(y - h/2, cross, h, color="#256b4e", zorder=3, label="Cross-vendor (GPT-5.2 acts, Claude audits & codes)")
for bars in (b1, b2):
    for r in bars:
        w = r.get_width()
        ax.text(w + 1.3, r.get_y() + r.get_height()/2, f"{w:.0f}%", va="center", ha="left", fontsize=9.5, fontweight="bold", color=r.get_facecolor())
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=10.5)
ax.set_xlim(0, 100); ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9, color="#666")
ax.set_xlabel("Share of the producer's own would-ship flaws caught (n=31 each, independent audit, blind-coded)", fontsize=10, color="#333")
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.invert_yaxis(); ax.tick_params(length=0)
ax.legend(loc="upper right", bbox_to_anchor=(0.995, 0.80), fontsize=8.6, frameon=True, facecolor="white", edgecolor="#cccccc")
fig.suptitle("The catch value replicates cross-vendor — a challenge recovers ~77–87% of the producer's own material flaws",
             x=0.5, y=0.965, fontsize=11.6, fontweight="bold", color="#1a1a1a")
ax.set_title("Robust across two model families: of ~4 material flaws/rec, a challenge recovers the large majority; self-review leaves a chunk in.\n"
             "Vendor-dependent: the Challenger's edge over the producer's OWN self-review is large for Claude (87 vs 68), "
             "marginal for GPT-5.2 (77 vs 74).\nThe produce-and-ship bars (0) are the definitional anchor — no review — not a measured condition.",
             fontsize=8.4, color="#444", pad=10)
fig.text(0.5, 0.02, "Single problems shared (n=8); model-established ground truth; directional pilot, no significance test. "
         "Sources: results-aggregate.json, results-aggregate-xvendor.json.", ha="center", fontsize=7.4, fontstyle="italic", color="#555")
plt.subplots_adjust(left=0.22, right=0.97, top=0.79, bottom=0.13)
fig.savefig(os.path.join(HERE, "catch-rate-v3-xvendor.svg"), format="svg", metadata={"Date": None})
print("wrote catch-rate-v3-xvendor.svg")
