#!/usr/bin/env python3
"""Parse the NCBE MEE Subject Matter Outline into a flat node list.

This is the candidate set for the structured non-model enumerator (rung G4 of the
independence ladder, design-note.md §4). It matters that it comes from here rather than
from a model: the outline was written by NCBE's examiners as an exhaustive statement of
what the exam covers, years before this study existed. It is frozen human judgment about
the *shape of the domain*, in the same way the answer keys are frozen human judgment about
individual problems.

Structure in the source:

    Family Law                          <- subject
    I.   Getting married                <- topic (roman)
         A. Marriage requirements       <- subtopic (letter)

Every (subject, topic, subtopic) triple becomes one node. Nodes are what the enumerator
walks; it never invents a candidate, it only decides which of these the facts raise.

NCBE text is not redistributed: taxonomy.json is written into the gitignored corpus dir.

Usage:  ./extract_taxonomy.py [corpus_dir]
"""
import argparse, json, os, re, sys

ROMAN = re.compile(r"^\s*([IVXL]+)\.\s+(.*\S)\s*$")
LETTER = re.compile(r"^\s*([A-Z])\.\s+(.*\S)\s*$")
# Subject headings are INDENTED on the first page and at column 0 on every page after,
# so the leading-space requirement has to be optional. Requiring it silently collapsed
# 319 of 343 nodes into one subject.
SUBJECT = re.compile("^\\s*([A-Z][A-Za-z][A-Za-z ,'\u2019&/-]{3,60})\\s*$")
SKIP = re.compile(r"(continued\)|Copyright|National Conference|MEE Subject|"
                  r"scope of coverage|^\s*NOTE:|^\s*\d+\s*$)", re.I)
# Section banners group subjects: "Business Associations" heads Agency and Partnership +
# Corporations; "Trusts and Estates" heads Decedents' Estates + Trusts and Future Interests.
# They are typographically identical to subject headings, and a hardcoded list got it
# wrong -- Civil Procedure, Criminal Law and Procedure, Real Property and Torts were
# listed as banners and silently dropped, losing 5 of 14 subjects.
#
# The reliable signal is structural: a BANNER is followed by another heading, a SUBJECT is
# followed by roman-numeral topics.


def parse(path):
    raw = open(path, encoding="utf-8", errors="replace").read().splitlines()
    lines = [ln for ln in raw if ln.strip() and not SKIP.search(ln)]

    # Resolve banners structurally: look ahead to the next content line. A heading whose
    # successor is another heading is a banner; one whose successor is a roman topic is a
    # subject.
    banners = set()
    for i, ln in enumerate(lines):
        m = SUBJECT.match(ln)
        if not m or ROMAN.match(ln) or LETTER.match(ln):
            continue
        for nxt in lines[i + 1:]:
            if ROMAN.match(nxt):
                break
            if SUBJECT.match(nxt) and not LETTER.match(nxt):
                banners.add(re.sub(r"\s+", " ", m.group(1)).strip())
            break

    nodes, subject, topic = [], None, None
    for ln in lines:
        m = ROMAN.match(ln)
        if m:
            topic = re.sub(r"\s+", " ", m.group(2)).strip()
            if subject:
                nodes.append({"subject": subject, "topic": topic, "subtopic": None})
            continue
        m = LETTER.match(ln)
        if m and topic:
            sub = re.sub(r"\s+", " ", m.group(2)).strip()
            nodes.append({"subject": subject, "topic": topic, "subtopic": sub})
            continue
        m = SUBJECT.match(ln)
        if m:
            cand = re.sub(r"\s+", " ", m.group(1)).strip()
            # A subject heading resets the topic; a banner does not introduce nodes.
            if cand not in banners and not cand.endswith("."):
                subject, topic = cand, None
            continue
    # A bare topic with lettered children is redundant with them; keep only leaves plus
    # childless topics, so the walk is not double-counting the same ground.
    has_child = {(n["subject"], n["topic"]) for n in nodes if n["subtopic"]}
    out = [n for n in nodes
           if n["subtopic"] or (n["subject"], n["topic"]) not in has_child]
    for i, n in enumerate(out):
        n["node_id"] = f"n{i:03d}"
        n["path"] = " > ".join(x for x in (n["subject"], n["topic"], n["subtopic"]) if x)
    return out


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("corpus_dir", nargs="?", default=os.path.join(here, "..", "corpus"))
    a = ap.parse_args()

    src = os.path.join(a.corpus_dir, "outline.txt")
    if not os.path.exists(src):
        pdf = os.path.join(a.corpus_dir, "NCBE_MEE_Subject_Matter_Outline.pdf")
        if not os.path.exists(pdf):
            sys.exit("no outline -- run scripts/fetch_corpus.sh first")
        os.system(f'pdftotext -layout "{pdf}" "{src}"')

    nodes = parse(src)
    out = os.path.join(a.corpus_dir, "taxonomy.json")
    json.dump({"n_nodes": len(nodes), "source":
               "NCBE MEE Subject Matter Outline (2023). Copyright NCBE; not redistributed.",
               "nodes": nodes}, open(out, "w"), indent=2)

    subs = {}
    for n in nodes:
        subs[n["subject"]] = subs.get(n["subject"], 0) + 1
    print(f"nodes    : {len(nodes)}")
    print(f"subjects : {len(subs)}  (MEE covers 14; a shortfall means the parse dropped some)")
    for s, c in sorted(subs.items(), key=lambda x: -x[1]):
        print(f"   {c:>3}  {s}")
    print(f"\nwrote {out}  (gitignored -- NCBE text)")


if __name__ == "__main__":
    main()
