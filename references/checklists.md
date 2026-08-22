# Review Checklists — Phase 1 Clause Taxonomy → Pitfall Catalog Index

**As of 2026-08.** Companion to `pitfalls.md`: maps every Phase 1 clause type to the matching
pitfall catalog entries (P-IDs) and their trigger conditions. This file is a **derived index** —
all pitfall content (names, legal bases, severities, trigger/symptom descriptions) lives in
`pitfalls.md` and is referenced by ID here, never duplicated. If this index and `pitfalls.md`
disagree, `pitfalls.md` wins.

Usage: during Phase 2 (clause-by-clause), for each tagged clause run the checklist(s) matching
its clause type; a checklist item fires when its trigger condition matches the clause text.
Phase 3 (cross-cutting) runs the Contract-Wide Red Flags checklist (§ 15) over the whole contract.

> **Derivation note (packaging, 2026-08-22):** generated mechanically from `pitfalls.md` — one
> entry per catalog item, grouped by primary category, trigger conditions condensed from each
> item's "Why it is a problem" field. No pitfalls, legal rules, severities, or citations were
> added or changed; categories and P-IDs are authoritative from `pitfalls.md`.

## 1. Probation & Trial Periods

### P1 — Probation beyond six months

- **Clause type:** Probation clause
- **Severity:** High
- **Trigger:** § 622 Abs. 3 BGB limits the two-week notice period to "längstens sechs Monate" of probation. A longer formular probation is invalid under § 307 BGB; the 2-week notice window then collapses and the statutory notice periods of § 622 Abs. 1–2 BGB apply. For fixed-term contracts, § 15 Abs. 3 TzBfG requires the probation to be proportionate to the expected term and the nature of the work.

### P2 — Probation in a fixed-term contract without termination right

- **Clause type:** Probation clause / fixed-term clause
- **Severity:** High
- **Trigger:** Under § 15 Abs. 4 TzBfG a fixed-term contract is terminable by ordinary notice only if this is individually agreed or provided by an applicable collective agreement. A probation clause in a fixed-term contract therefore achieves nothing unless the contract also states the contract "kann mit gesetzlicher Frist gekündigt werden" — otherwise the employer cannot dismiss during probation at all.

### P3 — Mislabeled "training" or "orientation" period

- **Clause type:** Probation clause (disguised)
- **Severity:** Medium
- **Trigger:** If the contract provides a 2-week notice right for an "Einarbeitungsphase" beyond six months, the label does not immunize it: AGB review looks at substance. A longer "training" period with reduced notice is invalid under § 307 Abs. 1 BGB by reference to § 622 Abs. 3 BGB's six-month ceiling; conversely a mere training/ramp-up arrangement does not by itself justify a 2-week notice period.

### P4 — Notice period below statutory minimum outside probation

- **Clause type:** Termination clause
- **Severity:** High
- **Trigger:** § 622 Abs. 2 BGB grades the employer's notice period by years of service (1 month → up to 7 months after 20 years). An individual contract may only *lengthen* the statutory periods (§ 622 Abs. 5 BGB); a shorter period is ineffective and the statutory period applies (§ 622 Abs. 5 BGB reads: "für den Arbeitgeber geltende längere Kündigungsfristen als die gesetzlichen können einzelvertraglich vereinbart werden" — only extensions allowed; shortenings void).

## 2. Duration & Termination

### P5 — Fixed term without Sachgrund beyond 2 years / 3 extensions

- **Clause type:** Fixed-term clause
- **Severity:** Critical
- **Trigger:** § 14 Abs. 2 Satz 1 TzBfG allows a fixed term without objective cause for max. 2 years and max. 3 extensions within that window. Exceeding either limit voids the term: the contract becomes indefinite (§ 16 Satz 1 TzBfG) and the employee can sue for a declaration within 3 weeks of expiry (§ 17 TzBfG). A prior employment relationship with the same employer (Vorbeschäftigungsverbot, § 14 Abs. 2 Satz 2 TzBfG) blocks a further sachgrundlose Befristung; the BVerfG forbade the BAG's "more than 3 years ago" relaxation (BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, 1 BvR 1375/14).

### P6 — Kettenbefristung (chain of successive fixed terms)

- **Clause type:** Fixed-term clause (successive)
- **Severity:** High
- **Trigger:** Successive sachgrundlose Befristungen with the same employer are structurally barred by § 14 Abs. 2 Satz 2 TzBfG (Vorbeschäftigungsverbot). Even with a Sachgrund, a chain may be abusive under § 242 BGB (Rechtsmissbrauch) where the ground is a pretext, the intervals are artificially short, or the same work continues indefinitely; the BAG reviews chains case-by-case.

### P7 — Fixed-term renewal without Schriftform

- **Clause type:** Fixed-term clause / amendment clause
- **Severity:** Critical
- **Trigger:** § 14 Abs. 4 TzBfG and § 623 BGB require the fixed term (and any extension) to be agreed in writing (Schriftform, § 126 BGB). E-mail or oral extension → the fixed term is void; the contract runs indefinitely. Note: for § 41 SGB VI (Altersbefristung/Hinausschieben) Textform sufficed under Bürokratieentlastungsgesetz IV for the "Hinausschiebevereinbarung", but the new § 41 Abs. 2 SGB VI Befristung itself requires Schriftform — per IHK München, simple e-mail is ineffective and an indefinite contract results.

### P8 — Termination modalities / clause with irrevocable Kündigungsverzicht

- **Clause type:** Termination clause
- **Severity:** Medium
- **Trigger:** A blanket, irrevocable mutual waiver of ordinary termination for years is invalid: it unacceptably restricts the employee's freedom of occupation (Art. 12 GG) and is AGB-invalid under § 307 BGB unless the employee receives compensation (Abfindungsregelung) or a quid pro quo; the BAG permits only limited, compensated waivers (e.g. in the context of Aufhebungs-/Abwicklungsverträge). A one-sided waiver favoring the employer is void.

### P9 — Garden leave (Freistellung) clause — void since BAG 25.03.2026

- **Clause type:** Termination modality clause
- **Severity:** Critical
- **Trigger:** A pre-formulated (AGB) clause giving the employer the right to release the employee from work during the notice period was held **unwirksam** by the BAG on 25.03.2026 (5 AZR 108/25): it disadvantages the employee unreasonably (§ 307 Abs. 1 BGB) by forcing immediate loss of work and variable-pay opportunities without balancing the employee's interests (vacation, variable compensation, new-job flexibility). The clause is void; the employer may still unilaterally release only where justified in the individual case.

### P10 — Termination on change of control / "key man" clauses

- **Clause type:** Termination clause (special)
- **Severity:** Medium
- **Trigger:** A formular clause allowing the employee to terminate for convenience on a change of control, or allowing the employer to terminate upon a restructuring event without social justification, conflicts with the Kündigungsschutzgesetz (social justification for dismissals, § 1 KSchG; Wartezeit § 1 Abs. 1 KSchG) and with § 613a Abs. 4 BGB (dismissal on transfer of business is void). Such clauses are AGB-invalid unless carefully bounded and compensated.

### P59 — Waiver of part-time rights (§ 8 / 9a TzBfG)

- **Clause type:** Part-time / waiver clause
- **Severity:** Medium
- **Trigger:** § 8 TzBfG grants employees (employer > 15 employees) a right to reduce working hours with 3 months' lead; refusal is only possible for operational reasons, and an unanswered, timely application is **deemed granted** (§ 8 Abs. 5 TzBfG Fiktion). § 9a TzBfG (Brückenteilzeit, employer > 45 employees, tenure > 6 months) grants a right to a temporary reduction of 1–5 years. A contract clause waiving these rights in advance, or "announcing-deadline tricks" that steer the employee past the § 8 Abs. 2 Satz 2 TzBfG deadline, is ineffective and AGB-invalid: the statutory rights are non-waivable and the employee can invoke them notwithstanding the waiver.

## 3. Remuneration

### P11 — Salary below Mindestlohn

- **Clause type:** Salary clause
- **Severity:** Critical
- **Trigger:** The statutory minimum wage binds every employment relationship (MiLoG); from 1.1.2026 it is **13,90 €/hour**, rising to 14,60 € on 1.1.2027 (5th MiLoV). A below-minimum salary is void to that extent (§ 134 BGB); the employee can claim the difference; the employer commits an administrative offense (§ 21 MiLoG). Salary must be structured so that all remunerative components (fixed, commission, allowances) aggregate to ≥ minimum wage per hour actually worked; deductions and offsets are restricted (see P14).

### P12 — Flat overtime "Abgeltung" clause

- **Clause type:** Overtime clause
- **Severity:** Critical
- **Trigger:** A formular clause stating that "all overtime" or "usual overtime" is covered by the base salary is AGB-invalid: it fails transparency (§ 307 Abs. 1 Satz 2 BGB) because the employee cannot tell how many hours are compensated (BAG, Urt. v. 01.09.2010 – 5 AZR 517/09; Urt. v. 17.08.2011 – 5 AZR 406/10). Where the employee actually works overtime, it must be paid. An **effective** clause must state the number of overtime hours covered and the compensation.

### P13 — Unfettered bonus / discretion clause

- **Clause type:** Bonus clause
- **Severity:** High
- **Trigger:** "Bonus nach freiem Ermessen" or a bonus clause without objective criteria gives the employer unbounded discretion; under § 315 BGB the determination must be equitable, and a total absence of criteria fails AGB transparency. If the contract promises a bonus but omits target-setting, the employee can claim damages equal to 100 % of the target bonus (BAG, Urt. v. 12.12.2007 – 10 AZR 97/07).

### P14 — Salary deductions & Verrechnung

- **Clause type:** Salary/deduction clause
- **Severity:** High
- **Trigger:** Set-off against wage claims is restricted: § 394 BGB bars set-off against unpfändbare wage components; § 4 EFZG protects continued-pay claims during sickness; and the employee's wage claim is protected from garnishment up to the Pfändungsfreigrenzen (§§ 850 ff. ZPO), which limits contractual deductions. A formular clause allowing the employer to deduct "any amounts owed" from salary is AGB-invalid (unreasonable disadvantage, § 307 BGB) and void under § 394 BGB where it reaches protected amounts.

### P15 — Gratifikation/13th month with excessive Rückzahlungsklausel

- **Clause type:** Bonus/gratification clause
- **Severity:** High
- **Trigger:** Clawback (Rückzahlung) clauses on a special payment are only valid within tight BAG limits: up to 31.03. of the following year if the payment is >100 € but <1 monthly salary; up to the next possible termination date, max. 30.06., if ≥1 monthly salary; if it is pure compensation for past work (Entgeltcharakter), clawback is invalid altogether. Binding beyond 30.06., or binding for pure remuneration, is AGB-invalid and a disproportionate restriction of Art. 12 GG.

### P16 — Pay-gap / gender pay structure (EntgTranspG; EU 2023/970 pending)

- **Clause type:** Salary structure / pay transparency
- **Severity:** High (compliance risk; direct liability only after transposition, but individual equal-pay claims already exist)
- **Trigger:** The EntgTranspG (2017) grants individual pay information rights and equal-pay claims for comparable work (§§ 3, 7–15 EntgTranspG). EU Directive 2023/970 (Pay Transparency) required transposition by 7.6.2026 — Germany has **not yet** transposed (draft expected Q1 2026 per Deloitte; as of 2026-08 no statute in force; public employers bound directly since 8.6.2026). A contract salary banding or pay practice that yields systematically lower pay for women for equal work breaches § 3 EntgTranspG / Art. 157 TFEU and exposes the employer to back-pay and information claims; "gender-neutral" drafting is a contract-wide red flag check.

### P17 — Provision/commission with unilateral target changes

- **Clause type:** Commission clause
- **Severity:** High
- **Trigger:** A formular clause permitting the employer to unilaterally change targets, quotas, or commission rates (e.g. "im unternehmerischen Ermessen") violates § 315 BGB (equitable determination) and AGB transparency; retroactive cuts of already-earned commissions are invalid; the employee keeps earned commission claims. Handelsvertreter-style rules (§ 87 ff. HGB) inform but do not directly bind employees.

## 4. Working Time & Leave

### P18 — Vacation carry-over/forfeiture clause violating BUrlG / 15-month rule

- **Clause type:** Vacation clause
- **Severity:** High
- **Trigger:** § 7 Abs. 3 BUrlG allows carry-over only for urgent operational/personal reasons; statutory minimum leave (4 weeks, § 3 BUrlG) cannot be contracted away (§ 13 Abs. 1 BUrlG). Since BAG 19.02.2019 (9 AZR 541/15, 9 AZR 423/16), vacation forfeits only if the employer has informed the employee of the accrual and the expiry date and the employee nevertheless fails to take it; the 15-month cap (31.03. of the second following year) applies to long-term sick leave per EuGH C-214/10 (Schulte). A clause that forfeits leave "automatically" at year-end, or beyond the statutory framework, is void to the extent it covers statutory minimum leave.

### P19 — Holiday pay / Urlaubsentgelt miscalculation

- **Clause type:** Vacation/pay clause
- **Severity:** High
- **Trigger:** § 11 BUrlG requires continued pay during vacation equivalent to average earnings of the preceding 13 weeks (including overtime, commission, allowances). A clause paying only base salary, or excluding variable components from holiday pay, is invalid (§§ 13 Abs. 1, 11 BUrlG); underpayment claims accrue.

### P20 — Arbeitszeiterfassung gap (post-BAG 2022)

- **Clause type:** Working-time clause / general
- **Severity:** Medium
- **Trigger:** Since BAG 13.09.2022 (1 ABR 22/21), the employer must record **all** working time (begin, end, duration), based on § 3 Abs. 2 Nr. 1 ArbSchG read with EU law (CJEU C-55/18 CCOO); the ArbZG itself (§ 16 Abs. 2 ArbZG) requires only overtime recording, but the statutory reform (electronic recording, weekly-hours shift) was still pending as of 2026-08. A contract that silently assumes no recording, or assigns recording to the employee without tools, leaves the employer liable for compliance gaps and shifts the burden of proof on overtime claims.

### P21 — Sunday/holiday work without compensation

- **Clause type:** Working-time clause
- **Severity:** High
- **Trigger:** § 9 ArbZG bars Sunday/holiday work with narrow exceptions (§ 10 ArbZG); where permitted, § 11 ArbZG mandates at least 15 compensated Sundays/paid holidays per year plus compensatory rest. A clause waiving this or declaring Sunday work "abgegolten" is void (§§ 9, 11 ArbZG; § 134 BGB); also, absence of a Betriebsrat co-determination check (§ 87 Abs. 1 Nr. 2 BetrVG) in unionized establishments.

### P22 — Arbeit auf Abruf without 20/25 % statutory thresholds

- **Clause type:** Working-time clause
- **Severity:** High
- **Trigger:** If no minimum weekly hours are agreed, § 12 Abs. 1 Satz 3 TzBfG presumes **20 hours/week**; the employer may call in only up to 25 % above the agreed minimum (§ 12 Abs. 2 TzBfG, i.e. min. 20 h → max. 25 h) and may not go below the minimum by more than 20 %. A clause leaving hours open or allowing unlimited fluctuation is ineffective; the statutory fictions apply and back-pay follows.

## 5. Restrictive Covenants

### P23 — Post-contractual non-compete without Karenzentschädigung

- **Clause type:** Non-compete clause
- **Severity:** Critical
- **Trigger:** For employees, § 110 GewO (analogous to §§ 74 ff. HGB) requires: (1) the covenant must protect a legitimate business interest, (2) duration ≤ 2 years, and (3) mandatory compensation of at least **50 % of the last contractual remuneration** for the entire restraint period, payable even if the employee terminated. Missing or insufficient compensation voids the clause **entirely** — the employee is free to compete.

### P24 — Non-compete longer than 2 years

- **Clause type:** Non-compete clause
- **Severity:** Critical
- **Trigger:** Beyond 2 years the covenant is void (§ 74a Abs. 1 Satz 3 HGB) — no partial validity (the clause fails in full; the employee is not bound at all); courts do not "blue-pencil" the duration for employees.

### P25 — Non-solicit of employees/customers overreach

- **Clause type:** Non-solicit clause
- **Severity:** Medium
- **Trigger:** Blanket bans on "any contact with customers" or "soliciting any employee" post-termination are AGB-invalid as unreasonable restraints on occupation (Art. 12 GG; §§ 74a, 74b HGB analog): they must be limited to customers the employee actually serviced and employees whose recruitment would genuinely harm the employer, and may not operate as a disguised non-compete without compensation. Overbroad clauses are void in full (§ 307 BGB).

### P26 — Confidentiality clause with post-contractual effect

- **Clause type:** Confidentiality clause
- **Severity:** Medium
- **Trigger:** Confidentiality of business secrets during employment is lawful (§ 17 UWG protects trade secrets; GeschGehG). But a clause banning all disclosure of "any information" — including general skills, know-how, or information the employee must disclose to authorities — indefinitely is AGB-invalid (overbreadth, § 307 BGB), conflicts with the GeschGehG whistleblower carve-out (§ 5 GeschGehG), and cannot restrict the employee's right to report violations (HinSchG, see P34).

### P27 — Vertragsstrafe (penalty clause) in the employment contract

- **Clause type:** Penalty clause
- **Severity:** High
- **Trigger:** A formular penalty for termination (e.g. "for leaving within 2 years, 3 monthly salaries") is AGB-invalid: the BAG requires the penalty to be reasonable, proportionate to the protected interest, and not to deter lawful termination (Art. 12 GG; § 307 BGB); penalties for exercising the right to terminate are void. The penalized breach must be concretely described (BAG 8 AZR 130/13); a blanket "Nichtantritt" or "Abwerbung" penalty without limits fails. Where valid (e.g. for non-compete breach), the penalty must be quantified reasonably.

### P28 — IP/invention clauses conflicting with ArbEG

- **Clause type:** IP/invention clause
- **Severity:** High
- **Trigger:** Diensterfindungen belong to the employee until the employer claims them; the employer must claim within 4 months (§ 6 ArbEG) and pay reasonable compensation (§ 9 ArbEG); pre-assignment of future inventions in the contract is void (ArbEG §§ 4–13, 22: statutory provisions cannot be contracted away to the employee's detriment — § 22 ArbnErfG); blanket "all IP vests in employer" clauses are ineffective and can even destroy the employer's rights (no valid Inanspruchnahme). Post-reporting agreements are allowed (§ 22 ArbnErfG).

## 6. Post-contractual Obligations

### P29 — Zeugnis waiver before termination

- **Clause type:** Reference/waiver clause
- **Severity:** Critical
- **Trigger:** The right to a written (qualified) reference under § 109 GewO / § 630 BGB is a mandatory employee right. A waiver of the qualified reference **before the employment ends** is void (BAG, Urt. v. 18.06.2025 – 2 AZR 96/24 (B)): the employee is still in the dependency relationship; the waiver violates the protective purpose of § 109 GewO and is AGB-invalid. Only a waiver after termination is effective.

### P30 — Return-of-property overreach

- **Clause type:** Property return clause
- **Severity:** Low
- **Trigger:** The employer may require return of its property (laptops, keys, documents) — § 667 BGB analog (Herausgabe). But a formular clause demanding return of "all materials, including copies, notes, and personal devices", or withholding final pay until return, is AGB-invalid (§ 307 BGB; retention of salary is barred — pay is due regardless); personal data/devices must be excluded; the clause must not cover the employee's own property.

### P31 — Retention of documents / Arbeitspapiere

- **Clause type:** Documentation clause
- **Severity:** Medium
- **Trigger:** The employer must issue an Arbeitsbescheinigung (§ 312 SGB III), Lohnsteuerbescheinigung, and health-insurance certificates promptly; withholding them (or threatening to) as leverage is unlawful and can constitute a tort/statutory violation; the employee can compel issuance. A clause conditioning documents on release/waiver is void (§ 134 BGB; § 307 BGB).

## 7. Data Protection & Monitoring

### P32 — Consent clause exploiting imbalance (§ 26 Abs. 2 BDSG)

- **Clause type:** Data-protection/consent clause
- **Severity:** High
- **Trigger:** Under § 26 Abs. 2 BDSG, consent to data processing in employment is valid only if freely given — which is regularly doubted in formular employment contracts ("Koppelungsverbot"): a blanket consent covering all personal data, bundled with the contract's conclusion, is invalid; the processing then lacks a legal basis (violation of Art. 6/88 GDPR, § 26 BDSG, fines).

### P33 — CCTV/e-mail/Internet/GPS/BYOD monitoring clauses

- **Clause type:** Monitoring clause
- **Severity:** High
- **Trigger:** Covert or blanket monitoring of employees is unlawful: § 26 Abs. 1 BDSG requires a concrete purpose and proportionality; video surveillance must be justified under § 4 BDSG and may require works-council consent (§ 87 Abs. 1 Nr. 6 BetrVG); e-mail/Internet monitoring needs a policy + transparency; GPS tracking of vehicles/phones is only permitted for legitimate, proportionate purposes; BYOD access by the employer to private devices must be strictly limited. Formular clauses granting "unlimited monitoring rights" are void (§ 307 BGB) and constitute administrative offenses under the GDPR.

### P34 — Whistleblower-NDA conflicts with HinSchG

- **Clause type:** Confidentiality clause
- **Severity:** High
- **Trigger:** § 9 HinSchG carves out disclosures to internal/external reporting channels and authorities from confidentiality duties; § 39 HinSchG voids agreements that restrict the right to report or penalize reporting; § 36 HinSchG bans reprisals with burden-of-proof reversal. A broad NDA/confidentiality clause that bars "any disclosure to third parties including authorities" is void to that extent and invites damages claims.

## 8. Secondary Employment & Exclusivity

### P35 — Blanket ban on secondary employment

- **Clause type:** Secondary-employment clause
- **Severity:** High
- **Trigger:** A blanket ban ("any other employment requires approval; approval may be refused at discretion" / "any secondary activity is prohibited") is AGB-invalid and violates Art. 12 GG: the BAG requires a concrete impairment of the employer's interests to justify restrictions (BAG, Urt. v. 11.12.2001 – 9 AZR 464/00: an approval-reservation clause that permits arbitrary refusal is ineffective; only concrete impairment justifies a ban). EU Directive 2019/1152 (transposed 2022) prohibits clauses barring other employment entirely.

### P36 — Exclusivity tied to remuneration model

- **Clause type:** Secondary-employment clause
- **Severity:** Medium
- **Trigger:** Contracting "exclusivity" in exchange for a special allowance (e.g. "Nebentätigkeitsverzichtszuschlag") does not cure the AGB problem: the clause still restricts Art. 12 GG and must be limited to concrete impairment; if the allowance is later removed, the exclusivity collapses. EU law (2019/1152) bars exclusivity clauses outright in the EU; German transposition did not create an explicit prohibition but the BAG case law achieves the same for employees.

## 9. Family/Care & Disability

### P37 — Maternity clauses vs. MuSchG

- **Clause type:** Special clause
- **Severity:** Critical
- **Trigger:** Dismissal during pregnancy/maternity leave (up to 4 months post-partum) is prohibited (§ 17 MuSchG) — any clause terminating on pregnancy, or a fixed term linked to pregnancy, is void (§ 134 BGB); fixed-term contracts ending during pregnancy are automatically extended (§ 17 Abs. 1 Satz 1 Nr. 1 MuSchG). The employer bears the burden of proving it did not know of the pregnancy in dismissal disputes.

### P38 — Parental-leave restrictions vs. BEEG

- **Clause type:** Special clause
- **Severity:** High
- **Trigger:** The right to parental leave (up to 3 years per child, § 15 BEEG) cannot be contracted away; the employer may not refuse, and termination based on the leave request is prohibited (§ 18 BEEG). A clause waiving parental leave or requiring repayment of benefits upon leave is void; also § 15 Abs. 7 BEEG (part-time during Elternzeit) may not be restricted contractually.

### P39 — Care-leave restrictions (PflegeZG/Familienpflegezeit)

- **Clause type:** Special clause
- **Severity:** High
- **Trigger:** Short-term care leave (10 days, § 2 PflegeZG), care leave (up to 6 months, § 3 PflegeZG), and Familienpflegezeit (§ 2 FPfZG) are statutory rights; the notice requirements (§ 3 PflegeZG: 10 days' notice with medical certificate) cannot be tightened contractually; dismissal during care leave is prohibited (§ 5 PflegeZG). Contract clauses conditioning leave on employer consent are void.

### P40 — Disability clauses violating SGB IX

- **Clause type:** Special clause
- **Severity:** High
- **Trigger:** Discrimination on disability grounds is barred (AGG § 7, § 1; SGB IX §§ 164 ff. — employer's duty to provide accommodations/barrierefreie Beschäftigung; special dismissal protection § 168 SGB IX requires the Inklusionsamt's consent). A clause declaring the employee "able-bodied" as a condition, or excluding accommodations, is void (§§ 134, 138 BGB; § 7 AGG) and triggers damages claims (§ 15 AGG).

## 10. Collective-Law Interplay

### P41 — Dynamic reference to expired collective agreement

- **Clause type:** Reference clause
- **Severity:** Medium
- **Trigger:** A dynamic reference ("the applicable collective agreement in its current version") to a specific TV that expires or is terminated creates a gap: Nachwirkung (§ 4 Abs. 5 TVG) preserves only normative terms that are not regulated otherwise — new TV versions no longer flow through; if the employer leaves the association, the reference may fail altogether. Formular dynamic references to non-parties' or future TVs are AGB-risk (unforeseeable changes). Conversely, static references freeze the old version. The outcome: uncertainty on pay and terms, and disputes over which version applies.

### P42 — Betriebsvereinbarung reference without gap regulation

- **Clause type:** Reference clause
- **Severity:** Medium
- **Trigger:** References to "the applicable Betriebsvereinbarungen" are common but, if the works council is dissolved or the BV is terminated, the terms lapse (Nachwirkung of BVs only where provided, § 77 Abs. 6 BetrVG — no general Nachwirkung for BVs!). The contract then has a gap. Formular references must not delegate essential terms (pay, hours) entirely to future BVs (intransparent, § 307 BGB).

### P43 — § 613a BGB collective-agreement continuity mishandled

- **Clause type:** Transfer clause / general
- **Severity:** High
- **Trigger:** On a business transfer (§ 613a BGB), the transferee steps into the employment relationships; collective agreements/works agreements applicable to the transferor continue normatively and may be transformed into individual terms (§ 613a Abs. 1 Satz 2–3 BGB); dismissal because of the transfer is void (§ 613a Abs. 4 BGB); the transferee must inform (§ 613a Abs. 5 BGB). A new employment contract after a transfer that silently abandons the continued terms, or that makes the transfer itself a ground for changing terms, is void/invalid (§§ 134, 138, 307 BGB; § 613a Abs. 4 BGB).

## 11. Cross-Border & Posting

### P44 — Choice-of-law clause evading mandatory German protection

- **Clause type:** Choice-of-law clause
- **Severity:** High
- **Trigger:** Rome I Art. 8 protects employees: absent a choice, the law of the habitual workplace applies; even with a choice of law (e.g. "English law"), the employee retains the mandatory protective provisions of the law that would apply absent choice (Art. 8 Abs. 1, 2 Rome I). A clause selecting a foreign law to strip German minimum protections (notice periods, minimum wage, vacation, KSchG where applicable) is ineffective to that extent — and, per BAG 18.06.2025 (2 AZR 96/24 (B)), cannot defeat the Zeugnis claim or other zwingende Arbeitnehmerschutzbestimmungen.

### P45 — Posting gaps (AEntG/Arbeitnehmer-Entsendegesetz)

- **Clause type:** Posting clause
- **Severity:** High
- **Trigger:** Posting employees to Germany (or from Germany) triggers the AEntG core employment terms (minimum wage, working time, vacation, industry-specific minimum conditions — § 8 AEntG), mandatory written notice (§ 18 AEntG), and the EU Posting Directive (96/71/EC as amended by 2018/957). A contract that applies only the home-country law and omits the German core terms violates mandatory law; the employee can claim the German minima. Conversely, German employers posting abroad must observe the posting rules of the destination state.

## 12. Formalities & Documentation

### P46 — Missing NachwG § 2 terms

- **Clause type:** Documentation clause (whole contract)
- **Severity:** Critical
- **Trigger:** Since 1.8.2022, § 2 NachwG requires a written record of a long catalogue of essential terms (identity of parties, start date, job description, pay components incl. overtime, working hours, vacation, notice periods, place of work, training rights, etc.) within 7 days (core) / 1 month (other terms) of commencement; since 1.1.2025 the record may be delivered in Textform/electronic form under conditions (§ 2 Abs. 1 Satz 2 NachwG). Omissions are administrative offenses (§ 4 NachwG, fine up to €2,000 per case) and shift the burden of proof on the omitted terms.

### P47 — § 126a BGB digital signature vs. Schriftform

- **Clause type:** Signature clause
- **Severity:** Critical
- **Trigger:** Where the law requires Schriftform (§ 126 BGB) — fixed-term agreements (§ 14 Abs. 4 TzBfG, § 623 BGB), Kündigung (§ 623 BGB), Aufhebungsvertrag, non-compete (in part), § 41 SGB VI Befristung — only wet-ink signatures or a qualified electronic signature (§ 126a BGB) satisfy it. Simple e-mail, PDF without QES, or a scanned signature is ineffective; for a Befristung the consequence is an indefinite contract; for a Kündigung, nullity (§ 125 BGB). Textform (§ 126b BGB) suffices only where the statute says so (e.g. § 3 NachwG info duties, notice of part-time requests, § 41 SGB VI Hinausschieben).

### P48 — Textform misuse for consent/waivers

- **Clause type:** Consent/waiver clause
- **Severity:** High
- **Trigger:** Several labor-law acts expressly require more than Textform: consent to data processing should be documented (§ 26 Abs. 2 Satz 3 BDSG: "in Textform" — but formular consent in an employment contract is invalid per se, see P32); the Niederschrift under NachwG was Schriftform until 1.1.2025, now Textform possible; Aufhebungsverträge and Kündigungen require Schriftform (§ 623 BGB). Using a mere e-mail confirmation for a Kündigung or Aufhebungsvertrag is void.

### P58 — Forfeiture clauses (Ausschlussfristen) too short or blanket

- **Clause type:** Forfeiture/claim-bar clause
- **Severity:** High
- **Trigger:** A valid forfeiture clause in a form employment contract must have at least two stages: written assertion within at least 3 months, then judicial assertion within at least 3 months after rejection (BAG 25.05.2005 – 5 AZR 572/04). Clauses with a shorter first stage are invalid (BAG 28.05.2014 – 5 AZR 422/12). A blanket clause covering "all claims" is void insofar as it covers claims for intentional breach (Vorsatzhaftung, § 276 Abs. 3 BGB; BAG 26.11.2020 – 8 AZR 58/20) and — since 2015 — minimum-wage claims (BAG 18.09.2018 – 9 AZR 162/18). The written-claim requirement must not be tightened to an unachievable form (e-mail may suffice where the clause does not demand more; BAG 16.12.2009 – 5 AZR 888/08).

## 13. Mobility & Workplace

### P49 — Home office / mobile work clauses without core terms

- **Clause type:** Workplace clause
- **Severity:** Medium
- **Trigger:** A clause granting "mobile work at the employee's discretion" without defining scope (days, location, data-security duties, reimbursement of costs, work-injury coverage, availability) creates disputes over: Arbeitsunfall coverage (§ 8 SGB VII — home office counts as insured workplace), equipment costs (§ 670 BGB analog — expenses reimbursement), and working-time recording (see P20). Formular clauses that shift all costs/risks to the employee are AGB-invalid.

### P50 — Travel time excluded from working time/pay

- **Clause type:** Travel-time clause
- **Severity:** High
- **Trigger:** For employees without a fixed workplace (Außendienst, Techniker), travel between customers is working time and must be paid (BAG, Urt. v. 11.07.2018 – 5 AZR 595/17; Urt. v. 17.10.2018 – 5 AZR 553/17: travel on foreign assignment is working time). A clause declaring "all travel time is not working time and unpaid" is void (§ 307 BGB); the employee can claim pay for the excluded hours.

### P51 — Work equipment cost-shifting

- **Clause type:** Equipment clause
- **Severity:** Medium
- **Trigger:** The employer must bear the costs of work equipment required for the job (tools, PPE per ArbSchG § 3, phone/PC where functionally required); a formular clause requiring the employee to buy/maintain its own equipment (BYOD without compensation) is AGB-invalid to the extent it shifts necessary costs (§ 307 BGB; § 670 BGB analog). PPE cost-shifting is a statutory violation (ArbSchG/ArbStättV).

### P52 — Relocation clauses

- **Clause type:** Mobility clause
- **Severity:** Medium
- **Trigger:** A clause allowing the employer to relocate the employee "anywhere in Germany/Europe" at will is AGB-invalid: it must respect § 106 GewO (Weisungsrecht nach billigem Ermessen) and the contract's place-of-work definition; an unlimited Versetzungsvorbehalt is unreasonable (§ 307 BGB; BAG practice requires a reasonable bound, notice of costs, and compensation for increased commuting). For works-council co-determination see § 95 BetrVG.

## 14. Special Clauses

### P53 — Kündigungsschutz waiver / Klageverzicht in severance context

- **Clause type:** Aufhebungs-/Abwicklungsvertrag clause
- **Severity:** High
- **Trigger:** Waivers of Kündigungsschutz claims (Klageverzicht) in an Aufhebungsvertrag are valid only if individually negotiated, transparent, and not procured by unlawful pressure; the BAG requires "faires Verhandeln" (BAG, Urt. v. 07.02.2019 – 6 AZR 75/18) — an Aufhebungsvertrag concluded under threat of a dismissal that is not seriously intended may be void (§ 123 BGB) or violate the fair-negotiation principle; blanket Ausgleichsklauseln ("all claims of any kind are settled") that sweep in non-waivable statutory claims (Zeugnis, P29) or unknowable future claims are invalid; the Aufhebungsvertrag itself must be in Schriftform (§ 623 BGB).

### P54 — Abfindungsklausel below statutory severance expectations

- **Clause type:** Severance clause
- **Severity:** Medium
- **Trigger:** There is no statutory severance entitlement absent a Sozialplan or § 1a KSchG (Abfindungsanspruch: 0.5 monthly salaries per year of service if the employer offers severance to avoid a dismissal dispute, § 1a Abs. 1, 2 KSchG). A formular clause that (a) caps severance below the § 1a KSchG level, (b) makes severance conditional on a waiver of all claims including non-waivable ones, or (c) is intransparent about triggers, is AGB-invalid and may fail to exclude the § 1a claim.

### P55 — Anrechnung Vorbeschäftigungszeiten (forfeiture of seniority)

- **Clause type:** Seniority clause
- **Severity:** Medium
- **Trigger:** Clauses stating that "prior employment with the employer/its predecessors is not credited" collide with: § 622 Abs. 2 BGB (notice-period grading by years of service — the BAG counts prior service in the same company, and § 622 Abs. 2 Satz 2 BGB's age-25 carve-out is EU-law-incompatible, see P4), § 1 KSchG Wartezeit (6 months, not excludable), and § 613a BGB continuity on transfers (P43). Contractual exclusion of service credit is ineffective where statutes mandate counting; otherwise it may be AGB-valid only if transparent and not discriminatory.

### P56 — Wertsicherungsklausel (indexation clause)

- **Clause type:** Salary-adjustment clause
- **Severity:** Medium
- **Trigger:** Under the Preisklauselgesetz (PrKG, since 14.9.2007), indexation of monetary obligations is generally barred unless it falls within the exceptions (§§ 2–7 PrKG: long-term contracts § 3, cost-element clauses § 4, etc.). Employment contracts rarely qualify (short term); a formular automatic CPI-indexation of salary is void (§ 1 Abs. 1, 2 PrKG; § 134 BGB) — the salary stays fixed and the indexation is unenforceable; conversely, one-sided "Nur-Erhöhung" clauses fail PrKG requirements.

### P57 — Arbitration/Mediation clauses

- **Clause type:** Dispute-resolution clause
- **Severity:** High
- **Trigger:** Arbitration agreements in employment contracts are **prohibited** by § 101 Abs. 1, 2 ArbGG unless the employee is an executive (§ 14 Abs. 2 KSchG) or a collective agreement provides otherwise; a formular arbitration clause is void (§ 134 BGB; the labor courts retain jurisdiction). Mediation clauses are permissible but must not impose cost burdens or time bars on the employee's right of access to the labor courts (§ 4 KSchG 3-week deadline cannot be tolled by a mediation agreement; a mandatory pre-mediation that jeopardizes the deadline is AGB-invalid).

### P60 — AÜG temp-agency contract issues

- **Clause type:** Temp-agency clause
- **Severity:** High
- **Trigger:** If an assignment is made without an AÜG permit, the contracts are void and employment is deemed to exist with the user undertaking (§§ 9, 10 AÜG Fiktion). Equal pay/conditions with comparable employees of the user is the statutory rule (§ 8 AÜG Gleichstellungsgrundsatz); deviation requires a sectoral collective agreement and, after 9 months, the deviation ends (max. 15 months step-up). The maximum assignment duration is 18 months to the same user (§ 17a AÜG); exceeding it triggers the deemed-employment fiction. Fee-splitting is prohibited (§ 9 Abs. 2 AÜG). A contract clause that waives equal pay, extends the assignment beyond 18 months, or shifts permit responsibility to the employee is void/ineffective.

### P61 — Insolvency clauses

- **Clause type:** Insolvency clause
- **Severity:** Medium
- **Trigger:** On insolvency, employment relationships continue with the insolvency estate (§ 108 InsO); the insolvency administrator may terminate with **3 months' notice** regardless of longer contractual notice periods, without KSchG social justification (§ 113 InsO); pre-insolvency wage claims are Insolvenzforderungen (quota), post-opening wages are Masseverbindlichkeiten (§ 55 InsO); Insolvenzgeld (§§ 165 ff. SGB III) covers the last 3 months. Contract clauses purporting to shorten the administrator's notice, to terminate automatically on insolvency, or to waive claims in anticipation of insolvency are void: the statutory rules are mandatory and override the clause (§§ 134, 138 BGB).

## 15. Contract-Wide Red Flags (cross-cutting, Phase 3)

Run over the whole contract during Phase 3, not per clause:

1. **Missing NachwG terms** — any contract lacking the § 2 NachwG catalogue (pay components, overtime rules, working hours, notice periods, place of work, TV/BV references, training, retirement provision) is an administrative offense (§ 4 NachwG, up to €2,000) and shifts proof burdens (P46).

2. **Internal contradictions** — e.g. probation clause vs. termination clause, fixed-term clause vs. "unbefristet" preamble, bonus promise vs. Freiwilligkeitsvorbehalt, Freistellungsklausel vs. variable-pay clause. Under § 305c Abs. 2 BGB ambiguities resolve against the drafter.

3. **Gaps** — no notice period (statute fills in § 622 BGB — usually fine but must be flagged), no place of work, no Arbeitszeit definition, no Überstundenregelung, no TV reference → gaps invite § 306 Abs. 2 BGB defaults and disputes.

4. **References to expired/terminated collective agreements** — dynamic references to lapsed TVs (P41) or BVs without Fortgeltung (P42) → pay/condition gaps; must be flagged for verification against the current TV register.

5. **Non-gender-neutral pay structure** — pay bands or criteria discriminating by gender (P16) violate EntgTranspG/Art. 157 TFEU and, post-2026, the pending EU 2023/970 transposition (public employers bound since 8.6.2026).

6. **Boilerplate from other jurisdictions** — US/UK legalese ("at will", "entire agreement" without German statutory interplay, "equitable relief", choice-of-law to foreign law, indemnity language, "no oral modification") — much of it is void or misleading under German mandatory law (P44, P47, P57, P29); must be translated into German-law-compliant terms.

7. **Gesamtzusage/Anspruch aufrecht "Tätigkeit nach freiem Ermessen"** — job-duties clauses delegating everything to the employer's discretion fail § 106 GewO/§ 307 BGB transparency.

8. **`law_in_flux` sweep** — any finding touching ArbZG hours, fixed-term limits (§ 14 TzBfG), pay transparency (EU 2023/970), or platform work must carry the pending-reform note (July-2026 coalition package, ArbZG electronic recording, Platform Work Directive deadline 2.12.2026 — none enacted as of 2026-08).

---

P-IDs referenced above resolve in `references/pitfalls.md`; statute/case-law bases cited there
are the authority for each entry. See `SKILL.md` Phase 2/Phase 3 loading map for when this file
is loaded (Phase 2 fully; Phase 3 NachwG/AGB sections).