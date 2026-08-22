# German Employment Contract Review — Arbeitsvertrags-Check

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Law as of: 2026-08-22](https://img.shields.io/badge/law%20as%20of-2026--08--22-blue?style=flat-square)](SKILL.md)
[![Release](https://img.shields.io/github/v/tag/donrami/employment-contract-review?style=flat-square)](https://github.com/donrami/employment-contract-review/releases)

Automated risk assessment of full German employment contracts (Arbeitsvertrag) under German law with an EU-law overlay: clause-by-clause pitfall findings, verified legal basis, and bilingual German/English reports.

Machine skill id: `ger-employment-contract-review` · Law as of: 2026-08-22.

> Clone → register SKILL.md as a skill → trigger with "prüfe diesen Arbeitsvertrag" → get report.md + report.json + report.html.

## What it is

A self-contained skill that reviews a complete German employment contract and returns structured, evidence-first findings: an employee-protective second reader for the recurring void-clause classes (probation periods, fixed-term limits, flat overtime clauses, non-competes, missing NachwG terms). Packaged as a portable skill definition (`SKILL.md` plus a curated reference knowledge base) that any skill-capable agent harness can load.

## Sample output

*Fictional sample (Muster GmbH / Erika Mustermann), not a real contract. Real reports include contract metadata and verbatim clause quotes.*

```markdown
## At a glance
- Contract: fixed-term employment contract · Muster GmbH · Erika Mustermann
- Review date: 2026-08-22 · Law as of: 2026-08-22
- Findings: 3 (1 critical · 1 high · 1 low)

| ID | Severity | Finding | Legal basis |
|----|----------|---------|-------------|
| F-01 | Critical | Third successive fixed-term contract with no objective reason; § 14 Abs. 2 TzBfG inapplicable (prior employment with same employer) | TzBfG § 14 |
| F-02 | High | Written statement of essential terms not delivered within one week of start | NachwG § 2 |
| F-03 | Low | Overtime clause sets no cap or compensation; transparency gap | BGB § 307 |
```

Full fictional samples: [`examples/sample-report.md`](examples/sample-report.md), [`examples/sample-report.json`](examples/sample-report.json), [`examples/sample-report.html`](examples/sample-report.html).

## Features

- **Clause inventory**: every clause tagged from a fixed taxonomy, quoted verbatim, split and merged as needed.
- **Per-finding severity**: each finding rated Critical / High / Medium / Low with a verified legal basis (statute section or whitelisted case law).
- **NachwG § 2 completeness check**: all 15 mandatory items against the inventory, with day-1 / 7-day / 1-month deadline classes.
- **Whole-contract AGB review**: transparency, surprising clauses, ambiguity-against-drafter, severability (for standard-form contracts).
- **Statutory-floor sweep**: every monetary, leave, and working-time term against mandatory floors (MiLoG, ArbZG, BUrlG, EFZG, KSchG, TzBfG, EntgTranspG).
- **Structured reports**: JSON (canonical), markdown (human-readable source of truth), and a self-contained HTML view.
- **Bilingual DE/EN**: findings reproducible in both languages via the glossary; detection of German, English, or mixed contracts.
- **Citation whitelist**: findings cite only statute sections, the verified case-law whitelist, or web-verified sources with URLs; a hallucination firewall against fabricated case numbers.
- **Law-as-of pinning**: every report prints `Law as of: 2026-08-22`; unsettled law is flagged `law_in_flux`, never applied early.

## Usage

This is a self-contained skill definition, independent of any particular harness:

1. Clone the repository.
2. Register `SKILL.md` as a skill with your harness's skill-install mechanism.
3. Trigger the skill with one of its trigger phrases:
   - "assess employment contract"
   - "review Arbeitsvertrag"
   - "find pitfalls in this contract"
   - "is this clause valid"
   - "check this contract for problems"
   - "prüfe diesen Arbeitsvertrag"
4. Supply a contract as PDF, scan, docx, pasted clauses, or URL.

Outputs land as three files: `report.json` (canonical), `report.md` (human-readable report), and `report.html` (self-contained HTML view).

## How it works

Five strictly sequential phases, each loading only the reference files it needs (the loading map: no wholesale loading, one fact lives in one file):

| Phase | What happens |
|---|---|
| 0 · Intake | Extract the contract (PDF, scan via OCR, docx, pasted text, or URL); detect language; determine jurisdiction and contract type (standard-form vs. individually negotiated) |
| 1 · Normalize | Strip headers/footers/page numbers; build the verbatim clause inventory (C01…); tag clause types |
| 2 · Clause-by-clause | Run the per-category checklists against each clause → candidate pitfall findings with verified legal basis |
| 3 · Cross-cutting | NachwG § 2 completeness, whole-contract AGB review, statutory-floor sweep, collective-law interplay, contradictions |
| 4 · Risk scoring | Severity per shared criteria; risk profile; confidence labels (high/medium/low) |
| 5 · Report | Emit three artifacts: JSON, markdown, and a rendered HTML view |

Each phase completes its uncertainty and escalation exits before the next begins: unreadable documents are reported, not guessed; unsourced suspicions are downgraded or dropped, never asserted.

## Report formats

Every review produces the same content in three views:

- **`report.json`**: canonical structured output, JSON Schema draft 2020-12.
- **`report.md`**: the human-readable source of truth, with at-a-glance verdict, action plan, findings table, risk profile, cross-cutting checks, and a clause-by-clause annex.
- **`report.html`**: self-contained HTML with severity badges, collapsible annex, and a print button. It is a derived view, generated from the markdown:

```bash
python3 tools/render_report.py report.md report.html
```

Stdlib only: no dependencies, no install step.

## Repository layout

| Path | Purpose |
|---|---|
| `SKILL.md` | Skill definition: procedure (phases 0–5), decision rules, loading map, JSON schema, report template, guardrails |
| `references/` | Curated legal knowledge base: `statutes.md`, `eu-law.md`, `pitfalls.md`, `case-law.md`, `checklists.md`, `glossary.md` |
| `tools/render_report.py` | Stdlib-only markdown-to-HTML report renderer |
| `output/` | Private run artifacts (contract OCR, page scans, generated reports); gitignored, never committed |

## Deutsche Zusammenfassung

- **Was ist das?** Eine fertige Agent-Skill, die komplette deutsche Arbeitsverträge Klausel für Klausel auf rechtliche Risiken prüft: Befristung, Probezeit, Überstundenabgeltung, Wettbewerbsverbote, AGB-Kontrolle, NachwG-Pflichtangaben und gesetzliche Mindeststandards, mit verifizierter Rechtsgrundlage (Gesetzestext oder Whitelist-Rechtsprechung) und Risikobewertung je Befund.
- **Was liefert es?** `report.md` (menschenlesbar), `report.json` (maschinenlesbar, JSON Schema draft 2020-12) und `report.html` (selbstständige HTML-Ansicht), zweisprachig DE/EN.
- **Start:** Klone das Repository, registriere `SKILL.md` als Skill und triggere z. B. mit *„Prüfe diesen Arbeitsvertrag"*. Details unter [Usage](#usage).
- **Aktualität:** `law_as_of: 2026-08-22`; das Wissen wird gepflegt (siehe [CHANGELOG.md](CHANGELOG.md)).
- **Rechtshinweis:** Dies ist keine Rechtsberatung; siehe [Disclaimer](#disclaimer).

## Development

The markdown report is the source of truth for the human-readable view. To regenerate the HTML after editing the markdown:

```bash
python3 tools/render_report.py report.md report.html
```

The HTML is derived and never hand-edited: any content change happens in the markdown (or the JSON), then the HTML is regenerated, so the two views cannot drift.

## License & disclaimer

- **License:** MIT. See [LICENSE](LICENSE).
- **Not legal advice:** This is not legal advice. The skill produces risk and validity assessments of contract clauses: findings, not guarantees of validity, invalidity, or litigation outcome. Law is pinned to the date printed in each report (`Law as of: 2026-08-22`) and can change; figures and thresholds are re-verified before each run. Built-in seek-counsel triggers fire boilerplate referral whenever a Critical finding appears, a High finding carries financial exposure, or a central term rests on unsettled law. A citation gate permits only verified sources: no case number is ever emitted without a whitelisted or web-verified source. When in doubt, consult a lawyer admitted in Germany.
- **Contributing:** see [CONTRIBUTING.md](CONTRIBUTING.md) · **Security:** see [SECURITY.md](SECURITY.md) · **Changelog:** [CHANGELOG.md](CHANGELOG.md)
