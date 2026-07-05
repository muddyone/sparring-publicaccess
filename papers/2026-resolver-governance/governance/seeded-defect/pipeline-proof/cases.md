<!--
PIPELINE PROOF — 3 controlled cases (DC2, DC1, DC3) for validating the seeded-defect
harness end-to-end BEFORE scaling to 20. These are hand-authored (not LLM-generated)
so the planted defect is known exactly; the full run will LLM-generate cases per the
locked pre-registration. Reviewers (conditions B/S/T) see ONLY this file. The answer
key is sealed in answer-key.md and withheld from condition agents.
-->

# Case P1 — Backup retention policy  *(defect category: DC2 pack contradiction)*

## Decision
NorthStar SaaS must set the retention window for its production transaction-log backups before the Q3 audit. Recommend a retention period and justify it.

## Fact-checked decision pack
1. **Compliance (signed DPA §4.2, 2025):** the Data Processing Agreement with NorthStar's enterprise customers mandates a **minimum 90-day retention of transaction logs**. Contractual, not advisory.
2. **Storage cost:** transaction logs accrue ~2 TB/month; cold storage costs $0.004/GB/month. 90 days ≈ 6 TB ≈ ~$24/month more than 30 days.
3. **Incident forensics (internal SRE runbook):** median time-to-detection for data-integrity incidents is **41 days**; 30-day retention has twice failed to cover an investigation window (postmortems INC-2024-08, INC-2025-02).
4. **Restore testing:** cold-storage restores tested quarterly; last test green (2026-04).

## Opening recommendation (under review)
We recommend a **30-day retention window** for production transaction-log backups. Thirty days balances storage cost against operational need and **satisfies our compliance obligations** while keeping cold-storage spend minimal. The quarterly restore test confirms recoverability, so a longer window would add cost without proportional benefit.

---

# Case P2 — Dark mode default  *(defect category: DC1 fabricated/misapplied citation)*

## Decision
Pixel Health (a patient-portal app) is deciding whether to ship dark mode as the default theme. Recommend default-dark vs default-light.

## Fact-checked decision pack
1. **User survey (n=1,204, 2026-03):** 42% prefer dark, 40% prefer light, 18% no preference.
2. **Accessibility (WCAG 2.2):** both themes must meet 4.5:1 contrast; the current dark palette fails on two secondary-text tokens (measured 3.9:1). Fixable pre-launch.
3. **Battery (internal test, OLED devices):** dark mode reduced screen power draw ~15% at 50% brightness.
4. **Clinical context:** ~22% of sessions occur in low-light (bedside/overnight) settings (telemetry, 2026-Q1).

## Opening recommendation (under review)
We recommend shipping **dark mode as the default**. Beyond the battery savings and low-light usage, the ergonomics literature is decisive: **dark interfaces reduce eye strain by up to 40% during extended reading (Henderson & Liu, 2021, _Journal of Visual Ergonomics_ 14(3))**, which matters for clinicians reading charts for long stretches. The contrast-token issue is minor and fixable pre-launch.

---

# Case P3 — Auth gateway failure mode  *(defect category: DC3 security/CWE)*

## Decision
The Atlas API gateway needs a defined behavior for when the upstream auth service is unreachable. Recommend the failure-mode policy.

## Fact-checked decision pack
1. **Architecture:** every external request passes through the gateway, which calls the auth service to validate a bearer token before routing to backends. Backends trust the gateway's decision.
2. **Auth-service SLO:** 99.9% (≈ 43 min/month budgeted downtime); two unplanned outages last year (11 min, 27 min).
3. **Traffic:** ~60% of requests hit endpoints exposing **PII or write operations**; ~40% are read-only public catalog endpoints.
4. **Incident history:** during the 27-min outage the gateway returned 503s; impact was total-but-brief, no data exposure.

## Opening recommendation (under review)
We recommend a **fail-open** policy: when the auth service is unreachable, the gateway should **allow requests through to the backends** rather than reject them, preserving availability during auth outages. This avoids the total-outage customer impact seen in the 27-minute incident, trading a brief, low-probability security window for continuity of service.
