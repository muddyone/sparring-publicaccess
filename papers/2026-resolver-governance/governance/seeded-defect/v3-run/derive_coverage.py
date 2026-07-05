#!/usr/bin/env python3
"""Derive frozen verifier-coverage breakdown for the v3 seeded-defect corpus.

For each legitimacy-coded concern (the canonical 99 across the 12 case files),
classify HOW its grounding could be machine-checked, by artifact type:

  - external-registry : cites a CWE / RFC / DOI / literature citation
                        (resolvable against MITRE / IETF / Crossref, no model)
  - in-briefing       : cites a briefing fact-id (#N / §X) OR carries no explicit
                        token but was grounded by the claim->fact mapper against
                        the persisted briefing
  - no-artifact       : no citable artifact at all (counted ungrounded)

Reads the canonical case-file codings (NOT the stale verdicts*.json early
extraction). Emits coverage.json. Reproducible: no network, no model.

Expected (cross-checked against the §8 prose and the gate review): 86 in-briefing
(70 explicit + 16 mapper-recovered) / 6 external / 7 no-artifact = 99.
"""
import json, glob, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

def classify_external(art):
    a = art.strip()
    if re.match(r'(?i)^(cwe|rfc)\b', a):
        return True
    if re.search(r'\b10\.\d{4,}/', a):            # DOI
        return True
    if re.search(r'\(\d{4}\)', a):                # Author (YEAR) literature citation
        return True
    return False

def main():
    cats = {"external-registry": 0, "in-briefing": 0, "no-artifact": 0}
    sub = {"in-briefing-explicit": 0, "in-briefing-mapper": 0}
    per_concern = []
    for f in sorted(glob.glob(os.path.join(HERE, "case-DC*.json"))):
        d = json.load(open(f))
        art_of = {c["id"]: (c.get("cited_artifact") or "").strip() for c in d.get("concerns", [])}
        for cd in d.get("codings", []):
            cid = cd["concern_id"]
            art = art_of.get(cid, "")
            grounded = cd["grounding"] != "UNGROUNDED"
            if art.startswith("#") or art.startswith("§"):
                cat, detail = "in-briefing", "in-briefing-explicit"
            elif art and classify_external(art):
                cat, detail = "external-registry", "external-registry"
            elif art == "" and grounded:
                cat, detail = "in-briefing", "in-briefing-mapper"   # mapper recovered to a briefing fact
            else:
                cat, detail = "no-artifact", "no-artifact"
            cats[cat] += 1
            if detail in sub:
                sub[detail] += 1
            per_concern.append({"dc": d["dc"], "concern_id": cid, "cited_artifact": art,
                                "grounding": cd["grounding"], "category": cat, "detail": detail})
    total = sum(cats.values())
    out = {
        "corpus": "seeded-defect v3 (12 cases, legitimacy-coded concerns)",
        "n_concerns": total,
        "machine_checkable": cats["external-registry"] + cats["in-briefing"],
        "by_category": cats,
        "in_briefing_breakdown": sub,
        "note": "Existence-resolution route per concern. in-briefing = explicit #/section-id OR mapper-recovered against the persisted briefing; external = CWE/RFC/DOI/citation against public registries; no-artifact = ungrounded. Derived from canonical case-file codings, not verdicts*.json.",
        "per_concern": per_concern,
    }
    with open(os.path.join(HERE, "coverage.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"n={total}  external={cats['external-registry']}  in-briefing={cats['in-briefing']} "
          f"(explicit={sub['in-briefing-explicit']} + mapper={sub['in-briefing-mapper']})  "
          f"no-artifact={cats['no-artifact']}  machine-checkable={out['machine_checkable']}")

if __name__ == "__main__":
    main()
