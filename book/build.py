#!/usr/bin/env python3
"""Build the book: render Mermaid diagrams to B&W PNG, assemble EPUB + print PDF.

Usage: python3 book/build.py [epub|pdf|all]   (default: all)

Requires on PATH: mmdc (@mermaid-js/mermaid-cli), pandoc, typst.
Outputs to dist/: eds-rules-book.epub, eds-rules-book-print.pdf
"""

import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent
REPO_ROOT = BOOK_DIR.parent
BUILD_DIR = BOOK_DIR / "_build"
DIAGRAM_DIR = BUILD_DIR / "diagrams"
DIST_DIR = REPO_ROOT / "dist"

SOURCES = [
    "00-front-matter.md",
    "ch01.md",
    "ch02.md",
    "ch03.md",
    "ch04.md",
    "ch05.md",
    "99-back-matter.md",
]

METADATA = {
    "title": "100 Rules for Writing My Software",
    "subtitle": "The Red Hat Way",
    "author": "Ed Haynes",
    "lang": "en-US",
    "rights": "Book text (c) Ed Haynes. Underlying rules repo CC-BY-4.0.",
}

# B&W print constraint: neutral theme renders in grayscale; scale 2 keeps
# diagrams crisp at 6"x9" trim.
MMDC_ARGS = ["-t", "neutral", "-b", "white", "-s", "2"]
PAPERSIZE = "us-trade"  # typst built-in 6"x9"

MERMAID_BLOCK = re.compile(r"^```mermaid\n(.*?)^```\n", re.M | re.S)


def require(tool: str) -> str:
    path = shutil.which(tool)
    if not path:
        sys.exit(f"error: required tool not on PATH: {tool}")
    return path


def render_diagram(source: str, name: str) -> Path:
    """Render one Mermaid block to PNG; skip if source unchanged."""
    digest = hashlib.sha256(source.encode()).hexdigest()[:12]
    mmd = DIAGRAM_DIR / f"{name}.mmd"
    png = DIAGRAM_DIR / f"{name}.png"
    stamp = DIAGRAM_DIR / f"{name}.{digest}.ok"
    if png.exists() and stamp.exists():
        return png
    mmd.write_text(source)
    subprocess.run(
        ["mmdc", "-i", str(mmd), "-o", str(png), *MMDC_ARGS],
        check=True, capture_output=True, text=True,
    )
    for old in DIAGRAM_DIR.glob(f"{name}.*.ok"):
        old.unlink()
    stamp.write_text("")
    return png


def preprocess(src: Path) -> Path:
    """Replace mermaid blocks with rendered-image references."""
    text = src.read_text()
    stem = src.stem
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        count += 1
        name = f"{stem}-d{count:02d}"
        png = render_diagram(match.group(1), name)
        return f"![]({png.relative_to(BUILD_DIR)})\n"

    out = BUILD_DIR / src.name
    out.write_text(MERMAID_BLOCK.sub(replace, text))
    print(f"  {src.name}: {count} diagram(s)")
    return out


def pandoc(processed: list[Path], target: Path, extra: list[str]) -> None:
    meta = [f"--metadata={k}:{v}" for k, v in METADATA.items()]
    subprocess.run(
        ["pandoc", *map(str, processed), "-o", str(target),
         "--toc", "--toc-depth=2", "--resource-path", str(BUILD_DIR),
         *meta, *extra],
        check=True,
    )
    print(f"built {target.relative_to(REPO_ROOT)} ({target.stat().st_size // 1024} KB)")


def main() -> None:
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target not in ("epub", "pdf", "all"):
        sys.exit(f"error: unknown target {target!r} (epub|pdf|all)")
    for tool in ("mmdc", "pandoc", "typst"):
        require(tool)
    DIAGRAM_DIR.mkdir(parents=True, exist_ok=True)
    DIST_DIR.mkdir(exist_ok=True)

    print("rendering diagrams + preprocessing:")
    processed = [preprocess(BOOK_DIR / name) for name in SOURCES]

    if target in ("epub", "all"):
        pandoc(processed, DIST_DIR / "eds-rules-book.epub",
               ["--split-level=1"])
    if target in ("pdf", "all"):
        pandoc(processed, DIST_DIR / "eds-rules-book-print.pdf",
               ["--pdf-engine=typst", f"--variable=papersize:{PAPERSIZE}"])


if __name__ == "__main__":
    main()
