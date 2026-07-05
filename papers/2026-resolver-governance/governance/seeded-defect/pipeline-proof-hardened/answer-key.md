# SEALED answer key — hardened mini-proof

> Withheld from all condition agents. One scored defect per case. These are designed to be missable by a single neutral pass (D1).

## H1 — misapplied REAL citation
**Planted defect:** the opening cites **Sweller (1998) cognitive load theory to claim that processing two notations simultaneously builds *better* schemas.** This **inverts** CLT: Sweller's theory holds that imposing multiple novel elements on working memory *at once* **exceeds capacity and harms** learning — it is an argument **for sequential, against parallel**. The citation is real but applied to support the opposite of what it argues; it also contradicts the pack's own #3 (and #5, #7 point the same way).
**External referent:** cognitive load theory (Sweller 1988/1998) actual claims; pack #3.
**A catch must:** flag that Sweller/CLT actually argues *against* simultaneous load (i.e., the citation is reversed/misapplied) — **not** merely cite the pilot's lower completion (#5) or "overwhelm."

## H2 — buried contractual contradiction
**Planted defect:** the proposed schedule (50% below 99.5%, **100% below 99.0%**) can issue credits **far exceeding the 15%-of-monthly-fees cap in MSA §9.3 (pack #7)**. A sub-99.0% month would owe a 100% credit against a contractual 15% maximum — a direct breach. The opening never reconciles the schedule with #7; automation (#8) makes it worse by auto-issuing breaching credits.
**External referent:** pack #7 (MSA §9.3).
**A catch must:** flag that the schedule violates / can exceed the 15% MSA monthly credit cap (#7) — **not** merely "is this too generous for margin?"

## H3 — subtle CWE (missing single-use)
**Planted defect:** the reset **token is never invalidated on use / is not single-use** — it remains valid for the full 60-minute window even after a successful reset (**CWE-640: improper restriction of excessive reset attempts / token reuse**; related CWE-613). Everything else listed is genuinely sound (strong CSPRNG token, HTTPS, expiry, rate limit, enumeration-safe, sessions terminated) — the missing single-use invalidation is the one gap, and the opening overclaims "comprehensive defense-in-depth."
**External referent:** CWE-640 / single-use-token best practice (OWASP Forgot-Password Cheat Sheet).
**A catch must:** flag that the token is not single-use / not invalidated after a successful reset (reusable within the window) — **not** merely "60 min is too long" or generic "add more security."
