Status: In Progress — 2026-06-23

# PLAN — Amazon KDP publication (Kindle + paperback)

Get *100 Rules for Writing My Software: The Red Hat Way* onto Amazon KDP as a
Kindle eBook **and** a 7×10 paperback. Title stays as built (legal cleared the
Red Hat trademark, 2026-06-23, Eddie). AI-coding-agent discoverability rides in
the KDP metadata, not the cover.

## Decisions (Eddie, 2026-06-23)
- Formats: **both** Kindle + paperback.
- Title: **keep "The Red Hat Way"** (reversed the AI-reframe after legal cleared).
- Cover: **author-generated** (typographic, Pillow; no fedora logo).
- ISBN: **free KDP-assigned** paperback ISBN; Kindle uses ASIN.

## Sprints
1. **Copyright page** — added to `book/00-front-matter.md` (©, edition, rights,
   CC-BY note, ISBN placeholder, imprint). ✅ done.
2. **Cover generator** — `book/cover.py` → `dist/cover-ebook.png` (1600×2560)
   and `dist/cover-wrap.{png,pdf}` (full wrap, spine from page count). ✅ built;
   ⏳ needs Eddie's visual sign-off (Rule: visual work isn't done until a human
   eyeballs the render).
3. **KDP listing kit** — `docs/KDP_LISTING.md`: identity, 3 categories, 7
   keywords, description (plain + HTML), pricing/royalty, upload checklist. ✅ done.
4. **Rebuild + validate** — rebuilt EPUB + 165pp PDF with the copyright page;
   covers regenerated at 165pp (spine 0.372"); **epubcheck → 0 errors / 0
   warnings** (EPUB 3.3). ✅ done.
5. **Commit + push** — committed locally (98a9607); stable cycle (1.4.6,
   even-minor) → **confirm before push**. ⏳ awaiting Eddie's go.

## Open questions
- Imprint: "Bard Technical Solutions" (default) vs the LLC vs "Independently
  published"? Affects copyright page + KDP Publisher field.
- Cover art direction: typographic draft only so far — keep, or commission/AI a
  pictorial cover? Eddie to view `dist/cover-ebook.png`.
- KDP Select (Kindle Unlimited + 90-day eBook exclusivity)? Default: no.

## Done-signal
Both artifacts validate, covers approved, KDP draft filled per the kit, ISBN
folded back into the copyright page, books published.
