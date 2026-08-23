#!/usr/bin/env python3
"""Annotate scanned contract pages with the skill's findings at their clause locations.

Fourth report artifact (SKILL.md § 5): the original contract pages, each finding anchored
at the clause it refers to. Every finding gets a yellow highlight over its quoted clause
plus a colored gutter callout beside it (F-id, severity, full recommended action). A cover
sheet lists all findings with severity chips and links them to the full report.

Locating a clause on a scan:
  1. Each page image is OCR'd with tesseract (deu) to word-level TSV (text + boxes).
  2. The finding's quote (verbatim from report.json) is token-matched against each page's
     word stream; the best page + word span wins (>= 4 matched tokens, gap-tolerant anchor
     walk with <= 2 consecutive misses tolerated for OCR glyph drift).
  3. The matched word boxes union into the highlight rectangle; the callout sits in a
     dedicated right gutter so no contract text is obscured.

Findings that cannot be located (quote spans pages, OCR drift, contract-wide scope like
NachwG gaps) are listed on the cover sheet as "nicht exakt verortet" - never dropped.

Usage:
    python3 tools/annotate_contract.py <report.json> <contract_ocr.txt> <output.pdf> <page-01.png> [page-02.png ...]

Dependencies: tesseract (deu), Pillow, reportlab. No network, no pypdf.
"""

import json
import re
import subprocess
import sys

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

SEV_COLOR = {
    "Critical": colors.HexColor("#d00000"),
    "High": colors.HexColor("#e87700"),
    "Medium": colors.HexColor("#d9a400"),
    "Low": colors.HexColor("#4a90d9"),
}
SEV_GLOSS = {
    "Critical": "Kritisch: unwirksam, bindet nicht, Handlungsbedarf",
    "High": "Hoch: sehr wahrscheinlich unwirksam oder erhebliches Risiko",
    "Medium": "Mittel: nur unter engen Bedingungen wirksam",
    "Low": "Niedrig: Gestaltungsschwäche / Transparenzproblem",
}
CONTRACT_WIDE = {"nachwg", "whole-contract", "transparency"}

DPI = 300
GUTTER = 120.0  # pt, right-hand annotation gutter


def norm(s):
    s = re.sub(r"\s+", " ", s)
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u201e", '"').replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")
    return s.strip()


def word_key(s):
    """OCR word -> comparable key: lowercase, punctuation stripped."""
    return re.sub(r"[^\w\u00C0-\uFFFF]", "", s).lower()


def tokens(s):
    return [t for t in re.findall(r"[A-Za-z0-9\u00c0-\u024f-]+", norm(s).lower()) if t]


def tok_close(a, b):
    """Fuzzy equality for OCR noise: exact, prefix, or small edit distance."""
    if a == b:
        return True
    if len(a) < 4 or len(b) < 4:
        return False
    if a.startswith(b) or b.startswith(a):
        return True
    # one-char edit distance (substitution / deletion / insertion)
    if abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(1 for x, y in zip(a, b) if x != y) <= 1
    short, long = (a, b) if len(a) < len(b) else (b, a)
    for i in range(len(long)):
        if long[:i] + long[i + 1:] == short:
            return True
    return False


def locate_quote(page, q_tokens):
    """Find the clause start on the page.

    Anchor on the first min(12) quote tokens (OCR noise tolerated per token),
    then extend the span over as many following quote tokens as still match.
    Returns (start_idx, end_idx, matched) over page.words, or None.
    """
    wtoks = [word_key(w) for w, *_ in page.words]
    anchor = q_tokens[:12]
    best = None  # (anchor_matched, extended_len, start, end)
    for i, t in enumerate(wtoks):
        if not tok_close(t, anchor[0]):
            continue
        if i + len(anchor) > len(wtoks):
            break
        # walk the anchor window
        j, k, misses, matched = 0, i, 0, 0
        while j < len(anchor) and k < len(wtoks) and misses <= 2:
            if tok_close(wtoks[k], anchor[j]):
                matched += 1
                j += 1
            else:
                misses += 1
            k += 1
        if matched < max(4, int(0.4 * len(anchor))):
            continue
        # extend over the rest of the quote
        end = k
        j, misses = len(anchor), 0
        while j < len(q_tokens) and end < len(wtoks) and misses <= 3:
            if tok_close(wtoks[end], q_tokens[j]):
                j += 1
                end += 1
                misses = 0
            else:
                misses += 1
                end += 1
        score = (matched, end - i)
        if best is None or score > best[0]:
            best = (score, i, end)
    if best is None:
        return None
    return best[1], best[2], best[0]


class Page:
    def __init__(self, path):
        self.path = path
        self.im = Image.open(path)
        self.w, self.h = self.im.size
        self.scale = 72.0 / DPI
        self.words = self._ocr_words()

    def _ocr_words(self):
        """tesseract TSV -> [(word, x0, y0, x1, y1)] in image px (top-left origin)."""
        out = subprocess.run(
            ["tesseract", self.path, "stdout", "-l", "deu", "--psm", "3", "tsv"],
            capture_output=True, text=True, timeout=120,
        ).stdout
        words = []
        for line in out.splitlines()[1:]:
            p = line.split("\t")
            if len(p) < 12:
                continue
            try:
                left, top, w, h, conf = int(p[6]), int(p[7]), int(p[8]), int(p[9]), float(p[10])
            except ValueError:
                continue
            word = p[11].strip()
            if not word or conf < 10:
                continue
            words.append((word, left, top, left + w, top + h))
        return words

    def pt(self, x, y):
        """image px (top-left origin) -> pdf pt (bottom-left origin)."""
        return x * self.scale, (self.h - y) * self.scale


def union_bbox(page, span):
    sel = page.words[span[0]:span[1]]
    x0 = min(w[1] for w in sel)
    y0 = min(w[2] for w in sel)
    x1 = max(w[3] for w in sel)
    y1 = max(w[4] for w in sel)
    return x0, y0, x1, y1


def wrap(text, width):
    out, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            out.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    if cur:
        out.append(cur)
    return out


def draw_callout(c, page, span, bbox, f, top):
    """Colored box + leader line in the right gutter at the highlight's height.

    Box height fits the full text; returns the next free stack top. Text is
    clipped with an ellipsis only if the box would run off the page bottom.
    """
    x0, y0 = page.pt(bbox[0], bbox[3])
    x1, y1 = page.pt(bbox[2], bbox[1])
    mid_y = (y0 + y1) / 2

    gutter_x = page.w * page.scale + 6
    box_w = GUTTER - 12

    text = f.get("recommended_action") or f.get("issue") or ""
    lines = wrap(text, 22)
    box_h = 28 + 8 * len(lines)
    # slide down if the box would cross the page top; bottom clamp is last resort
    page_h = page.h * page.scale
    if top + box_h > page_h:
        top = page_h - box_h
    max_lines = max(1, (top - 48) // 8)  # keep box bottom >= 20pt from page bottom
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while c.stringWidth(last + "\u2026", "Helvetica", 7) > box_w - 10 and len(last) > 1:
            last = last[:-1]
        lines[-1] = last + "\u2026"
    box_h = 28 + 8 * len(lines)

    color = SEV_COLOR.get(f.get("severity"), colors.black)
    c.setStrokeColor(color)
    c.setLineWidth(0.8)
    c.line(x1 + 2, mid_y, gutter_x, top + 34)

    c.setFillColor(color)
    c.roundRect(gutter_x, top, box_w, box_h, 4, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(gutter_x + 5, top + box_h - 14, f["id"] + "  " + (f.get("severity") or ""))
    c.setFont("Helvetica", 7)
    yy = top + box_h - 28
    for line in lines:
        c.drawString(gutter_x + 5, yy, line)
        yy -= 8
    return top - box_h - 8


def build_cover(c, report, unplaced):
    c.setPageSize(A4)
    w, h = A4
    findings = report["findings"]
    counts = report.get("risk_profile", {}).get("counts", {})
    y = h - 18 * mm
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(15 * mm, y, "Befunde im Vertrag verortet")
    y -= 8 * mm
    c.setFont("Helvetica", 9)
    c.drawString(15 * mm, y, "Annotierte Kopie des Originalvertrags - jede Markierung verweist auf die vollständige Analyse.")
    y -= 6 * mm
    for sev in ("Critical", "High", "Medium", "Low"):
        n = counts.get(sev, 0)
        c.setFillColor(SEV_COLOR[sev])
        c.circle(18 * mm, y + 2, 2.5, stroke=0, fill=1)
        c.setFillColor(colors.black)
        c.drawString(22 * mm, y, "%s (%d) - %s" % (sev, n, SEV_GLOSS[sev]))
        y -= 5 * mm
    y -= 4 * mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(15 * mm, y, "Findings:")
    y -= 5 * mm
    c.setFont("Helvetica", 8)
    for f in findings:
        if f["id"] in unplaced:
            continue
        c.setFillColor(SEV_COLOR.get(f.get("severity"), colors.black))
        c.circle(17 * mm, y + 1.5, 1.8, stroke=0, fill=1)
        c.setFillColor(colors.black)
        row = "%s %s - %s" % (f["id"], f.get("clause", {}).get("clause_id", ""), (f.get("issue") or ""))
        if c.stringWidth(row, "Helvetica", 8) > 175 * mm:
            while c.stringWidth(row + "…", "Helvetica", 8) > 175 * mm and len(row) > 10:
                row = row[:-1]
            row += "…"
        c.drawString(20 * mm, y, row)
        y -= 4 * mm
        if y < 15 * mm:
            break
    if unplaced:
        y -= 6 * mm
        c.setFillColor(colors.HexColor("#e87700"))
        c.setFont("Helvetica-Bold", 9)
        c.drawString(15 * mm, y, "Nicht exakt verortet (OCR / seitenübergreifend):")
        y -= 5 * mm
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.black)
        for fid in sorted(unplaced):
            f = next(x for x in findings if x["id"] == fid)
            row = "%s - %s" % (fid, (f.get("issue") or ""))
            if c.stringWidth(row, "Helvetica", 8) > 175 * mm:
                while c.stringWidth(row + "…", "Helvetica", 8) > 175 * mm and len(row) > 10:
                    row = row[:-1]
                row += "…"
            c.drawString(15 * mm, y, row)
            y -= 4 * mm
            if y < 10 * mm:
                break
    c.showPage()


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        sys.exit(2)
    json_path, ocr_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    pages = [Page(p) for p in sys.argv[4:]]

    report = json.load(open(json_path))
    findings = report["findings"]
    ocr = norm(open(ocr_path).read())
    ocr_tokens = tokens(ocr)

    # resolve findings -> (page_idx, span)
    placed = {}
    for f in findings:
        cat = (f.get("category") or "").lower()
        q_tokens = tokens(f["clause"]["quote"])
        if not q_tokens or cat in CONTRACT_WIDE:
            placed[f["id"]] = (None, None)
            continue
        best = None
        for pi, pg in enumerate(pages):
            res = locate_quote(pg, q_tokens)
            if res:
                span, matched = res[:2], res[2]
                if best is None or matched > best[0]:
                    best = (matched, pi, span)
        placed[f["id"]] = (best[1], best[2]) if best else (None, None)


    unplaced = {fid for fid, (pi, _) in placed.items() if pi is None}

    # render: cover + per-page image with highlight + gutter callouts
    c = canvas.Canvas(out_path)
    build_cover(c, report, unplaced)
    for pi, pg in enumerate(pages):
        img_w_pt = pg.w * pg.scale
        img_h_pt = pg.h * pg.scale
        c.setPageSize((img_w_pt + GUTTER, img_h_pt))
        c.drawImage(pg.path, 0, 0, width=img_w_pt, height=img_h_pt)
        top = pg.h * pg.scale - 100
        page_findings = [(fid, sp) for fid, (p, sp) in placed.items() if p == pi]
        for idx, (fid, span) in enumerate(page_findings):
            f = next(x for x in findings if x["id"] == fid)
            bbox = union_bbox(pg, span)
            # highlight
            x0, y0 = pg.pt(bbox[0], bbox[3])
            x1, y1 = pg.pt(bbox[2], bbox[1])
            c.setFillColor(colors.HexColor("#ffdd55"), alpha=0.45)
            c.rect(x0 - 1, y0 - 1, (x1 - x0) + 2, (y1 - y0) + 2, stroke=0, fill=1)
            top = draw_callout(c, pg, span, bbox, f, top)
        c.showPage()
    c.save()
    print("wrote %s (%d pages, %d findings, %d unplaced)" % (
        out_path, len(pages) + 1, len(findings), len(unplaced)))
    if unplaced:
        print("not exactly located: %s" % ", ".join(sorted(unplaced)))


if __name__ == "__main__":
    main()
