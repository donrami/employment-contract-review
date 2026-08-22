# What We Need to Build: An Agentic Skill for Assessing Employment Contracts under German and EU Law

**Integration owner's synthesis of four research slices** (01-german.md, 02-eu.md, 03-pitfalls.md, 04-arch.md). **Law as of 2026-08.** All four slices share the same as-of date, citation conventions, and severity scale; this document merges them, deduplicates, and fixes build-ready requirements. `[verify at build time]` marks items the slices left unresolved — nothing here invents law.

---

## 1. Executive summary

Build `ger-employment-contract-review`: an omp skill that ingests a full employment contract (Arbeitsvertrag) — PDF, DOCX, TXT, pasted text, or URL — and emits clause-level pitfall findings under German law with an EU-law overlay: clause inventory, per-finding severity (Critical/High/Medium/Low), verified legal basis (statute section + case number + URL), recommended rewording, NachwG § 2 completeness check, whole-contract AGB review, statutory-floor sweep, structured JSON + markdown report. Core value: an employee-protective, evidence-first second reader that catches the recurring void-clause classes (probation >6 months, fixed-term limits, flat overtime "Abgeltung", non-competes without 50% Karenzentschädigung, missing NachwG terms, penalty clauses, Zeugnis waivers) with citations a human lawyer can check in seconds. Biggest risks: (1) case-law hallucination — a plausible-but-fake BAG/CJEU citation is a Critical-class failure, mitigated by a citation whitelist + `[unverified]` convention; (2) law drift — Pay Transparency Directive transposition deadline missed (7.6.2026), ArbZG 8h→weekly-cap reform pending, Platform Work Directive due 2.12.2026, July-2026 coalition reform not enacted; every finding must carry `law_in_flux` flags and the `law_as_of` pin; (3) extraction garbage — scanned contracts must surface `extraction_confidence: low` rather than be analyzed. Assessment only: never a validity verdict, never full-contract drafting, never litigation prediction.

---

## 2. Requirements

### 2.1 Functional

- **Inputs:** one contract document — PDF (incl. scanned → OCR), DOCX, TXT, pasted clause text, or URL; optional auxiliary: referenced Tarifvertrag/Betriebsvereinbarung PDF as context (flagged, not fully reviewed). Phase 0 accepts exactly one contract; portfolios/framework agreements out of scope.
- **Language handling:** DE, EN, or mixed. Detect via glossary keyword scan; report in contract's dominant language or user preference; findings reproducible in both via DE↔EN glossary.
- **Jurisdiction:** German law presumed (German text, German statutes cited, German employer, works-council references). Non-German signals → conflict-of-laws note (Rome I Art. 8 mandatory-protection floor) and stop unless user confirms German-law review.
- **Contract type detection (gates AGB review):** standard-form (Formulararbeitsvertrag, § 305(1) BGB — full §§ 305–310 review) vs. individually negotiated (escapes §§ 307–309 but not mandatory floors, §§ 134/138/242 BGB). Ambiguous → treat as AGB (§ 305c(2) BGB, employee-protective default), label the assumption.
- **Workflow:** strictly sequential phases 0–5 (Intake → Normalize → Clause-by-clause → Cross-cutting → Risk scoring → Report); each phase must complete its uncertainty/escalation exits before the next.
- **Outputs (both, same content, two views):**
  - JSON findings report (schema § 6): contract metadata, risk profile, cross-cutting checks, findings array (F001…), each with clause quote, category, pitfall_id, legal_basis, severity, confidence, `law_in_flux` flag, recommended_action/wording, sources.
  - Markdown report: header (`Law as of`), executive summary, metadata table, findings table, risk profile, cross-cutting checks, clause annex, disclaimer.
- **Detection scope:** per-clause checklist matching → pitfall IDs (P-catalog); cross-cutting: NachwG § 2(1) 15-item completeness with per-item deadline classes, whole-contract AGB review (transparency § 307(1) S. 2, surprising clauses § 305c(1), ambiguity § 305c(2), severability § 306), statutory-floor sweep (MiLoG/ArbZG/BUrlG/EFZG/KSchG/TzBfG/EntgTranspG), collective-law interplay (§ 4(3) TVG Günstigkeitsprinzip), clause-vs-clause contradictions.
- **web_search:** bounded — max 2 queries in Phase 0, max 3 per contract in Phase 2, only for figures/thresholds newer than the knowledge base or explicit user ask; every web-derived claim needs URL + `[web-verified YYYY-MM-DD]`; exhausted budget → confidence `low`, never an invented citation.

### 2.2 Non-functional

- **Accuracy:** findings MUST carry legal basis from statute text (gesetze-im-internet.de) or the case-law whitelist; no basis → no legal consequence asserted (Low drafting note at most). No fabricated case law, hard rule (§ 7).
- **Currency / as-of pinning:** `law_as_of` constant in SKILL.md frontmatter; every report and finding prints it; annual figure re-verification cadence (1 Jan/1 Jul for Mindestlohn, Pfändungsfreigrenzen, BBG); single-pass update procedure (bump constant + all reference headers + smoke test).
- **Offline-capable:** full review runnable from references alone; web_search optional enhancement only.
- **Guardrails:** not-legal-advice disclaimer mandatory; seek-counsel boilerplate fires on any Critical finding, High with financial exposure, central-term `law_in_flux`, or user "should I sign?"; no outcome guarantees (§ 7).
- **Performance/context:** SKILL.md ≤ ~8–10 KB; references (~200 KB total) loaded per-phase per loading map, never wholesale; one fact lives in one file (no duplication).
- **Determinism:** same contract + same as-of date → same findings modulo explicitly surfaced web-verification deltas; severity criteria shared verbatim from pitfalls.md, never redefined per-run.

---

## 3. Skill architecture

### 3.1 File tree

```
ger-law/
  SKILL.md                 # procedure, phases 0–5, decision rules, loading map, output schema refs, guardrails, law_as_of
  references/
    statutes.md            # German statutory framework, per-statute floors (from 01-german.md)
    eu-law.md              # EU directives, CJEU case law, transposition status (from 02-eu.md)
    pitfalls.md            # master pitfall catalog: ID, name, basis, severity, fix (from 03-pitfalls.md)
    case-law.md            # verified citation index: BAG/BVerfG/CJEU, issue-tagged — the hallucination firewall
    checklists.md          # per-category review decision trees + NachwG/AGB checklists
    glossary.md            # DE↔EN terms, statute abbreviations, EU directive numbers
```

**Loading map (MUST follow):** Phase 0 → glossary.md (skim); Phase 1 → SKILL.md only; Phase 2 → checklists.md + pitfalls.md fully, case-law.md on demand; Phase 3 → statutes.md + eu-law.md fully, checklists.md NachwG/AGB sections; Phase 4 → pitfalls.md severity section; Phase 5 → SKILL.md schema.

### 3.2 Paste-ready frontmatter

```yaml
---
name: ger-employment-contract-review
description: >
  Assess full German employment contracts (Arbeitsvertrag, employment
  agreement, employment contract) for legal pitfalls under German law with
  EU-law overlay. Trigger phrases: "assess employment contract", "review
  Arbeitsvertrag", "find pitfalls in this contract", "is this clause valid",
  "check this contract for problems", "prüfe diesen Arbeitsvertrag".
  Activates when the user supplies a contract text — PDF, scan, docx,
  pasted clauses, or URL — and asks for review, validation, risk assessment,
  AGB/statutory compliance checking, or clause-by-clause analysis.
  Delivers: clause inventory, per-finding severity (Critical/High/Medium/
  Low), legal basis with verified citations, recommended rewording,
  NachwG § 2 completeness check, whole-contract AGB review, statutory-floor
  sweep, structured JSON + human-readable markdown report.
  Out of scope: drafting full contracts from scratch, legal advice or
  outcome guarantees, litigation strategy, collective-bargaining
  negotiation support, non-German law (flag and stop unless conflict-of-
  laws note is requested).
law_as_of: 2026-08-22
---
```

### 3.3 Workflow phases 0–5 (decision rules)

- **Phase 0 — Intake:** identify format (PDF/docx → `read` extraction; scanned → OCR with `extraction_confidence: low` per affected clause); detect language; determine jurisdiction; determine contract type (AGB vs individual, evidence: boilerplate layout, multi-employee form language, absence of hand-written amendments); note collective-agreement references; bounded web_search (max 2); escalation: legal-advice asks refused, unreadable doc → failure report with extraction error, no guessing.
- **Phase 1 — Normalize:** strip headers/footers/page numbers; build clause inventory (C01…, `clause_id_orig` preserved, verbatim quotes only); tag clause type from fixed taxonomy (probation, duration/fixed-term, remuneration, working-time, leave, termination, post-contractual restraint, confidentiality, secondary employment, overtime, on-call, training costs, pension, transfer/change, boilerplate, signature/misc); merge split clauses, split merged ones; untaggable → `category: other` + explicit note.
- **Phase 2 — Clause-by-clause:** run matching checklist per tagged clause → candidate pitfall IDs; one finding per distinct issue (same `clause_id` can carry several); no forced matches — checklist complete with no triggers → `no_issue_found`; bounded web_search (max 3); no verified basis → drop or Low drafting note, never a legal consequence; unsettled law → `law_in_flux` with current rule + pending change; fact-dependent validity (e.g. Matzak on-call intensity) → state the test, recommend counsel confirmation, don't resolve facts.
- **Phase 3 — Cross-cutting:** NachwG § 2(1) 15-item completeness + deadline classes (day 1: items 1, 7, 8; 7 days: 2–6, 9, 10; 1 month: 11–15); whole-contract AGB review; statutory-floor sweep; collective-law interplay (§ 4(3) TVG; § 77(6) BetrVG Nachwirkung gap); contradictions (clause-vs-clause, contract-vs-floor, contract-vs-NachwG-declared terms with § 4 S. 1 NachwG reversed burden).
- **Phase 4 — Risk scoring:** severity per shared criteria verbatim (Critical = void/violates mandatory statute; High = likely AGB-invalid under settled BAG law or significant financial risk; Medium = narrow conditions/fact-dependent/recent law; Low = drafting weakness); cross-cutting findings on same scale; risk profile = counts + top-3 by severity×dispute-likelihood + `critical_findings` flag, descriptive not verdict; uncertainty lowers confidence, never severity.
- **Phase 5 — Report:** both artifacts; header with `Law as of`, jurisdiction assumption, contract type, extraction confidence; confidence labels per finding; seek-counsel triggers; boilerplate disclaimer.

### 3.4 Tool policy

- `read` for extraction (PDF/docx/TXT/URL). `inspect_image`-style OCR path for scans — mark low confidence, never analyze garbage.
- `web_search` strictly budgeted (2+3 per contract) and only for post-pin figures or explicit asks; results cited with URL + `[web-verified]`.
- `browser`: not needed; `read` on URLs suffices. No LSP/bash needed — this is a knowledge+LLM skill, not code.
- No project-wide commands; no formatters/linters.

---

## 4. Legal knowledge base

Per reference file, contents and coverage (sources: slices 1–2; every floor keeps statute section + URL; each file self-pins as-of date).

### 4.1 statutes.md — German framework (from 01-german.md)

- **Norm hierarchy:** mandatory statute (zwingendes Recht) → Tarifvertrag (§ 4 TVG) → Betriebsvereinbarung (§§ 77, 87 BetrVG) → individual contract; detrimental deviations void (§ 134 BGB).
- **AGB-Kontrolle:** §§ 305(1), 305b, 305c(1)-(2), 306, 307(1)-(2) incl. Transparenzgebot, 308, 309 BGB applied to employment contracts via § 310(4) S. 2 BGB with employment-law peculiarities; clause-by-clause review; no geltungserhaltende Reduktion.
- **BGB:** § 611a (definition), § 612a (Maßregelungsverbot), § 615 (Annahmeverzug), § 616, § 619, §§ 620–623 (Schriftform for Kündigung — paper/wet signature, e-mail void), § 626 (fristlose Kündigung, 2-week period), § 628, § 630 (Zeugnis), § 613a (Betriebsübergang — step-in, transfer-dismissal void, information duty, 1-month objection), §§ 622(1)-(3) (notice periods, probation cap 6 months, age-25 carve-out EU-incompatible), § 276(3), § 394/400 (set-off/assignment limits), § 315 (billiges Ermessen).
- **NachwG (implementing EU 2019/1152, in force 1.8.2022):** § 2(1) 15 mandatory items (parties, start date, fixed-term end, place of work, job description, probation, pay composition itemized incl. overtime/bonuses + due date + method, working time/breaks/shifts, on-call terms, overtime conditions, leave, training, pension provider, termination procedure incl. Schriftform + notice periods + 3-week Kündigungsschutzklage deadline, TV/BV references); § 2(1) S. 9 deadline classes; § 2(2)-(3) posting items; § 2(5) full contract satisfies documentation; § 3 change notification; § 4 S. 1 reversed burden of proof + fine up to €2,000; § 5.
- **TzBfG:** § 4 (part-time non-discrimination), § 7 (change-of-hours request, 1-month reasoned reply), § 8 (reduction right, >15 employees, 3-month lead, operational-reasons refusal, deemed grant), § 9/9a (return to longer hours; Brückenteilzeit 1–5 years, >45 employees), § 12 (Arbeit auf Abruf — 20 h/week default fiction, 25%/20% fluctuation bands, reference periods), § 14(1) Sachgrund catalog, § 14(2) sachgrundlos 2 years/3 extensions + Vorbeschäftigungsverbot (BVerfG 6.6.2018; BAG 7 AZR 733/16 8-year gap blocks; 7 AZR 452/17 22-year gap OK; 7 AZR 203/23 different-kind prior employment blocks), § 14(2a) new companies 4 years, § 14(3) over-52s 5 years, § 14(4) Schriftform, § 15(2)-(4) notice/probation proportionality, § 16 (void term → indefinite), § 17 (3-week Klagefrist).
- **KSchG:** § 1 (social justification), § 1(1) Wartezeit >6 months, § 2 (Änderungskündigung, 3-week protest), §§ 4/5/7 (3-week Klagefrist, § 7 fiktive Wirksamkeit), § 23(1) Kleinbetriebsklausel ≤10 employees (≤5 pre-2004 contracts; part-time weighting 0.5/0.75), § 1a (0.5 monthly salaries/year severance), § 14(2) (executives). Special protection: MuSchG §§ 17–18, SGB IX §§ 168/85 ff., BetrVG § 15, ArbPlSchG § 2, PflegeZG § 5, BEEG § 18.
- **BUrlG:** §§ 1, 3(1) (24 Werktage = 4 weeks; 20 days on 5-day week), 4 (Wartezeit), 5, 7(1)-(4) (carry-over, 31.3., Abgeltung), 8 (illness during leave), 11 (13-week average pay), 13 (Abweichungsverbot).
- **EFZG:** §§ 2 (holiday pay), 3 (6 weeks sick pay, Wartezeit 4 weeks), 4 (U1), 12/eAU (mandatory electronic sick note for statutory-insured since 1.1.2023).
- **ArbZG:** § 3 (8h/day, 10h with 6-month/24-week averaging), § 4 (breaks), § 5 (11h Ruhezeit), § 6 (night work), § 7 (derogations), §§ 9–11 (Sunday/holiday rest), § 14; **time recording:** BAG 13.9.2022 – 1 ABR 22/21 — record start/end/duration for ALL employees via § 3(2) No. 1 ArbSchG + Art. 31(2) EU Charter + Dir. 2003/88 (C-55/18 CCOO); ArbZG electronic-recording reform announced June 2026, **not enacted**.
- **MiLoG:** § 1 (€13.90/h from 1.1.2026; €14.60 from 1.1.2027), § 2 (Fälligkeit, no set-off below minimum), § 3 scope, §§ 8/9/17 (record-keeping, 2-year retention), § 20 (Auftraggeberhaftung guarantor-style), §§ 13/14 (FKS enforcement).
- **EntgTranspG:** §§ 3, 7 (information right >200 employees), 10/21 (reporting >500), 12; BAG 8 AZR 483/18 (refusal shifts burden), 8 AZR 488/19 (comparator group).
- **AGG:** § 1 grounds, § 7 prohibition, § 15 compensation (3 salaries cap for non-hiring), § 22 burden of proof, § 12 prevention duty.
- **GewO/HGB:** § 106 GewO (Weisungsrecht per billiges Ermessen), § 109 GewO + § 630 BGB (Zeugnis — truthful and benevolent; no pre-termination waiver, BAG 18.6.2025 – 2 AZR 96/24 (B)), § 110 GewO + §§ 74–75c HGB (post-contractual non-compete: legitimate interest, ≤2 years, ≥50% Karenzentschädigung — else void; § 75 waiver payment; § 75a/75b release), § 60 HGB (in-employment loyalty).
- **BDSG/GDPR:** § 26(1) (contract-purpose processing), § 26(2) (free consent — imbalance presumption; blanket consent in form contract invalid), Art. 6/9/88 GDPR; CJEU C-34/21 (ÖGK — general clause insufficient for health data), C-439/19 (biometric = special category, explicit consent), C-61/19 (bundled consent not freely given).
- **AÜG:** § 8 (equal pay/conditions; tariff derogation, 9-month step-up), §§ 9/10 (no-permit contracts void; employment deemed with user), § 17a (18-month Überlassungshöchstdauer), § 13 (permit duty).
- **ArbnErfG (ArbEG):** §§ 4–13, 18, 22 (report duty, 4-month claim, reasonable compensation, no contracting out to employee's detriment; 2024/25 reform died with Bundestag dissolution — 1957 Act as amended 2009 applies).
- **Further:** HinSchG §§ 9, 36, 37, 39 (reporting carve-outs; restricting agreements void; retaliation ban + reversed burden), MuSchG/BEEG/PflegeZG (§§ 17–18, 15/18, 2–5), SGB IX § 208 (5 extra leave days), ZPO § 850c (Pfändungsfreigrenze), PrKG §§ 1–7 (indexation ban), ArbGG § 101 (arbitration prohibition), GeschGehG § 5 (whistleblower carve-out), InsO §§ 108/113/55 (insolvency), § 41 SGB VI (pensioner fixed-term, since 1.1.2026: 8 years/12 contracts).

### 4.2 eu-law.md — EU layer & transposition (from 02-eu.md)

- **Directive → transposition map:** 2003/88 → ArbZG; 97/81 + 99/70 → TzBfG; 2019/1152 → NachwG 2022 (+ TzBfG §§ 7(3), 12(3), 15(3); training costs § 111 GewO); 2000/78 + 2000/43 + 2006/54 → AGG; 96/71 + 2018/957 → AEntG; 2001/23 → § 613a BGB; GDPR → § 26 BDSG; 2019/1937 → HinSchG; 2022/2041 → MiLoG (partially annulled); 2023/970 → EntgTranspG (NOT transposed); 2024/2831 → platform work (NOT transposed).
- **Transposition-status flags (must be pinned in every report):**
  - **Pay Transparency (EU) 2023/970:** deadline 7.6.2026 **missed**; no statute by 2026-08. From 8.6.2026: directly binding on public employers; for private employers Art. 157 TFEU horizontal effect + conforming interpretation; Art. 7(6) pay-secrecy clauses void → strike via § 307 BGB; Art. 4 becomes interpretive yardstick for pay structures; ad pay-range disclosure (Art. 5), prior-pay questions ban (Art. 6), reporting (Art. 8), joint assessments (Art. 9) await legislation.
  - **Platform Work (EU) 2024/2831:** deadline 2.12.2026; no published draft as of 2026-08 (BMAS preparing; Direktanstellungsgebot under discussion); presumption of employment (Art. 5) will interact with § 611a BGB status testing.
  - **Minimum Wage (EU) 2022/2041:** partially annulled by CJEU C-19/23 (11.11.2025) — Art. 5(2)/(4) void (pay excluded from EU competence, Art. 153(5) TFEU); Art. 4 collective-bargaining promotion upheld; MiLoG unaffected. Do NOT cite Art. 5 criteria as binding.
  - **ArbZG reform:** June-2026 ministerial announcement (8h daily → weekly cap + electronic recording); not enacted; EU floor (Art. 6 48h weekly average, Art. 3 11h rest) unchanged; BAG recording duty stands on ArbSchG.
  - **July-2026 coalition package** ("Aufschwung und Beschäftigung"): sachgrundlose Befristung to 48 months/6 renewals for hires until end-2030, KSchG high-earner relaxation (2027), AU day 1 — **not enacted; MUST NOT be applied; MAY be flagged `law_in_flux`**. Relaxation would collide with CJEU fixed-term abuse doctrine (Adeneler C-212/04; Grupo Norte C-574/16).
- **CJEU doctrine to encode (issue-tagged):** leave carry-over (C-214/10 Schulte, C-337/10 Neidel, C-684/16 Max-Planck — 15-month rule + employer cooperation duty; C-569/16 Bauer — leave passes to heirs); time recording (C-55/18 CCOO); on-call intensity (C-518/15 Matzak, C-344/19 + C-580/19 DJ, C-214/20 Dublin — case-by-case intensity test); travel time (C-110/24, 9.10.2025 — employer-controlled travel = working time for no-fixed-workplace staff; not yet in BAG practice); fixed-term abuse/ex officio (C-212/04, C-574/16); age (C-144/04 Mangold, C-411/05 Palacios, C-341/08 Petersen, C-388/07); dress codes (C-157/15 Achbita — neutral general rules OK if proportionate; C-68/17 JR — religion-specific bans directly discriminatory); pregnancy (C-177/88 Dekker); employee data (C-34/21, C-439/19, C-61/19); notice-period age-25 carve-out (C-555/07 Kücükdeveci → § 622(2) S. 2 BGB disapplied); transfer (C-396/07 Juuri, C-561/11 Feyerbacher); burden of proof (C-109/88 Danfoss, C-415/10 Meister, C-83/14 CHEZ).
- **Cross-border:** Rome I Art. 8 (habitual-workplace law default; party choice cannot strip mandatory protection of Art. 8(2)/(3) law), Art. 9 (overriding mandatory provisions — MiLoG, ArbZG health limits, AGG core apply regardless); Brussels Ia Arts. 20–23 (employee-suits at habitual workplace; employer limited to employee's domicile; Art. 23 jurisdiction agreements only post-dispute/widening); habitual-workplace determination (C-29/10 Koelzsch — center of gravity, not registered base; C-384/10 Voogsgeerd); posting: AEntG notification + A1, host-state minima from day 1, ≥12 (extendable 18) months → all host terms (2018/957), NachwG § 2(2)/(3) docs, § 23c AEntG info duty.
- **DE-exceeds-EU / EU-constrains-DE table** (skill must not treat EU floors as German ceilings): AGB review and KSchG purely national; ArbZG daily cap stricter than EU 48h average (no German opt-out); EntgTranspG thresholds (>200/>500, 3-year intervals) exceed directive and are now under conforming-interpretation pressure; no explicit exclusivity-clause ban (Art. 9 2019/1152 implemented only via §§ 138/242/307 BGB + BAG 9 AZR 464/00); no electronic NachwG form (Germany deliberately stricter than Art. 3(2) 2019/1152); § 26 BDSG gap for special-category data post-C-34/21.

### 4.3 case-law.md — verified citation index

Whitelist of verified BAG/BVerfG/CJEU decisions with issue tags + URLs. **Findings MUST cite from here or mark `[unverified]`/`[web-verified]`.** Core set (all verified in slices): BAG 1 ABR 22/21 (time recording), 5 AZR 406/10 + 5 AZR 517/09 (flat overtime), 2 AZR 160/24 (30.10.2025, fixed-term probation proportionality — no 25% rule), 5 AZR 108/25 (25.3.2026, formular Freistellung void), 2 AZR 96/24 (B) (18.6.2025, pre-termination Zeugnis waiver void), 7 AZR 733/16 / 7 AZR 452/17 / 7 AZR 203/23 / 7 AZR 300/22 (Vorbeschäftigung/Schriftform), 9 AZR 423/16 + 9 AZR 541/15 + 9 AZR 199/20 + 9 AZR 245/19 (A) + 9 AZR 577/20 (A) (leave expiry), 8 AZR 58/20 + 9 AZR 162/18 (Ausschlussfristen vs Vorsatz/Mindestlohn), 5 AZR 572/04 + 5 AZR 422/12 (3-month minimum), 8 AZR 897/08 + 8 AZR 196/03 + 8 AZR 973/06 (Vertragsstrafe), 10 AZR 448/15 (non-compete without compensation), 9 AZR 464/00 + 6 AZR 23/19 (secondary employment), 9 AZR 352/04 + 6 AZR 683/16 + 9 AZR 227/11 + 9 AZR 478/18 (Zeugnis), 10 AZR 266/14 + 10 AZR 710/14 + 10 AZR 97/07 + 10 AZR 57/24 (bonus discretion), 10 AZR 825/06 + 10 AZR 634/06 (Gratifikation clawback), 5 AZR 595/17 + 5 AZR 553/17 (travel time), 6 AZR 75/18 (fair negotiation), 2 AZR 582/13 + 8 AZR 130/13 (penalty specifics), 10 AZR 162/24 (dynamic TV references), 5 AZR 700/09 (age-25 carve-out), 9 AZR 595/20 + 9 AZR 32/25 (part-time), 8 AZR 483/18 + 8 AZR 488/19 (EntgTranspG); BVerfG 1 BvL 7/14 + 1 BvR 1375/14 (Vorbeschäftigung); CJEU as § 4.2. **Known-trap citations to never emit:** "BAG 23.8.2023 – 7 AZR 308/22" (does not exist — closest 7 AZR 300/22, 16.8.2023); C-174/21 and C-477/20 as minimum-wage cases (unverifiable); C-61/19 as "biometric" case (wrong — that's C-439/19). `[verify at build time]`: any case number the build team cannot source stays out of the whitelist.

### 4.4 Current figures (as of 2026-08; verify annually at build time)

| Figure | Value | Basis |
|---|---|---|
| Mindestlohn | **€13.90/h** from 1.1.2026 (€14.60 from 1.1.2027; 2025: €12.82) | § 1 MiLoG; 5. Mindestlohnanpassungsverordnung; BMAS/Bundesregierung |
| Minijob-Grenze | €603/month (dynamic: 10 h × €13.90) | § 8(1a) SGB IV |
| Pfändungsfreigrenze (Grundbetrag) | €1,587.40/month net from 1.7.2026 (+ €595.28 per supported person) | § 850c ZPO; Pfändungsfreigrenzenbekanntmachung 2026 (BGBl. I 2026 Nr. 80) |
| BBG Kranken-/Pflegeversicherung | €5,812.50/month (€69,750/year) | SV-RechengrößenVO 2026 |
| BBG Renten-/Arbeitslosenversicherung | €8,450/month (€101,400/year), nationally uniform | SV-RechengrößenVO 2026 |
| Versicherungspflichtgrenze GKV | €6,450/month (€77,400/year) | SV-RechengrößenVO 2026 |
| Sachbezugswert Verpflegung | €345/month full board (€11.51/day) — **sources conflict €333 vs €345** `[verify at build time against SvEV 2026]` | § 2(1) SvEV |
| Sachbezugswert Unterkunft | €282–285/month — **minor source conflict** `[verify at build time]` | SvEV |
| Zusatzurlaub Schwerbehinderte | 5 additional paid workdays/year | § 208 SGB IX |
| Kündigungsfristen | Base 4 weeks to 15th/month-end § 622(1); probation 2 weeks § 622(3); employer tiers 1–7 months (2–20 yrs) § 622(2) | § 622 BGB |
| AÜG Überlassungshöchstdauer | 18 months | § 17a AÜG |
| eAU | mandatory since 1.1.2023 (statutory-insured) | § 5(1a) EFZG |

---

## 5. Pitfall catalog (merged, deduplicated)

Source of truth: 03-pitfalls.md (P1–P57, 14 categories). Folded in from slices 1–2: Ausschlussfristen (forfeiture clauses — German § 3.1, absent from catalog → **P58**), § 8/9a TzBfG part-time rights waiver (**P59**), AÜG temp-agency contract issues (**P60**), InsO/insolvency clauses (**P61**). Full entry format below; every field present in compact form — full expanded entries with typical language + recommended wording live in the skill's `pitfalls.md`.

**Severity scale (shared verbatim):** Critical = void (§§ 134, 138, 307–309 BGB) or mandatory-statute violation, direct liability, term nullified, fine exposure · High = likely AGB-invalid under settled BAG law or significant financial risk · Medium = valid only under narrow conditions, fact-dependent, or recent/reversed law · Low = drafting weakness/transparency gap.

### Category 1 — Probation & trial periods

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P1 | Probezeit >6 Monate / probation >6 months | High | § 622(3) BGB; § 307 BGB; BAG 2 AZR 160/24 | probation >6 months or open-ended; fixed-term: proportionality to term (no 25% rule, case-by-case) |
| P2 | Probezeit ohne Kündbarkeit im befristeten Vertrag / probation without terminability in fixed-term | High | § 15(4) TzBfG | probation clause in fixed-term contract lacking "mit gesetzlicher Frist kündbar" |
| P3 | Getarnte "Einarbeitungszeit" / disguised training period | Medium | § 622(3) BGB; § 307 BGB | reduced notice labelled "Einarbeitung/Training" beyond 6 months — substance over label |
| P4 | Kündigungsfrist unter gesetzlicher Staffelung / notice below statutory minimum | High | § 622(2),(5) BGB; § 134 BGB; C-555/07 Kücükdeveci | employer notice shorter than § 622(2) tiers; age-25 carve-out copy (disapplied) |

### Category 2 — Duration & termination

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P5 | Sachgrundlose Befristung >2 Jahre/3 Verlängerungen / fixed term without cause beyond limits | Critical | § 14(2), 16, 17 TzBfG | >24 months or 4th renewal without Sachgrund → indefinite contract; pensioner exception § 41(2) SGB VI (1.1.2026, 8 yrs/12 contracts) |
| P6 | Kettenbefristung / chain of fixed terms | High | § 14(2) S. 2 TzBfG; § 242 BGB; BVerfG 1 BvL 7/14 | any prior employment with same employer blocks sachgrundlos (8-yr gap blocks, 22-yr gap OK); pretext chains |
| P7 | Befristung ohne Schriftform / fixed term not in writing | Critical | § 14(4) TzBfG; §§ 125, 126 BGB | oral/e-mail extension → indefinite contract; QES (§ 126a) only exception |
| P8 | Unwiderruflicher Kündigungsverzicht / irrevocable termination waiver | Medium | §§ 134, 138, 307 BGB; Art. 12 GG | blanket mutual waiver without compensation |
| P9 | Pauschale Freistellungsklausel / automatic garden-leave clause | Critical | § 307(1) BGB; **BAG 25.3.2026 – 5 AZR 108/25 (new)** | formular clause releasing employee from work during notice period |
| P10 | Change-of-Control-Kündigung / change-of-control termination | Medium | § 1 KSchG; § 613a(4) BGB; § 307 BGB | employer termination right on restructuring/CoC events |
| P59 | Verzicht auf Teilzeitrechte (§ 8/9a TzBfG) / waiver of part-time rights | Medium | § 8, 9a TzBfG (Fiktion, >15/>45 employees) | clause waiving reduction/bridge-part-time rights or announcing-deadline tricks (BAG 9 AZR 595/20) |

### Category 3 — Remuneration

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P11 | Vergütung unter Mindestlohn / below minimum wage | Critical | §§ 1, 20, 21 MiLoG | hourly equivalent < €13.90 (2026) / €14.60 (2027); all-inclusive pay in low band |
| P12 | Pauschale Überstundenabgeltung / flat overtime "Abgeltung" | Critical | § 307(1) S. 2 BGB; BAG 5 AZR 406/10, 5 AZR 517/09 | "sämtliche Überstunden abgegolten" without hour cap (harmless only for very high earners) |
| P13 | Freies Ermessen bei Boni / unfettered bonus discretion | High | § 315 BGB; § 307 BGB; BAG 10 AZR 97/07, 10 AZR 266/14, 10 AZR 57/24 | "nach freiem Ermessen", zero-criteria bonus; Freiwilligkeitsvorbehalt contradicting promise |
| P14 | Lohnabzüge/Aufrechnung / salary deductions & set-off | High | §§ 394, 400 BGB; §§ 850 ff. ZPO; § 4 EFZG; MiLoG § 2(2); § 307 BGB | "Verrechnung mit allen Gegenansprüchen", sick-note-late deductions |
| P15 | Gratifikations-Rückzahlung über BAG-Grenzen / clawback beyond BAG limits | High | BAG 10 AZR 290/17, 10 AZR 825/06, 10 AZR 634/06 | binding >31.3. (<1 monthly salary) / >30.6. (≥1 salary); clawback on employer-initiated termination; pure Entgelt |
| P16 | Entgeltstruktur mit Geschlechterdiskriminierung / gendered pay structure | High | §§ 3, 7–15 EntgTranspG; Art. 157 TFEU; RL 2023/970 (deadline missed 7.6.2026) | pay secrecy clauses (void per Art. 7(6) → § 307 BGB), gendered bands; ad pay-range disclosure pending |
| P17 | Provisionsklausel mit einseitiger Zielanpassung / commission with unilateral quota change | High | § 315 BGB; § 307 BGB; BAG 10 AZR 171/23 | unilateral target/rate changes incl. retroactive cuts |

### Category 4 — Working time & leave

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P18 | Urlaubsverfall ohne Hinweisobliegenheit / leave forfeiture without employer cooperation | High | §§ 3, 7, 13 BUrlG; BAG 9 AZR 541/15, 9 AZR 423/16; C-684/16, C-214/10 | automatic year-end forfeiture; no 15-month employer-cooperation analysis; overgesetzlicher leave |
| P19 | Falsches Urlaubsentgelt / wrong holiday pay | High | §§ 11, 13 BUrlG | base-salary-only holiday pay excluding 13-week average variable components |
| P20 | Fehlende Arbeitszeiterfassung / missing time recording | Medium | BAG 1 ABR 22/21; § 3(2) Nr. 1 ArbSchG; § 16(2) ArbZG | "Vertrauensarbeitszeit ohne Erfassung" (reform pending → `law_in_flux`) |
| P21 | Sonn-/Feiertagsarbeit ohne Ausgleich / Sunday work without compensation | High | §§ 9, 10, 11 ArbZG; § 87(1) Nr. 2 BetrVG | waiver of compensatory rest/supplements |
| P22 | Abrufarbeit ohne 20/25%-Schwellen / on-call work ignoring § 12 TzBfG fictions | High | § 12 TzBfG | no minimum hours (20 h/week fiction), >25% above / >20% below bands |

### Category 5 — Restrictive covenants

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P23 | Wettbewerbsverbot ohne Karenzentschädigung / non-compete without compensation | Critical | §§ 74(2), 110 GewO; BAG 10 AZR 448/15 (salvatorische Klausel cannot cure) | <50% of last contractual remuneration per year → wholly void |
| P24 | Wettbewerbsverbot >2 Jahre / non-compete >2 years | Critical | § 74a(1) HGB; § 110 GewO | >24 months → void in full, no blue-pencil |
| P25 | Übermäßige Abwerbe-/Kundenschutzklauseln / overbroad non-solicit | Medium | §§ 74a, 74b HGB analog; Art. 12 GG; § 307 BGB | blanket customer/employee bans; disguised non-compete without compensation |
| P26 | Unbefristete Verschwiegenheitsklausel / indefinite confidentiality | Medium | § 307 BGB; § 5 GeschGehG; § 17 UWG | "all information, unlimited, to anyone" — overbreadth; whistleblower carve-out |
| P27 | Vertragsstrafe im Arbeitsvertrag / contractual penalty | High | § 309 Nr. 6 via § 310(4) BGB; BAG 8 AZR 897/08, 8 AZR 130/13 | formular penalty for termination (always void); penalty needs concrete breach + proportionality |
| P28 | IP-Klauseln gegen ArbEG / IP clauses conflicting with ArbEG | High | §§ 4–13, 18, 22 ArbnErfG | blanket "all IP vests in employer"; no report/claim/compensation procedure |

### Category 6 — Post-contractual obligations

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P29 | Zeugnisverzicht vor Beendigung / pre-termination reference waiver | Critical | § 109 GewO; § 630 BGB; **BAG 18.6.2025 – 2 AZR 96/24 (B)** | waiver in contract/Aufhebungsvertrag before termination; "nur einfaches Zeugnis" |
| P30 | Übermäßige Herausgabeklauseln / excessive return-of-property | Low | § 307 BGB; § 667 BGB analog; § 614 BGB | return demands covering private devices; pay conditioned on return |
| P31 | Zurückbehaltung von Arbeitspapieren / document retention leverage | Medium | § 312 SGB III; § 41b EStG; § 134 BGB | documents conditioned on release/signature |

### Category 7 — Data protection & monitoring

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P32 | Einwilligungsklausel mit Ungleichgewicht / consent via imbalance | High | § 26(2) BDSG; Art. 6, 88 GDPR; C-61/19 | blanket/unbundled consent in form contract; health data (C-34/21 — § 26(1) insufficient) |
| P33 | Überwachungsklauseln / monitoring clauses (CCTV, e-mail, GPS, BYOD) | High | §§ 4, 26 BDSG; Art. 5, 6, 88 GDPR; § 87(1) Nr. 6 BetrVG; BAG 2 AZR 597/16 | covert/blanket monitoring rights; biometric systems need explicit consent + DPIA (C-439/19) |
| P34 | Vertraulichkeitsklausel vs. HinSchG / confidentiality vs whistleblower law | High | §§ 9, 36, 37, 39 HinSchG | NDA barring reports to authorities/Meldestellen — void per § 39 HinSchG |

### Category 8 — Secondary employment & exclusivity

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P35 | Generelles Nebentätigkeitsverbot / blanket secondary-employment ban | High | Art. 12 GG; § 307 BGB; BAG 9 AZR 464/00; RL 2019/1152 Art. 9 | "jegliche Nebentätigkeit untersagt" / arbitrary Zustimmungsvorbehalt |
| P36 | Exklusivität mit Vergütungskopplung / compensated exclusivity | Medium | Art. 12 GG; § 307 BGB; RL 2019/1152 Art. 9 | exclusivity for allowance doesn't cure AGB defect (formular) |

### Category 9 — Family/care & disability

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P37 | Mutterschutzklauseln / maternity clauses | Critical | §§ 17, 18 MuSchG; § 134 BGB | termination/fixed-term end tied to pregnancy; fixed term auto-extends |
| P38 | Elternzeitbeschränkungen / parental-leave restrictions | High | §§ 15, 18, 19 BEEG | waiver/consent conditions on Elternzeit |
| P39 | Pflegezeitbeschränkungen / care-leave restrictions | High | §§ 2, 3, 5 PflegeZG; § 2 FPfZG | consent conditions; tightened notice |
| P40 | Behindertenklauseln / disability clauses | High | §§ 1, 7, 15 AGG; §§ 164, 168 SGB IX | "uneingeschränkt arbeitsfähig" statements; accommodations excluded |

### Category 10 — Collective-law interplay

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P41 | Dynamische Verweisung auf ausgelaufenen TV / dynamic reference to expired collective agreement | Medium | §§ 3, 4(5) TVG; § 307 BGB; BAG 10 AZR 162/24 | dynamic reference surviving expiry/exit — gap risk |
| P42 | BV-Verweisung ohne Fortgeltung / works-agreement reference without continuity | Medium | § 77(6) BetrVG; § 307 BGB | BV reference without Nachwirkung/Fortgeltung clause |
| P43 | § 613a-Kontinuität falsch behandelt / transfer collective-continuity mishandled | High | § 613a(1),(4),(5) BGB | post-transfer contract abandoning continued TV/BV terms; transfer-based change |

### Category 11 — Cross-border & posting

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P44 | Rechtswahl zulasten zwingenden deutschen Rechts / choice of law evading German protection | High | Art. 8, 9 Rom I-VO; BAG 2 AZR 96/24 (B) | foreign governing law for German habitual workplace — mandatory protection persists |
| P45 | Entsendungslücken / posting gaps | High | §§ 8, 18 AEntG; RL 96/71 + 2018/957 | home-law-only posting clause; no notification/A1/NachwG § 2(2)-(3) docs; forum-selection clauses void per Brüssel Ia Arts. 20–23 |

### Category 12 — Formalities & documentation

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P46 | Fehlende Pflichtangaben § 2 NachwG / missing mandatory terms | Critical | §§ 2, 3, 4 NachwG | any of the 15 items missing → fine €2,000 + reversed burden of proof (§ 4 S. 1); Textform delivery possible since 1.1.2025 under conditions |
| P47 | Elektronische Signatur statt Schriftform / e-signature where writing required | Critical | §§ 125, 126, 126a BGB; § 14(4) TzBfG; § 623 BGB | e-mail/scan without QES for Befristung/Kündigung → void |
| P48 | Textform-Missbrauch / Textform where Schriftform required | High | § 623 BGB; § 126b BGB; § 26(2) S. 3 BDSG | "Kündigung per E-Mail möglich" clauses |
| P58 | Ausschlussfristen zu kurz / forfeiture clauses too short or blanket | High | § 307 BGB; BAG 5 AZR 572/04, 5 AZR 422/12, 8 AZR 58/20, 9 AZR 162/18 | first stage <3 months; single-stage; covering Vorsatz claims (§ 276(3) BGB) or Mindestlohn — void |

### Category 13 — Mobility & workplace

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P49 | Homeoffice-Klauseln ohne Kernbedingungen / home-office without core terms | Medium | § 8 SGB VII; § 670 BGB analog; § 307 BGB; BAG 1 ABR 22/21 | open-ended mobile work; cost/risk shifted to employee |
| P50 | Reisezeit ausgeschlossen / travel time excluded | High | BAG 5 AZR 595/17, 5 AZR 553/17; § 307 BGB | "Reisezeit ist keine Arbeitszeit und unbezahlt" |
| P51 | Kostenabwälzung Arbeitsmittel / equipment cost-shifting | Medium | § 307 BGB; § 670 BGB analog; § 3 ArbSchG; § 618 BGB | BYOD without reimbursement; PPE cost-shifting (statutory violation) |
| P52 | Versetzungsklauseln / relocation clauses | Medium | § 106 GewO; § 307 BGB; § 95 BetrVG; BAG 9 AZR 36/09 | "beliebige Orte im In- und Ausland" without bounds/cost rules |

### Category 14 — Special clauses

| ID | Name (DE/EN) | Sev | Basis | Trigger |
|---|---|---|---|---|
| P53 | Klageverzicht im Aufhebungsvertrag / waiver of claims in severance | High | §§ 123, 138, 307 BGB; § 623 BGB; BAG 6 AZR 75/18 | blanket "sämtliche Ansprüche abgegolten" sweeping non-waivable claims (Zeugnis, Mindestlohn, Vorsatz) |
| P54 | Abfindung unter § 1a-Erwartung / severance below § 1a KSchG pattern | Medium | § 1a KSchG; § 307 BGB | caps below 0.5 salaries/year; conditional on unlawful waivers |
| P55 | Ausschluss der Vorbeschäftigungsanrechnung / prior-service credit exclusion | Medium | § 622(2) BGB; § 1 KSchG; § 613a BGB; BAG 5 AZR 700/09 | "frühere Beschäftigung wird nicht angerechnet" vs statutory counting |
| P56 | Wertsicherungsklausel / indexation clause | Medium | §§ 1–7 PrKG; § 134 BGB | automatic CPI indexation without PrKG exception |
| P57 | Schieds-/Mediationsklauseln / arbitration clauses | High | §§ 101, 110 ArbGG; § 14(2) KSchG; § 4 KSchG | formular arbitration → void (labor courts retain jurisdiction); mandatory pre-mediation endangering 3-week deadline |
| P60 | AÜG-Konstellationen / temp-agency contract issues | High | §§ 8, 9, 10, 17a AÜG | no-permit assignment (contract void, employment deemed with user), equal-pay deviation, >18 months |
| P61 | Insolvenzklauseln / insolvency clauses | Medium | §§ 108, 113, 55 InsO | clauses purporting to shorten insolvency notice/claims — statutory rules override |

### Contract-wide red flags (cross-cutting checklist, Phase 3)

1. Missing NachwG § 2 terms (P46).
2. Internal contradictions — probation vs termination clause, fixed-term vs "unbefristet" preamble, bonus promise vs Freiwilligkeitsvorbehalt, Freistellung vs variable pay (§ 305c(2) BGB resolves against drafter).
3. Gaps — no notice period, no place of work, no Arbeitszeit definition, no overtime rule → § 306(2) BGB defaults + disputes.
4. References to expired/terminated TV/BV (P41/P42) — flag for register verification.
5. Non-gender-neutral pay structure (P16; Art. 157 TFEU + 2023/970).
6. Foreign-jurisdiction boilerplate — "at will", foreign choice-of-law/forum, indemnity, "entire agreement" (P44/P57/P29) — largely void under German mandatory law.
7. Job-duties clauses delegating everything to employer discretion — § 106 GewO/§ 307 BGB transparency.
8. `law_in_flux` sweep — any finding touching ArbZG hours, fixed-term limits, pay transparency, or platform work must carry the pending-reform note (July-2026 package NOT law).

---

## 6. Output & report schema

### 6.1 JSON findings schema (draft 2020-12; exact schema in SKILL.md)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ContractFindingsReport",
  "type": "object",
  "required": ["schema_version", "law_as_of", "contract", "risk_profile", "cross_cutting", "findings"],
  "properties": {
    "schema_version": { "const": "1.0" },
    "law_as_of": { "type": "string", "format": "date" },
    "contract": {
      "type": "object",
      "required": ["id", "title", "language", "jurisdiction_assumption", "contract_type", "is_agb", "clause_count", "extraction_confidence"],
      "properties": {
        "id": { "type": "string" },
        "title": { "type": "string" },
        "language": { "enum": ["de", "en", "mixed"] },
        "jurisdiction_assumption": { "enum": ["german", "flagged", "non-german"] },
        "contract_type": { "enum": ["standard-form", "individually-negotiated", "unknown"] },
        "is_agb": { "type": "boolean" },
        "clause_count": { "type": "integer" },
        "extraction_confidence": { "enum": ["high", "medium", "low"] }
      }
    },
    "risk_profile": {
      "type": "object",
      "required": ["counts", "top_risks", "critical_findings"],
      "properties": {
        "counts": { "type": "object", "properties": {
          "Critical": { "type": "integer" }, "High": { "type": "integer" },
          "Medium": { "type": "integer" }, "Low": { "type": "integer" } } },
        "top_risks": { "type": "array", "items": { "type": "string" } },
        "critical_findings": { "type": "boolean" }
      }
    },
    "cross_cutting": {
      "type": "object",
      "required": ["nachwg", "agb_whole_contract", "statutory_floor", "contradictions"],
      "properties": {
        "nachwg": { "type": "object", "properties": {
          "complete": { "type": "boolean" },
          "missing_items": { "type": "array", "items": { "type": "integer" } },
          "deadline_violations": { "type": "array", "items": { "type": "string" } } } },
        "agb_whole_contract": { "type": "string" },
        "statutory_floor": { "type": "array", "items": { "type": "string" } },
        "contradictions": { "type": "array", "items": { "type": "string" } }
      }
    },
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "clause", "category", "issue", "legal_basis", "severity", "confidence", "recommended_action", "recommended_wording"],
        "properties": {
          "id": { "type": "string", "pattern": "^F[0-9]{3}$" },
          "clause": { "type": "object", "required": ["clause_id", "clause_id_orig", "quote"], "properties": {
            "clause_id": { "type": "string", "pattern": "^C[0-9]{2}$" },
            "clause_id_orig": { "type": "string" },
            "quote": { "type": "string" },
            "extraction_confidence": { "enum": ["high", "medium", "low"] } } },
          "category": { "type": "string" },
          "pitfall_id": { "type": "string" },
          "issue": { "type": "string" },
          "legal_basis": { "type": "array", "items": { "type": "string" } },
          "severity": { "enum": ["Critical", "High", "Medium", "Low"] },
          "confidence": { "enum": ["high", "medium", "low"] },
          "law_in_flux": { "type": "boolean" },
          "recommended_action": { "type": "string" },
          "recommended_wording": { "type": ["string", "null"] },
          "sources": { "type": "array", "items": { "type": "string", "format": "uri" } }
        }
      }
    }
  }
}
```

### 6.2 Markdown report template

```markdown
# Contract Review Report — <title>
**Law as of:** <law_as_of> · **Report language:** <lang> · **Extraction confidence:** <high|medium|low>

## Executive summary
<2–5 sentences: contract type, AGB status, severity counts, top risks, seek-counsel trigger if any>

## Contract metadata
| Field | Value |
|---|---|
| Jurisdiction assumption | german / flagged / non-german |
| Contract type | standard-form / individually-negotiated / unknown |
| AGB review applied | yes / no |
| Clauses analyzed | N |

## Findings table
| ID | Clause | Severity | Issue | Legal basis | Confidence |

## Risk profile
<counts per severity; top-3 risks; critical_findings flag>

## Cross-cutting checks
- NachwG § 2(1): <complete / missing items …>
- Whole-contract AGB: <notes>
- Statutory floors: <checks>
- Contradictions: <list>

## Clause-by-clause annex
<per clause: quote, findings, recommended wording>

## Disclaimer
<not legal advice; counsel referral triggers; law as-of date>
```

### 6.3 Example entry (drawn from P1, per 04-arch.md)

```json
{
  "id": "F001",
  "clause": { "clause_id": "C03", "clause_id_orig": "§ 3",
    "quote": "Die ersten zwölf Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden." },
  "category": "probation",
  "pitfall_id": "P1",
  "issue": "Probation beyond six months: the two-week notice window of § 622(3) BGB is limited to 'längstens sechs Monate'; a longer formular probation is AGB-invalid under § 307 BGB and the statutory notice periods of § 622(1)–(2) BGB apply instead.",
  "legal_basis": ["§ 622 Abs. 3 BGB", "§ 307 BGB", "BAG 30.10.2025 – 2 AZR 160/24"],
  "severity": "High", "confidence": "high", "law_in_flux": false,
  "recommended_action": "Reduce probation to six months for an indefinite contract; for fixed-term contracts calibrate probation to the term per BAG 2 AZR 160/24 (case-by-case proportionality, no fixed 25% rule).",
  "recommended_wording": "Die ersten sechs Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.",
  "sources": ["https://www.bundesarbeitsgericht.de/presse/probezeitkuendigung-im-befristeten-arbeitsverhaeltnis/", "https://www.gesetze-im-internet.de/bgb/__622.html"]
}
```

---

## 7. Guardrails & compliance

- **Not legal advice:** every report carries the disclaimer; seek-counsel triggers fire boilerplate referral, never recommendations. Findings phrased as risk/validity assessments, never guarantees.
- **Jurisdiction boundary:** German law by default; non-German → conflict-of-laws note (Rome I Art. 8/9) and stop unless user confirms German review; foreign governing-law + German workplace → German mandatory law note.
- **No fabricated case law (hard rule, Critical-class failure):** findings cite only (a) statute sections, (b) case-law.md whitelist entries, or (c) web-verified citations with URL + `[web-verified <date>]`. Unsourced case number → never emitted; `[unverified]` at best. Known-trap citations blacklisted (§ 4.3).
- **Confidence labels:** mandatory per finding (high/medium/low); `low` requires explicit reason (unverified basis, extraction-affected, unsettled law). `law_in_flux` for pending reforms (ArbZG, Pay Transparency, Platform Work, July-2026 package).
- **Critical → counsel:** any Critical or High-with-financial-exposure finding triggers referral boilerplate.
- **OCR/extraction uncertainty:** `read` extraction; low confidence surfaced per clause and in header; garbage is reported as illegible, never analyzed.
- **Multilingual:** glossary-backed DE↔EN; findings reproducible in both; subtle terms (Probezeit, Befristung, Abgeltung) flagged on mistranslation risk.
- **No scope creep:** assessment only — no full drafting, no TV drafting, no negotiation advice; `recommended_wording` is clause-level repair for flagged issues only.

---

## 8. Evaluation plan

- **Golden corpus (N = 20):** 15 seeded-bad contracts (2–4 known pitfalls each across distinct categories — probation P1/P2, § 14(2) TzBfG violations, missing NachwG items, below-floor pay, invalid non-compete, absolute secondary-employment ban, § 15(4) TzBfG trap, formular Freistellung P9, Zeugnis waiver P29); 5 clean contracts (false-positive measurement, incl. one borderline near-floor/individually-negotiated for severity calibration). Ground truth = pitfall IDs + clause IDs, reviewer-annotated.
- **Metrics (per category and overall):** Precision (pitfall_id AND clause_id match / total findings), Recall (detected seeded pitfalls / seeded), F1; false-Critical rate (must be ≤ 0 on the clean set); missed-Critical rate (must be 0); category-level breakdown.
- **Smoke test (MUST run on every knowledge-base update):** (1) known-bad contract → ≥1 Critical/High finding, pitfall IDs present, no invented citations; (2) clean contract → zero Critical/High; (3) both schema-valid JSON. Failure = update blocked.
- **Iteration loop:** every missed seeded pitfall → regression case appended to corpus; over-triggering catalog entries → tightened detection patterns in checklists.md; re-run metrics, record precision/recall deltas in changelog.

---

## 9. Build order

1. **SKILL.md skeleton + frontmatter + output schema (day 1, low effort/risk).** Fixes the contract: phases, loading map, `law_as_of`, JSON schema. Phase 2 detail deferred — checklists depend on the catalog.
2. **pitfalls.md (highest value, medium effort, low risk).** Port 03-pitfalls.md P1–P57 + add P58–P61 (this document § 5); stable IDs, normalized severity and fix wording; append-only after publication.
3. **statutes.md + eu-law.md + case-law.md (medium effort, low risk).** Port 01/02-german/eu.md to lookup form; build citation whitelist FIRST (hallucination firewall) before any checklist citing case law. Safe to parallelize (three independent ports).
4. **checklists.md (medium effort, medium risk).** Per-category decision trees; calibrate against corpus (step 5).
5. **Evaluation corpus + smoke harness (medium effort).** 20 contracts, annotation, metric script; gates any quality claim. `[verify at build time]`: benchmark `read` PDF/OCR path on 3 scanned samples.
6. **Workflow hardening (ongoing).** Refine Phase 2–4 decision rules from evaluation failures.

**What can ship first:** SKILL.md + statutes/eu-law/case-law + pitfalls.md + a working Phase 0–3 for plain-text contracts — a useful German-law checklist reviewer — before the corpus and checklists.md reach full fidelity.

---

## 10. Open questions & risks

- **[Critical] Case-law hallucination:** residual risk of plausible invented case numbers. Rule stands: no source → no citation. Open: may findings cite a case the model "knows" but that is absent from the whitelist? Recommended: yes, only with URL + `[web-verified]`.
- **[High] Law drift 2026 (real today):** Pay Transparency 2023/970 — deadline missed, direct effect for public employers from 8.6.2026, conforming interpretation for private; ArbZG 8h→weekly cap announced, not enacted; Platform Work 2024/2831 due 2.12.2026, no draft; Minimum Wage Directive partially annulled (C-19/23) — MiLoG unaffected; July-2026 coalition package (48-month fixed-term, KSchG high earners, AU day 1) NOT law. Skill MUST flag `law_in_flux`, never apply unenacted reform. `[verify at build time]`: track Bundestag passage monthly.
- **Sachbezugswerte discrepancy:** €333 vs €345 (board), €282 vs €285 (lodging) across sources — `[verify at build time]` against SvEV 2026 before pinning.
- **`[unverified]` residue from slices:** BAG 7 AZR 308/22 (nonexistent — use 7 AZR 300/22/203/23); C-174/21, C-477/20 (not minimum-wage cases — use C-19/23); C-61/19 is consent-validity, C-439/19 is biometric. All blacklisted.
- **Contract variants:** TV/BV references — skill flags interplay (§ 4(3) TVG, NachwG item 15) but cannot review unprovided documents. Open: accept accompanying TV/BV PDF as optional Phase-0 input? Recommended: yes, as auxiliary context, still out of full-review scope.
- **PDF extraction quality:** scanned contracts → OCR errors → missed pitfalls. Mitigation: `extraction_confidence` surfacing, never analyzing garbage, ask for text when OCR fails badly.
- **Multilingual:** subtle German terms mistranslated in review — glossary + dual-language findings mitigate; residual risk accepted.
- **Severity subjectivity (Medium/Low):** shared verbatim criteria + corpus calibration + tracked false-Critical rate.
- **Scope creep (drafting vs assessment):** `recommended_wording` edges toward drafting; guard is clause-level-fix-only and evaluation monitoring.
- **Two-stage § 14(2) TzBfG reform tension:** if the July-2026 48-month rule passes, it will collide with CJEU fixed-term-abuse doctrine (Adeneler, Grupo Norte) — a foreseeable reference; the skill must then re-pin the limit and flag the challenge risk. `[verify at build time]`.

---

*Synthesis produced 2026-08-22. Merged from 01-german.md, 02-eu.md, 03-pitfalls.md, 04-arch.md — same as-of date, same citation conventions, same severity scale. Build gates: case-law.md whitelist before checklists; corpus before quality claims; `law_as_of` pin on every output.*
