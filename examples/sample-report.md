# Contract Review Report — Befristeter Arbeitsvertrag · Muster GmbH / Erika Mustermann

*Fictional sample — not a real contract; generated for demonstration. Real reports include contract metadata and verbatim clause quotes.*

**Law as of:** 2026-08-22 · **Report language:** de · **Extraction confidence:** hoch

## At a glance

Standardformular-Befristungsvertrag der Muster GmbH (dritte aufeinanderfolgende Befristung, kein sachlicher Grund); AGB-Prüfung angewendet. Befunde: 1 kritisch, 1 hoch, 1 niedrig. Der kritische Befund zur Befristung erfordert vor Unterschrift eine anwaltliche Prüfung.

- **F001 (Kritisch)** — Die dritte Befristung ohne sachlichen Grund ist sehr wahrscheinlich unwirksam (unwirksam = bindet dich in der Befristung nicht); das Arbeitsverhältnis gilt dann als unbefristet fortbestehend und endet nicht am 28.02.2028.
- **F002 (Hoch)** — Die verspätete Niederschrift verschiebt die Beweislast zu deinem Vorteil (bestrittene Vertragsbedingungen gelten zu deinen Gunsten als vereinbart) und kann den Arbeitgeber bis 2.000 € kosten.
- **F003 (Niedrig)** — Der Arbeitszeitband ohne Kriterien ist ein Transparenzrisiko (dürfte im Streit gegen den Arbeitgeber ausgelegt werden); kein akuter Handlungsbedarf.

### Severity scale — fixed plain definitions (print verbatim, every report)

| Label | Plain meaning |
|---|---|
| Kritisch | Klausel ist unwirksam (rechtlich wirkungslos), bindet dich nicht, Handlungsbedarf vor Fristen |
| Hoch | Sehr wahrscheinlich unwirksam oder erhebliches Risiko — prüfen lassen |
| Mittel | Nur unter engen Bedingungen wirksam oder risikobehaftet |
| Niedrig | Gestaltungsschwäche / Transparenzproblem, kein akuter Handlungsbedarf |

### Top risks (one plain sentence each: ID + severity + one-line legal pointer; citations stay in annex)

1. **F001 (Kritisch)** — Dritte sachgrundlose Befristung trotz Vorbeschäftigung beim selben Arbeitgeber: § 14 Abs. 2 Satz 2 TzBfG sperrt die Befristung, der Vertrag ist unbefristet.
2. **F002 (Hoch)** — Niederschrift nach § 2 Abs. 1 NachwG erst 3 Wochen nach Arbeitsbeginn übergeben; Beweislastumkehr nach § 4 Satz 1 NachwG, Bußgeld bis 2.000 €.
3. **F003 (Niedrig)** — Verteilung der Arbeitszeit „nach betrieblichen Erfordernissen" ohne Kriterien: Transparenzdefizit nach § 307 Abs. 1 Satz 2 BGB, kein Verstoß gegen das ArbZG ersichtlich.

## Action plan

<Uncertainty legend: hoch → „—"; mittel → „mittlere Sicherheit — vor Umsetzung bestätigen lassen"; niedrig → „niedrige Sicherheit — verifizieren"; law_in_flux → „Rechtslage in Bewegung — Reform nicht in Kraft"; extraction niedrig → „OCR-unsicher — am Original prüfen".>

| # | Priorität | Finding | Wer handelt | Aktion (eine verständliche Handlungszeile) | Unsicherheit |
|---|---|---|---|---|---|
| 1 | 1 | — | Du | Anwalt einschalten: Klärung, ob das Arbeitsverhältnis unbefristet fortbesteht (F001) und ob Ansprüche aus der verspäteten Niederschrift bestehen (F002). | — |
| 2 | 1 | F001 | Du / Anwalt | Entfristung geltend machen; Frist des § 17 TzBfG (3 Wochen nach schriftlicher Mitteilung) beachten; keine Verlängerungsunterschrift ohne Rechtsrat. | — |
| 3 | 2 | F002 | Arbeitgeber | Schriftliche Nachbesserung verlangen: vollständige Niederschrift nach § 2 Abs. 1 NachwG inkl. Sonderzahlungsbedingungen (Nr. 13). | — |
| 4 | 3 | F003 | Arbeitgeber | Arbeitszeitband konkretisieren (Kernzeit, Verteilungsrahmen, Ausgleichsfenster); sonst Transparenzrisiko im Streitfall. | mittlere Sicherheit — vor Umsetzung bestätigen lassen |

## Contract metadata

| Feld | Wert |
|---|---|
| Jurisdiktionsannahme | german |
| Vertragstyp | standard-form |
| AGB-Prüfung angewendet | ja |
| Analysierte Klauseln | 4 |

## Findings table

| ID | Klausel | Kategorie | Schwere | Rechtliche Einordnung | Was das für dich bedeutet | Sicherheit |
|---|---|---|---|---|---|---|
| F001 | C01 | Befristung (Kettenbefristung) | **Kritisch** | § 14 Abs. 2 Satz 2 TzBfG sperrt die sachgrundlose Befristung bei Vorbeschäftigung; Befristung unwirksam (§ 16 TzBfG) | Du bist unbefristet beschäftigt; der Vertrag endet nicht am 28.02.2028 | hoch |
| F002 | C02 | NachwG | **Hoch** | § 2 Abs. 1 NachwG: Niederschrift verspätet und unvollständig; § 4 Satz 1 Beweislastumkehr, § 4 Satz 3 Bußgeld bis 2.000 € | Bestrittene Vertragsbedingungen gelten zu deinen Gunsten als vereinbart | hoch |
| F003 | C03 | Arbeitszeit (Transparenz) | **Niedrig** | § 307 Abs. 1 Satz 2 BGB: Arbeitszeitband ohne Kriterien intransparent; kein ArbZG-Verstoß ersichtlich | Im Streit dürfte die Verteilung zu deinen Gunsten ausgelegt werden | mittel |

## Risk profile

- **Zählung:** Kritisch 1 · Hoch 1 · Mittel 0 · Niedrig 1.
- **F001 (Kritisch)** — Kettenbefristung ohne Sachgrund: Rechtsfolge ist die Entfristung, nicht die Beendigung. Zentrale Frage des Vertrags; rechtliche Mechanik in der Annex-Stelle C01.
- **F002 (Hoch)** — NachwG-Verstoß mit Beweislastumkehr; finanzielle Exposition des Arbeitgebers (Bußgeld bis 2.000 €), kein direkter Anspruch für dich.
- **F003 (Niedrig)** — Transparenzdefizit, faktisch nur im Streit relevant.
- `critical_findings: true` — Seek-Counsel-Trigger ist ausgelöst (erste Aktionszeile).

## Cross-cutting checks

- **NachwG § 2(1) completeness:** unvollständig. Angaben zu Nr. 2–6, 9, 10 nicht innerhalb von 7 Tagen nach Arbeitsbeginn; Nr. 13 (Sonderzahlungen) fehlt vollständig. Ein vollständiger schriftlicher Vertrag nach § 2 Abs. 5 NachwG liegt nicht vor (Niederschrift erst nach 3 Wochen, ohne Sonderzahlungsbedingungen). Beweislastumkehr § 4 Satz 1, Bußgeldrahmen § 4 Satz 3 (bis 2.000 €).
- **Whole-contract AGB review:** Formularvertrag (keine handschriftlichen Änderungen, mehrfachverwendungsfähige Vorlagenformulierung). § 305c Abs. 2 BGB (Unklarheitenregel) wirkt zugunsten der Arbeitnehmerin beim Arbeitszeitband. Die salvatorische Klausel in § 7 kann eine unwirksame Befristung nicht heilen (§ 306 BGB; geltungserhaltende Reduktion unzulässig).
- **Statutory-floor sweep:** 4.200,00 € brutto / 39 h pro Woche ≈ 24,85 €/h ≥ MiLoG 13,90 €/h (2026) und 14,60 €/h (ab 1.1.2027) — keine Unterschreitung. 39 h/Woche innerhalb des ArbZG-Rahmens (8 h/Tag bei 5-Tage-Woche); keine Ruhezeitproblematik ersichtlich.
- **Contradictions:** keine zwischen Klauseln; kein TV/BV-Bezug im Vertrag (NachwG Nr. 14 entfällt mangels Tarifbindung).

## Clause-by-clause annex

### C01 · § 1 Laufzeit

> „Das Arbeitsverhältnis beginnt am 1. September 2026 und ist befristet bis zum 28. Februar 2028. Es handelt sich um die dritte aufeinanderfolgende befristete Anstellung bei der Muster GmbH; ein sachlicher Grund für die Befristung besteht nicht."

- **F001 (Kritisch)** — Kettenbefristung: dritte aufeinanderfolgende sachgrundlose Befristung trotz Vorbeschäftigung beim selben Arbeitgeber. § 14 Abs. 2 Satz 2 TzBfG sperrt die sachgrundlose Befristung bei Vorbeschäftigung (BVerfG, Beschl. v. 06.06.2018 – 1 BvL 7/14; BAG, Urt. v. 23.01.2019 – 7 AZR 733/16). Rechtsfolge: Befristung unwirksam, unbefristetes Arbeitsverhältnis (§ 16 TzBfG); Geltendmachung binnen 3 Wochen nach schriftlicher Mitteilung (§ 17 TzBfG). Confidence: hoch.
- **Was zu tun ist:** Anwalt einschalten und Entfristung geltend machen; keine Unterschrift auf eine Verlängerung ohne Rechtsrat.
- **Empfohlene Formulierung:** „Unbefristetes Arbeitsverhältnis; eine erneute Befristung nur mit schriftlich benanntem sachlichem Grund nach § 14 Abs. 1 TzBfG."

### C02 · § 3 Vergütung

> „Die monatliche Bruttovergütung beträgt 4.200,00 € bei einer wöchentlichen Arbeitszeit von 39 Stunden. Ein Weihnachtsgeld wird gewährt."

- **F002 (Hoch)** — NachwG: Niederschrift nach § 2 Abs. 1 NachwG erst 3 Wochen nach Arbeitsbeginn übergeben; Angaben zu Nr. 2–6, 9, 10 nicht innerhalb der 7-Tage-Frist; Nr. 13 (Sonderzahlungen) nicht konkretisiert (Weihnachtsgeld ohne Höhe, Fälligkeit, Rückzahlungsbedingungen). § 4 Satz 1 NachwG: Beweislastumkehr zugunsten der Arbeitnehmerin; § 4 Satz 3: Bußgeld bis 2.000 €. Confidence: hoch.
- **Was zu tun ist:** Schriftliche Nachbesserung verlangen; Sonderzahlungsbedingungen (Höhe, Fälligkeit, Rückzahlung) schriftlich fixieren.
- **Empfohlene Formulierung:** „Die Niederschrift nach § 2 Abs. 1 NachwG wird spätestens am ersten Arbeitstag übergeben und enthält alle 15 Angaben, einschließlich Höhe, Fälligkeit und Rückzahlungsbedingungen der Sonderzahlung."

### C03 · § 5 Arbeitszeit

> „Die wöchentliche Arbeitszeit beträgt 39 Stunden. Die Lage der Arbeitszeit richtet sich nach den betrieblichen Erfordernissen."

- **F003 (Niedrig)** — Transparenzdefizit: Verteilung der Arbeitszeit ohne Kriterien (keine Kernzeit, kein Verteilungsrahmen, kein Ausgleichsfenster) — § 307 Abs. 1 Satz 2 BGB. Kein Verstoß gegen das ArbZG ersichtlich (39 h/Woche); kein Abrufarbeitsverhältnis nach § 12 TzBfG. Confidence: mittel.
- **Was zu tun ist:** Arbeitszeitband konkretisieren (Kernzeit, Rahmen, Ausgleichsfenster); keine rechtliche Unwirksamkeit, aber Klarstellungsbedarf.
- **Empfohlene Formulierung:** „Die wöchentliche Arbeitszeit beträgt 39 Stunden im 6-Monats-Ausgleichsfenster. Kernzeit ist montags bis freitags 9–15 Uhr; der Arbeitszeitrahmen liegt zwischen 7 und 19 Uhr."

### C04 · § 7 Schlussbestimmungen

> „Änderungen dieses Vertrags bedürfen der Schriftform. Sollten einzelne Bestimmungen unwirksam sein, bleibt der Vertrag im Übrigen wirksam."

- **Kein Befund (no_issue_found):** Schriftformklausel und salvatorische Klausel sind Standardformulierung. Hinweis: Die salvatorische Klausel kann eine unwirksame Befristung nicht heilen (§ 306 BGB, keine geltungserhaltende Reduktion) — verweist auf F001.

## Disclaimer

**Das ist keine Rechtsberatung.** Dieser Bericht bewertet Risiken und Wirksamkeit von Vertragsklauseln — Befunde, keine Garantien für Wirksamkeit, Unwirksamkeit oder Prozessausgang. Das Recht ist auf das im Bericht genannte Datum fixiert (Law as of: 2026-08-22) und kann sich ändern; Beträge und Schwellen werden vor jedem Lauf neu verifiziert. Eingebaute Seek-Counsel-Trigger lösen bei jedem kritischen Befund, bei hohen Befunden mit finanzieller Exposition oder bei zentralen Klauseln mit ungesicherter Rechtslage eine Verweisung an einen Anwalt aus. Es werden ausschließlich verifizierte Quellen zitiert: keine Aktenzeichen ohne Whitelist- oder web-verifizierte Quelle. Bei Zweifeln: Fachanwalt für Arbeitsrecht in Deutschland konsultieren.
