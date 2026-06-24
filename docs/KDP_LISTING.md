# Amazon KDP Listing Kit — *100 Rules for Writing My Software: The Red Hat Way*

Everything to paste into Kindle Direct Publishing for **both** the Kindle eBook
and the 7×10 paperback. Title stays as built (Red Hat, legal cleared); the
AI-coding-agent audience signal lives here in the **keywords, categories, and
description**, where Amazon search reads it — not on the cover.

Royalty/printing numbers are estimates; **KDP's own calculator at upload is
authoritative.**

---

## 1. Identity fields (both formats)

| Field | Value |
|---|---|
| Title | `100 Rules for Writing My Software` |
| Subtitle | `The Red Hat Way` |
| Author | `Ed Haynes` |
| Series | *(optional)* `100 Rules` — set if more titles are planned |
| Edition number | `1` |
| Publisher / Imprint | `Bard Technical Solutions` *(edit on the copyright page + here if you'd rather list "Independently published")* |
| Language | English |
| Primary audience | Adult; not a children's/teen title |
| Low-content / large-print | No |

**ISBN:** choose **"Get a free KDP ISBN"** for the paperback (Amazon = publisher
of record; the ISBN is not portable to other stores). The Kindle eBook needs no
ISBN — Amazon auto-assigns an ASIN. After KDP issues the paperback ISBN, paste
it into the copyright page (`book/00-front-matter.md`, the `979-8-XXXXXXX-X-X`
placeholder) and rebuild.

---

## 2. Categories (pick 3 at upload; BISAC)

1. `COMPUTERS / Software Development & Engineering / General`
2. `COMPUTERS / Artificial Intelligence / General`
3. `COMPUTERS / Programming / General`

(If KDP offers the newer browse paths: *Computers & Technology → AI & Machine
Learning* and *→ Software Development*.)

## 3. Keywords (7 slots — fill all 7)

```
AI coding agents
AI pair programming
software engineering best practices
prompt engineering for developers
LLM coding workflow
clean code discipline
Claude Code Copilot Cursor
```

Rationale: the cover says "Red Hat Way"; these seven put the book in front of
the people searching for how to *work with AI coding tools*. The last slot
deliberately names the live tools (allowed — they're descriptive search terms).

---

## 4. Description (paste into the KDP "Description" box)

KDP accepts light HTML. Plain-text version below the rule; HTML version under it.

Plain text:

```
Forty-seven years of software discipline, rewritten for the age of AI coding agents.

One hundred numbered rules — the lines you never cross, the gates that hold when memory doesn't, and the crew of five AI roles that run them. Distilled from defense networking, embedded real-time systems, and enterprise open source, and sharpened against the one thing that changed everything: the patience to reach 100% test coverage is no longer human patience.

AI changed the economics of software discipline. The messy work that made teams cut corners — merges, regression suites, the four-hundredth test case, regenerating a README from scratch — is exactly what machines now do well and without getting bored. But out of the box a coding model writes C-grade code, because it learned from most of the code ever published, and most of the code ever published is bad. This book is the discipline you put in front of it.

Inside:
- The hard rules an agent must never break — scan before every commit, never hardcode a secret, never destroy without confirmation.
- The Powell rule: get 90% of the information, then decide.
- Configuration over hardcoding, contract-first testing, 100% line and branch coverage.
- Secret hygiene, immutable tags, versioning, and written memory that survives the session.
- Operating an AI fleet: sizing sprints for first-try success, slicing work, and a small "axiom core" every model carries while the rest pages in on demand.

Each chapter closes with a one-page checklist for the wall by your monitor. Opinionated by design — take what works, fork what doesn't. The short-form rules ship as a companion open-source repository you can drop straight into Claude Code, Copilot, Cursor, or any agent harness.

For working developers, architects, and anyone directing AI to write production code people depend on.
```

HTML (same copy, KDP-safe tags `<b> <i> <ul> <li> <br>`):

```html
<b>Forty-seven years of software discipline, rewritten for the age of AI coding agents.</b><br><br>
One hundred numbered rules — the lines you never cross, the gates that hold when memory doesn't, and the crew of five AI roles that run them. Distilled from defense networking, embedded real-time systems, and enterprise open source, and sharpened against the one thing that changed everything: the patience to reach 100% test coverage is no longer human patience.<br><br>
AI changed the economics of software discipline. The messy work that made teams cut corners — merges, regression suites, the four-hundredth test case — is exactly what machines now do well and without getting bored. But out of the box a coding model writes C-grade code, because it learned from most of the code ever published, and most of it is bad. This book is the discipline you put in front of it.<br><br>
<b>Inside:</b>
<ul>
<li>The hard rules an agent must never break — scan before every commit, never hardcode a secret, never destroy without confirmation.</li>
<li>The Powell rule: get 90% of the information, then decide.</li>
<li>Configuration over hardcoding, contract-first testing, 100% line and branch coverage.</li>
<li>Secret hygiene, immutable tags, versioning, and written memory that survives the session.</li>
<li>Operating an AI fleet: a small axiom core every model carries while the rest pages in on demand.</li>
</ul>
Each chapter closes with a one-page checklist for the wall by your monitor. The short-form rules ship as a companion open-source repository you can drop straight into Claude Code, Copilot, Cursor, or any agent harness.<br><br>
<i>For working developers, architects, and anyone directing AI to write production code people depend on.</i>
```

---

## 5. Paperback interior + cover specs

| Spec | Value |
|---|---|
| Trim size | 7" × 10" |
| Bleed | Yes (0.125" — diagrams/art run to edge) |
| Paper | White |
| Ink | Black & white |
| Interior file | `dist/eds-rules-book-print.pdf` (rebuild before upload) |
| Page count | 196 (12pt body; confirm after rebuild — drives spine) |
| Spine width | pages × 0.002252" ≈ 0.441" at 196pp |
| Cover file | `dist/cover-wrap.pdf` (full wrap, generated by `book/cover.py --pages <N>`) |

Cover regeneration after the final rebuild:

```bash
PAGES=$(python3 -c "from pypdf import PdfReader; \
print(len(PdfReader('book/eds-rules-book-print.pdf').pages))")
python3 book/cover.py --pages "$PAGES"
```

The wrap reserves the lower-right of the back cover for KDP's auto-placed ISBN
barcode — leave it clear.

## 6. Kindle eBook file

| Spec | Value |
|---|---|
| Manuscript | `dist/eds-rules-book.epub` (rebuild before upload) |
| Cover | `dist/cover-ebook.png` (1600×2560) |
| DRM | Author's call — recommend **no DRM** (matches the CC-BY companion ethos) |

Validate the EPUB before upload (KDP runs epubcheck and will reject on errors):

```bash
# one-time: brew install epubcheck   (or: npm i -g epubcheck)
epubcheck dist/eds-rules-book.epub
```

---

## 7. Pricing & royalty (estimates — confirm in KDP)

**Kindle eBook** — 70% royalty band is $2.99–$9.99.
- List **$6.99** → ≈ **$4.86/sale** (70% minus a small delivery fee).

**Paperback** — printing cost (US, B&W, 7×10, 196pp) ≈ $1.00 + 196×$0.012 ≈ **$3.35**.
- 60% royalty: minimum list to break even ≈ $3.00 / 0.60 ≈ **$5.00**.
- List **$14.99** → ≈ $14.99×0.60 − $3.00 ≈ **$5.99/copy**.

Suggested launch: **$6.99 Kindle / $14.99 paperback.** Enroll Kindle in **KDP
Select** only if you want Kindle Unlimited reach and accept 90-day Amazon
exclusivity on the *eBook* (paperback and the CC-BY repo are unaffected).

---

## 8. Upload checklist

Pre-flight (local):
- [ ] Rebuild both artifacts: `python3 book/build.py all`
- [ ] Confirm page count; regenerate covers with `--pages <N>`
- [ ] `epubcheck dist/eds-rules-book.epub` → zero errors
- [ ] Eyeball `dist/cover-ebook.png` and `dist/cover-wrap.pdf` at 100%
- [ ] Paste the KDP-issued paperback ISBN into the copyright page; rebuild PDF

KDP — Kindle eBook:
- [ ] New Title → Kindle eBook → fill §1 identity, §2 categories, §3 keywords
- [ ] Description from §4 · Upload `dist/eds-rules-book.epub` · cover `cover-ebook.png`
- [ ] Preview in the Online Previewer · set price §7 · publish

KDP — Paperback:
- [ ] + Create Paperback (links to the same book) · choose **free KDP ISBN**
- [ ] Print options: 7×10, white paper, B&W, bleed ON, matte or glossy cover
- [ ] Upload interior `dist/eds-rules-book-print.pdf` · cover `dist/cover-wrap.pdf`
- [ ] Run the Print Previewer (fix any margin/bleed flags) · set price · publish

---

*Open question for Eddie:* imprint name — list **Bard Technical Solutions**, the
LLC, or "Independently published"? (Affects copyright page + the KDP Publisher
field; default above is Bard Technical Solutions.)
