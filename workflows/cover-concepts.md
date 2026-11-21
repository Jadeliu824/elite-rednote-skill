# 封面创意系统（3 方向）

封面是内容传播资产，不是文章配图。每篇先做**封面创意策划**，再进视觉生产（`workflows/visual-production.md`）。品牌规范见 `references/visual-guidelines.md`。

## 禁止

- 默认机房 / 数据中心 / 办公室等无差异化图库照片（此前 Anthropic 用机房图、表现不佳即此问题）。
- 直接拿新闻配图当封面。
- 无视觉中心的复杂拼贴、大量小字、通用 AI 商务科技背景。
- 抽象水印 / 纯文字占位当封面。

## 硬规则

**每期封面必须用真实图像**（实拍照片 / 数据图表），从 CC0 / 公有领域图源找暗调素材，不用抽象占位。注意 license 署名（优先 CC0，避免 CC BY-SA 的商用授权顾虑）。

## 三个封面方向

**A. Editorial Photography** — 杂志编辑气质的摄影画面。
**B. Conceptual Visual** — 用隐喻、象征或视觉冲突表达核心观点。
**C. Data / Financial Graphic** — 用有冲击力的数据、图表、数字表达主题。

每个方向说明：视觉主体、构图、光线与色彩、画面情绪、标题在画面中的位置、为什么比普通配图更值得点击。

## 选择

选最合适的方向。输出填 `templates/cover-concepts.md`，最终方案进 `templates/visual-spec.md`（含完整图像生成指令、构图、排版、品牌色、备选方向）。

若环境支持图像生成，优先生成可直接用的封面（配合 `scripts/render_carousel.py` 的 `cover.image`）；需用户确认的，先交付方案，不擅自发布。
