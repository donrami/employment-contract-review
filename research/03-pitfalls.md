# Pitfalls Taxonomy — Master Catalog of German Employment-Contract Pitfalls

**As of 2026-08.** This catalog enumerates the recurring legal pitfalls an agentic skill must detect when assessing German employment contracts. Legal bases were verified against statute text and BAG/BVerfG/EuGH decisions via web research on 2026-08-22; all citations carry URLs. Case numbers without a confirming source are marked `[unverified]`. Severity reflects the employee-protective default of German labor law: formular (pre-formulated, AGB) clauses are construed against the drafter (§ 305c Abs. 2 BGB) and are invalid if they disadvantage the employee contrary to good faith (§ 307 Abs. 1 BGB), which statutory provisions cannot remedy (§ 307 Abs. 2 Nr. 1 BGB).

## Severity Criteria

- **Critical** — Clause is void (§§ 134, 138, 307–309 BGB) or violates a mandatory statutory provision (statutory violation), creating direct liability, nullifying the term (e.g. fixed term → indefinite contract), or exposing the employer to fines. Requires immediate correction.
- **High** — Likely AGB-invalid under settled BAG case law, or creates significant financial/legal risk (back-pay claims, restitution, loss of enforceability of restrictive covenant). High probability a court would strike it.
- **Medium** — Risky or unsettled: valid only under narrow conditions, depends on facts, or rests on recent/reversed case law; drafters should tighten language.
- **Low** — Drafting weakness / best-practice gap: ambiguity, intransparency, or missing formal elements that invite dispute or fail AGB transparency review, but no immediate nullity.

---

## 1. Probation & Trial Periods

### P1 — Probation beyond six months
- **Name:** Probezeit über sechs Monate / Probation longer than six months
- **Category:** Probation & trial periods
- **Clause type:** Probation clause
- **Why it is a problem:** § 622 Abs. 3 BGB limits the two-week notice period to "längstens sechs Monate" of probation. A longer formular probation is invalid under § 307 BGB; the 2-week notice window then collapses and the statutory notice periods of § 622 Abs. 1–2 BGB apply. For fixed-term contracts, § 15 Abs. 3 TzBfG requires the probation to be proportionate to the expected term and the nature of the work.
- **Legal basis:** § 622 Abs. 3 BGB; § 15 Abs. 3 TzBfG; BAG, Urt. v. 30.10.2025 – 2 AZR 160/24 (no fixed "25 % rule" for fixed-term probation; case-by-case proportionality; 4 months for a 1-year contract with onboarding plan upheld) — https://www.bundesarbeitsgericht.de/presse/probezeitkuendigung-im-befristeten-arbeitsverhaeltnis/
- **Severity:** High
- **Typical clause language:**
```text
Die ersten zwölf Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.
```
- **Recommended fix:**
```text
Die ersten sechs Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.
```
For fixed-term contracts ≤ 2 years, calibrate probation to the term (BAG 2025: case-by-case; short terms → shorter probation); ≥ 6 months in a 1-year contract is defensible only with documented onboarding phases.
- **Uncertainty:** BAG 2 AZR 160/24 (30.10.2025) explicitly rejected the LAG's 25 % rule of thumb; proportionality now turns on individual facts (expected duration, nature of work, onboarding plan).

### P2 — Probation in a fixed-term contract without termination right
- **Name:** Probezeit ohne vereinbarte Kündbarkeit im befristeten Vertrag / Probation in a fixed-term contract without agreed terminability
- **Category:** Probation & trial periods
- **Clause type:** Probation clause / fixed-term clause
- **Why it is a problem:** Under § 15 Abs. 4 TzBfG a fixed-term contract is terminable by ordinary notice only if this is individually agreed or provided by an applicable collective agreement. A probation clause in a fixed-term contract therefore achieves nothing unless the contract also states the contract "kann mit gesetzlicher Frist gekündigt werden" — otherwise the employer cannot dismiss during probation at all.
- **Legal basis:** § 15 Abs. 4 TzBfG; see BAG, Urt. v. 30.10.2025 – 2 AZR 160/24 (contract explicitly "mit den gesetzlichen Fristen kündbar") — https://www.bundesarbeitsgericht.de/presse/probezeitkuendigung-im-befristeten-arbeitsverhaeltnis/
- **Severity:** High
- **Typical clause language:**
```text
Das Arbeitsverhältnis ist befristet auf zwölf Monate. Die ersten vier Monate gelten als Probezeit.
```
- **Recommended fix:**
```text
Das Arbeitsverhältnis ist befristet auf zwölf Monate und kann während der Probezeit mit einer Frist von zwei Wochen, danach mit der gesetzlichen Frist gekündigt werden. Die ersten vier Monate gelten als Probezeit.
```
- **Uncertainty:** None on the statutory rule; only the proportionality assessment of the probation length is fact-dependent (see P1).

### P3 — Mislabeled "training" or "orientation" period
- **Name:** Als „Einarbeitungszeit"/„Trainingsphase" getarnte Probezeit / Mislabeled "training" period
- **Category:** Probation & trial periods
- **Clause type:** Probation clause (disguised)
- **Why it is a problem:** If the contract provides a 2-week notice right for an "Einarbeitungsphase" beyond six months, the label does not immunize it: AGB review looks at substance. A longer "training" period with reduced notice is invalid under § 307 Abs. 1 BGB by reference to § 622 Abs. 3 BGB's six-month ceiling; conversely a mere training/ramp-up arrangement does not by itself justify a 2-week notice period.
- **Legal basis:** § 622 Abs. 3 BGB (ceiling), § 307 Abs. 1, 2 Nr. 1 BGB; analogous reasoning to BAG 2 AZR 160/24 (probation requires Erprobung; length judged by content, not label) — https://www.bundesarbeitsgericht.de/presse/probezeitkuendigung-im-befristeten-arbeitsverhaeltnis/
- **Severity:** Medium
- **Typical clause language:**
```text
Die ersten neun Monate dienen der Einarbeitung. Während dieser Zeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.
```
- **Recommended fix:** Use the term "Probezeit", cap at six months, and keep any reduced notice period inside that window:
```text
Die ersten sechs Monate gelten als Probezeit; während dieser Zeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden. Eine anschließende Einarbeitungsphase ist vertraglich nicht mit einer verkürzten Kündigungsfrist verbunden.
```
- **Uncertainty:** None material; courts assess substance, not labels.

### P4 — Notice period below statutory minimum outside probation
- **Name:** Kündigungsfrist unterhalb der gesetzlichen Staffelung / Notice period below the statutory minimum
- **Category:** Probation & trial periods / Duration & termination
- **Clause type:** Termination clause
- **Why it is a problem:** § 622 Abs. 2 BGB grades the employer's notice period by years of service (1 month → up to 7 months after 20 years). An individual contract may only *lengthen* the statutory periods (§ 622 Abs. 5 BGB); a shorter period is ineffective and the statutory period applies (§ 622 Abs. 5 BGB reads: "für den Arbeitgeber geltende längere Kündigungsfristen als die gesetzlichen können einzelvertraglich vereinbart werden" — only extensions allowed; shortenings void).
- **Legal basis:** § 622 Abs. 2, 5 BGB; § 134 BGB. EU-law overlay: § 622 Abs. 2 Satz 2 BGB (ignoring service before age 25) held incompatible with EU law — EuGH, Urt. v. 19.01.2010 – C-555/07 (Kücükdeveci) and BAG, Urt. v. 01.09.2010 – 5 AZR 700/09 (service before age 25 counts) — https://www.haufe.de/id/entscheidung/bag-urteil-vom-01092010-5-azr-70009-HI2538755.html
- **Severity:** High
- **Typical clause language:**
```text
Das Arbeitsverhältnis kann von beiden Seiten mit einer Frist von einem Monat zum Monatsende gekündigt werden.
```
- **Recommended fix:**
```text
Die Kündigungsfristen richten sich für den Arbeitgeber nach § 622 Abs. 2 BGB in der jeweils geltenden Fassung. Für den Arbeitnehmer gilt eine Frist von vier Wochen zum Fünfzehnten oder zum Ende eines Kalendermonats; längere Fristen für den Arbeitnehmer bedürfen gesonderter Vereinbarung.
```
(Deletion note: if the contract is silent, § 622 BGB applies by default — silence is safe.)
- **Uncertainty:** The age-25 carve-out (§ 622 Abs. 2 Satz 2 BGB) remains on the books but is disapplied by courts as EU-law-incompatible; contracts should not copy it.

---

## 2. Duration & Termination

### P5 — Fixed term without Sachgrund beyond 2 years / 3 extensions
- **Name:** Sachgrundlose Befristung über 2 Jahre / 3 Verlängerungen / Fixed term without cause exceeding 2 years or 3 renewals
- **Category:** Duration & termination
- **Clause type:** Fixed-term clause
- **Why it is a problem:** § 14 Abs. 2 Satz 1 TzBfG allows a fixed term without objective cause for max. 2 years and max. 3 extensions within that window. Exceeding either limit voids the term: the contract becomes indefinite (§ 16 Satz 1 TzBfG) and the employee can sue for a declaration within 3 weeks of expiry (§ 17 TzBfG). A prior employment relationship with the same employer (Vorbeschäftigungsverbot, § 14 Abs. 2 Satz 2 TzBfG) blocks a further sachgrundlose Befristung; the BVerfG forbade the BAG's "more than 3 years ago" relaxation (BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, 1 BvR 1375/14).
- **Legal basis:** § 14 Abs. 2, 16, 17 TzBfG; BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, 1 BvR 1375/14 — https://cms.law/de/deu/legal-updates/Handlungsbedarf-bei-befristeten-Arbeitsverhaeltnissen-Bundesverfassungsgericht-kippt-BAG-Rechtsprechung-zur-Vorbeschaeftigung ; exception for pensioners: § 41 Abs. 2 SGB VI (since 1.1.2026, caps 8 years / 12 contracts) — https://www.ihk-muenchen.de/ratgeber/recht/arbeitsrecht/bestehende-arbeitsverhaeltnisse-kuendigung-sozialversicherung/befristete-beschaeftigung-rentner/
- **Severity:** Critical
- **Typical clause language:**
```text
Das Arbeitsverhältnis wird ohne sachlichen Grund für die Dauer von 30 Monaten befristet geschlossen. Es kann zweimal verlängert werden.
```
- **Recommended fix:** Cap at 24 months with max. 3 extensions total (a 4th renewal voids it); if longer is needed, draft an objective Sachgrund under § 14 Abs. 1 TzBfG (Vertretung, Projektbezug, etc.) with the ground stated in the contract:
```text
Das Arbeitsverhältnis wird bis zum [Datum] befristet geschlossen, da die Arbeitnehmerin zur Vertretung von [Name] im Wege der Elternzeit [Sachgrund] eingestellt wird.
```
- **Uncertainty:** The Vorbeschäftigungsverbot (§ 14 Abs. 2 Satz 2 TzBfG) was softened only for pensioners (§ 41 Abs. 2 SGB VI, in force 1.1.2026; scope for never-employed-by-this-employer pensioners debated — IHK München flags the point as "umstritten"). For all other employees the prohibition applies irrespective of the gap since prior employment.

### P6 — Kettenbefristung (chain of successive fixed terms)
- **Name:** Kettenbefristung / Chain of successive fixed-term contracts
- **Category:** Duration & termination
- **Clause type:** Fixed-term clause (successive)
- **Why it is a problem:** Successive sachgrundlose Befristungen with the same employer are structurally barred by § 14 Abs. 2 Satz 2 TzBfG (Vorbeschäftigungsverbot). Even with a Sachgrund, a chain may be abusive under § 242 BGB (Rechtsmissbrauch) where the ground is a pretext, the intervals are artificially short, or the same work continues indefinitely; the BAG reviews chains case-by-case.
- **Legal basis:** § 14 Abs. 2 Satz 2 TzBfG; § 242 BGB; BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14, 1 BvR 1375/14 (Kettenbefristung must be excluded; exceptions only where no risk of a chain: long-past, qualitatively different, or very short prior employment) — https://cms.law/de/deu/legal-updates/Handlungsbedarf-bei-befristeten-Arbeitsverhaeltnissen-Bundesverfassungsgericht-kippt-BAG-Rechtsprechung-zur-Vorbeschaeftigung
- **Severity:** High
- **Typical clause language:**
```text
An das bisherige, zum 31.12.2025 befristete Arbeitsverhältnis schließt sich ein weiteres befristetes Arbeitsverhältnis vom 01.01.2026 bis zum 30.06.2026 an, wiederum ohne sachlichen Grund.
```
- **Recommended fix:** No chain without a genuine, documented Sachgrund per extension; where possible, convert to an indefinite contract. For pensioners, § 41 Abs. 2 SGB VI (since 1.1.2026) permits repeated sachgrundlose Befristung up to 8 years total / 12 contracts — https://www.ihk-muenchen.de/ratgeber/recht/arbeitsrecht/bestehende-arbeitsverhaeltnisse-kuendigung-sozialversicherung/befristete-beschaeftigung-rentner/
- **Uncertainty:** Abuse-of-rights review is fact-intensive (length of intervals, nature of work, whether the Sachgrund is real). § 41 Abs. 2 SGB VI application to persons never previously employed by that employer is disputed.

### P7 — Fixed-term renewal without Schriftform
- **Name:** Befristungsverlängerung ohne Schriftform / Fixed-term extension not in writing
- **Category:** Duration & termination
- **Clause type:** Fixed-term clause / amendment clause
- **Why it is a problem:** § 14 Abs. 4 TzBfG and § 623 BGB require the fixed term (and any extension) to be agreed in writing (Schriftform, § 126 BGB). E-mail or oral extension → the fixed term is void; the contract runs indefinitely. Note: for § 41 SGB VI (Altersbefristung/Hinausschieben) Textform sufficed under Bürokratieentlastungsgesetz IV for the "Hinausschiebevereinbarung", but the new § 41 Abs. 2 SGB VI Befristung itself requires Schriftform — per IHK München, simple e-mail is ineffective and an indefinite contract results.
- **Legal basis:** § 14 Abs. 4 TzBfG; § 623 BGB (Schriftform); § 125 BGB (form defect → void); IHK München on § 41 Abs. 2 SGB VI — https://www.ihk-muenchen.de/ratgeber/recht/arbeitsrecht/bestehende-arbeitsverhaeltnisse-kuendigung-sozialversicherung/befristete-beschaeftigung-rentner/
- **Severity:** Critical
- **Typical clause language:**
```text
Per E-Mail: "Wir verlängern Ihr Arbeitsverhältnis um weitere sechs Monate bis zum 31.12.2026."
```
- **Recommended fix:** Written, signed (or qualified e-signature per § 126a BGB) amendment referencing the original contract and expressly stating the new end date and that all other terms continue:
```text
Die Parteien sind sich einig, dass das mit Vertrag vom [Datum] befristet begründete Arbeitsverhältnis um sechs Monate bis zum 31.12.2026 verlängert wird. Im Übrigen bleiben die bisherigen Vertragsbedingungen unverändert bestehen.
```
- **Uncertainty:** None — Schriftform for Befristung is settled.

### P8 — Termination modalities / clause with irrevocable Kündigungsverzicht
- **Name:** Unwiderruflicher Kündigungsverzicht / Irrevocable waiver of termination rights
- **Category:** Duration & termination
- **Clause type:** Termination clause
- **Why it is a problem:** A blanket, irrevocable mutual waiver of ordinary termination for years is invalid: it unacceptably restricts the employee's freedom of occupation (Art. 12 GG) and is AGB-invalid under § 307 BGB unless the employee receives compensation (Abfindungsregelung) or a quid pro quo; the BAG permits only limited, compensated waivers (e.g. in the context of Aufhebungs-/Abwicklungsverträge). A one-sided waiver favoring the employer is void.
- **Legal basis:** §§ 134, 138, 307 BGB; Art. 12 GG; BAG case law on Kündigungsverzicht (e.g. BAG, Urt. v. 27.11.2014 – 2 AZR 883/13 [unverified case number]; settled principle: only with compensation and for good cause) — https://www.hensche.de/Rechtsanwalt_Arbeitsrecht_Handbuch_Aufhebungsvertrag_Anfechtung_Widerruf.html
- **Severity:** Medium
- **Typical clause language:**
```text
Beide Parteien verzichten unwiderruflich und wechselseitig für die Dauer von drei Jahren auf das Recht zur ordentlichen Kündigung.
```
- **Recommended fix:** Cap duration (typically ≤ 1–2 years), justify with a business interest, and compensate the employee (e.g. wage guarantee, Abfindung); or delete and rely on § 622 BGB:
```text
Für die Dauer von zwölf Monaten wird das Recht zur ordentlichen Kündigung wechselseitig ausgeschlossen; hierfür erhält der Arbeitnehmer eine Abfindung in Höhe von [X] Euro, die auch bei einer einvernehmlichen Beendigung vor Ablauf nicht zurückzuzahlen ist.
```
- **Uncertainty:** Duration and compensation benchmarks are case-law-shaped, not statutory; longer waivers are increasingly difficult to sustain.

### P9 — Garden leave (Freistellung) clause — void since BAG 25.03.2026
- **Name:** Pauschale Freistellungsklausel / Automatic garden-leave clause (now void)
- **Category:** Duration & termination
- **Clause type:** Termination modality clause
- **Why it is a problem:** A pre-formulated (AGB) clause giving the employer the right to release the employee from work during the notice period was held **unwirksam** by the BAG on 25.03.2026 (5 AZR 108/25): it disadvantages the employee unreasonably (§ 307 Abs. 1 BGB) by forcing immediate loss of work and variable-pay opportunities without balancing the employee's interests (vacation, variable compensation, new-job flexibility). The clause is void; the employer may still unilaterally release only where justified in the individual case.
- **Legal basis:** BAG, Urt. v. 25.03.2026 – 5 AZR 108/25 (ECLI cited at dejure 2026,7559) — https://www.brak.de/newsroom/news/bag-pauschale-freistellungsklausel-in-arbeitsvertrag-unwirksam/ ; https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=25.03.2026&Aktenzeichen=5+AZR+108%2F25
- **Severity:** Critical
- **Typical clause language:**
```text
Der Arbeitgeber ist berechtigt, den Arbeitnehmer nach Ausspruch einer Kündigung bis zum Ablauf der Kündigungsfrist unter Fortzahlung der Vergütung von der Arbeitsleistung freizustellen.
```
- **Recommended fix:** Delete the clause. If garden leave is needed, negotiate it individually with compensation (e.g. vacation crediting, bonus protection) or rely on the employer's one-sided right of release only where a legitimate interest exists (e.g. Wettbewerbsverbot, Zugangskontrolle):
```text
(Streichen) — Eine Freistellung erfolgt nur im Einzelfall nach Ausspruch der Kündigung und wird gesondert vereinbart; etwaige Urlaubs- und Bonusanwartschaften bleiben unberührt.
```
- **Uncertainty:** BAG 5 AZR 108/25 is new (March 2026); scope of permissible individually negotiated clauses is being litigated. Any formular version should be treated as void.

### P10 — Termination on change of control / "key man" clauses
- **Name:** „Change-of-Control"-Kündigungsrechte / Change-of-control termination rights
- **Category:** Duration & termination
- **Clause type:** Termination clause (special)
- **Why it is a problem:** A formular clause allowing the employee to terminate for convenience on a change of control, or allowing the employer to terminate upon a restructuring event without social justification, conflicts with the Kündigungsschutzgesetz (social justification for dismissals, § 1 KSchG; Wartezeit § 1 Abs. 1 KSchG) and with § 613a Abs. 4 BGB (dismissal on transfer of business is void). Such clauses are AGB-invalid unless carefully bounded and compensated.
- **Legal basis:** § 1 KSchG; § 613a Abs. 4 BGB; § 307 BGB
- **Severity:** Medium
- **Typical clause language:**
```text
Im Falle eines Kontrollwechsels kann jede Partei das Arbeitsverhältnis mit einer Frist von sechs Monaten zum Monatsende kündigen.
```
- **Recommended fix:** Bounded variant with objective trigger and no circumvention of § 613a BGB:
```text
Bei einem Kontrollwechsel im Sinne von [Definition] kann der Arbeitnehmer das Arbeitsverhältnis innerhalb von drei Monaten nach Mitteilung des Kontrollwechsels mit einer Frist von sechs Monaten zum Monatsende kündigen. Ein Kündigungsrecht des Arbeitgebers wird hierdurch nicht begründet.
```
- **Uncertainty:** Highly negotiated territory; enforceability depends on individual bargaining (not AGB) and the specific trigger.

---

## 3. Remuneration

### P11 — Salary below Mindestlohn
- **Name:** Vergütung unterhalb des Mindestlohns / Remuneration below the statutory minimum wage
- **Category:** Remuneration
- **Clause type:** Salary clause
- **Why it is a problem:** The statutory minimum wage binds every employment relationship (MiLoG); from 1.1.2026 it is **13,90 €/hour**, rising to 14,60 € on 1.1.2027 (5th MiLoV). A below-minimum salary is void to that extent (§ 134 BGB); the employee can claim the difference; the employer commits an administrative offense (§ 21 MiLoG). Salary must be structured so that all remunerative components (fixed, commission, allowances) aggregate to ≥ minimum wage per hour actually worked; deductions and offsets are restricted (see P14).
- **Legal basis:** §§ 1, 20, 21 MiLoG; 5. MiLoV (Beschluss v. 29.10.2025); BMAS press release — https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/mindestlohn-steigt-zum-ersten-januar-2026.html ; https://www.arbeitsrechte.de/kommission-empfiehlt-mindestlohnlohnerhoehung-fuer-2026-auf-1390-euro/
- **Severity:** Critical
- **Typical clause language:**
```text
Der Arbeitnehmer erhält ein Bruttogehalt von 2.100,00 Euro monatlich bei einer wöchentlichen Arbeitszeit von 40 Stunden.
```
- **Recommended fix:** Verify hourly rate ≥ 13,90 € (2026) / 14,60 € (2027) after dividing monthly pay by actual hours; add a compliance statement and avoid all-inclusive "Abgeltung" of overtime in low-wage bands (see P12):
```text
Die monatliche Bruttovergütung beträgt [X] Euro bei einer wöchentlichen Arbeitszeit von [Y] Stunden. Die sich daraus ergebende Stundenvergütung liegt über dem gesetzlichen Mindestlohn.
```
- **Uncertainty:** None on the amounts; note further statutory rises on 1.1.2027.

### P12 — Flat overtime "Abgeltung" clause
- **Name:** Pauschale Überstundenabgeltung / Flat-rate overtime compensation clause
- **Category:** Remuneration / Working time
- **Clause type:** Overtime clause
- **Why it is a problem:** A formular clause stating that "all overtime" or "usual overtime" is covered by the base salary is AGB-invalid: it fails transparency (§ 307 Abs. 1 Satz 2 BGB) because the employee cannot tell how many hours are compensated (BAG, Urt. v. 01.09.2010 – 5 AZR 517/09; Urt. v. 17.08.2011 – 5 AZR 406/10). Where the employee actually works overtime, it must be paid. An **effective** clause must state the number of overtime hours covered and the compensation.
- **Legal basis:** § 307 Abs. 1 Satz 2 BGB; BAG, Urt. v. 01.09.2010 – 5 AZR 517/09 — https://www.bundesarbeitsgericht.de/entscheidung/5-azr-517-09/ ; BAG, Urt. v. 17.08.2011 – 5 AZR 406/10 — https://www.hensche.de/Ueberstunden_Bezahlung_Ueberstundenpauschalabgeltung_BAG_5AZR406-10_u.html
- **Severity:** Critical
- **Typical clause language:**
```text
Mit dem monatlichen Bruttogehalt sind sämtliche Überstunden abgegolten.
```
- **Recommended fix:** Quantify:
```text
Mit der monatlichen Bruttovergütung sind monatlich bis zu zehn Überstunden abgegolten. Darüber hinaus geleistete Überstunden werden mit einem Zuschlag von 25 % auf den Stundenlohn vergütet oder, im Einvernehmen mit dem Arbeitnehmer, durch Freizeit ausgeglichen.
```
- **Uncertainty:** None on the invalidity of blanket clauses; the admissible number of "free" overtime hours is not fixed (courts assess proportionality), so a concrete cap is the safe path.

### P13 — Unfettered bonus / discretion clause
- **Name:** Vorbehaltloses Ermessen bei Boni / Unfettered bonus discretion clause
- **Category:** Remuneration
- **Clause type:** Bonus clause
- **Why it is a problem:** "Bonus nach freiem Ermessen" or a bonus clause without objective criteria gives the employer unbounded discretion; under § 315 BGB the determination must be equitable, and a total absence of criteria fails AGB transparency. If the contract promises a bonus but omits target-setting, the employee can claim damages equal to 100 % of the target bonus (BAG, Urt. v. 12.12.2007 – 10 AZR 97/07).
- **Legal basis:** § 315 BGB; § 307 Abs. 1 Satz 2 BGB; BAG, Urt. v. 12.12.2007 – 10 AZR 97/07 — https://www.bag-urteil.com/12-12-2007-10-azr-97-07/
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer kann eine jährliche Sonderzahlung erhalten, deren Höhe der Arbeitgeber nach freiem Ermessen festlegt. Ein Rechtsanspruch besteht nicht.
```
- **Recommended fix:** Define targets, weighting, payout corridor, and a duty to set objectives:
```text
Der Arbeitnehmer erhält eine variable Vergütung von bis zu [X] % des Jahresgrundgehalts auf Grundlage jährlich zu vereinbarender Ziele. Die Ziele werden jeweils im ersten Quartal vereinbart; unterbleibt dies aus Gründen, die der Arbeitgeber zu vertreten hat, gilt der Zielbonus als erreicht. Die Zielerreichung wird nach [Kriterien] gemessen.
```
- **Uncertainty:** As of 2026, "Freiwilligkeitsvorbehalt" clauses remain valid only if unambiguous and not contradicting a promised payment (BAG, Urt. v. 20.02.2013 – 10 AZR 177/12); purely discretionary bonus clauses are on shaky ground (see also BAG 10 AZR 171/23, 03.07.2024, on § 315 determination) — https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=03.07.2024&Aktenzeichen=10+AZR+171%2F23

### P14 — Salary deductions & Verrechnung
- **Name:** Lohnabzüge und Aufrechnung / Salary deductions and set-off
- **Category:** Remuneration
- **Clause type:** Salary/deduction clause
- **Why it is a problem:** Set-off against wage claims is restricted: § 394 BGB bars set-off against unpfändbare wage components; § 4 EFZG protects continued-pay claims during sickness; and the employee's wage claim is protected from garnishment up to the Pfändungsfreigrenzen (§§ 850 ff. ZPO), which limits contractual deductions. A formular clause allowing the employer to deduct "any amounts owed" from salary is AGB-invalid (unreasonable disadvantage, § 307 BGB) and void under § 394 BGB where it reaches protected amounts.
- **Legal basis:** § 394 BGB; § 4 EFZG; §§ 850 ff. ZPO; § 307 BGB
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitgeber ist berechtigt, fällige Gegenansprüche jeder Art mit der laufenden Vergütung zu verrechnen.
```
- **Recommended fix:**
```text
Eine Aufrechnung durch den Arbeitgeber ist nur zulässig, soweit die Vergütung pfändbar ist (§ 394 BGB) und der Anspruch unbestritten oder rechtskräftig festgestellt ist.
```
- **Uncertainty:** None material; the boundaries of unpfändbar/pfändbar are statutory.

### P15 — Gratifikation/13th month with excessive Rückzahlungsklausel
- **Name:** Rückzahlungsklausel für Gratifikation über die BAG-Grenzen / Gratification clawback beyond the BAG limits
- **Category:** Remuneration
- **Clause type:** Bonus/gratification clause
- **Why it is a problem:** Clawback (Rückzahlung) clauses on a special payment are only valid within tight BAG limits: up to 31.03. of the following year if the payment is >100 € but <1 monthly salary; up to the next possible termination date, max. 30.06., if ≥1 monthly salary; if it is pure compensation for past work (Entgeltcharakter), clawback is invalid altogether. Binding beyond 30.06., or binding for pure remuneration, is AGB-invalid and a disproportionate restriction of Art. 12 GG.
- **Legal basis:** BAG, Urt. v. 27.06.2018 – 10 AZR 290/17 (tariff clawback to 31.03. valid; BAG 10 AZR 26/12, 16.01.2013, Weihnachtsgeld clawback) — https://www.bundesarbeitsgericht.de/entscheidung/10-azr-290-17/ ; https://dejure.org/dienste/vernetzung/rechtsprechung?Text=10+AZR+26%2F12 ; IHK Köln Merkblatt Gratifikationen — https://www.ihk.de/koeln/hauptnavigation/recht-steuern/uebersicht-arbeitsrecht/gratifikationen-merkblatt--5203158 ; arbeitskammer.de (Bindung bis max. 30.06. bei ≥ 1 Monatsgehalt) — https://www.arbeitskammer.de/fileadmin/user_upload/---------------AK_Download_Datenbank-------------/Publikationen/Faltblaetter/deutsche_Faltblaetter/Gratifikationen.pdf
- **Severity:** High
- **Typical clause language:**
```text
Die Weihnachtsgratifikation in Höhe von 500 Euro ist zurückzuzahlen, wenn der Arbeitnehmer bis zum 30. September des Folgejahres auf eigenen Wunsch ausscheidet.
```
- **Recommended fix:** Tier the binding period to the amount; max. 31.03. (<1 monthly salary) or max. 30.06. (≥1 monthly salary); never for pure past-work compensation:
```text
Die Gratifikation wird unter dem Vorbehalt gezahlt, dass das Arbeitsverhältnis nicht bis zum 31. März des Folgejahres auf Veranlassung des Arbeitnehmers endet. Bei einem Ausscheiden bis zu diesem Datum besteht eine Rückzahlungspflicht in voller Höhe. Diese Regelung entfällt, soweit die Zahlung reines Entgelt für bereits geleistete Arbeit darstellt.
```
- **Uncertainty:** Classification as Gratifikation (Bindungszweck) vs. Entgelt is case-by-case; Stichtags- und Rückzahlungsklauseln beyond the guidelines are void.

### P16 — Pay-gap / gender pay structure (EntgTranspG; EU 2023/970 pending)
- **Name:** Entgeltstruktur mit Entgeltdiskriminierung / Gender pay-gap structure
- **Category:** Remuneration
- **Clause type:** Salary structure / pay transparency
- **Why it is a problem:** The EntgTranspG (2017) grants individual pay information rights and equal-pay claims for comparable work (§§ 3, 7–15 EntgTranspG). EU Directive 2023/970 (Pay Transparency) required transposition by 7.6.2026 — Germany has **not yet** transposed (draft expected Q1 2026 per Deloitte; as of 2026-08 no statute in force). A contract salary banding or pay practice that yields systematically lower pay for women for equal work breaches § 3 EntgTranspG / Art. 157 TFEU and exposes the employer to back-pay and information claims; "gender-neutral" drafting is a contract-wide red flag check.
- **Legal basis:** §§ 3, 7–15 EntgTranspG; Art. 157 TFEU; RL (EU) 2023/970 (deadline 7.6.2026, not transposed) — https://www.deloitte.com/de/de/services/tax/perspectives/eu-entgelttransparenzrichtlinie.html ; https://www.dgfp.de/aktuell/neue-eu-entgelttransparenzrichtlinie
- **Severity:** High (compliance risk; direct liability only after transposition, but individual equal-pay claims already exist)
- **Typical clause language:**
```text
(Keine Klausel, sondern Struktur) Eingruppierung und Gehaltsbänder, die nach Geschlecht oder Familienstand differenzieren; Geheimhaltung der Gehaltsstruktur; Verbot, Auskunft über Gehälter zu erteilen.
```
- **Recommended fix:** Neutral, criteria-based grading (Tätigkeit, Verantwortung, Erfahrung, Leistung); remove pay-secrecy clauses (they conflict with § 10 EntgTranspG); prepare pay-range disclosure for job postings for the upcoming Umsetzungsgesetz:
```text
Die Vergütung richtet sich ausschließlich nach der Eingruppierung gemäß [Gehaltsband/Kriterien]; eine Differenzierung nach Geschlecht findet nicht statt. Die Arbeitnehmerin kann Auskunft über die Kriterien der Vergütungsfindung verlangen.
```
- **Uncertainty:** The EU directive's horizontal direct effect post-deadline (7.6.2026) is debated (see Eversheds) — https://www.eversheds-sutherland.com/de/germany/insights/the-pay-transparency-directive-and-the-issue-of-horizontal-third-party-effect

### P17 — Provision/commission with unilateral target changes
- **Name:** Provisionsklausel mit einseitiger Zielanpassung / Commission clause with unilateral quota changes
- **Category:** Remuneration
- **Clause type:** Commission clause
- **Why it is a problem:** A formular clause permitting the employer to unilaterally change targets, quotas, or commission rates (e.g. "im unternehmerischen Ermessen") violates § 315 BGB (equitable determination) and AGB transparency; retroactive cuts of already-earned commissions are invalid; the employee keeps earned commission claims. Handelsvertreter-style rules (§ 87 ff. HGB) inform but do not directly bind employees.
- **Legal basis:** § 315 BGB; § 307 Abs. 1 BGB; BAG case law on Leistungsbestimmung (e.g. BAG 10 AZR 171/23) — https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=03.07.2024&Aktenzeichen=10+AZR+171%2F23
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitgeber kann die Provisionssätze und Verkaufsziele jederzeit an veränderte Marktbedingungen anpassen; eine Anpassung ist nicht anfechtbar.
```
- **Recommended fix:** Prospective-only adjustment with objective triggers and equitable balancing:
```text
Ziele und Provisionssätze werden jeweils zum 01.01. für das Kalenderjahr festgelegt; eine unterjährige Anpassung ist nur bei wesentlicher Änderung der Vertriebsbedingungen möglich, wirkt nur für die Zukunft und berücksichtigt die Interessen beider Parteien (§ 315 BGB). Bereits verdiente Provisionen bleiben unberührt.
```
- **Uncertainty:** Individual vs. formular use matters; individually negotiated commission agreements enjoy more latitude.

---

## 4. Working Time & Leave

### P18 — Vacation carry-over/forfeiture clause violating BUrlG / 15-month rule
- **Name:** Urlaubsverfallsklausel ohne Hinweis-/Aufforderungspflicht / Vacation forfeiture clause ignoring the BAG's Hinweisobliegenheit
- **Category:** Working time & leave
- **Clause type:** Vacation clause
- **Why it is a problem:** § 7 Abs. 3 BUrlG allows carry-over only for urgent operational/personal reasons; statutory minimum leave (4 weeks, § 3 BUrlG) cannot be contracted away (§ 13 Abs. 1 BUrlG). Since BAG 19.02.2019 (9 AZR 541/15, 9 AZR 423/16), vacation forfeits only if the employer has informed the employee of the accrual and the expiry date and the employee nevertheless fails to take it; the 15-month cap (31.03. of the second following year) applies to long-term sick leave per EuGH C-214/10 (Schulte). A clause that forfeits leave "automatically" at year-end, or beyond the statutory framework, is void to the extent it covers statutory minimum leave.
- **Legal basis:** §§ 3, 7, 13 BUrlG; BAG, Urt. v. 19.02.2019 – 9 AZR 541/15 — https://www.bag-urteil.com/19-02-2019-9-azr-541-15 ; BAG, Urt. v. 19.02.2019 – 9 AZR 423/16 [case cited in BAG 9 AZR 401/19 materials]; EuGH C-214/10 (Schulte-Hostedde) — https://www.hensche.de/Urlaub_Krankheit_Urlaub_und_Krankheit_Krankheitsbedingt_nicht_genommener_Urlaub_kann_nach_15_Monaten_verfallen_EuGH_C214-10_KHS-gg-Schulte.html
- **Severity:** High
- **Typical clause language:**
```text
Nicht genommener Urlaub verfällt am 31.12. des jeweiligen Kalenderjahres ohne Übertragungsmöglichkeit.
```
- **Recommended fix:**
```text
Der Urlaub ist im laufenden Kalenderjahr zu nehmen. Soweit dringende betriebliche oder persönliche Gründe eine Übertragung erfordern, erfolgt sie auf die ersten drei Monate des Folgejahres. Der Arbeitgeber weist den Arbeitnehmer jeweils rechtzeitig auf den Urlaubsbestand und dessen Verfall hin und fordert zur Inanspruchnahme auf.
```
- **Uncertainty:** The 15-month cap for sick employees is settled; carry-over rules for contractual (übergesetzlicher) leave may deviate but must remain transparent and fair.

### P19 — Holiday pay / Urlaubsentgelt miscalculation
- **Name:** Falsche Urlaubsentgeltberechnung / Incorrect holiday pay calculation
- **Category:** Working time & leave
- **Clause type:** Vacation/pay clause
- **Why it is a problem:** § 11 BUrlG requires continued pay during vacation equivalent to average earnings of the preceding 13 weeks (including overtime, commission, allowances). A clause paying only base salary, or excluding variable components from holiday pay, is invalid (§§ 13 Abs. 1, 11 BUrlG); underpayment claims accrue.
- **Legal basis:** §§ 11, 13 BUrlG
- **Severity:** High
- **Typical clause language:**
```text
Während des Urlaubs wird nur das Grundgehalt fortgezahlt; Überstunden- und Provisionsbestandteile entfallen.
```
- **Recommended fix:**
```text
Das Urlaubsentgelt bemisst sich nach der durchschnittlichen Vergütung der letzten dreizehn Wochen vor Urlaubsbeginn einschließlich aller regelmäßigen variablen Bestandteile (§ 11 BUrlG).
```
- **Uncertainty:** None material.

### P20 — Arbeitszeiterfassung gap (post-BAG 2022)
- **Name:** Fehlende Regelung zur Arbeitszeiterfassung / Missing time-recording arrangement
- **Category:** Working time & leave
- **Clause type:** Working-time clause / general
- **Why it is a problem:** Since BAG 13.09.2022 (1 ABR 22/21), the employer must record **all** working time (begin, end, duration), based on § 3 Abs. 2 Nr. 1 ArbSchG read with EU law; the ArbZG itself (§ 16 Abs. 2 ArbZG) requires only overtime recording, but the statutory reform (electronic recording, weekly-hours shift) was still pending as of 2026-08. A contract that silently assumes no recording, or assigns recording to the employee without tools, leaves the employer liable for compliance gaps and shifts the burden of proof on overtime claims.
- **Legal basis:** BAG, Beschl. v. 13.09.2022 – 1 ABR 22/21 — https://www.bundesarbeitsgericht.de/entscheidung/1-abr-22-21 ; § 16 Abs. 2 ArbZG; Reform-Referentenentwurf (electronische Aufzeichnung) still pending — https://www.esche.de/news-wissen/esche-blog/elektronische-arbeitszeiterfassung-geplante-aenderungen-des-arbeitszeitgesetzes
- **Severity:** Medium
- **Typical clause language:**
```text
(Fehlende Regelung) Überstunden sind gesondert zu beantragen; eine systematische Zeiterfassung erfolgt nicht.
```
- **Recommended fix:** Implement a recording system and reflect it in the contract:
```text
Der Arbeitgeber stellt ein System zur elektronischen Erfassung von Beginn, Ende und Dauer der täglichen Arbeitszeit bereit; der Arbeitnehmer erfasst seine Arbeitszeit täglich unverzüglich nach deren Ende. Anordnungen von Überstunden bedürfen der Schriftform.
```
- **Uncertainty:** The ArbZG amendment (electronic recording duty) has not passed as of 2026-08; but the BAG obligation applies already. Watch the legislator: reform announced for 2026.

### P21 — Sunday/holiday work without compensation
- **Name:** Sonn- und Feiertagsarbeit ohne Ausgleich / Sunday/holiday work without compensatory time
- **Category:** Working time & leave
- **Clause type:** Working-time clause
- **Why it is a problem:** § 9 ArbZG bars Sunday/holiday work with narrow exceptions (§ 10 ArbZG); where permitted, § 11 ArbZG mandates at least 15 compensated Sundays/paid holidays per year plus compensatory rest. A clause waiving this or declaring Sunday work "abgegolten" is void (§§ 9, 11 ArbZG; § 134 BGB); also, absence of a Betriebsrat co-determination check (§ 87 Abs. 1 Nr. 2 BetrVG) in unionized establishments.
- **Legal basis:** §§ 9, 10, 11 ArbZG; § 87 Abs. 1 Nr. 2 BetrVG
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer erklärt sich mit der Arbeit an Sonn- und Feiertagen einverstanden; ein Freizeitausgleich ist nicht vorgesehen.
```
- **Recommended fix:**
```text
Sonn- und Feiertagsarbeit erfolgt nur im Rahmen der gesetzlichen Ausnahmen (§ 10 ArbZG). Für jeden geleisteten Sonn- oder Feiertag erhält der Arbeitnehmer einen Ersatzruhetag innerhalb der gesetzlichen Frist sowie die gesetzlichen Zuschläge nach [TV/Betriebsvereinbarung].
```
- **Uncertainty:** Exceptions under § 10 ArbZG are industry-specific; clause must not purport to waive statutory minima.

### P22 — Arbeit auf Abruf without 20/25 % statutory thresholds
- **Name:** Abrufarbeit ohne die gesetzlichen Fiktionen (§ 12 TzBfG) / On-call work ignoring the statutory working-time fictions
- **Category:** Working time & leave
- **Clause type:** Working-time clause
- **Why it is a problem:** If no minimum weekly hours are agreed, § 12 Abs. 1 Satz 3 TzBfG presumes **20 hours/week**; the employer may call in only up to 25 % above the agreed minimum (§ 12 Abs. 2 TzBfG, i.e. min. 20 h → max. 25 h) and may not go below the minimum by more than 20 %. A clause leaving hours open or allowing unlimited fluctuation is ineffective; the statutory fictions apply and back-pay follows.
- **Legal basis:** § 12 TzBfG; BAG on the 20-hour fiction — https://www.audibkk.de/portale/arbeitgeber/news/arbeit-auf-abruf-gesetzliche-vorgaben-beachten ; https://www.gesetze-im-internet.de/tzbfg/__12.html
- **Severity:** High
- **Typical clause language:**
```text
Die Arbeitszeit richtet sich nach dem Arbeitsanfall; der Arbeitgeber kann den Arbeitnehmer bei Bedarf einsetzen. Eine Mindestarbeitszeit wird nicht vereinbart.
```
- **Recommended fix:**
```text
Die wöchentliche Arbeitszeit beträgt mindestens [X] und höchstens [Y] Stunden. Der Arbeitgeber darf höchstens 25 % der vereinbarten Mindestarbeitszeit zusätzlich abrufen und die Mindestarbeitszeit nicht um mehr als 20 % unterschreiten (§ 12 TzBfG).
```
- **Uncertainty:** None on the statutory thresholds; the employee cannot waive the minimum.

---

## 5. Restrictive Covenants

### P23 — Post-contractual non-compete without Karenzentschädigung
- **Name:** Nachvertragliches Wettbewerbsverbot ohne Karenzentschädigung / Post-termination non-compete without compensation
- **Category:** Restrictive covenants
- **Clause type:** Non-compete clause
- **Why it is a problem:** For employees, § 110 GewO (analogous to §§ 74 ff. HGB) requires: (1) the covenant must protect a legitimate business interest, (2) duration ≤ 2 years, and (3) mandatory compensation of at least **50 % of the last contractual remuneration** for the entire restraint period, payable even if the employee terminated. Missing or insufficient compensation voids the clause **entirely** — the employee is free to compete.
- **Legal basis:** §§ 74, 74a, 74c HGB; § 110 GewO; settlement: BAG, Urt. v. 07.02.2019 – 6 AZR 75/18 (fair negotiation; compensation requirement) — https://www.anwalt24.de/urteile/bag/2019-02-07/6-azr-75_18 ; practical summary — https://www.anwalt.de/rechtstipps/arbeitsrecht-fuer-arbeitgeber-der-richtige-aufhebungsvertrag-265702.html
- **Severity:** Critical
- **Typical clause language:**
```text
Für die Dauer von zwei Jahren nach Beendigung des Arbeitsverhältnisses ist es dem Arbeitnehmer untersagt, für ein Konkurrenzunternehmen tätig zu werden. Eine Entschädigung wird nicht gezahlt.
```
- **Recommended fix:**
```text
Für die Dauer von [max. 24] Monaten nach Beendigung des Arbeitsverhältnisses ist der Arbeitnehmer an einem Wettbewerbsverbot gebunden, soweit dies zum Schutz berechtigter geschäftlicher Interessen erforderlich ist (§ 74a HGB). Der Arbeitgeber zahlt für die Dauer des Verbots eine Entschädigung in Höhe von 50 % der zuletzt bezogenen vertragsmäßigen Leistungen (§ 74 Abs. 2 HGB). Die Verpflichtung entfällt, wenn der Arbeitgeber das Verbot vor Beendigung schriftlich freigibt.
```
- **Uncertainty:** None on the compensation requirement; the 50 % floor is mandatory for employees (GewO/HGB analog).

### P24 — Non-compete longer than 2 years
- **Name:** Wettbewerbsverbot über zwei Jahre / Non-compete exceeding two years
- **Category:** Restrictive covenants
- **Clause type:** Non-compete clause
- **Why it is a problem:** Beyond 2 years the covenant is void (§ 74a Abs. 1 Satz 3 HGB) — no partial validity (the clause fails in full; the employee is not bound at all); courts do not "blue-pencil" the duration for employees.
- **Legal basis:** § 74a Abs. 1 Satz 3 HGB; § 110 GewO
- **Severity:** Critical
- **Typical clause language:**
```text
Das Wettbewerbsverbot gilt für die Dauer von drei Jahren nach Beendigung des Arbeitsverhältnisses.
```
- **Recommended fix:** Cap at 24 months (see P23).
- **Uncertainty:** None.

### P25 — Non-solicit of employees/customers overreach
- **Name:** Übermäßige Abwerbe- und Kundenschutzklauseln / Excessive employee/customer non-solicit
- **Category:** Restrictive covenants
- **Clause type:** Non-solicit clause
- **Why it is a problem:** Blanket bans on "any contact with customers" or "soliciting any employee" post-termination are AGB-invalid as unreasonable restraints on occupation (Art. 12 GG; §§ 74a, 74b HGB analog): they must be limited to customers the employee actually serviced and employees whose recruitment would genuinely harm the employer, and may not operate as a disguised non-compete without compensation. Overbroad clauses are void in full (§ 307 BGB).
- **Legal basis:** §§ 74a, 74b HGB analog; § 307 BGB; Art. 12 GG; BAG practice (settled) — https://www.hensche.de/Rechtsanwalt_Arbeitsrecht_Handbuch_Aufhebungsvertrag_Anfechtung_Widerruf.html
- **Severity:** Medium
- **Typical clause language:**
```text
Nach Beendigung darf der Arbeitnehmer für zwölf Monate weder Kunden des Arbeitgebers kontaktieren noch Mitarbeiter des Arbeitgebers abwerben oder für ein Konkurrenzunternehmen tätig werden.
```
- **Recommended fix:** Narrow scope + list + time limit + no disguised non-compete:
```text
Für die Dauer von sechs Monaten nach Beendigung ist es dem Arbeitnehmer untersagt, Kunden, die er in den letzten zwölf Monaten betreut hat, aktiv zur Abwerbung zu kontaktieren und Mitarbeiter abzuwerben, die im unmittelbaren Kundenkontakt tätig sind. Eine Tätigkeit für Wettbewerber bleibt hiervon unberührt, soweit kein Wettbewerbsverbot nach § 74 HGB vereinbart ist.
```
- **Uncertainty:** Fact-dependent (actual customer relationships); courts balance Art. 12 GG vs. legitimate interests case-by-case.

### P26 — Confidentiality clause with post-contractual effect
- **Name:** Unbefristete/übermäßige Verschwiegenheitsklausel / Indefinite or overbroad confidentiality clause
- **Category:** Restrictive covenants
- **Clause type:** Confidentiality clause
- **Why it is a problem:** Confidentiality of business secrets during employment is lawful (§ 17 UWG protects trade secrets; GeschGehG). But a clause banning all disclosure of "any information" — including general skills, know-how, or information the employee must disclose to authorities — indefinitely is AGB-invalid (overbreadth, § 307 BGB), conflicts with the GeschGehG whistleblower carve-out (§ 5 GeschGehG), and cannot restrict the employee's right to report violations (HinSchG, see P46).
- **Legal basis:** §§ 307, 611a BGB; § 5 GeschGehG; § 17 UWG
- **Severity:** Medium
- **Typical clause language:**
```text
Der Arbeitnehmer verpflichtet sich, sämtliche Informationen, die er während seiner Tätigkeit erlangt, zeitlich unbegrenzt und gegenüber jedermann geheim zu halten, auch nach Beendigung des Arbeitsverhältnisses.
```
- **Recommended fix:**
```text
Der Arbeitnehmer verpflichtet sich, Geschäftsgeheimnisse im Sinne des GeschGehG, die ihm im Rahmen der Tätigkeit anvertraut wurden, während und nach der Beendigung des Arbeitsverhältnisses vertraulich zu behandeln. Diese Verpflichtung gilt nicht für Informationen, die offenkundig sind, für die Offenlegung gegenüber Behörden oder nach dem Hinweisgeberschutzgesetz sowie für die Nutzung allgemeiner beruflicher Kenntnisse und Erfahrungen.
```
- **Uncertainty:** Trade-secret scope under GeschGehG is fact-dependent; post-termination confidentiality is enforceable only for genuine Geschäftsgeheimnisse, not general know-how.

### P27 — Vertragsstrafe (penalty clause) in the employment contract
- **Name:** Vertragsstrafenklausel / Contractual penalty clause
- **Category:** Restrictive covenants / Special clauses
- **Clause type:** Penalty clause
- **Why it is a problem:** A formular penalty for termination (e.g. "for leaving within 2 years, 3 monthly salaries") is AGB-invalid: the BAG requires the penalty to be reasonable, proportionate to the protected interest, and not to deter lawful termination (Art. 12 GG; § 307 BGB); penalties for exercising the right to terminate are void. The penalized breach must be concretely described (BAG 8 AZR 130/13); a blanket "Nichtantritt" or "Abwerbung" penalty without limits fails. Where valid (e.g. for non-compete breach), the penalty must be quantified reasonably.
- **Legal basis:** §§ 339 ff. BGB (contractual penalty); § 307 BGB; BAG, Urt. v. 23.01.2014 – 2 AZR 582/13 and BAG, Urt. v. 23.01.2014 – 8 AZR 130/13 (concrete breach required) — https://www.rechtsanwalt-bach.de/arbeitsrecht-leipzig/vertragsstrafe-arbeitsvertrag/ ; https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/urteilsanmerkungfdarbr201805-2018-02-14 (widersprüchliche Strafklauseln unwirksam)
- **Severity:** High
- **Typical clause language:**
```text
Verlässt der Arbeitnehmer das Unternehmen innerhalb von zwei Jahren nach Vertragsbeginn, zahlt er eine Vertragsstrafe in Höhe von drei Bruttomonatsgehältern.
```
- **Recommended fix:** Delete penalty for termination entirely; if a penalty is needed (e.g. non-compete breach), tie it to the concrete breach with a cap:
```text
Verstößt der Arbeitnehmer gegen die Verpflichtung aus § [X] (Wettbewerbsverbot), zahlt er eine Vertragsstrafe von bis zu [Betrag, höchstens ein Monatsgehalt pro Fall und insgesamt höchstens drei Monatsgehälter]; die Geltendmachung weiterer Ansprüche bleibt unberührt, soweit die Strafe angemessen ist.
```
- **Uncertainty:** BAG allows penalties for specific breaches (non-compete, training repayment) but reviews amount and transparency strictly; penalties for terminating are always void.

### P28 — IP/invention clauses conflicting with ArbEG
- **Name:** Erfindungsklauseln entgegen dem ArbEG / IP clauses conflicting with the Employee Invention Act
- **Category:** Restrictive covenants
- **Clause type:** IP/invention clause
- **Why it is a problem:** Diensterfindungen belong to the employee until the employer claims them; the employer must claim within 4 months (§ 6 ArbEG) and pay reasonable compensation (§ 9 ArbEG); pre-assignment of future inventions in the contract is void (ArbEG §§ 4–13, 22: statutory provisions cannot be contracted away to the employee's detriment — § 22 ArbnErfG); blanket "all IP vests in employer" clauses are ineffective and can even destroy the employer's rights (no valid Inanspruchnahme). Post-reporting agreements are allowed (§ 22 ArbnErfG).
- **Legal basis:** §§ 4–13, 22, 23 ArbnErfG (ArbEG); § 22: "Die Vorschriften dieses Gesetzes können zuungunsten des Arbeitnehmers nicht abgedungen werden" — https://www.gesetze-im-internet.de/arbnerfg/BJNR007560957.html ; https://www.buzer.de/gesetz/4473/a61844.htm
- **Severity:** High
- **Typical clause language:**
```text
Sämtliche Rechte an Erfindungen und geistigem Eigentum, die der Arbeitnehmer während seiner Tätigkeit macht, gehen kraft Vertrags auf den Arbeitgeber über; eine Vergütung ist hierin enthalten.
```
- **Recommended fix:** Reference the ArbEG procedure instead:
```text
Der Arbeitnehmer meldet Diensterfindungen unverzüglich nach § 5 ArbEG. Der Arbeitgeber erklärt die Inanspruchnahme innerhalb der Frist des § 6 ArbEG. Die Vergütung richtet sich nach den §§ 9 ff. ArbEG. Vereinbarungen über einzelne Erfindungen nach der Meldung bleiben vorbehalten.
```
- **Uncertainty:** Pauschale Vergütung (§ 12 ArbEG) is permitted only in narrow statutory bounds and is subject to Billigkeitskontrolle (§ 23 ArbEG); BGH 2025 reiterated that unbillige pauschal- oder Festbetragsvereinbarungen are void — https://legal-patent.com/arbeitnehmererfindung/rbeitnehmererfindungen-verguetungskalkulator-2026

---

## 6. Post-contractual Obligations

### P29 — Zeugnis waiver before termination
- **Name:** Verzicht auf Arbeitszeugnis vor Beendigung / Waiver of the employment reference before termination
- **Category:** Post-contractual obligations
- **Clause type:** Reference/waiver clause
- **Why it is a problem:** The right to a written (qualified) reference under § 109 GewO / § 630 BGB is a mandatory employee right. A waiver of the qualified reference **before the employment ends** is void (BAG, Urt. v. 18.06.2025 – 2 AZR 96/24 (B)): the employee is still in the dependency relationship; the waiver violates the protective purpose of § 109 GewO and is AGB-invalid. Only a waiver after termination is effective.
- **Legal basis:** § 109 GewO — https://www.gesetze-im-internet.de/gewo/__109.html ; § 630 BGB; BAG, Urt. v. 18.06.2025 – 2 AZR 96/24 (B) — https://www.fachanwalt.de/ratgeber/vorzeitiger-verzicht-auf-qualifiziertes-arbeitszeugnis-unwirksam
- **Severity:** Critical
- **Typical clause language:**
```text
Mit Abschluss dieses Aufhebungsvertrags verzichtet der Arbeitnehmer unwiderruflich auf die Erteilung eines Arbeitszeugnisses.
```
- **Recommended fix:** Replace waiver with a commitment to issue a qualified reference:
```text
Der Arbeitgeber erteilt dem Arbeitnehmer zum Beendigungszeitpunkt ein qualifiziertes Arbeitszeugnis, das Art und Dauer der Tätigkeit sowie Leistung und Verhalten bewertet.
```
- **Uncertainty:** None after BAG 18.06.2025 — pre-termination waiver (also via US-law choice-of-law clauses, as in the underlying case) is void.

### P30 — Return-of-property overreach
- **Name:** Übermäßige Herausgabeklauseln / Excessive return-of-property clauses
- **Category:** Post-contractual obligations
- **Clause type:** Property return clause
- **Why it is a problem:** The employer may require return of its property (laptops, keys, documents) — § 667 BGB analog (Herausgabe). But a formular clause demanding return of "all materials, including copies, notes, and personal devices", or withholding final pay until return, is AGB-invalid (§ 307 BGB; retention of salary is barred — pay is due regardless); personal data/devices must be excluded; the clause must not cover the employee's own property.
- **Legal basis:** § 307 BGB; § 667 BGB analog; § 614 BGB (pay due after service)
- **Severity:** Low
- **Typical clause language:**
```text
Bei Beendigung des Arbeitsverhältnisses sind sämtliche Unterlagen, Datenträger und Geräte, einschließlich privater Geräte mit dienstlichen Inhalten, zurückzugeben. Die letzte Gehaltszahlung erfolgt erst nach vollständiger Rückgabe.
```
- **Recommended fix:**
```text
Bei Beendigung sind die vom Arbeitgeber gestellten Arbeitsmittel (insbesondere Laptop, Mobiltelefon, Schlüssel, Firmenwagen) sowie dienstliche Unterlagen und Datenträger zurückzugeben. Die Vergütung wird unabhängig von der Rückgabe fristgemäß ausgezahlt.
```
- **Uncertainty:** None material.

### P31 — Retention of documents / Arbeitspapiere
- **Name:** Zurückbehaltung von Arbeitspapieren / Retention of work documents
- **Category:** Post-contractual obligations
- **Clause type:** Documentation clause
- **Why it is a problem:** The employer must issue an Arbeitsbescheinigung (§ 312 SGB III), Lohnsteuerbescheinigung, and health-insurance certificates promptly; withholding them (or threatening to) as leverage is unlawful and can constitute a tort/statutory violation; the employee can compel issuance. A clause conditioning documents on release/waiver is void (§ 134 BGB; § 307 BGB).
- **Legal basis:** § 312 SGB III; § 41b EStG; § 630 BGB analog; § 134 BGB
- **Severity:** Medium
- **Typical clause language:**
```text
Die Arbeitspapiere werden erst nach Unterzeichnung einer umfassenden Ausgleichs- und Schlussquittung ausgehändigt.
```
- **Recommended fix:**
```text
Die gesetzlich geschuldeten Bescheinigungen (Arbeitsbescheinigung, Lohnsteuerbescheinigung) werden unverzüglich nach Beendigung ausgestellt und übermittelt.
```
- **Uncertainty:** None; statutory duties are unconditional.

---

## 7. Data Protection & Monitoring

### P32 — Consent clause exploiting imbalance (§ 26 Abs. 2 BDSG)
- **Name:** Einwilligungsklausel mit strukturellem Ungleichgewicht / Consent clause invalid due to imbalance
- **Category:** Data protection & monitoring
- **Clause type:** Data-protection/consent clause
- **Why it is a problem:** Under § 26 Abs. 2 BDSG, consent to data processing in employment is valid only if freely given — which is regularly doubted in formular employment contracts ("Koppelungsverbot"): a blanket consent covering all personal data, bundled with the contract's conclusion, is invalid; the processing then lacks a legal basis (violation of Art. 6/88 GDPR, § 26 BDSG, fines).
- **Legal basis:** § 26 Abs. 2 BDSG; Art. 6, 88 GDPR; DSK guidance
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer willigt unwiderruflich in die Erhebung, Verarbeitung und Nutzung aller seiner personenbezogenen Daten einschließlich Gesundheitsdaten ein.
```
- **Recommended fix:** Separate, specific, revocable consent; rely primarily on § 26 Abs. 1 BDSG (Vertragsdurchführung) and Art. 6 Abs. 1 lit. b GDPR:
```text
Soweit personenbezogene Daten verarbeitet werden, erfolgt dies auf Grundlage des § 26 Abs. 1 BDSG bzw. Art. 6 Abs. 1 lit. b DSGVO. Eine darüber hinausgehende Verarbeitung erfolgt nur auf Grundlage gesonderter, freiwilliger und jederzeit widerruflicher Einwilligungen.
```
- **Uncertainty:** None on the principle; the exact boundary of "freiwillig" is assessed case-by-case.

### P33 — CCTV/e-mail/Internet/GPS/BYOD monitoring clauses
- **Name:** Überwachungsklauseln (Video, E-Mail, Internet, GPS, BYOD) / Monitoring clauses (CCTV, e-mail, Internet, GPS, BYOD)
- **Category:** Data protection & monitoring
- **Clause type:** Monitoring clause
- **Why it is a problem:** Covert or blanket monitoring of employees is unlawful: § 26 Abs. 1 BDSG requires a concrete purpose and proportionality; video surveillance must be justified under § 4 BDSG and may require works-council consent (§ 87 Abs. 1 Nr. 6 BetrVG); e-mail/Internet monitoring needs a policy + transparency; GPS tracking of vehicles/phones is only permitted for legitimate, proportionate purposes; BYOD access by the employer to private devices must be strictly limited. Formular clauses granting "unlimited monitoring rights" are void (§ 307 BGB) and constitute administrative offenses under the GDPR.
- **Legal basis:** §§ 4, 26 BDSG; Art. 5, 6, 88 GDPR; § 87 Abs. 1 Nr. 6 BetrVG
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitgeber ist berechtigt, sämtliche Kommunikation (E-Mail, Internet, Telefon) sowie den Aufenthaltsort des Arbeitnehmers jederzeit zu überwachen, auch ohne vorherige Information.
```
- **Recommended fix:** Purpose-bound, transparent, proportionate; separate policy:
```text
Eine Überwachung erfolgt nur auf Grundlage einer gesonderten Richtlinie, die Zweck, Umfang, Dauer und Rechtsgrundlage konkret benennt, und nur, soweit § 26 BDSG und ggf. § 87 Abs. 1 Nr. 6 BetrVG dies zulassen. Heimliche Überwachung ist ausgeschlossen.
```
- **Uncertainty:** Case-by-case proportionality; works-council co-determination where applicable.

### P34 — Whistleblower-NDA conflicts with HinSchG
- **Name:** Vertraulichkeitsklausel im Konflikt mit dem HinSchG / Confidentiality clause conflicting with the Whistleblower Protection Act
- **Category:** Data protection & monitoring / Restrictive covenants
- **Clause type:** Confidentiality clause
- **Why it is a problem:** § 9 HinSchG carves out disclosures to internal/external reporting channels and authorities from confidentiality duties; § 39 HinSchG voids agreements that restrict the right to report or penalize reporting; § 36 HinSchG bans reprisals with burden-of-proof reversal. A broad NDA/confidentiality clause that bars "any disclosure to third parties including authorities" is void to that extent and invites damages claims.
- **Legal basis:** §§ 9, 33, 36, 37, 39 HinSchG — https://www.gesetze-im-internet.de/hinschg/__36.html ; https://www.buzer.de/9_HinSchG.htm
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer verpflichtet sich, keinerlei Informationen über das Unternehmen an Dritte weiterzugeben, auch nicht an Behörden oder Aufsichtsstellen.
```
- **Recommended fix:**
```text
Die Vertraulichkeitsverpflichtung gilt nicht für Meldungen nach dem Hinweisgeberschutzgesetz an interne oder externe Meldestellen, für Offenlegungen nach § 32 HinSchG sowie für Auskünfte an Behörden und Gerichte.
```
- **Uncertainty:** None on the statutory carve-out; § 36 HinSchG's Beweislastumkehr applies to retaliations.

---

## 8. Secondary Employment & Exclusivity

### P35 — Blanket ban on secondary employment
- **Name:** Generelles Nebentätigkeitsverbot / Blanket prohibition of secondary employment
- **Category:** Secondary employment & exclusivity
- **Clause type:** Secondary-employment clause
- **Why it is a problem:** A blanket ban ("any other employment requires approval; approval may be refused at discretion" / "any secondary activity is prohibited") is AGB-invalid and violates Art. 12 GG: the BAG requires a concrete impairment of the employer's interests to justify restrictions (BAG, Urt. v. 11.12.2001 – 9 AZR 464/00: an approval-reservation clause that permits arbitrary refusal is ineffective; only concrete impairment justifies a ban). EU Directive 2019/1152 (transposed 2022) prohibits clauses barring other employment entirely.
- **Legal basis:** § 307 BGB; Art. 12 GG; BAG, Urt. v. 11.12.2001 – 9 AZR 464/00 — https://www.bag-urteil.com/11-12-2001-9-azr-464-00/ ; RL (EU) 2019/1152 Art. 9 (exclusivity ban) — https://eur-lex.europa.eu/legal-content/de/ALL/?uri=CELEX:32019L1152
- **Severity:** High
- **Typical clause language:**
```text
Jede Nebentätigkeit des Arbeitnehmers ist untersagt. Ausnahmen bedürfen der vorherigen schriftlichen Zustimmung des Arbeitgebers, die frei widerruflich ist.
```
- **Recommended fix:** Consent model with objective criteria:
```text
Eine Nebentätigkeit ist zulässig, soweit sie die arbeitsvertraglichen Pflichten nicht beeinträchtigt, insbesondere nicht während der vertraglichen Arbeitszeit oder bei Konkurrenztätigkeit ausgeübt wird. Sie ist dem Arbeitgeber vorab anzuzeigen. Eine Ablehnung ist nur zulässig, wenn die Nebentätigkeit berechtigte Interessen des Arbeitgebers konkret beeinträchtigt.
```
- **Uncertainty:** None on the invalidity of blanket bans; the concrete-impairment test is case-by-case.

### P36 — Exclusivity tied to remuneration model
- **Name:** Exklusivitätsklausel mit Vergütungskopplung / Exclusivity tied to compensation
- **Category:** Secondary employment & exclusivity
- **Clause type:** Secondary-employment clause
- **Why it is a problem:** Contracting "exclusivity" in exchange for a special allowance (e.g. "Nebentätigkeitsverzichtszuschlag") does not cure the AGB problem: the clause still restricts Art. 12 GG and must be limited to concrete impairment; if the allowance is later removed, the exclusivity collapses. EU law (2019/1152) bars exclusivity clauses outright in the EU; German transposition did not create an explicit prohibition but the BAG case law achieves the same for employees.
- **Legal basis:** Art. 12 GG; § 307 BGB; BAG 9 AZR 464/00; RL (EU) 2019/1152 Art. 9
- **Severity:** Medium
- **Typical clause language:**
```text
Der Arbeitnehmer verzichtet gegen einen monatlichen Zuschlag von 200 Euro auf jede anderweitige Erwerbstätigkeit.
```
- **Recommended fix:** Delete exclusivity; keep only the concrete-impairment rule (see P35). If the employer genuinely needs exclusivity (e.g. senior management), negotiate individually with real compensation and objective boundaries.
- **Uncertainty:** Individually negotiated, compensated exclusivity for senior staff may be enforceable; formular versions are not.

---

## 9. Family/Care & Disability

### P37 — Maternity clauses vs. MuSchG
- **Name:** Mutterschutzklauseln entgegen dem MuSchG / Maternity clauses violating the Maternity Protection Act
- **Category:** Family/care & disability
- **Clause type:** Special clause
- **Why it is a problem:** Dismissal during pregnancy/maternity leave (up to 4 months post-partum) is prohibited (§ 17 MuSchG) — any clause terminating on pregnancy, or a fixed term linked to pregnancy, is void (§ 134 BGB); fixed-term contracts ending during pregnancy are automatically extended (§ 17 Abs. 1 Satz 1 Nr. 1 MuSchG). The employer bears the burden of proving it did not know of the pregnancy in dismissal disputes.
- **Legal basis:** §§ 17, 18 MuSchG; § 134 BGB
- **Severity:** Critical
- **Typical clause language:**
```text
Das befristete Arbeitsverhältnis endet mit dem Tag des Beginns der Mutterschutzfrist, spätestens mit der Geburt des Kindes.
```
- **Recommended fix:** Delete; rely on statutory extension:
```text
(Streichen) — Bei Schwangerschaft gilt § 17 MuSchG: Das befristete Arbeitsverhältnis verlängert sich bis zum Ablauf der Schutzfristen.
```
- **Uncertainty:** None; the extension rule is mandatory.

### P38 — Parental-leave restrictions vs. BEEG
- **Name:** Elternzeitbeschränkungen / Parental-leave restrictions
- **Category:** Family/care & disability
- **Clause type:** Special clause
- **Why it is a problem:** The right to parental leave (up to 3 years per child, § 15 BEEG) cannot be contracted away; the employer may not refuse, and termination based on the leave request is prohibited (§ 18 BEEG). A clause waiving parental leave or requiring repayment of benefits upon leave is void; also § 15 Abs. 7 BEEG (part-time during Elternzeit) may not be restricted contractually.
- **Legal basis:** §§ 15, 18, 19 BEEG
- **Severity:** High
- **Typical clause language:**
```text
Elternzeit wird nur gewährt, wenn der Arbeitnehmer zuvor auf die Rückkehrgarantie und auf den gesetzlichen Kündigungsschutz verzichtet.
```
- **Recommended fix:** Delete; the statutory rights are non-waivable. Standard: no contractual clause needed — statute applies.
- **Uncertainty:** None.

### P39 — Care-leave restrictions (PflegeZG/Familienpflegezeit)
- **Name:** Pflegezeitbeschränkungen / Care-leave restrictions
- **Category:** Family/care & disability
- **Clause type:** Special clause
- **Why it is a problem:** Short-term care leave (10 days, § 2 PflegeZG), care leave (up to 6 months, § 3 PflegeZG), and Familienpflegezeit (§ 2 FPfZG) are statutory rights; the notice requirements (§ 3 PflegeZG: 10 days' notice with medical certificate) cannot be tightened contractually; dismissal during care leave is prohibited (§ 5 PflegeZG). Contract clauses conditioning leave on employer consent are void.
- **Legal basis:** §§ 2, 3, 5 PflegeZG; § 2 FPfZG
- **Severity:** High
- **Typical clause language:**
```text
Pflegezeit wird nur nach vorheriger Zustimmung des Arbeitgebers und bei Vorliegen betrieblicher Erfordernisse gewährt.
```
- **Recommended fix:** Delete; reference statute:
```text
Ansprüche auf Pflegezeit und Familienpflegezeit richten sich ausschließlich nach dem Pflegezeitgesetz und dem Familienpflegezeitgesetz.
```
- **Uncertainty:** None.

### P40 — Disability clauses violating SGB IX
- **Name:** Klauseln zu Behinderung / Disability-related clauses
- **Category:** Family/care & disability
- **Clause type:** Special clause
- **Why it is a problem:** Discrimination on disability grounds is barred (AGG § 7, § 1; SGB IX §§ 164 ff. — employer's duty to provide accommodations/barrierefreie Beschäftigung; special dismissal protection § 168 SGB IX requires the Inklusionsamt's consent). A clause declaring the employee "able-bodied" as a condition, or excluding accommodations, is void (§§ 134, 138 BGB; § 7 AGG) and triggers damages claims (§ 15 AGG).
- **Legal basis:** §§ 1, 7, 15 AGG; §§ 164, 168 SGB IX
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer versichert, uneingeschränkt arbeitsfähig zu sein; eine Behinderung ist dem Arbeitgeber nicht angezeigt worden. Leistungen zur Teilhabe werden nicht beansprucht.
```
- **Recommended fix:** Delete; no health/disability statements in the contract:
```text
(Streichen) — Nachteilsausgleiche und Ansprüche aus dem SGB IX bleiben unberührt.
```
- **Uncertainty:** None on invalidity; accommodation duties are case-specific.

---

## 10. Collective-Law Interplay

### P41 — Dynamic reference to expired collective agreement
- **Name:** Dynamische Verweisung auf ausgelaufenen Tarifvertrag / Dynamic reference to an expired collective agreement
- **Category:** Collective-law interplay
- **Clause type:** Reference clause
- **Why it is a problem:** A dynamic reference ("the applicable collective agreement in its current version") to a specific TV that expires or is terminated creates a gap: Nachwirkung (§ 4 Abs. 5 TVG) preserves only normative terms that are not regulated otherwise — new TV versions no longer flow through; if the employer leaves the association, the reference may fail altogether. Formular dynamic references to non-parties' or future Tvs are AGB-risk (unforeseeable changes). Conversely, static references freeze the old version. The outcome: uncertainty on pay and terms, and disputes over which version applies.
- **Legal basis:** §§ 3, 4 Abs. 5 TVG; § 307 Abs. 1 BGB (transparency); BAG 10 AZR 162/24 (30.10.2024, limited reference to individual TV norms is not control-free) — https://www.bundesarbeitsgericht.de/entscheidung/10-azr-162-24/
- **Severity:** Medium
- **Typical clause language:**
```text
Es gilt der jeweils gültige Tarifvertrag der [Branche] in seiner aktuellen Fassung, auch nach dessen Kündigung oder Austritt des Arbeitgebers aus dem Arbeitgeberverband.
```
- **Recommended fix:** Pin the reference to the employer's own tariff binding and provide a fallback:
```text
Die Vergütung und die übrigen Arbeitsbedingungen richten sich nach dem Tarifvertrag [Name], soweit der Arbeitgeber tarifgebunden ist. Endet die Tarifbindung, gelten die zuletzt vereinbarten Bedingungen als vertraglich vereinbart fort, bis eine abweichende Regelung getroffen ist.
```
- **Uncertainty:** The gap risk after expiry/exit is real; courts fill gaps via § 306 Abs. 2 BGB (statutory default) or ergänzende Vertragsauslegung — outcomes vary.

### P42 — Betriebsvereinbarung reference without gap regulation
- **Name:** Verweisung auf Betriebsvereinbarungen ohne Geltungsregelung / Reference to works agreements without continuity rule
- **Category:** Collective-law interplay
- **Clause type:** Reference clause
- **Why it is a problem:** References to "the applicable Betriebsvereinbarungen" are common but, if the works council is dissolved or the BV is terminated, the terms lapse (Nachwirkung of BVs only where provided, § 77 Abs. 6 BetrVG — no general Nachwirkung for BVs!). The contract then has a gap. Formular references must not delegate essential terms (pay, hours) entirely to future BVs (intransparent, § 307 BGB).
- **Legal basis:** § 77 Abs. 6 BetrVG (Nachwirkung only if agreed); § 307 Abs. 1 BGB; BAG practice on BV-Referenzklauseln (e.g. BAG 22.03.2005 – 9 AZR 481/04 [unverified number]) — general source: https://www.betriebsrat.com/wissen/personale-angelegenheiten/tarifvertrag
- **Severity:** Medium
- **Typical clause language:**
```text
Die jeweils geltenden Betriebsvereinbarungen sind Bestandteil des Arbeitsvertrags.
```
- **Recommended fix:**
```text
Auf das Arbeitsverhältnis finden die jeweils geltenden Betriebsvereinbarungen Anwendung, soweit sie das Arbeitsverhältnis betreffen. Endet die Geltung einer Betriebsvereinbarung, gelten ihre Regelungen vertraglich fort, bis eine neue Regelung getroffen wird.
```
- **Uncertainty:** Whether a mere reference creates a contractual continuation after the BV lapses is disputed; an express "Fortgeltungsklausel" reduces the risk.

### P43 — § 613a BGB collective-agreement continuity mishandled
- **Name:** § 613a BGB: Tarif-/Betriebsvereinbarungskontinuität / Transfer of business: collective-agreement continuity
- **Category:** Collective-law interplay
- **Clause type:** Transfer clause / general
- **Why it is a problem:** On a business transfer (§ 613a BGB), the transferee steps into the employment relationships; collective agreements/works agreements applicable to the transferor continue normatively and may be transformed into individual terms (§ 613a Abs. 1 Satz 2–3 BGB); dismissal because of the transfer is void (§ 613a Abs. 4 BGB); the transferee must inform (§ 613a Abs. 5 BGB). A new employment contract after a transfer that silently abandons the continued terms, or that makes the transfer itself a ground for changing terms, is void/invalid (§§ 134, 138, 307 BGB; § 613a Abs. 4 BGB).
- **Legal basis:** § 613a Abs. 1, 4, 5 BGB — https://www.gesetze-im-internet.de/bgb/__613a.html ; case law on transformierte Betriebsvereinbarungen — https://www.rechtslupe.de/arbeitsrecht/betriebsuebergang-und-die-nachwirkung-einer-betriebsvereinbarung-3244686
- **Severity:** High
- **Typical clause language:**
```text
Mit dem Betriebsübergang enden sämtliche beim bisherigen Arbeitgeber geltenden kollektivrechtlichen Regelungen; es gelten ausschließlich die Regelungen des übernehmenden Unternehmens.
```
- **Recommended fix:** No such clause — § 613a Abs. 1 Satz 2 BGB continues collective terms; changes require a lawful Änderungskündigung or individual agreement after proper information:
```text
(Streichen) — Die Rechte und Pflichten aus § 613a BGB bleiben unberührt; eine Anpassung kollektivrechtlicher Regelungen erfolgt nur im Rahmen der gesetzlichen Vorgaben.
```
- **Uncertainty:** Transformation mechanics (normative → individual terms) are settled but fact-intensive; timing of information and employee objection rights (§ 613a Abs. 6 BGB) matter.

---

## 11. Cross-Border & Posting

### P44 — Choice-of-law clause evading mandatory German protection
- **Name:** Rechtswahlklausel zulasten zwingender deutscher Schutzvorschriften / Choice of law evading mandatory German protection
- **Category:** Cross-border & posting
- **Clause type:** Choice-of-law clause
- **Why it is a problem:** Rome I Art. 8 protects employees: absent a choice, the law of the habitual workplace applies; even with a choice of law (e.g. "English law"), the employee retains the mandatory protective provisions of the law that would apply absent choice (Art. 8 Abs. 1, 2 Rome I). A clause selecting a foreign law to strip German minimum protections (notice periods, minimum wage, vacation, KSchG where applicable) is ineffective to that extent — and, per BAG 18.06.2025 (2 AZR 96/24 (B)), cannot defeat the Zeugnis claim or other zwingende Arbeitnehmerschutzbestimmungen.
- **Legal basis:** Art. 8 Rom I-VO (Verordnung (EG) 593/2008); BAG, Urt. v. 18.06.2025 – 2 AZR 96/24 (B) — https://www.fachanwalt.de/ratgeber/vorzeitiger-verzicht-auf-qualifiziertes-arbeitszeugnis-unwirksam
- **Severity:** High
- **Typical clause language:**
```text
This agreement is governed by the laws of England and Wales. The parties exclude the application of German law.
```
- **Recommended fix:** Choose German law for work performed in Germany, or add a protective clause:
```text
Auf das Arbeitsverhältnis findet deutsches Recht Anwendung. Soweit eine Rechtswahl vereinbart ist, bleiben die zwingenden Schutzvorschriften des Rechts, das ohne Rechtswahl anzuwenden wäre (Art. 8 Rom I-VO), unberührt.
```
- **Uncertainty:** None on the mandatory-protection floor; dispute only on which provisions are "zwingend" in the specific case.

### P45 — Posting gaps (AEntG/Arbeitnehmer-Entsendegesetz)
- **Name:** Entsendungslücken (AEntG) / Posting gaps under the German Posting Act
- **Category:** Cross-border & posting
- **Clause type:** Posting clause
- **Why it is a problem:** Posting employees to Germany (or from Germany) triggers the AEntG core employment terms (minimum wage, working time, vacation, industry-specific minimum conditions — § 8 AEntG), mandatory written notice (§ 18 AEntG), and the EU Posting Directive (96/71/EC as amended by 2018/957). A contract that applies only the home-country law and omits the German core terms violates mandatory law; the employee can claim the German minima. Conversely, German employers posting abroad must observe the posting rules of the destination state.
- **Legal basis:** §§ 8, 18 AEntG; RL 96/71/EG; RL (EU) 2018/957
- **Severity:** High
- **Typical clause language:**
```text
Der Arbeitnehmer wird vorübergehend in Deutschland eingesetzt; es gelten ausschließlich die Rechtsvorschriften des Heimatlandes, insbesondere keine deutschen Mindeststandards.
```
- **Recommended fix:**
```text
Bei einem Einsatz in Deutschland gelten zusätzlich zu den vertraglichen Regelungen die zwingenden Bestimmungen des AEntG (Mindestlohn, Arbeitszeit, Urlaub) und die Mitteilungspflichten nach § 18 AEntG. Der Arbeitgeber stellt vor Beginn der Entsendung eine schriftliche Unterrichtung in deutscher Sprache bereit.
```
- **Uncertainty:** Industry-specific AEntG minimum conditions (Bau, Pflege, etc.) vary; maximum posting duration (12/18 months) under 2018/957 relevant for social-security and labor-law scope.

---

## 12. Formalities & Documentation

### P46 — Missing NachwG § 2 terms
- **Name:** Fehlende Pflichtangaben nach § 2 NachwG / Missing mandatory terms under the Evidence Act
- **Category:** Formalities & documentation
- **Clause type:** Documentation clause (whole contract)
- **Why it is a problem:** Since 1.8.2022, § 2 NachwG requires a written record of a long catalogue of essential terms (identity of parties, start date, job description, pay components incl. overtime, working hours, vacation, notice periods, place of work, training rights, etc.) within 7 days (core) / 1 month (other terms) of commencement; since 1.1.2025 the record may be delivered in Textform/electronic form under conditions (§ 2 Abs. 1 Satz 2 NachwG). Omissions are administrative offenses (§ 4 NachwG, fine up to €2,000 per case) and shift the burden of proof on the omitted terms.
- **Legal basis:** §§ 2, 3, 4 NachwG — https://www.gesetze-im-internet.de/nachwg/BJNR094610995.html ; amendments 2022 (1.8.2022) and 2025 (Textform) — https://www.brak.de/newsroom/news/arbeitsvertraege-jetzt-nur-noch-schriftlich-und-mit-mehr-inhalt/ ; https://fasp.de/2025/02/11/aenderungen-zum-nachweisgesetz-ab-01-01-2025/ ; fine — https://www.arbeitsrechte.de/nachweisgesetz/
- **Severity:** Critical
- **Typical clause language:**
```text
(Fehlende Angaben) Vertrag ohne Angaben zu: Überstundenregelung, Arbeitsort bei wechselnden Einsatzorten, Vergütungsbestandteile, Probezeitdauer, Hinweis auf anwendbare Tarifverträge, Fortbildungsanspruch, Ruhestandsversorgung.
```
- **Recommended fix:** Include all § 2 NachwG items as a checklist; e.g. add:
```text
Wechselnde Arbeitsorte: Der Arbeitnehmer kann an wechselnden Einsatzorten innerhalb des Gebiets [X] eingesetzt werden. Anwendbare Tarifverträge/Betriebsvereinbarungen: [Name, Fundstelle]. Die Vergütung setzt sich zusammen aus [Grundgehalt, Zulagen, variable Bestandteile]; Überstundenvergütung gemäß § [X].
```
- **Uncertainty:** None on the obligation; the electronic-delivery conditions (accessibility, storage, printability, receipt confirmation) must be met since 1.1.2025.

### P47 — § 126a BGB digital signature vs. Schriftform
- **Name:** Elektronische Signatur statt Schriftform / Electronic signature instead of required writing
- **Category:** Formalities & documentation
- **Clause type:** Signature clause
- **Why it is a problem:** Where the law requires Schriftform (§ 126 BGB) — fixed-term agreements (§ 14 Abs. 4 TzBfG, § 623 BGB), Kündigung (§ 623 BGB), Aufhebungsvertrag, non-compete (in part), § 41 SGB VI Befristung — only wet-ink signatures or a qualified electronic signature (§ 126a BGB) satisfy it. Simple e-mail, PDF without QES, or a scanned signature is ineffective; for a Befristung the consequence is an indefinite contract; for a Kündigung, nullity (§ 125 BGB). Textform (§ 126b BGB) suffices only where the statute says so (e.g. § 3 NachwG info duties, notice of part-time requests, § 41 SGB VI Hinausschieben).
- **Legal basis:** §§ 125, 126, 126a, 126b BGB; § 14 Abs. 4 TzBfG; § 623 BGB; IHK München (e-mail Befristung unwirksam) — https://www.ihk-muenchen.de/ratgeber/recht/arbeitsrecht/bestehende-arbeitsverhaeltnisse-kuendigung-sozialversicherung/befristete-beschaeftigung-rentner/
- **Severity:** Critical
- **Typical clause language:**
```text
(Digitaler Vertragsschluss per E-Mail ohne qualifizierte elektronische Signatur) "Bitte senden Sie den unterschriebenen Vertrag einfach als Scan per E-Mail zurück."
```
- **Recommended fix:** Use a QES provider for Schriftform documents or wet-ink; state the form requirement explicitly:
```text
Änderungen und Ergänzungen dieses Vertrags, insbesondere Befristungsabreden und Kündigungen, bedürfen der Schriftform (§ 126 BGB); die elektronische Form ist nur bei Vorliegen einer qualifizierten elektronischen Signatur (§ 126a BGB) gewahrt.
```
- **Uncertainty:** None on the principle; note the 2025 reform discussion about extending Textform to § 623 BGB has not been enacted as of 2026-08 (Gleiss Lutz flagged a ministerial plan in 2024 — not law) — https://www.gleisslutz.com/de/know-how/nachweisgesetz-textform-endlich-auch-deutschland

### P48 — Textform misuse for consent/waivers
- **Name:** Textform für Einwilligungen/Verzichte / Using simple text form where writing or more is required
- **Category:** Formalities & documentation
- **Clause type:** Consent/waiver clause
- **Why it is a problem:** Several labor-law acts expressly require more than Textform: consent to data processing should be documented (§ 26 Abs. 2 Satz 3 BDSG: "in Textform" — but formular consent in an employment contract is invalid per se, see P32); the Niederschrift under NachwG was Schriftform until 1.1.2025, now Textform possible; Aufhebungsverträge and Kündigungen require Schriftform (§ 623 BGB). Using a mere e-mail confirmation for a Kündigung or Aufhebungsvertrag is void.
- **Legal basis:** § 623 BGB (Schriftform); § 126b BGB (Textform); § 26 Abs. 2 Satz 3 BDSG
- **Severity:** High
- **Typical clause language:**
```text
Kündigungen und Aufhebungsvereinbarungen können auch per E-Mail erklärt werden.
```
- **Recommended fix:** Delete or correct:
```text
Kündigungen bedürfen der Schriftform (§ 623 BGB) und sind dem Empfänger in der nach § 130 BGB maßgeblichen Weise zugegangen zu erklären. E-Mail genügt nicht.
```
- **Uncertainty:** None.

---

## 13. Mobility & Workplace

### P49 — Home office / mobile work clauses without core terms
- **Name:** Homeoffice-/Mobile-Work-Klauseln ohne Kernbedingungen / Home-office/mobile-work clauses lacking core terms
- **Category:** Mobility & workplace
- **Clause type:** Workplace clause
- **Why it is a problem:** A clause granting "mobile work at the employee's discretion" without defining scope (days, location, data-security duties, reimbursement of costs, work-injury coverage, availability) creates disputes over: Arbeitsunfall coverage (§ 8 SGB VII — home office counts as insured workplace), equipment costs (§ 670 BGB analog — expenses reimbursement), and working-time recording (see P20). Formular clauses that shift all costs/risks to the employee are AGB-invalid.
- **Legal basis:** § 8 SGB VII; § 670 BGB analog; § 307 BGB; Arbeitszeitrecht (recording obligation per BAG 1 ABR 22/21)
- **Severity:** Medium
- **Typical clause language:**
```text
Der Arbeitnehmer darf im Homeoffice arbeiten. Sämtliche mit der Tätigkeit verbundenen Kosten trägt der Arbeitnehmer.
```
- **Recommended fix:**
```text
Homeoffice im Umfang von bis zu [X] Tagen pro Woche nach Absprache. Der Arbeitgeber stellt die erforderliche Ausstattung (Laptop, Bildschirm, Kommunikationsmittel) und trägt die beruflich veranlassten Mehrkosten. Die gesetzliche Unfallversicherung gilt auch für die Homeoffice-Tätigkeit; die Arbeitszeit ist gemäß [Zeiterfassungssystem] zu dokumentieren.
```
- **Uncertainty:** Reimbursement of home-office costs is not comprehensively statutory (except § 670 BGB analog for veranlasste Aufwendungen); tax/duty rules (Tätigkeitsort) evolve.

### P50 — Travel time excluded from working time/pay
- **Name:** Reisezeit nicht als Arbeitszeit / Travel time excluded from working time
- **Category:** Mobility & workplace
- **Clause type:** Travel-time clause
- **Why it is a problem:** For employees without a fixed workplace (Außendienst, Techniker), travel between customers is working time and must be paid (BAG, Urt. v. 11.07.2018 – 5 AZR 595/17; Urt. v. 17.10.2018 – 5 AZR 553/17: travel on foreign assignment is working time). A clause declaring "all travel time is not working time and unpaid" is void (§ 307 BGB); the employee can claim pay for the excluded hours.
- **Legal basis:** BAG, Urt. v. 11.07.2018 – 5 AZR 595/17 and Urt. v. 17.10.2018 – 5 AZR 553/17 — https://www.lto.de/recht/hintergruende/h/bag-5azr55317-verguetung-reisezeit-auslandsentsendung-regulaere-arbeitszeit ; https://rechtstipp24.de/2018/10/22/reisezeit-ist-grundsaetzlich-arbeitszeit-bag-urteil-v-17-10-2018-5-azr-553-17
- **Severity:** High
- **Typical clause language:**
```text
Reisezeiten des Außendienstmitarbeiters gelten nicht als Arbeitszeit und werden nicht vergütet.
```
- **Recommended fix:**
```text
Reisezeiten zwischen Kundenterminen und zu auswärtigen Einsatzorten gelten als Arbeitszeit und werden vergütet, soweit sie während der regelmäßigen Arbeitszeit anfallen oder vom Arbeitgeber angeordnet sind. Reisezeiten außerhalb der regelmäßigen Arbeitszeit werden mit [Zuschlag/Freizeit] ausgeglichen.
```
- **Uncertainty:** The commute to a fixed workplace is still not working time; the classification depends on fixed vs. variable workplace and on whether the employee can use the travel time freely (passive travel).

### P51 — Work equipment cost-shifting
- **Name:** Kostenabwälzung für Arbeitsmittel / Shifting work-equipment costs to the employee
- **Category:** Mobility & workplace
- **Clause type:** Equipment clause
- **Why it is a problem:** The employer must bear the costs of work equipment required for the job (tools, PPE per ArbSchG § 3, phone/PC where functionally required); a formular clause requiring the employee to buy/maintain its own equipment (BYOD without compensation) is AGB-invalid to the extent it shifts necessary costs (§ 307 BGB; § 670 BGB analog). PPE cost-shifting is a statutory violation (ArbSchG/ArbStättV).
- **Legal basis:** § 307 BGB; § 670 BGB analog; § 3 ArbSchG (PSA kostenlos); § 618 BGB (Fürsorgepflicht)
- **Severity:** Medium
- **Typical clause language:**
```text
Der Arbeitnehmer nutzt für die Tätigkeit ein eigenes Endgerät; Anschaffungs- und Betriebskosten trägt der Arbeitnehmer.
```
- **Recommended fix:**
```text
Der Arbeitgeber stellt die für die Tätigkeit erforderlichen Arbeitsmittel einschließlich erforderlicher persönlicher Schutzausrüstung kostenlos bereit. Soweit ein privates Gerät genutzt wird, erstattet der Arbeitgeber die beruflich veranlassten Kosten auf Nachweis.
```
- **Uncertainty:** BYOD reimbursement practice is negotiated; the statutory floor (free PPE, employer bears business costs) is firm.

### P52 — Relocation clauses
- **Name:** Versetzungsklauseln / Relocation clauses
- **Category:** Mobility & workplace
- **Clause type:** Mobility clause
- **Why it is a problem:** A clause allowing the employer to relocate the employee "anywhere in Germany/Europe" at will is AGB-invalid: it must respect § 106 GewO (Weisungsrecht nach billigem Ermessen) and the contract's place-of-work definition; an unlimited Versetzungsvorbehalt is unreasonable (§ 307 BGB; BAG practice requires a reasonable bound, notice of costs, and compensation for increased commuting). For works-council co-determination see § 95 BetrVG.
- **Legal basis:** § 106 GewO; § 307 BGB; § 95 BetrVG (Versetzungen)
- **Severity:** Medium
- **Typical clause language:**
```text
Der Arbeitgeber ist berechtigt, den Arbeitnehmer jederzeit an beliebige Orte im In- und Ausland zu versetzen.
```
- **Recommended fix:**
```text
Der Arbeitgeber kann den Arbeitnehmer im Rahmen des § 106 GewO an einen anderen Einsatzort innerhalb [Stadt/Region/Bundesland] versetzen, soweit dies billigem Ermessen entspricht. Eine Versetzung, die eine wesentliche Änderung der Arbeitsbedingungen mit sich bringt, bedarf der Zustimmung des Arbeitnehmers oder erfolgt im Rahmen einer Änderungskündigung. Mehraufwendungen (Fahrt, Unterkunft) werden erstattet.
```
- **Uncertainty:** The permissible radius is case-law-shaped; "wesentliche Vertragsbedingungen" cannot be changed unilaterally without Änderungskündigung.

---

## 14. Special Clauses

### P53 — Kündigungsschutz waiver / Klageverzicht in severance context
- **Name:** Klageverzicht/Ausgleichsklausel im Aufhebungsvertrag / Waiver of claims in severance agreements
- **Category:** Special clauses
- **Clause type:** Aufhebungs-/Abwicklungsvertrag clause
- **Why it is a problem:** Waivers of Kündigungsschutz claims (Klageverzicht) in an Aufhebungsvertrag are valid only if individually negotiated, transparent, and not procured by unlawful pressure; the BAG requires "faires Verhandeln" (BAG, Urt. v. 07.02.2019 – 6 AZR 75/18) — an Aufhebungsvertrag concluded under threat of a dismissal that is not seriously intended may be void (§ 123 BGB) or violate the fair-negotiation principle; blanket Ausgleichsklauseln ("all claims of any kind are settled") that sweep in non-waivable statutory claims (Zeugnis, P29) or unknowable future claims are invalid; the Aufhebungsvertrag itself must be in Schriftform (§ 623 BGB).
- **Legal basis:** §§ 123, 138, 134, 307 BGB; § 623 BGB; BAG, Urt. v. 07.02.2019 – 6 AZR 75/18 — https://www.anwalt24.de/urteile/bag/2019-02-07/6-azr-75_18
- **Severity:** High
- **Typical clause language:**
```text
Mit dieser Vereinbarung sind sämtliche Ansprüche aus dem Arbeitsverhältnis und seiner Beendigung, gleich aus welchem Rechtsgrund, abgegolten. Der Arbeitnehmer verzichtet auf die Erhebung von Klagen.
```
- **Recommended fix:** Bound the waiver to known, enumerated claims; exclude statutory non-waivable rights; keep Schriftform:
```text
Mit dieser Vereinbarung sind die wechselseitigen Ansprüche aus dem Arbeitsverhältnis und seiner Beendigung abgegolten, soweit sie den Parteien bei Abschluss bekannt waren und nicht gesetzlich unabdingbar sind. Ansprüche auf ein Arbeitszeugnis, auf gesetzliche Mindestlohnbeträge, auf Sozialversicherungsleistungen und aus vorsätzlichem Handeln bleiben unberührt.
```
- **Uncertainty:** Fair-negotiation review is fact-intensive; waivers of § 1 KSchG rights inside a negotiated severance are enforceable when the employee receives adequate consideration.

### P54 — Abfindungsklausel below statutory severance expectations
- **Name:** Abfindungsklausel mit ungünstiger Berechnung / Severance clause with unfavorable calculation
- **Category:** Special clauses
- **Clause type:** Severance clause
- **Why it is a problem:** There is no statutory severance entitlement absent a Sozialplan or § 1a KSchG (Abfindungsanspruch: 0.5 monthly salaries per year of service if the employer offers severance to avoid a dismissal dispute, § 1a Abs. 1, 2 KSchG). A formular clause that (a) caps severance below the § 1a KSchG level, (b) makes severance conditional on a waiver of all claims including non-waivable ones, or (c) is intransparent about triggers, is AGB-invalid and may fail to exclude the § 1a claim.
- **Legal basis:** § 1a KSchG; § 307 BGB
- **Severity:** Medium
- **Typical clause language:**
```text
Bei betriebsbedingter Kündigung erhält der Arbeitnehmer eine Abfindung von 0,2 Monatsgehältern pro Beschäftigungsjahr, höchstens jedoch 5.000 Euro.
```
- **Recommended fix:**
```text
Bei einer betriebsbedingten Kündigung, gegen die der Arbeitnehmer keine Kündigungsschutzklage erhebt, erhält er eine Abfindung in Höhe von 0,5 Bruttomonatsgehältern je vollendetem Beschäftigungsjahr (§ 1a KSchG) oder einer hiervon abweichenden, individuell vereinbarten höheren Abfindung.
```
- **Uncertainty:** Individual negotiations dominate; § 1a KSchG is the statutory floor pattern.

### P55 — Anrechnung Vorbeschäftigungszeiten (forfeiture of seniority)
- **Name:** Ausschluss der Anrechnung von Vorbeschäftigungszeiten / Exclusion of prior-service credit
- **Category:** Special clauses
- **Clause type:** Seniority clause
- **Why it is a problem:** Clauses stating that "prior employment with the employer/its predecessors is not credited" collide with: § 622 Abs. 2 BGB (notice-period grading by years of service — the BAG counts prior service in the same company, and § 622 Abs. 2 Satz 2 BGB's age-25 carve-out is EU-law-incompatible, see P4), § 1 KSchG Wartezeit (6 months, not excludable), and § 613a BGB continuity on transfers (P43). Contractual exclusion of service credit is ineffective where statutes mandate counting; otherwise it may be AGB-valid only if transparent and not discriminatory.
- **Legal basis:** § 622 Abs. 2 BGB; § 1 KSchG; § 613a BGB; BAG 5 AZR 700/09 — https://www.haufe.de/id/entscheidung/bag-urteil-vom-01092010-5-azr-70009-HI2538755.html
- **Severity:** Medium
- **Typical clause language:**
```text
Zeiten einer früheren Beschäftigung bei der Gesellschaft oder einem verbundenen Unternehmen werden bei der Berechnung der Kündigungsfristen und sonstiger Rechte nicht angerechnet.
```
- **Recommended fix:** Align with statute:
```text
Für die Berechnung der gesetzlichen Kündigungsfristen und der Wartezeit des § 1 KSchG gelten die gesetzlichen Vorschriften; Zeiten früherer Beschäftigung bei demselben Arbeitgeber sind gesetzlich zu berücksichtigen, soweit die Vorschriften dies vorsehen.
```
- **Uncertainty:** None for the statutory minima; only company-specific benefits (e.g. anniversary bonuses) can be freely conditioned.

### P56 — Wertsicherungsklausel (indexation clause)
- **Name:** Wertsicherungsklausel / Price-indexation clause
- **Category:** Special clauses
- **Clause type:** Salary-adjustment clause
- **Why it is a problem:** Under the Preisklauselgesetz (PrKG, since 14.9.2007), indexation of monetary obligations is generally barred unless it falls within the exceptions (§§ 2–7 PrKG: long-term contracts § 3, cost-element clauses § 4, etc.). Employment contracts rarely qualify (short term); a formular automatic CPI-indexation of salary is void (§ 1 Abs. 1, 2 PrKG; § 134 BGB) — the salary stays fixed and the indexation is unenforceable; conversely, one-sided "Nur-Erhöhung" clauses fail PrKG requirements.
- **Legal basis:** §§ 1–7 PrKG; Gabler/IHK practice notes — https://www.ihk.de/pfalz/recht/recht/wertsicherungsklausel-1274074 ; https://www.gabler-banklexikon.de/definition/wertsicherungsklauseln-62647
- **Severity:** Medium
- **Typical clause language:**
```text
Das Gehalt wird jährlich automatisch an die Veränderung des Verbraucherpreisindex angepasst, ohne Rücksicht auf die wirtschaftliche Lage des Arbeitgebers.
```
- **Recommended fix:** Replace with an annual review/negotiation clause (not automatic indexation):
```text
Die Parteien verhandeln jährlich über eine Anpassung der Vergütung an die wirtschaftliche Entwicklung; ein Automatismus besteht nicht. Eine Indexbindung ist ausgeschlossen.
```
- **Uncertainty:** PrKG exceptions are narrow; automatic CPI clauses in employment contracts are practically unenforceable; individually negotiated long-term contracts (>12 months) may qualify under § 3 PrKG.

### P57 — Arbitration/Mediation clauses
- **Name:** Schieds- und Mediationsklauseln / Arbitration and mediation clauses
- **Category:** Special clauses
- **Clause type:** Dispute-resolution clause
- **Why it is a problem:** Arbitration agreements in employment contracts are **prohibited** by § 101 Abs. 1, 2 ArbGG unless the employee is an executive (§ 14 Abs. 2 KSchG) or a collective agreement provides otherwise; a formular arbitration clause is void (§ 134 BGB; the labor courts retain jurisdiction). Mediation clauses are permissible but must not impose cost burdens or time bars on the employee's right of access to the labor courts (§ 4 KSchG 3-week deadline cannot be tolled by a mediation agreement; a mandatory pre-mediation that jeopardizes the deadline is AGB-invalid).
- **Legal basis:** §§ 4, 101, 110 ArbGG; § 14 Abs. 2 KSchG; § 4 KSchG (3-week deadline)
- **Severity:** High
- **Typical clause language:**
```text
Alle Streitigkeiten aus dem Arbeitsverhältnis werden durch ein Schiedsgericht nach der DIS-Schiedsgerichtsordnung entschieden. Vor Klageerhebung ist ein Mediationsverfahren durchzuführen.
```
- **Recommended fix:** Delete the arbitration part; keep only a voluntary, non-blocking mediation clause:
```text
Die Parteien können sich im Konfliktfall um eine einvernehmliche Lösung bemühen, auch im Rahmen einer freiwilligen Mediation. Die Zuständigkeit der Arbeitsgerichte und gesetzliche Fristen, insbesondere die Frist des § 4 KSchG, bleiben hiervon unberührt.
```
- **Uncertainty:** None on the arbitration prohibition for employees (with the statutory exceptions); mediation clauses are enforceable only as non-binding process agreements.

---

## Contract-Wide Red Flags (cross-cutting checklist)

1. **Missing NachwG terms** — any contract lacking the § 2 NachwG catalogue (pay components, overtime rules, working hours, notice periods, place of work, TV/BV references, training, retirement provision) is an administrative offense (§ 4 NachwG, up to €2,000) and shifts proof burdens.
2. **Internal contradictions** — e.g. probation clause vs. termination clause, fixed-term clause vs. "unbefristet" preamble, bonus promise vs. Freiwilligkeitsvorbehalt, Freistellungsklausel vs. variable-pay clause. Under § 305c Abs. 2 BGB ambiguities resolve against the drafter.
3. **Gaps** — no notice period (statute fills in § 622 BGB — usually fine but must be flagged), no place of work, no Arbeitszeit definition, no Überstundenregelung, no TV reference → gaps invite § 306 Abs. 2 BGB defaults and disputes.
4. **References to expired/terminated collective agreements** — dynamic references to lapsed TVs (P41) or BVs without Fortgeltung (P42) → pay/condition gaps; must be flagged for verification against the current TV register.
5. **Non-gender-neutral pay structure** — pay bands or criteria discriminating by gender (P16) violate EntgTranspG/Art. 157 TFEU and, post-2026, the pending EU 2023/970 transposition.
6. **Boilerplate from other jurisdictions** — US/UK legalese ("at will", "entire agreement" without German statutory interplay, "equitable relief", choice-of-law to foreign law, indemnity language, "no oral modification") — much of it is void or misleading under German mandatory law (P44, P47, P57, P29); must be translated into German-law-compliant terms.
7. **Gesamtzusage/Anspruch aufrecht "Tätigkeit nach freiem Ermessen"** — job-duties clauses delegating everything to the employer's discretion fail § 106 GewO/§ 307 BGB transparency.

## Source Notes

- All statute citations reflect the version in force as of 2026-08 (NachwG: 2022 + 1.1.2025 amendments; § 41 Abs. 2 SGB VI: in force 1.1.2026; Mindestlohn 13,90 € from 1.1.2026, 14,60 € from 1.1.2027; EU 2023/970 deadline 7.6.2026 not yet transposed; ArbZG electronic-recording reform pending).
- Verified BAG decisions cited with case numbers and dates: 5 AZR 517/09 (01.09.2010), 5 AZR 406/10 (17.08.2011), 10 AZR 97/07 (12.12.2007), 10 AZR 290/17 (27.06.2018), 10 AZR 26/12 (16.01.2013), 9 AZR 464/00 (11.12.2001), 1 ABR 22/21 (13.09.2022), 9 AZR 541/15 (19.02.2019), 2 AZR 160/24 (30.10.2025), 2 AZR 96/24 (B) (18.06.2025), 5 AZR 108/25 (25.03.2026), 5 AZR 595/17 (11.07.2018), 5 AZR 553/17 (17.10.2018), 6 AZR 75/18 (07.02.2019), 2 AZR 582/13 + 8 AZR 130/13 (23.01.2014), 10 AZR 162/24 (30.10.2024), 5 AZR 700/09 (01.09.2010).
- Case numbers without a confirming primary/secondary source are marked `[unverified]` inside the entries (P8, P42 use them only as secondary pointers with the rule anchored in settled principles).
