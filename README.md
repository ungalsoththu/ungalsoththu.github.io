# UngalSoththu — உங்கள் சொத்து (GitHub Pages site)

Public website for the **UngalSoththu** transit-accountability desk of
[CashlessConsumer](https://cashlessconsumer.in). Live at
**https://ungalsoththu.github.io/** — English at `/`, Tamil at `/ta/`.

## Structure

- Astro 5 static site (bilingual: `/` EN, `/ta/` TA), deployed by the GitHub
  Action in `file .github/workflows/deploy.yml` on every push to `main`.
- `public/daily-briefs/` — **Daily transit briefs subsite** (pre-built HTML;
  Astro copies `public/` verbatim).
- `public/grm-weekly/` — **Weekly grievance-redress audit subsite** (pre-built).
- `file public/og.png` — social card.

## Daily update pipeline

The briefs are authored in the CashlessConsumer workspace (NOT in this repo):

- Source notes: `file UngalSoththu/notes/*-daily-transit-brief*.md` and
  `file UngalSoththu/notes/*transit-grm-weekly*.md` (local workspace path).
- `file scripts/build.py` renders new/updated notes with pandoc into
  `public/daily-briefs/` and `public/grm-weekly/`, and regenerates both
  subsite indexes.
- `file scripts/publish.sh` = build → commit → push. The deploy Action then builds
  Astro and publishes (\~2 min).

A scheduled Zo automation runs `file scripts/publish.sh` daily at \~09:15 IST after
posting the @UngalSoththu X thread, and after each weekly GRM audit.

## History

2026-01: bilingual Astro foundation (see `.planning/`).
2026-10-03: daily-briefs + grm-weekly subsites added; EN/TA hubs upgraded from
the temporary placeholder.