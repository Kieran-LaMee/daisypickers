#!/usr/bin/env python3
"""Prepare team photos for the site.

    python3 photos.py     reads photos/<season>/*, writes assets/photos/

Put originals in photos/<season>/, where <season> is the season name in lower
case with a hyphen, e.g. photos/fall-2026/. Loose files in photos/ are skipped.
photos/ holds the full-size originals and is not committed.

Each photo is written twice with macOS `sips`: <n>.jpg at up to 1600px on its
long side, opened on click, and <n>-s.jpg at up to 640px, shown in the grid.
Neither is ever enlarged. Both are stripped of EXIF, XMP and IPTC, which can
carry GPS coordinates and the camera owner. The colour profile is kept. The list of photos per season, with sizes, is written to
assets/photos/index.json, which build.py puts into the page.
"""
import json
import pathlib
import shutil
import struct
import subprocess

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "photos"
OUT = ROOT / "assets" / "photos"
SIZES = {"": 1600, "-s": 640}   # file suffix: longest side in px
QUALITY = 80
IMAGES = {".jpg", ".jpeg", ".png", ".heic"}


def strip_metadata(data):
    """Drop APP1 (EXIF, XMP) and APP13 (IPTC) segments from a JPEG."""
    assert data[:2] == b"\xff\xd8", "not a JPEG"
    out, i = bytearray(data[:2]), 2
    while i < len(data) and data[i] == 0xFF:
        marker = data[i + 1]
        if marker == 0xDA:  # start of scan: the rest is image data
            break
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker not in (0xE1, 0xED):
            out += data[i:i + 2 + length]
        i += 2 + length
    return bytes(out + data[i:])


def size(path):
    """Width and height from the JPEG's frame header."""
    data, i = path.read_bytes(), 2
    while True:
        marker = data[i + 1]
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        if 0xC0 <= marker <= 0xC3:
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + length


def original_size(path):
    out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return [int(line.split()[-1]) for line in out.splitlines()[1:]]


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    index = {}
    for folder in sorted(p for p in SRC.iterdir() if p.is_dir()):
        files = sorted(p for p in folder.iterdir() if p.suffix.lower() in IMAGES)
        if not files:
            continue
        (OUT / folder.name).mkdir()
        index[folder.name] = []
        for n, src in enumerate(files, 1):
            long_side = max(original_size(src))
            for suffix, edge in SIZES.items():
                dest = OUT / folder.name / f"{n}{suffix}.jpg"
                subprocess.run(["sips", "-Z", str(min(edge, long_side)), "-s", "format", "jpeg",
                                "-s", "formatOptions", str(QUALITY), str(src), "--out", str(dest)],
                               check=True, capture_output=True)
                dest.write_bytes(strip_metadata(dest.read_bytes()))
            w, h = size(OUT / folder.name / f"{n}-s.jpg")
            index[folder.name].append([n, w, h])
        print(f"{folder.name}  {len(files)} photos")
    (OUT / "index.json").write_text(json.dumps(index) + "\n")
    total = sum(p.stat().st_size for p in OUT.rglob("*.jpg"))
    print(f"assets/photos  {total / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
