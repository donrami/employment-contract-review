# Agentic Skill Architecture — German & EU Employment-Contract Assessment (omp skill)

**As of 2026-08-22.** Design deliverable for an oh-my-pi (omp) skill that ingests full employment-contract texts (Arbeitsvertrag) and produces clause-level pitfall findings under German law with EU-law overlay. Grounded in the three sibling research reports (01-german.md, 02-eu.md, 03-pitfalls.md); every legal example cited here is drawn from those verified sources and uses their citation conventions (case number + URL, `[unverified]` marker for unconfirmed claims).

---

## 1. Skill identity

**Proposed `name`:** `ger-employment-contract-review`

**Proposed `description` (frontmatter, paste-ready):**

```yaml
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
---
```

**Scope boundaries (MUST be enforced in Phase 0, restated in every report):**

- Assessment support only: identify pitfalls, cite legal basis, propose clause-level fixes. NEVER issue an opinion on the contract's overall validity as a matter of law, never predict litigation outcome.
- No full-contract drafting. Recommended wording is clause-level repair for flagged issues only.
- Single-contract focus. Multi-contract portfolios, framework agreements, or collective-agreement (Tarifvertrag) drafting are out of scope; a contract that *references* a TV/BV is in scope (see Phase 0, Phase 3).
- Jurisdiction: German employment law presumed; EU law applied where it binds via directives/CJEU case law. Non-German-governed contracts → conflict-of-laws note, then proceed only on the German-law aspects if the user confirms, else stop.
- Output language: contract language, or user preference (DE/EN), stated in the report header.

---

## 2. File structure

```
ger-law/
  SKILL.md                 # procedure, decision rules, output contract, guardrails
  references/
    statutes.md            # German statutory framework, per-statute floors (from 01-german.md)
    eu-law.md              # EU directives, CJEU case law, transposition status (from 02-eu.md)
    pitfalls.md            # master pitfall catalog: ID, name, basis, severity, fix (from 03-pitfalls.md)
    case-law.md            # verified citation index: BAG/BVerfG/CJEU, issue-tagged
    checklists.md          # per-category review checklists (operational decision trees)
    glossary.md            # DE↔EN terms, abbreviations, statute short names
```

**Split rationale — SKILL.md vs references:**

- **SKILL.md (MUST be small, ≤ ~8–10 KB of procedure):** workflow phases 0–5, decision rules, severity criteria (one-line summary, full criteria live in pitfalls.md), output schema reference, guardrails, LAW_AS_OF constant, reference-file loading map (table: phase → files to load). The model loads SKILL.md in full on activation; it must be loadable in one context pass without crowding the working context. Procedure changes (how to review) go here; *knowledge* changes (what the law says) go to references. Keeping procedure and knowledge separate means a law update never requires editing the workflow, and a workflow refinement never requires re-verifying citations.
- **references/ (lookup knowledge, loaded on demand):** each file self-pins its own as-of date in the header. Loaded per phase per the loading map below; NEVER pre-loaded wholesale (they total ~200 KB; loading all of it would dominate context).
- **Loading map (MUST follow):**

| Phase | Files loaded | Why |
|---|---|---|
| 0 Intake | glossary.md (skim) | language/jurisdiction keywords |
| 1 Normalize | — (SKILL.md only) | pure extraction, no law needed |
| 2 Clause-by-clause | checklists.md (fully), pitfalls.md (fully), case-law.md (on demand via issue tags) | detection engine |
| 3 Cross-cutting | statutes.md (fully), eu-law.md (fully), checklists.md (NachwG/AGB sections) | floors, NachwG § 2 list, transposition status |
| 4 Risk scoring | pitfalls.md (severity criteria section) | severity calibration |
| 5 Report | — (schema lives in SKILL.md) | formatting only |

- **LAW_AS_OF constant:** stored in SKILL.md frontmatter as `law_as_of: 2026-08-22`. Every report MUST print `Law as of: <law_as_of>`. On update, bump the constant AND every reference header in one pass (see § 4).

---

## 3. Workflow design

Numbered phases with inputs, decision rules, bounded web_search use, uncertainty handling, escalation. Phases 0→5 strictly sequential; a phase MUST complete (including its uncertainty/escalation exits) before the next begins.

### Phase 0 — Intake

**Inputs:** document (path/URL/paste), user ask, any user-stated jurisdiction/context.

**Decision rules:**
1. **Format:** identify source. PDF/docx → `read` extraction. Scanned image inside PDF → OCR path; set `extraction_confidence = low` for affected clauses and surface it in the report (§ 6). Paste → verbatim text, no extraction step.
2. **Language:** detect DE/EN (glossary.md keyword scan). Mixed → review both, report in contract's dominant language (or user preference).
3. **Jurisdiction:** German law presumed when: contract is in German, cites German statutes (BGB, TzBfG, ArbZG, MiLoG…), German employer address, German works-council references. Non-German signals (foreign governing-law clause, non-German employer, English-only with no German references) → conflict-of-laws note; if the user confirms German-law review, proceed with a `jurisdiction_assumption: flagged` label; else STOP and report.
4. **Contract type (MUST determine — gates AGB review):** standard form (Formulararbeitsvertrag, pre-formulated, § 305(1) BGB) vs individually negotiated (Individualvereinbarung). Individually negotiated terms escape §§ 307–309 AGB review but NOT mandatory statutory floors (§ 134 BGB) or §§ 138/242 BGB abuse control. Evidence: boilerplate layout, multi-employee form language, no hand-written amendments. Ambiguous → treat as AGB (employee-protective default, § 305c(2) BGB) and label the assumption.
5. **Collective-agreement context:** any reference to Tarifvertrag/Betriebsvereinbarung/Dienstvereinbarung (NachwG § 2(1) item 15) → note; full TV review out of scope, but § 4(3) TVG Günstigkeitsprinzip interplay is checked in Phase 3.
6. **web_search:** only if the user's ask or the contract cites a figure the references don't pin (e.g. a novel statutory amount). Max 2 queries. Otherwise none — references are authoritative.
7. **Escalation exits:** ask for legal advice/outcome prediction → refuse (guardrail, § 6), offer findings + counsel referral. Unreadable document (binary garbage, broken PDF) → report failure with the extraction error, do not guess content.

### Phase 1 — Normalize

**Inputs:** raw extracted text.

**Decision rules:**
1. Strip headers/footers/page numbers/signature blocks (keep signature date as metadata).
2. Build clause inventory: numbered clauses (`C01`, `C02`, …; original numbering preserved as `clause_id_orig`), headings, verbatim text (NEVER paraphrase inside the inventory — findings quote it).
3. Tag clause type from a fixed taxonomy: probation, duration/fixed-term, remuneration, working-time, leave, termination, post-contractual restraint (Wettbewerbsverbot), confidentiality, secondary employment, overtime, on-call work (Arbeit auf Abruf), training costs, pension, transfer/change, boilerplate (severability, choice of law), signature/miscellaneous.
4. Merge split clauses (a clause continuing over page break); split merged clauses (multiple issues in one numbered clause → multiple tagged entries, same `clause_id`).
5. **Uncertainty:** OCR-garbled text → mark clause `extraction_confidence: low`, still analyze the legible portion, flag in report. Untaggable clause → `category: other` + explicit note, not silence.

### Phase 2 — Clause-by-clause analysis

**Inputs:** clause inventory (Phase 1), checklists.md + pitfalls.md (loaded), case-law.md on demand.

**Decision rules:**
1. For each tagged clause, run the matching category checklist (checklists.md). Each checklist yields candidate pitfalls with a pitfall ID (P1…, from pitfalls.md).
2. One finding per distinct issue. Two issues in one clause → two findings, same `clause_id`. Two clauses with the same issue → two findings (clause-level granularity is required for the report annex).
3. Match clause text against the catalog's detection patterns; never force a match — absence of a catalog hit ≠ clean clause, it means "no known pitfall" (label `no_issue_found` in inventory only when the checklist completes with no triggers).
4. **web_search (bounded):** permitted ONLY when (a) a clause depends on a figure or threshold newer than the references' as-of (e.g. minimum wage after 1.1.2027, post-2026-08 BAG rulings), or (b) the user explicitly asks about a recent development. Budget: max 3 queries per contract. Every web-derived claim MUST be cited with URL and marked `[web-verified 2026-08-22]` in the finding's `sources`. Exhausted budget with no verification → confidence `low`, `[unverified]` marker, never an invented citation.
5. **Uncertainty:** no verified legal basis for a suspicion → finding with severity `Low` (drafting weakness) or drop it, but NEVER assert a legal consequence without a basis. Unsettled law (e.g. ArbZG 8h reform pending, 2026) → finding marked `law_in_flux` with both current rule and pending-change note (see § 9).
6. **Escalation:** a clause whose validity turns on facts not in the contract (e.g. whether on-call intensity is Matzak-level, C-518/15) → finding states the fact-dependence and the test, recommends counsel confirmation; do not resolve the fact yourself.

### Phase 3 — Cross-cutting checks

**Inputs:** full inventory, statutes.md + eu-law.md (loaded), checklists.md NachwG/AGB sections.

**Decision rules (each is a distinct deliverable):**
1. **NachwG completeness (§ 2(1)):** check all 15 items against the inventory; per-item deadline class (day 1: items 1, 7, 8; 7 days: 2–6, 9, 10; 1 month: 11–15). Missing item → finding `category: nachwg` (severity per pitfalls.md — missing pay documentation is High, reversed burden of proof § 4 S.1 NachwG; fine exposure €2,000 per violation). A full written contract satisfying § 2(5) NachwG counts as the Niederschrift — completeness check still runs.
2. **Whole-contract AGB review:** transparency (§ 307(1) S. 2 BGB, BAG 24.8.2017 – 8 AZR 378/16), surprising clauses (§ 305c(1), BAG 31.8.2005 – 5 AZR 545/04), ambiguity against user (§ 305c(2)), severability (§ 306) — including the note that a salvatorische Klausel cannot cure void clauses. Only for form contracts (Phase 0 decision).
3. **Statutory-floor sweep:** every monetary/leave/time term vs mandatory floors — MiLoG (€13.90 from 1.1.2026, €14.60 from 1.1.2027), ArbZG (8h/day, 11h rest), BUrlG (4 weeks minimum), EFZG, KSchG notice periods, TzBfG, EntgTranspG. Below-floor → Critical/High per criteria.
4. **Collective-law interplay:** contract references TV/BV → check that deviations from a referenced TV aren't to the employee's detriment (§ 4(3) TVG); note when the TV itself must be consulted (not in scope).
5. **Consistency/contradictions:** clause-vs-clause (e.g. probation 12 months vs termination § 622(3) 6-month window), contract-vs-statutory-floor, contract-vs-NachwG-declared terms (contract says X, § 4 S.1 NachwG reversed-burden favors the employee's asserted terms). Contradiction → one finding referencing both clause IDs.

### Phase 4 — Risk scoring

**Inputs:** findings (Phases 2–3), pitfalls.md severity criteria section.

**Decision rules:**
1. Severity per finding uses the shared criteria verbatim (from pitfalls.md; MUST NOT diverge):
   - **Critical** — void (§§ 134, 138, 307–309 BGB) or mandatory-statute violation; direct liability, term nullified (fixed term → indefinite), or fine exposure.
   - **High** — likely AGB-invalid under settled BAG case law, or significant financial/legal risk.
   - **Medium** — valid only under narrow conditions, fact-dependent, or rests on recent/reversed case law.
   - **Low** — drafting weakness/transparency gap, no immediate nullity.
2. Cross-cutting findings (NachwG gaps, contradictions) use the same scale; NachwG missing-item findings default to the catalog severity.
3. **Overall risk profile:** counts per severity, affected categories, top-3 risks by severity×likelihood of dispute, `critical_findings: bool`. Profile is descriptive, not a verdict.
4. No finding downgrading to make the profile look better; uncertainty moves confidence down, never severity.

### Phase 5 — Report

**Inputs:** inventory, findings, risk profile.

**Decision rules:**
1. Emit BOTH artifacts: JSON (schema § 5) and markdown report (template § 5). Same content, two views.
2. Header MUST include: `Law as of: <law_as_of>`; `Contract: <title>`, jurisdiction assumption, contract type (AGB/individual), extraction confidence, report language.
3. Confidence labels on every finding: `high` (basis in statute text or settled case law with citation), `medium` (case-law-dependent, recent, or interpretation), `low` (no verified basis, `[unverified]`, or extraction-affected).
4. **Seek-counsel triggers (MUST fire):** any Critical finding; any High with financial exposure (back-pay, restitution, restraint-of-trade unenforceability); any `law_in_flux` finding on a central term; any contract the user intends to sign with open Medium+ findings. Trigger text is boilerplate, not advice.
5. **Escalation:** user asks "should I sign?" → findings + counsel referral, no recommendation.

---

## 4. Knowledge-base content plan

**Per-file content (sources: sibling reports; each file self-pins as-of):**

| File | Content | Update cadence |
|---|---|---|
| `statutes.md` | Norm hierarchy (§ 611a, §§ 305–310 BGB, § 134/§ 138, § 622/623/626 BGB); NachwG § 2(1) 15-item list + deadline classes + § 4/§ 5 sanctions; MiLoG rates; ArbZG caps; BUrlG; EFZG; TzBfG (§§ 4, 7, 9, 12, 14, 15); KSchG; EntgTranspG; AEntG § 23c. Every floor with section number + gesetze-im-internet.de URL. | Annual figures 1 Jan/1 Jul (MiLoG, Pfändungsfreigrenzen); statutory amendments as enacted |
| `eu-law.md` | Directive → German-transposition mapping (2003/88→ArbZG; 97/81, 99/70→TzBfG; 2019/1152→NachwG 2022; 96/71→AEntG); CJEU doctrine (CCOO C-55/18 time recording, Matzak C-518/15, Grupo Norte C-574/16, Adeneler C-212/04, C-19/23 partial annulment of Minimum Wage Directive); transposition-status flags (Pay Transparency 2023/970 — deadline missed 7.6.2026, direct effect from 8.6.2026; Platform Work 2024/2831 — deadline 2.12.2026). | On transposition events; quarterly freshness check |
| `pitfalls.md` | Master catalog: pitfall ID (P1…), name (DE+EN), category, clause type, why-it's-a-problem with legal basis, severity, typical clause language, recommended fix wording, uncertainty note. Categories: probation, fixed-term, remuneration, working time, leave, termination, restraint of trade, confidentiality/secondary employment, overtime/on-call, training costs, boilerplate. | Append-only; new entries on BAG rulings; regression cases from evaluation (§ 7) |
| `case-law.md` | Citation index: case number → issue tags → one-line holding → source URL. Whitelist for findings — a finding MUST cite from here or mark `[unverified]`. | On BAG/BVerfG/CJEU press releases; purged of superseded holdings |
| `checklists.md` | Per-category decision trees: for each clause type, ordered checks with pitfall-ID outcomes (e.g. probation: length > 6 months? → P1; fixed-term with probation but no termination right? → P2; § 15(4) TzBfG). Also NachwG item checklist and AGB whole-contract checklist (Phase 3). | Coupled to pitfalls.md changes |
| `glossary.md` | DE↔EN terms (Arbeitsvertrag, Probezeit, Befristung, Vergütung, Arbeitszeit, Kündigung, Wettbewerbsverbot, Betriebsvereinbarung…), statute abbreviations (BGB, TzBfG, ArbZG, MiLoG, NachwG, KSchG, EFZG, BUrlG, BetrVG, TVG), EU directive numbers. | Rare; on new abbreviations |

**LAW_AS_OF pinning:** single constant in SKILL.md frontmatter (`law_as_of: 2026-08-22`). Update procedure (MUST be one pass): bump constant → update each reference header → run the smoke test (§ 7) to confirm no citation broke → commit. Every report and every finding carries the constant; findings never silently mix law versions.

**Cross-file consistency rules:**
- One fact, one home. Severity criteria live ONLY in pitfalls.md; statutes floors ONLY in statutes.md; citation whitelist ONLY in case-law.md. Other files reference by ID (`see P1`, `see case-law: BAG 2 AZR 160/24`), never duplicate the fact.
- Pitfall IDs are stable; renumbering forbidden once published in a report — append new IDs.
- On any reference edit: grep the other files for stale IDs/figures; a stale figure is a Critical-class defect in the knowledge base.

---

## 5. Output schema

**JSON findings schema (draft 2020-12):**

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

**Markdown report template:**

```markdown
# Contract Review Report — <title>
**Law as of:** <law_as_of> · **Report language:** <lang> · **Extraction confidence:** <high|medium|low>

## Executive summary
<2–5 sentences: contract type, AGB status, severity counts, top risks, seek-counsel trigger if any>

## Contract metadata
| Field | Value |
|---|---|
| Jurisdiction assumption | german / flagged / non-german |
| Contract type | standard-form / individually-negotiated / unknown |
| AGB review applied | yes / no |
| Clauses analyzed | N |

## Findings table
| ID | Clause | Severity | Issue | Legal basis | Confidence |

## Risk profile
<counts per severity; top-3 risks; critical_findings flag>

## Cross-cutting checks
- NachwG § 2(1): <complete / missing items …>
- Whole-contract AGB: <notes>
- Statutory floors: <checks>
- Contradictions: <list>

## Clause-by-clause annex
<per clause: quote, findings, recommended wording>

## Disclaimer
<not legal advice; counsel referral triggers; law as-of date>
```

**Example finding entry (JSON + table row), drawn from pitfalls.md P1:**

```json
{
  "id": "F001",
  "clause": {
    "clause_id": "C03",
    "clause_id_orig": "§ 3",
    "quote": "Die ersten zwölf Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden."
  },
  "category": "probation",
  "pitfall_id": "P1",
  "issue": "Probation beyond six months: the two-week notice window of § 622(3) BGB is limited to 'längstens sechs Monate'; a longer formular probation is AGB-invalid under § 307 BGB and the statutory notice periods of § 622(1)–(2) BGB apply instead.",
  "legal_basis": ["§ 622 Abs. 3 BGB", "§ 307 BGB", "BAG 30.10.2025 – 2 AZR 160/24"],
  "severity": "High",
  "confidence": "high",
  "law_in_flux": false,
  "recommended_action": "Reduce probation to six months for an indefinite contract; for fixed-term contracts calibrate probation to the term per BAG 2 AZR 160/24 (case-by-case proportionality, no fixed 25% rule).",
  "recommended_wording": "Die ersten sechs Monate des Arbeitsverhältnisses gelten als Probezeit. Während der Probezeit kann das Arbeitsverhältnis mit einer Frist von zwei Wochen gekündigt werden.",
  "sources": ["https://www.bundesarbeitsgericht.de/presse/probezeitkuendigung-im-befristeten-arbeitsverhaeltnis/", "https://www.gesetze-im-internet.de/bgb/__622.html"]
}
```

| F001 | C03 (§ 3) | High | Probation 12 months — § 622(3) BGB caps the 2-week notice window at 6 months | § 622(3) BGB; § 307 BGB; BAG 2 AZR 160/24 | high |

---

## 6. Guardrails

- **Not legal advice:** every report MUST carry the disclaimer; every seek-counsel trigger fires boilerplate referral. NEVER phrase findings as guarantees of invalidity/validity in litigation.
- **Jurisdiction boundary:** German law only by default. Non-German contract → conflict-of-laws note (Rome I Reg. (EC) 593/2008 relevance: Art. 8 mandatory provisions apply regardless of chosen law) and stop unless user confirms German-law review. Foreign governing-law clause + German workplace → note that German mandatory law still applies to the employment relationship.
- **No fabricated case law (hard rule):** findings cite ONLY (a) statute sections, (b) entries from case-law.md whitelist, or (c) web-verified citations with URL + `[web-verified <date>]`. A case number without a source is `[unverified]` at best; a case number the model cannot source MUST NOT be emitted. This is a Critical-class failure if violated.
- **Confidence labels:** mandatory per finding (high/medium/low); `low` requires an explicit reason (unverified basis, extraction-affected, unsettled law). `law_in_flux` flag for pending reforms (ArbZG 8h→weekly cap, Pay Transparency transposition, Platform Work directive).
- **Critical → counsel:** any Critical finding (or High with financial exposure) triggers the counsel-referral boilerplate in the report.
- **Scanned/OCR contracts:** `read` the PDF; extraction uncertainty MUST be surfaced — `extraction_confidence: low` per affected clause and in the report header. Do not analyze garbage; report what was illegible.
- **Output language:** contract language or user preference; glossary.md backs the DE/EN mapping so findings are reproducible in both.
- **No scope creep:** assessment only — no full-contract drafting, no TV drafting, no negotiation advice (§ 1).

---

## 7. Evaluation plan

**Golden test corpus (target N = 20 contracts):**
- 15 seeded-bad contracts: each contains 2–4 known pitfalls from distinct categories, drawn from BAG decisions and textbook examples already in pitfalls.md (probation P1/P2, fixed-term § 14(2) TzBfG violations, missing NachwG items, below-floor pay, invalid restraint of trade, absolute secondary-employment ban, 12-month probation, § 15(4) TzBfG trap, etc.). Ground truth = pitfall IDs + clause IDs, annotated by a reviewer per contract.
- 5 clean contracts: no known pitfalls, used for false-positive measurement. Include one borderline (individually-negotiated terms, near-floor values) to test severity calibration.

**Metrics (per run, per pitfall category and overall):**
- Precision = correct findings / total findings (a finding is correct when its pitfall_id matches ground truth AND clause_id matches).
- Recall = detected seeded pitfalls / seeded pitfalls.
- F1. Plus: false-Critical rate (findings rated Critical that ground truth rates ≤ High), missed-Critical rate (must be 0).
- Category-level breakdown: probation, fixed-term, remuneration, working time, NachwG completeness, AGB/termination, restraint of trade.

**Smoke-test procedure (MUST run on every knowledge-base update, § 4):**
1. Run skill on one known-bad contract → expect ≥ 1 Critical or High finding, pitfall IDs present, no invented citations.
2. Run on one clean contract → expect zero Critical/High findings; at most Low drafting notes.
3. Both must produce schema-valid JSON (§ 5). Failure = update blocked.

**Iteration loop:** every missed seeded pitfall becomes a regression case appended to the corpus; catalog entries that over-trigger (false positives) get tightened detection patterns in checklists.md. Re-run metrics after each change; record precision/recall deltas in the knowledge-base changelog.

---

## 8. Build order

1. **SKILL.md skeleton + frontmatter + output schema (day 1, low effort, low risk).** Defines the contract: phases, loading map, LAW_AS_OF, JSON schema. Everything else hangs off it. Do NOT detail Phase 2 fully yet — checklists depend on the catalog.
2. **pitfalls.md catalog (highest value, medium effort, low risk).** Source: 03-pitfalls.md; assign stable IDs, normalize severity and fix wording. Drives detection quality; everything downstream consumes it. The report (04-arch) already pins the format; convert, don't redesign.
3. **statutes.md + eu-law.md + case-law.md (medium effort, low risk).** Port from 01-german.md/02-eu.md; strip narrative to lookup form; build the citation whitelist. Case-law.md is the hallucination firewall — build it before any Phase 2 checklist that cites case law.
4. **checklists.md (medium effort, medium risk).** Operational decision trees per category; risk: over- or under-triggering — calibrate against the corpus in step 5.
5. **Evaluation corpus + smoke test (medium effort).** 20 contracts, annotation, metric harness. Without this, steps 2–4 are unverified claims.
6. **Workflow detail hardening (ongoing).** Refine Phase 2–4 decision rules from evaluation failures.

Risk notes: steps 1–3 are safe to parallelize (three port files from three reports); step 4 depends on 2–3; step 5 gates any claim of quality. The single biggest risk is case-law hallucination — hence case-law.md whitelist lands before checklist detail.

---

## 9. Open questions & risks

- **Hallucination of case law (Critical risk).** Mitigated by the case-law.md whitelist + `[unverified]` convention + web-verified citation rule (§ 6). Residual risk: model invents a *plausible* case number. Hard rule: no source → no citation, regardless of confidence. Decide whether findings MAY cite a case the model knows but that is absent from the whitelist — recommended: yes, but only with URL and `[web-verified]`.
- **Law drift 2026 (High risk, real today):** Pay Transparency Directive (EU) 2023/970 — transposition deadline 7.6.2026 missed; direct effect from 8.6.2026 (public employers) and conforming-interpretation duties (private). ArbZG reform — 8h daily cap → weekly cap announced June 2026, not enacted; skill MUST flag `law_in_flux` on working-time findings rather than assert the 8h cap will change. Platform Work Directive 2024/2831 — deadline 2.12.2026, no draft published. Minimum Wage Directive partially annulled (CJEU C-19/23, 11.11.2025) — MiLoG unaffected. The July 2026 coalition package (fixed-term relaxation to 48 months, KSchG high-earner changes) is not enacted — MUST NOT be applied; MAY be noted as `law_in_flux`.
- **Contract variants:** works agreements (Betriebsvereinbarung) and TV references — skill can flag the interplay (§ 4(3) TVG, NachwG item 15) but cannot review documents not provided. Open question: accept an accompanying TV/BV PDF as optional input? Recommended: yes, Phase 0 accepts it as auxiliary context, still out of scope for full review.
- **PDF extraction quality:** scanned contracts → OCR errors → missed pitfalls. Mitigation: `extraction_confidence` surfacing, never analyzing garbage, user asked to supply text when OCR fails badly. Open question: benchmark the harness `read` PDF path on 3 scanned samples during corpus build.
- **Multilingual contracts:** mixed DE/EN clauses, EN-only contracts with German references. Mitigation: glossary, dual-language findings, jurisdiction flag. Risk: subtle German terms (Probezeit, Befristung) mistranslated in review.
- **Scope creep (drafting vs assessment):** the `recommended_wording` field edges toward drafting. Guard: clause-level fix only, only for flagged issues, never a full contract; monitor evaluation for mission creep.
- **Severity subjectivity:** Medium/Low boundary is judgment-heavy. Mitigation: shared criteria verbatim from pitfalls.md, calibration against the corpus, false-Critical rate tracked as a metric.

---

*Report produced 2026-08-22. Consistent with 01-german.md, 02-eu.md, 03-pitfalls.md (same as-of date, same citation conventions, same severity scale).*
