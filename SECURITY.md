# Security

## Reporting a vulnerability

Report via **private vulnerability reporting** (Settings → Code security → Private vulnerability reporting).
Do not include contract text or PII; if you must share a contract, use a redacted fictional excerpt.
Private reporting is the only supported channel — no email addresses are used for this project.

## Scope

Security-relevant areas of this project:

- **Skill outputs** — the JSON / markdown / HTML reports the skill produces from a contract.
- **`tools/render_report.py`** — the stdlib-only markdown-to-HTML renderer (input handling, HTML
  escaping, path handling).
- **Reference-content accuracy** — `references/` and `SKILL.md` are curated legal knowledge;
  incorrect citations or invented case law are treated as defects.

## Policy

- This is **legal-information tooling, not legal advice**. Reports are risk and validity
  assessments, not guarantees; when in doubt, consult a lawyer admitted in Germany.
- **No secrets or PII belong in the repository.** `output/` holds private run artifacts (real
  contract OCR, page scans, generated reports) and is gitignored — never commit anything from it.
  If you find personal data in any committed file, report it via private vulnerability reporting.
- Findings are limited to verified sources: statute sections, the `case-law.md` whitelist, or
  web-verified citations with URL and date. No fabricated citations.

## Responsible disclosure

Please give maintainers a reasonable window to respond to and fix a reported issue before public
disclosure.
