#!/usr/bin/env python3
"""Generate a synthetic 4-page German employment contract (PNG pages + PDF)
for README demo media.

Pages are drawn from examples/sample-report.json: the F001-F003 clause quotes
appear verbatim in the drawn text, so annotate_contract.py's OCR locate matches
by construction. All data is fictional (Muster GmbH / Erika Mustermann).

Usage: make_demo_contract.py [report.json] [outdir]
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 2480, 3508          # A4 @ 300 DPI
FONT_CANDIDATES = [
    "/usr/share/fonts/TTF/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
]
SIZE = 44                  # pt proven OCR-clean under tesseract -l deu --psm 3
Y_START = 260
Y_STEP = 78
X_LEFT = 200
MAX_CHARS = 78             # keeps text clear of the right gutter callouts


def find_font():
    for p in FONT_CANDIDATES:
        if Path(p).exists():
            return p
    sys.exit("no DejaVuSans found")


def wrap(text):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if len(trial) <= MAX_CHARS:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_page(lines, out_path):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(find_font(), SIZE)
    y = Y_START
    for ln in lines:
        d.text((X_LEFT, y), ln, fill="black", font=font)
        y += Y_STEP
    img.save(out_path)


def main():
    report_path = Path(sys.argv[1] if len(sys.argv) > 1 else "examples/sample-report.json")
    outdir = Path(sys.argv[2] if len(sys.argv) > 2 else "docs/media")
    outdir.mkdir(parents=True, exist_ok=True)

    report = json.loads(report_path.read_text(encoding="utf-8"))
    quotes = {f["id"]: f["clause"]["quote"] for f in report["findings"]
              if f.get("clause", {}).get("quote")}

    pages = [
        # ---- page 1: header + parties + § 1 Laufzeit (F001 quote) ----
        ["Befristeter Arbeitsvertrag",
         "",
         "zwischen",
         "",
         "Muster GmbH, Musterstraße 12, 12345 Musterstadt (Arbeitgeber)",
         "",
         "und",
         "",
         "Frau Erika Mustermann, Musterallee 34, 12345 Musterstadt",
         "(Arbeitnehmerin)",
         "",
         "— Musterdaten, ausschließlich zu Demonstrationszwecken —",
         "",
         "§ 1 Laufzeit des Arbeitsverhältnisses",
         *wrap(quotes["F001"]),
         "Das Arbeitsverhältnis endet ohne weiteres Zutun mit Ablauf der",
         "Befristungsdauer."],
        # ---- page 2: § 3 Vergütung (F002) + § 5 Arbeitszeit (F003) ----
        ["§ 3 Vergütung",
         *wrap(quotes["F002"]),
         "Die Vergütung wird am Ende eines jeden Monats auf ein Konto der",
         "Arbeitnehmerin überwiesen (Musterbank, IBAN DE02 1234 5678 9012).",
         "",
         "§ 5 Arbeitszeit",
         *wrap(quotes["F003"]),
         "Die Arbeitnehmerin kann ihre tägliche Arbeitszeit im Rahmen des",
         "betrieblich erforderlichen Umfangs flexibel gestalten."],
        # ---- page 3: weitere Klauseln ----
        ["§ 6 Urlaub",
         "Der Arbeitnehmerin stehen 24 Werktage bezahlter Urlaub pro Kalender-",
         "jahr zu. Urlaub ist im laufenden Kalenderjahr zu nehmen.",
         "",
         "§ 7 Überstunden",
         "Überstunden sind mit dem Bruttomonatsgehalt abgegolten.",
         "",
         "§ 8 Kündigung",
         "Das Arbeitsverhältnis kann mit einer Frist von vier Wochen zum Fünf-",
         "zehnten eines Monats gekündigt werden.",
         "",
         "§ 9 Wettbewerbsverbot",
         "Der Arbeitnehmerin ist für die Dauer von zwei Jahren nach Beendigung",
         "des Arbeitsverhältnisses jede konkurrierende Tätigkeit verboten."],
        # ---- page 4: salvatorische Klausel + Unterschriften ----
        ["§ 10 Salvatorische Klausel",
         "Sollte eine Bestimmung dieses Vertrages unwirksam sein oder werden,",
         "wird die Wirksamkeit der übrigen Bestimmungen hiervon nicht berührt.",
         "",
         "Musterstadt, den 1. September 2026",
         "",
         "",
         "_________________________          _________________________",
         "Muster GmbH                        Erika Mustermann",
         "(Arbeitgeber)                      (Arbeitnehmerin)"],
    ]

    for i, lines in enumerate(pages, 1):
        draw_page(lines, outdir / f"pg-{i:02d}.png")
        print(outdir / f"pg-{i:02d}.png")


if __name__ == "__main__":
    main()
