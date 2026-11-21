# Carousel (Stage 4 output — multi-slide)

Slide-by-slide copy. Rules:

- 6-9 cards; one idea per card; every card independently readable (no "接上一条").
- The 判断 (the creator's own view) gets its own card where possible.
- Emphasis is marked `**重点**` on a phrase, never a whole paragraph.
- To render this as PNG cards, write it as `carousel.json` and run `scripts/render_carousel.py` (see `workflows/visual-production.md` §6). The `**重点**` marks become gold highlights.

```markdown
## 主标题
（≤ 20 字，与封面一致）

## 来源
（创作者/来源名 · 日期，若适用）

## 一句话总结
（150-250 字，读者看完这一句就能带走的东西）

## 卡片脚本
| 卡 | 内容 | 类型 |
|----|------|------|
| 1 | 封面：大标题 + 一句话钩子 | 封面 |
| 2 | | 论点/论据/案例/判断 |
| 3 | | |
| 4 | | |
| 5 | | 判断（我的看法）|
| … | | |

### 逐卡文案
#### 卡 1（封面）
- 大标题：
- 钩子/一句话：

#### 卡 2
（独立成段的小节标题 + 正文，`**重点**` 标注）

#### 卡 3 …
```
