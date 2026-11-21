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

> **核验记录（2026-11-21，Notion MCP 直读）：** 知识库真实存在，结构完整。workspace「ELITE Studio」，首页即知识库，含「使用指南」+ 7 大分类，每类下挂数据库。**定价 ¥169，走小红书 personal sale（私域直接成交）**；部分分类的数据库名仍是占位（`New database`：101/102/104/106/107）。

**产品定位**（使用指南原话）：一套按主题整理的知识与资源库——深度阅读、创作者观点、实用工具、信息源、书籍、思维模型、专题合集。「按问题检索，或沿专题路径阅读」「价值不在收藏了多少，而在帮你更快找到线索、建立联系、形成自己的判断」。

| 产品名称 | 类型 | 状态 | 实际内容与功能 | 对应栏目 | 适用人群 | 可宣传价值 | 购买入口 | 最后核验 |
|---------|------|------|----------------|---------|---------|-----------|---------|---------|
| ELITE Studio 知识库（Notion） | 知识库 | 已存在（¥169） | 使用指南 + 101 深度阅读 / 102 创作者精华 / 103 实用工具 / 104 信息源 / 105 书籍推荐 / 106 思维模型 / 107 专题合集 | WORLD（深度阅读/信息源）· BUSINESS（深度阅读/专题）· CAPITAL（深度阅读/思维模型）· BUILD（实用工具/思维模型） | 想理解商业/科技/社会议题、找工具与思维模型、持续追踪领域的读者 | 真实存在的 7 分类知识库；按问题检索 + 专题路径 + 判断转化 | 小红书 personal sale · ¥169 | 2026-11-21 |

## 栏目 → 知识库映射（用于 Product Bridge）

| 内容栏目 | 可自然桥接到的真实分类 |
|---------|------------------------|
| WORLD | 101 深度阅读 · 104 信息源 · 107 专题合集 |
| BUSINESS | 101 深度阅读 · 107 专题合集 · 103 实用工具 |
| CAPITAL | 101 深度阅读 · 106 思维模型 · 107 专题合集 |
| BUILD | 103 实用工具 · 106 思维模型 |

## 当前可做 / 不可做

- ✅ **可做**：Trust 内容自然桥接（「关于估值逻辑，我在 ELITE 知识库的深度阅读/思维模型里整理了更系统的研究」）；Product 内容真实展示 7 分类目录；Conversion 内容明确引导购买（¥169，小红书 personal sale）。
- ⚠️ **合规**：personal sale 属私域交易，须遵守小红书当期导流/交易规则，发布前核查。

## How the workflow uses this

`workflows/topic-discovery.md` records the content role; the Product Bridge step (in `workflows/content-production.md` / `editorial-strategy.md`) checks this inventory. If no 已存在 entry matches the note's topic, the Product Bridge is "无直接产品关联" and there is no product CTA.
