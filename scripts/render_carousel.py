#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ELITE 小红书 carousel renderer — legacy editorial layout（迁移自 jade-claude-skills/elite-carousel）.

输入: carousel.json
  { slug, title, author, source, screenshot, summary, sections:[{heading, paragraphs:[...]}] }
输出: 封面 + 正文卡片 PNG (3:4 = 1080x1440 @2x = 2160x2880)
      ~/ELITE/组图/<slug>/ + 桌面副本 ~/Desktop/ELITE组图_<slug>/

设计规范（恢复旧版排版，保留 Midnight Sky #16151D）:
- logo 顶部居中、放大（84px 高），每张图都有
- 封面: logo → 截图(不裁剪) → 大标题 → 作者 → 底部一段话总结，space-between 占满
- 正文: logo → 小节主题(金色左竖条) → 段落，重点=金色半透明高亮；自动分页填满
用法: python3 render_carousel.py <carousel.json>
依赖: Google Chrome (headless)
"""
import json, os, sys, re, html, subprocess, shutil, tempfile, math
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CANVAS_W, CANVAS_H = 1080, 1440          # 3:4
SCALE = 2

# 迁移后的配色：Midnight Sky 底 + 遗产排版（金 #D4AF37 与品牌 accent 一致）
BG = "#16151D"
TEXT = "#F0F0F0"
MUTED = "#989898"
GOLD = "#D4AF37"
HL = "rgba(212,175,55,0.30)"

PAD_X = 72
PAD_TOP = 52
LOGO_H = 84
LOGO_MB = 40
PAD_BOTTOM = 52
BODY_FS = 46
BODY_LH = 1.75
HEAD_FS = 54
HEAD_LH = 1.28
PARA_MB = 36
HEAD_MB = 40
TITLE_FS = 66
AUTHOR_FS = 26
SUMMARY_FS = 30

CONTENT_W = CANVAS_W - 2 * PAD_X
USABLE_H = CANVAS_H - PAD_TOP - LOGO_H - LOGO_MB - PAD_BOTTOM

DEFAULT_LOGO = Path.home() / "ELITE" / "logo.png"


def esc(t):
    return html.escape(str(t), quote=False)


def md(t):
    """**重点** → 金色半透明底高亮"""
    parts = re.split(r"(\*\*.*?\*\*)", t)
    out = []
    for p in parts:
        if p.startswith("**") and p.endswith("**"):
            out.append('<span class="hl">%s</span>' % esc(p[2:-2]))
        else:
            out.append(esc(p))
    return "".join(out)


def uri(p):
    return Path(p).as_uri()


def logo_html():
    if DEFAULT_LOGO.exists():
        return f'<div class="logo"><img src="{uri(DEFAULT_LOGO)}"></div>'
    return '<div class="logo logo-text">ELITE</div>'


def est_lines(text, fs):
    if not text:
        return 0
    per_line = max(1, int(CONTENT_W / fs))
    return max(1, math.ceil(len(text) / per_line))


def block_height(b):
    if b["type"] == "heading":
        return est_lines(b["text"], HEAD_FS) * HEAD_FS * HEAD_LH + HEAD_MB
    return est_lines(b["text"], BODY_FS) * BODY_FS * BODY_LH + PARA_MB


def paginate(blocks):
    """贪心装页：标题连续流动，只在放不下时换页（标题后至少能跟一段）"""
    cards, cur, cur_h = [], [], 0
    i = 0
    while i < len(blocks):
        b = blocks[i]
        bh = block_height(b)
        if b["type"] == "heading":
            next_h = block_height(blocks[i + 1]) if i + 1 < len(blocks) else 0
            if cur and cur_h + bh + next_h > USABLE_H:
                cards.append(cur)
                cur, cur_h = [], 0
            cur.append(b)
            cur_h += bh
        else:
            if cur and cur_h + bh > USABLE_H:
                cards.append(cur)
                cur, cur_h = [], 0
            cur.append(b)
            cur_h += bh
        i += 1
    if cur:
        cards.append(cur)
    return cards


BASE_CSS = f"""
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:{CANVAS_W}px; height:{CANVAS_H}px; }}
body {{
  background:{BG};
  font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  color:{TEXT};
  padding:{PAD_TOP}px {PAD_X}px {PAD_BOTTOM}px;
  display:flex; flex-direction:column;
  overflow:hidden;
  position:relative;
}}
.logo {{ display:flex; justify-content:center; margin-bottom:{LOGO_MB}px; }}
.logo img {{ height:{LOGO_H}px; }}
.logo-text {{ height:{LOGO_H}px; align-items:center; font-size:34px; letter-spacing:12px;
  color:{TEXT}; font-weight:600; }}
.hl {{
  background:{HL};
  color:#FFFFFF;
  padding:2px 6px;
  border-radius:5px;
  font-weight:600;
}}
"""


def cover_html(spec):
    shot = spec.get("screenshot", "")
    if shot and Path(shot).exists():
        shot_html = f'<div class="shot"><img src="{uri(shot)}"></div>'
    else:
        # 封面必须有真图：用户附的 / 人物图 / 实拍图。缺图时不放文字占位，只保留标题/作者/总结。
        shot_html = ""
    summary = spec.get("summary", "").strip()
    summary_html = f'<div class="summary">{md(summary)}</div>' if summary else ""
    author = esc(spec.get("author", ""))
    source = esc(spec.get("source", ""))
    byline = ""
    if author and source:
        byline = f'<div class="author"><b>{author}</b> · {source}</div>'
    elif author:
        byline = f'<div class="author"><b>{author}</b></div>'
    elif source:
        byline = f'<div class="author">{source}</div>'
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
{BASE_CSS}
body.cover {{ justify-content:space-between; }}
body.cover .logo {{ margin-bottom:0; }}
.shot {{ width:100%; border-radius:14px; overflow:hidden; border:1px solid rgba(255,255,255,0.10); }}
.shot img {{ width:100%; height:auto; display:block; }}
.title {{ font-size:{TITLE_FS}px; font-weight:800; line-height:1.2; letter-spacing:-0.5px; }}
.author {{ font-size:{AUTHOR_FS}px; color:{MUTED}; }}
.author b {{ color:{TEXT}; font-weight:600; }}
.summary {{ padding-top:24px; border-top:1px solid rgba(255,255,255,0.12); font-size:{SUMMARY_FS}px; line-height:1.7; color:#C9C9C9; }}
</style></head>
<body class="cover">
{logo_html()}
{shot_html}
<div class="title">{md(spec.get("title", ""))}</div>
{byline}
{summary_html}
</body></html>"""


def body_html(blocks, idx, total):
    parts = []
    for b in blocks:
        if b["type"] == "heading":
            parts.append(f'<div class="heading">{md(b["text"])}</div>')
        else:
            parts.append(f'<p>{md(b["text"])}</p>')
    body = "\n".join(parts)
    pageno = f'<span class="pageno">{idx}/{total}</span>'
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
{BASE_CSS}
.heading {{ font-size:{HEAD_FS}px; font-weight:700; line-height:{HEAD_LH}; margin-bottom:{HEAD_MB}px; padding-left:22px; border-left:6px solid {GOLD}; }}
.body-text p {{ font-size:{BODY_FS}px; line-height:{BODY_LH}; margin-bottom:{PARA_MB}px; color:{TEXT}; }}
.pageno {{ position:absolute; top:{PAD_TOP+6}px; right:{PAD_X}px; font-size:22px; color:{MUTED}; }}
</style></head>
<body>
{logo_html()}
<div class="body-text">{body}</div>
{pageno}
</body></html>"""


def render(html_str, out_png):
    fd, path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(html_str)
    try:
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             f"--force-device-scale-factor={SCALE}",
             f"--window-size={CANVAS_W},{CANVAS_H}",
             f"--screenshot={out_png}", f"file://{path}"],
            check=True, capture_output=True, timeout=60,
        )
    finally:
        os.remove(path)


def build_blocks(spec):
    blocks = []
    for s in spec.get("sections", []):
        blocks.append({"type": "heading", "text": s.get("heading", "")})
        for p in s.get("paragraphs", []):
            blocks.append({"type": "para", "text": p})
    return blocks


def main():
    if len(sys.argv) < 2:
        print("用法: python3 render_carousel.py <carousel.json>")
        sys.exit(1)
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    slug = spec.get("slug") or re.sub(r"[^\w一-鿿]+", "-", spec.get("title", "content")).strip("-")[:40]
    outdir = Path.home() / "ELITE" / "组图" / slug
    if outdir.exists():
        for old in outdir.glob("*.png"):
            old.unlink()
    outdir.mkdir(parents=True, exist_ok=True)

    render(cover_html(spec), outdir / "01_cover.png")
    print("✓ 01_cover.png (封面)")

    cards = paginate(build_blocks(spec))
    for i, blocks in enumerate(cards):
        n = i + 2
        render(body_html(blocks, n, len(cards) + 1), outdir / f"{n:02d}.png")
        heads = " / ".join(b["text"][:12] for b in blocks if b["type"] == "heading")
        print(f"✓ {n:02d}.png  <- {heads or '(续)'}")

    desktop = Path.home() / "Desktop" / f"ELITE组图_{slug}"
    if desktop.exists():
        shutil.rmtree(desktop)
    shutil.copytree(outdir, desktop)
    print(f"\n完成: {outdir}")
    print(f"桌面: {desktop}")
    print(f"共 {len(cards) + 1} 张")


if __name__ == "__main__":
    main()
