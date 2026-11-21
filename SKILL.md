---
name: elite-rednote-skill
description: ELITE Studio 小红书 editorial engine. Research-driven production of high-judgment Chinese Xiaohongshu content end to end — topic discovery and scoring (with commercial content role), primary-source research and fact-checking, editorial angle development, human-sounding Chinese writing (six-step editing process, 100-point scoring), Midnight Sky editorial visual design and rendered carousel images, Xiaohongshu search optimization, publishing prep, product conversion (Product Bridge / content roles / Product Inventory), and post-publication performance review. Use when producing, planning, improving, or evaluating ELITE Studio Xiaohongshu (小红书/Rednote) content, or when the user asks for a topic, a post, a carousel, a cover, an editorial review, or a commercialization/conversion task under the ELITE brand (four pillars WORLD / BUSINESS / CAPITAL / BUILD).
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
3. **No hard sell, no engagement-begging.** No 引导私信/评论/关注. Editorial content completes itself. Product content may use an honest, natural Product Bridge (`references/commercial-strategy.md`) that references only what `references/product-inventory.md` confirms exists — never a cliffhanger, never a fake promise.
4. **No 标题党.** Titles promise exactly what the post delivers.
5. **Human-sounding Chinese.** Ban AI-style transitions and empty motivation (see `references/editorial-guidelines.md`).
6. **Midnight Sky is fixed.** Primary background is `#16151D`. Never change it or substitute a generic dark.
7. **合规第一.** Follow platform rules; never risk the account for reach (see `references/platform-guidelines.md`).

## The pipeline

The full closed loop: Notion 选题库 → 筛选 → 研究 → 标题 → 写作 → 封面 → 发布 → 回填 → 复盘 → 反哺下一期. For a partial request, start at the relevant stage but always run Stage 8 (QA + audit) before delivering.

| # | Stage | What it produces | Load |
|---|-------|------------------|------|
| 1 | Topic Selection | Scored topic from the Notion plan (or a fresh opportunity) + content role | `workflows/topic-selection.md` + `references/notion-content-plan.md` + `references/commercial-strategy.md` → `templates/topic-brief.md` |
| 2 | Research | Verified facts + tracked sources | `workflows/research.md` + `references/research-standards.md` → `templates/research-notes.md` |
| 3 | Editorial Strategy | Target reader, core question, argument, angle, Product Bridge | `workflows/editorial-strategy.md` + `references/product-inventory.md` → `templates/editorial-brief.md` |
| 4 | Title | 5-direction title options + best pick | `workflows/title-system.md` → `templates/title-options.md` |
| 5 | Writing | The post copy (Chinese) | `workflows/content-production.md` + `references/editorial-guidelines.md` → `templates/carousel.md` / `templates/single-post.md` |
| 6 | Cover + Visual | 3-direction cover concept + rendered PNG cards | `workflows/cover-concepts.md` + `workflows/visual-production.md` + `references/visual-guidelines.md` → `templates/cover-concepts.md` + `templates/visual-spec.md` + `scripts/render_carousel.py` |
| 7 | Optimization | Keywords, hashtags, description | `workflows/optimization.md` + `references/platform-guidelines.md` → `templates/publishing-copy.md` |
| 8 | QA + Pre-Publish Audit | 100-point score + pre-publish verdict | `workflows/quality-assurance.md` + `workflows/pre-publish-audit.md` |
| 9 | Publish + Backfill | Publish package; update the original Notion record | `workflows/publish-and-backfill.md` → `templates/publish-package.md` + `templates/review-record.md` |
| 10 | Performance + Learning | Traffic/commercial learning loop + learning log | `workflows/performance-review.md` + `references/editorial-learning-log.md` |

### Stage 1 — Topic Selection

Read today's candidate tasks from the Notion content plan (`references/notion-content-plan.md`), exclude cancelled/published, prioritize overdue → today → P0/P1, score each on the eight dimensions, and commit to one. Record the source Notion page_id for backfill. If the database is not yet authorized, ask the user to connect it — do not invent topics.

### Stage 2 — Research

Primary sources first, reliable secondary sources for context. Verify every date, number, name, and claim. Separate fact / interpretation / opinion. Record sources so they are traceable.

### Stage 3 — Editorial Strategy

Define target reader, core question, central argument, editorial angle, reader takeaway, why ELITE — and the Product Bridge (real, from `product-inventory.md`).

### Stage 4 — Title

Produce 5 title directions (冲突/反常识/悬念/数字/读者利益), each with click motive + risks, then pick the best. No abstract news titles, no clickbait, no promising what the post doesn't deliver.

### Stage 5 — Writing

Pick the format, then write natural, intelligent Chinese through the six-step editing process. No AI-style transitions, no empty motivation, no bullet fragmentation, no forced conclusion.

### Stage 6 — Cover + Visual

Design 3 cover directions (editorial photography / conceptual / data-financial) — never a generic server-room stock photo — then render the finished carousel as PNG cards.

### Stage 7 — Optimization

Search keywords, hashtags, description — natural, no stuffing. Editorial quality is never sacrificed to the algorithm.

### Stage 8 — QA + Pre-Publish Audit

100-point score + the nine editorial checks + commercial checks + the pre-publish audit (title/cover/content/commercialization). Weak output is revised, not shipped.

### Stage 9 — Publish + Backfill

Output the full publish package. Default: the user confirms and publishes (never auto-publish without authorization). After the user provides the link + data, update the original Notion record: status → 已发布, link, structured 复盘 (未采集 where missing).

### Stage 10 — Performance + Learning

Read the numbers as reach/engagement/business-outcome, write the structured review back, and record reusable learnings in the learning log (facts vs hypotheses). Feed them into the next Stage 1.

## Working files & output location

Save every stage's record to the **user's content working directory or an explicit output folder** — never into this skill's own folders. `SKILL.md`, `references/`, `workflows/`, `templates/`, `examples/`, and `tests/` are instructions and templates, not a scratch space.

The records form a traceable package: `topic-brief` → `research-notes` → `editorial-brief` → `carousel`/`single-post` → `visual-spec` → `publishing-copy`. Keep them together so a later review, correction, or performance review can reopen the chain and trace a claim to its source.

## Quick reference

- Brand identity and color tokens: `references/brand-identity.md`
- Pillars, voice, writing standards: `references/editorial-guidelines.md`
- Visual system (from the reference image): `references/visual-guidelines.md`
- Sourcing and fact-checking: `references/research-standards.md`
- Platform mechanics and metrics: `references/platform-guidelines.md`
- Commercial strategy and Product Bridge: `references/commercial-strategy.md`
- What is actually for sale (Product Inventory): `references/product-inventory.md`
- Notion 选题库 config + field mapping: `references/notion-content-plan.md`
- Reusable learnings (facts vs hypotheses): `references/editorial-learning-log.md`

The reference image `排版参考.jpeg` is the visual source of truth. Do not delete, rename, or modify it.
