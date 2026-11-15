#!/usr/bin/env python3
"""Pull candidate appellate opinions from CourtListener into a local cache.

Target class (design-note.md §2): opinions where the appellate court HOLDS that the
court below erred by failing to consider something. The bare phrase "failed to
consider" is not that class -- it appears overwhelmingly in claims the appellate court
REJECTS (verified on the first sampled opinion, Moore v. Moore, Ohio App. 2026-08-27,
where the court answers the argument by pointing at where the trial court did consider
it). So the search uses holding-voice phrases, and a model screen (screen_cases.py)
still has to confirm agreement case by case.

Free Law Project is a non-profit and the search endpoint is rate-limited to 5/min
(measured 2026-08-29). This script throttles hard, caches every fetch to corpus/raw/,
and is resumable: re-running skips anything already on disk. The corpus is pulled ONCE.

Filed-after defaults to 2026-06-01, which is past the training cutoff of both vendors
under test -- the contamination argument in seed-corpus-recon.md depends on it.

Usage:
  ./fetch_opinions.py                       # search + fetch, default queries
  ./fetch_opinions.py --search-only         # build the candidate list, fetch nothing
  ./fetch_opinions.py --limit 60
"""
import argparse, json, os, sys, time, urllib.parse

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(HERE, "..", "corpus"))
RAW = os.path.join(CORPUS, "raw")
API = "https://www.courtlistener.com/api/rest/v4"

# Holding-voice phrases. A court writing "erred in failing to consider" is stating its
# own conclusion; a court writing "failed to consider" is usually reciting an appellant's
# argument it is about to reject. Both forms of the phrase are included because courts
# split roughly evenly between "in" and "by".
QUERIES = [
    '"erred in failing to consider"',
    '"erred by failing to consider"',
    '"erred in not considering"',
    '"failed to consider" "we reverse"',
    '"failed to consider" "we vacate"',
    # Added 2026-08-29 to widen recall WITHIN the same post-cutoff window rather than by
    # reaching further back in time. The contamination argument depends on filed_after
    # staying past both vendors' training cutoffs, so the date filter is not the knob to
    # turn; the phrasing is. Courts split across "consider" / "address" / "make findings",
    # and across reverse / vacate / remand.
    '"erred in failing to address"',
    '"erred by failing to address"',
    '"failed to consider" "we remand"',
    '"abused its discretion by failing to consider"',
    '"abused its discretion in failing to consider"',
    '"failed to make the required findings"',
    '"without considering whether" "we reverse"',
    '"neglected to consider"',
]

# THREE limits, discovered one at a time by hitting each in turn (2026-08-29). The
# DAILY one is the binding constraint and the one that matters for planning:
#
#   search    5 / minute
#   opinions  50 / hour
#   ACCOUNT   125 / DAY, shared across BOTH endpoints
#
# The daily cap is the planning constraint and it is small: a single 122-opinion pull plus
# its searches very nearly exhausts a day's budget. Two earlier notes in this file called
# 50/hour "the binding one" -- that was wrong, and it was wrong because each limit was
# assumed to be the last one after it was found. Budget a corpus pull in DAYS, not hours,
# and search deliberately: every exploratory query spends opinions you cannot fetch.
#
# On exhaustion the API reports the wait honestly ("Expected available in 62537 seconds"),
# and the backoff below will faithfully sleep ~17 hours. That is correct behaviour and
# almost never what you want -- check the message before leaving a pull running.
SEARCH_GAP = 13.0
FETCH_GAP = 75.0


QUOTA_WALL = 900.0   # a 429 asking for longer than this is a spent quota, not a throttle


class QuotaExhausted(RuntimeError):
    """The daily cap is gone. Stop cleanly rather than sleeping until it resets.

    Sleeping is what the API asks for and it is the wrong thing to do: the process stays
    alive, prints nothing further, and looks identical to slow progress. Everything
    already fetched is cached, so exiting loses nothing and re-running resumes.
    """

    def __init__(self, detail, seconds):
        super().__init__(detail)
        self.seconds = seconds


def token():
    # DEPOSIT COPY: the working-repository original read a hard-coded, machine-specific
    # .env path here. The token now comes from COURTLISTENER_TOKEN in the environment,
    # or from a KEY=VALUE file named by SPARRING_ENV_FILE.
    if os.environ.get("COURTLISTENER_TOKEN"):
        return os.environ["COURTLISTENER_TOKEN"]
    path = os.environ.get("SPARRING_ENV_FILE")
    if path:
        for line in open(path):
            line = line.strip()
            if line.startswith("COURTLISTENER_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("COURTLISTENER_TOKEN not set (environment or SPARRING_ENV_FILE)")


def get(session, url, params=None, gap=FETCH_GAP, tries=5):
    """GET with throttle + backoff on 429. Returns parsed JSON."""
    delay = gap
    for attempt in range(tries):
        time.sleep(delay)
        r = session.get(url, params=params, timeout=120)
        if r.status_code == 200:
            return r.json()
        if r.status_code == 429:
            # CourtListener tells us how long to wait, and it is telling the truth -- but
            # a per-minute throttle and an exhausted DAILY quota both arrive as a 429 with
            # a number attached. Sleeping through the first is right; sleeping through the
            # second means a process sitting idle for most of a day while looking healthy.
            wait, msg = 20.0, ""
            try:
                msg = r.json().get("detail", "")
                for tok in msg.replace(":", " ").split():
                    if tok.isdigit():
                        wait = float(tok) + 3
                        break
            except Exception:
                pass
            if wait > QUOTA_WALL:
                raise QuotaExhausted(msg or f"throttled for {wait:.0f}s", wait)
            print(f"    throttled; sleeping {wait:.0f}s", flush=True)
            delay = wait
            continue
        if r.status_code >= 500:
            # CourtListener returns a transient 502 under load; back off and retry.
            delay = min(gap * (attempt + 2), 60.0)
            print(f"    {r.status_code} from server; retrying in {delay:.0f}s", flush=True)
            continue
        raise RuntimeError(f"{r.status_code}: {r.text[:200]}")
    raise RuntimeError(f"exhausted retries on {url}")


def search(session, q, filed_after, max_pages):
    """One query, paginated, newest first. Returns cluster stubs."""
    out, url = [], f"{API}/search/"
    params = {"q": q, "type": "o", "order_by": "dateFiled desc",
              "filed_after": filed_after}
    for page in range(max_pages):
        d = get(session, url, params=params, gap=SEARCH_GAP)
        got = d.get("results", [])
        for r in got:
            out.append({
                "cluster_id": r.get("cluster_id"),
                "case_name": r.get("caseName"),
                "date_filed": r.get("dateFiled"),
                "court": r.get("court"),
                "docket_number": r.get("docketNumber"),
                "url": "https://www.courtlistener.com" + (r.get("absolute_url") or ""),
                "found_by": q,
            })
        nxt = d.get("next")
        print(f"    page {page+1}: +{len(got)}  (total for this query: {len(out)})",
              flush=True)
        if not nxt or not got:
            break
        url, params = nxt, None
    return out


def fetch_text(session, cluster_id):
    """Full opinion text for a cluster. Concatenates sub-opinions in order."""
    d = get(session, f"{API}/opinions/", params={"cluster": cluster_id})
    parts = []
    for r in d.get("results", []):
        txt = r.get("plain_text") or ""
        if not txt:
            html = r.get("html_with_citations") or r.get("html") or ""
            if html:
                import re
                txt = re.sub(r"<[^>]+>", " ", html)
                txt = re.sub(r"&#\d+;|&[a-z]+;", " ", txt)
        if txt.strip():
            parts.append({"opinion_id": r.get("id"), "type": r.get("type"),
                          "text": txt})
    return parts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--filed-after", default="2026-06-01",
                    help="past both vendors' training cutoffs (contamination argument)")
    ap.add_argument("--limit", type=int, default=80, help="max opinions to FETCH")
    ap.add_argument("--max-pages", type=int, default=3, help="pages per query")
    ap.add_argument("--search-only", action="store_true")
    a = ap.parse_args()

    os.makedirs(RAW, exist_ok=True)
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token()}",
                      "User-Agent": "SPARRING research pilot"})

    cand_path = os.path.join(CORPUS, "candidates.json")
    if os.path.exists(cand_path):
        cands = json.load(open(cand_path))["candidates"]
        print(f"reusing {len(cands)} candidates from {cand_path} "
              f"(delete it to re-search)\n")
    else:
        print(f"searching CourtListener, filed_after={a.filed_after}, "
              f"{SEARCH_GAP:.0f}s between calls\n")
        seen, cands = set(), []
        for q in QUERIES:
            print(f"  {q}", flush=True)
            for r in search(s, q, a.filed_after, a.max_pages):
                cid = r["cluster_id"]
                if cid and cid not in seen:
                    seen.add(cid)
                    cands.append(r)
        cands.sort(key=lambda r: r["date_filed"] or "", reverse=True)
        json.dump({"filed_after": a.filed_after, "queries": QUERIES,
                   "n": len(cands), "candidates": cands},
                  open(cand_path, "w"), indent=2)
        print(f"\n{len(cands)} distinct clusters -> {cand_path}")

    by_court = {}
    for c in cands:
        by_court[c["court"]] = by_court.get(c["court"], 0) + 1
    print("\ntop courts:")
    for court, n in sorted(by_court.items(), key=lambda x: -x[1])[:8]:
        print(f"  {n:>3}  {court}")

    if a.search_only:
        return

    todo = [c for c in cands
            if not os.path.exists(os.path.join(RAW, f"{c['cluster_id']}.json"))][:a.limit]
    print(f"\nfetching text for {len(todo)} of {len(cands)} "
          f"({len(cands)-len(todo)} already cached or over --limit)\n")
    for i, c in enumerate(todo, 1):
        cid = c["cluster_id"]
        try:
            parts = fetch_text(s, cid)
        except QuotaExhausted:
            # MUST propagate. The broad except below exists so one malformed opinion
            # cannot kill a long pull -- but it swallowed quota exhaustion too, so the
            # loop burned through every remaining candidate printing ERROR and then
            # announced "next: ./screen_cases.py" and exited 0. A failed pull that
            # reports success is worse than one that crashes.
            raise
        except Exception as e:  # noqa: BLE001 - one bad opinion must not kill the pull
            print(f"  {i:>3}/{len(todo)}  {cid}  ERROR {e}")
            continue
        chars = sum(len(p["text"]) for p in parts)
        json.dump({**c, "opinions": parts, "chars": chars},
                  open(os.path.join(RAW, f"{cid}.json"), "w"), indent=2)
        print(f"  {i:>3}/{len(todo)}  {cid}  {chars:>7} chars  "
              f"{(c['case_name'] or '')[:52]}", flush=True)

    cached = [f for f in os.listdir(RAW) if f.endswith(".json")]
    print(f"\ncached: {len(cached)} opinions in {RAW}")
    print("next: ./screen_cases.py")


if __name__ == "__main__":
    try:
        main()
    except QuotaExhausted as e:
        hrs = e.seconds / 3600.0
        cached = len([f for f in os.listdir(RAW) if f.endswith(".json")]) \
            if os.path.isdir(RAW) else 0
        print(f"\nSTOPPED: CourtListener quota exhausted.\n  {e}\n"
              f"  resets in ~{hrs:.1f}h\n"
              f"  {cached} opinions cached; re-run this script then to resume.",
              file=sys.stderr)
        sys.exit(75)   # EX_TEMPFAIL -- retry later, nothing is wrong with the request
