# Sourcing a corpus of documented misses

**Status: reconnaissance complete. Two viable sources found, one blocked on a free
credential, one usable immediately in a different domain. Decision required.**
Serves the unrun experiment named in
[`seeded-holdout-result.md`](./seeded-holdout-result.md) §4.

---

## What the experiment needs

Seeds satisfying three conditions. The hold-out design met only the first two:

1. **known-material** — something establishes it mattered
2. **outside the scoring key** — so it must surface as off-key or not at all
3. **outside the key entirely and outside the model ecosystem** — the one no available
   source supplied without authoring (circular) or an expert (unavailable)

The target class: **cases where the decisive consideration is on record precisely because
someone failed to raise it.**

## Checked and rejected

| source | why not |
|---|---|
| **NASA Lessons Learned (LLIS)** | Best structural fit on paper — records are literally *Driving Event* + *Lesson Learned*. But `llis.nasa.gov` serves a 1.7 KB single-page shell with no server-rendered content, and the data.gov entry links only that HTML page. No API, no bulk file. |
| **NTSB CAROL** | Public query endpoint rejected the documented request shape. Recoverable with more effort, but the fit is weaker: a probable-cause finding is a *causal factor*, not a consideration a decision-maker failed to weigh. |
| **CourtListener bulk S3** | The bucket **is** publicly listable without credentials (506 objects), but the opinion-text table is not in it — the largest object is 0.01 GB of oral-argument metadata. Text lives behind the authenticated endpoint. |

## Viable — option A: appellate opinions (CourtListener API)

**The best fit, blocked on a free account.**

```
query   "failed to consider", opinions, newest first
hits    57,215
recent  Moore v. Moore · State v. Davis (Ohio App.)  2026-08-27
        People v. Hazlett (Cal. Supreme)             2026-08-27
```

- **The structure is exactly right.** The appellate court states the facts, and states what
  the court below failed to consider. The lower court is a decision-maker who missed
  something; the appellate court is independent, human, and authoritative gold.
- **Contamination is solved, not mitigated.** Opinions filed days ago post-date any model's
  training. This is a materially stronger position than the MEE corpus, whose every answer
  key is 2016–2020 ([`corpus-recon.md`](./corpus-recon.md) §3).
- **It transfers.** Same domain as the existing corpus, so the generator prompt, the
  matching pass, the blind judge and the scoring machinery all work unchanged.
- **Blocked by:** search is open, but `/api/rest/v4/opinions/{id}/` returns **401**. Text
  needs a free API token, which means an account. The public case page returns 0 bytes and
  `download_url` points at Westlaw.

**This is a two-minute signup, and it is Bart's to make — creating an account on his behalf
is not mine to do.**

## Viable — option B: public incident post-mortems

**Usable right now, no credentials, different domain.**

- 241 curated links (Cloudflare, Datadog, Facebook, AWS and others), publicly fetchable —
  verified end-to-end on the 18 November 2025 Cloudflare outage (19 KB of clean text).
- **The missed consideration is stated in the document.** That post-mortem says outright:
  *"there were assumptions made in the past, that the list of columns returned by a query
  like this would only include the default database"* — a decisive factor, on record
  because it was overlooked.
- Recent entries sit at or past training cutoffs.

**Costs.** It is an engineering domain, not law: the generator prompt, the notion of a
"key", and the whole answer-key apparatus would have to be rebuilt. And each post-mortem
needs splitting into *situation given to the generator* and *what was missed* — extraction
rather than invention, and checkable against the document, but still an editorial hand in
the loop that option A does not require.

## Recommendation

**Option A, and ask Bart for a CourtListener token.** The domain fit means the experiment
reuses everything already built and validated in this study rather than starting a second
apparatus; the recency means contamination stops being a caveat that has to travel with
every number. Option B is the fallback if the token is declined, and it is a real fallback
rather than a consolation — but it costs a rebuild.

Either way the sourcing problem is **solved in principle**: corpora of documented misses
exist, are public, and are large. This was the open question, and the answer is yes.
