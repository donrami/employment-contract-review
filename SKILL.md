---
name: ger-employment-contract-review
description: >
  Assess full German employment contracts (Arbeitsvertrag, employment
  agreement, employment contract) for legal pitfalls under German law with
  EU-law overlay. Trigger phrases: "assess employment contract", "review
  Arbeitsvertrag", "find pitfalls in this contract", "is this clause valid",
  "check this contract for problems", "prüfe diesen Arbeitsvertrag".
  Activates when the user supplies a contract text — PDF, scan, docx,
  pasted clauses, or URL — and asks for review, validation, risk assessment,
  AGB/statutory compliance checking, or clause-by-clause analysis.
  Delivers: clause inventory, per-finding severity (Critical/High/Medium/
  Low), legal basis with verified citations, recommended rewording,
  NachwG § 2 completeness check, whole-contract AGB review, statutory-floor
  sweep, structured JSON + human-readable markdown report.
  Out of scope: drafting full contracts from scratch, legal advice or
  outcome guarantees, litigation strategy, collective-bargaining
  negotiation support, non-German law (flag and stop unless conflict-of-
  laws note is requested).
law_as_of: 2026-08-22
---

# Procedure — German/EU employment-contract assessment

Assessment support only. Emit clause-level pitfall findings with verified legal basis. RFC-2119: MUST/SHOULD are binding.

## 1. File tree & knowledge base

```
ger-law/
  SKILL.md                 # procedure, phases 0–5, decision rules, loading map, schema, guardrails, law_as_of
  references/
    statutes.md            # German statutory framework, per-statute floors
    eu-law.md              # EU directives, CJEU case law, transposition status
    pitfalls.md            # master pitfall catalog: ID, name, basis, severity, fix
    case-law.md            # verified citation index: BAG/BVerfG/CJEU, issue-tagged — the hallucination firewall
    checklists.md          # per-category review decision trees + NachwG/AGB checklists
    glossary.md            # DE↔EN terms, statute abbreviations, EU directive numbers
```

**Loading map (MUST follow):** Phase 0 → glossary.md (skim); Phase 1 → SKILL.md only; Phase 2 → checklists.md + pitfalls.md fully, case-law.md on demand; Phase 3 → statutes.md + eu-law.md fully, checklists.md NachwG/AGB sections; Phase 4 → pitfalls.md severity section; Phase 5 → SKILL.md schema.

NEVER load reference files wholesale; each phase loads only its map entries. One fact lives in one file — reference by ID (`see P1`, `case-law: BAG 2 AZR 160/24`), never duplicate. Severity criteria live ONLY in pitfalls.md; statutory floors ONLY in statutes.md; citation whitelist ONLY in case-law.md. Every reference file self-pins its as-of date; every report MUST print `Law as of: <law_as_of>` from this frontmatter.

## 2. Phases 0–5 (strictly sequential; each phase MUST complete its uncertainty/escalation exits before the next)

### Phase 0 — Intake
1. **Format:** PDF/docx → `read` extraction. Scanned image → OCR path; set `extraction_confidence: low` per affected clause and surface in report. Paste → verbatim text, no extraction.
2. **Language:** detect DE/EN/mixed via glossary keyword scan; report in contract's dominant language or user preference.
3. **Jurisdiction:** German law presumed when contract is in German, cites German statutes (BGB, TzBfG, ArbZG, MiLoG…), German employer address, works-council references. Non-German signals (foreign governing law, non-German employer, English-only with no German references) → conflict-of-laws note (Rome I Art. 8 mandatory-protection floor; Art. 9 overriding mandatory provisions). Proceed on German-law aspects only if the user confirms; label `jurisdiction_assumption: flagged`; else STOP and report.
4. **Contract type (MUST determine — gates AGB review):** standard-form (§ 305(1) BGB, full §§ 305–310 review) vs individually-negotiated (escapes §§ 307–309 but NOT mandatory floors §§ 134/138/242 BGB). Evidence: boilerplate layout, multi-employee form language, absence of hand-written amendments. Ambiguous → treat as AGB (§ 305c(2) BGB, employee-protective default), label the assumption.
5. **Collective-agreement context:** reference to TV/BV (NachwG § 2(1) item 15) → note; full TV review out of scope; § 4(3) TVG interplay checked in Phase 3. Optional auxiliary TV/BV PDF accepted as context only.
6. **web_search:** max 2 queries, only for figures/thresholds the references don't pin or explicit user ask. Otherwise none.
7. **Escalation exits:** legal-advice/outcome-prediction asks → refuse, offer findings + counsel referral. Unreadable document → failure report with extraction error; NEVER guess content.

### Phase 1 — Normalize
1. Strip headers/footers/page numbers/signature blocks (keep signature date as metadata).
2. Build clause inventory: `C01`… (`clause_id_orig` preserved), headings, verbatim quotes only — NEVER paraphrase in the inventory; findings quote it.
3. Tag clause type from fixed taxonomy: probation, duration/fixed-term, remuneration, working-time, leave, termination, post-contractual restraint, confidentiality, secondary employment, overtime, on-call, training costs, pension, transfer/change, boilerplate, signature/misc.
4. Merge split clauses (page-break continuation); split merged clauses (multiple issues in one numbered clause → multiple tagged entries, same `clause_id`).
5. **Uncertainty:** OCR-garbled text → `extraction_confidence: low`, analyze legible portion only, flag in report. Untaggable → `category: other` + explicit note, never silence.

### Phase 2 — Clause-by-clause
1. Per tagged clause, run the matching checklist from checklists.md → candidate pitfall IDs (P-catalog, pitfalls.md).
2. One finding per distinct issue. Two issues in one clause → two findings, same `clause_id`. Same issue in two clauses → two findings (clause-level granularity required for the annex).
3. No forced matches: checklist completes with no triggers → `no_issue_found`, never invent an issue.
4. **web_search:** max 3 queries per contract, only when (a) a clause depends on a figure/threshold newer than the references' as-of, or (b) the user explicitly asks about a recent development. Every web-derived claim cited with URL + `[web-verified 2026-08-22]` in `sources`. Budget exhausted without verification → `confidence: low`, `[unverified]` marker; NEVER an invented citation.
5. **Uncertainty:** no verified legal basis for a suspicion → `Low` drafting note or drop; NEVER assert a legal consequence without a basis. Unsettled law (e.g. ArbZG 8h→weekly reform pending) → `law_in_flux: true` with current rule + pending-change note; never apply unenacted reform.
6. **Fact-dependent validity** (e.g. Matzak-level on-call intensity, C-518/15) → state the legal test, recommend counsel confirmation; do not resolve facts yourself.

### Phase 3 — Cross-cutting
1. **NachwG § 2(1) completeness:** all 15 mandatory items vs inventory; per-item deadline classes — day 1: items 1, 7, 8; 7 days: items 2–6, 9, 10; 1 month: items 11–15. Missing → finding `category: nachwg` at catalog severity (reversed burden of proof § 4 S. 1; fine exposure up to €2,000). A full written contract satisfying § 2(5) counts as the Niederschrift — completeness check still runs.
2. **Whole-contract AGB review** (form contracts only): transparency § 307(1) S. 2 BGB; surprising clauses § 305c(1); ambiguity against drafter § 305c(2); severability § 306 — salvatorische Klausel cannot cure void clauses.
3. **Statutory-floor sweep:** every monetary/leave/time term vs mandatory floors — MiLoG (§ 1: €13.90/h from 1.1.2026, €14.60 from 1.1.2027), ArbZG (8 h/day, 11 h rest), BUrlG (4 weeks), EFZG, KSchG notice periods, TzBfG, EntgTranspG. Below floor → Critical/High per criteria.
4. **Collective-law interplay:** contract references TV/BV → deviations to the employee's detriment violate § 4(3) TVG; § 77(6) BetrVG Nachwirkung gap on expired works agreements. Note when the TV/BV itself must be consulted (out of scope).
5. **Contradictions:** clause-vs-clause, contract-vs-floor, contract-vs-NachwG-declared terms (§ 4 S. 1 NachwG reversed burden favors employee's asserted terms). Contradiction → one finding referencing both clause IDs.

### Phase 4 — Risk scoring
1. Severity per shared criteria, verbatim from pitfalls.md, MUST NOT diverge:
   - **Critical** — void (§§ 134, 138, 307–309 BGB) or mandatory-statute violation; direct liability, term nullified, fine exposure.
   - **High** — likely AGB-invalid under settled BAG law, or significant financial/legal risk.
   - **Medium** — valid only under narrow conditions, fact-dependent, or recent/reversed law.
   - **Low** — drafting weakness/transparency gap.
2. Cross-cutting findings on the same scale; NachwG missing items default to catalog severity.
3. **Risk profile:** counts per severity, affected categories, top-3 risks by severity×dispute likelihood, `critical_findings` flag. Descriptive, never a verdict.
4. Never downgrade to improve the profile; uncertainty lowers confidence, never severity.

### Phase 5 — Report
1. Emit FOUR artifacts — JSON (schema § 3), markdown report (template § 4), self-contained HTML view, and an annotated copy of the contract pages. Same content, four views: JSON canonical; markdown source-of-truth human view; HTML is a derived rendering of the markdown and MUST be produced with `python3 tools/render_report.py <report.md> <report.html>` (severity badges, collapsible annex, print button — no manual HTML authoring, no content re-wording). The annotated PDF is derived from JSON + page scans: MUST be produced with `python3 tools/annotate_contract.py <report.json> <intake-ocr.txt> <report-annotated.pdf> <page-1.png> ... <page-N.png>` (yellow highlight over each quoted clause, colored gutter callout with F-id/severity/full recommended action; cover sheet lists findings; unplaced findings listed on the cover — never silently dropped).
2. Header MUST include: `Law as of: <law_as_of>`, contract title, jurisdiction assumption, contract type, extraction confidence, report language.
3. Confidence label on every finding: `high` (statute text or settled case law with citation), `medium` (case-law-dependent/recent/interpretation), `low` (no verified basis, `[unverified]`, or extraction-affected — reason required).
4. **Seek-counsel triggers (MUST fire, boilerplate only):** any Critical finding; any High with financial exposure; any central-term `law_in_flux`; any contract the user intends to sign with open Medium+ findings.
5. **Escalation:** "should I sign?" → findings + counsel referral, no recommendation.
6. **At a glance MUST be decision-first and plain:** verdict sentence + severity counts first; severity labels with their fixed plain definitions printed verbatim (template § 5); top risks in one plain sentence each (legal status AND practical consequence for the user, hedge carried over from `law_in_flux`/confidence), each with its F-reference. Jargon is glossed, never replaced: legal term keeps its German name and gains a one-time plain gloss (e.g. "unwirksam (rechtlich wirkungslos — bindet dich nicht)"). Everyday substitutes as the only formulation are prohibited.
7. **Action plan MUST restate the full finding set** (never a subset — findings without action appear as "keine Änderung nötig" rows), priority-ordered (critical first), every row naming: finding ID, severity, who acts (Du / Anwalt / Arbeitgeber), one plain-German sentence (contract edit or counsel trigger, never an outcome promise), uncertainty marker. When any Critical finding exists, the FIRST action row MUST be the seek-counsel trigger. Plain sections (At a glance, Action plan, consequence column) are a derived view of the annex: they restate findings with F-references and never add analysis.
8. **Plain-language claims carry uncertainty markers:** findings flagged `law_in_flux` or `confidence: medium/low` keep that marker in every plain sentence (e.g. "neues BAG-Urteil vom März 2026 — noch nicht gefestigt"; "OCR-unsicher — am Original prüfen"). Hedges (`regelmäßig`, `insoweit`, `grundsätzlich`, `dürfte`, `kann`) survive the rewrite — never upgraded to certainty, never dropped.
9. **Cross-cutting checks and the clause annex stay fully technical** (AGB mechanics, NachwG, Beweislastumkehr); the layperson view lives only in At a glance / Action plan / findings-table consequence column. Every annex finding carries a mandatory "Was zu tun ist" line. The Disclaimer section is printed verbatim and never plain-language-edited.

## 3. Tool policy
- `read` for extraction (PDF/docx/TXT/URL). OCR path for scans — mark `extraction_confidence: low`, NEVER analyze garbage; report illegible portions as such.
- `web_search` strictly budgeted (max 2 in Phase 0, max 3 in Phase 2 per contract), only for post-pin figures or explicit asks; every result cited with URL + `[web-verified <date>]`.
- `browser` not needed — `read` on URLs suffices. No LSP/bash needed; this is a knowledge + LLM skill, not code.
- No project-wide commands; no formatters/linters.

## 4. JSON output schema (draft 2020-12, verbatim)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ContractFindingsReport",
  "type": "object",
  "required": ["schema_version", "law_as_of", "contract", "risk_profile", "cross_cutting", "findings"],
  "properties": {
    "schema_version": { "const": "1.0" },
    "law_as_of": { "type": "string", "format": "date" },
    "contract": {
      "type": "object",
      "required": ["id", "title", "language", "jurisdiction_assumption", "contract_type", "is_agb", "clause_count", "extraction_confidence"],
      "properties": {
        "id": { "type": "string" },
        "title": { "type": "string" },
        "language": { "enum": ["de", "en", "mixed"] },
        "jurisdiction_assumption": { "enum": ["german", "flagged", "non-german"] },
        "contract_type": { "enum": ["standard-form", "individually-negotiated", "unknown"] },
        "is_agb": { "type": "boolean" },
        "clause_count": { "type": "integer" },
        "extraction_confidence": { "enum": ["high", "medium", "low"] }
      }
    },
    "risk_profile": {
      "type": "object",
      "required": ["counts", "top_risks", "critical_findings"],
      "properties": {
        "counts": {
          "type": "object",
          "properties": {
            "Critical": { "type": "integer" },
            "High": { "type": "integer" },
            "Medium": { "type": "integer" },
            "Low": { "type": "integer" }
          }
        },
        "top_risks": { "type": "array", "items": { "type": "string" } },
        "critical_findings": { "type": "boolean" }
      }
    },
    "cross_cutting": {
      "type": "object",
      "required": ["nachwg", "agb_whole_contract", "statutory_floor", "contradictions"],
      "properties": {
        "nachwg": {
          "type": "object",
          "properties": {
            "complete": { "type": "boolean" },
            "missing_items": { "type": "array", "items": { "type": "integer" } },
            "deadline_violations": { "type": "array", "items": { "type": "string" } }
          }
        },
        "agb_whole_contract": { "type": "string", "description": "transparency/surprising-clause/severability notes" },
        "statutory_floor": { "type": "array", "items": { "type": "string" } },
        "contradictions": { "type": "array", "items": { "type": "string" } }
      }
    },
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "clause", "category", "issue", "legal_basis", "severity", "confidence", "recommended_action", "recommended_wording"],
        "properties": {
          "id": { "type": "string", "pattern": "^F[0-9]{3}$" },
          "clause": {
            "type": "object",
            "required": ["clause_id", "clause_id_orig", "quote"],
            "properties": {
              "clause_id": { "type": "string", "pattern": "^C[0-9]{2}$" },
              "clause_id_orig": { "type": "string" },
              "quote": { "type": "string", "description": "verbatim clause text (or legible portion if extraction low)" },
              "extraction_confidence": { "enum": ["high", "medium", "low"] }
            }
          },
          "category": { "type": "string" },
          "pitfall_id": { "type": "string", "description": "catalog ID, e.g. P1; null for non-catalog findings" },
          "issue": { "type": "string" },
          "legal_basis": { "type": "array", "items": { "type": "string" }, "description": "statute sections and/or case numbers" },
          "severity": { "enum": ["Critical", "High", "Medium", "Low"] },
          "confidence": { "enum": ["high", "medium", "low"] },
          "law_in_flux": { "type": "boolean", "description": "true when the rule is under pending reform (e.g. ArbZG 2026)" },
          "recommended_action": { "type": "string" },
          "recommended_wording": { "type": ["string", "null"], "description": "clause-level fix; null when no rewording applies" },
          "sources": { "type": "array", "items": { "type": "string", "format": "uri" } }
        }
      }
    }
  }
}
```

Finding IDs `F001`…; clause IDs `C01`…; `pitfall_id` null for non-catalog findings (NachwG gaps, contradictions).

## 5. Markdown report template (verbatim structure)

```markdown
# Contract Review Report — <title>
**Law as of:** <law_as_of> · **Report language:** <lang> · **Extraction confidence:** <high|medium|low>

## At a glance
<verdict sentence, decision-first: contract type + AGB status + severity counts + seek-counsel trigger if any>
<2–4 sentences max: one plain-language consequence per top risk, each carrying its F-reference>

### Severity scale — fixed plain definitions (print verbatim, every report)
| Label | Plain meaning |
|---|---|
| Kritisch | Klausel ist unwirksam (rechtlich wirkungslos), bindet dich nicht, Handlungsbedarf vor Fristen |
| Hoch | Sehr wahrscheinlich unwirksam oder erhebliches Risiko — prüfen lassen |
| Mittel | Nur unter engen Bedingungen wirksam oder risikobehaftet |
| Niedrig | Gestaltungsschwäche / Transparenzproblem, kein akuter Handlungsbedarf |

### Top risks (one plain sentence each: ID + severity + one-line legal pointer; citations stay in annex)
1. **F00x (Severity)** — <plain: legal status + practical consequence for the user; hedge per law_in_flux/confidence; never an outcome guarantee>

## Action plan
<priority tiers, critical first; when critical_findings is true, row 1 MUST be the seek-counsel trigger>
| # | Priority | Finding | Who acts | Action (one plain-German sentence) | Uncertainty |
|---|---|---|---|---|---|
| 1 | 1 | — | Du | <counsel trigger when Critical exists: "Anwalt einschalten …"> | — |
| 2 | 1 | F00x | Du / Anwalt / Arbeitgeber | <contract edit or counsel trigger; names who acts; no outcome promises> | <marker or —> |

<Uncertainty legend (print verbatim): high confidence → "—"; medium → "mittlere Sicherheit — vor Umsetzung bestätigen lassen"; low → "niedrige Sicherheit — verifizieren"; law_in_flux → "Rechtslage in Bewegung — Reform nicht in Kraft"; extraction low → "OCR-unsicher — am Original prüfen". Rows for findings without action ("keine Änderung nötig") are included so the full finding set is restated.>

## Contract metadata
| Field | Value |
|---|---|
| Jurisdiction assumption | german / flagged / non-german |
| Contract type | standard-form / individually-negotiated / unknown |
| AGB review applied | yes / no |
| Clauses analyzed | N |

## Findings table
| ID | Clause | Category | Severity | Legal finding | What this means for you | Confidence |
<every finding F001…, unchanged severity/legal basis; consequence column is plain restatement (F-reference implied by row ID)>

## Risk profile
<counts per severity; plain lead sentence per risk; top-3 risks with F-references; critical_findings flag; legal mechanics + citations stay here>

## Cross-cutting checks
<fully technical: NachwG completeness, whole-contract AGB, statutory floors, contradictions, law_in_flux notes; no plain glosses — the layperson view lives in At a glance / Action plan>

## Clause-by-clause annex
<per clause: quote, findings, legal basis + citations, confidence; per finding a mandatory "Was zu tun ist" line (contract edit / counsel trigger / "Keine Änderung erforderlich"), then recommended wording>

## Disclaimer
<verbatim, unchanged: not legal advice; counsel referral triggers; law as-of date>
```

### 5a. HTML view (derived, never hand-written)
Generated with `python3 tools/render_report.py <report.md> <report.html>`; structure: header title + metadata line; sections mirroring the markdown (same heading order); findings table rows link to the matching `#annex-F00x` clause entries; clause annex rendered as collapsible `<details>` blocks that auto-open for printing; severity cells rendered as colored badges (Kritisch/Hoch/Mittel/Niedrig); fixed print button (top-right, `window.print()`); `@media print` CSS hides the button, opens all clause details, avoids page-breaks inside rows/clauses, prints without link underlines. The HTML is a derived view: any change to report content happens in the markdown (or the JSON), then the HTML is regenerated.
### 5b. Annotated contract PDF (derived, never hand-written)
Generated with `python3 tools/annotate_contract.py <report.json> <intake-ocr.txt> <report-annotated.pdf> <page-1.png> ... <page-N.png>`; structure: cover sheet (title, severity counts, list of findings with F-id and one-line issue, unplaced findings called out explicitly) then one page per contract page scan with each finding's quoted clause highlighted yellow and a colored gutter callout beside it (F-id, severity, full recommended action, leader line to the highlight). The annotated PDF is a derived view: any change to report content happens in the JSON (or the markdown), then all derived views are regenerated.


## 6. Guardrails
- **Not legal advice:** every report carries the disclaimer; seek-counsel triggers fire boilerplate referral only. Findings are risk/validity assessments, never guarantees of invalidity/validity or litigation outcome.
- **Jurisdiction boundary:** German law by default; non-German → conflict-of-laws note (Rome I Art. 8/9) and stop unless user confirms German review; foreign governing law + German workplace → German mandatory law still applies.
- **No fabricated case law (hard rule, Critical-class failure):** findings cite ONLY (a) statute sections, (b) case-law.md whitelist entries, or (c) web-verified citations with URL + `[web-verified <date>]`. A case number without a source is `[unverified]` at best; a case number the model cannot source MUST NOT be emitted.
- **Confidence labels:** mandatory per finding (high/medium/low); `low` requires explicit reason (unverified basis, extraction-affected, unsettled law). `law_in_flux` for pending reforms (ArbZG, Pay Transparency 2023/970, Platform Work 2024/2831, July-2026 coalition package — none is law; never apply unenacted reform).
- **Critical → counsel:** any Critical or High-with-financial-exposure finding triggers referral boilerplate.
- **OCR/extraction uncertainty:** `read` extraction; low confidence surfaced per clause and in header; garbage reported illegible, never analyzed.
- **Multilingual:** glossary-backed DE↔EN; findings reproducible in both; subtle terms (Probezeit, Befristung, Abgeltung) flagged on mistranslation risk.
- **No scope creep:** assessment only — no full-contract drafting, no TV drafting, no negotiation advice; `recommended_wording` is clause-level repair for flagged issues only.

## 7. Citation gate
Findings may cite: (a) statute sections, (b) case-law.md whitelist entries, or (c) web-verified citations with URL + `[web-verified <date>]`. Unsourced → never emitted; `[unverified]` at most, with `confidence: low`.
