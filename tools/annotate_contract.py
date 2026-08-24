#!/usr/bin/env python3
"""Annotate scanned contract pages with the skill's findings at their clause locations.

Fourth report artifact (SKILL.md § 5): each finding anchored at its clause on the original
pages — per-line yellow highlights over the quote plus a colored gutter callout (badge,
id, severity, legal basis, action, wording). Linked cover sheet, outline bookmarks and
internal links connect cover rows, highlights and endnotes; a severity triage strip sits
in each gutter footer. Locating: tesseract (deu) word TSV per page; quotes token-matched
against the page word stream (>= 4 matches, <= 2 consecutive OCR misses tolerated);
matched words group per printed LINE into highlight quads, borders encode confidence.
Unlocatable findings land in distinct cover sections (contract-wide vs locate failure),
never dropped; clipped callouts point "→ Anm. <n>" at the endnotes carrying every shown
finding's full issue/action/wording/legal_basis/sources. PASS A (resolve/plan_callouts)
computes all geometry without the canvas; PASS B only paints.

Usage:
    python3 tools/annotate_contract.py <report.json> <output.pdf> <page-01.png> [pageN.png ...]
        [--min-severity CRITICAL|HIGH|MEDIUM|LOW]

Dependencies: tesseract (deu), Pillow, reportlab. No network, no pypdf.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import NamedTuple

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
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
SEV_ORDER = ("Critical", "High", "Medium", "Low")
DPI = 300
GUTTER = 120.0  # pt, right-hand annotation gutter
STACK_TOP_PAD, STACK_BOTTOM_PAD = 100.0, 56.0   # pt; bottom reserves footer-strip space
CALLOUT_LINE_H, CALLOUT_HEADER_H, CALLOUT_MIN_H = 8.0, 28.0, 24.0
POINTER_FMT = "\u2192 Anm. %s"
BADGE_R = 7.0                                    # numbered badge radius, pt
CONF_BORDER = {"medium": colors.HexColor("#e87700"), "low": colors.HexColor("#d00000")}


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


def sev_rank(sev):
    """Severity -> rank (Critical=0 .. Low=3); unknown/None -> len(SEV_ORDER)."""
    s = str(sev or "").strip().lower()
    for i, name in enumerate(SEV_ORDER):
        if name.lower() == s:
            return i
    return len(SEV_ORDER)


def sev_color(sev):
    """Case-insensitive severity -> color; unknown/missing -> black."""
    s = str(sev or "").strip().lower()
    for name, col in SEV_COLOR.items():
        if name.lower() == s:
            return col
    return colors.black


def conf_style(conf):
    """Confidence value -> (fill_alpha, border_color_or_None); missing/unknown -> medium."""
    s = conf.strip().lower() if isinstance(conf, str) else ""
    if s == "high":
        return 0.45, None
    return (0.25, CONF_BORDER["low"]) if s == "low" else (0.45, CONF_BORDER["medium"])


def locate_quote(page, q_tokens):
    """Find the clause start: anchor on the first min(12) quote tokens (OCR noise
    tolerated per token), then extend over as many following quote tokens as still match.
    Candidates near the page end are kept: the walk bounds at len(wtoks).
    Returns (start_idx, end_idx, matched) over page.words, or None.
    """
    wtoks = [word_key(w) for w, *_ in page.words]
    anchor = q_tokens[:12]
    best = None  # (anchor_matched, extended_len, start, end)
    for i, t in enumerate(wtoks):
        if not tok_close(t, anchor[0]):
            continue
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


class Word(NamedTuple):
    text: str
    x0: int
    y0: int
    x1: int
    y1: int
    block: int   # tesseract TSV cols 2-4, kept for per-line quad grouping
    par: int
    line: int
    conf: float


class Page:
    def __init__(self, path):
        self.path = path
        self.im = Image.open(path)
        self.w, self.h = self.im.size
        self.scale = 72.0 / DPI
        self.words = self._ocr_words()

    def _ocr_words(self):
        """tesseract TSV -> [Word(text, x0, y0, x1, y1, block, par, line, conf)] in px."""
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
                block, par, line_no = int(p[2]), int(p[3]), int(p[4])
            except ValueError:
                continue
            word = p[11].strip()
            if not word or conf < 10:
                continue
            words.append(Word(word, left, top, left + w, top + h, block, par, line_no, conf))
        return words

    def pt(self, x, y):
        """image px (top-left origin) -> pdf pt (bottom-left origin)."""
        return x * self.scale, (self.h - y) * self.scale


def group_line_quads(page, span):
    """Span words grouped by TSV (block,par,line); one px-rect per line, reading order.
    Inter-line gaps / untouched words between matched lines stay uncovered (fixes D8).
    """
    groups, order = {}, []
    for w in page.words[span[0]:span[1]]:
        key = (w.block, w.par, w.line)
        g = groups.get(key)
        if g is None:
            groups[key] = [w.x0, w.y0, w.x1, w.y1]
            order.append(key)
        else:
            g[0] = min(g[0], w.x0)
            g[1] = min(g[1], w.y0)
            g[2] = max(g[2], w.x1)
            g[3] = max(g[3], w.y1)
    return [tuple(groups[k]) for k in order]


def wrap_w(text, font, size, max_w):
    """Greedy word wrap measured with stringWidth; a single overlong word hard-splits."""
    out, cur = [], ""
    for word in str(text or "").split():
        while stringWidth(word, font, size) > max_w and len(word) > 1:
            n = len(word) - 1
            while n > 1 and stringWidth(word[:n], font, size) > max_w:
                n -= 1
            head, word = word[:n], word[n:]
            if cur:
                out.append(cur)
                cur = ""
            out.append(head)
        cand = cur + " " + word if cur else word
        if cur and stringWidth(cand, font, size) > max_w:
            out.append(cur)
            cur = word
        else:
            cur = cand
    if cur:
        out.append(cur)
    return out


def _join_vals(val):
    """Tolerant '; '-join: str passes through, list/tuple joins, None/empty -> ''."""
    if val is None:
        return ""
    if isinstance(val, str):
        return val
    return "; ".join(str(v) for v in val if v)


def fit_sections(secs, slots):
    """Fit tagged (kind, font, lines) sections into the line budget; clip order per spec:
    wording whole, then legal whole, then remaining lines truncated (one slot reserved
    for the pointer). Returns (kept_secs, clipped).
    """
    def total(ss):
        return sum(len(t) for _, _, t in ss)

    clipped = total(secs) > slots
    kept = [s for s in secs if not (clipped and s[0] == "wording")]
    if clipped and total(kept) > slots:
        kept = [s for s in kept if s[0] != "legal"]
    if clipped and total(kept) > slots:
        remaining = max(slots - 1, 0)
        trimmed = []
        for kind, font, lines in kept:
            take = lines[:remaining]
            if take:
                trimmed.append((kind, font, take))
                remaining -= len(take)
            if remaining <= 0:
                break
        kept = trimmed
    return kept, clipped


# ---- PASS A: layout (no canvas access below until PASS B) -------------------

@dataclass
class Placement:
    f: dict
    fid: str
    status: str                    # "placed" | "contract_wide" | "unplaced"
    page_idx: int = None           # placed only
    span: tuple = None             # placed only: (start_idx, end_idx) over page.words
    quads: list = field(default_factory=list)   # pdf-pt rects (x0,y0,x1,y1), bottom-left origin
    mid_y: float = None            # leader-line anchor, pt (vertical center of quads union)
    callout: tuple = None          # (top_edge_y, box_h) gutter coords; None = gutter exhausted
    lines: list = field(default_factory=list)   # wrapped body lines (possibly clipped)
    clipped: bool = False          # text was truncated -> pointer line drawn
    badge: int = None              # reserved for P1 gutter badges
    endnote_no: int = 0            # 1-based report-order number among shown findings

    @property
    def dest(self):
        return "find-" + self.fid


@dataclass
class Layout:
    placements: list               # report order, shown findings only
    by_page: dict                  # page_idx -> [Placement] (placed, report order)
    contract_wide: list            # [Placement]
    unplaced: list                 # [Placement]
    page_counts: dict              # page_idx -> {severity: n} (post-filter)


def resolve(report, pages, min_rank):
    """PASS A: filter by severity, classify, locate, then plan gutter boxes.

    Unknown/missing severities are ALWAYS kept regardless of min_rank: an unrecognized
    label must never silently drop a legal finding (rendered black downstream).
    """
    findings = report.get("findings") or []
    known_sev = {s.lower() for s in SEV_ORDER}

    picked, pos = [], {}
    for f in findings:
        sev = f.get("severity")
        if isinstance(sev, str) and sev.strip().lower() in known_sev and sev_rank(sev) > min_rank:
            continue
        fid = f.get("id")
        if fid in pos:
            print("warning: duplicate finding id %r - keeping the last occurrence" % fid,
                  file=sys.stderr)
            picked[pos[fid]] = None
        pos[fid] = len(picked)
        picked.append(f)
    picked = [f for f in picked if f is not None]

    placements = []
    for f in picked:
        fid = str(f.get("id"))
        cat = str(f.get("category") or "").lower()
        quote = ((f.get("clause") or {}).get("quote")) or ""
        q_tokens = tokens(quote)
        if cat in CONTRACT_WIDE:
            placements.append(Placement(f=f, fid=fid, status="contract_wide"))
            continue
        best = None
        if q_tokens:
            for pi, pg in enumerate(pages):
                res = locate_quote(pg, q_tokens)
                if res and (best is None or res[2] > best[0]):
                    best = (res[2], pi, res[:2])
        if best:
            placements.append(Placement(f=f, fid=fid, status="placed",
                                        page_idx=best[1], span=best[2]))
        else:
            placements.append(Placement(f=f, fid=fid, status="unplaced"))

    for n, pl in enumerate(placements, 1):
        pl.endnote_no = n

    by_page = {}
    for pl in placements:
        if pl.status == "placed":
            by_page.setdefault(pl.page_idx, []).append(pl)

    page_counts = {}
    for pi, pls in by_page.items():
        counts = {}
        for pl in pls:
            sev = str(pl.f.get("severity") or "Unknown").strip()
            canon = next((s for s in SEV_ORDER if s.lower() == sev.lower()), "Unknown")
            counts[canon] = counts.get(canon, 0) + 1
        page_counts[pi] = counts

    lay = Layout(placements=placements, by_page=by_page,
                 contract_wide=[p for p in placements if p.status == "contract_wide"],
                 unplaced=[p for p in placements if p.status == "unplaced"],
                 page_counts=page_counts)
    for pi, pg in enumerate(pages):
        plan_callouts(pg, by_page.get(pi, []))
    return lay


def plan_callouts(pg, pls):
    """PASS A: stack gutter boxes top-down over the highlights.

    Sorts placements descending by mid_y (ties keep report order via stable sort) so
    leader lines cannot cross. Geometry: per-TSV-line quads, mid_y at quads' union
    center. Content assembled as tagged sections (conf note, legal basis, body, wording),
    fitted by fit_sections; clipped boxes reserve their last slot for the pointer.
    Mutates .quads/.mid_y/.callout/.lines/.clipped.
    """
    for pl in pls:
        qp = group_line_quads(pg, pl.span)
        pl.quads = [(*pg.pt(q[0], q[3]), *pg.pt(q[2], q[1])) for q in qp]
        top_y = pg.pt(min(q[0] for q in qp), max(q[3] for q in qp))[1]
        bot_y = pg.pt(max(q[2] for q in qp), min(q[1] for q in qp))[1]
        pl.mid_y = (top_y + bot_y) / 2.0

    page_h = pg.h * pg.scale
    top = page_h - STACK_TOP_PAD
    for pl in sorted(pls, key=lambda p: -p.mid_y):
        f = pl.f
        max_w = GUTTER - 22                       # GUTTER-12 box minus 2x5pt padding
        secs = []
        if conf_style(f.get("confidence"))[1] is CONF_BORDER["low"]:
            secs.append(("conf", "Helvetica-Bold", ["\u00b7 Konfidenz niedrig"]))
        lb = f.get("legal_basis") or []
        legal = _join_vals(lb[:2] if isinstance(lb, list) else lb)
        if legal:
            secs.append(("legal", "Helvetica-Oblique",
                         wrap_w(legal, "Helvetica-Oblique", 7, max_w)))
        body = str(f.get("recommended_action") or f.get("issue") or "")
        if body:
            secs.append(("body", "Helvetica", wrap_w(body, "Helvetica", 7, max_w)))
        wording = f.get("recommended_wording")
        if wording:
            secs.append(("wording", "Helvetica",
                         wrap_w("Wortlaut: %s" % wording, "Helvetica", 7, max_w)))
        slots = int((top - STACK_BOTTOM_PAD - CALLOUT_HEADER_H) // CALLOUT_LINE_H)
        kept, clipped = fit_sections(secs, slots)
        n_lines = sum(len(t) for _, _, t in kept)
        box_h = CALLOUT_HEADER_H + CALLOUT_LINE_H * (n_lines + (1 if clipped and kept else 0))
        if clipped and not kept:
            box_h = CALLOUT_HEADER_H              # collapsed to header; pointer joins header
        if top - box_h < 0.0:                     # gutter exhausted; endnote still carries it
            pl.callout = None
            continue
        pl.callout = (top, box_h)
        pl.lines = [(k, ln) for k, _, ls in kept for ln in ls]
        pl.clipped = clipped
        top -= box_h + 8.0


# ---- PASS B: render (pure painting, no stacking decisions) ------------------

def draw_highlight(c, pg, pl):
    """Fill each line quad; a dashed border encodes reduced confidence."""
    alpha, border = conf_style(pl.f.get("confidence"))
    rects = [(x0 - 1, y0 - 1, x1 + 1, y1 + 1) for x0, y0, x1, y1 in pl.quads]
    for x0, y0, x1, y1 in rects:
        c.setFillColor(colors.HexColor("#ffdd55"), alpha=alpha)
        c.rect(x0, y0, x1 - x0, y1 - y0, stroke=0, fill=1)
    if border:
        c.setStrokeColor(border)
        c.setLineWidth(1)
        c.setDash(3, 3)
        for x0, y0, x1, y1 in rects:
            c.rect(x0, y0, x1 - x0, y1 - y0, stroke=1, fill=0)
        c.setDash([])                             # no dash bleed into later strokes


CALLOUT_FONT = {"legal": "Helvetica-Oblique", "body": "Helvetica",
                "wording": "Helvetica", "conf": "Helvetica-Bold"}


def draw_badge(c, x, y, n, color, invert=False):
    """Filled disc + number; invert=True renders white disc + colored number."""
    c.setFillColor(colors.white if invert else color)
    c.circle(x, y, BADGE_R, stroke=0, fill=1)
    c.setFillColor(color if invert else colors.white)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(x, y - 3, str(n))


def draw_footer_strip(c, pg, counts):
    """Severity triage chips in the gutter bottom; omitted when nothing is annotated."""
    if not counts:
        return
    gutter_x = pg.w * pg.scale + 6
    limit = gutter_x + GUTTER - 6
    x, y = gutter_x + 4, 14.0
    compact = []
    for sev in SEV_ORDER:
        n = counts.get(sev, 0)
        if not n:
            continue
        label = "\u00d7%d" % n
        lab_w = stringWidth(label, "Helvetica", 7)
        if x + 8 + 4 + lab_w <= limit:
            c.setFillColor(SEV_COLOR[sev])
            c.rect(x, y, 8, 8, stroke=0, fill=1)
            c.setFillColor(colors.black)
            c.setFont("Helvetica", 7)
            c.drawString(x + 12, y + 0.5, label)
            x += 12 + lab_w + 8
        else:                                     # gutter full: deterministic text form
            compact.append("%s%d" % (sev[0], n))
    if compact:
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(gutter_x + 4, y - 10, " ".join(compact))


def draw_callout(c, pg, pl):
    """Colored box + leader line at the geometry precomputed in plan_callouts."""
    if not pl.callout:
        return
    top, box_h = pl.callout
    color = sev_color(pl.f.get("severity"))

    gutter_x = pg.w * pg.scale + 6
    box_w = GUTTER - 12

    qx1 = max(q[2] for q in pl.quads)
    c.setStrokeColor(color)
    c.setLineWidth(0.8)
    c.line(qx1 + 2, pl.mid_y, gutter_x, top - 14)

    header = "%s  %s" % (pl.fid, str(pl.f.get("severity") or ""))
    if pl.clipped and not pl.lines:
        header += "  " + POINTER_FMT % pl.endnote_no
    c.setFillColor(color)
    c.roundRect(gutter_x, top - box_h, box_w, box_h, 4, stroke=0, fill=1)
    draw_badge(c, gutter_x + BADGE_R + 3, top - 11, pl.endnote_no, color, invert=True)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(gutter_x + 2 * BADGE_R + 8, top - 14, header)
    yy = top - CALLOUT_HEADER_H
    if pl.lines:
        for kind, text in pl.lines:
            c.setFont(CALLOUT_FONT[kind], 7)
            c.drawString(gutter_x + 5, yy, text)
            yy -= CALLOUT_LINE_H
    if pl.clipped and pl.lines:
        c.setFont("Helvetica-Bold", 7)
        c.drawString(gutter_x + 5, yy, POINTER_FMT % pl.endnote_no)


def _cover_row_text(c, pl):
    """Cover row for one placement; 'S. N' suffix appended AFTER issue truncation."""
    row = "%s %s - %s" % (pl.fid, ((pl.f.get("clause") or {}).get("clause_id")) or "",
                          str(pl.f.get("issue") or ""))
    if c.stringWidth(row, "Helvetica", 8) > 175 * mm:
        while c.stringWidth(row + "…", "Helvetica", 8) > 175 * mm and len(row) > 10:
            row = row[:-1]
        row += "…"
    if pl.status == "placed":
        row += ", S. %d" % (pl.page_idx + 2)   # cover = PDF page 1, body page i = PDF page i+2
    return row

def _cover_row(c, pl, x, y):
    """Draw one cover row text plus its internal link (placed -> highlight, else endnote)."""
    text = _cover_row_text(c, pl)
    c.drawString(x, y, text)
    dest = pl.dest if pl.status == "placed" else "note-" + pl.fid
    c.linkAbsolute("", dest,
                   Rect=(x - 1, y - 2, x + stringWidth(text, "Helvetica", 8) + 3, y + 3))


def build_cover(c, report, lay):
    c.setPageSize(A4)
    c.bookmarkPage("cover")
    c.addOutlineEntry("Deckblatt", "cover", level=0, closed=False)
    w, h = A4
    counts = report.get("risk_profile", {}).get("counts", {})
    y = h - 18 * mm
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(15 * mm, y, "Befunde im Vertrag verortet")
    y -= 8 * mm
    c.setFont("Helvetica", 9)
    c.drawString(15 * mm, y, "Annotierte Kopie des Originalvertrags - jede Markierung verweist auf die vollständige Analyse.")
    y -= 6 * mm
    for sev in SEV_ORDER:
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
    for pl in lay.placements:
        if pl.status != "placed":
            continue
        c.setFillColor(sev_color(pl.f.get("severity")))
        c.circle(17 * mm, y + 1.5, 1.8, stroke=0, fill=1)
        c.setFillColor(colors.black)
        _cover_row(c, pl, 20 * mm, y)
        y -= 4 * mm
        if y < 15 * mm:
            break
    for title, items in (
        ("Vertragweit geprüft (keine Einzelverortung):", lay.contract_wide),
        ("Nicht exakt verortet (OCR / seitenübergreifend):", lay.unplaced),
    ):
        if not items:
            continue
        y -= 6 * mm
        c.setFillColor(colors.HexColor("#e87700"))
        c.setFont("Helvetica-Bold", 9)
        c.drawString(15 * mm, y, title)
        y -= 5 * mm
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.black)
        for pl in sorted(items, key=lambda p: p.fid):
            _cover_row(c, pl, 15 * mm, y)
            y -= 4 * mm
            if y < 10 * mm:
                break
    c.showPage()


def build_body(c, pages, lay):
    """Paint each scanned page: highlights, badges, gutter callouts, footer strip;
    register page/finding destinations and outline entries."""
    for pi, pg in enumerate(pages):
        img_w_pt = pg.w * pg.scale
        img_h_pt = pg.h * pg.scale
        c.setPageSize((img_w_pt + GUTTER, img_h_pt))
        c.drawImage(pg.path, 0, 0, width=img_w_pt, height=img_h_pt)
        c.bookmarkPage("page-%d" % pi)
        c.addOutlineEntry("Seite %d" % (pi + 1), "page-%d" % pi, level=0, closed=False)
        for pl in lay.by_page.get(pi, []):
            draw_highlight(c, pg, pl)
            qx0, _, _, qy1 = pl.quads[0]
            draw_badge(c, qx0 + 2, min(qy1 + BADGE_R + 2, img_h_pt - BADGE_R - 4),
                       pl.endnote_no, sev_color(pl.f.get("severity")))
            c.bookmarkPage(pl.dest, fit="XYZ",
                           top=max(q[3] for q in pl.quads) + 20)
            cid = ((pl.f.get("clause") or {}).get("clause_id")) or ""
            c.addOutlineEntry("%s \u00b7 %s" % (pl.fid, cid), pl.dest, level=1,
                              closed=False)
        for pl in sorted(lay.by_page.get(pi, []), key=lambda p: -(p.callout[0] if p.callout else 0)):
            draw_callout(c, pg, pl)
        draw_footer_strip(c, pg, lay.page_counts.get(pi) or {})
        c.showPage()


def build_endnotes(c, report, lay):
    """A4 endnotes: one numbered entry per SHOWN finding (placed/contract-wide/unplaced);
    headers never split, long entries flow onto "Anmerkungen (Fortsetzung)" pages; placed
    entries back-link to their body-page anchor. Retires gutter clipping as content loss.
    Returns the number of endnote pages.
    """
    w, h = A4
    max_w = 180 * mm
    state = {"page": 0, "y": 0.0}

    def start_page():
        if state["page"]:
            c.showPage()
        c.setPageSize(A4)
        state["page"] += 1
        y = h - 18 * mm
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 15)
        c.drawString(15 * mm, y, "Anmerkungen" if state["page"] == 1
                     else "Anmerkungen (Fortsetzung)")
        if state["page"] == 1:
            c.bookmarkPage("endnotes")
            c.addOutlineEntry("Anmerkungen", "endnotes", level=0, closed=False)
        state["y"] = y - 10 * mm

    start_page()
    if not lay.placements:
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 8)
        c.drawString(15 * mm, state["y"], "(keine Befunde nach Filter)")
        return 1
    for pl in lay.placements:
        f = pl.f
        cid = ((f.get("clause") or {}).get("clause_id")) or ""
        header = "%s \u00b7 %s \u00b7 %s" % (pl.fid, cid, str(f.get("severity") or ""))
        secs = [
            str(f.get("issue") or ""),
            str(f.get("recommended_action") or ""),
            ("Wortlaut: %s" % f.get("recommended_wording"))
            if f.get("recommended_wording") else "",
            ("Rechtsgrundlage: %s" % _join_vals(f.get("legal_basis")))
            if f.get("legal_basis") else "",
            ("Quellen: %s" % _join_vals(f.get("sources"))) if f.get("sources") else "",
            ("Rechtsstand in Bewegung: %s" % f.get("law_in_flux"))
            if f.get("law_in_flux") else "",
        ]
        lines = []
        for sec in secs:
            if sec:
                lines.extend(wrap_w(sec, "Helvetica", 8, max_w))
        if state["y"] < 26 * mm:                  # header + at least one body line must fit
            start_page()
        hy = state["y"]
        c.bookmarkPage("note-" + pl.fid)
        draw_badge(c, 17 * mm, hy + 2, pl.endnote_no, sev_color(f.get("severity")))
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(20 * mm, hy, header)
        if pl.status == "placed":
            hw = stringWidth(header, "Helvetica-Bold", 9)
            c.linkAbsolute("", pl.dest,
                           Rect=(20 * mm - 1, hy - 2, 20 * mm + hw + 3, hy + 4))
        state["y"] = hy - 5 * mm
        c.setFont("Helvetica", 8)
        for ln in lines:
            if state["y"] < 20 * mm:
                start_page()
                c.setFont("Helvetica", 8)
            c.drawString(15 * mm, state["y"], ln)
            state["y"] -= 4 * mm
        state["y"] -= 2 * mm                      # gap between entries
    return state["page"]


# ---- entry ------------------------------------------------------------------
def _existing_file(value):
    """argparse type: reject nonexistent page images with a usage error (exit 2)
    instead of a mid-pipeline traceback -- argparse alone cannot distinguish
    legacy invocations that passed a dead fourth argv slot before the pages."""
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError("no such file: %s" % value)
    return value


def build_parser():
    p = argparse.ArgumentParser(
        description="Annotate scanned contract pages with located findings "
                    "(see module docstring for the pipeline).")
    p.add_argument("report", help="report.json from the analysis pipeline")
    p.add_argument("out", help="output PDF path")
    p.add_argument("pages", nargs="+", type=_existing_file,
                   help="scanned page images (PNG etc.), in reading order")
    p.add_argument("--min-severity", choices=("CRITICAL", "HIGH", "MEDIUM", "LOW"),
                   type=str.upper, default="LOW",
                   help="drop findings strictly below this severity (unknown severities are kept)")
    return p


MIN_RANK = {name.upper(): i for i, name in enumerate(SEV_ORDER)}


def main(argv=None):
    args = build_parser().parse_args(argv)
    with open(args.report) as fh:
        report = json.load(fh)
    pages = [Page(p) for p in args.pages]

    lay = resolve(report, pages, MIN_RANK[args.min_severity])

    c = canvas.Canvas(args.out)
    build_cover(c, report, lay)
    build_body(c, pages, lay)
    n_endnotes = build_endnotes(c, report, lay)
    c.save()

    total = len(report.get("findings") or [])
    print("wrote %s (%d pages, %d/%d findings, %d vertragweit, %d nicht verortet)" % (
        args.out, len(pages) + n_endnotes, len(lay.placements), total,
        len(lay.contract_wide), len(lay.unplaced)))
    if lay.unplaced:
        print("not exactly located: %s" % ", ".join(sorted(pl.fid for pl in lay.unplaced)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
