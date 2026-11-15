#!/usr/bin/env python3
"""Extract the fact-pattern text for each MEE question.

Separate from extract_gold.py on purpose: the gold set is the examiners' answer
key, the questions are what the generators see. They must never travel together
into a prompt, and keeping them in different files makes that hard to get wrong.

The free administrations use two header conventions, so both are read:
  2016-2018 :  "FAMILY LAW QUESTION"      (uppercase subject, then QUESTION)
  2019-2020 :  "QUESTION 3-AGENCY & PARTNERSHIP"

Question bodies run from their header to the next header, stopping at the start
of the analyses section -- everything past that point is answer key.

Output is NOT committed (NCBE text, copyrighted); it is written to the gitignored
corpus dir alongside the source PDFs.

Usage:  ./extract_questions.py [corpus_dir] [-o questions.json]
"""
import argparse, json, os, re, sys

UPPER_HDR = re.compile(r"^\s*([A-Z][A-Z &,/'-]{2,60}?)\s+QUESTION\s*$")
NUM_HDR = re.compile(r"^\s*QUESTION\s+(\d+)\s*[–—-]\s*(.+?)\s*$")
ANALYSES_START = re.compile(r"^\s*(MEE\s+Analyses|ANALYSIS)\s*$", re.I)
# 2019+ administrations INTERLEAVE: Question 1, Analysis 1, Question 2, ... so
# there is no single section boundary and each question ends at its own analysis.
ANALYSIS_MARK = re.compile(r"^\s*MEE\s+Analysis\s+\d+\s*$", re.I)
PAGE_NUM = re.compile(r"^\s*\d+\s*$")


def _admin(stem):
    m = re.search(r"(Feb(?:ruary)?|July)\D*(\d{4})", stem, re.I)
    return f"{'February' if m.group(1).lower().startswith('feb') else 'July'} {m.group(2)}" if m else stem


def parse(path):
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    stem = os.path.basename(path)[:-4]
    admin = _admin(stem)

    # Two layouts. Interleaved (2019+): each question ends at its own
    # "MEE Analysis n". Sectioned (2016-2018): one analyses section, and
    # everything from it onward is answer key.
    marks = [i for i, l in enumerate(lines) if ANALYSIS_MARK.match(l)]
    interleaved = len(marks) >= 2
    cut = (marks[-1] if interleaved
           else next((i for i, l in enumerate(lines) if ANALYSES_START.match(l)),
                     len(lines)))

    # Collect header positions before the cut. The first "QUESTION n-SUBJECT"
    # occurrences are the TOC; take the LAST run of them before the cut, which is
    # the question section proper. For the uppercase convention the TOC uses
    # title case, so those matches are already unambiguous.
    hits = []
    for i, l in enumerate(lines[:cut]):
        m = UPPER_HDR.match(l)
        if m:
            hits.append((i, m.group(1).strip().title()))
            continue
        m = NUM_HDR.match(l)
        if m:
            hits.append((i, m.group(2).strip().title()))
    # Drop TOC duplicates. Sectioned layout: the TOC precedes the question
    # section, so the LAST occurrence of a label is the real one. Interleaved
    # layout: the label recurs over the analysis too, so anchor each question on
    # its FIRST occurrence after the TOC and end it at its own analysis marker.
    if interleaved:
        seen, kept = set(), []
        for i, subj in hits:
            if subj not in seen:
                seen.add(subj)
                kept.append((i, subj))
        hits = kept
    else:
        last = {}
        for i, subj in hits:
            last[subj] = i
        hits = sorted((i, s) for s, i in last.items())

    out = []
    for n, (start, subj) in enumerate(hits):
        if interleaved:
            nxt = [m for m in marks if m > start]
            end = nxt[0] if nxt else (hits[n + 1][0] if n + 1 < len(hits) else cut)
        else:
            end = hits[n + 1][0] if n + 1 < len(hits) else cut
        body = [l for l in lines[start + 1:end] if not PAGE_NUM.match(l)]
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(body)).strip()
        if len(text) < 500:      # a TOC fragment or a stray match, not a question
            continue
        out.append({"administration": admin, "subject": subj,
                    "source_pdf": stem + ".pdf",
                    "chars": len(text), "text": text})
    return out


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("corpus_dir", nargs="?", default=os.path.join(here, "..", "corpus"))
    ap.add_argument("-o", "--out", default=None)
    a = ap.parse_args()
    out = a.out or os.path.join(a.corpus_dir, "questions.json")

    txts = sorted(f for f in os.listdir(a.corpus_dir)
                  if f.endswith(".txt") and "Subject_Matter_Outline" not in f
                  and f != "questions.json")
    if not txts:
        sys.exit(f"no corpus .txt in {a.corpus_dir} -- run fetch_corpus.sh first")

    qs = []
    for t in txts:
        got = parse(os.path.join(a.corpus_dir, t))
        qs.extend(got)
        print(f"  {t[:44]:<44} questions={len(got)}")

    json.dump({"n_questions": len(qs), "questions": qs}, open(out, "w"), indent=2)
    short = [q for q in qs if q["chars"] < 1500]
    print(f"\ntotal questions : {len(qs)}  (expected 60)")
    print(f"mean chars      : {sum(q['chars'] for q in qs)//max(len(qs),1)}")
    print(f"suspiciously short (<1500 chars): {len(short)}")
    for q in short:
        print(f"   {q['administration']:<15} {q['subject']:<30} {q['chars']}")
    print(f"\nwrote {out}  (gitignored -- NCBE text)")


if __name__ == "__main__":
    main()
