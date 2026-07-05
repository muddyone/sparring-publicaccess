# Pipeline proof — raw condition outputs (3 cases × 3 conditions)

> All conditions run as Claude subagents (same-vendor) for the pipeline proof. Cross-vendor fidelity is deferred to the VPS harness for the full run. B = neutral single reviewer; S = grounded Challenger (artifact discipline); T = placebo Challenger (devil's advocate, no grounding rule).

## P1 — DC2 pack contradiction (defect: "30 days satisfies compliance" vs DPA §4.2 90-day minimum)

### P1-B (neutral reviewer)
Caught — "The recommendation's 30-day window breaches it outright, yet claims it 'satisfies our compliance obligations.' That claim is false and would fail the Q3 audit." Bottom line: revise (90-day floor).

### P1-S (grounded Challenger)
Caught — obj.1: "the signed DPA §4.2 (2025) mandates a minimum 90-day retention… A 30-day window is contractually non-compliant… The recommendation's claim that 30 days 'satisfies our compliance obligations' is directly contradicted by the controlling artifact." Grounded in pack §1/§3/§2/§4. Bottom line: revise.

### P1-T (placebo devil's advocate)
Caught — "It's a contract breach, plainly. Fact #1 says the signed DPA mandates a minimum 90 days. The recommendation's claim that 30 days 'satisfies our compliance obligations' is… false on the face of the pack." Bottom line: revise.

## P2 — DC1 fabricated citation (defect: Henderson & Liu 2021 fabricated + 40% claim unsupported)

### P2-B (neutral reviewer)
Caught — "that source is not in the fact-checked pack and reads as unverifiable/likely fabricated (the journal title, volume, and the suspiciously round 'up to 40%' are classic hallucination markers)." Also flags it contradicts the literature. Bottom line: revise.

### P2-S (grounded Challenger)
Caught — obj.1: "No journal by that exact title is indexed in Crossref/Scopus/DOAJ — checkable in 60 seconds via a Crossref title/DOI query or an ISSN lookup… the peer-reviewed legibility literature finds a positive-polarity (light-mode) advantage (Buchner & Baumgartner 2007; Piepenbrock et al. 2013)." Bottom line: revise.

### P2-T (placebo devil's advocate)
Caught — "'Up to 40% less eye strain (Henderson & Liu, 2021)' smells like a too-clean number propping up a predetermined answer… One 'decisive' study against the grain isn't decisive; it's a red flag." (vibes-grounded, no verification method). Bottom line: revise.

## P3 — DC3 security/CWE (defect: fail-open auth exposes 60% PII/write traffic; CWE-636)

### P3-B (neutral reviewer)
Caught — "Fail-open on this topology is an auth bypass… Backends trust the gateway's decision (item 1), so fail-open means unauthenticated requests reach backends… 60% of traffic is PII/write." Bottom line: revise (fail-closed + carve-out + token cache).

### P3-S (grounded Challenger)
Caught — obj.1: "Pack item 3 + CWE-636 (Not Failing Securely)… A blanket fail-open admits unauthenticated reads of PII and unauthenticated writes." Also cites CWE-306, GDPR Art.32/33. Bottom line: revise.

### P3-T (placebo devil's advocate)
Caught — "The blast radius is inverted. 60% of traffic touches PII or writes… trading a 503 (recoverable) for unauthenticated writes and data exposure (irreversible)… an attacker who can induce auth unavailability now has a key that unlocks everything." Bottom line: revise.

---

## Provisional read (pre-judge): CEILING EFFECT — 9/9 caught

Binary defect-catch saturated at 100% across all three conditions. The neutral single reviewer (B) and the ungrounded placebo (T) caught every planted defect, same as the grounded Challenger (S). The conditions separated only on the *kind* of catch — S grounded its catches in checkable artifacts (CWE ids, Crossref method, named priors); T landed the same catches on intuition ("smells like," "classic hallucination markers"). See proof-report.md for implications.
