# ELITE Visual Guidelines

Load this before Stage 5 (visual production). It translates the reference image `排版参考.jpeg` into actionable design rules, adapted to the ELITE Midnight Sky identity.

Color tokens live in `brand-identity.md`; this file defines how to *use* them.

## 1. What the reference image teaches

The reference (`排版参考.jpeg`) is a magazine-style editorial composition. Its structure, read top to bottom:

1. **Image-led upper section** (~top 40%): a full-bleed photograph in muted/dark tones. The image carries mood and subject, not information.
2. **Typographic lower section** (~bottom 60%): a warm paper field with large, dominant typography, a small amount of supporting text, and near-black ink. High contrast, generous whitespace, minimal information.

The lessons to carry over — **composition, hierarchy, spacing, editorial character** — are:

- **Split-page structure.** Image field on top, type field below. The two halves do different jobs.
- **Image = atmosphere, type = message.** The photograph is not decorative filler, but it also does not carry the argument; the headline does.
- **One dominant typographic element.** There is one big statement, not five competing blocks.
- **Minimal supporting information.** A small amount of secondary text, placed quietly.
- **Print character.** Restraint, ruled lines, editorial type treatment — not social-media gloss.

Do **not** copy the reference's original branding, wording, subject matter, or its cream/paper background. Those are not ELITE.

## 2. Adapting to Midnight Sky

The reference is light-on-dark reversed into dark-on-light. The adaptation:

| Reference element | ELITE adaptation |
|-------------------|------------------|
| Cream paper field | Midnight Sky `#16151D` background |
| Near-black ink text | Warm white `#F2EFE9` primary text |
| Muted print gray | Light gray `#A9A6A0` / muted `#6F6C69` |
| (none — new) | Champagne `#D4AF37` or silver `#C7C5BF` as restrained accent |
| Print texture | Optional very subtle grain on the type field; never a cream/light background |

The print character survives through composition and typography, not through a literal paper color.

## 3. Canvas

- **3:4 portrait** — `1080 × 1440` (Xiaohongshu standard).
- Render at **@2x** (`2160 × 2880`) for export.
- This is the same canvas the existing ELITE carousel pipeline uses; keep it consistent.

## 4. Layout system

### Cover (first image)

Split-page editorial composition:

- **Upper field (~40-45% height):** full-bleed image. Muted, dark-leaning, atmosphere-first. A subject photograph, a screenshot (uncropped, kept in full), or a restrained abstract. No text on top of the image unless it is a deliberate, legible overlay.
- **Lower field (~55-60% height):** Midnight Sky type field. Contains, top to bottom:
  1. A small kicker: the pillar label (`WORLD` / `BUSINESS` / `CAPITAL` / `BUILD`) in small caps or spaced letters, in accent or muted color.
  2. The **cover headline** — the single dominant element. Large, tight leading, warm white.
  3. Supporting copy (one or two short lines): source/author/date, or the one-sentence takeaway.
- **Spacing:** distribute the lower field with generous, even negative space. Do not cram to fill; do not leave a ragged bottom.

### Content slides (carousel body)

- Midnight Sky background throughout.
- One idea per card. No card does two jobs.
- A small structural marker (pillar label or slide index) in accent/muted, kept tiny.
- Body text in warm white, secondary lines in light gray; emphasis via champagne highlight (a half-opacity tint behind a phrase, or an accent-colored key line — not whole-paragraph highlighting).
- Slide text fills toward the bottom naturally; never leave a card half-empty with a big dead gap, and never overflow.

## 5. Typography hierarchy

- **Typeface:** PingFang SC (system). For the Latin/English kicker, a serif or letterspaced small caps reads more "magazine" than a bold sans; a restrained didone-style serif is preferred for pillar labels.
- **Weights:** heavy/medium for headlines, regular for body, light for captions.

| Level | Size (on 1080×1440) | Weight | Color |
|-------|---------------------|--------|-------|
| Kicker / pillar label | ~36px, letterspaced | regular | accent or `muted` |
| Cover headline | ~88-120px | semibold/bold | `warm-white` |
| Section heading (slide) | ~64-84px | semibold | `warm-white` |
| Body | ~40-48px, line-height ~1.7 | regular | `warm-white` |
| Secondary / meta | ~32-36px | regular | `light-gray` |
| Caption / footnote | ~28px | regular | `muted` |

Sizes are starting points, not locks — the headline size wins over everything else. Do not set body text so small it becomes a wall of gray.

## 6. Image direction

- **Editorial photography** (moody, real, imperfect) over glossy stock.
- Muted/dark palettes that sit naturally on Midnight Sky; avoid saturated, busy, or "stock-y" imagery.
- A screenshot may serve as the upper-field image when the post is about a specific source or product — show it fully, uncropped.
- The image sets atmosphere; the headline carries the message. Never rely on the image to convey the argument.

## 7. Do / Don't

**Do:**
- Let the headline dominate.
- Keep one accent color, used sparingly.
- Use generous negative space.
- Keep the split-page structure on covers.

**Don't:**
- ❌ Generic AI-template look: rounded cards, gradients, emoji, drop shadows, sticker badges.
- ❌ Cheap luxury: gold foiling, marble, crown/laurel motifs, "premium" stock clichés.
- ❌ Change `#16151D` to another dark.
- ❌ Decorative borders, frames, or backgrounds around the whole card.
- ❌ Over-highlight body text (whole paragraphs in accent).
- ❌ Type over busy imagery (unreadable = rejected).
