# Security

## Reporting a vulnerability

Open a **GitHub issue** on this repository and apply the `security` label. Do not include
confidential information, personal data, or real contract text in the issue. Issues are the only
supported reporting channel — no email addresses are used for this project.

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
  If you find personal data in any committed file, report it via the issue channel above.
- Findings are limited to verified sources: statute sections, the `case-law.md` whitelist, or
  web-verified citations with URL and date. No fabricated citations.

## Responsible disclosure

Please give maintainers a reasonable window to respond to and fix a reported issue before public
disclosure.
