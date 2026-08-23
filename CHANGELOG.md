# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Annotated contract PDF: `tools/annotate_contract.py` embeds every finding at its
  clause location on the original scanned pages (yellow highlight, severity callout in a
  dedicated gutter, cover sheet). Fourth report artifact, wired into SKILL.md Phase 5.
  Gutter callouts size to fit the full recommended action, no truncation.

### Fixed
- Gutter callouts in the annotated PDF truncated long recommended-action texts; boxes now
  size to fit the full text (with page-boundary clamping).

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
