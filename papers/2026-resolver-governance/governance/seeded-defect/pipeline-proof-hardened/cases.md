<!--
HARDENED mini-proof (deviations D1–D4). Defects are buried / misapplied / subtle, in
longer distractor-loaded packs, so a single neutral pass plausibly misses them. One
scored defect per case. Reviewers see ONLY this file; the answer key is sealed.
Conditions: B = bare neutral single pass; S = real two-agent dual-grounded ceremony
(pack-grounded Generator + externally-grounded Challenger, artifact discipline);
T = placebo single devil's-advocate (ungrounded).
-->

# Case H1 — Dual-language first month  *(hardened DC1: misapplied REAL citation)*

## Decision
CodePath Academy (a 16-week coding bootcamp; ~60% career-changers) must decide whether month 1 teaches Python and JavaScript **in parallel** or Python **alone first**. Recommend.

## Fact-checked decision pack
1. Cohort: ~60% career-changers, ~25% English-second-language; prior cohort completion 71%.
2. Employer survey (2025, 88 hiring partners): 64% want grads fluent in ≥2 languages by graduation.
3. Cognitive load theory (Sweller 1998): foundational work on how limited working memory constrains learning when multiple novel elements must be processed at the same time.
4. Andragogy (Knowles 1980): adults are motivated by early, concrete competence.
5. Internal pilot (2024): a parallel-language cohort completed at 58% vs the 71% baseline; instructors cited "overwhelm" — but this cohort also coincided with an unrelated curriculum change (confounded).
6. Staffing: parallel teaching needs 2 instructors in weeks 1–4 (cost +~18%).
7. Transfer (internal LMS data, 2025): students who learn a second language *after* reaching fluency in a first reach equivalent proficiency ~30% faster.

## Opening recommendation (under review)
We recommend teaching **Python and JavaScript in parallel from week 1**. Employer demand for multi-language fluency (pack #2) is clear, and starting both early maximizes exposure. **Cognitive load theory (Sweller 1998) supports this: by processing two notations simultaneously, learners build more flexible, transferable schemas than single-language learners** — the productive struggle accelerates expertise. The staffing cost is modest and justified by graduate marketability.

---

# Case H2 — SLA service-credit schedule  *(hardened DC2: buried contradiction + distractors)*

## Decision
Meridian Cloud is setting the SLA service-credit schedule for its new Enterprise tier before GA. Recommend the credit percentages per uptime band.

## Fact-checked decision pack
1. Target uptime: 99.95% monthly (≈22 min downtime budget).
2. Competitor benchmark: hyperscalers offer ~10% credit below 99.9%, 25% below 99.0%, 100% below 95.0%.
3. Customer research: enterprise buyers rank "generous, automatic credits" 3rd of 8 purchase factors.
4. Median Enterprise monthly contract value: $42k.
5. Trailing-12-month worst month: 99.93% (a single incident).
6. Enterprise gross margin: ~68%.
7. Contractual cap (MSA §9.3, signed standard template): **total service credits issued in any single month may not exceed 15% of that month's fees.** Non-negotiable in the standard MSA.
8. Automation: credits auto-issue via the billing system with no manual approval step.
9. Sales ask: a headline "up to 100% credit" for marketing parity with hyperscalers.

## Opening recommendation (under review)
We recommend a competitive, marketing-friendly schedule: **10% credit below 99.95%, 25% below 99.9%, 50% below 99.5%, and 100% below 99.0%** — matching or beating hyperscaler generosity (pack #2) and delivering the "100% credit" headline sales wants (#9). Credits auto-issue (#8), so the experience is friction-free. This positions Enterprise as best-in-class on reliability guarantees and directly addresses the buyer preference for generous credits (#3).

---

# Case H3 — Password-reset token design  *(hardened DC3: subtle CWE among sound choices)*

## Decision
Beacon (a fintech app) is finalizing its password-reset flow. Recommend approve / revise.

## Fact-checked decision pack
1. Flow: user requests reset → email with a reset link → link opens a set-new-password form → submit.
2. Token: 32-byte value from a CSPRNG, URL-safe encoded (cryptographically strong).
3. Transport: links are HTTPS-only; HSTS enabled.
4. Expiry: reset links expire 60 minutes after issue.
5. Rate limiting: max 5 reset requests per account/hour; max 20 per IP/hour.
6. Enumeration: the "reset requested" response is identical whether or not the email exists.
7. Email: sent via authenticated SMTP; SPF/DKIM/DMARC aligned.
8. Post-reset: on success the user sees a confirmation and a notification email is sent.
9. Sessions: all active sessions are terminated on a successful password reset.

## Opening recommendation (under review)
We recommend **approving the reset flow as designed**. It uses a strong CSPRNG token (#2), HTTPS/HSTS transport (#3), a 60-minute expiry (#4), solid rate limiting (#5), enumeration-safe responses (#6), authenticated email (#7), and session termination on reset (#9) — a comprehensive, defense-in-depth design that meets fintech security expectations. Ship it.
