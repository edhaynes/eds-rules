#!/usr/bin/env python3
"""Extract spoken-text-only prose from an episode .md.

Keeps only the words Eddie would say: strips '#' headers, '[CARD: ...]' cues,
'---' horizontal rules, the front-matter (Author/Delivery/bullet) block, and
everything from the '### Notes' block onward. Output is plain prose paragraphs
separated by blank lines.
"""
import sys
from pathlib import Path


def extract(md_text: str) -> str:
    lines = md_text.splitlines()
    out: list[str] = []
    in_notes = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("### Notes"):
            in_notes = True
            continue
        if in_notes:
            continue
        if not stripped:
            out.append("")
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("[CARD:"):
            continue
        if stripped == "---":
            continue
        if stripped.startswith("Author:") or stripped.startswith("Delivery:"):
            continue
        if stripped.startswith("- GOOD:") or stripped.startswith("- BAD:"):
            continue
        if stripped.startswith("Each episode pairs") or stripped.startswith("(bottom)"):
            continue
        out.append(stripped)
    # collapse multiple blank lines into single, trim ends
    prose: list[str] = []
    prev_blank = True
    for line in out:
        if line == "":
            if prev_blank:
                continue
            prose.append("")
            prev_blank = True
        else:
            prose.append(line)
            prev_blank = False
    return "\n".join(prose).strip() + "\n"


def main() -> None:
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    dst.write_text(extract(src.read_text()), encoding="utf-8")
    print(f"{src.name} -> {dst} ({len(dst.read_text().split())} words)")


if __name__ == "__main__":
    main()
