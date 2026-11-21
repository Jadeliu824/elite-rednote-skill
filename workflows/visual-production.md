# Stage 5 — Visual Production

Translate the written content into a visual spec: cover concept, cover headline, and slide-by-slide design instructions. Rules are in `references/visual-guidelines.md` and `references/brand-identity.md`; this is the procedure.

## 1. From brief to cover concept

Take the `editorial-brief` (central argument + angle) and decide:

- **Cover headline** — the single dominant line. It is the argument compressed, not a slogan. It must survive being read in one second.
- **Upper-field image** — what atmosphere serves the argument: a subject photograph, a full screenshot (uncropped) of the source, or a restrained abstract. Muted/dark-leaning; it sets mood, it does not carry the argument.
- **Kicker** — the pillar label (`WORLD` / `BUSINESS` / `CAPITAL` / `BUILD`), small and letterspaced.
- **Supporting copy** — one or two quiet lines (source/author/date, or the one-sentence takeaway).

## 2. Compose the layout

Follow the split-page structure from `visual-guidelines.md` §4:

- Image field ~40-45% height, full-bleed, no unreadable text on top.
- Midnight Sky type field below: kicker → headline → supporting copy, distributed with generous even spacing.
- One dominant typographic element (the headline). No competing blocks.

## 3. Slide-by-slide (carousel only)

For each content card, specify:

- The card's single idea (from `templates/carousel.md`).
- Section heading, body, and any emphasis (champagne highlight on a phrase, or an accent key line — never a whole paragraph).
- The small structural marker (pillar label or slide index).

Every card inherits Midnight Sky, the type hierarchy, and the accent rules. No card introduces a new color or layout.

## 4. Apply the tokens exactly

Use the tokens from `brand-identity.md` §2 verbatim. Never approximate a color. `#16151D` is the background; `#F2EFE9` primary text; `#D4AF37`/`#C7C5BF` accents used sparingly.

## 5. Record the spec

Fill `templates/visual-spec.md`: cover concept, cover headline, supporting copy, image direction, layout instructions, type hierarchy, and exact color values — plus slide-by-slide instructions for carousels. This spec is what a designer or image-generation step executes against; it must be unambiguous.
