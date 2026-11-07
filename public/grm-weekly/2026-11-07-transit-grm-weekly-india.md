# 🚌 Weekly India Transit Grievance Redressal Audit

[INDIA-TRANSIT] [MTC] [CMRL] [SR] [CUMTA] [TNSTC] [SETC] [BEST] [BMTC] [DTC] [KSRTC]

**Window:** 31 October 2026, 09:00 IST – 7 November 2026, 09:00 IST  
**Scope:** Ten configured agencies; X-visible passenger grievances and direct visible agency replies. Searches followed `site/detection/grm-detection.json` v1.2: current/history handles plus configured broad-name searches, plus reply-side sweeps (`from:` handle) after zero-result smells. Follow-ups and commentary merged into parent incidents; agency replies never counted as complaints.  
**Result:** **46 distinct complaints; 27 got a visible agency reply (59%); 1 confirmed resolution (DTC fined a driver ₹200 after investigation).** X API rate limits repeatedly blocked thread fetches, so three agencies (SR, BMTC, DTC) carry reply-evidenced complaint threads whose original post text could not be retrieved — these are counted as distinct incidents (unique conversation roots / named parents) and flagged content-unverified. Deepavali week (festival on ~8 Nov) drove a wave of TNSTC/SETC app payment failures and crowded-service complaints. X date filters work at day granularity; every counted post's timestamp was decoded from its snowflake ID and verified inside the window.

## Findings by agency

### MTC Chennai — @MtcChennai
**Complaints:** 4 · **Replies:** 4 (100%) · **Response time:** 2 minutes–15 hours 27 minutes; median about 1 hour 27 minutes.  
**Categories:** route/frequency (2), delay (1), breakdown/maintenance (1).

- Route 570S AC bus (CDK 5516) Karapakkam–Koyambedu: passengers paid AC fare but the bus was sweltering; rider claims all AC buses are the same. MTC replied in 2 minutes: forwarded to depot for inspection, crew instructed on cooling. No outcome verified. [Complaint](https://x.com/arun_skm/status/2116394421008949672) · [reply](https://x.com/MtcChennai/status/2116394925688570148) — ❌
- M1 services from Keelkattalai and Thiruvanmiyur bunching "like a train", hour-long gaps; rider says repeated complaints brought no improvement. MTC replied ~15 h 27 m later: bunching noted, depot officials to monitor scheduling. [Complaint](https://x.com/HARIHARANMULTI1/status/2117208351327031517) · [reply](https://x.com/MtcChennai/status/2117441848008646729) — ❌
- Route 102 (CDK 5564) held ~20 min outside TCS Gate 1 on a flimsy "gap for bus ahead" excuse while another 102 AC overtook; crew laughed off passenger concerns. MTC replied in 19 minutes: driver/conductor to be enquired. [Complaint](https://x.com/v_siddhesh/status/2117572832377151956) · [reply](https://x.com/MtcChennai/status/2117577673040118242) — ❌
- S70K Korattur canal-road route: frequency collapsed to 2–3 hour waits after free travel for women; timings controlled arbitrarily, GPS switched off, no depot oversight. MTC replied in 2 h 34 m: depot officials to be taken up, instructions for regular service and monitoring. [Complaint](https://x.com/devishree_g/status/2117856942463091071) · [reply](https://x.com/MtcChennai/status/2117895801955561553) — ❌

### CMRL Chennai Metro — @cmrlofficial
**Complaints:** 0 · **Replies:** 0 · **Response rate:** N/A.

Current/legacy handle and broad searches surfaced no qualifying first-hand passenger grievance. The window contained one real, documented service failure — the **3 Nov evening peak AFC/ticketing blackout** (gates and counter printers down ~1 hour, riders stranded inside stations) — but every X post about it was a news summary or media link (DT Next), not a first-hand complaint; one unanchored grievance ("they sent a reply to look considerate but nothing happened") named no specific failure and was excluded. @cmrlofficial posted Diwali service extensions and promo content in-window and replied to an unrelated housekeeping complaint, but to no counted grievance. Handle is clearly live; the zero is genuine, not a stale watch.

### Chennai Suburban & MRTS — @DrmChennai
**Complaints:** 5 · **Replies:** 5 (100%) · **Response time:** 37–58 minutes for three; 2 h 25 m for one; 1 undecodable (parent not captured).  
**Categories:** other/unclassified (5) — parent texts not retrievable within rate limits.

The complaint-side searches returned zero raw grievances, but the reply-side sweep found @DrmChennai replying to five distinct passenger complaint threads in-window — the zero-complaint check did its job. Four parents are pinned by conversation ID (roots of 1 Nov, 3 Nov, 4 Nov, 5 Nov); one further reply ("train delayed but NOT diverted") answers a fifth complaint whose root was not captured. All replies are the standard "we regret… escalated to the concerned department" template; none confirms an outcome. DRM also replied on 4 Nov to a 24 Sep thread — out-of-window parent, not counted. [Reply 1](https://x.com/DrmChennai/status/2116686121535152469) · [Reply 2](https://x.com/DrmChennai/status/2117568838820913541) · [Reply 4](https://x.com/DrmChennai/status/2117950469255639282) · [Reply 5](https://x.com/DrmChennai/status/2118353572555624460) · [delay-not-diverted reply](https://x.com/DrmChennai/status/2117479901108621820) — ❌ (all)

### CUMTA — @CumtaOfficial
**Complaints:** 0 · **Replies:** 0 · **Response rate:** N/A.

Only the audit's own @UngalSoththu accountability threads surfaced under CUMTA/Chennai-transit searches; those are our published commentary, not passenger grievances, and were excluded (rule added to config this week). No passenger tagged @CumtaOfficial with a specific service failure. No replacement handle indicated.

### TNSTC (statewide) — shared candidate @tnstc_setc
**Complaints:** 2 · **Replies:** 0 (0%). **Categories:** fare/ticketing (2).

- Payment succeeded in the TNSTC app for Tiruppur→Thiruthuraipoondi but no ticket or confirmation was issued. No response. [Post](https://x.com/DieHardFanOfTh4/status/2118762599773020516) — ❌
- Vellore→Kumbakonam booked via Paytm through the app: money debited, ticket cancelled, no redress. No response. [Post](https://x.com/writterBB/status/2118767075598746067) — ❌

Two passengers hit the same payment-capture failure ~17 minutes apart on Deepavali-eve booking night; together they suggest a systemic payment glitch, but each is counted as its own incident.

### SETC — shared candidate @tnstc_setc
**Complaints:** 2 · **Replies:** 0 (0%). **Categories:** breakdown/maintenance (1), fare/ticketing (1).

- SETC fleet condition: "zero maintenance", video of bus interior, no new AC sleeper-seater purchased in eight years. Unverified allegation but backed by posted video evidence. [Post](https://x.com/gkez0102/status/2118878549855928583) — ❌
- Booked SETC bus dispatched wrong, and the substitute bus's AC was not working, during Deepavali travel. [Post](https://x.com/VelkuttyTweets/status/2118837881078992921) — ❌

**Handle caveat (unchanged):** the shared candidate account's bio refers to TNSTC/SETC but official status is not independently verified; it posted no authored replies in-window. Both TNSTC and SETC went 0-for-2 during the festival rush.

### BEST Mumbai — @myBESTBus
**Complaints:** 4 · **Replies:** 3 (75%) · **Response time:** 25 minutes–21 hours 27 minutes.  
**Categories:** staff conduct (1), breakdown/maintenance (1), other/unclassified (2).

- A Chalo Bus driver abandoned the vehicle mid-street for ~30 minutes with doors shut and walked away; rider asks who would have been responsible in a fire. No BEST reply. [Post](https://x.com/ManasJoshi/status/2118382499802046810) — ❌
- Depot-fleet thread: 13 of 30 buses reportedly unfit (battery/tyre issues) with the driver contractor untraceable; BEST forwarded the parent complaint to the concerned HOD in 12 h 3 m — a forward, not a resolution. The dtrivedi96 commentary post is merged into this same incident. [Parent root](https://x.com/i/status/2117998719111172357) (author not captured) · [BEST forward](https://x.com/myBESTBus/status/2118180714495766822) · [commentary merged](https://x.com/dtrivedi96/status/2118011208615993615) — ❌
- Two further distinct complaint threads (roots 3 Nov and 4 Nov) received BEST forwards ("concerned HOD"/"concerned Authority"); parent texts not retrievable within rate limits. [Forward A](https://x.com/myBESTBus/status/2117812506714599512) · [Forward B](https://x.com/myBESTBus/status/2117811962361114833) — ❌ (both)

### BMTC Bengaluru — @BMTC_BENGALURU
**Complaints:** 14 · **Replies:** 8 (57%) · **Response time:** 55 minutes–14 hours 16 minutes; median about 5 hours.  
**Categories (verified content):** safety/accessibility (2), fare/ticketing (1), delay (1), crowding (1), staff conduct (1), breakdown/maintenance (1), other/unclassified (7 content-unverified docket threads).

Verified first-hand complaints (six, none replied in-window):
- AC bus not cooling despite fare hike — crew and driver unwilling to run cooling. [Post](https://x.com/Iamaninas/status/2118593919378448735) — ❌
- Reckless driving injured two women riders at separate stops; staff blamed the women. [Post](https://x.com/willowscx/status/2118624883559272607) — ❌
- Route 143: ticketing machine fault, conductor refusing male passengers, skipping Johnson Market stop in pouring rain. [Post](https://x.com/BrindaAdige/status/2118657285266563402) — ❌
- Route 500CA Kundalahalli–Bellandur: 25-minute trip stretched to 45 by idle stops, mid-route ticketing and rash driving. [Post](https://x.com/Manan_13/status/2118277543208046780) — ❌
- Daily commute: buses overcrowded to the point of riders hanging at doors, plus 35% fare increase. Underspecified; flagged unverified. [Post](https://x.com/TheRubric_Medic/status/2117902561470787767) — ❌
- Conductor refused to help after a phone-theft incident, blocked calling 112, rider forced to visit the police station in person; follow-up says BMTC ignored CCTV request. [Thread](https://x.com/madvish_/status/2117610345292542410) — ❌

Docket-verified threads (eight distinct conversations; BMTC acknowledged each with a docket within ~1–14 h; no closure visible):
- Emergency exit missing and walkway narrowed on bus KA57F0327 — docket BMTC2026018065 in 3 h 25 m. [Complaint](https://x.com/ManjunathMadiw9/status/2118345614467744061) · [docket](https://x.com/BMTC_BENGALURU/status/2118397283335290910) — ❌
- Seven further distinct docketed threads (dockets BMTC2026017714/766/769/7812/7905/8002/8005), parent texts unretrievable. [Docket replies](https://x.com/BMTC_BENGALURU/status/2116908858061058289) · [..769](https://x.com/BMTC_BENGALURU/status/2117207230378623206) · [..7905](https://x.com/BMTC_BENGALURU/status/2117840690889847287) · [..8002](https://x.com/BMTC_BENGALURU/status/2118230533906026601) · [..8005](https://x.com/BMTC_BENGALURU/status/2118235266968441018) — ❌ (all)
- BMTC also asked one complainant for date/time details and promised crew education in two further in-window replies whose parents were not captured.

### DTC Delhi — @dtchq_delhi
**Complaints:** 15 · **Replies:** 7 (47%) · **1 confirmed resolution.**  
**Categories:** route/frequency (8), staff conduct (3), fare/ticketing (3), breakdown/maintenance (1).

Verified first-hand complaints (eight, none replied in-window):
- Driver refused to open the gate, abused the rider's mother, conductor refused the complaint book; bus DL1PD4888, route 113. [Post](https://x.com/iamppsharma/status/2118743917659308218) — ❌
- Route 463 app ticketing offers no Mehrauli Terminal option; rider forced to travel without a ticket. [Post](https://x.com/Sachin_Writer17/status/2118389846100320652) — ❌
- Bus pass applied but not issued. [Post](https://x.com/Umesh98038793/status/2118289593372127476) — ❌
- Conductor refused UPI ticket and threatened the rider on board DL1PD5522. [Post](https://x.com/tiknasingh/status/2118173082942914907) — ❌
- ₹2,850 refund sought for a duplicate e-bus pass application (ID 7527102680298) stuck in processing delays. [Post](https://x.com/sanatani919/status/2117922723494277260) — ❌
- Conductor without uniform, allegedly drunk, took money without issuing ticket on DL1PD4962; video attached. Unverified allegation. [Post](https://x.com/Delhikiawaaj/status/2117919834633871796) — ❌
- Same-number buses bunching then a 40-minute gap; driver drove past waving passengers despite the app showing 5 minutes. Operator (DTC vs cluster) not named; retained as Delhi city-bus grievance flagged unverified-operator. [Post](https://x.com/ojhaanjali/status/2116890536431026523) — ❌
- DTC bus breakdown mid-Delhi Cantt, passengers stranded, routes curtailed. [Post](https://x.com/AshishXL/status/2118007625426321512) — ❌

Reply-verified complaints (seven; all answered in DTC's 6 Nov reply batch):
- Route 118 bus DL1PD7254 skipped Netaji Subhash Marg stand: DTC investigated and **imposed a ₹200 penalty on the driver** — the week's only confirmed resolution. [Reply](https://x.com/dtchq_delhi/status/2118641065142182224) — ✅
- Route 424 bus DL51GD9209 did not stop at FA stand despite passengers signalling: GPS/BMS investigation, driver counselled, disciplinary action initiated, penalty on concessionaire promised — action begun, not closed. [Reply](https://x.com/dtchq_delhi/status/2118608233925579083) — ❌
- Route 833/6 bus 5507 not stopping properly: driver ID identified, strict instructions issued, warning recorded. [Reply](https://x.com/dtchq_delhi/status/2118678904865177995) — ❌
- OMS route service sufficiency: DTC answered with scheduled service counts (45+/43−) and said extra buses may be considered later — request not acceded. [Reply](https://x.com/dtchq_delhi/status/2118713048538177541) — ❌
- Route 605 frequency, route D-9905 services, route 729 driver action: three further DTC replies in-window; gist-level detail only. — ❌

### KSRTC Kerala — @keralasrtc
**Complaints:** 0 · **Replies:** 0 · **Response rate:** N/A.

The handle is live (account ID 183629311, bio "Kerala State Road Transport Corporation") but posted nothing findable in-window. Broad KSRTC searches returned almost entirely **Karnataka** KSRTC noise (Tumakuru consumer-case news, Airavat sleeper complaints, V Kaveri cancellations) — all excluded on agency mismatch. Kerala news posts (consumer-court fine of ₹45,000 over a passenger injury; seat-reallocation case) are court/news items, not in-window X grievances, and were excluded. One account, @srdmekur1, replies to KSRTC complaints in official tone ("transferred to higher official for investigation") — flagged as a candidate official-adjacent handle to verify next week rather than counted.

## Cross-agency notes

- **Shared handle:** TNSTC/SETC searched once per config; incidents attributed by named operator; nothing left unassigned.
- **Own-account exclusion:** @UngalSoththu accountability threads surfaced in five agencies' searches; excluded from all counts (new config rule).
- **Rate-limit caveat:** X API 429s blocked most thread fetches; three agencies carry content-unverified, reply-evidenced incidents. The counts above are floors, not totals.
- **Window boundary:** the earliest counted post (MTC 570S) posted 31 Oct 10:28 IST, inside the window; a DRM reply to a 24 Sep thread was excluded as out-of-window.

## Detection update (v1.2 → v1.3)

- **Reply-side sweep mandated every week** (new search pattern `from:{handle}`): this week the complaint-side searches read zero for Chennai Suburban while the reply-side sweep proved five live complaint threads — the single biggest undercount risk in the method.
- **Own-account posts and news-only reposts added to the exclude list**, codifying this week's two judgment calls (UngalSoththu threads; the 3 Nov CMRL AFC blackout that appeared only via news summaries).
- **Karnataka-vs-Kerala KSRTC disambiguation note** added after Karnataka brands (Airavat, V Kaveri, Tumakuru venue) polluted Kerala searches; @srdmekur1 logged as a candidate handle to verify.
- Eval set unchanged: all 13 labeled complaint cases still classify with the same agency and category under v1.3 rules, and all three known-miss drills still reproduce (obsolete Kerala handle returns zero; MTC legacy-tag thread recoverable; praise + feature request excluded). The changes are additive exclusions/patterns only — no handle or category edits.

## Metrics summary

| Agency | Complaints | Replies | Rate | Confirmed resolved |
| --- | --- | --- | --- | --- |
| MTC Chennai | 4 | 4 | 100% | 0 |
| CMRL | 0 | 0 | N/A | — |
| Chennai Suburban/MRTS | 5 | 5 | 100% | 0 |
| CUMTA | 0 | 0 | N/A | — |
| TNSTC | 2 | 0 | 0% | 0 |
| SETC | 2 | 0 | 0% | 0 |
| BEST Mumbai | 4 | 3 | 75% | 0 |
| BMTC Bengaluru | 14 | 8 | 57% | 0 |
| DTC Delhi | 15 | 7 | 47% | 1 |
| KSRTC Kerala | 0 | 0 | N/A | — |
| **Total** | **46** | **27** | **59%** | **1** |
