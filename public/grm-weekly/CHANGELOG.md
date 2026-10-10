# Detection changelog

Every change to `grm-detection.json` lands here first: what changed, the lesson that
triggered it, and the eval-set outcome after the change.

## v1.2 — 2026-10-10 · Chennai handle recovery, broad-name coverage, shared TNSTC/SETC watch

**Lesson.** Zero-result checks found two bad Chennai watch entries: `@drmsrchennai` no longer resolves, while `@DrmChennai` is the active Chennai Division account; `@CumtaChennai` had no profile/activity evidence, while `@CumtaOfficial` identifies as CUMTA and is referenced by Chennai One. The same checks surfaced an untagged Gummidipoondi–Chennai Central delay grievance and a Route 105 MTC live-tracking grievance missed by handle-only searches. A broad TNSTC search also found a passenger report of a slow TNSTC trip. The account `@tnstc_setc` describes itself as TNSTC & SETC, but its official status is not independently linked from a government site; the headlight complaint tagged there does not identify the operator.

**Change.** Repointed Chennai Division and CUMTA to their currently identified profiles and retained the old entries in `handle_history`. Replaced inactive TNSTC/SETC handles with the shared candidate `@tnstc_setc`, preserving the prior handles. Added agency-specific broad search terms and a fourth `{search_term}` search pattern so untagged service grievances are not dependent on a zero-result week. Added an explicit cross-agency rule: search shared accounts once, assign only when the service/operator is identified, and otherwise count the incident once as shared/unassigned. The joint account’s officiality caveat is explicit in the config.

**Detection review.** “Live tracking unavailable,” missed stops, pass issuance/refund failures, and slow journeys fit existing categories; no taxonomy or reply-rule change was needed. An official CMRL QR-ticketing notice and its restoration post, suburban derailment news, a general CUMTA criticism, a lane-change question, praise, and posts outside the exact 09:00 IST cutoff were excluded because they were not in-window passenger grievances matching the include rules. Image-led BMTC cases with no visible description are flagged unverified only where BMTC itself acknowledged a complaint. No hourly scheduler data was used.

**Eval.** Re-checked all 13 labeled complaint cases against the updated watchlist, broad terms, and unchanged inclusion/exclusion rules: every expected agency/category label remains valid. All 3 known-miss drills remain intact: the obsolete Kerala handle returns no results, the MTC legacy handle remains searchable, and praise/feature requests remain excluded. [Evaluation set](https://ungalsoththu.github.io/grm-weekly/eval-set.json).

**Evidence.** [Chennai Division profile](https://x.com/DrmChennai) · [suburban-delay complaint](https://x.com/AswaniK95518339/status/2108052168351834320) · [Route 105 tracking grievance and reply](https://x.com/SmonishaHarish/status/2106986190725583199) · [CUMTA profile](https://x.com/CumtaOfficial) · [Chennai One reference](https://x.com/Chennai_One) · [joint TNSTC/SETC profile](https://x.com/tnstc_setc) · [TNSTC slow-service complaint](https://x.com/KoushikNaarayan/status/2108179293981573168) · [shared headlight complaint](https://x.com/JrsPrabu/status/2108602580171685964).

## v1.1 — 2026-10-03 · stale-handle repair

**Lesson.** The first audits under-counted Chennai and read Kerala as silent. Four of the
ten watchlist handles were stale: `@mtc_chennai` → `@MtcChennai`, `@cmrlchennai` →
`@cmrlofficial`, `@dtc_india` → `@dtchq_delhi`, and `@KSRTC_Kerala` was never the Kerala
agency at all (it is `@keralasrtc`). A week of "no complaints found" was really a dead
watch.

**Change.** Corrected all four handles; added `handle_history` so searches also cover
legacy names riders still tag; added the `zero_complaint_check` rule — a zero week for a
known-active agency triggers a handle-liveness check before it can be reported.

**Eval.** 13 labeled complaint cases + 3 known-miss drills seeded from the 2026-09-26 and
2026-10-03 audits; all cases correctly classifiable under v1.1 rules (legacy-tag thread
`sibin_91/2105505463530063992` recovered via the reply from the current handle).

## v1.0 — 2026-03-30 · initial watchlist

Weekly audit automation created: 10 agencies, 7-day window, complaint/reply detection,
"acknowledged is not resolved" reporting rule.
