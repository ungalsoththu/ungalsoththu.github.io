#!/usr/bin/env python3
"""Build the UngalSoththu daily-briefs + GRM-weekly subsites from workspace notes.

Sources (read-only):
  ../../notes/*-daily-transit-brief*.md   -> public/daily-briefs/
  ../../notes/*transit-grm-weekly*.md     -> public/grm-weekly/

Outputs (pre-built static HTML; Astro copies public/ verbatim into dist/):
  public/daily-briefs/index.html + <name>.html
  public/grm-weekly/index.html + <name>.html
  public/og.png (copied from repo root public/ if missing — managed via git)

The Astro hub (src/pages/index.astro, /ta/) links to these subsites.

Zero-dep besides pandoc (system). Deterministic; safe to re-run.
"""
import html
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
NOTES = SITE.parent / "notes"
PUBLIC = SITE / "public"
BRIEFS = PUBLIC / "daily-briefs"
REPORTS = PUBLIC / "grm-weekly"
SITE_URL = "https://ungalsoththu.github.io"
DETECTION = SITE / "detection"

PALETTE = {
    "bg": "#0b2e2f",
    "fg": "#eef7f5",
    "muted": "#c9e4e0",
    "accent": "#f0b429",
    "accent_alt": "#8fd0c8",
    "danger": "#c62828",
    "card": "rgba(17,52,53,0.85)",
}

CSS = f"""
:root {{
  --bg: {PALETTE['bg']}; --fg: {PALETTE['fg']}; --muted: {PALETTE['muted']};
  --accent: {PALETTE['accent']}; --accent-alt: {PALETTE['accent_alt']};
  --danger: {PALETTE['danger']}; --card: {PALETTE['card']};
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: Inter, 'Noto Sans Tamil', system-ui, sans-serif;
  line-height: 1.65; -webkit-font-smoothing: antialiased;
}}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.wrap {{ max-width: 780px; margin: 0 auto; padding: 0 20px 64px; }}
header.site {{
  border-bottom: 1px solid rgba(238,247,245,0.14);
  padding: 28px 0 22px; margin-bottom: 8px;
}}
.wordmark {{
  font-size: 26px; font-weight: 800; letter-spacing: 0.14em; color: var(--fg);
}}
.wordmark .ta {{ color: var(--accent-alt); font-weight: 600; letter-spacing: 0; margin-left: 10px; }}
.tagline {{ color: var(--muted); font-size: 15px; margin-top: 6px; max-width: 620px; }}
nav.links {{ margin-top: 14px; font-size: 14px; display: flex; gap: 18px; flex-wrap: wrap; }}
nav.links a {{ color: var(--accent-alt); font-weight: 600; }}
h1 {{ font-size: 26px; margin: 34px 0 6px; }}
h2 {{ font-size: 19px; margin: 30px 0 10px; color: var(--accent-alt); }}
section.brief-list {{ margin-top: 18px; }}
.brief-row {{
  display: flex; align-items: baseline; gap: 14px;
  padding: 10px 0; border-bottom: 1px solid rgba(238,247,245,0.09);
}}
.brief-row .date {{ min-width: 150px; font-weight: 700; color: var(--fg); }}
.brief-row .meta {{ color: var(--muted); font-size: 14px; }}
.brief-row .thread {{ margin-left: auto; font-size: 13px; white-space: nowrap; }}
.card {{
  background: var(--card); border: 1px solid rgba(238,247,245,0.12);
  border-radius: 12px; padding: 18px 20px; margin: 18px 0;
}}
article {{
  background: var(--card); border: 1px solid rgba(238,247,245,0.12);
  border-radius: 12px; padding: 26px 30px; margin-top: 18px;
}}
article h1 {{ font-size: 24px; margin-top: 0; }}
article h2 {{ color: var(--accent-alt); }}
article a {{ word-break: break-word; }}
article blockquote {{
  border-left: 3px solid var(--accent); margin: 14px 0; padding: 2px 16px;
  color: var(--muted);
}}
.crumb {{ font-size: 13px; color: var(--muted); margin-top: 22px; }}
.crumb a {{ color: var(--accent-alt); }}
footer.site {{
  margin-top: 56px; border-top: 1px solid rgba(238,247,245,0.14);
  padding-top: 20px; color: var(--muted); font-size: 14px;
}}
footer.site .ta-line {{ color: var(--accent); font-weight: 700; }}
.updated {{ color: var(--muted); font-size: 13px; margin-top: 4px; }}table {{ border-collapse: collapse; margin: 12px 0; width: 100%; }}
table td, table th {{ border: 1px solid rgba(238,247,245,0.18); padding: 8px 12px; text-align: left; font-size: 0.93em; }}
table th {{ background: rgba(240,180,41,0.12); }}
table .dim {{ font-weight: 400; }}
.cols {{ display: flex; gap: 24px; flex-wrap: wrap; }}
.cols > div {{ flex: 1; min-width: 260px; }}
.cols ul {{ padding-left: 20px; margin: 6px 0; }}
.dim {{ color: var(--muted); font-size: 0.9em; }}
"""

HEADER = """<header class="site">
  <div class="wordmark"><a href="/" style="color:inherit">UNGALSOTHTHU</a><span class="ta">உங்கள் சொத்து</span></div>
  <div class="tagline">Public transit and urban infrastructure, examined with open data — in the public interest. Chennai &amp; Tamil Nadu: MTC, CMRL, suburban rail, CUMTA, TNSTC, SETC.</div>
  <nav class="links">
    <a href="/">Home</a>
    <a href="/daily-briefs/">Daily briefs</a>
    <a href="/grm-weekly/">GRM weeklies</a>
    <a href="https://x.com/UngalSoththu">@UngalSoththu on X</a>
    <a href="https://logicinczo.github.io/chennai-flood-undersight/">ChennaiFloodUndersight</a>
  </nav>
</header>"""

FOOTER = """<footer class="site">
  <div>Published by the UngalSoththu desk of <a href="https://cashlessconsumer.in">CashlessConsumer</a>. Sources: linked news reports and agency replies; figures are as reported by the cited publication on the cited date.</div>
  <div class="ta-line">Public transit is a public asset. இது உங்கள் சொத்து.</div>
</footer>"""


def page(title: str, desc: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE_URL}/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+Tamil:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{HEADER}
{body}
{FOOTER}
</div>
</body>
</html>
"""


def render_md(md_path: Path) -> str:
    return subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", str(md_path)],
        check=True, capture_output=True, text=True,
    ).stdout

def build_method() -> None:
    """Render public/grm-weekly/how.html from detection/ and publish raw configs."""
    import json
    cfg = json.loads((DETECTION / "grm-detection.json").read_text(encoding="utf-8"))
    evals = json.loads((DETECTION / "eval-set.json").read_text(encoding="utf-8"))

    watch_rows = []
    for a in cfg["agencies"]:
        hist = ""
        if a.get("handle_history"):
            olds = ", ".join("@" + h["handle"] for h in a["handle_history"])
            hist = f'<div class="dim">was: {html.escape(olds)}</div>'
        watch_rows.append(
            f'<tr><td>{html.escape(a["name"])}</td><td>@{html.escape(a["handle"])}{hist}</td>'
            f'<td>{html.escape(a["city"])}</td></tr>')
    watch_html = "\n".join(watch_rows)

    inc = "".join(f"<li>{html.escape(x)}</li>" for x in cfg["include"])
    exc = "".join(f"<li>{html.escape(x)}</li>" for x in cfg["exclude"])
    cats = ", ".join(cfg["categories"])
    n_cases = len(evals["complaint_cases"])
    n_drills = len(evals["known_miss_drills"])
    n_replied = sum(1 for c in evals["complaint_cases"] if c.get("replied"))
    changelog_html = render_md(DETECTION / "CHANGELOG.md")

    body = f"""
<div class="crumb"><a href="index.html">← All audits</a></div>
<h1>How this audit is made — and how it improves</h1>
<div class="updated">The weekly grievance-redress audit is produced by a scheduled agent
running against the watchlist and rules on this page. The configuration is versioned,
published in full, and changes only through a logged decision (see the changelog below).
Config version <strong>{html.escape(cfg['version'])}</strong>, updated {html.escape(cfg['updated'])}.</div>

<h2>The pipeline</h2>
<ol>
<li><strong>Watchlist.</strong> Search the agencies below on X, over the past 7 days, using
the patterns in <code>grm-detection.json</code> (mentions of the agency handle and replies from it,
date-filtered).</li>
<li><strong>Classify.</strong> Keep passenger grievances about a specific service failure.
Exclude praise, feature requests and official announcements — the full include/exclude
rules are published with the config.</li>
<li><strong>Dedupe.</strong> One incident = one complaint, however many posts; follow-ups
merge into the original.</li>
<li><strong>Replies.</strong> Detect any visible reply from the agency handle. A reply may be
just a forward or a docket number — acknowledged is explicitly not resolved, and each
report says which.</li>
<li><strong>Measure.</strong> Response rate, category counts, approximate response times
decoded from post IDs.</li>
<li><strong>Publish.</strong> Report goes live here, to the archive index, and a summary to
Telegram the same morning.</li>
<li><strong>Review &amp; improve.</strong> After every run the agent reviews what it may have
missed; watchlist or rule changes land as a new config version with a changelog entry,
and the labeled eval set below is re-checked.</li>
</ol>

<h2>The watchlist</h2>
<table>
<tr><th>Agency</th><th>X handle</th><th>City</th></tr>
{watch_html}
</table>
<div class="dim">Handles go stale when agencies rename accounts — a silent week of zero
complaints is treated as a stale-handle smell, not a finding. Previous handles are kept
in the config because riders still tag old names.</div>

<h2>What counts, what doesn't</h2>
<div class="cols">
<div><strong>Included</strong>
<ul>{inc}</ul></div>
<div><strong>Excluded</strong>
<ul>{exc}</ul></div>
</div>
<div class="dim">Categories: {html.escape(cats)}.</div>

<h2>Known limits</h2>
<div class="card">{html.escape(cfg['limits'])}</div>

<h2>The self-improvement loop</h2>
<p>Detection improves through three published artifacts, all in the
<a href="https://github.com/ungalsoththu/ungalsoththu.github.io/tree/main/detection">repo's <code>detection/</code> folder</a>:</p>
<ul>
<li><strong>Config</strong> — <a href="grm-detection.json"><code>grm-detection.json</code></a>: the watchlist,
search patterns, include/exclude and reply rules the agent actually executes.</li>
<li><strong>Changelog</strong> — <a href="CHANGELOG.md"><code>CHANGELOG.md</code></a>: every config change
with the lesson that triggered it.</li>
<li><strong>Eval set</strong> — <a href="eval-set.json"><code>eval-set.json</code></a>: {n_cases} labeled
complaint posts ({n_replied} with known agency replies) plus {n_drills} known-miss drills,
seeded from past audits. After any config change, these must still be detected correctly
before the change ships.</li>
</ul>
{changelog_html}
"""
    (REPORTS / "how.html").write_text(
        page("How the weekly GRM audit is made · UngalSoththu — உங்கள் சொத்து",
             "Methodology of the weekly India transit grievance-redressal audit: "
             "watchlist, detection rules, changelog and labeled eval set.",
             body),
        encoding="utf-8")
    for name in ("grm-detection.json", "eval-set.json", "CHANGELOG.md"):
        shutil.copyfile(DETECTION / name, REPORTS / name)


def fmt_date(iso: str) -> str:
    d = datetime.strptime(iso, "%Y-%m-%d")
    return d.strftime("%-d %b %Y (%a)")


def brief_meta(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    iso = md_path.stem[:10]
    items = len(re.findall(r"^\d+\.\s+\*\*\[", text, re.M))
    m = re.search(r"## Thread URL\s*\n+\s*(https://\S+)", text)
    thread = m.group(1) if m else None
    skipped = "skipped" in md_path.stem
    return {"iso": iso, "date": fmt_date(iso), "items": items,
            "thread": thread, "skipped": skipped, "name": md_path.stem}


def report_title(md_path: Path) -> str:
    first = md_path.read_text(encoding="utf-8").splitlines()[0]
    return first.lstrip("# ").strip()


def sync_and_render() -> tuple[list[dict], list[dict]]:
    BRIEFS.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    briefs: list[dict] = []
    reports: list[dict] = []

    for src in sorted(NOTES.glob("*-daily-transit-brief*.md")):
        dest_md = BRIEFS / src.name
        shutil.copyfile(src, dest_md)
        meta = brief_meta(dest_md)
        meta["href"] = f"{src.stem}.html"
        body = render_md(dest_md)
        title = f"Daily Transit Brief — {meta['iso']} · UngalSoththu"
        (BRIEFS / f"{src.stem}.html").write_text(
            page(title,
                 f"Chennai/Tamil Nadu transit news brief for {meta['date']}, "
                 f"with sources — the UngalSoththu desk.",
                 f'<div class="crumb"><a href="index.html">← All briefs</a></div>'
                 f"<article>{body}</article>"),
            encoding="utf-8")
        briefs.append(meta)

    for src in sorted(NOTES.glob("*transit-grm-weekly*.md")):
        dest_md = REPORTS / src.name
        shutil.copyfile(src, dest_md)
        title = f"{report_title(dest_md)} · UngalSoththu"
        body = render_md(dest_md)
        (REPORTS / f"{src.stem}.html").write_text(
            page(title,
                 "Weekly India transit grievance-redressal audit from the "
                 "UngalSoththu desk — complaints, agency replies, fixes shown.",
                 f'<div class="crumb"><a href="index.html">← All audits</a></div>'
                 f"<article>{body}</article>"),
            encoding="utf-8")
        reports.append({"iso": src.stem[:10], "name": src.stem,
                        "title": title, "href": f"{src.stem}.html"})

    briefs.sort(key=lambda b: b["iso"], reverse=True)
    reports.sort(key=lambda r: r["iso"], reverse=True)
    return briefs, reports


def build_briefs_index(briefs: list[dict]) -> None:
    rows = []
    for b in briefs:
        if b["skipped"]:
            rows.append(f'<div class="brief-row"><span class="date">{b["date"]}</span>'
                        f'<span class="meta">no brief (fewer than 2 items found)</span></div>')
            continue
        thread = (f'<a href="{b["thread"]}">thread ↗</a>' if b["thread"] else "")
        rows.append(
            f'<div class="brief-row"><span class="date">{b["date"]}</span>'
            f'<span class="meta">{b["items"]} items</span>'
            f'<a href="{b["href"]}">read</a>'
            f'<span class="thread">{thread}</span></div>')
    brief_html = "\n".join(rows) or "<p>No briefs yet.</p>"

    latest = briefs[0]["date"] if briefs and not briefs[0]["skipped"] else "—"
    total_items = sum(b["items"] for b in briefs)
    n = len([b for b in briefs if not b["skipped"]])
    body = f"""
<h1>Daily transit briefs</h1>
<div class="updated">{n} briefs · {total_items} sourced items · latest {latest}. Each brief rounds up the last 24 hours of Chennai/Tamil Nadu transit news, every item with publication + date + link — the same thread posted daily to <a href="https://x.com/UngalSoththu">@UngalSoththu</a>.</div>
<section class="brief-list">
{brief_html}
</section>

<div class="card">
<strong>About this desk.</strong> "Ithu Ungal Soththu" — this is YOUR property.
Chennai's buses, metros, suburban trains and the agencies that run them are public
assets. UngalSoththu tracks their operations, plans, budgets and the accountability
gaps in between: service changes, fares, fleet, ridership, project progress, audits —
number-led, source-linked, never party-political.
</div>
"""
    (BRIEFS / "index.html").write_text(
        page("Daily Transit Briefs · UngalSoththu — உங்கள் சொத்து",
             "Daily Chennai/Tamil Nadu transit news briefs — sourced, "
             "number-led, riders-first. A CashlessConsumer desk.",
             body),
        encoding="utf-8")


def build_reports_index(reports: list[dict]) -> None:
    rep_rows = []
    for r in reports:
        rep_rows.append(
            f'<div class="brief-row"><span class="date">{r["iso"]}</span>'
            f'<a href="{r["href"]}">{html.escape(r["title"])}</a></div>')
    rep_html = "\n".join(rep_rows) or "<p>No weekly reports yet.</p>"

    body = f"""
<h1>Weekly grievance-redress audits</h1>
<div class="updated">India-wide weekly audit of passenger complaints and visible agency replies on X — acknowledgement is not a fix; we track whether anything was actually resolved.</div>
<div class="card"><strong>How is this made?</strong> A scheduled agent searches a published watchlist, and improves its own detection through a versioned, reviewed process. <a href="how.html">Read the methodology →</a></div>
<section class="brief-list">
{rep_html}
</section>
"""
    (REPORTS / "index.html").write_text(
        page("Weekly Grievance-Redress Audits · UngalSoththu — உங்கள் சொத்து",
             "India-wide weekly transit grievance-redressal audit — "
             "complaints, agency replies, fixes shown.",
             body),
        encoding="utf-8")


def main() -> None:
    briefs, reports = sync_and_render()
    build_briefs_index(briefs)
    build_reports_index(reports)
    build_method()
    print(f"built: {len(briefs)} briefs, {len(reports)} reports, method page -> {PUBLIC}")


if __name__ == "__main__":
    main()
