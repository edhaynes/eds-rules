# Face-Cover Creatures — Spec (ep103)

Status: In Progress — assets not yet generated (2026-06-25)

Original critter set that sits over **passersby faces** in the ep103 video, so we
obscure bystanders for privacy **without** copyrighted IP (see coding-rules §0.8 —
no Pokémon/trademarked characters in a *published* episode). Same playful slap-a-
monster-on-the-face gag; zero legal exposure.

These are **original designs**. They MUST NOT resemble any existing franchise
creature closely enough to read as a knock-off (substantial-similarity is its own
IP risk, not just a names problem).

---

## Why four, and why these shapes

Multiple passersby can be on screen at once. Four creatures with **distinct
silhouettes and distinct hues** means each tracked person gets a different face-
cover (assigned by track ID), so the audience can tell two bystanders apart and it
reads as deliberate, not a glitch. Silhouette carries more than color at motion-
blur scale, so the four are shape-first different: round / avian / boxy / blobby.

Four **original cartoon animals** (owl, moose, frog, rabbit). Real animals are
public-domain — only a *specific franchise character* would be an IP problem, and
these are our own designs, so they're clear. The owl deliberately echoes the
project's existing `owl.png` mascot; the frog is a wink at the `frogstation` box.

| # | Animal | Silhouette | Palette | Distinguishing features | Vibe |
|---|--------|-----------|---------|-------------------------|------|
| 1 | **Owl**    | round head, tufted ears (echoes the project mascot) | amber `#E0A52A` + brown | big round spectacled eyes, ear tufts, tiny beak | wise, smug |
| 2 | **Moose**  | broad head crowned by **big palmate antlers** | chocolate `#6B4A2B` + tan muzzle | huge antlers, long droopy snout, dopey grin | lovable galoot |
| 3 | **Frog**   | wide flat head, **eyes bulging on top** | green `#5FA844` + cream throat | googly top-mounted eyes, wide flat mouth, rosy cheeks | chill, smiley |
| 4 | **Rabbit** | small head, **two tall upright ears** | slate-grey `#9AA3AD` + cream | long ears, buck teeth, twitchy whiskers, big eyes | jittery, alert |

Silhouettes are shape-first distinct — tufts / antlers / top-eyes / tall-ears —
so two covers never read as the same critter on a busy frame, even at motion-blur
scale where color washes out. Antlers and ears especially carry from a distance.

---

## Visual style (applies to all four)

- **Flat cartoon, thick uniform outline** (~6px @ 512). No gradients-heavy realism;
  bold shapes read at small size and survive video compression.
- **Front-facing, symmetrical, head-on.** The cover replaces a forward-facing face,
  so the creature looks straight at camera. No 3/4 turns.
- **Big features, high contrast** — one or two dominant features each (the eye, the
  tufts, the bolt, the leaf). Busy detail disappears at overlay scale.
- **Consistent line weight + palette across all four** so the set looks like one
  family, not four clip-art grabs.
- **No text, no logos, no resemblance** to Pikachu/Bulbasaur/etc. — original or it
  doesn't ship.

## Technical / pipeline requirements

- **Format:** 512×512 **PNG with alpha**, fully transparent background.
- **Framing:** head fills ~80% of the canvas, ~10% transparent margin all round, so
  the overlay can scale to a detected head bbox + ~20% padding and fully cover it.
- **Centering:** face centroid at canvas center; the pipeline scales the PNG to the
  YOLO person/head box, so consistent centering keeps every cover aligned.
- **Naming:** `creature_1_owl.png`, `creature_2_moose.png`, `creature_3_frog.png`, `creature_4_rabbit.png` in this directory.
- **One static pose per creature** for v1 (no animation). A subtle 2-frame bob is a
  v2 nice-to-have, not in scope now.
- Deliver a `contact-sheet.png` (all four on a checkerboard alpha bg) for a quick
  visual-verify before they go into the render.

## Production route

- **Owner:** Claudina (design/frontend) specs final art; generation on **Gladius
  (gx10) ComfyUI** or frogstation — FLUX, original prompts, then alpha-cut.
- Generation prompts live alongside the assets as `prompts.md` (one per creature,
  built from the table above) so the look is reproducible.
- Hand-illustration or a vector pass is an acceptable fallback if FLUX can't hold a
  clean transparent edge — these are simple shapes.

## Acceptance

- [ ] 4 × 512² RGBA PNGs, transparent bg, named as above
- [ ] Distinct silhouette **and** hue per the table; one family in style
- [ ] No franchise resemblance (original)
- [ ] `contact-sheet.png` for visual verify
- [ ] Eddie signs off on the look before they go into the ep103 render
