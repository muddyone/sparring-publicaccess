#!/usr/bin/env python3
"""
Grounding verifier — P1 + P1.5 (Path A) for the seeded-defect pilot.

Provenance: this is the RESEARCH ORIGIN copy. The same engine is productized in loom
at skills/shared/spar/scripts/verify_grounding.py, where /spar's verification gate calls
it. Keep the two in sync when the engine changes (loom is the product, this is the origin).
This copy resolves cite_check.py via the CITE_CHECK_PY env var (the portable default below
points at a loom-relative path that does not resolve from here — always export the env var).

Makes the v2 grounding axis OBJECTIVE: take each concern + its cited artifact,
resolve it against EXTERNAL truth, and (optionally) judge whether the resolved
artifact actually SUPPORTS the concern's claim.

P1  (resolution, no keys) — does the artifact EXIST?
    backends: literature (Crossref, reusing cite_check.py), cwe (MITRE API),
    rfc (IETF datatracker), code (resolve a path:line / file / symbol against the
    working tree — `repo_root` on the concern or $VERIFY_REPO_ROOT, default cwd),
    pack (resolve the cited fact #/§ against the PROVIDED pack text; needs `pack_text`).
    catches FABRICATION (cited but nonexistent — incl. a missing file/line and a
    pack fact-id not in the pack).
P1.5 (supports-claim judge, needs ANTHROPIC_API_KEY + OPENAI_API_KEY) — is the
    real artifact actually being applied correctly, or cited for a claim it does
    not support (e.g. a paper cited *backwards*)? Dual-substrate (Claude+OpenAI)
    via cite_check's callers, reconciled. Catches MISAPPLICATION.
    Enable with --judge. Without it, supports_claim = DEFERRED_TO_JUDGE.
Stubs (P2): url -> UNVERIFIED_NOT_CHECKED.

Grounding verdict:
  UNGROUNDED              no checkable artifact cited
  GROUNDED_VERIFIED       artifact resolves (and, if judged, SUPPORTS the claim)
  GROUNDED_REFUTED        artifact doesn't resolve (fabricated) OR, if judged,
                          resolves but does NOT support the claim (misapplied)
  UNVERIFIED_NOT_CHECKED  backend not built (P2) or network/backend error

Mapper (--map-claims): most concerns ground in a pack fact by DESCRIPTION (no #N
    token). A single-substrate mapper proposes which fact(s) the concern relies on,
    then it is verified in-pack. Mapping is extraction; the grounding judgment stays
    dual-substrate. Needs pack_text + ANTHROPIC_API_KEY.

Usage:
  verify_grounding.py --self-test            # P1 resolution (network, no keys)
  verify_grounding.py --judge-selftest       # P1.5 wiring (network, fake judge, no keys)
  verify_grounding.py --map-selftest         # mapper wiring (fake mapper, no keys)
  verify_grounding.py --in concerns.json [--judge] [--map-claims] [--out verdicts.json]
"""
import argparse, importlib.util, json, os, re, sys, urllib.parse, urllib.request, urllib.error

def _find_cite_check():
    """Locate the cite_check.py engine (the literature/Crossref backend reuses it).
    Robust across a git worktree, a parent clone, or a fresh checkout: honor an explicit
    CITE_CHECK_PY override, then try the repo-relative path, then the Loom shared-skill
    install (where the /cite-check skill actually lives — it is NOT vendored into this
    repo). Returns the first existing candidate, else the repo-relative path so the
    degraded-backend message stays informative."""
    env = os.environ.get("CITE_CHECK_PY")
    if env:
        return env
    here = os.path.dirname(os.path.abspath(__file__))
    loom = os.environ.get("LOOM_DIR", os.path.expanduser("~/projects/loom"))
    candidates = [
        os.path.join(here, "..", "..", "cite-check", "scripts", "cite_check.py"),
        os.path.join(loom, "skills", "shared", "cite-check", "scripts", "cite_check.py"),
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return candidates[0]


CITE_CHECK_PY = _find_cite_check()
CWE_API = "https://cwe-api.mitre.org/api/v1/cwe/weakness/{id}"
RFC_API = "https://datatracker.ietf.org/api/v1/doc/document/rfc{id}/?format=json"
HTTP_TIMEOUT = 30
_STOP = set("the a an of for and or to in on at by with from is are was were be as that this "
            "its their our your his her not no than then when which who whom whose into over "
            "claim claims study studies paper journal vol issue pp et al eds ed".split())


def _load_cite_check():
    try:
        spec = importlib.util.spec_from_file_location("cite_check", CITE_CHECK_PY)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m
    except Exception as e:  # pragma: no cover
        sys.stderr.write(f"[verify] could not load cite_check engine ({e}); literature backend degraded\n")
        return None


CC = _load_cite_check()


def _http_json(url):
    req = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "sparring-grounding-verifier/0.1"})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as r:
        return r.status, json.loads(r.read().decode("utf-8", "replace"))


# ---------------- artifact classifier ----------------
def classify(ref):
    s = (ref or "").strip()
    if not s:
        return "none"
    if re.search(r"\bCWE-\d+\b", s, re.I):
        return "cwe"
    if re.search(r"\bRFC[\s-]?\d+\b", s, re.I):
        return "rfc"
    if re.search(r"10\.\d{4,9}/\S+", s) or re.search(r"arxiv[:/ ]?\d{4}\.\d{4,5}", s, re.I):
        return "literature"
    if re.search(r"https?://", s):
        return "url"
    if re.search(r"[\w/]+\.\w{1,5}:\d+", s) or re.search(r"\b\w+\.(php|py|js|ts|go|java|rb|cpp|sql)\b", s):
        return "code"
    if re.search(r"(^|\s)(#\s?\d|§\s?\d|pack\b|item\s?\d|MSA\b)", s, re.I):
        return "pack"
    if re.search(r"[A-Z][a-z]+.*\b(19|20)\d{2}\b", s):
        return "literature"
    return "none"


# ---------------- literature backend (Crossref via cite_check) ----------------
def _cited_surnames(ref):
    head = re.split(r"\b(?:19|20)\d{2}\b", ref)[0]
    out = []
    for part in re.split(r"[,&]| and ", head):
        toks = re.findall(r"[A-Z][a-zA-Z\-]{2,}", part)
        if toks:
            out.append(toks[0].lower())
    return out


def _topic_terms(*texts):
    blob = " ".join(t or "" for t in texts).lower()
    return {w for w in re.findall(r"[a-z][a-z\-]{3,}", blob) if w not in _STOP}


def backend_literature(ref, concern_text):
    """Returns (grounding, evidence_str, judge_evidence)."""
    if CC is None or not hasattr(CC, "lookup_crossref_search"):
        return "UNVERIFIED_NOT_CHECKED", "cite_check engine unavailable", None
    cited_surnames = _cited_surnames(ref)
    ym = re.search(r"\b(19|20)\d{2}\b", ref)
    cited_year = int(ym.group(0)) if ym else None
    topic = _topic_terms(ref, concern_text)
    try:
        _, items = CC.lookup_crossref_search(ref)
    except Exception as e:
        return "UNVERIFIED_NOT_CHECKED", f"crossref error: {e}", None
    for it in items:
        cand_surnames = [(_a.split(",")[0].strip().lower()) for _a in (it.get("authors") or [])]
        surname_ok = bool(cited_surnames) and any(cs in cand_surnames for cs in cited_surnames)
        cand_text = f"{it.get('title') or ''} {it.get('container_title') or ''}".lower()
        topic_ok = (not topic) or any(w in cand_text for w in topic)
        if surname_ok and topic_ok:
            cy = it.get("year")
            yflag = "exact-ish" if (cited_year and cy and abs(int(cy) - cited_year) <= 1) \
                else f"area match (cited {cited_year}, found {cy})"
            ev = f"resolved [{yflag}]: {', '.join((it.get('authors') or [])[:2])} ({cy}) — {it.get('title')!r} [{it.get('doi')}]"
            judge_ev = f"{it.get('title')}. {it.get('abstract') or '(no abstract indexed)'}"
            return "GROUNDED_VERIFIED", ev, judge_ev
    return "GROUNDED_REFUTED", f"no Crossref record corroborates author+topic for {ref!r} (fabricated/unverifiable)", None


# ---------------- CWE backend (MITRE) ----------------
def backend_cwe(ref):
    """Returns (grounding, evidence_str, judge_evidence)."""
    m = re.search(r"CWE-(\d+)", ref, re.I)
    if not m:
        return "UNVERIFIED_NOT_CHECKED", "no CWE id parsed", None
    cid = m.group(1)
    try:
        _, data = _http_json(CWE_API.format(id=cid))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "GROUNDED_REFUTED", f"CWE-{cid} does not exist (MITRE 404)", None
        return "UNVERIFIED_NOT_CHECKED", f"MITRE http {e.code}", None
    except Exception as e:
        return "UNVERIFIED_NOT_CHECKED", f"MITRE error: {e}", None
    weaknesses = data.get("Weaknesses") or data.get("weaknesses") or []
    if weaknesses:
        w = weaknesses[0]
        name = w.get("Name") or "?"
        desc = " ".join(filter(None, [w.get("Description"), w.get("ExtendedDescription")]))
        return "GROUNDED_VERIFIED", f"CWE-{cid}: {name}", f"CWE-{cid} {name}. {desc}"
    return "GROUNDED_REFUTED", f"CWE-{cid} not found at MITRE", None


# ---------------- RFC / IETF backend (datatracker) ----------------
def backend_rfc(ref):
    """Returns (grounding, evidence_str, judge_evidence). Resolves against the IETF
    datatracker; an RFC is real iff the document exists and carries a title."""
    m = re.search(r"RFC[\s-]?(\d+)", ref, re.I)
    if not m:
        return "UNVERIFIED_NOT_CHECKED", "no RFC number parsed", None
    num = m.group(1)
    try:
        _, data = _http_json(RFC_API.format(id=num))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "GROUNDED_REFUTED", f"RFC {num} does not exist (IETF datatracker 404)", None
        return "UNVERIFIED_NOT_CHECKED", f"datatracker http {e.code}", None
    except Exception as e:
        return "UNVERIFIED_NOT_CHECKED", f"datatracker error: {e}", None
    title = data.get("title")
    if not title:
        return "GROUNDED_REFUTED", f"RFC {num} not found at IETF datatracker", None
    abstract = data.get("abstract") or "(no abstract indexed)"
    return "GROUNDED_VERIFIED", f"RFC {num}: {title}", f"RFC {num} {title}. {abstract}"


# ---------------- code/file backend (resolve against the working tree) ----------------
# No network, no keys: a path:line resolves against the repo; a bare symbol/flag is
# grepped. Catches a FABRICATED file/line (cited but not in the tree). Test-execution is
# deliberately NOT done (running an AI-named command is a security risk) — read + grep only.
_CODE_SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", "__pycache__", ".venv", ".cache"}
_CODE_TEXT_EXT = {".py", ".js", ".ts", ".tsx", ".jsx", ".php", ".go", ".java", ".rb", ".c", ".cc",
                  ".cpp", ".h", ".hpp", ".cs", ".rs", ".kt", ".swift", ".sh", ".sql", ".md", ".txt",
                  ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".html", ".css", ".scss"}


def _repo_root(c):
    return c.get("repo_root") or os.environ.get("VERIFY_REPO_ROOT") or os.getcwd()


def _safe_join(root, rel):
    """Resolve rel under root, refusing any path that escapes the repo root."""
    root = os.path.realpath(root)
    full = os.path.realpath(os.path.join(root, rel))
    if full == root or full.startswith(root + os.sep):
        return full
    return None


def _grep_repo(repo_root, needle):
    """Bounded substring grep across text files in the tree. Returns up to 5 (relpath,line,text)
    hits, or None if the root isn't a directory."""
    root = os.path.realpath(repo_root)
    if not os.path.isdir(root):
        return None
    out, scanned = [], 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _CODE_SKIP_DIRS]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext and ext not in _CODE_TEXT_EXT:
                continue
            fp = os.path.join(dirpath, fn)
            try:
                if os.path.getsize(fp) > 1_000_000:
                    continue
                for i, line in enumerate(open(fp, encoding="utf-8", errors="replace"), 1):
                    scanned += 1
                    if needle in line:
                        out.append((os.path.relpath(fp, root), i, line.strip()[:120]))
                        if len(out) >= 5:
                            return out
                    if scanned > 4_000_000:
                        return out
            except Exception:
                continue
    return out


def backend_code(ref, concern_text, repo_root):
    """Returns (grounding, evidence_str, judge_evidence)."""
    s = ref.strip()
    m = re.match(r"^(.+?):(\d+)(?:-(\d+))?$", s)
    if m:
        rel = m.group(1)
    elif "/" in s and re.search(r"\.\w{1,6}$", s) or re.match(r"^[\w.\-]+\.\w{1,6}$", s):
        rel = s            # bare file path (has an extension)
    else:
        rel = None         # a symbol / flag — fall through to grep
    if rel is not None:
        full = _safe_join(repo_root, rel)
        if full is None:
            return "UNVERIFIED_NOT_CHECKED", f"path {rel!r} escapes the repo root", None
        if not os.path.isfile(full):
            return "GROUNDED_REFUTED", f"{rel} not found in the repo (fabricated path)", None
        try:
            lines = open(full, encoding="utf-8", errors="replace").read().splitlines()
        except Exception as e:
            return "UNVERIFIED_NOT_CHECKED", f"could not read {rel}: {e}", None
        if not m:
            return "GROUNDED_VERIFIED", f"{rel} exists ({len(lines)} lines)", f"{rel} (full file, {len(lines)} lines)"
        l1 = int(m.group(2))
        l2 = int(m.group(3)) if m.group(3) else l1
        if l1 < 1 or l1 > len(lines):
            return "GROUNDED_REFUTED", f"{rel} has {len(lines)} lines; cited line {l1} does not exist", None
        cited = "\n".join(lines[l1 - 1:l2])
        ctx = "\n".join(lines[max(0, l1 - 3):min(len(lines), l2 + 2)])
        return "GROUNDED_VERIFIED", f"{rel}:{l1}: {cited.strip()[:120]}", f"{rel} lines {l1}-{l2}:\n{ctx}"
    hits = _grep_repo(repo_root, s)
    if hits is None:
        return "UNVERIFIED_NOT_CHECKED", "repo root not a directory; symbol search unavailable", None
    if hits:
        rp, ln, txt = hits[0]
        return "GROUNDED_VERIFIED", f"found {s!r} at {rp}:{ln}", f"{rp}:{ln}: {txt}"
    return "GROUNDED_REFUTED", f"symbol {s!r} not found anywhere in the repo (fabricated reference)", None


# ---------------- in-pack backend (resolve against the PROVIDED pack) ----------------
_FACT_TOKEN = re.compile(
    r"#\s?(\d{1,3})\b|§\s?(\d+(?:\.\d+)*)|\bpack\s+(?:fact\s+|#)?(\d{1,3})\b|\bfact\s+(\d{1,3})\b", re.I)


def _cited_pack_tokens(*texts):
    nums, secs = set(), set()
    for t in texts:
        for m in _FACT_TOKEN.finditer(t or ""):
            n = m.group(1) or m.group(3) or m.group(4)
            if n:
                nums.add(n)
            if m.group(2):
                secs.add(m.group(2))
    return nums, secs


def backend_pack(ref, concern_text, pack_text):
    """Resolve an in-pack artifact against the PROVIDED pack text.
    Existence (P1): is the cited fact #/section actually present in the pack? Support
    (P1.5, with --judge): does the pack back the claim? Needs the pack text; without it
    the concern is UNVERIFIED_NOT_CHECKED — the v2-run case, where the per-case packs
    were not persisted, so there is nothing to resolve against."""
    if not pack_text:
        return ("UNVERIFIED_NOT_CHECKED",
                "in-pack artifact but no pack text supplied (pack not persisted)", None)
    nums, secs = _cited_pack_tokens(ref, concern_text)
    if not nums and not secs:
        # cites the pack with no explicit fact-id — defer existence; judge support against the full pack
        return "GROUNDED_VERIFIED", "in-pack reference (no explicit fact-id; judged against full pack)", pack_text
    present, missing = [], []
    for n in sorted(nums, key=int):
        if re.search(rf"(^|\n)\s*{n}[\.\)]", pack_text) or re.search(rf"#\s?{n}\b", pack_text):
            present.append(f"#{n}")
        else:
            missing.append(f"#{n}")
    for s in sorted(secs):
        if re.search(rf"§\s?{re.escape(s)}\b", pack_text) or re.escape(s) in pack_text:
            present.append(f"§{s}")
        else:
            missing.append(f"§{s}")
    if missing and not present:
        return ("GROUNDED_REFUTED",
                f"cited pack element(s) {', '.join(missing)} not found in the pack (fabricated reference)", None)
    ev = f"resolves in pack: {', '.join(present)}" + (f"; not found: {', '.join(missing)}" if missing else "")
    return "GROUNDED_VERIFIED", ev, pack_text


# ---------------- claim->fact mapper (reach prose-grounded concerns) ----------------
# A prose concern grounds itself in a pack fact by DESCRIPTION, with no #N token. The
# mapper (single-substrate, cheap) proposes which fact(s) it relies on; the existing
# dual-substrate judge then confirms SUPPORT. Mapping is extraction; the grounding
# JUDGMENT stays two-vendor.
_MAPPER_SYS = (
    "You map a reviewer's concern to the numbered fact(s) in a decision pack it relies on. "
    "Reply ONLY compact JSON: {\"facts\": [<int>...], \"reason\": \"<=15 words\"}. "
    "facts = the pack fact numbers the concern's claim is grounded in or refers to; "
    "return [] if the concern is grounded outside the pack or in nothing checkable.")


def _real_mapper(concern_text, pack_text):
    user = (f"DECISION PACK:\n{pack_text}\n\nCONCERN:\n{concern_text}\n\n"
            "Which pack fact number(s) does this concern rely on?")
    j = CC.extract_json(CC.call_anthropic(_MAPPER_SYS, user)) or {}
    facts = [str(n) for n in (j.get("facts") or []) if str(n).strip().isdigit()]
    return facts, (j.get("reason") or "")


# ---------------- P1.5 supports-claim judge (dual-substrate) ----------------
_JUDGE_SYS = (
    "You assess whether a cited source SUPPORTS a specific claim made in a review. "
    "Reply ONLY compact JSON: {\"verdict\": \"SUPPORTS|REFUTES|UNRELATED|INSUFFICIENT\", \"reason\": \"<=20 words\"}. "
    "REFUTES = the source argues the opposite of, or contradicts, the claim (a misapplication). "
    "UNRELATED = the source is about something else. INSUFFICIENT = not enough source content to tell.")


def _reconcile(a, b):
    if a == b:
        return a
    s = {a, b}
    if "REFUTES" in s and "SUPPORTS" in s:
        return "DISPUTED"
    if "REFUTES" in s:
        return "REFUTES"            # one refutes, other unrelated/insufficient -> misapplication
    if "UNRELATED" in s and "SUPPORTS" in s:
        return "DISPUTED"
    if "SUPPORTS" in s:             # SUPPORTS + INSUFFICIENT -> lean supports
        return "SUPPORTS"
    if "UNRELATED" in s:
        return "UNRELATED"
    return "INSUFFICIENT"


def _real_judge(claim, evidence_text):
    """Dual-substrate (Claude + OpenAI) via cite_check's callers. Requires API keys."""
    user = f"CLAIM (from a review):\n{claim}\n\nCITED SOURCE CONTENT:\n{evidence_text}"
    out = {}
    for label, fn in (("anthropic", CC.call_anthropic), ("openai", CC.call_openai)):
        txt = fn(_JUDGE_SYS, user)
        j = CC.extract_json(txt) or {}
        out[label] = (j.get("verdict") or "INSUFFICIENT").upper()
    return {"verdict": _reconcile(out["anthropic"], out["openai"]),
            "anthropic": out["anthropic"], "openai": out["openai"]}


# ---------------- dispatcher ----------------
def verify_concern(c, judge=False, map_claims=False):
    """judge / map_claims: False=off | True=real (needs keys) | callable=injected (tests).
    map_claims: for a prose concern with no explicit artifact, ask which pack fact(s) it
    relies on, then verify those as in-pack. Needs pack_text; no-op without it."""
    ref = (c.get("artifact_ref") or "").strip()
    text = c.get("concern_text") or ""
    pack_text = c.get("pack_text") or ""
    atype = c.get("artifact_type") or classify(ref)
    mapped = None
    if atype == "none" and pack_text and map_claims:
        mfn = map_claims if callable(map_claims) else _real_mapper
        facts, why = mfn(text, pack_text)
        if facts:
            ref = " ".join(f"#{n}" for n in facts)
            atype = "pack"
            mapped = f"mapped to {ref} ({why})"
    judge_ev = None
    if atype == "none":
        grounding, backend, ev = "UNGROUNDED", "none", "no checkable artifact cited"
    elif atype == "literature":
        grounding, ev, judge_ev = backend_literature(ref, text); backend = "crossref"
    elif atype == "cwe":
        grounding, ev, judge_ev = backend_cwe(ref); backend = "mitre-cwe"
    elif atype == "rfc":
        grounding, ev, judge_ev = backend_rfc(ref); backend = "ietf-datatracker"
    elif atype == "code":
        grounding, ev, judge_ev = backend_code(ref, text, _repo_root(c)); backend = "repo"
    elif atype == "pack":
        grounding, ev, judge_ev = backend_pack(ref, text, pack_text); backend = "in-pack"
    else:
        grounding, backend, ev = "UNVERIFIED_NOT_CHECKED", f"{atype}-backend (P2)", "backend not built (P2)"

    supports = "DEFERRED_TO_JUDGE"
    if grounding == "GROUNDED_VERIFIED" and judge and judge_ev:
        jfn = judge if callable(judge) else _real_judge
        jr = jfn(text, judge_ev)
        supports = jr["verdict"]
        if supports in ("REFUTES", "UNRELATED"):
            grounding = "GROUNDED_REFUTED"
            ev = f"resolves but judge={supports} — artifact does not support the claim (misapplied). {ev}"
    if mapped:
        backend = f"{backend}+mapper"
        ev = f"[{mapped}] {ev}"
    return {
        "concern_id": c.get("id"),
        "artifact_ref": ref,
        "artifact_type": atype,
        "backend": backend,
        "grounding": grounding,
        "supports_claim": supports,
        "evidence": ev,
    }


# ---------------- self-tests ----------------
SELF_TESTS = [
    ("fabricated citation -> REFUTED",
     {"id": "t1", "artifact_ref": "Henderson & Liu, 2021, Journal of Visual Ergonomics 14(3)",
      "concern_text": "dark mode reduces eye strain by 40% during extended reading"}, "GROUNDED_REFUTED"),
    ("real citation -> VERIFIED",
     {"id": "t2", "artifact_ref": "Sweller 1998, cognitive load theory",
      "concern_text": "simultaneous novel elements overwhelm working memory"}, "GROUNDED_VERIFIED"),
    ("real CWE -> VERIFIED",
     {"id": "t3", "artifact_ref": "CWE-640", "concern_text": "reset token not single-use"}, "GROUNDED_VERIFIED"),
    ("nonexistent CWE -> REFUTED",
     {"id": "t4", "artifact_ref": "CWE-9999999", "concern_text": "x"}, "GROUNDED_REFUTED"),
    ("real RFC -> VERIFIED",
     {"id": "t7", "artifact_ref": "RFC 8725", "concern_text": "pin the JWT algorithm; do not trust the alg header"},
     "GROUNDED_VERIFIED"),
    ("nonexistent RFC -> REFUTED",
     {"id": "t8", "artifact_ref": "RFC 999999", "concern_text": "x"}, "GROUNDED_REFUTED"),
    ("no artifact -> UNGROUNDED",
     {"id": "t5", "artifact_ref": "", "concern_text": "this just smells risky"}, "UNGROUNDED"),
    ("in-pack fact present -> VERIFIED",
     {"id": "t9", "artifact_ref": "#3", "concern_text": "inverts pack #3",
      "pack_text": "1. Cohort.\n2. Employer survey.\n3. Cognitive load theory (Sweller 1998).\n"},
     "GROUNDED_VERIFIED"),
    ("in-pack fact absent -> REFUTED (fabricated pack ref)",
     {"id": "t10", "artifact_ref": "#9", "concern_text": "see pack #9",
      "pack_text": "1. Cohort.\n2. Survey.\n3. CLT.\n"}, "GROUNDED_REFUTED"),
    ("in-pack but pack not persisted -> not-checked",
     {"id": "t6", "artifact_ref": "pack #7 (MSA §9.3)", "concern_text": "breaches the 15% cap", "pack_text": ""},
     "UNVERIFIED_NOT_CHECKED"),
]


def _code_self_tests():
    """code-backend checks need a real file, so they build a temp repo (no network)."""
    import tempfile
    cases = []
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "stubs.php"), "w") as fh:
            fh.write("<?php\n$rt_is_admin = fn() => true; // auth=open|none\nreturn $rt_is_admin;\n")
        def vc(ref, ct="x"):
            return verify_concern({"id": "c", "artifact_type": "code", "artifact_ref": ref,
                                   "concern_text": ct, "repo_root": d})
        cases = [
            ("code path:line present -> VERIFIED", vc("stubs.php:2")["grounding"] == "GROUNDED_VERIFIED"),
            ("code file present (no line) -> VERIFIED", vc("stubs.php")["grounding"] == "GROUNDED_VERIFIED"),
            ("code missing file -> REFUTED", vc("nope.php:1")["grounding"] == "GROUNDED_REFUTED"),
            ("code line past EOF -> REFUTED", vc("stubs.php:999")["grounding"] == "GROUNDED_REFUTED"),
            ("code path traversal -> not-checked", vc("../../../etc/passwd:1")["grounding"] == "UNVERIFIED_NOT_CHECKED"),
            ("code symbol grep hit -> VERIFIED", vc("rt_is_admin")["grounding"] == "GROUNDED_VERIFIED"),
            ("code symbol absent -> REFUTED", vc("nonexistent_symbol_xyz")["grounding"] == "GROUNDED_REFUTED"),
        ]
    return cases


def run_self_test():
    ok = True
    for label, concern, expected in SELF_TESTS:
        got = verify_concern(concern)
        passed = got["grounding"] == expected
        ok = ok and passed
        print(f"[{'PASS' if passed else 'FAIL'}] {label}: got {got['grounding']} (expected {expected})")
    for label, passed in _code_self_tests():
        ok = ok and passed
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
    print(f"\n{'ALL PASS' if ok else 'SOME FAILED'}")
    return 0 if ok else 1


def _fake_judge(verdict):
    return lambda claim, ev: {"verdict": verdict, "anthropic": verdict, "openai": verdict}


def run_judge_wiring_test():
    """P1.5 integration, offline (network for resolution, fake judge instead of keys).
    A resolved artifact + judge=SUPPORTS stays VERIFIED; + judge=REFUTES flips to REFUTED (misapplication)."""
    base = {"id": "j", "artifact_ref": "CWE-640", "concern_text": "reset token not single-use"}
    sup = verify_concern(dict(base), judge=_fake_judge("SUPPORTS"))
    ref = verify_concern(dict(base), judge=_fake_judge("REFUTES"))
    unr = verify_concern(dict(base), judge=_fake_judge("UNRELATED"))
    checks = [
        ("resolved + SUPPORTS stays VERIFIED", sup["grounding"] == "GROUNDED_VERIFIED" and sup["supports_claim"] == "SUPPORTS"),
        ("resolved + REFUTES flips to REFUTED (misapplication)", ref["grounding"] == "GROUNDED_REFUTED" and ref["supports_claim"] == "REFUTES"),
        ("resolved + UNRELATED flips to REFUTED", unr["grounding"] == "GROUNDED_REFUTED"),
        ("reconcile SUPPORTS/REFUTES -> DISPUTED", _reconcile("SUPPORTS", "REFUTES") == "DISPUTED"),
        ("reconcile REFUTES/INSUFFICIENT -> REFUTES", _reconcile("REFUTES", "INSUFFICIENT") == "REFUTES"),
    ]
    ok = all(p for _, p in checks)
    for label, p in checks:
        print(f"[{'PASS' if p else 'FAIL'}] {label}")
    print(f"\n{'ALL PASS' if ok else 'SOME FAILED'} (offline wiring; live dual-substrate needs ANTHROPIC_API_KEY+OPENAI_API_KEY)")
    return 0 if ok else 1


def run_map_wiring_test():
    """claim->fact mapper integration, offline (fake mapper instead of keys).
    A prose concern (no token) + mapper->[3] routes to in-pack existence (fact 3 present)
    -> VERIFIED; mapper->[] leaves it UNGROUNDED."""
    pack = "1. Cohort.\n2. Survey.\n3. Cognitive load theory (Sweller 1998).\n"
    base = {"id": "m", "artifact_ref": "",
            "concern_text": "the recommendation inverts cognitive load theory", "pack_text": pack}
    hit = verify_concern(dict(base), map_claims=lambda t, p: (["3"], "CLT is pack fact 3"))
    miss = verify_concern(dict(base), map_claims=lambda t, p: ([], "external"))
    none_pack = verify_concern({"id": "m2", "artifact_ref": "", "concern_text": "vibes"},
                               map_claims=lambda t, p: (["3"], "x"))  # no pack_text -> mapper skipped
    checks = [
        ("mapper->[3] routes prose concern to in-pack VERIFIED",
         hit["grounding"] == "GROUNDED_VERIFIED" and "mapper" in hit["backend"]),
        ("mapped ref is #3", hit["artifact_ref"] == "#3"),
        ("mapper->[] leaves concern UNGROUNDED", miss["grounding"] == "UNGROUNDED"),
        ("no pack_text -> mapper is a no-op (UNGROUNDED)", none_pack["grounding"] == "UNGROUNDED"),
    ]
    ok = all(p for _, p in checks)
    for label, p in checks:
        print(f"[{'PASS' if p else 'FAIL'}] {label}")
    print(f"\n{'ALL PASS' if ok else 'SOME FAILED'} (offline wiring; live mapper needs ANTHROPIC_API_KEY)")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Grounding verifier P1 + P1.5.")
    ap.add_argument("--self-test", action="store_true", help="P1 resolution self-test")
    ap.add_argument("--judge-selftest", action="store_true", help="P1.5 integration wiring test (fake judge, no keys)")
    ap.add_argument("--map-selftest", action="store_true", help="claim->fact mapper wiring test (fake mapper, no keys)")
    ap.add_argument("--judge", action="store_true", help="enable live P1.5 supports-claim judge (needs API keys)")
    ap.add_argument("--map-claims", action="store_true",
                    help="map prose concerns (no explicit artifact) to the pack fact(s) they rely on, "
                         "then verify in-pack (needs pack_text + ANTHROPIC_API_KEY)")
    ap.add_argument("--in", dest="infile", help="JSON array of concerns")
    ap.add_argument("--out", dest="outfile")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(run_self_test())
    if args.judge_selftest:
        sys.exit(run_judge_wiring_test())
    if args.map_selftest:
        sys.exit(run_map_wiring_test())
    judge = map_claims = False
    if args.judge:
        if CC is None:
            sys.exit("[verify] --judge needs the cite_check engine; not loadable.")
        CC.get_key("ANTHROPIC_API_KEY"); CC.get_key("OPENAI_API_KEY")  # die early if missing
        judge = True
    if args.map_claims:
        if CC is None:
            sys.exit("[verify] --map-claims needs the cite_check engine; not loadable.")
        CC.get_key("ANTHROPIC_API_KEY")  # die early if missing
        map_claims = True
    raw = open(args.infile).read() if args.infile else sys.stdin.read()
    concerns = json.loads(raw)
    verdicts = [verify_concern(c, judge=judge, map_claims=map_claims) for c in concerns]
    out = json.dumps(verdicts, indent=2)
    (open(args.outfile, "w").write(out + "\n") if args.outfile else print(out))


if __name__ == "__main__":
    main()
