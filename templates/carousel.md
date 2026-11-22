# Carousel（轮播 · 遗产排版）

把**整篇长文的全部内容**写进 `carousel.json`，渲染器自动分页成卡片（不是手工一卡一意）。规则：

- **不删减内容**——长文的每个小节、每段都放进去，渲染器自动分页。
- 段落里把真正有判断增量的话标 `**重点**`（渲染成金色半透明高亮），每节 1-3 处，不整段标。
- 一个段落过长（>80 字）拆成两段，方便分页。
- 封面 `screenshot` 放真图/来源截图路径；没有则留空，渲染器放「来源名 + 作者」占位。

```json
{
  "slug": "price-vs-value-2026",
  "title": "股价涨，不代表公司变好了",
  "author": "巴菲特 · 高盛 2008",
  "source": "普通人理解资本市场 · Day 4",
  "screenshot": "/Users/lusonghua/ELITE/组图素材/nyse_floor.jpg",
  "summary": "一段话总结（150-250字，放封面底部）",
  "sections": [
    { "heading": "两回事", "paragraphs": ["段落一", "**重点**句"] },
    { "heading": "高盛 2008", "paragraphs": ["……"] }
  ]
}
```

渲染：

```
python3 scripts/render_carousel.py carousel.json
```

输出封面 + N 张正文卡片（自动分页）。检查每张 2160×2880、正文填到接近底部、无溢出裁剪。
