# Stage 1 — 选题筛选（Notion 驱动）

从 Notion 选题库选今天要做的题。配置与字段映射见 `references/notion-content-plan.md`；评估维度对齐 `references/editorial-guidelines.md` §5.1 与 `references/commercial-strategy.md` §3。

## 1. 读取候选任务

查询 Data Source `41be78d0-d6d0-818e-a4c5-000bae749918`：

- 按「日期」和「优先级」排序。
- 排除「取消」「已发布」状态。
- 保留每条记录的 **page_id**（用于回填），以及 栏目/日期/优先级/发布主题/状态。

**若 404**：数据库未授权，提示用户「Connections → Claude」，然后停下来等授权，不要自行创造选题。

## 2. 优先级

1. 已到期但仍是「计划/进行中」的（最优先）。
2. 今天的任务。
3. 最近的 P0/P1。
4. P2 按内容价值与传播机会调整。

不因「听起来专业」就判为值得发。宽泛的知识介绍、无冲突/问题/反常识的选题，先找更有传播力的切入角度再启动。

## 3. 八维评估（每个候选打分）

受众相关性 · 传播潜力 · 新鲜度 · 认知价值 · 视觉潜力 · 内容深度 · 商业关联（`product-inventory.md` 是否有真实对应）· 竞争程度。

如果出现更重大的新闻/更高价值选题，可**提出替换建议，但需用户批准**——不为追热点破坏长期定位。

## 4. 记录并汇报

填 `templates/topic-brief.md`，并明确写入 Notion 来源：原记录 page_id、原始选题、栏目、优先级。

向用户简要汇报：
- 选中的 Notion 任务（+ 为什么是它）。
- 预计面向什么读者。
- 主要传播角度。
- 对应商业目标（内容角色 + Product Bridge 方向）。

若无合适任务，回到 `workflows/topic-discovery.md` 找新鲜机会（也需用户认可）。
