#!/usr/bin/env python3
"""Knowledge-base coverage eval against the sebischair rules dataset.

Dataset: github.com/sebischair/Employment-Contract-Clauses-German (CC BY-NC 4.0).
License-clean: rules.json + topics.json are fetched at runtime, never vendored.
Committed results carry only `_id` hashes and German topic labels — no rule
titles, rule text, clause content, or explanations ever land in this repo.

What it checks (deterministic, no LLM in the loop):
  * topic-map freshness : eval/topic-map.json must cover the fetched topic set
                          exactly (ids + labels) and pin the same dataset version
  * mapped              : sampled rule's topic has a non-"none" mapping
  * pitfalls-exist      : every mapped pitfalls section really exists as a
                          "## N. Name" heading in references/pitfalls.md
  * category-exists     : every skill_clause_type appears in SKILL.md's Phase-1
                          fixed clause-type taxonomy line
  * broken_refs         : rules whose `references` field is absent, empty, or
                          not a list of strings

Usage:
    python3 knowledge_eval.py [--smoke | --sample N] [--json PATH]

Exit status is 0 even when individual checks fail (failures are reported in
the aggregate); nonzero only on fetch, parse, or topic-map staleness errors.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

RULES_URL = (
    "https://raw.githubusercontent.com/sebischair/"
    "Employment-Contract-Clauses-German/main/v3_2026-01/data/rules.json"
)
TOPICS_URL = (
    "https://raw.githubusercontent.com/sebischair/"
    "Employment-Contract-Clauses-German/main/v3_2026-01/data/topics.json"
)
DATASET_VERSION = "v3_2026-01"

EVAL_DIR = Path(__file__).resolve().parent
REPO_ROOT = EVAL_DIR.parent
TOPIC_MAP_PATH = EVAL_DIR / "topic-map.json"
PITFALLS_PATH = REPO_ROOT / "references" / "pitfalls.md"
SKILL_PATH = REPO_ROOT / "SKILL.md"
CACHE_DIR = EVAL_DIR / "cache"
RESULTS_DIR = EVAL_DIR / "results"


class EvalError(Exception):
    """Fatal fetch/parse/staleness error."""


def fetch_json(url: str) -> list | dict:
    """Fetch a JSON document from a URL (mirrors citations/crosscheck.py)."""
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def rid(rule_id: str) -> str:
    """Anonymized rule identity: sha256 of the dataset `_id`, first 16 hex."""
    return hashlib.sha256(rule_id.encode("utf-8")).hexdigest()[:16]


def load_topic_map() -> dict:
    if not TOPIC_MAP_PATH.is_file():
        raise EvalError(f"topic map missing: {TOPIC_MAP_PATH}")
    try:
        return json.loads(TOPIC_MAP_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise EvalError(f"topic map is not valid JSON: {exc}") from exc


def check_topic_map_freshness(topic_map: dict, topics: list[dict]) -> None:
    """Hard-fail unless the map covers the fetched topic set exactly."""
    ds = topic_map.get("dataset", {})
    if ds.get("version") != DATASET_VERSION:
        raise EvalError(
            f"stale topic map: pinned version {ds.get('version')!r} "
            f"!= fetched {DATASET_VERSION!r}"
        )
    upstream = {t["_id"]: t["title"] for t in topics}
    mapped = {t["topic_id"]: t["topic"] for t in topic_map.get("topics", [])}
    missing = sorted(set(upstream) - set(mapped))
    extra = sorted(set(mapped) - set(upstream))
    relabeled = sorted(
        k for k in set(upstream) & set(mapped) if upstream[k] != mapped[k]
    )
    problems = []
    if missing:
        problems.append(f"topics missing from map: {[upstream[k] for k in missing]}")
    if extra:
        problems.append(f"map entries without upstream topic: {extra}")
    if relabeled:
        problems.append(
            f"relabels vs upstream: {[(mapped[k], upstream[k]) for k in relabeled]}"
        )
    if problems:
        raise EvalError("stale topic map — update eval/topic-map.json: " + "; ".join(problems))


def parse_pitfalls_sections(path: Path) -> dict[int, str]:
    """Extract numbered `## N. Name` section headings from pitfalls.md."""
    sections: dict[int, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (\d+)\.\s+(.+?)\s*$", line)
        if m:
            sections[int(m.group(1))] = m.group(2)
    return sections


def parse_skill_taxonomy(path: Path) -> set[str]:
    """Extract the Phase-1 fixed clause-type list from SKILL.md."""
    text = path.read_text(encoding="utf-8")
    m = re.search(
        r"^3\.\s+Tag clause type from fixed taxonomy:\s*(.+)$", text, re.MULTILINE
    )
    if not m:
        raise EvalError("could not find the Phase-1 clause-type taxonomy line in SKILL.md")
    raw = m.group(1).rstrip(".").strip()
    types = {t.strip() for t in raw.split(",")}
    if len(types) < 10:  # sanity: the taxonomy has 16 members today
        raise EvalError(f"suspiciously small taxonomy parsed from SKILL.md: {sorted(types)}")
    return types


def stratified_sample(rules: list[dict], topics_by_id: dict[str, str],
                      per_topic: int = 1) -> list[dict]:
    """Deterministic stratified sample: per-topic first-k by `_id`,
    topic groups ordered by German label."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rules:
        groups[r.get("topic", "")].append(r)
    picked: list[dict] = []
    for topic_id in sorted(groups, key=lambda tid: topics_by_id.get(tid, "")):
        picked.extend(sorted(groups[topic_id], key=lambda r: r["_id"])[:per_topic])
    return picked


def evaluate_rule(rule: dict, by_topic_id: dict[str, dict],
                  pitfalls_sections: dict[int, str], taxonomy: set[str]) -> dict:
    """Run all deterministic checks for one rule. Returns a check record."""
    entry = by_topic_id.get(rule.get("topic"))
    checks = {"mapped": False, "pitfalls_exist": None, "category_exists": None}
    if entry is not None and entry.get("mapping") != "none":
        checks["mapped"] = True
        sec = entry.get("pitfalls_section")
        if sec is not None:
            checks["pitfalls_exist"] = (
                pitfalls_sections.get(sec["number"]) == sec["name"]
            )
        else:
            checks["pitfalls_exist"] = True  # partial mappings may omit a section
        wanted = entry.get("skill_clause_types") or []
        checks["category_exists"] = all(t in taxonomy for t in wanted)

    refs = rule.get("references")
    refs_ok = isinstance(refs, list) and bool(refs) and all(isinstance(x, str) for x in refs)
    return {"checks": checks, "refs_ok": refs_ok}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--smoke", action="store_true",
                      help="1 rule per mapped topic instead of the full set")
    mode.add_argument("--sample", type=int, metavar="N", default=None,
                      help="stratified sample of N rules instead of the full set")
    ap.add_argument("--json", metavar="PATH", default=None,
                    help="also write the aggregate JSON here "
                           "(default: eval/results/knowledge-eval-<mode>.json)")
    args = ap.parse_args()

    try:
        rules = fetch_json(RULES_URL)
        topics = fetch_json(TOPICS_URL)
    except Exception as exc:  # noqa: BLE001 — any network failure is fatal
        print(f"error: dataset fetch failed: {exc}", file=sys.stderr)
        return 2

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    (CACHE_DIR / "rules.json").write_text(json.dumps(rules, ensure_ascii=False), encoding="utf-8")
    (CACHE_DIR / "topics.json").write_text(json.dumps(topics, ensure_ascii=False), encoding="utf-8")

    try:
        topic_map = load_topic_map()
        check_topic_map_freshness(topic_map, topics)
        pitfalls_sections = parse_pitfalls_sections(PITFALLS_PATH)
        taxonomy = parse_skill_taxonomy(SKILL_PATH)
    except EvalError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    topics_by_id = {t["_id"]: t["title"] for t in topics}

    if args.smoke:
        sample = stratified_sample(rules, topics_by_id, per_topic=1)
        mode_name = "smoke"
    elif args.sample is not None:
        if not 0 < args.sample <= len(rules):
            print(f"error: --sample must be in 1..{len(rules)}", file=sys.stderr)
            return 2
        sample = stratified_sample(rules, topics_by_id,
                                   per_topic=-(-args.sample // len(topics)))[: args.sample]
        mode_name = f"sample-{args.sample}"
    else:
        sample = sorted(rules, key=lambda r: r["_id"])
        mode_name = "full"

    by_topic_id = {t["topic_id"]: t for t in topic_map["topics"]}
    per_topic: dict[str, dict] = {}
    broken_refs: list[str] = []
    unmapped_rule_ids: list[str] = []

    for rule in sample:
        label = topics_by_id.get(rule.get("topic"), "<unknown>")
        bucket = per_topic.setdefault(
            label,
            {
                "rules_in_dataset": sum(1 for r in rules if r.get("topic") == rule.get("topic")),
                "rules_sampled": 0,
                "checks_passed": 0,
                "mapping": by_topic_id.get(rule.get("topic"), {}).get("mapping", "<unknown>"),
            },
        )
        bucket["rules_sampled"] += 1
        result = evaluate_rule(rule, by_topic_id, pitfalls_sections, taxonomy)
        ok = result["checks"]["mapped"]
        if result["checks"]["pitfalls_exist"] is False:
            ok = False
        if result["checks"]["category_exists"] is False:
            ok = False
        if ok:
            bucket["checks_passed"] += 1
        else:
            unmapped_rule_ids.append(rid(rule["_id"]))
        if not result["refs_ok"]:
            broken_refs.append(rid(rule["_id"]))

    evaluated = len(sample)
    mapped_count = evaluated - len(unmapped_rule_ids)
    aggregate = {
        "tool": "eval/knowledge_eval.py",
        "mode": mode_name,
        "dataset_version": DATASET_VERSION,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "license": "CC BY-NC 4.0 — fetched at runtime; identifiers below are sha256(_id)[:16]",
        "rules_total": len(rules),
        "rules_evaluated": evaluated,
        "map_rate": round(mapped_count / evaluated, 4) if evaluated else None,
        "per_topic": dict(sorted(per_topic.items())),
        "broken_refs": sorted(broken_refs),
        "broken_ref_count": len(broken_refs),
        "unmapped_rule_ids": sorted(unmapped_rule_ids),
        "taxonomy_size": len(taxonomy),
        "pitfalls_sections_found": len(pitfalls_sections),
    }

    out_path = Path(args.json) if args.json else RESULTS_DIR / f"knowledge-eval-{mode_name}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(aggregate, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")

    print(f"knowledge eval — mode={mode_name} dataset={DATASET_VERSION}")
    print(f"  rules total {aggregate['rules_total']}, evaluated {evaluated}")
    print(f"  map_rate {aggregate['map_rate']}")
    print(f"  broken_refs {aggregate['broken_ref_count']}")
    print(f"  per-topic:")
    for label, b in aggregate["per_topic"].items():
        print(f"    {label}: mapping={b['mapping']} "
              f"{b['checks_passed']}/{b['rules_sampled']} passed "
              f"(dataset total {b['rules_in_dataset']})")
    print(f"  results written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
