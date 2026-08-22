# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
