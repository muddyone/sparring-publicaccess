#!/usr/bin/env python3
"""Score Stage 0b and compute the main run's n by the locked rule (design note §5.3, §15).

Reads runs/baseline/seqs/<model>/M0-CC-*.json. For each model: the proportion of sequences whose
TEST machine (the fourth) is correct, meaning both the nexiom pair and the rule type are right.
Parse failures are left out of the denominator and counted. A model whose parse-failure rate is
above 5% is flagged unreadable (§7). Then:

  p0 = mean of the four models' proportions; stop if p0 >= 0.80 (§5.3 stop rule)
  p0 bounded to [0.10, 0.70]; p1 = p0 + 0.20
  n = ceil((1.96 + 0.84)^2 * (p0(1-p0) + p1(1-p1)) / 0.20^2), bounded to [30, 100]

Writes runs/baseline/baseline.json and prints the same.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent / "runs" / "baseline"


def main() -> int:
    per = {}
    for d in sorted((RUN / "seqs").iterdir()):
        ok = scored = parse_fail = 0
        for f in sorted(d.glob("M0-CC-*.json")):
            m = json.loads(f.read_text())["machines"][3]
            if m["outcome"] == "parse_failure":
                parse_fail += 1
                continue
            scored += 1
            a, t = m["answer"], m["truth"]
            ok += bool(a) and sorted(a["nexioms"]) == sorted(t["nexioms"]) and a["rule"] == t["rule"]
        total = scored + parse_fail
        per[d.name] = {"sequences": total, "scored": scored, "correct": ok, "parse_failures": parse_fail,
                       "p": round(ok / scored, 4) if scored else None,
                       "unreadable": total > 0 and parse_fail / total > 0.05}
    ps = [v["p"] for v in per.values() if v["p"] is not None]
    p0_raw = sum(ps) / len(ps)
    out = {"models": per, "p0_unbounded": round(p0_raw, 4), "stop": p0_raw >= 0.80}
    if not out["stop"]:
        p0 = min(max(p0_raw, 0.10), 0.70)
        p1 = p0 + 0.20
        n = math.ceil((1.96 + 0.84) ** 2 * (p0 * (1 - p0) + p1 * (1 - p1)) / 0.20 ** 2)
        out.update(p0_bounded=round(p0, 4), n_formula=n, n=min(max(n, 30), 100))
    (RUN / "baseline.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
