#!/usr/bin/env python3
"""Apply the footer (slide number bottom-left, BAE Systems logo bottom-right) to every slide.

Hype has no master slide, so this script plays that role. Re-run it after
adding, removing, or reordering slides, or after changing the theme:

    python3 footer.py            # updates presentation.md and images/footer-NN.svg

Text slides get a placed image, images/footer-NN.svg: a transparent overlay the
size of the slide (placed at size=100%, which maps it 1:1 onto the slide) with
the number and logo drawn in the corners. Slides that already draw an ```svg
diagram can't take a second image, so the number and logo are drawn inside the
diagram (id="slide-number" and id="bae-logo") at the same spots on the slide.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DECK = HERE / "presentation.md"
IMAGES = HERE / "images"
LOGO = IMAGES / "baesystems.svg"

# Slide coordinates: a 1280 x 720 render (measured with `hype render`).
SLIDE_W, SLIDE_H = 1280, 720
LOGO_W, LOGO_H = 688, 106                  # logo artwork units
LOGO_X, LOGO_Y, LOGO_PX_W = 1087, 657, 152 # logo box on the slide
U = LOGO_PX_W / LOGO_W                     # slide px per logo unit
NUM_X = SLIDE_W - LOGO_X - LOGO_PX_W       # left margin mirrors the logo's right margin
NUM_Y = LOGO_Y + 80 * U                    # baseline, level with the logo lettering
NUM_SIZE = 72 * U

# Where Hype fits an ```svg block on the slide.
AREA_X, AREA_Y, AREA_W, AREA_H = 67, 187, 1146, 486

PLACED = re.compile(r"^!\[position=[a-z-]+ size=[\d.]+%\]\((?:baesystems|footer-\d+)\.svg\)\n+", re.M)
LOGO_GROUP = re.compile(r'\n?[ \t]*<g id="bae-logo"[^>]*>.*?</g>(?=\n)', re.S)
NUMBER = re.compile(r'\n?[ \t]*<text id="slide-number"[^>]*>[^<]*</text>(?=\n)')


def front_matter(src):
    end = src.index("\n---\n", 4) + 5
    fm = src[:end]
    get = lambda key, default: (re.search(rf'^{key}:\s*"?([^"\n]+)"?', fm, re.M) or [None, default])[1]
    return end, get("color_foreground", "#808080"), get("font", "sans-serif")


def logo_group(x, y, scale, logo_d):
    return (f'<g id="bae-logo" transform="translate({x:.1f},{y:.1f}) scale({scale:.4f})">'
            f'<rect width="{LOGO_W}" height="{LOGO_H}" fill="#ED1A3B"/>'
            f'<path fill="#FFFFFF" fill-rule="evenodd" d="{logo_d}"/></g>')


def number_text(n, x, y, size, fill, font=None):
    family = f' font-family="{font}"' if font else ""
    return f'<text id="slide-number" x="{x:.1f}" y="{y:.1f}" font-size="{size:.1f}" fill="{fill}"{family}>{n}</text>'


def footer_file(n, logo_d, fill, font):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SLIDE_W} {SLIDE_H}"'
            f' width="{SLIDE_W}" height="{SLIDE_H}">\n'
            f'{number_text(n, NUM_X, NUM_Y, NUM_SIZE, fill, font)}\n'
            f'{logo_group(LOGO_X, LOGO_Y, U, logo_d)}\n</svg>\n')


def diagram_footer(slide, n, logo_d):
    m = re.search(r'<svg viewBox="0 0 ([\d.]+) ([\d.]+)"', slide)
    vw, vh = float(m[1]), float(m[2])
    k = min(AREA_W / vw, AREA_H / vh)
    ox, oy = AREA_X + (AREA_W - vw * k) / 2, AREA_Y + (AREA_H - vh * k) / 2
    to_svg = lambda px, py: ((px - ox) / k, (py - oy) / k)
    nx, ny = to_svg(NUM_X, NUM_Y)
    lx, ly = to_svg(LOGO_X, LOGO_Y)
    return (f'\n  {number_text(n, nx, ny, NUM_SIZE / k, "var(--foreground)")}'
            f'\n  {logo_group(lx, ly, U / k, logo_d)}')


def main():
    src = DECK.read_text()
    fm_end, fill, font = front_matter(src)
    logo_d = re.search(r' d="([^"]+)"', LOGO.read_text())[1]
    slides = src[fm_end:].split("\n\n---\n\n")
    wanted = set()
    for i, slide in enumerate(slides):
        n = i + 1
        lead = "\n" if slide.startswith("\n") else ""
        slide = PLACED.sub("", slide.lstrip("\n"))
        if "```svg" in slide:
            slide = NUMBER.sub("", LOGO_GROUP.sub("", slide))
            slide = slide.replace("\n</svg>", diagram_footer(slide, n, logo_d) + "\n</svg>", 1)
        elif "![" in slide:
            print(f"slide {n}: already has an image or video; no footer added", file=sys.stderr)
        else:
            name = f"footer-{n:02d}.svg"
            (IMAGES / name).write_text(footer_file(n, logo_d, fill, font))
            wanted.add(name)
            slide = f"![position=center size=100%]({name})\n\n{slide}"
        slides[i] = lead + slide
    for old in IMAGES.glob("footer-*.svg"):
        if old.name not in wanted:
            old.unlink()
    DECK.write_text(src[:fm_end] + "\n\n---\n\n".join(slides))
    print(f"{len(slides)} slides numbered")


main()
