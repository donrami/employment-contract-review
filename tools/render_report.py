#!/usr/bin/env python3
"""Render the skill's markdown contract-review report to a self-contained HTML view.

Derived view: reads the markdown report (which is itself derived from the canonical
report.json) and produces one HTML file with print CSS and a print button. No content
is re-authored here, so the HTML cannot drift from the markdown.

Usage:
    python3 tools/render_report.py <input.md> <output.html>
"""

import html
import re
import sys

SEVERITY = {"Kritisch": "critical", "Hoch": "high", "Mittel": "medium", "Niedrig": "low"}

CSS = """
:root {
  --critical: #b3261e; --high: #d95f00; --medium: #9a6b00; --low: #2e7d32;
  --ink: #1c1c1e; --muted: #6b6b70; --line: #e2e2e6; --bg: #ffffff; --soft: #f6f6f8;
}
* { box-sizing: border-box; }
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: var(--ink); background: var(--bg); margin: 0; line-height: 1.55; font-size: 15px;
}
.wrap { max-width: 920px; margin: 0 auto; padding: 40px 28px 80px; }
h1 { font-size: 1.6em; margin: 0 0 4px; line-height: 1.25; }
h2 {
  font-size: 1.15em; margin: 34px 0 10px; padding-top: 14px; border-top: 2px solid var(--line);
}
h2:first-of-type { border-top: 0; padding-top: 0; }
h3 { font-size: 1.02em; margin: 20px 0 6px; }
p { margin: 8px 0; }
.meta { color: var(--muted); font-size: 0.92em; margin: 6px 0 0; }
strong { font-weight: 650; }
code { background: var(--soft); border: 1px solid var(--line); border-radius: 4px;
  padding: 0 4px; font-size: 0.9em; }
a { color: #0b57d0; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 0.93em; }
th, td { border: 1px solid var(--line); padding: 7px 10px; text-align: left; vertical-align: top; }
th { background: var(--soft); font-weight: 650; }
tbody tr:nth-child(even) { background: #fafafc; }
ul, ol { margin: 8px 0; padding-left: 26px; }
li { margin: 4px 0; }
.badge {
  display: inline-block; border-radius: 999px; padding: 1px 10px; font-size: 0.82em;
  font-weight: 650; white-space: nowrap; color: #fff;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
.badge.critical { background: var(--critical); }
.badge.high { background: var(--high); }
.badge.medium { background: #b8860b; color: #fff; }
.badge.low { background: var(--low); }
.badge.p1 { background: var(--critical); }
.badge.p2 { background: var(--high); }
.badge.p3 { background: var(--medium); }
.badge.p4 { background: var(--low); }
details.clause { border: 1px solid var(--line); border-radius: 8px; margin: 10px 0;
  background: #fcfcfd; }
details.clause summary { cursor: pointer; padding: 9px 14px; font-weight: 650; list-style: none; }
details.clause summary::-webkit-details-marker { display: none; }
details.clause summary::before { content: "▸ "; color: var(--muted); }
details.clause[open] summary::before { content: "▾ "; }
details.clause > div { padding: 2px 16px 12px; }
details.clause ul { padding-left: 20px; }
.print-btn {
  position: fixed; top: 16px; right: 16px; z-index: 50;
  background: var(--ink); color: #fff; border: 0; border-radius: 999px;
  padding: 9px 18px; font-size: 0.9em; font-weight: 600; cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}
.print-btn:hover { background: #000; }
@media print {
  body { font-size: 11.5pt; }
  .wrap { max-width: none; padding: 0; }
  .print-btn { display: none; }
  h2 { border-top-color: #000; page-break-after: avoid; }
  h3, details.clause { page-break-inside: avoid; }
  tr { page-break-inside: avoid; }
  a { color: inherit; text-decoration: none; }
  details.clause { border-color: #999; background: #fff; }
  details.clause > div { display: block !important; }
}
"""

INLINE_RE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\)|\*[^*]+\*)")

def inline(text):
    out = []
    pos = 0
    for m in INLINE_RE.finditer(text):
        if m.start() > pos:
            out.append(html.escape(text[pos : m.start()]))
        tok = m.group(0)
        if tok.startswith("**") and tok.endswith("**"):
            out.append("<strong>" + inline(tok[2:-2]) + "</strong>")
        elif tok.startswith("`") and tok.endswith("`"):
            out.append("<code>" + html.escape(tok[1:-1]) + "</code>")
        elif tok.startswith("[") and "](" in tok:
            label, url = tok[1:].split("](", 1)
            out.append('<a href="%s">%s</a>' % (html.escape(url[:-1], quote=True), inline(label)))
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            out.append("<em>" + inline(tok[1:-1]) + "</em>")
        else:
            out.append(html.escape(tok))
        pos = m.end()
    if pos < len(text):
        out.append(html.escape(text[pos:]))
    return "".join(out)


def split_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells


def is_sep_row(line):
    cells = split_row(line)
    return all(re.fullmatch(r":?-{2,}:?", c) for c in cells)


def badge(sev):
    cls = SEVERITY.get(sev)
    if cls:
        return f'<span class="badge {cls}">{html.escape(sev)}</span>'
    return None


def render_cell(text, header, annex_map):
    if header == "Schwere":
        m = re.search(r"\*\*([^*]+)\*\*", text)
        if m and m.group(1) in SEVERITY:
            return badge(m.group(1))
    if header == "Priorität":
        p = text.strip()
        if p in {"1", "2", "3", "4"}:
            return f'<span class="badge p{p}">{p}</span>'
    if header in {"Finding", "ID"} and re.fullmatch(r"F\d{3}", text.strip()):
        fid = text.strip()
        target = annex_map.get(fid)
        if target:
            return f'<a href="#{target}">{fid}</a>'
    return inline(text)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    md_path, html_path = sys.argv[1], sys.argv[2]

    with open(md_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    title = "Vertragsprüfung"
    meta = ""
    sections = []  # (level2_heading, [block-html strings])
    cur = None
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            cur = [line[3:].strip(), []]
            sections.append(cur)
        elif line.startswith("### "):
            if cur is not None:
                cur[1].append(("h3", line[4:].strip()))
        elif not line.strip():
            pass
        elif line.startswith("|"):
            rows = []
            header = None
            while i < n and lines[i].startswith("|"):
                if header is None:
                    header = split_row(lines[i])
                elif is_sep_row(lines[i]):
                    pass
                else:
                    rows.append(split_row(lines[i]))
                i += 1
            i -= 1
            if cur is not None:
                cur[1].append(("table", (header, rows)))
        elif line.startswith("- "):
            items = []
            while i < n and lines[i].startswith("- "):
                items.append(lines[i][2:].strip())
                i += 1
            i -= 1
            if cur is not None:
                cur[1].append(("ul", items))
        elif re.match(r"^\d+\.\s", line):
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i]):
                items.append(re.sub(r"^\d+\.\s", "", lines[i]))
                i += 1
            i -= 1
            if cur is not None:
                cur[1].append(("ol", items))
        elif line.startswith("**Law as of:**"):
            meta = inline(line)
        elif cur is not None:
            cur[1].append(("p", line))
        i += 1

    annex_map = {}
    for _, blocks in sections:
        for kind, payload in blocks:
            if kind == "ul":
                for item in payload:
                    m = re.match(r"\*\*(F\d{3})\b", item)
                    if m:
                        annex_map[m.group(1)] = "annex-" + m.group(1)

    body = []
    for heading, blocks in sections:
        body.append(f"<section>\n<h2>{html.escape(heading)}</h2>")
        annex = heading == "Clause-by-clause annex"
        for kind, payload in blocks:
            if kind == "h3":
                if annex:
                    body.append(
                        f'<details class="clause"><summary>{html.escape(payload)}</summary><div>'
                    )
                else:
                    body.append(f"<h3>{html.escape(payload)}</h3>")
            elif kind == "p":
                body.append(f"<p>{inline(payload)}</p>")
            elif kind == "ul":
                body.append("<ul>")
                for item in payload:
                    m = re.match(r"\*\*(F\d{3})\b", item)
                    if annex and m:
                        body.append(f'<li id="annex-{m.group(1)}">{inline(item)}</li>')
                    else:
                        body.append(f"<li>{inline(item)}</li>")
                body.append("</ul>")
            elif kind == "ol":
                body.append("<ol>")
                for item in payload:
                    body.append(f"<li>{inline(item)}</li>")
                body.append("</ol>")
            elif kind == "table":
                header, rows = payload
                body.append("<table>")
                body.append("<thead><tr>" + "".join(f"<th>{html.escape(h)}</th>" for h in header) + "</tr></thead>")
                body.append("<tbody>")
                for row in rows:
                    body.append("<tr>" + "".join(f"<td>{render_cell(c, h, annex_map)}</td>" for c, h in zip(row, header)) + "</tr>")
                body.append("</tbody></table>")
            if kind == "h3" and annex:
                body.append("</div></details>")
        body.append("</section>")

    js = """
function printReport() { window.print(); }
var before = function () {
  document.querySelectorAll('details.clause').forEach(function (d) {
    if (!d.hasAttribute('open')) { d.dataset.autoOpen = '1'; d.setAttribute('open', ''); }
  });
};
var after = function () {
  document.querySelectorAll('details.clause[data-auto-open]').forEach(function (d) {
    d.removeAttribute('open'); delete d.dataset.autoOpen;
  });
};
window.addEventListener('beforeprint', before);
window.addEventListener('afterprint', after);
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.createElement('button');
  btn.className = 'print-btn'; btn.type = 'button'; btn.textContent = 'Drucken';
  btn.addEventListener('click', printReport);
  document.body.appendChild(btn);
});
"""

    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<h1>{html.escape(title)}</h1>
{("<p class=\"meta\">" + meta + "</p>") if meta else ""}
{chr(10).join(body)}
</div>
<script>{js}</script>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"wrote {html_path} ({len(doc)} bytes)")


if __name__ == "__main__":
    main()
