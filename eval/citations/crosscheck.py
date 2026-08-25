#!/usr/bin/env python3
"""Cross-check sebischair rule citations against the ger-law case-law whitelist.

Dataset: github.com/sebischair/Employment-Contract-Clauses-German (CC BY-NC 4.0).
License-clean: fetched at runtime, never vendored. We only compare citation
strings — no clauses, rules, or explanations are copied into this repo.

Both directions are reported:
  * dataset-side: each sebischair rule reference that matches a whitelist entry
  * whitelist-side: each whitelist case that appears in the dataset references
  * gap analysis: which cases each side has that the other lacks

Matching normalizes citation strings to a canonical form before comparison
(case number + court + date), so spelling/punctuation drift does not hide a
real overlap.

Usage:
    python3 crosscheck.py [--rules URL|PATH] [--whitelist PATH] [--json]

Outputs human-readable tables; with --json, a JSON object instead.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

RULES_URL = (
    "https://raw.githubusercontent.com/sebischair/"
    "Employment-Contract-Clauses-German/main/v3_2026-01/data/rules.json"
)
DEFAULT_WHITELIST = Path(__file__).resolve().parents[2] / "references" / "case-law.md"

# Court names as they appear in the dataset references.
COURT_ALIASES = {
    "BAG": "BAG",
    "BGH": "BGH",
    "EuGH": "CJEU",
    "LAG": "LAG",
    "OLG": "OLG",
    "BMF": "BMF",  # not a court — kept for completeness, never matches whitelist
}
_ECJ_NAMES = {"EuGH", "CJEU", "ECJ", "eugh"}

# Case-number regex: senate/division prefix, number, slash, year. Handles
# "8 AZR 897/08", "C-684/16", "VIII ZR 232/75", "13/12 Sa 1479/02".
_CASE_RE = re.compile(
    r"(?P<num>(?:[A-Z]-\s*)?\d{1,3}(?:/\d{2,4})?\s+[A-Za-z]+\s+\d+/\d{2,4}"
    r"|C-\d+/\d{2,4}"
    r"|[IVX]+(?:\s+[A-Za-z]+)+\s+\d+/\d{2,4}"
    r"|\d{1,3}(?:/\d{1,3})?\s+[A-Za-z]+\s+\d+/\d{2,4})",
    re.IGNORECASE,
)
# Full decision date, e.g. "01.09.2010" or "22.3.2017" in a court reference.
_DATE_RE = re.compile(r"\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b")
# Court refs in the dataset always carry a decision date ("BAG, Urteil vom ...").
_COURT_REF_RE = re.compile(r"^(BAG|BGH|EuGH|LAG|OLG),", re.IGNORECASE)


def fetch_json(url: str) -> list[dict]:
    """Fetch a JSON array from a URL."""
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def load_whitelist(path: Path) -> list[dict]:
    """Parse case-law.md into rows: court, case number, date (if present)."""
    rows = []
    court = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("|---") or line.startswith("| Case"):
            continue
        if line.startswith("## "):
            court = line[3:].strip().split(" ")[0]  # "BAG — ..." -> "BAG"
            continue
        if line.startswith("| ") and "|" in line[1:]:
            cells = [c.strip() for c in line[1:].split("|")]
            # Table rows: case no. | date | tags | holding | url
            if len(cells) >= 5 and cells[0] and cells[1]:
                rows.append(
                    {
                        "court": court or "",
                        "case": cells[0],
                        "date": cells[1],
                    }
                )
    return rows


def norm_case(raw: str) -> str:
    """Canonicalize a case number: uppercase, collapse spaces, strip trailing
    parentheticals (senate qualifiers like "(A)"/"(B)" and CJEU case names
    like "(Max-Planck)")."""
    s = raw.strip().upper()
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace("–", "-").replace("—", "-")
    return s


def norm_date(raw: str) -> str:
    """Canonicalize a decision date: d.m.yyyy and dd.mm.yyyy become dd.mm.yyyy."""
    m = _DATE_RE.search(raw or "")
    if not m:
        return ""
    d, mo, y = m.groups()
    return f"{int(d):02d}.{int(mo):02d}.{y}"


def parse_court_ref(ref: str) -> dict | None:
    """Extract {court, case, date} from a dataset reference string.

    Returns None for statute/directive/letter references (no court decision).
    """
    m = _COURT_REF_RE.match(ref)
    if not m:
        return None
    court = m.group(1).upper()
    cm = _CASE_RE.search(ref)
    if not cm:
        return None
    dm = _DATE_RE.search(ref)
    return {
        "court": COURT_ALIASES.get(court, court),
        "case": norm_case(cm.group("num")),
        "date": dm.group(0) if dm else "",
    }


def whitelist_cases(rows: list[dict]) -> dict[str, dict]:
    """Map normalized case number -> whitelist row."""
    out = {}
    for row in rows:
        key = norm_case(row["case"])
        out.setdefault(key, row)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rules", default=RULES_URL, help="rules.json URL or local path")
    ap.add_argument("--whitelist", type=Path, default=DEFAULT_WHITELIST, help="case-law.md path")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of tables")
    args = ap.parse_args()

    rules_src = args.rules
    if rules_src.startswith(("http://", "https://")):
        rules = fetch_json(rules_src)
    else:
        rules = json.loads(Path(rules_src).read_text(encoding="utf-8"))

    wl_rows = load_whitelist(args.whitelist)
    wl = whitelist_cases(wl_rows)

    # ---- dataset side: parse references into court decisions ----
    parsed = []  # (rule_title, ref, court, case, date)
    for rule in rules:
        title = rule.get("title", "")
        for ref in rule.get("references", []):
            info = parse_court_ref(ref)
            if info:
                parsed.append((title, ref, info["court"], info["case"], info["date"]))

    # ---- overlap: dataset refs that are whitelisted ----
    hits = []  # (rule_title, ref, case, dataset_date, wl_date, wl_court, mismatch)
    for title, ref, court, case, date in parsed:
        if case in wl:
            wl_date = wl[case]["date"]
            mismatch = bool(wl_date) and bool(date) and norm_date(wl_date) != norm_date(date)
            hits.append((title, ref, case, date, wl_date, wl[case]["court"], mismatch))
    hit_cases = {h[2] for h in hits}

    # ---- dataset-side: refs not in whitelist ----
    missing = [p for p in parsed if p[3] not in wl]

    # ---- whitelist-side: whitelisted cases absent from dataset ----
    dataset_cases = {p[3] for p in parsed}
    wl_only = [k for k in sorted(wl) if k not in dataset_cases]

    # ---- stats ----
    n_wl = len(wl)
    n_dataset = len(parsed)
    n_dataset_unique = len(dataset_cases)
    n_hits = len(hits)
    n_hit_unique = len(hit_cases)

    if args.json:
        print(
            json.dumps(
                {
                    "dataset": {
                        "source": rules_src,
                        "rules": len(rules),
                        "court_references": n_dataset,
                        "unique_cases": n_dataset_unique,
                    },
                    "whitelist": {"entries": n_wl},
                    "overlap": {
                        "matching_references": n_hits,
                        "unique_matching_cases": n_hit_unique,
                        "hits": [
                            {
                                "rule": t,
                                "reference": r,
                                "case": c,
                                "dataset_date": dd,
                                "whitelist_date": wd,
                                "whitelist_court": wc,
                                "date_mismatch": mm,
                            }
                            for t, r, c, dd, wd, wc, mm in hits
                        ],
                    },
                    "dataset_only": [
                        {"rule": t, "reference": r, "case": c, "court": crt, "date": d}
                        for t, r, crt, c, d in missing
                    ],
                    "whitelist_only": wl_only,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0

    print(f"Dataset: {len(rules)} rules, {n_dataset} court references "
          f"({n_dataset_unique} unique cases)")
    print(f"Whitelist: {n_wl} case entries")
    print(f"Overlap: {n_hits} references match whitelist "
          f"({n_hit_unique} unique cases)\n")

    print("== Dataset references matching the whitelist ==")
    if not hits:
        print("  (none)")
    for t, r, c, dd, wd, wc, mm in sorted(hits, key=lambda h: h[2]):
        flag = "  **DATE MISMATCH**" if mm else ""
        print(f"  {c}  [{wc}]  dataset {dd} vs whitelist {wd}{flag}")
        print(f"      rule: {t}")
        print(f"      ref : {r}")

    print("\n== Dataset court references NOT in whitelist ==")
    for t, r, c, d, court in sorted(missing, key=lambda p: p[3]):
        print(f"  {c}  ({court} {d})")
        print(f"      rule: {t}")
        print(f"      ref : {r}")

    print("\n== Whitelist cases NOT referenced by dataset ==")
    print(f"  ({len(wl_only)} cases)")
    for c in wl_only:
        print(f"  {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
