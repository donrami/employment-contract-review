# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-08-24

### Added
- Annotated contract PDF: `tools/annotate_contract.py` embeds every finding at its
  clause location on the original scanned pages (yellow highlight, severity callout in a
  dedicated gutter, cover sheet). Fourth report artifact, wired into SKILL.md Phase 5.
- `--min-severity CRITICAL|HIGH|MEDIUM|LOW` filter: only findings at or above the
  chosen severity are annotated; contract-wide findings are always included.
- Cover sheet now lists each placed finding with its page reference, plus separate
  sections for contract-wide findings and any unlocated quotes.
- Test suite `tests/test_annotate_contract.py` (14 unittest tests) with on-the-fly
  fixtures covering quote location, highlight quads, callout wrapping, and CLI parsing.

### Fixed
- Gutter callouts truncated long recommended-action texts; boxes now size to fit the
  full text (with page-boundary clamping and a pointer to the full report).
- Leader lines could cross when multiple findings shared a page; findings are now
  drawn in vertical order so lines never cross.
- Removed the dead fourth argv slot from legacy invocations.

## [1.0.0] - 2026-08-22

### Added
- Initial public release: SKILL.md with phase-driven German employment-contract review
  (`name: ger-employment-contract-review`, `law_as_of: 2026-08-22`).
- Curated knowledge base: `references/` (statutes, EU law, pitfalls, case-law whitelist,
  checklists, glossary).
- Stdlib-only renderer `tools/render_report.py` → report.md / report.json / report.html
  (JSON Schema draft 2020-12).
- MIT license, CONTRIBUTING.md, SECURITY.md.

## Versioning

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
with the following mapping:

- **Major** — breaking skill-interface/schema changes (JSON Schema, phase structure).
- **Minor** — new pitfall/checklist categories or law updates.
- **Patch** — corrections/renderer fixes.
