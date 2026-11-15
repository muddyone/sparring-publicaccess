#!/usr/bin/env python3
"""Screen cached opinions, then split the keepers into situation / seed / key.

TWO STAGES, deliberately separated.

  SCREEN   Did the appellate court itself HOLD that the tribunal below failed to
           consider something, and did that failure drive relief? The bare phrase is
           usually an appellant's argument the court is about to reject (verified on
           Moore v. Moore, Ohio App. 2026-08-27), so this cannot be a keyword test.
           A case is kept only with a quoted holding sentence in the court's own voice.

  EXTRACT  Split the keeper into the three parts of design-note.md §2:
             situation -- facts + posture as they stood BELOW. The generator's only input.
             seed      -- the consideration the court says was not weighed.
             key       -- the grounds the tribunal below DID address.

WHY THE STAGES ARE SEPARATE. Screening is a yes/no over the whole opinion; extraction is
a rewrite that must not see its own screening rationale as a target. Separating them also
means a screen failure is visible as a screen failure rather than as a strange extraction.

THE LEAKAGE PROBLEM (design-note.md §4.1). The statement of facts is written by someone
who knows the answer. The extractor is therefore instructed to EXCLUDE any sentence that
names the missed doctrine, states the holding, or characterises the reasoning below as
deficient -- and to RECORD what it excluded, so the cut is auditable rather than trusted.
That is mitigation, not a fix; the leakage audit in score_seed.py measures the residue.

The extractor is claude-opus-4-8, a DIFFERENT VENDOR from g1 (gpt-5.2), and its output
is committed. It is not blind -- it reads the holding -- which is why every extraction is
inspectable and why the decoy control exists.

Resumable: re-running skips cases already screened/extracted. Cheap to add cases later.

Usage:
  ./screen_cases.py                 # screen + extract everything cached
  ./screen_cases.py --screen-only
  ./screen_cases.py --limit 40
"""
import argparse, json, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))
RAW = os.path.join(CORPUS, "raw")
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))


def load_env(path=os.environ.get("SPARRING_ENV_FILE")):
    # DEPOSIT COPY: the working-repository original read a hard-coded, machine-specific
    # .env path here. Keys now come from the environment (ANTHROPIC_API_KEY,
    # OPENAI_API_KEY); set SPARRING_ENV_FILE to a KEY=VALUE file to load them from one.
    if not path:
        return
    for line in open(path):
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v.strip().strip('"'))


load_env()
from lib_llm import claude_json  # noqa: E402

EXTRACTOR = "claude-opus-4-8"   # different vendor from g1 (gpt-5.2)

# Opinions run to 90k chars. The holding is what screening needs and it is near the end;
# the facts are near the start. Send both ends rather than a truncated head.
HEAD, TAIL = 26000, 22000

SCREEN_SYS = """You are screening appellate opinions for a research corpus.

KEEP an opinion only if BOTH hold:
  (a) the appellate court, IN ITS OWN VOICE, concludes that the tribunal below failed to
      consider / failed to address / did not weigh some specific consideration; AND
  (b) that failure is a ground for the relief granted (reversal, vacatur, or remand).

REJECT if:
  - the phrase appears only in a party's ARGUMENT that the court then rejects
    (very common -- the court answers by showing where the tribunal DID consider it);
  - the failure is attributed to a party, counsel, an agency witness, or a jury rather
    than to the tribunal whose decision is under review;
  - the "failure" is a purely procedural or ministerial defect (missing findings form,
    untimely filing) with no substantive consideration behind it;
  - the court assumes error without deciding it, or finds it harmless;
  - you cannot locate a holding sentence in the court's own voice.

Also reject if the missed consideration cannot be stated without reciting the outcome --
the corpus needs a consideration a decision-maker could have weighed, not a conclusion.

Return JSON:
{"keep": true|false,
 "holding_quote": "<the sentence in the court's own voice, verbatim, or empty>",
 "missed_short": "<the missed consideration in <=15 words, or empty>",
 "tribunal_below": "<trial court / agency / BIA / juvenile court / etc, or empty>",
 "reason": "<=25 words on why kept or rejected>"}"""

# SUPERSEDED by the three-call extraction below (deviations.md D3). Kept as a record of
# what was tried: asking ONE sighted call to both identify the seed and write a document
# concealing it produced situations that stated the seed almost verbatim.
_EXTRACT_SYS_V1_SUPERSEDED = """You are building a research stimulus from an appellate
opinion. You will produce three parts. Accuracy matters more than polish; do not invent.

1. SITUATION -- what was before the tribunal below, written so a competent lawyer could
   work the matter from it alone.
     * Include: the facts, the parties' positions, the procedural posture, the relief
       sought, the governing statute/standard IF the opinion says it was invoked below.
     * Write it in neutral, present-tense case-file voice. Do NOT write it as an appellate
       narrative and do NOT reference THIS appeal, this court, or any error.
     * WRITE IT AT THE POSTURE THE TRIBUNAL BELOW OCCUPIED. This is critical and easy to
       get wrong. The tribunal below is not always a trial court.
         - trial court / agency / board deciding in the first instance -> a case file:
           the matter as it comes to that decision-maker.
         - a tribunal REVIEWING an earlier decision (an intermediate appellate court, a
           board reviewing a hearing officer, a district court on agency review) -> the
           file must include the posture that tribunal actually sat in: what was decided
           below IT, on what record, and what was argued to it. Without that posture the
           consideration it missed cannot exist in the file at all, and the stimulus is
           void.
       The test: could a competent reviewer, holding only this file and occupying the
       tribunal below's seat, raise the consideration in part 2 on their own? If the
       posture needed to raise it is missing, the file is wrong.
     * CRITICAL EXCLUSIONS -- omit entirely:
         - any sentence naming or gesturing at the consideration that was missed;
         - the appellate holding, reasoning, disposition, or standard of review;
         - any characterisation of the tribunal below as having erred, overlooked,
           failed, or neglected anything;
         - anything that would tell a reader what the right answer is.
     * A reader of the SITUATION alone must not be able to tell what was missed.

2. SEED -- the consideration the appellate court says the tribunal below failed to weigh.
   State it as a consideration a decision-maker could have raised, not as a verdict.
   One sentence, plus one sentence of why it mattered.

3. KEY -- the grounds the tribunal below DID address (what it actually considered and
   decided). These are the "already graded" region. 3-10 entries, each a short label plus
   the question it puts in play. Include only grounds the opinion states were addressed
   below; do not include the seed, and do not include issues raised for the first time
   on appeal.

Also report EXCLUDED_SPANS: short verbatim fragments (<=20 words each) you removed from
the situation because they would have leaked the seed. This is an audit trail; be honest
and complete rather than tidy.

Return JSON:
{"situation": "<the stimulus>",
 "seed": {"consideration": "<one sentence>", "why_material": "<one sentence>"},
 "key": [{"label": "<8 words max>", "question": "<one sentence>"}],
 "excluded_spans": ["<fragment>", ...],
 "self_check": {"situation_mentions_seed": true|false,
                "situation_mentions_appeal": true|false}}"""


# --------------------------------------------------------------- three-call extraction
#
# The v1 single call above leaked badly (deviations.md D3): situations carried the seed
# nearly verbatim ("The Board did not directly address the direct service-connection
# claim"). One call cannot reliably write a document that conceals the thing it is
# simultaneously reasoning about.
#
# The replacement splits the work so that the call which WRITES the stimulus has never
# seen the answer, and the cut that decides what it writes from is STRUCTURAL rather than
# semantic:
#
#   1. BOUNDARY  where does the court stop reciting and start analysing? Asked with no
#                mention of the seed, so the cut cannot be placed to hide or expose it.
#   2. HOLDING   the seed, the key, the tribunal. Sighted, separate call. Its output never
#                reaches the writer.
#   3. COMPOSE   BLIND. Receives only the text before the boundary. It cannot leak what it
#                was not shown.
#
# Residual leakage after this is the COURT'S OWN -- what an appellate judge chose to put in
# the fact recitation. That is a property of the corpus, reportable as such, rather than a
# property of my extraction. The leakage audit measures it either way.

BOUNDARY_SYS = """You are marking TWO structural boundaries in a judicial opinion, so that
the court's own recitation of the case can be cut out of it.

A published opinion is layered:

  [caption, docket, counsel]  [SYLLABUS / headnotes / summary]  [RECITATION: facts,
  procedural history, rulings and arguments below]  [ANALYSIS: the court's reasoning]

You must find where the RECITATION starts and where it ends.

START -- the first sentence of the court's own recitation of what happened.
  * Everything before it must be skipped: the caption, docket numbers, counsel listings,
    and CRITICALLY any syllabus, headnote, summary, or "At issue is..." / "We hold that..."
    passage. Those state the outcome and must not be included.
  * The recitation usually opens with a heading such as I., BACKGROUND, FACTS, or
    FACTUAL AND PROCEDURAL HISTORY, or with a plain narrative sentence about the parties.
  * If the opinion opens directly with narrative and has no syllabus, START is that first
    narrative sentence.

END -- the first point where the opinion stops reciting and starts analysing.
  * Often a heading: DISCUSSION, ANALYSIS, or a numbered section; or a sentence like
    "We review de novo" / "We turn to". A standard-of-review sentence IS analysis.
  * Prefer the earliest genuine transition into the court's own reasoning.

For each, return the first 12 words at that point, copied EXACTLY as they appear so the
text can be located by search. If the opinion interleaves so thoroughly that no recitation
block exists, set found=false.

Do not summarise, characterise, or comment on the opinion's subject. Report only the
boundaries.

Return JSON: {"found": true|false,
              "start_words": "<exactly 12 words>",
              "end_words": "<exactly 12 words>",
              "heading": "<the analysis section heading if any, else empty>"}"""

HOLDING_SYS = """You are recording what an appellate court held, for a research index.

Return three things:

1. SEED -- the consideration the appellate court says the tribunal below failed to weigh.
   State it as a consideration a decision-maker could have raised BEFORE deciding, not as a
   verdict or an appellate conclusion. One sentence, plus one sentence on why it mattered.

2. KEY -- the grounds the tribunal below DID address (what it actually considered and
   decided). 3-10 entries, each a short label plus the question it puts in play. Include
   only grounds the opinion states were addressed below. Do NOT include the seed, and do
   not include issues raised for the first time on review.

3. TRIBUNAL_BELOW -- whose decision was under review (trial court, agency, board, BIA,
   juvenile court, intermediate appellate court, ...).

Return JSON:
{"seed": {"consideration": "<one sentence>", "why_material": "<one sentence>"},
 "key": [{"label": "<8 words max>", "question": "<one sentence>"}],
 "tribunal_below": "<short phrase>"}"""

COMPOSE_SYS = """You are turning a court's recitation of a case into a working case file.

You are given ONLY the recitation portion of an opinion -- the facts, the procedural
history, the parties' positions, and the rulings below. You have NOT been given the court's
analysis or its conclusion, and you must not speculate about either.

Write a case file a competent lawyer could work the matter from:

  * Neutral, present-tense case-file voice. Cover the facts, the parties' positions, the
    procedural posture, the relief sought, and any governing statute or standard the
    recitation says was invoked.
  * Write it at the posture of the decision-maker whose decision is being reviewed. If the
    recitation shows an earlier ruling under review, include what was decided, on what
    record, and what is argued about it -- that posture is part of the file.
  * Do NOT refer to the reviewing court, this appeal, the outcome, or any error.
  * Do NOT flag, foreshadow, or draw attention to any particular issue as important,
    unresolved, overlooked, or contested. Give every part of the recitation even treatment;
    a reader must not be able to tell which issue the case turned on.
  * Include the ordinary, unremarkable detail as well as the striking detail. A file that
    keeps only what seems significant tells the reader what is significant.
  * Preserve substance over concision. Do not compress the recitation into a summary --
    length is fine.
  * Invent nothing. Everything in the file must trace to the recitation.

Return JSON: {"situation": "<the case file>"}"""


def body(rec):
    t = "\n\n".join(p["text"] for p in rec.get("opinions", []))
    t = re.sub(r"[ \t]+", " ", t)
    if len(t) <= HEAD + TAIL:
        return t
    return t[:HEAD] + "\n\n[... middle of opinion omitted ...]\n\n" + t[-TAIL:]


def full_text(rec):
    t = "\n\n".join(p["text"] for p in rec.get("opinions", []))
    return re.sub(r"[ \t]+", " ", t)


def locate_boundary(text, first_words, after=0):
    """Find a boundary by literal search, then fuzzily. Returns an offset or None.

    Literal first: the boundary call is asked to copy words verbatim, so an exact hit is
    the common case and is unambiguous. The fallback matches on the first 5 words with
    flexible whitespace, which survives the line-wrapping in plain_text. Returns None
    rather than guessing -- a mislocated cut would silently hand the writer the court's
    analysis or its syllabus, which is the exact failure this design removes.
    """
    fw = (first_words or "").strip()
    if not fw:
        return None
    i = text.find(fw, after)
    if i >= 0:
        return i
    words = re.findall(r"\S+", fw)[:5]
    if len(words) < 3:
        return None
    pat = r"\s+".join(re.escape(w) for w in words)
    m = re.search(pat, text[after:])
    return after + m.start() if m else None


MIN_RECITATION = 1500   # below this the cut left nothing to compose a case file from


def extract_case(rec, model, notes):
    """Three calls: structural boundary, sighted holding, blind compose."""
    text = full_text(rec)

    b = claude_json(model, BOUNDARY_SYS, f"OPINION\n{text[:HEAD+TAIL]}", max_tokens=800)
    if not b.get("found"):
        notes.append("no boundary found")
        return None
    start = locate_boundary(text, b.get("start_words", ""))
    if start is None:
        notes.append(f"start not locatable: {str(b.get('start_words'))[:40]!r}")
        return None
    # The END must come after the START, or the syllabus would be re-admitted through a
    # cut that reads backwards.
    cut = locate_boundary(text, b.get("end_words", ""), after=start + MIN_RECITATION)
    if cut is None:
        notes.append(f"end not locatable after start: {str(b.get('end_words'))[:40]!r}")
        return None
    recitation = text[start:cut].strip()
    if len(recitation) < MIN_RECITATION:
        notes.append(f"recitation too short ({len(recitation)} chars)")
        return None

    h = claude_json(model, HOLDING_SYS, f"OPINION\n{body(rec)}", max_tokens=3000)
    if not h.get("seed") or not h.get("key"):
        notes.append("holding call incomplete")
        return None

    # BLIND: only the recitation. The seed and the analysis are not in this context.
    c = claude_json(model, COMPOSE_SYS, f"RECITATION\n{recitation}", max_tokens=8000)
    situation = (c.get("situation") or "").strip()
    if len(situation) < 800:
        notes.append(f"composed situation too short ({len(situation)})")
        return None

    return {"situation": situation, "seed": h["seed"], "key": h["key"],
            "tribunal_below": h.get("tribunal_below"),
            "extraction": {"method": "three-call blind compose, two-sided cut (D3)",
                           "boundary_heading": b.get("heading", ""),
                           "start_words": b.get("start_words", ""),
                           "end_words": b.get("end_words", ""),
                           "start_offset": start, "end_offset": cut,
                           "skipped_preamble_chars": start,
                           "recitation_chars": len(recitation),
                           "opinion_chars": len(text)}}


def dedupe(files):
    """One case per (case name, court) -- deviations.md D2.

    The search returns the same decision under more than one cluster: an identical
    docket filed twice (People v Eads, 168205), and companion appeals consolidated in
    one opinion (Carter v. Cabell, 24-6706 and 24-6741). Both would double-count, and
    the companions are not independent -- they share facts, record and holding, so a
    generator's hit or miss on one is not new evidence about the other.

    Keeps the longest cached text in each group, which is the fullest opinion.
    """
    groups = {}
    for f in files:
        rec = json.load(open(os.path.join(RAW, f)))
        k = ((rec.get("case_name") or "").strip().lower(),
             (rec.get("court") or "").strip().lower())
        groups.setdefault(k, []).append((rec.get("chars", 0), f))
    kept = sorted(max(v)[1] for v in groups.values())
    if len(kept) < len(files):
        print(f"dedupe: {len(files)} cached -> {len(kept)} distinct cases "
              f"({len(files)-len(kept)} duplicate/companion clusters dropped)")
    return kept


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="0 = all cached")
    ap.add_argument("--screen-only", action="store_true")
    ap.add_argument("--model", default=EXTRACTOR)
    a = ap.parse_args()

    screen_path = os.path.join(CORPUS, "screen.json")
    cases_path = os.path.join(CORPUS, "cases.json")
    screened = json.load(open(screen_path))["screened"] if os.path.exists(screen_path) else {}
    cases = json.load(open(cases_path))["cases"] if os.path.exists(cases_path) else {}

    files = sorted(f for f in os.listdir(RAW) if f.endswith(".json"))
    files = dedupe(files)
    if a.limit:
        files = files[:a.limit]
    print(f"{len(files)} cached opinions   extractor {a.model}")
    print(f"already screened: {len(screened)}   already extracted: {len(cases)}\n")

    kept = 0
    for n, f in enumerate(files, 1):
        cid = f[:-5]
        rec = json.load(open(os.path.join(RAW, f)))
        name = (rec.get("case_name") or "")[:46]

        if cid not in screened:
            try:
                out = claude_json(a.model, SCREEN_SYS,
                                  f"OPINION\n{body(rec)}", max_tokens=1500)
            except Exception as e:  # noqa: BLE001
                print(f"  {n:>3} {cid} SCREEN-ERROR {str(e)[:70]}")
                continue
            screened[cid] = {"cluster_id": cid, "case_name": rec.get("case_name"),
                             "court": rec.get("court"), "date_filed": rec.get("date_filed"),
                             "url": rec.get("url"), **out}
            json.dump({"model": a.model, "n": len(screened), "screened": screened},
                      open(screen_path, "w"), indent=2)

        s = screened[cid]
        if not s.get("keep"):
            print(f"  {n:>3} {cid} drop  {name:<46} {s.get('reason','')[:40]}")
            continue
        kept += 1
        print(f"  {n:>3} {cid} KEEP  {name:<46} {s.get('missed_short','')[:44]}")

        if a.screen_only or cid in cases:
            continue
        notes = []
        try:
            ex = extract_case(rec, a.model, notes)
        except Exception as e:  # noqa: BLE001
            print(f"      EXTRACT-ERROR {str(e)[:70]}")
            continue
        if not ex:
            print(f"      EXTRACT-SKIPPED: {'; '.join(notes)}")
            continue
        cases[cid] = {"cluster_id": cid, "case_name": rec.get("case_name"),
                      "court": rec.get("court"), "date_filed": rec.get("date_filed"),
                      "url": rec.get("url"),
                      "holding_quote": s.get("holding_quote"),
                      "extractor": a.model, **ex}
        json.dump({"extractor": a.model, "n": len(cases), "cases": cases},
                  open(cases_path, "w"), indent=2)
        m = ex["extraction"]
        print(f"      situation {len(ex['situation']):>5} chars   key {len(ex['key'])} pts"
              f"   recitation {m['recitation_chars']:>6}/{m['opinion_chars']} "
              f"[{(m['boundary_heading'] or 'no heading')[:22]}]")

    print(f"\nscreened {len(screened)}   kept {sum(1 for v in screened.values() if v.get('keep'))}"
          f"   extracted {len(cases)}")
    print(f"  {screen_path}\n  {cases_path}")
    if not a.screen_only:
        print("\nnext: ./generate_miss.py")


if __name__ == "__main__":
    main()
