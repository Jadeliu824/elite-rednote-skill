---
name: elite-rednote-skill
description: ELITE Studio 小红书 editorial engine. Research-driven production of high-judgment Chinese Xiaohongshu content end to end — topic discovery and scoring, primary-source research and fact-checking, editorial angle development, human-sounding Chinese writing, Midnight Sky editorial visual design, Xiaohongshu search optimization, publishing prep, and post-publication performance review. Use when producing, planning, improving, or evaluating ELITE Studio Xiaohongshu (小红书/Rednote) content, or when the user asks for a topic, a post, a carousel, a cover, or an editorial review under the ELITE brand (four pillars WORLD / BUSINESS / CAPITAL / BUILD).
---

# ELITE 小红书 Editorial Engine

A reusable, research-driven editorial production system. Not a copywriting prompt: a full pipeline that turns a topic into a fact-checked, judgment-driven, brand-consistent Xiaohongshu post.

Output is always **Chinese content** for ELITE Studio (小红书 主阵地). Instructions and procedures in this skill are English; every deliverable is Chinese.

## When to use

- The user asks for a new ELITE 小红书 post, carousel, cover, or topic.
- The user asks to plan, improve, or audit ELITE content.
- The user pastes raw material (a podcast, article, screenshot, note) and wants it turned into a post.
- The user asks "is this worth posting" or "why did this post underperform".

Not for: generic non-ELITE Xiaohongshu content, other platforms, or pure image editing with no editorial intent.

## Non-negotiables (apply to every stage)

1. **Never fabricate.** No invented sources, quotes, statistics, names, or case studies. If you cannot verify it, drop it or say so.
2. **Judgment over aggregation.** Every post must contain a point of view the reader can argue with. Summaries are not content.
3. **No CTA, no hard sell.** No 引导私信/评论/关注, no 硬广. Let the content do the work.
4. **No 标题党.** Titles promise exactly what the post delivers.
5. **Human-sounding Chinese.** Ban AI-style transitions and empty motivation (see `references/editorial-guidelines.md`).
6. **Midnight Sky is fixed.** Primary background is `#16151D`. Never change it or substitute a generic dark.
7. **合规第一.** Follow platform rules; never risk the account for reach (see `references/platform-guidelines.md`).

## The pipeline

Run the eight stages in order for a full production. For a partial request, start at the relevant stage but still run Stage 7 (QA) before delivering anything.

| # | Stage | What it produces | Load |
|---|-------|------------------|------|
| 1 | Topic Discovery | A scored, justified topic decision | `workflows/topic-discovery.md` → `templates/topic-brief.md` |
| 2 | Research | Verified facts + tracked sources | `workflows/research.md` + `references/research-standards.md` → `templates/research-notes.md` |
| 3 | Editorial Strategy | Target reader, core question, argument, angle | `workflows/editorial-strategy.md` → `templates/editorial-brief.md` |
| 4 | Writing | The post copy (Chinese) | `workflows/content-production.md` + `references/editorial-guidelines.md` → `templates/carousel.md` or `templates/single-post.md` |
| 5 | Visual Production | Cover + slide/image design instructions | `workflows/visual-production.md` + `references/visual-guidelines.md` → `templates/visual-spec.md` |
| 6 | Optimization | Title, keywords, hashtags, description | `workflows/optimization.md` + `references/platform-guidelines.md` → `templates/publishing-copy.md` |
| 7 | Quality Assurance | Pass / revise / reject verdict | `workflows/quality-assurance.md` |
| 8 | Performance Review | Learning loop back into Stage 1 | `workflows/performance-review.md` |

### Stage 1 — Topic Discovery

Find candidates (emerging developments, strong sources, reader questions), then score each on **originality, relevance, information value, discussion potential, brand fit** (rubric in `workflows/topic-discovery.md`). Reject repetitive or low-value topics. Output a `topic-brief` with the decision and its rationale.

### Stage 2 — Research

Primary sources first, reliable secondary sources for context. Verify every date, number, name, and claim. Separate fact / interpretation / opinion. Record sources so they are traceable. Stop researching when the argument is supported — do not collect for its own sake.

### Stage 3 — Editorial Strategy

Before writing, define: **target reader, core question, central argument, editorial angle, reader takeaway, and why ELITE should publish this.** A topic without a clear angle is rejected here, not rescued in writing.

### Stage 4 — Writing

Pick the right format (single image, carousel, essay, case study, commentary, framework, building-in-public update), then write natural, intelligent Chinese: strong opening, clear progression, specific examples, real reasoning. No AI-style transitions, no empty motivation, no bullet fragmentation, no forced conclusion.

### Stage 5 — Visual Production

Translate the brief into a visual spec: cover concept, cover headline, supporting copy, image direction, layout, type hierarchy, and exact color tokens. Follow the ELITE visual system (Midnight Sky + editorial composition from the reference image). Slide-by-slide content when it is a carousel.

### Stage 6 — Optimization

Optimize the title for readability **and** search intent, identify search keywords, prepare hashtags, write the description. No keyword stuffing; editorial quality is never sacrificed to the algorithm.

### Stage 7 — Quality Assurance

Evaluate the deliverable against the QA checklist (factual accuracy, source quality, argument, originality, reader value, narrative, brand consistency, visual consistency, platform suitability). Weak output is revised, not shipped. See `workflows/quality-assurance.md`.

### Stage 8 — Performance Review

After publishing, collect reach (impressions, views, CTR), engagement (likes, saves, comments, shares), and business outcomes (profile visits, leads) — and treat them as three different things. Convert findings into concrete changes for the next Stage 1, rather than chasing traffic blindly.

## Working files & output location

Save every stage's record to the **user's content working directory or an explicit output folder** — never into this skill's own folders. `SKILL.md`, `references/`, `workflows/`, `templates/`, `examples/`, and `tests/` are instructions and templates, not a scratch space.

The records form a traceable package: `topic-brief` → `research-notes` → `editorial-brief` → `carousel`/`single-post` → `visual-spec` → `publishing-copy`. Keep them together so a later review, correction, or performance review can reopen the chain and trace a claim to its source.

## Quick reference

- Brand identity and color tokens: `references/brand-identity.md`
- Pillars, voice, writing standards: `references/editorial-guidelines.md`
- Visual system (from the reference image): `references/visual-guidelines.md`
- Sourcing and fact-checking: `references/research-standards.md`
- Platform mechanics and metrics: `references/platform-guidelines.md`

The reference image `排版参考.jpeg` is the visual source of truth. Do not delete, rename, or modify it.
