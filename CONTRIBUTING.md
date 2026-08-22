# Contributing

**German Employment Contract Review** is a self-contained skill definition that assesses full
German employment contracts (Arbeitsvertrag) for legal pitfalls under German law with an EU-law overlay.

## How to contribute

- **Open an issue first** for any knowledge-base change (references/) or SKILL.md change. The
  knowledge base is curated and verified; changes are reviewed against the citation gate below
  before merging.
- For bugs, documentation fixes, or packaging improvements, open an issue or submit a pull
  request directly.

## Quality bar

- **No fabricated case law (hard rule).** Findings may cite only:
  1. statute sections,
  2. entries from the `references/case-law.md` whitelist, or
  3. web-verified citations with URL and date.
  A case number that cannot be sourced must never be emitted.
- **Confidence labels are mandatory.** Every finding carries a `high` / `medium` / `low`
  confidence label; `low` requires an explicit reason (unverified basis, extraction-affected,
  unsettled law).
- **`law_as_of` must be updated** in `SKILL.md` frontmatter whenever legal content changes, and
  every reference file self-pins its as-of date.
- **HTML reports are derived, never hand-edited.** Any content change happens in the markdown (or
  the JSON), then the HTML is regenerated with `python3 tools/render_report.py report.md report.html`.
- **Keep `output/` out of commits.** It holds private run artifacts (real contract OCR, page
  scans, generated reports) with personal data — it is gitignored and must stay that way.

## Scope notes

- Legal content lives in `references/` (statutes, EU law, pitfalls, case-law, checklists,
  glossary); `SKILL.md` holds procedure, decision rules, and the output schema.
- One fact lives in one file: reference by ID (`see P1`, `case-law: BAG 2 AZR 160/24`), never
  duplicate.
