# EU Employment Law Layer — lookup

**As of 2026-08-22.** Lookup reference for the EU-law overlay on German employment-contract assessment (German statutory layer lives in `statutes.md`; case-law whitelist in `case-law.md`). Every directive block carries its German transposition vehicle, status flag, and source URL. Transposition status and figures were verified by web search against EUR-Lex, gesetze-im-internet.de, Bundestag documents, and practitioner commentary on 2026-08-22. This is a research reference, not legal advice.

**Top-line status flags (2026-08):**
- **Pay Transparency (EU) 2023/970** — deadline 7.6.2026 **missed**; no German statute. Binding on public employers since 8.6.2026 (vertical direct effect); private employers: Art. 157 TFEU + conforming interpretation; Art. 7(6) pay-secrecy clauses void.
- **Platform Work (EU) 2024/2831** — deadline 2.12.2026; Referentenentwurf in preparation (BMAS), no public draft.
- **Minimum Wage (EU) 2022/2041** — **partially annulled** by CJEU C-19/23 (11.11.2025); Art. 5(2)/(4) void; Art. 4 upheld; MiLoG unaffected (€13.90 from 1.1.2026, €14.60 from 1.1.2027).
- **ArbZG reform** — new Referentenentwurf circulating since ~June 2026 ("interne Arbeitsfassung"); **not enacted**; § 3 ArbZG 8h daily cap unchanged.
- **July-2026 coalition package** ("Aufschwung und Beschäftigung") — political agreement of 1.7.2026 only; **no bill introduced**; flag `law_in_flux`, never apply.

---

## 1. Directive → transposition table

| Directive | German vehicle | Status | Notes |
|---|---|---|---|
| 2003/88/EC working time | ArbZG | transposed (stricter) | DE daily cap 8h (§ 3) exceeds EU 48h weekly average (Art. 6); no individual opt-out (Art. 22 not transposed) |
| 97/81/EC part-time framework | TzBfG | transposed | § 4 non-discrimination, § 5 pro-rata, § 8 hours-reduction right |
| 99/70/EC fixed-term framework | TzBfG | transposed | § 14(1) objective reason; § 14(2) 2 years/3 renewals + Vorbeschäftigungsverbot; CJEU abuse doctrine constrains chains |
| (EU) 2019/1152 transparent & predictable conditions | NachwG 2022 (+ TzBfG §§ 7(3), 12(3), 15(3); § 111 GewO) | transposed (in force 1.8.2022) | Germany stricter: paper form kept; no explicit exclusivity-clause ban (Art. 9 via §§ 138/242/307 BGB only) |
| 2000/78/EC employment framework | AGG | transposed | religion, disability, age, sexual orientation |
| 2000/43/EC racial equality | AGG | transposed | race/ethnic origin |
| 2006/54/EC gender equality (recast) | AGG | transposed | equal pay, pregnancy/maternity |
| 96/71/EC + (EU) 2018/957 posted workers | AEntG | transposed | § 16 notification, § 23c info duty; host-state minima day 1; ≥12 (extendable 18) months → all host terms |
| 2001/23/EC transfer of undertakings | § 613a BGB | transposed | CJEU C-396/07, C-561/11 bind interpretation |
| (EU) 2016/679 GDPR | § 26 BDSG | directly applicable (gap) | § 26(1) general clause insufficient for special-category data post-C-34/21 |
| (EU) 2019/1937 whistleblowing | HinSchG | transposed (in force 2.7.2023) | § 39: agreements restricting reporting rights void |
| (EU) 2022/2041 adequate minimum wages | MiLoG | **partially annulled** | C-19/23: Art. 5(2)/(4) void; MiLoG stands |
| (EU) 2023/970 pay transparency | EntgTranspG | **not transposed** (deadline missed) | directive bites from 8.6.2026 via direct effect (public) + conforming interpretation (private) |
| (EU) 2024/2831 platform work | pending | **not transposed** (deadline 2.12.2026) | Art. 5 presumption of employment; BMAS drafting |

---

## 2. Directive blocks

### 2.1 Working time — Directive 2003/88/EC → ArbZG

- **Key provisions:** max weekly average 48h incl. overtime (Art. 6); min daily rest 11 consecutive hours (Art. 3); min weekly rest 35h incl. daily rest (Art. 5); breaks (Art. 4); at least 4 weeks paid annual leave (Art. 7(1)). Legal basis Art. 153(1)(a) TFEU.
- **German implementation:** ArbZG § 3 max 8h/day, extendable to 10h if average over 6 months/24 weeks ≤8h (EU 48h weekly average floors German law; German daily cap is stricter). § 4 breaks; § 5 11h rest; § 6a night work; § 7 collective-agreement derogations, bounded by EU minimums.
- **Recording (C-55/18):** BAG 13.9.2022 (1 ABR 22/21) derives the employer's time-recording duty from § 3(2)(1) ArbSchG — all employers, all employees; electronic recording not mandated by BAG. Contract clauses excluding recording ("Vertrauensarbeitszeit ohne Erfassung") invalid in practice.
- **Status flag:** ArbZG reform draft (June 2026) not enacted; EU floor (Art. 6 48h average, Art. 3 11h rest) unchanged; see § 3.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003L0088 · ArbZG `https://www.gesetze-im-internet.de/arbzg/`

### 2.2 Part-time & fixed-term — Directives 97/81/EC and 99/70/EC → TzBfG

- **Key provisions:** part-time framework clause 4 non-discrimination vs comparable full-timer; fixed-term framework clause 5 measures against successive-contract abuse, clause 4 non-discrimination.
- **German implementation:** TzBfG § 2 (part-time definition), § 4(1) (non-discrimination), § 5 (pro-rata pay/benefits), § 7 (change-of-hours request; since 1.8.2022 reasoned written reply within 1 month), § 8 (hours reduction, >15 employees, deemed grant § 8(5)), § 9 (return to longer hours), § 14(1) objective justification, **§ 14(2)** fixed term without objective reason up to **2 years, max 3 renewals**, only without prior employment with the same employer (**Vorbeschäftigungsverbot**, § 14(2) s. 2).
- **CJEU abuse doctrine (applies to chains and by analogy to any reform):** C-212/04 Adeneler — national courts must convert successive fixed-term contracts into indefinite ones and interpret national law to prevent abuse; C-574/16 Grupo Norte — court must verify misuse ex officio and apply effective sanctions. No CJEU ruling directly on § 14(2) TzBfG as of 2026-08; BAG upholds its compatibility with clause 5 (e.g. BAG 26.10.2016 – 7 AZR 140/15; BAG 23.1.2019 – 7 AZR 733/16). July-2026 package's planned 48-month/6-renewal rule would be assessed against clause 5 — a CJEU challenge is foreseeable.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31997L0081 · https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31999L0070 · TzBfG `https://www.gesetze-im-internet.de/tzbfg/`

### 2.3 Transparent & predictable working conditions — Directive (EU) 2019/1152 → NachwG (2022)

- **Key provisions:** written statement of essential conditions (Art. 3), change notification (Art. 4), probation cap 6 months (Art. 6), ban on exclusivity clauses (Art. 9), predictability (Art. 10), free mandatory training (Art. 13), enforcement (Art. 18). Transposition deadline 1.8.2022.
- **German implementation (in force 1.8.2022, BGBl. I 2022 S. 1170):**
  - § 2(1) NachwG — expanded mandatory documentation (paper form retained; electronic form option of Art. 3(2) deliberately not used): 15 items incl. itemized pay composition, overtime, bonuses/allowances/special payments, due date and method (item 7); agreed working time, breaks, shift system (item 8); on-call work per § 12 TzBfG (item 9).
  - § 2(1) s. 4 deadlines: items 1, 7, 8 by **first day of work**; items 2–6, 9, 10 within **7 calendar days**; items 11–15 within **1 month**. Changes: § 3 NachwG on the day they take effect.
  - § 4 NachwG — fine up to **€2,000** for non/incorrect/incomplete/late documentation; § 4 s. 1 Beweislastumkehr (undocumented terms presumed as asserted).
  - § 2(2)/(3) — postings abroad >4 consecutive weeks: country, duration, currency, allowances, return conditions; posting per Directive 96/71/EC as amended: host-state remuneration + link to official national website.
  - § 23c AEntG (new) — information duty for recruiting EU citizens resident abroad ("Faire Mobilität").
  - TzBfG amendments: § 7(3) reasoned reply within 1 month (also § 18(2) for indefinite-contract request, >6 months employment); § 12(3) reference days/hours mandatory + 4-day advance notice; § 15(3) probation proportionate to fixed-term duration.
  - § 111 GewO / § 32a SeeArbG — mandatory training costs not chargeable to employee; counts as working time outside regular hours.
- **Exclusivity clauses (Art. 9):** no explicit German statutory ban; implemented only via contractual freedom limits (§§ 138, 242, 307 BGB; BAG 18.11.1988 – 8 AZR 12/86; BAG 11.12.2001 – 9 AZR 464/00). Absolute exclusivity bans without objective justification fail AGB review — flag, but they are not per se void.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1152 · NachwG `https://www.gesetze-im-internet.de/nachwg/`

### 2.4 Anti-discrimination — Directives 2000/78/EC, 2000/43/EC, 2006/54/EC → AGG

- **Key provisions:** 2000/78 employment framework (religion, belief, disability, age, sexual orientation); 2000/43 racial/ethnic origin; 2006/54 gender in employment incl. equal pay and pregnancy/maternity (Art. 2(2)(c)).
- **German implementation:** AGG § 1 grounds, § 7 prohibition incl. contractual terms, **§ 22 burden of proof** (employee establishes prima facie indicia; employer proves no discrimination), § 15 compensation (up to 3 monthly salaries for non-hiring, uncapped otherwise), § 16 no retaliation.
- **Drafting impact:** dress-code/grooming clauses must be neutral on their face and objectively justified; religion-specific bans directly discriminatory (C-157/15 Achbita, C-68/17 JR); any clause/practice disadvantaging pregnant employees void (C-177/88 Dekker + AGG § 7, MuSchG); age limits need documented legitimate aim + proportionality (AGG § 10; C-144/04, C-411/05, C-341/08, C-388/07).
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32000L0078 · https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32000L0043 · https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0054 · AGG `https://www.gesetze-im-internet.de/agg/`

### 2.5 Data protection in employment — GDPR + § 26 BDSG

- **Key provisions:** GDPR directly applicable; Art. 88 GDPR + Art. 7 consent conditions. German implementing provision § 26 BDSG (processing for employment-relationship purposes; necessity or consent per Art. 7 GDPR/§ 26(2) BDSG).
- **CJEU constraints on contract clauses:**
  - **C-34/21 (ÖGK, 30.3.2023):** Art. 88(1) GDPR — national provisions on employee health data must be sufficiently specific; § 26(1) BDSG as general clause **cannot** justify special-category (health) data processing; consent/works-agreement basis alone insufficient for health data.
  - **C-439/19 (B, 22.6.2021)** — **the biometric-data case:** special-category data under Art. 9(2)(b) GDPR requires explicit consent and a national legal basis establishing necessity; employer biometric systems (time recording, access control) need explicit, free consent under Art. 9(2)(a) GDPR + § 26(2) BDSG, and German supervisory authorities treat them as high-risk (Art. 35 GDPR DPIA).
  - **C-61/19 (Orange România, 11.11.2020)** — consent validity for retention of ID copies; pre-ticked/annexed consent not freely given. Applied to employment: consent embedded in contract documents is suspect; monitoring clauses relying on contract consent alone are weak.
- **Drafting impact:** monitoring clauses (video, e-mail, GPS, keylogging) need concrete necessity + transparency + usually works agreement (BAG 29.6.2017 – 2 AZR 597/16; proportionality balancing per BVerfG 4.4.2006 – 1 BvR 518/02); consent clauses must be unbundled and voluntary (EDPB Guidelines 5/2020: imbalance of power presumed in employment); whistleblower data processing per HinSchG § 10, not GDPR consent.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679 · BDSG `https://www.gesetze-im-internet.de/bdsg_2018/__26.html` · C-439/19 https://dejure.org/dienste/vernetzung/rechtsprechung?Aktenzeichen=C-439%2F19&Datum=22.06.2021&Gericht=EuGH

### 2.6 Adequate minimum wages — Directive (EU) 2022/2041 → MiLoG

- **Key provisions:** framework for adequacy of statutory minimum wages (Art. 5) and promotion of collective bargaining (Art. 4; coverage target ≥80%). In force 14.11.2022; transposition deadline 15.11.2024.
- **CJEU 11.11.2025, C-19/23 (Denmark v Parliament and Council):** directive **partially annulled** — **Art. 5(2) and Art. 5(4) void** (binding criteria for setting/updating statutory minimum wages: purchasing power, wage level/distribution, growth rates, productivity) for lack of competence under Art. 153(5) TFEU ("pay" excluded). Rest of directive valid; Art. 4 (collective bargaining promotion) upheld.
- **German effect:** MiLoG stands independently; Mindestlohnkommission: **€13.90/h from 1.1.2026, €14.60/h from 1.1.2027** (Cabinet decision 29.10.2025). Collective-bargaining coverage ~49% west/~44% east [unverified exact figure; IAB]; the 80% target is not binding on Germany after C-19/23.
- **Status flag:** do **NOT** cite Art. 5 criteria as binding.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2041 · LTO https://www.lto.de/recht/hintergruende/h/eugh-c1923-urteil-eu-mindestlohn-richtlinie-teilweise-unwirksam · Bundestag WD paper https://www.bundestag.de/resource/blob/1127460/urteil-eugh-mindestlohnrichtlinie.pdf · BMAS https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/mindestlohn-steigt-zum-ersten-januar-2026.html

### 2.7 Posted workers — Directive 96/71/EC as amended by (EU) 2018/957 → AEntG

- **Key provisions (2018/957, in force 30.7.2020):** posting ≥12 months (extendable 6) → all applicable host-state terms; equal pay for posted workers (host-state minimum wages incl. statutory and universally applicable collective agreements); subcontracted-chain liability; administrative controls (A1, notification).
- **German implementation:** AEntG §§ 1–7 (working conditions incl. minimum wage and extended collective agreements by Rechtsverordnung under § 7), §§ 8–11 (social security), § 16 posting notification (before start; 4-week validity), § 23c (2022) information duty to EU citizens recruited abroad; NachwG § 2(2)/(3) posting documentation.
- **Cross-border law:** Rome I Art. 8/9 and Brussels Ia Arts. 20–23 — see § 5.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01996L0071-20200730 · AEntG `https://www.gesetze-im-internet.de/aentg/`

### 2.8 Platform work — Directive (EU) 2024/2831 → pending

- **Key provisions:** in force 1.12.2024; transposition **2.12.2026**. **Art. 5: rebuttable presumption of employment relationship** where the platform controls working conditions (covers self-employed and employees); algorithmic management transparency (Arts. 6–12: information, human review of significant decisions, limits on automated monitoring/decision-making for personal data; workers' representatives rights); subcontractor-chain measures (Art. 3).
- **German status (2026-08):** BMAS preparing Referentenentwurf (Bundestag answer 24.4.2026, hib 344/2026); **no published draft**; government examining Art. 3 measures incl. possible direct-employment obligation (Direktanstellungsgebot) for delivery platforms. Deadline 2.12.2026 likely missed or met at the last minute. Presumption will interact with § 611a BGB status testing and BAG crowdworker case law.
- **Status flag:** `law_in_flux` — pending; do not assess contracts against the presumption as binding German law before transposition.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2831 · Bundestag hib 344/2026 https://www.bundestag.de/presse/hib/kurzmeldungen-1167478 · Gleiss Lutz https://www.gleisslutz.com/de/know-how/update-eu-richtlinie-zur-verbesserung-der-arbeitsbedingungen-der-plattformarbeit-kraft…

### 2.9 Whistleblowing — Directive (EU) 2019/1937 → HinSchG

- **Key provisions:** deadline 17.12.2021 (extended to 17.12.2023 for <250 employees); protection against retaliation, internal/external reporting channels.
- **German implementation:** HinSchG in force 2.7.2023. § 1 personal scope; § 2 material scope (EU-law violations; after 17.12.2023 extended to federal/national law [BVerfG partial suspension of that extension to constitutional-law violations reported — case number unverified `[unverified]`]); § 3(6) retaliation definition; **§ 36 burden of proof** (presumption of retaliation); **§ 39: agreements restricting whistleblower rights are void** — voids confidentiality clauses barring reports; § 37(1) retaliation prohibited; §§ 12–18 internal reporting channels (employers 50+ employees mandatory).
- **Drafting impact:** clauses obliging confidentiality "in all circumstances", gag clauses in settlement agreements, or clauses penalizing reports are **void per § 39 HinSchG**.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1937 · § 39 HinSchG https://www.gesetze-im-internet.de/hinschg/__39.html · § 3 HinSchG https://www.gesetze-im-internet.de/hinschg/__3.html · ADVANT Beiten https://www.advant-beiten.com/aktuelles/schweigsame-hinweisgeber-auswirkungen-des-hinweisgeberschutzgesetzes-auf-vertraulichkeitsvereinbarungen

### 2.10 Pay transparency — Directive (EU) 2023/970 → NOT transposed

- **Key provisions** (in force 6.6.2023; **transposition deadline 7.6.2026**): Art. 4 gender-neutral pay structures; Art. 5 **pay-range disclosure in job ads and before interview**; Art. 6 no questions about previous pay; Art. 7 right to information on pay levels (median) of comparator group + **Art. 7(6): agreements restricting disclosure of one's own pay are void/unenforceable**; Art. 8 reporting (≥250 employees annually; 150–249 every 3 years; 100–149 every 3 years); Art. 9 joint pay assessments (gap ≥5% unjustified); Art. 10 equal-work/equal-value comparison; Art. 13 burden of proof shifts on indicia.
- **German status (2026-08, memo wins):** deadline **missed**; no Referentenentwurf as of late May 2026; no statute by 2026-08. Existing law: EntgTranspG (2017) — § 3 prohibition, § 4 equal pay, §§ 10 ff. individual information right (only >200 employees, every 3 years), § 4(5) presumption of adequacy for collective-agreement pay, §§ 17 ff. reporting (500+).
- **Effect from 8.6.2026 without transposition:**
  - **Public employers (all state subdivisions, public-law bodies, state-owned companies with special powers): directly bound** by sufficiently precise directive provisions (vertical direct effect).
  - **Private employers:** no horizontal direct effect; but Art. 157 TFEU equal-pay principle applies horizontally; courts must interpret EntgTranspG/AGG/BGB/BetrVG/TVG conformingly; Art. 4 criteria become the interpretive yardstick; § 22 AGG burden read employee-favorably; **Art. 7(6) used to strike pay-secrecy clauses via § 307 BGB**; BAG 23.10.2025 – 8 AZR 300/24 ("Paarvergleich") shows lowered hurdles.
  - **Organizational duties (Art. 5 ad disclosure, Art. 8 reporting, Art. 9 joint assessments) cannot be created by judicial interpretation** — they await legislation (realistic earliest national act end-2026/2027).
- **Drafting impact (contract offers):** salary bands in job ads; no prior-pay questions; no pay-secrecy clauses; documentation of pay decisions; comparison-group transparency.
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L0970 · PWWL https://pwwl.de/eu-entgelttransparenzrichtlinie-ab-dem-8-juni-2026-was-gilt-auch-ohne-deutsches-umsetzungsgesetz/ · Kliemt (memo source) https://kliemt.blog/2026/05/26/keine-puenktliche-etrl-umsetzung-in-deutschland-was-gilt-ab-7-juni-2026 · Deloitte https://www.deloitte.com/de/de/services/tax/perspectives/eu-entgelttransparenzrichtlinie.html · Personio https://www.personio.de/hr-lexikon/entgelttransparenzgesetz/ · reteach https://www.reteach.com/eu-entgelttransparenzrichtlinie-2026/ · afa-anwalt https://www.afa-anwalt.de/news/entgelttransparenzgesetz-2026-rl-2023-970/

---

## 3. Transposition-status flags (pinned — every assessment output must carry "as of YYYY-MM-DD")

1. **Pay Transparency (EU) 2023/970 — deadline missed.** No statute by 2026-08. From 8.6.2026: directly binding on public employers; private employers: Art. 157 TFEU horizontal effect + conforming interpretation; Art. 7(6) pay-secrecy clauses void → strike via § 307 BGB; Art. 4 becomes the interpretive yardstick for pay structures; ad pay-range disclosure (Art. 5), prior-pay questions ban (Art. 6), reporting (Art. 8), joint assessments (Art. 9) await legislation.
2. **Platform Work (EU) 2024/2831 — deadline 2.12.2026.** No published draft as of 2026-08 (BMAS preparing; Direktanstellungsgebot under discussion). Art. 5 presumption of employment will interact with § 611a BGB status testing. `law_in_flux`.
3. **Minimum Wage (EU) 2022/2041 — partially annulled.** CJEU C-19/23 (11.11.2025): **Art. 5(2)/(4) void** (pay excluded from EU competence, Art. 153(5) TFEU); Art. 4 collective-bargaining promotion upheld; MiLoG unaffected (€13.90/€14.60 trajectory stands). Do **NOT** cite Art. 5 criteria as binding.
4. **ArbZG reform — announced June 2026, not enacted.** New Referentenentwurf ("interne Arbeitsfassung"): electronic recording of Beginn/Ende/Dauer as default (§ 16(2) ArbZG-E), weekly cap only via Tarifvertrag parties (§ 7(1) Nr. 1b ArbZG-E), fines up to €30,000, transition periods 1–5 years by company size. **§ 3 ArbZG 8h daily cap unchanged and in force**; EU floor (Art. 6 48h weekly average, Art. 3 11h rest) unchanged; BAG recording duty stands on ArbSchG. `law_in_flux`.
5. **July-2026 coalition package** ("Aufschwung und Beschäftigung", agreed 1.7.2026) — sachgrundlose Befristung to 48 months/6 renewals for hires until end-2030, KSchG high-earner relaxation (2027), AU day 1 — **not enacted; no bill introduced in Bundestag as of 2026-08 (only Kleine Anfrage BT-Drs. 21/7226); MUST NOT be applied; MAY be flagged `law_in_flux`.** Relaxation would collide with CJEU fixed-term abuse doctrine (Adeneler C-212/04; Grupo Norte C-574/16).

Re-check dates: platform draft (before 2.12.2026), ArbZG RefE, coalition-package bill (watch Bundestag Drucksachen).
URLs: ArbZG RefE https://www.gleisslutz.com/de/know-how/bmas-update-neuer-referentenentwurf-zur-aenderung-des-arbeitszeitgesetzes · coalition package PDF https://www.bundesregierung.de/resource/blob/2196306/2445592/bc8e5e160d879f0bdd593121a96a45d2/2026-07-02-koaausschuss-data.pdf · BT-Drs. 21/7226 https://dserver.bundestag.de/btd/21/072/2107226.pdf

---

## 4. CJEU doctrine — issue-tagged (one-line holdings)

| Issue | Cases | Holding / drafting relevance |
|---|---|---|
| Annual leave carry-over (long-term sickness) | C-214/10 Schulte; C-337/10 Neidel; C-684/16 Max-Planck (with C-619/16) | Paid leave continues to accrue during sick leave; forfeiture only after 15 months if employer enabled actual exercise (Max-Planck); employer must actively put the employee in a position to take leave (BAG 19.2.2019 – 9 AZR 541/15; 9 AZR 423/16). Clauses restricting leave accrual during sickness void. |
| Death of worker | C-569/16 Bauer (with C-570/16) | Right to paid leave passes to heirs as monetary entitlement upon death; clauses forfeiting accrued leave on death void. |
| Time-recording obligation | C-55/18 CCOO | Member states must require objective, reliable, accessible time-recording systems (Art. 3, 5, 6, 16(2) Dir. 2003/88) → BAG 13.9.2022 (ArbSchG basis). |
| On-call time = working time | C-518/15 Matzak; C-344/19 + C-580/19 Radiotelevizija Slovenija; C-214/20 Dublin City Council | Intensity test: standby with constraints that objectively and very significantly affect free-time management = working time (location requirement alone insufficient); occasional availability with freedom to pursue private life = rest. Clauses paying flat-rate for on-call must meet minimum wage per hour of working time. |
| Travel time (2025) | C-110/24 (9.10.2025) | Employer-controlled travel (company transport, fixed meeting point, set schedule) for workers with no fixed workplace = working time for safety purposes, regardless of driving/working/resting. Not yet in BAG practice; review tightly organized travel against ArbZG caps. |
| Fixed-term abuse, ex officio review | C-212/04 Adeneler; C-574/16 Grupo Norte | National courts must convert successive fixed-term contracts into indefinite ones and verify misuse ex officio; effective, proportionate, dissuasive sanctions. Applies to § 14(1) chains and by analogy to the planned 48-month rule. |
| Age discrimination | C-144/04 Mangold; C-411/05 Palacios; C-341/08 Petersen; C-388/07 Age Concern | Objective justification + proportionality for age limits (retirement age, age caps for benefits); need documented legitimate aim; AGG § 10 mirrors. |
| Dress codes / religious symbols | C-157/15 Achbita; C-68/17 JR | Neutral general rules (applied generally/indifferently, proportionate genuine employer need) OK; religion-specific bans = direct discrimination, only genuine occupational requirements justify (Art. 4(1) Dir. 2000/78). Clauses singling out religious garb directly discriminatory. |
| Pregnancy | C-177/88 Dekker | Refusal to hire/dismiss for pregnancy = direct sex discrimination (2006/54/EC Art. 2(2)(c)); German: AGG + MuSchG + KSchG § 9 MuSchG special dismissal ban. |
| Data: employee-data legal bases | C-34/21 ÖGK | Art. 88 GDPR: national rules on employee health data must be specific; § 26(1) BDSG general clause insufficient for special categories; specific law/works agreement + necessity required. |
| Data: biometric data | C-439/19 B | Special-category data (Art. 9(2)(b)) requires explicit consent + national law establishing necessity; employer biometric systems need explicit free consent (Art. 9(2)(a) + § 26(2) BDSG) and a DPIA. |
| Data: consent validity | C-61/19 Orange România | Pre-ticked/annexed consent not freely given (Art. 7 GDPR); consent embedded in contract documents is suspect. |
| Conflict-of-laws: habitual workplace | C-29/10 Koelzsch; C-384/10 Voogsgeerd | Habitual workplace = place of actual performance center of gravity, not registered base/letterbox (Koelzsch); "engaging establishment" test under Brussels I (Voogsgeerd). |
| Transfer of undertakings | C-396/07 Juuri; C-561/11 Feyerbacher | § 613a BGB interpretation bound by Directive 2001/23/EC (information, transfer effects). |
| Notice periods / age | C-555/07 Kücükdeveci | Age-based statutory notice-period carve-outs violate the general principle of non-discrimination; § 622(5) BGB disapplied. |

Other 2024–2026 CJEU items: C-110/24 (travel time) and C-19/23 (minimum wage) are the consequential 2025 rulings for German contract drafting; no other 2024–2026 CJEU judgment specifically reshaping German employment-contract drafting identified [unverified].

---

## 5. Cross-border: applicable law, jurisdiction, posting

- **Applicable law — Rome I (EC) 593/2008:**
  - Art. 8: default = law of habitual workplace (Art. 8(2)); temporary posting does not change it (Art. 8(3) = law of sending state where posting temporary with close connection; 2018/957 aligns host-state pay rules on top); party choice allowed (Art. 8(1)) **but cannot deprive the employee of mandatory protection of the habitual-workplace law**; closest-connection fallback (Art. 8(4)).
  - **Art. 9: overriding mandatory provisions** of the forum (and place of performance) apply regardless of choice of law — German MiLoG, ArbZG health limits, AGG core, KSchG (as overriding public policy per BAG practice), § 613a BGB transfer rules treated as such.
  - **Flag:** choice-of-law clauses selecting a low-protection law for work habitually performed in Germany are ineffective as to mandatory German rules (Art. 8(1) proviso + Art. 9).
- **Jurisdiction — Brussels I recast (EU) 1215/2012, Arts. 20–23:** employer may sue employee only in employee's domicile (Art. 22(1)); employee may sue employer in employer's domicile, the habitual/last workplace (Art. 21(1)(b)(i)), or the engaging establishment (Art. 21(1)(b)(ii)); jurisdiction agreements only post-dispute or widening employee options (Art. 23). **Flag:** forum-selection clauses favoring the employer's home court are void except within Art. 23 bounds.
- **Habitual workplace determination:** actual performance center of gravity (C-29/10 Koelzsch — international road transport); engaging establishment (C-384/10 Voogsgeerd — seafarers); C-266/14 Tyco (travel for no-fixed-workplace workers = working time under 2003/88). **Flag:** contracts designating a "registered office"/"mailbox" as workplace do not defeat the actual-workplace test.
- **Posting:** AEntG notification (§ 16) + A1; host-state minimum wage and universally applicable collective agreements from day 1 (2018/957); **≥12 months (extendable to 18) → all host terms**; NachwG § 2(2)/(3) documentation; § 23c AEntG information duty. **Flag:** pure "letterbox posting" (no genuine service provision) is abuse; A1 fraud affects criminal liability but not civil working conditions.
- **Dual employment:** parallel contracts with different employers lawful absent exclusivity clauses; each contract assessed separately; 48h weekly average aggregates across employers under EU law (Art. 6(2) Dir. 2003/88; ArbZG § 2(1) covers all employment relationships) [specific CJEU/BAG case for aggregation unverified]; MiLoG applies per employer-hour.

---

## 6. DE-exceeds-EU / EU-constrains-DE (EU floors are not German ceilings)

| Area | Direction | Detail |
|---|---|---|
| AGB review (§§ 305–310 BGB) | DE exceeds EU | Purely national; no EU analogue for employment contracts; catch-all clause control (transparency § 307) beyond directive floors. |
| KSchG unfair-dismissal protection | DE exceeds EU | No EU dismissal-protection directive; only non-discrimination + specific protections; § 613a BGB implements 2001/23/EC with national additions. |
| ArbZG daily cap | DE exceeds EU | 8h/10h daily rule stricter than EU 48h weekly average (Art. 6 Dir. 2003/88); German opt-out (Art. 22) **not** used — no individual opt-out in ArbZG. |
| BUrlG 24 days | DE exceeds EU | 24 working days (4 weeks) vs EU 4 weeks; but EU Art. 7 puts German carry-over law (15-month rule via CJEU case law) under pressure. |
| MuSchG, EntgFG, BetrVG, TzBfG detail | DE exceeds EU | National layers beyond directives. |
| EntgTranspG thresholds | EU constrains DE | >200/>500 employees, 3-year intervals exceed Directive 2023/970's stricter requirements; conforming-interpretation pressure; thresholds themselves cannot be judicially lowered (PWWL). |
| Fixed-term limits | EU constrains DE | CJEU doctrine (Adeneler, Grupo Norte) requires effective sanctions for successive contracts; § 14(1)/14(2) TzBfG implement clause 5 framework agreement; planned 2026 reform (48 months/6 renewals) assessed against clause 5 — CJEU challenge foreseeable. |
| Vorbeschäftigungsverbot § 14(2) s. 2 TzBfG | DE exceeds EU | National strictness; EU does not require it; 2026 reform would relax. |
| Time-recording | EU constrains DE | C-55/18 → BAG derived obligation from ArbSchG; a future ArbZG amendment cannot reduce below the CJEU floor. |
| AGG § 22 burden of proof | EU constrains DE | Implements Dir. 2000/78 Art. 10, 2006/54 Art. 19, 2000/43 Art. 8; CJEU sets the indicia threshold (C-109/88 Danfoss; C-415/10 Meister; C-83/14 CHEZ). |
| Employee data | EU constrains DE | C-34/21: § 26(1) BDSG general clause cannot cover special categories; works-agreement practice must adapt. |
| Platform work | EU constrains DE (from 2.12.2026) | 2024/2831 will constrain German status testing and require algorithmic-transparency rules regardless of national reform debate. |
| Exclusivity clauses | EU gap in DE | Art. 9 Dir. 2019/1152 implemented only via §§ 138/242/307 BGB + BAG 9 AZR 464/00; no explicit ban. |
| Electronic NachwG form | DE stricter than EU | Art. 3(2) Dir. 2019/1152 permits electronic form; Germany deliberately kept paper (NachwG § 2(1)). |

---

## 7. Citation blacklist (hallucination firewall)

- **C-174/21 and C-477/20 are NOT minimum-wage cases** — could not be confirmed as employment-law CJEU cases; the confirmed minimum-wage-directive case is **C-19/23** (11.11.2025). Never cite C-174/21 or C-477/20.
- **BAG "7 AZR 308/22" does not exist** (near-misses only: 6 AZR 308/22, 7 AZR 308/97, 8 AZR 308/24). Correct citations: **7 AZR 300/22** (16.8.2023, Schriftform § 14(4) TzBfG) and **7 AZR 203/23** (12.6.2024, Gleichstellungsbeauftragte § 14(1) s. 2 No. 3 TzBfG), both confirmed on bundesarbeitsgericht.de.
- **Biometric-data case is C-439/19 (B)**; C-61/19 (Orange România) = consent validity, not biometrics.
- Case-law findings MUST cite from `case-law.md` or carry `[unverified]`/`[web-verified]`.
