#!/usr/bin/env python3
"""Extract the structured gold set from NCBE MEE Questions-and-Analyses text.

Each MEE administration carries 6 fact patterns. Each fact pattern's ANALYSIS
opens with an enumerated `Legal Problems:` list and is then developed in weighted
`Point One (30%)` headings whose percentages sum to 100. Those two artifacts are
what make this corpus usable as a coverage gold set:

  - the Legal Problems list is the enumerated issue set   -> what to score recall against
  - the Point percentages are a human-authored weighting  -> the materiality key

Both were authored by NCBE's examiners before this system existed, which is what
makes them a frozen human judgment rather than a rating we produced (design-note §3).

NCBE text is NOT written to the output. Each gold item records the issue text
extracted from the examiners' own enumeration -- required, since it IS the gold --
but no discussion prose, and every record carries its source citation.

Usage:  ./extract_gold.py [corpus_dir] [-o gold.json]
"""
import argparse, json, os, re, sys
from collections import Counter

LEGAL_PROBLEMS = re.compile(r"^Legal Problems:\s*$")
# "Point One (30%)", "Point Three(a) (10%)", "Point Two (60% total)"
POINT = re.compile(r"^\s*Point\s+([A-Z][a-z]+)(\([a-z]\))?\s*\((\d+)%[^)]*\)\s*$")
# "(1)(a) Under the state statute, when is ..." / "(2)  What assets are divisible ..."
PROBLEM_ITEM = re.compile(r"^\s*\((\d+)\)(\([a-z]\))?\s+(.*\S)\s*$")
RUNNING_HDR = re.compile(r"^\s*([A-Z][A-Za-z '&/-]{2,38}?)\s+Analysis\s*$")
# 2019+ administrations label the subject on the question header instead of in a
# running header: "QUESTION 3-AGENCY & PARTNERSHIP" (em dash). Both conventions
# appear in the free set (6 admins use running headers, 4 use question headers),
# so the extractor reads whichever the document supplies.
QUESTION_HDR = re.compile(r"^\s*QUESTION\s+(\d+)\s*[\u2013\u2014-]\s*(.+?)\s*$")
PAGE_NUM = re.compile(r"^\s*\d+\s*$")

WORD_ORD = {w: i for i, w in enumerate(
    "One Two Three Four Five Six Seven Eight Nine Ten".split(), start=1)}


def _admin_label(stem: str) -> str:
    m = re.search(r"(Feb(?:ruary)?|July)\D*(\d{4})", stem, re.I)
    if not m:
        return stem
    return f"{'February' if m.group(1).lower().startswith('feb') else 'July'} {m.group(2)}"


def parse_admin(path: str):
    """Return a list of fact-pattern dicts for one administration's .txt."""
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    stem = os.path.basename(path)[:-4]
    admin = _admin_label(stem)

    # Anchor on each ANALYSIS block's "Legal Problems:" line; a block runs to the
    # next one (or EOF). The TOC near the top has no such line, so it self-excludes.
    # Subject by question number, where the administration labels them that way.
    # Take the FIRST occurrence of each number: the header repeats in the TOC and
    # again over the analysis, and the question section comes first.
    subj_by_num = {}
    for ln in lines:
        m = QUESTION_HDR.match(ln)
        if m:
            subj_by_num.setdefault(int(m.group(1)), m.group(2).strip().title())

    starts = [i for i, ln in enumerate(lines) if LEGAL_PROBLEMS.match(ln)]
    out = []
    for n, s in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        block = lines[s:end]

        # Subject = most common running header "<Subject> Analysis" in the block.
        hdrs = Counter()
        for ln in block:
            m = RUNNING_HDR.match(ln)
            if m and len(m.group(1)) < 40:
                hdrs[m.group(1).strip()] += 1
        subject = (subj_by_num.get(n + 1)
                   or (hdrs.most_common(1)[0][0] if hdrs else f"Question {n+1}"))

        # --- the enumerated issue list, up to DISCUSSION/Summary ---
        problems, cur = [], None
        for ln in block[1:]:
            if re.match(r"^\s*(DISCUSSION|Summary)\s*$", ln):
                break
            m = PROBLEM_ITEM.match(ln)
            if m:
                if cur:
                    problems.append(cur)
                cur = {"id": f"({m.group(1)}){m.group(2) or ''}",
                       "text": m.group(3)}
            elif cur and ln.strip() and not PAGE_NUM.match(ln):
                cur["text"] += " " + ln.strip()
        if cur:
            problems.append(cur)

        # --- weighted points ---
        points = []
        for ln in block:
            m = POINT.match(ln)
            if m:
                pid = f"({WORD_ORD.get(m.group(1), 0)}){m.group(2) or ''}"
                if any(p["id"] == pid for p in points):
                    continue  # running headers repeat the heading on later pages
                points.append({"id": pid,
                               "ordinal": m.group(1) + (m.group(2) or ""),
                               "weight_pct": int(m.group(3))})

        # The GOLD UNIT is the weighted Point, not the Legal Problems entry.
        #
        # The two enumerations agree in 57 of 60 fact patterns, but they are
        # independent and disagree in both directions: Feb-2018 Contracts lists
        # (2)(a) and (2)(b) under a single "Point Two (40%)", while Feb-2020
        # Question 2 lists a bare (2) developed as "Point Two(a)/(b)". Anchoring
        # on Points is what makes the set complete and total-100 everywhere
        # (verified: 60/60 blocks sum to exactly 100), and the weight is the
        # materiality key that cannot be reconstructed if it is dropped.
        #
        # Legal Problems text is attached where it resolves: exact id, else the
        # parent id ("(2)(a)" -> "(2)"), else the sole child sharing the number.
        prob_by_id = {pr["id"]: pr for pr in problems}
        gold = []
        for p in points:
            pid = p["id"]
            parent = re.sub(r"\([a-z]\)$", "", pid)
            pr = prob_by_id.get(pid) or prob_by_id.get(parent)
            if pr is None:
                kids = [q for k, q in prob_by_id.items() if k.startswith(parent)]
                pr = kids[0] if len(kids) == 1 else None
            gold.append({
                "gold_id": f"{admin}|{subject}|{pid}",
                "point_id": pid,
                "point": "Point " + p["ordinal"],
                "issue": re.sub(r"\s+", " ", pr["text"]).strip() if pr else None,
                "issue_id": pr["id"] if pr else None,
                "weight_pct": p["weight_pct"],
            })

        out.append({
            "administration": admin,
            "subject": subject,
            "source_pdf": stem + ".pdf",
            "source": "NCBE Multistate Essay Examination, Questions and Analyses "
                      f"({admin}). Copyright NCBE; not redistributed.",
            "n_gold": len(gold),
            "weights_sum": sum(g["weight_pct"] for g in gold),
            "gold": gold,
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("corpus_dir", nargs="?",
                    default=os.path.join(here, "..", "corpus"))
    ap.add_argument("-o", "--out",
                    default=os.path.join(here, "..", "gold", "gold.json"))
    a = ap.parse_args()

    txts = sorted(f for f in os.listdir(a.corpus_dir)
                  if f.endswith(".txt") and "Subject_Matter_Outline" not in f)
    if not txts:
        sys.exit(f"no corpus .txt in {a.corpus_dir} -- run fetch_corpus.sh first")

    patterns = []
    for t in txts:
        patterns.extend(parse_admin(os.path.join(a.corpus_dir, t)))

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump({"n_fact_patterns": len(patterns),
               "n_gold_items": sum(p["n_gold"] for p in patterns),
               "fact_patterns": patterns},
              open(a.out, "w"), indent=2)

    # --- integrity report: weights must sum to 100, every issue must carry one ---
    bad_sum = [p for p in patterns if p["weights_sum"] != 100]
    untexted = [(p, g) for p in patterns for g in p["gold"]
                if not g["issue"]]
    print(f"fact patterns : {len(patterns)}")
    print(f"gold items    : {sum(p['n_gold'] for p in patterns)}")
    print(f"mean gold/FP  : {sum(p['n_gold'] for p in patterns)/max(len(patterns),1):.2f}")
    print(f"weights != 100: {len(bad_sum)}")
    for p in bad_sum:
        print(f"   {p['administration']:<15} {p['subject']:<28} sum={p['weights_sum']:<4} n={p['n_gold']}")
    print(f"no issue text : {len(untexted)}")
    for p, g in untexted[:10]:
        print(f"   {p['administration']:<15} {p['subject']:<28} {g['point_id']}")
    nosubj = [p for p in patterns if p["subject"].startswith("Question ")]
    print(f"subject unset : {len(nosubj)}")
    for p in nosubj:
        print(f"   {p['administration']:<15} {p['source_pdf']}")
    print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
