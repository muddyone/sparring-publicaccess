#!/usr/bin/env python3
"""Full 2x2x2 (Generator x Challenger x Audit): catch-rate heatmap. Reads ../results-2x2-grid.json."""
import json, os
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "catchrate-2x2"
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
g = json.load(open(os.path.join(HERE, "..", "results-2x2-grid.json")))
plt.rcParams["font.family"] = "serif"; plt.rcParams["font.serif"] = ["TeX Gyre Pagella", "DejaVu Serif"]
plt.rcParams["svg.fonttype"] = "none"

cells = ["claudegen_claudeaudit", "claudegen_gptaudit", "gptgen_claudeaudit", "gptgen_gptaudit"]
collabels = ["Claude-gen\nClaude-audit", "Claude-gen\nGPT-audit", "GPT-gen\nClaude-audit", "GPT-gen\nGPT-audit"]
rows = [("Produce-and-ship (anchor)", "ship"), ("Neutral review", "NEUTRAL"), ("Self-review", "SELF"),
        ("Same-vendor Challenger", "CHAL_SAME"), ("Cross-vendor Challenger", "CHAL_CROSS")]
M = np.array([[ (0.0 if key=="ship" else g[c][key]) for c in cells] for _, key in rows])

# Native canvas kept close to the paper's text-column width so the DOCX build
# (which fits each figure to the column) barely downscales it — that is what keeps
# the on-figure text legible in Word. The dense multi-line detail that used to sit
# in the title/subtitle lives in the caption; the figure carries only the takeaway.
fig, ax = plt.subplots(figsize=(7.4, 4.9))
im = ax.imshow(M, cmap="YlGn", vmin=0, vmax=100, aspect="auto")
ax.set_xticks(range(4)); ax.set_xticklabels(collabels, fontsize=10.5)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=11.5)
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        v = M[i, j]
        ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=14,
                color="#222" if v < 65 else "#0a3d23", fontweight="bold")
ax.set_xticks(np.arange(-.5,4,1), minor=True); ax.set_yticks(np.arange(-.5,len(rows),1), minor=True)
ax.grid(which="minor", color="white", linewidth=2); ax.tick_params(which="minor", length=0); ax.tick_params(length=0)
cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02); cb.set_label("catch-rate (%)", fontsize=10); cb.ax.tick_params(labelsize=9)
fig.suptitle("A challenge recovers 78–94% of flaws in every model × role combination",
             x=0.5, y=0.975, fontsize=14, fontweight="bold", color="#1a1a1a")
ax.set_title("Self-review's miss is a real, generator-dependent blind spot",
             fontsize=10.5, color="#444", pad=8)
plt.subplots_adjust(left=0.27, right=0.965, top=0.85, bottom=0.14)
fig.savefig(os.path.join(HERE, "catch-rate-2x2.svg"), format="svg", metadata={"Date": None})
print("wrote catch-rate-2x2.svg")
