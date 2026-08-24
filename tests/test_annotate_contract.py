#!/usr/bin/env python3
"""Tests for tools/annotate_contract.py (spec: research/annotate-spec.md §8).

Synthetic fixtures (2 German-text page PNGs + report.json) are generated on the
fly in setUpClass into tests/fixtures/ (gitignored) -- no binary fixtures are
committed. OCR-dependent smoke tests skip when tesseract is missing; pypdf /
pdftotext assertions degrade gracefully.
"""

import importlib.util
import json
import shutil
import subprocess
import sys
import types
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TOOL = REPO / "tools" / "annotate_contract.py"
FIXDIR = Path(__file__).resolve().parent / "fixtures"

HAVE_TESSERACT = shutil.which("tesseract") is not None

_spec = importlib.util.spec_from_file_location("annotate_contract", TOOL)
ac = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ac)


# ---------------------------------------------------------------- fixtures --

FONT_CANDIDATES = [
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "C:\\Windows\\Fonts\\arial.ttf",
]

FILLER1 = ("Der Arbeitgeber weist auf die geltenden Regelungen des Betriebsverfassungs"
           "gesetzes hin und behält sich das Hausrecht vor.")
FILLER2 = ("Soweit einzelne Bestimmungen dieses Vertrages unwirksam sein sollten, bleibt "
           "die Wirksamkeit der übrigen Regelungen unberührt.")

Q1_LINE1 = "Der Arbeitnehmer erhält einen bezahlten Jahresurlaub von dreißig Kalendertagen,"
Q1_LINE2 = "wobei der Urlaub vor dem dreißigsten Juni des Folgejahres genommen werden muss."
Q1 = Q1_LINE1 + " " + Q1_LINE2  # 19 tokens incl. umlauts/ß, spans 2 printed lines

Q2 = "Die Probezeit beträgt maximal sechs Monate."

LONG_WORDING_F001 = (
    "Neufassung: „Der Arbeitnehmer hat einen bezahlten Jahresurlaub von dreißig "
    "Kalendertagen. Der Urlaub ist in der freien Zeit zwischen dem 01. Juli und dem "
    "30. September zu gewähren; ein Verfall des Urlaubs bedarf einer ausdrücklichen "
    "gesonderten schriftlichen Hinweisbelehrung durch den Arbeitgeber im Kalenderjahr "
    "des Urlaubsanspruchs sowie der Mitwirkung des Arbeitnehmers, und jede abweichende "
    "Vereinbarung ist nur mit Schriftform wirksam.“")

LONG_ACTION = ("Die Klausel ist wegen Verstoßes gegen §§ 7, 13 BUrlG unwirksam; "
               "der Arbeitgeber muss die Urlaubsrichtlinie neu fassen und den Verfall "
               "ausschließen, andernfalls drohen Kündigungsrisiken und Nachzahlungen "
               "für gewährten aber verfallenen Resturlaub über mehrere Jahre hinweg. "
               ) * 4


def _find_font():
    for p in FONT_CANDIDATES:
        if Path(p).exists():
            return p
    return None


def _make_report():
    def f(fid, sev, conf, cat, quote, **kw):
        d = {"id": fid, "severity": sev, "confidence": conf, "category": cat,
             "clause": {"clause_id": kw.pop("cid", fid.lower()), "quote": quote},
             "issue": "Musterbefund %s: prüfungsrelevante Klausel." % fid,
             "recommended_action": kw.pop("action", "Klausel überprüfen und anpassen."),
             }
        if quote is not None:
            pass
        else:
            del d["clause"]["quote"]
        d.update(kw)
        return d

    findings = [
        f("F001", "Critical", "high", "Befristung", Q1,
          cid="urlaub",
          recommended_wording=LONG_WORDING_F001,
          legal_basis=["§ 7 BUrlG", "§ 13 BUrlG"],
          sources=["https://example.gesetze/burlg"]),
        f("F002", "High", "medium", "Entlohnung", Q2,
          cid="probezeit",
          # no legal_basis field at all
          recommended_wording="„Die Probezeit beträgt höchstens sechs Monate.“"),
        f("F003", "Low", "low", "transparency", None,
          cid="arbeitszeit",
          issue="Vertragweit: Arbeitszeittransparenz insgesamt unzureichend dokumentiert.",
          law_in_flux="EuGH-Rechtsprechung in Bewegung"),
        f("F004", "Medium", "high", "Klausel", None,
          cid="salvatorisch",
          quote_missing=True,   # words appearing NOWHERE -> unplaceable
          clause={"clause_id": "salvatorisch"},
          ),
        f("F005", "Low", "high", "Klausel", Q1 + " Und zwar unverzüglich.",
          cid="urlaub-var"),
    ]
    # F004: quote of words that appear nowhere in the fixtures
    findings[3]["clause"]["quote"] = ("Quixotischer Zwergfederball Helikopterlandeplatz")
    counts = {"Critical": 1, "High": 1, "Medium": 1, "Low": 2}
    return {"$schema": "./schema/report.schema.v1.json", "title": "Testvertrag",
            "schema_version": "1.0", "law_as_of": "2026-08",
            "contract": {"employer": "Test GmbH", "role": "Fachkraft"},
            "risk_profile": {"counts": counts, "top_risks": []},
            "findings": findings}


def _draw_page(draw, font, lines):
    y = 260
    for text in lines:
        draw.text((200, y), text, fill="black", font=font)
        y += 78


def _page_lines(page_no):
    if page_no == 1:                       # Q1 twice, once in filler context
        return [FILLER1 + " Zusätzlich gilt die genannte Urlaubsregelung.",
                FILLER2,
                Q1_LINE1,
                Q1_LINE2,
                FILLER1]
    return [FILLER2,                       # page 2: single-line quote Q2
            Q2,
            FILLER1]


def _generate_fixtures():
    from PIL import Image, ImageDraw, ImageFont
    FIXDIR.mkdir(parents=True, exist_ok=True)
    font_path = _find_font()
    if not font_path:
        raise unittest.SkipTest("no truetype font found for fixture drawing")
    font = ImageFont.truetype(font_path, 44)
    paths = []
    for i in range(2):
        img = Image.new("RGB", (2480, 3508), "white")
        _draw_page(ImageDraw.Draw(img), font, _page_lines(i))
        p = FIXDIR / ("p%d.png" % (i + 1))
        img.save(p)
        paths.append(p)
    report_path = FIXDIR / "report.json"
    report_path.write_text(json.dumps(_make_report(), ensure_ascii=False, indent=1),
                           encoding="utf-8")
    return paths, report_path


# ---------------------------------------------------------------- helpers --

def extract_pdf_text(pdf_path):
    """(full_text_with_single_spaces, list_of_page_texts, n_endnote_pages)."""
    try:
        from pypdf import PdfReader
        pages = [(p.extract_text() or "") for p in PdfReader(str(pdf_path)).pages]
    except ImportError:
        r = subprocess.run(["pdftotext", str(pdf_path), "-"],
                           capture_output=True, text=True)
        full = r.stdout
        pages = full.split("\f")
    flat = " ".join(" ".join(p.split()) for p in pages)
    n_end = sum(1 for p in pages if "Anmerkungen" in p)
    return flat, pages, n_end


class FakeWord(tuple):
    """2-tuple shaped for `for w, *_ in page.words` (locate_quote only reads w[0])."""


# ---------------------------------------------------------------- unit tests --

class TestLocateQuotePageEnd(unittest.TestCase):
    """P0-6: anchor running past the page end still locates via partial window."""

    @staticmethod
    def fake_page(words_text):
        pg = types.SimpleNamespace()
        pg.words = [FakeWord((t,)) for t in words_text]
        return pg

    def test_anchor_past_end_located(self):
        q = ("eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf "
             "dreizehn vierzehn").split()          # 14-token anchor
        tail = q[:5]                               # clean leading matches at page end
        words = ["füllwort"] * 20 + ["anderes"] + tail
        res = ac.locate_quote(self.fake_page(words), q)
        self.assertIsNotNone(res)
        start, end, matched = res
        self.assertEqual(end, len(words))          # span clamped to page end
        self.assertGreaterEqual(matched[0], 4)

    def test_below_threshold_rejected(self):
        q = ["eins", "zwei", "drei", "vier"]
        words = ["füllwort"] * 10 + ["eins"]       # single match < max(4, ...)
        self.assertIsNone(ac.locate_quote(self.fake_page(words), q))


class TestWrapW(unittest.TestCase):
    def test_lines_fit_measured_width(self):
        text = ("Die außerordentliche Kündigung ist ausgeschlossen es sei denn es "
                "liegen sachliche Gründe vor die eine Fortsetzung unmöglich machen.") * 6
        max_w = ac.GUTTER - 22
        for line in ac.wrap_w(text, "Helvetica", 7, max_w):
            self.assertLessEqual(
                __import__("reportlab.pdfbase.pdfmetrics", fromlist=["stringWidth"])
                .stringWidth(line, "Helvetica", 7), max_w + 0.51)

    def test_overlong_word_hard_split(self):
        word = "x" * 200
        lines = ac.wrap_w(word, "Helvetica", 7, 98.0)
        self.assertGreater(len(lines), 1)
        for line in lines:
            self.assertLessEqual(ac.stringWidth(line, "Helvetica", 7), 98.0)


class TestConfStyle(unittest.TestCase):
    def table_case(self, conf, expected):
        self.assertEqual(ac.conf_style(conf), expected)

    def test_high(self):
        self.table_case("high", (0.45, None))
        self.table_case("HIGH", (0.45, None))

    def test_medium_and_missing(self):
        med = (0.45, ac.CONF_BORDER["medium"])
        self.table_case("Medium", med)
        self.table_case(None, med)          # missing -> medium treatment
        self.table_case(42, med)            # non-string -> missing
        self.table_case("", med)

    def test_low(self):
        low = (0.25, ac.CONF_BORDER["low"])
        self.table_case("LOW", low)
        self.table_case("Low", low)


class TestGroupLineQuads(unittest.TestCase):
    def test_three_line_keys_three_quads_narrower_than_span(self):
        W = ac.Word
        words = [
            W("aa", 100, 1000, 300, 1050, 1, 1, 1, 90),
            W("bb", 320, 1000, 520, 1050, 1, 1, 1, 90),
            W("cc", 100, 1100, 400, 1150, 1, 1, 2, 90),
            W("dd", 150, 1200, 450, 1250, 2, 1, 1, 90),
            W("ee", 470, 1200, 700, 1250, 2, 1, 1, 90),
        ]
        pg = types.SimpleNamespace(words=words)
        quads = ac.group_line_quads(pg, (0, 5))
        self.assertEqual(len(quads), 3)
        span_x0 = min(q[0] for q in quads)
        span_x1 = max(q[2] for q in quads)
        for x0, _, x1, _ in quads:
            self.assertGreater(x1 - x0, 0)
            self.assertLess(x1 - x0, span_x1 - span_x0)   # narrower than union
        # reading order preserved
        self.assertEqual(quads[0][1], 1000)
        self.assertEqual(quads[1][1], 1100)
        self.assertEqual(quads[2][1], 1200)


class TestDeepStackNoOverlap(unittest.TestCase):
    """P0-5: >=8 clipped callouts stay in the gutter, pointers assigned, no overlap."""

    def test_deep_stack(self):
        W = ac.Word
        n_findings = 10
        words = []
        spans = {}
        idx = 0
        for k in range(n_findings):
            ws = ["anker%d" % k, "folge%d" % k, "schluss%d" % k]
            for t in ws:
                words.append(W(t, 100, 500 + idx * 30, 300, 525 + idx * 30, k + 1, 1, 1, 95))
                idx += 1
            spans["D%03d" % k] = (idx - 3, idx)
        pg = types.SimpleNamespace(words=words)
        pg.h = 3508
        pg.scale = 72.0 / 300
        pg.pt = lambda x, y: (x * pg.scale, (pg.h - y) * pg.scale)
        findings = [{"id": "D%03d" % k, "severity": "High", "confidence": "high",
                     "category": "Klausel",
                     "clause": {"clause_id": "c%d" % k, "quote": "irrelevant"},
                     "recommended_action":
                         LONG_ACTION if k >= 8 else
                         "Klausel %d ist anzupassen und neu zu fassen." % k}
                    for k in range(n_findings)]
        lay = types.SimpleNamespace()
        pls = [ac.Placement(f=f, fid=f["id"], status="placed",
                            page_idx=0, span=spans[f["id"]]) for f in findings]
        for n, pl in enumerate(pls, 1):
            pl.endnote_no = n
        ac.plan_callouts(pg, pls)
        boxes = sorted([pl for pl in pls if pl.callout],
                       key=lambda p: -p.callout[0])
        self.assertGreaterEqual(len(boxes), 8)
        self.assertTrue(any(pl.clipped for pl in pls))
        # monotone decreasing tops with 8pt gap, nothing below y=0
        prev_top = None
        for pl in boxes:
            top, box_h = pl.callout
            if prev_top is not None:
                self.assertLessEqual(top, prev_top - box_h_prev - 8.0 + 0.01)
            self.assertGreaterEqual(top - box_h, 0.0)
            prev_top, box_h_prev = top, box_h
        # P0-5: the pointer line is pdftotext-greppable once actually painted
        pg.w = 2480
        from io import BytesIO
        from pypdf import PdfReader
        buf = BytesIO()
        rc = ac.canvas.Canvas(buf)
        rc.setPageSize((pg.w * pg.scale + ac.GUTTER, 841.89))
        for pl in boxes:
            ac.draw_callout(rc, pg, pl)
        rc.showPage()
        rc.save()
        buf.seek(0)
        text = " ".join("".join(p.extract_text() or "" for p in PdfReader(buf).pages).split())
        self.assertIn("\u2192 Anm.", text)


# ---------------------------------------------------------------- smoke tests --

@unittest.skipUnless(HAVE_TESSERACT, "tesseract binary not available")
@unittest.skipIf(_find_font() is None, "no truetype font for fixture drawing")
class SmokeTest(unittest.TestCase):
    PAGES = None
    REPORT = None

    @classmethod
    def setUpClass(cls):
        cls.PAGES, cls.REPORT = _generate_fixtures()

    @classmethod
    def tearDownClass(cls):
        for p in list(FIXDIR.glob("*.png")) + list(FIXDIR.glob("*.pdf")):
            p.unlink(missing_ok=True)

    def run_cli(self, out_name, extra=()):
        out = FIXDIR / out_name
        cmd = [sys.executable, str(TOOL), str(self.REPORT), str(out)] + \
              [str(p) for p in self.PAGES] + list(extra)
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        return r, out

    def test_smoke_default(self):
        r, out = self.run_cli("out.pdf")
        self.assertEqual(r.returncode, 0, msg="stderr=%s stdout=%s" % (r.stderr, r.stdout))
        self.assertGreater(out.stat().st_size, 20_000)
        flat, pages, n_end = extract_pdf_text(out)
        # cover + 2 body pages + endnotes
        self.assertGreaterEqual(len(pages), 4)
        self.assertEqual(len(pages), 1 + 2 + n_end)
        self.assertIn("Anmerkungen", flat)
        # every shown fid appears on cover AND in endnotes (>=2 occurrences)
        for fid in ("F001", "F002", "F003", "F004", "F005"):
            self.assertGreaterEqual(flat.count(fid), 2, msg=fid)
        # P0-2: placed finding's cover row carries its body page number
        self.assertIn("S. 2", flat)
        # P0-3: distinct sections
        iv = flat.index("Vertragweit geprüft")
        self.assertGreater(flat.index("F003"), iv)
        self.assertIn("Nicht exakt verortet", flat)
        self.assertGreater(flat.index("F004"), flat.index("Nicht exakt verortet"))
        # P1-6: long wording fully present in the endnote (whitespace-normalized)
        norm = " ".join(LONG_WORDING_F001.split())
        self.assertIn(norm.replace("\u201e", "").replace("\u201c", ""),
                      flat.replace("\u201e", "").replace("\u201c", ""))
        # summary line counts contract-wide / unplaced separately
        self.assertIn("1 vertragweit, 1 nicht verortet", " ".join(r.stdout.split()))

    def test_outline_and_links(self):
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest("pypdf unavailable")
        r, out = self.run_cli("links.pdf")
        self.assertEqual(r.returncode, 0)
        reader = PdfReader(str(out))
        named = set(reader.named_destinations.keys())
        # outline: Deckblatt, Seite N, Anmerkungen
        titles = []

        def walk(ol, depth=0):
            for item in ol:
                if isinstance(item, list):
                    walk(item, depth + 1)
                else:
                    titles.append(item.title)
                    if depth == 0 and getattr(item, "children", None):
                        pass
        walk(reader.outline)
        self.assertIn("Deckblatt", titles)
        self.assertIn("Anmerkungen", titles)
        self.assertTrue(any(t.startswith("Seite ") for t in titles))
        # zero dangling link destinations
        for page in reader.pages:
            annots = page.get("/Annots") or []
            for a in annots:
                obj = a.get_object()
                dest = obj.get("/Dest")
                if dest is None and obj.get("/A"):
                    dest = obj["/A"].get_object().get("/D")
                if isinstance(dest, str):
                    self.assertIn(dest, named, msg="dangling dest %s" % dest)

    def test_smoke_min_severity(self):
        r, out = self.run_cli("min.pdf", ["--min-severity", "HIGH"])
        self.assertEqual(r.returncode, 0, msg=r.stderr)
        flat, pages, n_end = extract_pdf_text(out)
        # rank(HIGH)=1 keeps Critical+High only; Medium/Low are filtered document-wide
        self.assertNotIn("F003", flat)
        self.assertNotIn("F005", flat)
        self.assertNotIn("F004", flat)      # Medium rank 2 > HIGH rank 1 (spec §1)
        self.assertIn("F001", flat)
        self.assertIn("F002", flat)
        # unknown-severity survival is exercised separately below

    def test_unknown_severity_survives_critical_filter(self):
        rep = json.loads(self.REPORT.read_text(encoding="utf-8"))
        rep["findings"].append({"id": "F900", "severity": "Blocker", "confidence": "high",
                                "category": "Klausel",
                                "issue": "Unbekannter Schweregrad bleibt erhalten.",
                                "clause": {"clause_id": "x"}})
        rp = FIXDIR / "report-unknown.json"
        rp.write_text(json.dumps(rep, ensure_ascii=False), encoding="utf-8")
        out = FIXDIR / "unknown.pdf"
        cmd = [sys.executable, str(TOOL), str(rp), str(out)] + [str(p) for p in self.PAGES] \
            + ["--min-severity", "CRITICAL"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        self.assertEqual(r.returncode, 0, msg=r.stderr)
        flat, _, _ = extract_pdf_text(out)
        self.assertIn("F900", flat)
        rp.unlink()

    def test_old_cli_rejected(self):
        # legacy 4-positional invocation must fail loudly (argparse usage error)
        r = subprocess.run(
            [sys.executable, str(TOOL), str(self.REPORT), str(FIXDIR / "p1.png"),
             str(FIXDIR / "p2.png"), "unused-out.pdf"],
            capture_output=True, text=True, timeout=120)
        self.assertNotEqual(r.returncode, 0)
        self.assertNotEqual(r.returncode, -6)
        self.assertIn("usage", (r.stderr + r.stdout).lower())


if __name__ == "__main__":
    unittest.main()
