# ELITE Product Inventory

The single source of truth for what ELITE can honestly sell. Before any Product Bridge or product CTA, consult this file. **Content may only reference products and features that are listed here as 已存在 (exists) and verified.**

## Schema

| Field | Meaning |
|-------|---------|
| 产品名称 | product name |
| 产品类型 | knowledge base / digital product / other |
| 产品状态 | 已存在 / 开发中 / 待验证 |
| 实际内容与功能 | what it actually contains (catalog, features) |
| 对应栏目 | WORLD / BUSINESS / CAPITAL / BUILD |
| 适用人群 | who it is for |
| 可宣传价值 | the value that may truthfully be advertised |
| 购买入口 | product page / purchase link |
| 最后核验日期 | when the above was last verified against the real product |

## Rules

- **已存在** entries: only advertise the content listed under 实际内容与功能. Do not invent a catalog, case, feature, or update promise.
- **开发中 / 待验证** entries: may be *mentioned* only with that status ("正在整理"), never described as available.
- **待核验** (this file's current state): treat as unverified. Do **not** reference specifics in a Product Bridge. Write "无直接产品关联" until the entry is filled and dated.
- Update 最后核验日期 whenever the real product changes.

## Inventory

> ⚠️ **待填充 — fill this with real product data before using Product Bridge.** The entries below are placeholders from the brand's known direction; their content has not been verified against the live knowledge base. Until each is filled and dated, Product Bridge must not cite them specifically.

| 产品名称 | 类型 | 状态 | 实际内容与功能 | 对应栏目 | 适用人群 | 可宣传价值 | 购买入口 | 最后核验 |
|---------|------|------|----------------|---------|---------|-----------|---------|---------|
| ELITE 策展（curated insights） | 知识库 | 待核验 | （待填真实目录/专题） | BUSINESS / CAPITAL | （待填） | （待填） | （待填） | — |
| 人生操作系统（life operating system） | 知识库 | 待核验 | （待填真实目录/框架） | BUILD | （待填） | （待填） | （待填） | — |

## How the workflow uses this

`workflows/topic-discovery.md` records the content role; the Product Bridge step (in `workflows/content-production.md` / `editorial-strategy.md`) checks this inventory. If no 已存在 entry matches the note's topic, the Product Bridge is "无直接产品关联" and there is no product CTA.
