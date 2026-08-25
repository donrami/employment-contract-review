# Citation Cross-Check: sebischair rules vs. ger-law case-law whitelist

**Date:** 2026-08-25 · **Dataset:** v3_2026-01 `rules.json` (30 rules, 35 court references)
**Whitelist:** `references/case-law.md` (92 entries, law pinned 2026-08-22)
**License:** CC BY-NC 4.0 dataset — fetched at runtime, never vendored; no clause/rule
text or wording copied. Script: `eval/citations/crosscheck.py`.

## Method

`crosscheck.py` fetches `rules.json` from the TUM sebis repo, extracts court-decision
references (`BAG/EuGH/BGH/LAG/OLG` + case number), normalizes case numbers (strips
CJEU name suffixes, senate qualifiers, dash variants), and compares both directions
against the whitelist. A second check compares decision dates on matched pairs to
catch same-case-number/different-date drift.

## Headline findings

| Metric | Count |
|---|---|
| Dataset court references | 35 (34 unique cases) |
| Whitelist entries | 92 |
| **Overlapping cases (both sides)** | **7** |
| Matching references | 8 (one case cited by 2 rules) |
| Dataset-only citations | 27 |
| Whitelist-only cases | 85 |
| **Date discrepancies on matches** | **1 (dataset error)** |

### Overlap (dataset refs that are whitelisted) — 7 cases

| Case | Dataset rule | Date (dataset / whitelist) |
|---|---|---|
| 5 AZR 517/09 | Abgegoltene Überstunden | 01.09.2010 / 1.9.2010 ✓ |
| 6 AZR 23/19 | Nebenbeschäftigung Einschränkung | 19.12.2019 / 19.12.2019 ✓ |
| 8 AZR 897/08 | Vertragsstrafe in Probezeit | 23.09.2010 / 23.9.2010 ✓ |
| 10 AZR 448/15 | Wettbewerbsverbot Karenzentschädigung + Max. Dauer | 22.03.2017 / 22.3.2017 ✓ |
| 10 AZR 710/14 | Günstigkeitsprinzip | **20.07.2016 / 3.8.2016 ✗** |
| C-684/16 | Urlaub Übertragbarkeit | 06.11.2018 / 6.11.2018 ✓ |
| C-619/16 | Urlaub Übertragbarkeit | 06.11.2018 / 6.11.2018 ✓ |

The claimed overlap cases `9 AZR 203/10` and `9 AZR 323/19` are **not** whitelisted
— they are dataset-only (see below). This corrects the earlier assumption in
brainstorm-notes.md that they were shared.

### One-sided: dataset-only citations — 27

Not in the whitelist; grouped by topic (all BAG unless noted):

- **Ausschlussfristen:** 9 AZR 44/19, 5 AZR 262/17, 5 AZR 52/05, 5 AZR 43/18, 5 AZR 498/21, 8 AZR 280/12, 9 AZR 461/21, **9 AZR 203/10**, **9 AZR 323/19**
- **Kündigungsfrist:** 6 AZR 705/15, 2 AZR 264/6, 8 AZR 896/07, 6 AZR 158/16, 8 AZR 717/07, 2 AZR 213/23
- **Überstunden/Abgeltung:** 5 AZR 765/10, 5 AZR 452/18
- **Wettbewerbsverbot:** 10 AZR 392/17
- **Urlaub:** 9 AZR 266/20
- **Vergütung:** 9 AZR 187/22, 9 AZR 260/21
- **Verschwiegenheit:** 3 AZR 83/79, LAG Mecklenburg-Vorpommern 2 Sa 183/09
- **Vertragsstrafe:** 8 AZR 665/14
- **Form/Postzugang:** 9 AZR 382/07, 8 AZR 136/22
- **Pausenregelung:** 5 AZR 200/10
- **Sonstige:** BGH VIII ZR 232/75

High-value candidate additions to the whitelist if verified by URL (BAG press
release / court page): 9 AZR 203/10 and 9 AZR 323/19 (Einseitige Ausschlussfrist —
core employee-protective topic), plus 9 AZR 461/21, 9 AZR 266/20, 10 AZR 392/17.

### One-sided: whitelist-only cases — 85

Cases our whitelist has that the dataset never cites. Notable absences from the
dataset's rule set:

- **EntgTranspG / equal pay:** 8 AZR 483/18, 8 AZR 488/19, 8 AZR 300/24 — no equal-pay rule at all
- **Gratifikation/clawback:** 10 AZR 825/06, 10 AZR 634/06, 10 AZR 290/17, 10 AZR 26/12, 10 AZR 529/92, 10 AZR 177/12
- **Zeugnis:** 9 AZR 352/04, 6 AZR 683/16, 9 AZR 227/11, 2 AZR 96/24
- **Ausschlussfristen detail:** 5 AZR 572/04, 5 AZR 422/12, 5 AZR 888/08, 5 AZR 313/99, 8 AZR 58/20, 9 AZR 162/18
- **Fixed-term / Vorbeschäftigung:** 7 AZR 733/16, 7 AZR 140/15, 7 AZR 452/17, 7 AZR 203/23, 7 AZR 300/22, 1 BvL 7/14
- **Leave (CJEU):** C-214/10, C-337/10, C-569/16, C-570/16, C-684/16-related 9 AZR 423/16 etc.
- **Vertragsstrafe depth:** 8 AZR 196/03, 8 AZR 973/06, 2 AZR 582/13, 8 AZR 130/13, 8 AZR 378/16, 5 AZR 703/15
- **Non-compete:** 9 AZR 464/00, 8 AZR 12/86 (Nebentätigkeit); 10 AZR 448/15 is the only non-compete overlap

## Verified data error in the dataset

`10 AZR 710/14` (rule "Günstigkeitsprinzip") is dated **20.07.2016** in the dataset;
authoritative sources (BAG press release 41/16, juris, ECLI:DE:BAG:2016:030816.U.10AZR710.14.0)
give **3.8.2016**. Our whitelist is correct; the dataset has a typo. The cross-check
flags this automatically via date comparison.

## Implications

1. **Whitelist coverage gap:** 27 dataset-cited BAG decisions are absent from our
   whitelist. The two headline ones (`9 AZR 203/10`, `9 AZR 323/19` — both
   Ausschlussfristen, one of the dataset's 100%-unfair/void topics) should be
   considered for addition after URL verification, per the whitelist's own
   maintenance rules.
2. **Dataset does not cover our full scope:** 85 whitelist cases (Entgelt-
   transparentz, Zeugnis, Gratifikation, fixed-term depth, CJEU leave) have no
   counterpart in the dataset's 30 rules — the dataset is not a superset of our
   knowledge base, so it is a benchmark complement, not a replacement.
3. **Benchmark value:** the 7 shared cases are the strongest anchor for a future
   eval set — both sides independently cite the same authority. The dataset's
   citation typo (10 AZR 710/14) is a caution for using its references as ground
   truth without independent verification.

## Reproduction

```bash
python3 eval/citations/crosscheck.py          # tables
python3 eval/citations/crosscheck.py --json   # machine-readable
```

Network required for the dataset fetch; the whitelist is read locally from
`references/case-law.md`.
