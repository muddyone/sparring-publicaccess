#!/usr/bin/env python3
"""Does off-key discovery recover the consideration a real court failed to weigh?

FOUR PASSES. The first two are the parent study's, unchanged, so its machinery transfers.

  Pass A  matching   items + the KEY (what the tribunal below did address)  -> recall,
                     and which items are absorbed by the key
  Pass B  audit      items + the SITUATION, never the key                   -> sound /
                     raised / material / duplicate, hence signal and off-key
  Pass C  seed-match items + the SITUATION + a SHUFFLED list of considerations, of which
                     exactly one is the real seed and the rest are decoys from other
                     cases                                                  -> recovery
  Pass D  leakage    the SITUATION + the seed                               -> does the
                     stimulus telegraph its own answer?

WHY PASS C IS SHUFFLED AND MIXED. The parent study's sharpest documented failure was a
sanity test that could only detect error in one direction. Scoring the decoys in the same
call as the real seed, with no marker distinguishing them, makes the false-positive rate a
measurement on the identical judge, prompt and context rather than a separate experiment
that could differ in a dozen ways. A generous judge inflates BOTH numbers, and the decoy
column shows it.

Pass C also asks whether each consideration is even APPLICABLE to these facts. A decoy that
genuinely applies (generic requirements -- make findings, state reasons -- apply everywhere)
is not the same error as a decoy the judge endorses despite it having nothing to do with the
case. The second is the one that would void the study.

THE TWO RECOVERY NUMBERS.

  raw recovery      any emitted item addresses the seed. Upper bound, no gating.
  off-key recovery  an item addressing the seed is ALSO in the off-key set -- signal, and
                    matched to no key point. This is the measure under validation.

Their difference is deviation D14 made observable: items that address the seed but were
absorbed into the key by a coarse match. In the parent hold-out that effect made the
structured walk's recovery undefined and was inferred; here it is counted.

Usage:
  ./score_seed.py [-k 2] [--decoys 3] [--rungs g1,g3]
"""
import argparse, collections, glob, json, os, random, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))
RUNS = os.path.abspath(os.path.join(HERE, "..", "runs"))
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "coverage-residual-validation-2026-08-29", "scripts")))
sys.path.insert(0, os.path.abspath(os.path.join(
    HERE, "..", "..", "resolver-iteration-2026-06-29", "scripts")))

from score_pair import pass_a, pass_b, majority, norm_id, GPT, CLAUDE  # noqa: E402
from lib_llm import gpt_json, claude_json  # noqa: E402


# ------------------------------------------------------------------ Pass C: seed match

PASS_C_SYS = """You are checking whether a candidate issue list addresses certain
considerations.

You are given a case file, a numbered candidate issue list produced by someone reviewing
that case file, and a lettered list of CONSIDERATIONS. The considerations come from mixed
sources; some bear on this case and some do not. Nothing distinguishes them and you should
not try to guess which is which.

For EACH consideration, judge two things independently:

  applicable  - do THESE facts actually put this consideration in play? Answer on the
                case file alone. A consideration can be perfectly sensible in the abstract
                and still not be applicable here.
  addressed   - does the candidate list contain an item that puts this consideration in
                play? Wording will differ; judge substance, not phrasing. An item stated
                more narrowly or more broadly still counts if it raises the same question.
                Answer this even when applicable is false.

Do not credit an item that merely touches the same area of law. The item must raise the
consideration itself.

Return JSON:
{"checks":[{"id":"<letter>","applicable":bool,"addressed":bool,"by":[<item indices>],
            "note":"<8 words max>"}]}
Every consideration must appear exactly once."""


def pass_c(items, situation, considerations, k, model):
    """considerations: list of (letter, text). Returns k replicate dicts letter -> verdict."""
    cand = "\n".join(f"[{i}] {it}" for i, it in enumerate(items))
    cons = "\n".join(f"{ltr}. {txt}" for ltr, txt in considerations)
    user = (f"CASE FILE\n{situation}\n\nCANDIDATE ISSUE LIST\n{cand}\n\n"
            f"CONSIDERATIONS\n{cons}")
    reps = []
    for _ in range(k):
        out = (gpt_json(model, PASS_C_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_C_SYS, user, max_tokens=4000))
        rep = {}
        for c in out.get("checks", []):
            cid = str(c.get("id", "")).strip().strip(".").upper()[:1]
            if cid:
                rep[cid] = {"applicable": bool(c.get("applicable")),
                            "addressed": bool(c.get("addressed")),
                            "by": [int(x) for x in (c.get("by") or [])
                                   if str(x).isdigit()]}
        reps.append(rep)
    return reps


# ------------------------------------------------------------------ Pass D: leakage

PASS_D_SYS = """You are auditing a research stimulus. Two independent judgments.

You are given a CASE FILE and one CONSIDERATION. The case file was edited from a longer
document that discussed this consideration; the edit was supposed to remove every trace of
it while leaving the file workable.

JUDGMENT 1 -- RAISABLE. Could a competent reviewer, holding only this case file, raise this
consideration on their own? Say false only when the file lacks the context in which the
consideration could exist at all -- most often because the consideration belongs to a
procedural posture the file does not occupy (it concerns how an earlier decision should be
reviewed, but the file is written as a first-instance matter; or it turns on a record or a
ruling the file never mentions). Difficulty is NOT the test: a consideration that is hard,
subtle, or easy to overlook is still raisable. Only impossibility counts.

JUDGMENT 2 -- LEAKAGE. How much trace of the consideration remains in the file?
Rate the case file:
  explicit - it names the consideration, its governing standard, or its doctrine outright.
             A reader would not have to think.
  hinted   - it does not name it, but it dwells on facts that point at it unusually hard:
             a detail included with no other purpose, a conspicuous emphasis, an odd
             specificity. A reader would likely be steered to it.
  neutral  - the facts that bear on it are present as ordinary case facts with no special
             emphasis, or are absent. A reader would have to raise it on their own.

Judge emphasis and salience, not mere presence: the facts underlying the consideration
SHOULD be in the case file -- otherwise it could not be raised at all. The question is
whether the file points at the consideration.

Procedural posture is NOT leakage. A file that says an earlier motion was denied and the
matter proceeded is stating the posture the decision-maker sits in. Rate it explicit only
if the file goes further and points at what should be done about that posture.

EVIDENCE MUST BE VERBATIM. Quote a span COPIED EXACTLY from the case file, at least 8 words
long. Do not paraphrase, summarise, stitch fragments together, or reconstruct what the file
"in effect" says -- a quote that cannot be found in the file by exact search is a wrong
answer. If you cannot produce such a quote, the file is not explicit: rate it hinted or
neutral and leave evidence empty.

Return JSON:
{"raisable":true|false,"raisable_reason":"<=20 words>",
 "stratum":"explicit|hinted|neutral","evidence":"<verbatim span, >=8 words, or empty>",
 "reason":"<=20 words>"}"""


def pass_d(situation, seed_text, k, model):
    user = f"CASE FILE\n{situation}\n\nCONSIDERATION\n{seed_text}"
    votes, raisable = [], []
    for _ in range(k):
        out = (gpt_json(model, PASS_D_SYS, user) if model.startswith("gpt")
               else claude_json(model, PASS_D_SYS, user, max_tokens=1200))
        s = str(out.get("stratum", "")).strip().lower()
        if s in ("explicit", "hinted", "neutral"):
            votes.append((s, out.get("evidence", ""), out.get("reason", "")))
        raisable.append((bool(out.get("raisable")), out.get("raisable_reason", "")))
    if not votes:
        return {"stratum": "unknown", "evidence": "", "reason": "", "raisable": True}
    tally = collections.Counter(v[0] for v in votes)
    # Ties resolve to the MORE leaky stratum: leakage inflates recovery, so an
    # undecided case belongs in the confounded bucket, not the clean one.
    order = {"explicit": 0, "hinted": 1, "neutral": 2}
    top = sorted(tally.items(), key=lambda kv: (-kv[1], order[kv[0]]))[0][0]
    ev = next((v for v in votes if v[0] == top), ("", "", ""))
    # Raisability ties resolve to RAISABLE -- dropping a case is the intervention, so
    # an undecided stimulus stays in and counts against recovery rather than vanishing.
    n_yes = sum(1 for r, _ in raisable if r)
    ok = n_yes * 2 >= len(raisable) if raisable else True

    # Verify the quote. An "explicit" verdict whose evidence cannot be found in the file
    # by normalised search is the judge reconstructing what the file "in effect" says --
    # which is inference, not leakage. Downgrade it to hinted and record the downgrade
    # rather than letting an unverifiable quote push a case out of the headline stratum.
    def norm(s):
        return " ".join((s or "").lower().replace("’", "'").split())

    verified = bool(ev[1]) and norm(ev[1])[:60] in norm(situation)
    downgraded = False
    if top == "explicit" and not verified:
        top, downgraded = "hinted", True
    return {"stratum": top, "evidence": ev[1], "reason": ev[2],
            "unanimity": tally[top] / len(votes),
            "quote_verified": verified, "downgraded_unverified": downgraded,
            "raisable": ok,
            "raisable_reason": next((m for r, m in raisable if r == ok), "")}


# ------------------------------------------------------------------ scoring one run

def seed_text(seed):
    c = (seed or {}).get("consideration", "")
    w = (seed or {}).get("why_material", "")
    return f"{c} {w}".strip()


def as_gold(key):
    """Adapt the extracted key to the parent study's gold shape so pass_a transfers.

    The holding call usually returns {label, question} objects but occasionally emits a
    plain list of strings for the same field. Both are accepted: rejecting the string
    form would silently drop whole cases from the corpus on a formatting difference, and
    a dropped case is indistinguishable from a case that scored zero.
    """
    n = max(1, len(key))
    w = 100.0 / n
    out = []
    for i, p in enumerate(key):
        if isinstance(p, str):
            label, question = p, ""
        elif isinstance(p, dict):
            label = str(p.get("label", "") or "")
            question = str(p.get("question", "") or "")
        else:
            label, question = str(p), ""
        out.append({"point_id": f"K{i+1}", "weight_pct": round(w, 2),
                    "issue": f"{label}: {question}".strip(": ").strip(),
                    "point": label})
    return out


def score_run(run, case, decoy_specs, k, match_model, audit_model, seed_model, rng):
    items = [i.get("label", "") for i in run["raw"].get("issues", [])]
    if not items:
        return None
    situation, gold = case["situation"], as_gold(case["key"])

    A = pass_a(items, gold, k, match_model)
    B = pass_b(items, situation, k, audit_model)

    covered, cites = {}, {}
    for g in gold:
        v, _ = majority(A, norm_id(g["point_id"]), "covered")
        covered[g["point_id"]] = bool(v)
    for rep in A:
        for kid, m in rep.items():
            if m["covered"]:
                for i in m["by"]:
                    cites[i] = cites.get(i, 0) + 1
    key_matched = {i for i, c in cites.items() if c * 2 >= len(A)}
    recall = sum(g["weight_pct"] for g in gold if covered[g["point_id"]]) / 100.0

    verdicts, signal = {}, set()
    for i in range(len(items)):
        s, _ = majority(B, i, "sound")
        r, _ = majority(B, i, "raised")
        m, _ = majority(B, i, "material")
        dup = sum(1 for rep in B
                  if i in rep and rep[i].get("duplicate_of") is not None) * 2 >= len(B)
        verdicts[i] = {"sound": s, "raised": r, "material": m, "duplicate": dup}
        if s and r and m and not dup:
            signal.add(i)
    offkey = signal - key_matched

    # Positive control, over points the run actually covered (parent study's respecified
    # form -- otherwise it is just recall again).
    ctrl_ok = ctrl_n = 0
    for g in gold:
        if not covered[g["point_id"]]:
            continue
        ctrl_n += 1
        kid = norm_id(g["point_id"])
        c = {i for rep in A for k2, m in rep.items() if k2 == kid and m["covered"]
             for i in m["by"]}
        ctrl_ok += bool([i for i in c if verdicts.get(i, {}).get("sound")
                         and verdicts.get(i, {}).get("raised")
                         and verdicts.get(i, {}).get("material")])

    # Pass C: the real seed and the decoys, shuffled, indistinguishable.
    specs = [("SEED", seed_text(case["seed"]))] + [("DECOY", t) for _, t in decoy_specs]
    rng.shuffle(specs)
    letters = [chr(ord("A") + i) for i in range(len(specs))]
    considerations = [(letters[i], specs[i][1]) for i in range(len(specs))]
    C = pass_c(items, situation, considerations, k, seed_model)

    checks = []
    for i, ltr in enumerate(letters):
        kind = specs[i][0]
        add, _ = majority(C, ltr, "addressed")
        app, _ = majority(C, ltr, "applicable")
        by = collections.Counter(j for rep in C for j in (rep.get(ltr, {}).get("by") or []))
        cited = {j for j, n in by.items() if n * 2 >= len(C)}
        checks.append({
            "kind": kind, "letter": ltr, "text": specs[i][1][:160],
            "applicable": bool(app), "addressed": bool(add),
            "cited": sorted(cited),
            # off-key recovery: at least one citing item is signal AND unabsorbed by the key
            "offkey_recovered": bool(add and (cited & offkey)),
            # the D14 gap: addressed, but every citing item was absorbed into the key
            "absorbed_only": bool(add and cited and not (cited & offkey)),
            # PARTIAL CREDIT (the fix the parent study specified). Drops the exclusive-match
            # rule: an item counts for the seed if the blind judge rated it signal, whether
            # or not the matcher ALSO credited it to a key point. The quality bar is
            # unchanged -- still sound + raised + material + non-duplicate -- so this is
            # not a looser measure, only one that stops discarding evidence for being
            # dual-purpose.
            "partial_recovered": bool(add and (cited & signal)),
        })

    seed_chk = next(c for c in checks if c["kind"] == "SEED")
    return {
        "cluster_id": run["cluster_id"], "rung": run["rung"], "replicate": run["replicate"],
        "emitted": len(items), "signal": len(signal), "offkey": len(offkey),
        "key_matched": len(key_matched),
        "recall": recall, "yield": len(signal) / len(items),
        "offkey_rate": len(offkey) / len(items),
        "control": (ctrl_ok / ctrl_n) if ctrl_n else None, "control_n": ctrl_n,
        "raw_recovery": seed_chk["addressed"],
        "offkey_recovery": seed_chk["offkey_recovered"],
        "absorbed_only": seed_chk["absorbed_only"],
        "partial_recovery": seed_chk["partial_recovered"],
        "signal_idx": sorted(signal), "offkey_idx": sorted(offkey),
        "seed_applicable": seed_chk["applicable"],
        "checks": checks,
    }


# ------------------------------------------------------------------ main

class SingleWriter:
    """Refuse to start if another scorer is already writing these files (deviations.md D5).

    Two scorers ran concurrently once, each computed the leakage audit independently, and
    each stamped rows with its own draw -- moving the reported headline by 8 points. The
    run scores were unaffected (per-run and idempotent); the stratum labels were not.
    A stale lock from a killed process is reclaimed rather than blocking forever.
    """

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        if os.path.exists(self.path):
            try:
                pid = int(open(self.path).read().strip())
                os.kill(pid, 0)
            except (ValueError, ProcessLookupError, PermissionError, OSError):
                print(f"[lock] reclaiming stale lock at {self.path}")
            else:
                sys.exit(f"another scorer is running (pid {pid}); refusing to race on "
                         f"scored.json/leakage.json. Remove {self.path} if that is wrong.")
        with open(self.path, "w") as fh:
            fh.write(str(os.getpid()))
        return self

    def __exit__(self, *exc):
        try:
            os.remove(self.path)
        except OSError:
            pass


def _main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", type=int, default=2, help="replicates per per-run judging pass")
    ap.add_argument("--k-leak", type=int, default=None,
                    help="replicates for the leakage audit (pass D). Defaults to -k. "
                         "Worth raising INDEPENDENTLY: pass D runs once per CASE (~34 calls "
                         "per replicate) while A/B/C run once per RUN (~136 each), so "
                         "stabilising the strata is an order of magnitude cheaper than "
                         "stabilising the run scores. D5 found two cases flipping stratum "
                         "between k=2 draws, which is what collapsed the hinted/explicit "
                         "gradient in result.md sec.2.")
    ap.add_argument("--decoys", type=int, default=3)
    ap.add_argument("--rungs", default="g1,g3")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--match-model", default=GPT)
    ap.add_argument("--audit-model", default=CLAUDE)
    ap.add_argument("--seed-model", default=CLAUDE, help="pass C judge")
    ap.add_argument("--leak-model", default=GPT,
                    help="pass D judge; different vendor from the extractor")
    ap.add_argument("--seed", type=int, default=20260829, help="decoy shuffle seed")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    k_leak = a.k_leak or a.k
    cases = json.load(open(os.path.join(CORPUS, "cases.json")))["cases"]
    ids = sorted(cases)
    if a.limit:
        ids = ids[:a.limit]
    rng = random.Random(a.seed)

    print(f"cases {len(ids)}   rungs {a.rungs}   k={a.k} (leakage k={k_leak})   "
          f"decoys/case {a.decoys}")
    print(f"matcher {a.match_model}   blind judge {a.audit_model}   "
          f"seed judge {a.seed_model}   leakage {a.leak_model}\n")

    # ---- Pass D: leakage, once per case, cached.
    leak_path = os.path.join(CORPUS, "leakage.json")
    leak = json.load(open(leak_path))["leakage"] if os.path.exists(leak_path) else {}
    todo = [c for c in ids if c not in leak]
    if todo:
        print(f"leakage audit on {len(todo)} cases")
        for cid in todo:
            try:
                leak[cid] = pass_d(cases[cid]["situation"],
                                   seed_text(cases[cid]["seed"]), k_leak, a.leak_model)
            except Exception as e:  # noqa: BLE001
                print(f"  {cid} LEAK-ERROR {str(e)[:70]}")
                continue
            json.dump({"model": a.leak_model, "k": k_leak, "leakage": leak},
                      open(leak_path, "w"), indent=2)
            print(f"  {cid}  {leak[cid]['stratum']}")
        print()
    strata = collections.Counter(leak[c]["stratum"] for c in ids if c in leak)
    print("leakage strata: " + "  ".join(f"{k2} {v}" for k2, v in strata.items()))

    # ---- stimulus-validity gate (deviations.md D1). Judged from the situation and the
    # seed ALONE, with no generator output in existence -- so this is corpus construction,
    # not an outcome-conditioned filter. A stimulus whose posture makes the seed
    # impossible to raise measures extraction quality, not coverage.
    void = [c for c in ids if c in leak and not leak[c].get("raisable", True)]
    if void:
        print(f"stimulus-validity gate: dropping {len(void)} case(s) whose seed is not "
              f"raisable from the file")
        for c in void:
            print(f"    {c}  {cases[c]['case_name'][:44]}  "
                  f"{leak[c].get('raisable_reason','')[:60]}")
    ids = [c for c in ids if c not in void]
    print()

    # ---- score every run, cached per run
    scored_path = os.path.join(RUNS, "scored.json")
    scored = json.load(open(scored_path))["rows"] if os.path.exists(scored_path) else {}
    rungs = a.rungs.split(",")
    paths = [p for cid in ids for rung in rungs
             for p in sorted(glob.glob(os.path.join(RUNS, f"{cid}.{rung}.r*.json")))]
    print(f"scoring {len(paths)} runs ({sum(1 for p in paths if os.path.basename(p)[:-5] in scored)} cached)")

    for n, p in enumerate(paths, 1):
        rid = os.path.basename(p)[:-5]
        if rid in scored:
            continue
        run = json.load(open(p))
        cid = run["cluster_id"]
        others = [c for c in ids if c != cid]
        rng.shuffle(others)
        decoys = [(c, seed_text(cases[c]["seed"])) for c in others[:a.decoys]]
        try:
            row = score_run(run, cases[cid], decoys, a.k, a.match_model,
                            a.audit_model, a.seed_model, rng)
        except Exception as e:  # noqa: BLE001
            print(f"  {rid}  ERROR {str(e)[:80]}")
            continue
        if not row:
            continue
        row["leakage"] = leak.get(cid, {}).get("stratum", "unknown")
        row["decoy_ids"] = [c for c, _ in decoys]
        scored[rid] = row
        json.dump({"k": a.k, "rows": scored}, open(scored_path, "w"), indent=2)
        print(f"  {n:>4}/{len(paths)} {rid:<28} recall {row['recall']:.2f} "
              f"offkey {row['offkey']:>2}  raw {int(row['raw_recovery'])} "
              f"offkeyrec {int(row['offkey_recovery'])}  [{row['leakage']}]", flush=True)

    # Re-stamp EVERY row's leakage stratum from leakage.json at REPORT time rather than at
    # scoring time. Rows are cached across invocations while the leakage audit can be
    # legitimately re-run (a higher --k-leak, a re-audit), so a stamp written when a row was
    # first scored goes stale silently. That is the shape of D5, which moved a reported
    # headline by 8 points. Stamping here makes leakage.json the single source of truth on
    # every report, whatever order things were computed in.
    restamped = 0
    for r in scored.values():
        cur = leak.get(r["cluster_id"], {}).get("stratum", "unknown")
        if r.get("leakage") != cur:
            r["leakage"] = cur
            restamped += 1
    if restamped:
        json.dump({"k": a.k, "rows": scored}, open(scored_path, "w"), indent=2)
        print(f"re-stamped {restamped} cached row(s) from the current leakage audit\n")

    rows = [r for rid, r in scored.items()
            if r["rung"] in rungs and r["cluster_id"] in ids]
    if not rows:
        sys.exit("nothing scored")
    report(rows, a, cases, leak)


def main():
    with SingleWriter(os.path.join(RUNS, ".score_seed.lock")):
        _main()


def report(rows, a, cases, leak):  # cases used by the exploratory tribunal cut
    def frac(v):
        return statistics.mean(v) if v else float("nan")

    ctrl = [r["control"] for r in rows if r["control"] is not None]
    control = frac(ctrl)

    print("\n" + "=" * 78)
    print("POSITIVE CONTROL (over key points the run covered): "
          f"{control:.2f}   floor 0.90  -> {'PASS' if control >= 0.90 else 'FAIL'}")
    if control < 0.90:
        print("  the blind judge is not reliable enough; off-key figures below are NOT")
        print("  interpretable. Rebuild before reporting.")

    # Negative control -- the number that decides whether anything else is readable.
    dec = [c for r in rows for c in r["checks"] if c["kind"] == "DECOY"]
    dec_add = [c["addressed"] for c in dec]
    dec_inapp = [c["addressed"] for c in dec if not c["applicable"]]
    dec_app = [c["addressed"] for c in dec if c["applicable"]]
    print(f"\nNEGATIVE CONTROL (decoy seeds, n={len(dec)}):")
    print(f"  decoy 'recovered' overall          {frac(dec_add):.2f}")
    print(f"  ... decoys judged NOT applicable   {frac(dec_inapp):.2f}   (n={len(dec_inapp)})"
          "   <- the false-positive rate that matters")
    print(f"  ... decoys judged applicable       {frac(dec_app):.2f}   (n={len(dec_app)})"
          "   <- generic considerations that really do apply")
    verdict = ("CLEAN" if frac(dec_inapp) < 0.10 else
               "MARGINAL" if frac(dec_inapp) < 0.25 else "FIRING")
    print(f"  verdict: {verdict}")
    if verdict == "FIRING":
        print("  the seed judge endorses items for considerations that do not even apply.")
        print("  STOP: no recovery number below is readable (design-note.md §5).")

    print("\n" + "=" * 78)
    print(f"{'stratum':<10} {'n':>4} {'raw':>6} {'offkey':>7} {'partial':>8} "
          f"{'absorb':>7} {'decoy*':>7}")
    print("-" * 78)
    for st in ("neutral", "hinted", "explicit", "unknown"):
        sub = [r for r in rows if r["leakage"] == st]
        if not sub:
            continue
        d = [c["addressed"] for r in sub for c in r["checks"]
             if c["kind"] == "DECOY" and not c["applicable"]]
        print(f"{st:<10} {len(sub):>4} {frac([r['raw_recovery'] for r in sub]):>6.2f} "
              f"{frac([r['offkey_recovery'] for r in sub]):>7.2f} "
              f"{frac([r.get('partial_recovery') for r in sub if 'partial_recovery' in r]):>8.2f} "
              f"{frac([r['absorbed_only'] for r in sub]):>7.2f} {frac(d):>7.2f}")
    print("-" * 78)
    print(f"{'ALL':<10} {len(rows):>4} {frac([r['raw_recovery'] for r in rows]):>6.2f} "
          f"{frac([r['offkey_recovery'] for r in rows]):>7.2f} "
          f"{frac([r.get('partial_recovery') for r in rows if 'partial_recovery' in r]):>8.2f} "
          f"{frac([r['absorbed_only'] for r in rows]):>7.2f} {frac(dec_inapp):>7.2f}")
    print("=" * 78)
    print("raw    = any emitted item addresses the seed (upper bound)")
    print("offkey = an item addressing the seed is ALSO off-key  <- THE MEASURE")
    print("partial= exclusive-match rule DROPPED: any signal item addressing the seed counts")
    print("absorb = addressed, but every citing item was absorbed into the key (D14)")
    print("decoy* = decoys judged not applicable yet 'recovered' -- false-positive floor")

    print("\nby generator:")
    for rung in sorted({r["rung"] for r in rows}):
        sub = [r for r in rows if r["rung"] == rung]
        neu = [r for r in sub if r["leakage"] == "neutral"]
        print(f"  {rung:<4} n={len(sub):>3}  raw {frac([r['raw_recovery'] for r in sub]):.2f}"
              f"  offkey {frac([r['offkey_recovery'] for r in sub]):.2f}"
              f"  | neutral-only n={len(neu):>3} offkey "
              f"{frac([r['offkey_recovery'] for r in neu]):.2f}"
              f"  | items {statistics.mean(r['emitted'] for r in sub):.0f}"
              f"  recall {frac([r['recall'] for r in sub]):.2f}")

    # ---- EXPLORATORY, not pre-registered. Labelled as such wherever it is reported.
    # Roughly a third of the corpus has a REVIEWING body as the tribunal below (an
    # intermediate appellate court, the BIA adopting an IJ, a court on certiorari review).
    # Their seeds tend to be about how the earlier decision should have been reviewed, so
    # the stimulus must carry the posture -- which is also what the leakage audit reacts
    # to. If the two tribunal types behave differently, that is worth knowing before the
    # next corpus is built; it is not a result this study was designed to produce.
    REVIEWING = ("appeal", "review", "adopting", "certiorari", "bia",
                 "board of immigration")

    def is_reviewing(cid):
        t = (cases.get(cid, {}).get("tribunal_below") or "").lower()
        return any(w in t for w in REVIEWING)

    print("\nEXPLORATORY (not pre-registered) -- by tribunal type below:")
    for label, pred in (("first-instance", lambda c: not is_reviewing(c)),
                        ("reviewing", is_reviewing)):
        sub = [r for r in rows if pred(r["cluster_id"])]
        if not sub:
            continue
        neu = [r for r in sub if r["leakage"] == "neutral"]
        share = statistics.mean([r["leakage"] == "neutral" for r in sub])
        print(f"  {label:<15} n={len(sub):>3} over "
              f"{len({r['cluster_id'] for r in sub})} cases   "
              f"raw {frac([r['raw_recovery'] for r in sub]):.2f}   "
              f"offkey {frac([r['offkey_recovery'] for r in sub]):.2f}   "
              f"neutral-stratum share {share:.2f} (n={len(neu)})")

    neutral = [r for r in rows if r["leakage"] == "neutral"]
    print("\n" + "=" * 78)
    print("HEADLINE (pre-registered): off-key recovery, neutral leakage stratum, pooled")
    if len(neutral) < 20:
        print(f"  n={len(neutral)} scored runs in the neutral stratum -- UNDERPOWERED.")
        print("  Reports as reconnaissance, not a result (design-note.md §6).")
    if neutral:
        print(f"  off-key recovery = {frac([r['offkey_recovery'] for r in neutral]):.2f}"
              f"   (raw {frac([r['raw_recovery'] for r in neutral]):.2f},"
              f" n={len(neutral)} runs over"
              f" {len({r['cluster_id'] for r in neutral})} cases)")
    print("=" * 78)

    out = a.out or os.path.join(RUNS, "seed-recovery-report.json")
    json.dump({"k": a.k, "decoys": a.decoys, "rungs": a.rungs,
               "models": {"match": a.match_model, "audit": a.audit_model,
                          "seed": a.seed_model, "leak": a.leak_model},
               "n_runs": len(rows), "n_cases": len({r["cluster_id"] for r in rows}),
               "positive_control": control,
               "negative_control": {"decoy_overall": frac(dec_add),
                                    "decoy_inapplicable": frac(dec_inapp),
                                    "decoy_applicable": frac(dec_app),
                                    "verdict": verdict},
               "raw_recovery": frac([r["raw_recovery"] for r in rows]),
               "offkey_recovery": frac([r["offkey_recovery"] for r in rows]),
               "absorbed_only": frac([r["absorbed_only"] for r in rows]),
               "headline_neutral_offkey": frac([r["offkey_recovery"] for r in neutral]),
               "n_neutral": len(neutral),
               "rows": rows}, open(out, "w"), indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
