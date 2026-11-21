#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ELITE 小红书 editorial carousel renderer (Midnight Sky style).

输入: carousel.json  (pillar / title / cover / slides)
输出: PNG 卡片 3:4 = 1080x1440，@2x = 2160x2880
      ~/ELITE/组图/<slug>/  + 桌面副本 ~/Desktop/ELITE组图_<slug>/

风格: split-page 杂志封面（图上区 + Midnight Sky 文字下区）+ 金色 kicker + 重点金色标注。
颜色/排版规范见 references/visual-guidelines.md 与 references/brand-identity.md。

用法: python3 render_carousel.py <carousel.json> [--out DIR]
依赖: Google Chrome (headless)
"""
import json, os, sys, re, html, subprocess, shutil, tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CANVAS_W, CANVAS_H = 1080, 1440          # 3:4
SCALE = 2

# Midnight Sky tokens (single source of truth: references/brand-identity.md)
BG      = "#16151D"
SURFACE = "#201F28"
HAIRLINE = "#2E2D38"
WARM    = "#F2EFE9"
GRAY    = "#A9A6A0"
MUTED   = "#6F6C69"
GOLD    = "#D4AF37"
SILVER  = "#C7C5BF"

# print-like grain (feTurbulence), very subtle on the dark field
GRAIN = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E"
         "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E"
         "%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E")

PAD_X = 68
PAD_TOP = 56
PAD_BOTTOM = 60
COVER_IMG_H = 42   # % height of the image field on the cover

# type scale (CSS in 1080x1440 coordinate space; Chrome scales x2)
KICKER_FS = 20
HEADLINE_FS = 82
HOOK_FS = 27
SUPPORT_FS = 21
SLIDE_HEAD_FS = 58
SLIDE_BODY_FS = 50
PAGENO_FS = 20


def esc(t):
    return html.escape(str(t), quote=False)


def md(t):
    """**重点** -> gold highlight"""
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


BASE_CSS = f"""
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:{CANVAS_W}px; height:{CANVAS_H}px; }}
body {{
  background:{BG};
  font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  color:{WARM};
  overflow:hidden;
  position:relative;
}}
.grain {{
  position:absolute; inset:0; pointer-events:none; opacity:0.045;
  background-image:url("{GRAIN}");
  background-size:160px 160px;
}}
.kicker {{
  font-family:"Didot","Bodoni 72","Times New Roman",serif;
  font-size:{KICKER_FS}px; letter-spacing:7px; text-transform:uppercase;
  color:{GOLD}; font-weight:500;
}}
.hl {{ color:{GOLD}; font-weight:600; }}
"""


def cover_html(spec):
    cover = spec.get("cover", {})
    img = cover.get("image", "")
    if img and Path(img).exists():
        field = f'<img class="cover-img" src="{uri(img)}">'
    else:
        wm = esc(spec.get("pillar", "ELITE"))
        field = f'<div class="watermark">{wm}</div>'
    head = md(cover.get("headline") or spec.get("title", ""))
    hook = md(cover.get("hook", ""))
    supp = esc(cover.get("supporting", ""))
    hook_html = f'<div class="hook">{hook}</div>' if hook else ""
    supp_html = f'<div class="supporting">{supp}</div>' if supp else ""
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
{BASE_CSS}
.image-field {{ height:{COVER_IMG_H}%; position:relative; overflow:hidden; background:{SURFACE}; }}
.cover-img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.image-field::after {{
  content:""; position:absolute; inset:0;
  background:linear-gradient(180deg, rgba(22,21,29,0.10) 0%, rgba(22,21,29,0.45) 100%);
}}
.watermark {{
  position:absolute; inset:0; display:flex; align-items:center; justify-content:center;
  font-family:"Didot","Bodoni 72","Times New Roman",serif;
  font-size:150px; letter-spacing:14px; color:{WARM}; opacity:0.08; font-weight:600;
}}
.cover-type {{
  height:{100 - COVER_IMG_H}%; padding:{PAD_TOP}px {PAD_X}px {PAD_BOTTOM}px;
  display:flex; flex-direction:column; justify-content:space-between;
}}
.headline {{ font-size:{HEADLINE_FS}px; font-weight:700; line-height:1.16; letter-spacing:-0.5px; }}
.cover-foot {{ border-top:1px solid {HAIRLINE}; padding-top:26px; }}
.hook {{ font-size:{HOOK_FS}px; line-height:1.6; color:{GRAY}; margin-bottom:16px; }}
.supporting {{ font-size:{SUPPORT_FS}px; color:{MUTED}; letter-spacing:1px; }}
</style></head>
<body class="cover">
<div class="image-field">{field}</div>
<div class="cover-type">
  <div class="kicker">{esc(spec.get("pillar", "ELITE"))}</div>
  <div class="headline">{head}</div>
  <div class="cover-foot">{hook_html}{supp_html}</div>
</div>
<div class="grain"></div>
</body></html>"""


def slide_html(spec, slide, idx, total):
    head = md(slide.get("heading", ""))
    head_html = f'<div class="heading">{head}</div>' if head else ""
    paras = "\n".join(f"<p>{md(p)}</p>" for p in slide.get("paragraphs", []))
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
{BASE_CSS}
body.slide {{ padding:{PAD_TOP}px {PAD_X}px; display:flex; flex-direction:column; }}
.slide-head {{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:56px; flex-shrink:0; }}
.pageno {{ font-size:{PAGENO_FS}px; color:{MUTED}; letter-spacing:2px; }}
.slide-body {{ flex:1; display:flex; flex-direction:column; justify-content:center; padding-bottom:{PAD_BOTTOM}px; }}
.heading {{
  font-size:{SLIDE_HEAD_FS}px; font-weight:700; line-height:1.3; margin-bottom:40px;
  padding-left:22px; border-left:5px solid {GOLD}; color:{WARM};
}}
.slide-body p {{ font-size:{SLIDE_BODY_FS}px; line-height:1.62; margin-bottom:34px; color:{WARM}; }}
</style></head>
<body class="slide">
<div class="slide-head">
  <div class="kicker">{esc(spec.get("pillar", "ELITE"))}</div>
  <div class="pageno">{idx:02d} / {total:02d}</div>
</div>
<div class="slide-body">{head_html}{paras}</div>
<div class="grain"></div>
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


def main():
    args = [a for a in sys.argv[1:]]
    if not args or args[0] in ("-h", "--help"):
        print("用法: python3 render_carousel.py <carousel.json> [--out DIR]")
        sys.exit(1)
    spec = json.load(open(args[0], encoding="utf-8"))
    slug = spec.get("slug") or re.sub(r"[^\w一-鿿]+", "-", spec.get("title", "content")).strip("-")[:40]

    outdir = None
    if "--out" in args:
        outdir = Path(args[args.index("--out") + 1])
    else:
        outdir = Path.home() / "ELITE" / "组图" / slug
    if outdir.exists():
        for old in outdir.glob("*.png"):
            old.unlink()
    outdir.mkdir(parents=True, exist_ok=True)

    slides = spec.get("slides", [])
    total = len(slides) + 1

    render(cover_html(spec), outdir / "01_cover.png")
    print("✓ 01_cover.png (封面)")

    for i, s in enumerate(slides):
        n = i + 2
        render(slide_html(spec, s, n, total), outdir / f"{n:02d}.png")
        print(f"✓ {n:02d}.png  <- {s.get('heading','') or '(正文)'}")

    desktop = Path.home() / "Desktop" / f"ELITE组图_{slug}"
    if desktop.exists():
        shutil.rmtree(desktop)
    shutil.copytree(outdir, desktop)
    print(f"\n完成: {outdir}")
    print(f"桌面: {desktop}")
    print(f"共 {total} 张")


if __name__ == "__main__":
    main()
