#!/usr/bin/env python3
"""Build the Daisy Pickers site.

    python3 build.py              writes index.html, the page that gets deployed
    python3 build.py --artifact   also writes dist/prototype.html, the controls-on
                                  version in the shape claude.ai artifacts expect

Everything is inlined into one HTML file: the fonts (as base64), the traced
daisy shapes, the season data, the styles and the script. No dependencies
beyond the Python standard library.
"""
import base64
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"

FONTS = [
    ("Barlow Semi Condensed", "BarlowSemiCondensed-Bold.woff2", 700),
    ("Geist", "Geist-Regular.woff2", 400),
    ("Geist", "Geist-Medium.woff2", 500),
    ("Geist Mono", "GeistMono-Regular.woff2", 400),
]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Daisy Pickers softball: every season and who played it.">
<link rel="icon" type="image/svg+xml" href="assets/logos/daisy-a-ink.svg">
<style>[hidden]{display:none!important}html{-webkit-text-size-adjust:100%}</style>
"""


def font_css():
    css = ""
    for family, filename, weight in FONTS:
        data = base64.b64encode((SRC / "fonts" / filename).read_bytes()).decode()
        css += (
            f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:normal;'
            f'font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}\n'
        )
    return css


def render(controls):
    template = (SRC / "template.html").read_text()
    shapes = json.loads((SRC / "shapes.json").read_text())
    shapes = [{k: s[k] for k in ("d", "w", "h", "c")} for s in shapes]
    out = template.replace("/*FONTS*/", font_css())
    out = out.replace("/*SHAPES*/", json.dumps(shapes))
    out = out.replace("/*CONTROLS*/", controls)
    for marker in ("/*FONTS*/", "/*SHAPES*/", "/*CONTROLS*/"):
        assert marker not in out, f"{marker} was not filled in"
    return out


def main():
    # The deployed page: the tuning panel only appears at daisypickers.com/#controls
    page = render("location.hash === '#controls'")
    page = page.replace("<title>Daisy Pickers Hero</title>", "<title>Daisy Pickers</title>", 1)
    head_end = page.index("</style>") + len("</style>")
    html = HEAD + page[:head_end] + "\n</head>\n<body>\n" + page[head_end:].lstrip() + "\n</body>\n</html>\n"
    (ROOT / "index.html").write_text(html)
    print(f"index.html  {len(html):,} bytes")

    if "--artifact" in sys.argv:
        # claude.ai artifacts add their own <html>/<head>/<body>, so this one has none
        dist = ROOT / "dist"
        dist.mkdir(exist_ok=True)
        proto = render("true")
        (dist / "prototype.html").write_text(proto)
        print(f"dist/prototype.html  {len(proto):,} bytes")


if __name__ == "__main__":
    main()
