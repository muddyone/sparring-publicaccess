#!/usr/bin/env python3
"""
capture_check.py — Phase-0 capture-completeness gate for the seeded-defect **v3** run.

Enforces the v3 pre-registration (`pre-registration-v3.md`) §7 capture protocol — the
*abort condition* — and operationalizes the §9 Phase-0 dry-run. A v3 case is admissible
only if all of its inputs were persisted (so the verifier can run end-to-end later) and
every in-briefing fact-id a concern cites actually resolves to a fact in that case's
briefing. This is the single check that would have prevented the v2 data loss, where only
the answer-keys were saved and the briefings were lost (see `pre-registration-v3.md` §1).

Per-case contract (one `case-<id>.json` per case; see `v3-run/case-EXAMPLE.json`):
  identity   : id, dc, domain, answer_key            (carried over from v2)
  §7 item 1  : recommendation        — the flawed artifact under review
  §7 item 2  : briefing              — {context, facts:[{id,text,source?}]} with STABLE fact-ids
  §7 item 3  : prompts               — {B,S,T} exact prompts issued
  §7 item 4  : outputs               — {B:str, S:{generator,challenger,converged}, T:str}
  §7 item 5  : concerns              — [{id,condition,text,cited_artifact,atomic:[...]}]
  §7 item 6  : codings               — [{concern_id,coder,substrate,ts,legitimacy,grounding}]

Abort rule (§7): a case missing any of items 1–5 is VOID and must be regenerated.
Item 6 (codings) is produced after coding, so it is required only in `--phase full`.

Usage:
  python3 scripts/capture_check.py v3-run/case-EXAMPLE.json      # one case
  python3 scripts/capture_check.py v3-run/                       # every case-*.json in a dir
  python3 scripts/capture_check.py --phase capture v3-run/       # items 1–5 only (post-generation, pre-coding)
  python3 scripts/capture_check.py --selftest                    # prove the gate PASSES valid / ABORTS broken

Exit: 0 = all admissible · 2 = at least one case VOID (abort the run) · 1 = usage error.
Stdlib only.
"""

import json
import os
import re
import sys

LEGIT = {"TRUE_POSITIVE", "FALSE_POSITIVE"}
GROUND = {"GROUNDED_VERIFIED", "GROUNDED_REFUTED", "UNGROUNDED"}
CONDS = {"B", "S", "T"}
# a cited artifact that LOOKS like an in-briefing fact reference (must then resolve);
# external artifacts (CWE-/RFC/DOI/http) are the verifier's job, not checked here.
FACT_REF = re.compile(r"^(F#?\d+|#\d+|§\S+)$")


def _is_nonempty_str(x):
    return isinstance(x, str) and x.strip() != ""


def check_case(case, phase):
    """Return a list of error strings; empty list == admissible."""
    e = []

    # identity
    for k in ("id", "dc", "domain"):
        if not _is_nonempty_str(case.get(k)):
            e.append(f"missing/empty identity field: {k}")
    if not isinstance(case.get("answer_key"), dict) or not case["answer_key"].get("planted_defect"):
        e.append("answer_key missing or has no planted_defect")

    # §7 item 1 — recommendation
    if not _is_nonempty_str(case.get("recommendation")):
        e.append("item 1: recommendation missing/empty")

    # §7 item 2 — briefing (+ stable fact-ids)
    fact_ids = set()
    br = case.get("briefing")
    if not isinstance(br, dict):
        e.append("item 2: briefing missing or not an object")
    else:
        if not _is_nonempty_str(br.get("context")):
            e.append("item 2: briefing.context missing/empty")
        facts = br.get("facts")
        if not isinstance(facts, list) or not facts:
            e.append("item 2: briefing.facts missing/empty")
        else:
            for i, f in enumerate(facts):
                fid = f.get("id") if isinstance(f, dict) else None
                if not _is_nonempty_str(fid):
                    e.append(f"item 2: briefing.facts[{i}] has no stable id")
                elif fid in fact_ids:
                    e.append(f"item 2: duplicate fact-id {fid!r}")
                else:
                    fact_ids.add(fid)
                if isinstance(f, dict) and not _is_nonempty_str(f.get("text")):
                    e.append(f"item 2: fact {fid!r} has no text")

    # §7 item 3 — prompts
    pr = case.get("prompts")
    if not isinstance(pr, dict):
        e.append("item 3: prompts missing or not an object")
    else:
        for c in CONDS:
            if not _is_nonempty_str(pr.get(c)):
                e.append(f"item 3: prompts.{c} missing/empty")

    # §7 item 4 — outputs
    out = case.get("outputs")
    if not isinstance(out, dict):
        e.append("item 4: outputs missing or not an object")
    else:
        if not _is_nonempty_str(out.get("B")):
            e.append("item 4: outputs.B missing/empty")
        if not _is_nonempty_str(out.get("T")):
            e.append("item 4: outputs.T missing/empty")
        s = out.get("S")
        if not isinstance(s, dict) or not _is_nonempty_str(s.get("converged")):
            e.append("item 4: outputs.S must be an object with a non-empty 'converged'")
        elif not (_is_nonempty_str(s.get("generator")) and _is_nonempty_str(s.get("challenger"))):
            e.append("item 4: outputs.S should record both 'generator' and 'challenger' transcripts")

    # §7 item 5 — concerns (+ fact-id resolution, the §9 Phase-0 check)
    concern_ids = set()
    co = case.get("concerns")
    if not isinstance(co, list) or not co:
        e.append("item 5: concerns missing/empty")
    else:
        for i, c in enumerate(co):
            cid = c.get("id") if isinstance(c, dict) else None
            if not _is_nonempty_str(cid):
                e.append(f"item 5: concerns[{i}] has no id")
            else:
                concern_ids.add(cid)
            if isinstance(c, dict):
                if c.get("condition") not in CONDS:
                    e.append(f"item 5: concern {cid!r} has bad condition {c.get('condition')!r}")
                if not _is_nonempty_str(c.get("text")):
                    e.append(f"item 5: concern {cid!r} has no text")
                if not isinstance(c.get("atomic"), list) or not c["atomic"]:
                    e.append(f"item 5: concern {cid!r} not atomized (atomic[] missing)")
                art = c.get("cited_artifact")
                if isinstance(art, str) and FACT_REF.match(art.strip()):
                    if art.strip() not in fact_ids:
                        e.append(f"item 5: concern {cid!r} cites in-briefing fact {art!r} "
                                 f"that does NOT resolve in this briefing  <-- the v2 failure mode")

    # §7 item 6 — codings (only enforced in full phase)
    if phase == "full":
        cd = case.get("codings")
        if not isinstance(cd, list) or not cd:
            e.append("item 6: codings missing/empty (required in --phase full)")
        else:
            for i, c in enumerate(cd):
                if not isinstance(c, dict):
                    e.append(f"item 6: codings[{i}] not an object"); continue
                if c.get("concern_id") not in concern_ids:
                    e.append(f"item 6: coding references unknown concern_id {c.get('concern_id')!r}")
                for k in ("coder", "substrate", "ts"):
                    if not _is_nonempty_str(c.get(k)):
                        e.append(f"item 6: coding for {c.get('concern_id')!r} missing {k}")
                if c.get("legitimacy") not in LEGIT:
                    e.append(f"item 6: coding for {c.get('concern_id')!r} bad legitimacy {c.get('legitimacy')!r}")
                if c.get("grounding") not in GROUND:
                    e.append(f"item 6: coding for {c.get('concern_id')!r} bad grounding {c.get('grounding')!r}")

    return e


def _iter_case_paths(arg):
    if os.path.isdir(arg):
        for name in sorted(os.listdir(arg)):
            if name.startswith("case-") and name.endswith(".json"):
                yield os.path.join(arg, name)
    else:
        yield arg


def run(paths, phase):
    any_void = False
    n = 0
    for arg in paths:
        for p in _iter_case_paths(arg):
            n += 1
            try:
                case = json.load(open(p))
            except Exception as ex:
                print(f"ABORT  {p}: unreadable JSON — {ex}")
                any_void = True
                continue
            errs = check_case(case, phase)
            label = case.get("id", os.path.basename(p))
            if errs:
                any_void = True
                print(f"ABORT  {label}  ({p}) — VOID, regenerate:")
                for er in errs:
                    print(f"         - {er}")
            else:
                print(f"PASS   {label}  ({p}) — capture complete ({phase} phase)")
    if n == 0:
        print("no case-*.json found", file=sys.stderr)
        return 1
    print(f"\n{'ABORT' if any_void else 'OK'}: {n} case(s) checked, "
          f"{'at least one VOID — do not proceed' if any_void else 'all admissible'}.")
    return 2 if any_void else 0


def _selftest():
    valid = json.load(open(os.path.join(os.path.dirname(__file__), "..", "v3-run", "case-EXAMPLE.json")))
    assert check_case(valid, "full") == [], "EXAMPLE should be admissible"
    # break it three ways the v2 loss / a bad capture would look like:
    broken = json.loads(json.dumps(valid))
    del broken["briefing"]                              # lost the briefing (the v2 failure)
    assert any("briefing missing" in x for x in check_case(broken, "full"))
    broken2 = json.loads(json.dumps(valid))
    broken2["concerns"][0]["cited_artifact"] = "F999"   # cite a fact-id that doesn't resolve
    assert any("does NOT resolve" in x for x in check_case(broken2, "full"))
    broken3 = json.loads(json.dumps(valid))
    broken3["concerns"][0].pop("atomic")                # not atomized
    assert any("not atomized" in x for x in check_case(broken3, "full"))
    print("selftest OK: gate PASSES the valid example and ABORTS lost-briefing / "
          "unresolved-fact-id / un-atomized cases.")
    return 0


def main(argv):
    phase = "full"
    args = []
    i = 0
    while i < len(argv):
        if argv[i] == "--selftest":
            return _selftest()
        if argv[i] == "--phase":
            phase = argv[i + 1] if i + 1 < len(argv) else ""
            i += 2
            continue
        args.append(argv[i])
        i += 1
    if phase not in ("capture", "full"):
        print("--phase must be 'capture' or 'full'", file=sys.stderr)
        return 1
    if not args:
        print(__doc__)
        return 1
    return run(args, phase)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
