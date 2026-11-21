# ELITE 小红书 Editorial Engine

A reusable, research-driven editorial production skill for **ELITE Studio** Xiaohongshu (小红书) content. It is not a copywriting prompt — it is a full pipeline that turns a topic into a fact-checked, judgment-driven, brand-consistent post: from topic discovery through research, editorial strategy, writing, visual design, search optimization, quality assurance, and performance review.

Output is **Chinese content**. Instructions are English; every deliverable is Chinese.

## What it does

- **Discovers and scores topics** (originality, relevance, information value, discussion potential, brand fit).
- **Researches** from primary sources and verifies dates, numbers, names, and quotes — never fabricating.
- **Develops a real editorial angle** before writing, so every post carries a point of view the reader can argue with.
- **Writes natural, intelligent Chinese** through a six-step editing process (worth-writing → narrative entry → argument route → draft → three edit rounds → reader simulation) and a 100-point quality score — no AI-style transitions, no empty motivation, no 标题党, no hard sell.
- **Designs and renders editorial visuals** on the fixed Midnight Sky identity — split-page covers and slide cards (`scripts/render_carousel.py`), following the composition of `排版参考.jpeg`.
- **Optimizes for Xiaohongshu search** without keyword stuffing.
- **Converts readers into customers** — content roles (Traffic/Trust/Product/Conversion), an honest Product Bridge, a Product Inventory, and a conversion funnel with commercial metrics.
- **Quality-gates** every deliverable before it ships.
- **Reviews performance** — both traffic and commercial (主页访问率 × 商品点击率 × 成交率) — and feeds learnings back into topic selection and product development.

## Repository structure

```
SKILL.md                     # entry point: 8-stage pipeline + non-negotiables
排版参考.jpeg                 # visual reference (do not modify)
references/                  # deep guidance, loaded on demand
  brand-identity.md          #   Midnight Sky color tokens + voice
  editorial-guidelines.md    #   pillars, angle, writing standards
  visual-guidelines.md       #   reference-image → design rules
  research-standards.md      #   sourcing + fact-checking
  platform-guidelines.md     #   search optimization + metrics
  commercial-strategy.md    #   3-tier value, content roles, Product Bridge, funnel
  product-inventory.md      #   what is actually for sale (source of truth)
  notion-content-plan.md    #   Notion 选题库 config + field mapping
  editorial-learning-log.md #   reusable learnings (facts vs hypotheses)
workflows/                   # stage runbooks (Stages 1-10)
  topic-selection.md         #   Notion-driven topic selection
  topic-discovery.md         #   fresh-opportunity fallback
  research.md
  editorial-strategy.md
  title-system.md            #   5-direction titles
  content-production.md
  cover-concepts.md          #   3-direction covers
  visual-production.md
  optimization.md
  quality-assurance.md
  pre-publish-audit.md       #   pre-publish checks
  publish-and-backfill.md    #   publish package + Notion backfill
  performance-review.md
templates/                   # fill-in output structures
  topic-brief.md  research-notes.md  editorial-brief.md
  carousel.md  single-post.md  visual-spec.md  publishing-copy.md
  title-options.md  cover-concepts.md  publish-package.md  review-record.md
scripts/
  render_carousel.py         # renders carousel.json -> PNG cards (Midnight Sky style)
examples/
  good-examples.md  bad-examples.md
tests/
  evaluation-cases.md
```

## Installation

This is an **Agent Skill**: a folder containing a `SKILL.md` entry point with `name` and `description` frontmatter, plus modular reference files that are loaded as needed (progressive disclosure).

- **Claude Code** — place the folder in the skills directory and the `SKILL.md` is discovered via its frontmatter. For a per-user install, clone to `~/.claude/skills/elite-rednote-skill/`; for a project-scoped install, clone to `.claude/skills/elite-rednote-skill/` inside the working repo.
- **Other agents** — any agent that loads `SKILL.md`-format skills (frontmatter `name` + `description`) can use this folder directly. Compatibility with a specific agent has only been verified where that agent documents `SKILL.md` discovery; do not claim compatibility beyond what that agent supports.

The content pipeline has no dependencies. Rendering PNG cards via `scripts/render_carousel.py` additionally requires **Google Chrome** (used headless) on the machine.

## Usage

Invoke the skill when producing, planning, improving, or evaluating ELITE Xiaohongshu content. The agent follows `SKILL.md`:

1. **Full production** — run the eight stages in order. Each stage loads its workflow + reference files and fills its template.
2. **Partial request** — start at the relevant stage (a topic, a draft, a cover, an audit), but always run Stage 7 (QA) before delivering anything.

The stages: Topic Discovery → Research → Editorial Strategy → Writing → Visual Production → Optimization → Quality Assurance → Performance Review.

## Brand reference (quick)

- **Primary background:** Midnight Sky `#16151D` (PANTONE 20-0195 TPM; RGB 22, 21, 29). Fixed.
- **Type:** warm white `#F2EFE9` (primary), light gray `#A9A6A0` (secondary), muted `#6F6C69` (captions).
- **Accent:** champagne `#D4AF37` (default), metallic silver `#C7C5BF` (alternative), used sparingly.
- **Pillars:** WORLD · BUSINESS · CAPITAL · BUILD (extensible).

Full spec in `references/brand-identity.md`.

## Validation

The skill ships with `tests/evaluation-cases.md` — nine cases covering scoring, angle rejection, AI-flavor removal, visual tokens, optimization, the QA gate, fabrication refusal, and an end-to-end run. Run them after any change to confirm the skill still produces the right behavior.
