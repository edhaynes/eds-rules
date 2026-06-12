Status: Ready for Claudina — 2026-06-12

# Brief: visual production — plates, EPUB QA, proof checks, cover spec

Context: PLAN_agent-assignments.md; the placeholder line-art plates in
`book/art/` (title-page crew + 5 chapter dividers, swap-by-filename).

1. **Plate generation specs:** for each of the six pieces, a ComfyUI prompt
   + negative prompt + composition notes (B&W pen-and-ink, no shading
   gradients that die in print, portrait ~3:4 for the divider slot which
   letterboxes `width 100% × height 62%, fit: contain`). Themes: the crew;
   the gate (first principles); the portico (design); the crane (build); the
   shield (protect/prove); the boat + v1.0 tag (ship/remember). Deliver as
   `plans/DESIGN_plates.md` for Eddie to run on his ComfyUI box.
2. **EPUB QA:** open `dist/eds-rules-book.epub` in Kindle Previewer (or
   epubcheck at minimum) — flag SVG support issues (plates + 30 diagrams),
   TOC, chapter splits, metadata. Cross-platform is non-negotiable: note
   anything that renders differently across Kindle/Apple Books/Calibre.
3. **Proof checks (bugs.md B6):** Rule 13 sprint-lanes diagram and the
   widest flowcharts at 7"×10" trim — verify legibility at print size, list
   any that need redrawing narrower.
4. **Cover spec:** 7"×10" KDP cover requirements (spine width at ~137 B&W
   pages, bleed, barcode zone) + a layout brief consistent with the interior
   line-art style. Title treatment carries the disclaimer constraint (the
   trademark answer may rename the subtitle — keep the title block
   swappable).

Acceptance: Eddie can generate plates and approve a cover direction without
further research; every QA finding filed to bugs.md with repro.
