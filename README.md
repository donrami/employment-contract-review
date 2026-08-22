# German Employment Contract Review — Arbeitsvertrags-Check

Automated risk assessment of full German employment contracts (Arbeitsvertrag) under German law with an EU-law overlay — clause-by-clause pitfall findings, verified legal basis, and bilingual German/English reports.

Machine skill id: `ger-employment-contract-review` · Law as of: 2026-08-22.

## What it is

A self-contained skill that reviews a complete German employment contract and returns structured, evidence-first findings — an employee-protective second reader for the recurring void-clause classes (probation periods, fixed-term limits, flat overtime clauses, non-competes, missing NachwG terms). Packaged as a portable skill definition (`SKILL.md` plus a curated reference knowledge base) that any skill-capable agent harness can load.

### Features

- **Clause inventory** — every clause tagged from a fixed taxonomy, quoted verbatim, split and merged as needed.
- **Per-finding severity** — each finding rated Critical / High / Medium / Low with a verified legal basis (statute section or whitelisted case law).
- **NachwG § 2 completeness check** — all 15 mandatory items against the inventory, with day-1 / 7-day / 1-month deadline classes.
- **Whole-contract AGB review** — transparency, surprising clauses, ambiguity-against-drafter, severability (for standard-form contracts).
- **Statutory-floor sweep** — every monetary, leave, and working-time term against mandatory floors (MiLoG, ArbZG, BUrlG, EFZG, KSchG, TzBfG, EntgTranspG).
- **Structured reports** — JSON (canonical), markdown (human-readable source of truth), and a self-contained HTML view.
- **Bilingual DE/EN** — findings reproducible in both languages via the glossary; detection of German, English, or mixed contracts.
- **Citation whitelist** — findings cite only statute sections, the verified case-law whitelist, or web-verified sources with URLs; a hallucination firewall against fabricated case numbers.
- **Law-as-of pinning** — every report prints `Law as of: 2026-08-22`; unsettled law is flagged `law_in_flux`, never applied early.

## How it works

Five strictly sequential phases, each loading only the reference files it needs (the loading map — no wholesale loading, one fact lives in one file):

| Phase | What happens |
|---|---|
| 0 — Intake | Extract the contract (PDF, scan via OCR, docx, pasted text, or URL); detect language; determine jurisdiction and contract type (standard-form vs. individually negotiated) |
| 1 — Normalize | Strip headers/footers/page numbers; build the verbatim clause inventory (C01…); tag clause types |
| 2 — Clause-by-clause | Run the per-category checklists against each clause → candidate pitfall findings with verified legal basis |
| 3 — Cross-cutting | NachwG § 2 completeness, whole-contract AGB review, statutory-floor sweep, collective-law interplay, contradictions |
| 4 — Risk scoring | Severity per shared criteria; risk profile; confidence labels (high/medium/low) |
| 5 — Report | Emit three artifacts: JSON, markdown, and a rendered HTML view |

Each phase completes its uncertainty and escalation exits before the next begins — unreadable documents are reported, not guessed; unsourced suspicions are downgraded or dropped, never asserted.

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

## Reports

Every review produces the same content in three views:

- **`report.json`** — canonical structured output, JSON Schema draft 2020-12.
- **`report.md`** — the human-readable source of truth: at-a-glance verdict, action plan, findings table, risk profile, cross-cutting checks, and a clause-by-clause annex.
- **`report.html`** — self-contained HTML with severity badges, collapsible annex, and a print button. It is a derived view, generated from the markdown:

```bash
python3 tools/render_report.py report.md report.html
```

Stdlib only — no dependencies, no install step.

## Repository layout

| Path | Purpose |
|---|---|
| `SKILL.md` | Skill definition: procedure (phases 0–5), decision rules, loading map, JSON schema, report template, guardrails |
| `references/` | Curated legal knowledge base: `statutes.md`, `eu-law.md`, `pitfalls.md`, `case-law.md`, `checklists.md`, `glossary.md` |
| `tools/render_report.py` | Stdlib-only markdown-to-HTML report renderer |
| `output/` | Private run artifacts (contract OCR, page scans, generated reports) — gitignored, never committed |

## Disclaimer

**This is not legal advice.** The skill produces risk and validity assessments of contract clauses — findings, not guarantees of validity, invalidity, or litigation outcome. Law is pinned to the date printed in each report (`Law as of: 2026-08-22`) and can change; figures and thresholds are re-verified before each run. Built-in seek-counsel triggers fire boilerplate referral whenever a Critical finding appears, a High finding carries financial exposure, or a central term rests on unsettled law. A citation gate permits only verified sources: no case number is ever emitted without a whitelisted or web-verified source. When in doubt, consult a lawyer admitted in Germany.

## License, Contributing, Security

- **License:** MIT.
- **Contributing:** see [CONTRIBUTING.md](CONTRIBUTING.md).
- **Security:** see [SECURITY.md](SECURITY.md).

## Development

The markdown report is the source of truth for the human-readable view. To regenerate the HTML after editing the markdown:

```bash
python3 tools/render_report.py report.md report.html
```

The HTML is derived and never hand-edited: any content change happens in the markdown (or the JSON), then the HTML is regenerated, so the two views cannot drift.
