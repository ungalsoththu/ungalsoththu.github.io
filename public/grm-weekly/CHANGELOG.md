# Detection changelog

Every change to `grm-detection.json` lands here first: what changed, the lesson that
triggered it, and the eval-set outcome after the change.

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
