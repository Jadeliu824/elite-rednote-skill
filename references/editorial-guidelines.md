# ELITE Editorial Guidelines

How ELITE chooses, frames, and writes content. Load this before Stage 3 (strategy) and Stage 4 (writing).

## 1. Editorial pillars

Four pillars organize the content. They are a starting taxonomy, not a straitjacket — if a topic fits better somewhere else, extend the taxonomy rather than force the topic.

### WORLD — 世界
Global affairs, technology, culture, society, international perspectives, emerging trends. What is changing in the world and why it matters to a Chinese founder/reader. Not news headlines: the underlying shift and its second-order consequences.

Example territory: a technology inflection point, a geopolitical development's effect on markets or building, a cultural trend that changes how products are made.

### BUSINESS — 商业
Business models, entrepreneurship, companies, marketing, sales, strategy, organizational dynamics. How businesses are built, won, and lost. Concrete decisions and mechanisms over abstract "management wisdom."

Example territory: a founder's specific decision and its outcome, a pricing or go-to-market model, a company's structural advantage.

### CAPITAL — 资本
Financial markets, investing, capital allocation, wealth creation, financial decision-making. How capital thinks and moves. Frameworks and second-order effects over market commentary.

Example territory: an investor's decision framework, a capital-allocation lesson, how a financing structure shapes incentives.

### BUILD — 构建
Real projects, personal experiments, knowledge systems, product development, building in public. First-person making — the inside view of building, including ELITE's own work. This is the pillar where 日记层 (diary) content naturally lives.

Example territory: a product decision being made now, a system being built, a build-in-public update with a real lesson.

**Extensibility rule:** when a topic spans pillars, pick the one whose question the post actually answers. When none fits, propose a new pillar name and scope before using it — do not silently jam the topic in.

## 2. Content layers (cross-cutting)

Orthogonal to pillars, every piece is one of three layers. Keep the mix deliberate: evergreen is the backbone.

- **常青层 (evergreen) — ~55%.** Judgment and frameworks that stay useful for months. The durable asset.
- **时效层 (timely) — ~30%.** A current event or fresh development, filtered through judgment. Must still say something that outlasts the news cycle.
- **日记层 (diary) — ~15%.** First-person building updates. Personal experience is texture, never the primary content; do not turn it into a sales channel.

## 3. Editorial philosophy

Eight operating principles, distilled from the brand:

1. Quality over quantity.
2. Editorial judgment over generic AI generation.
3. Original thinking over content aggregation.
4. Evidence over unsupported claims.
5. Human-sounding writing over AI-style templates.
6. Brand consistency over short-term visual trends.
7. Reusability over one-off prompts.
8. Practical execution over theoretical documentation.

In practice, these mean: a post is a **claim, supported by evidence, argued with a point of view** — not a list of facts, not a summary, not a collection of quotes.

## 4. Developing an angle

A topic is not yet content. Before writing, the angle must pass these tests:

- **The "so what" test.** Why does this deserve attention *now*, from *this* reader?
- **The tension test.** Is there something to argue with? A counterintuitive claim, a disagreement, a "here's what people get wrong"? Consensus and "correct but boring" both fail.
- **The originality test.** Would a competent summary of the same source produce the same post? If yes, it is aggregation, not ELITE content.
- **The judgment test.** Is there a place for the creator's own view — "如果是我会怎么做" / "我不同意" / "普遍解读漏掉了关键"? If the creator has nothing to add, the topic is not ready.

The output of passing these tests is captured in `templates/editorial-brief.md`.

## 5. Writing standards (Chinese)

The deliverable is natural, intelligent Chinese. These rules are mandatory.

### 5.1 去 AI 味 — highest priority

Banned words and patterns (do not use):

- ❌ 开场套话："在当今时代""随着……的发展""众所周知""不可否认""总而言之"
- ❌ 空洞强调："值得注意的是""令人惊叹的是""毋庸置疑""从某种角度来说""不可否认"
- ❌ 术语堆砌："赋能""迭代""底层逻辑""颗粒度""维度""闭环""抓手""心智""私域""复盘" (when used as decoration)
- ❌ 万能句式："这是一个……的过程""体现了一种……""本质上是……""归根结底"
- ❌ 每段以"首先/其次/最后/此外/另外"开头
- ❌ 结尾强行升华、鸡汤收尾、重复开头的"人工结论"

Allowed and encouraged:

- ✅ 像在对话："说实话""有意思的是""你可能会想""问题不在……而在……"
- ✅ 用自己的话转述，不堆术语
- ✅ 反问、设问制造节奏
- ✅ 不完整的句子、口语化转折、一个破折号表示转折或强调

### 5.2 短句表达长句意思

- 中文句子尽量不超过 40 字（必要列举除外）。
- 一句话只讲一件事。能断句就断句：句号 > 逗号 > 分号。
- 读起来像人在说话，有停顿、有重音、有节奏。

### 5.3 具体 > 模糊 > 抽象

- 先讲"为什么重要"，再讲"是什么"。
- 抽象概念用具体例子落地。
- 名字、数字、时间——能具体的都不模糊。引用不超过 1-2 行，其余用自己的话。

### 5.4 有条理但不像大纲

- 有逻辑推进，但读起来是"顺着想下去"，不是"第一点第二点第三点"。
- 一个问题引出下一个问题，用空行分隔小节。

### 5.5 开头与结尾

- 强开头：直接进入核心问题或冲突，不绕。
- 结尾自然收束，不重复开头、不强行拔高、不喊口号。

### 5.6 语气

- 用"你"，不过度。
- 幽默干冷克制，偶尔 understatement。
- 允许"我"（个人判断）+ "我们"（信息收集验证）的混合，但以判断为主。

## 6. Format catalog

Choose the format that serves the argument, not the other way around.

| Format | Use when | Output template |
|--------|----------|-----------------|
| 单图 (single image) | One sharp claim or idea; the image carries the argument | `templates/single-post.md` |
| 多图轮播 (carousel) | An argument that unfolds in steps; 6-9 cards, one idea per card | `templates/carousel.md` |
| 长文 (editorial essay) | A full argument that needs room to breathe | `templates/single-post.md` |
| 案例研究 (case study) | One specific decision/company, examined in depth | `templates/carousel.md` |
| 评论 (commentary) | A fresh take on a current event | `templates/single-post.md` |
| 框架 (framework) | A reusable mental model, explained | `templates/carousel.md` |
| 构建记录 (building in public) | First-person build progress with a real lesson | `templates/single-post.md` |

Each card in a carousel must be independently readable — no "接上一条" dependencies.
