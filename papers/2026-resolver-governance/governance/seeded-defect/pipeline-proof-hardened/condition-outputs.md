# Hardened mini-proof — raw condition outputs (verbatim)

> The 12 reviewer outputs (3 cases × {B neutral, S-Gen, S-Chal, T placebo}), same-vendor (Claude). Saved verbatim as the source for Phase-0 per-concern coding (`phase0-results.md`). For the v2 measure, the **S condition = S-Gen ∪ S-Chal** (the two-agent ceremony's combined concern set).

## H1 — Sweller/CLT cited backwards (anchor defect: the citation supports the *opposite* of CLT)

### H1-B (neutral)
1. CLT cited backwards (#3) — the central error; Sweller says simultaneous novel elements overwhelm working memory, arguing against parallel. 2. Population is worst-case for parallel load (~60% career-changers, ~25% ESL, #1). 3. #7 (transfer: 2nd language after fluency ~30% faster) contradicts and is ignored. 4. Employer demand (#2) is "by graduation," misapplied to week-1 timing. 5. Andragogy (#4) cuts against (early concrete competence). 6. Completion risk unaddressed (#5 pilot 58% vs 71%, confounded but directionally aligned). 7. Cost "modest/justified" is editorialized (#6). Bottom line: revise (flip to Python-first).

### H1-S-Gen (pack-grounded)
1. #2 partial support, overstated (by-graduation, not week-1). 2. #3 Sweller directly contradicts — "processing two notations simultaneously builds flexible schemas" inverts the cited theory; most serious flaw. 3. #5 pilot undercuts (58% vs 71%, confounded). 4. #7 transfer favors sequential. 5. #4 andragogy undercuts. 6. #1 cohort (ESL/career-changers) most exposed to #3 load risk. 7. #6 "modest" is a weak value claim; sequencing gets the same marketability via #7. Bottom line: revise (Python-first).

### H1-S-Chal (learning-science evidence base)
1. Inverts CLT (#3, Sweller 1998) — Sweller, van Merriënboer & Paas (1998) center element interactivity / intrinsic load and prescribe *reducing* simultaneous novel demands (worked-example, split-attention effects); the load-bearing error. 2. "Productive struggle" miscited — desirable difficulties (Bjork) / expertise-reversal effect (Kalyuga, Ayres, Chandler & Sweller 2003) help only learners with existing schemas; for novices the same difficulty is extraneous load. 3. #7 transfer favors sequential, omitted from rationale. 4. #2 misread as a week-1 mandate. 5. #5 pilot aligns with theory despite confound. 6. #1 ESL compounds element interactivity. 7. #4 Knowles cuts against, ignored. 8. #6 cost spent on the disfavored arm. Bottom line: revise.

### H1-T (placebo)
1. Misreads its own headline source — CLT (#3) says simultaneous novel elements overwhelm; argues against parallel; "can't build flexible schemas out of two things you don't have one of." 2. "You ran the experiment and it lost" (#5, 58% vs 71%; confound is being used as license to ignore a 13-point drop). 3. Population worst-case for parallel load (#1). 4. #2 is graduation-not-week-1; #7 points the other way. 5. Andragogy (#4) cuts against. 6. Cost framing backwards — pays more per graduate if completion drops. 7. Falsifiable test: re-pilot with confound removed + completion floor. Bottom line: Python-first then JavaScript.

## H2 — schedule breaches the buried 15% MSA cap (anchor defect: pack #7)

### H2-B (neutral)
1. Hard contradiction with the 15% MSA cap (#7) — 25/50/100% bands are unpayable; auto-issue (#8) will breach or silently truncate; blocks ship. 2. "Up to 100%" headline (#9) misleading / legal-marketing risk vs §9.3. 3. Trigger at target not below — worst month 99.93% (#5) already in band-1; recurring payout vs margin (#6)/ACV (#4) unreconciled. 4. Buyer-preference (#3) over-weighted (3rd of 8). 5. Resolution path unstated (renegotiate §9.3 or cap schedule at 15%). Bottom line: revise.

### H2-S-Gen (pack-grounded)
1. Threshold design beats benchmark (supported, #1/#2/#3). 2. CRITICAL — schedule collides with #7 cap; 25/50/100% bands arithmetically unreachable, collapse to 15%; ladder cosmetic. 3. "100%" headline (#9) vs #7 = deceptive-marketing risk; load-bearing failure. 4. Auto-issue (#8) fine but doesn't rescue. 5. Financials trivially safe (15% cap ≈ $6,300 on $42k #4 vs ~$28.5k margin #6) — arguably over-conservative, but #7 says cap non-negotiable. Bottom line: revise (align to §9.3, drop "100%").

### H2-S-Chal (contract/finance evidence base)
1. "100%" headline undeliverable — §9.3 (#7) caps at 15%; overstates ceiling ~6.7×; written misrepresentation. 2. Three of four tiers are dead numbers (25/50/100 all > 15% cap); only 10% and 15% reachable. 3. "Matches/beats hyperscalers" false where it matters — after cap, Meridian pays 15% in the severe-outage region where hyperscalers pay 25–100% (#2); worse, not better. 4. The 100% tier would breach gross margin (#6) absent the cap (refunds 1.47× profit). 5. Auto-issue (#8) enforcement seam — pays per schedule (breach) or silently clamps (contradicts headline). 6. Justification leans on mid-ranked #3 (3rd of 8). 7. Cap-stacking basis unspecified (per-incident vs monthly). Bottom line: publish tiers within 15% or renegotiate §9.3; drop "100%."

### H2-T (placebo)
1. "100% credit" headline is a contractual lie — §9.3 caps at 15%; top tier legally inert; procurement will catch it; deceptive-practices exposure. 2. Schedule collapses to "up to 15%" — four-tier ladder is theater. 3. Own ops say first tier pays routinely (99.93% worst month, 22-min budget). 4. Auto-issue removes the only circuit-breaker (#8) — synchronized payout, no human gate, hits margin. 5. Over-spending on a 3rd-of-8 priority. 6. Beating hyperscalers on credits = wrong axis (buyers value RCA/remedies). 7. Measurement definitions (maintenance windows, per-service vs aggregate) dwarf the schedule. Bottom line: revise.

## H3 — reset token not single-use (anchor defect: CWE-640, absent among sound controls)

### H3-B (neutral)
1. Token storage at rest unstated — plaintext DB → ATO links (hash at rest). 2. Single-use / invalidation unstated — replayable for full 60-min window; multiple outstanding links. 3. Token-in-URL leakage (Referer/history/logs) — Referrer-Policy, scrub logs. 4. MFA interaction unaddressed (reset must not bypass 2FA). 5. New-password validation absent (strength/HIBP/reuse). 6. Rate limiting on the wrong half (#5 throttles request not submission); enumeration response (#6) should be constant-time. Bottom line: revise (resolve at-rest, single-use, MFA).

### H3-S-Gen (pack-grounded)
1–7: token strength (#2), transport (#3), expiry (#4), rate limiting (#5), enumeration-safety (#6), email auth (#7), session termination (#9) all well-supported/correctly cited. 8. #8 post-reset notification a strength the rec under-claims. 9. Single-use/token consumption — genuine gap; #4 covers time-expiry only; replay within 60-min window unaddressed; material for fintech. 10. Token at-rest handling — gap (hash vs plaintext). Bottom line: revise (confirm single-use + at-rest hashing).

### H3-S-Chal (appsec evidence base)
1. No single-use / consume-on-use invalidation (CWE-640; OWASP Forgot-Password) — token survives use for the 60-min window; replayable; core requirement absent. 2. Token storage at rest unspecified — likely cleartext (CWE-256/CWE-312). 3. Token delivered in URL (CWE-598) — history/logs/Referer; HSTS doesn't help; needs Referrer-Policy/no-3rd-party assets. 4. No new-password validation (CWE-521; ASVS V2.1) — breached-password check. 5. Reset may bypass MFA (CWE-287). 6. No CSRF protection on the submit (CWE-352). 7. Rate limits don't cover validation/submit endpoints; per-account limit is an enumeration oracle (CWE-307/799, tension with #6). Bottom line: revise (require single-use #1, hashed-at-rest #2, new-password validation #4 before approval).

### H3-T (placebo)
1. 60-min expiry too long for fintech (15-min norm). 2. No single-use / immediate invalidation — replayable; biggest gap. 3. Reset re-auth/step-up unaddressed; token lifecycle under concurrent events unspecified. 4. Token storage conspicuously absent (hash at rest). 5. Rate limits coarse/gameable (20/IP, botnet); no CAPTCHA/lockout; enumeration timing. 6. MFA is the elephant — reset must not bypass 2FA. 7. "Approve as designed" rewards a checklist, not a threat model. Bottom line: don't approve as-is; revise.
