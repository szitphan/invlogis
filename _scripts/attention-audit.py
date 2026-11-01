#!/usr/bin/env python3
"""A7 — thứ tự chú ý: phần khung (breadcrumb, icon thanh trên, menu) có "nặng" hơn nội dung không.

Rule: .claude/rules/ui-review.md Mục 2 (dòng "Thứ tự chú ý"). Ngưỡng là hằng số dưới đây — sửa thì sửa
cả bảng trong rule. Người đọc kết quả: @visual-reviewer (bước "Thứ tự chú ý").

Cách đo = phép thử nheo mắt (squint test): ảnh màn → xám → làm mờ BLUR_PX → độ tối 0..1. Mỗi vùng thu
khung về sát phần có mực (> INK_THR) rồi lấy trung bình → "độ nặng". Thu khung để kết quả không đổi theo
việc khoanh vùng rộng hay hẹp. Pilot 28/10 (màn Lệnh vận tải, 3 kiểu breadcrumb): bản đồ nhiệt AI
(HotGaze deep/UNISAL) KHÔNG phân biệt được chữ đậm/nhạt — không dùng làm căn cứ; HotGaze fast chỉ in INFO.

Vai trò vùng (role): khung · tieu-de · chinh · hanh-dong · phu.

Dùng:
  # HTML: đánh dấu phần tử data-attn="role" hoặc data-attn="role:tên"
  python3 _scripts/attention-audit.py --html man.html [--width 1280 --height 800] [--out DIR] [--json] [--hotgaze]
  # Ảnh (vd ảnh Figma get_screenshot) + file vùng
  python3 _scripts/attention-audit.py --image man.png --regions vung.json [--out DIR] [--json] [--hotgaze]
    vung.json = {"scale": 2, "regions": [{"name": "breadcrumb", "role": "khung", "box": [x, y, w, h]}, ...]}
    box theo toạ độ thiết kế (px của frame); scale = px ảnh / px thiết kế (ảnh @2x → 2).
--out ghi: squint.png (ảnh nheo mắt), overlay.png (khung vùng + độ nặng), report.json.
Thoát 1 khi có FAIL.

Giới hạn (in cuối báo cáo): đo độ nặng thị giác, không đo người dùng có hiểu/bấm không; vùng nội dung lớn
nhiều khoảng trắng (bảng) luôn nhẹ khi nheo mắt — nên KHÔNG so khung với bảng, chỉ so với tiêu đề trang.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import numpy as np
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    sys.exit("Cần Pillow + numpy: python3 -m pip install pillow numpy")

# --- Ngưỡng (đồng bộ .claude/rules/ui-review.md Mục 2) ---
BLUR_PX = 8            # bán kính làm mờ ở tỷ lệ 1x
INK_THR = 0.04         # độ tối tối thiểu để tính là "có mực" khi thu khung
K1_WARN = 0.60         # khung / tiêu đề trang
K1_FAIL = 0.80
ROLES = ("khung", "tieu-de", "chinh", "hanh-dong", "phu")

BOX_JS = """
<script>
addEventListener('load', () => setTimeout(() => {
  const out = [...document.querySelectorAll('[data-attn]')].map((el, i) => {
    const r = el.getBoundingClientRect(), [role, name] = el.dataset.attn.split(':');
    return {name: name || (role + '-' + i), role, box: [r.x, r.y, r.width, r.height].map(Math.round)};
  });
  const s = document.createElement('script'); s.type = 'application/json'; s.id = '__attn';
  s.textContent = JSON.stringify(out); document.body.appendChild(s);
}, 300));
</script>
"""


def chrome_bin():
    for c in (os.environ.get("CHROME_BIN"),
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser")):
        if c and Path(c).exists():
            return c
    sys.exit("Không tìm thấy Chrome — đặt CHROME_BIN")


def render_html(html, width, height, workdir):
    """Chụp màn + lấy toạ độ các phần tử data-attn (Chrome headless, không cần Playwright)."""
    src = Path(html).resolve()
    text = src.read_text(encoding="utf-8")
    base = f'<base href="{src.parent.as_uri()}/">'
    text = re.sub(r"<head[^>]*>", lambda m: m.group(0) + base, text, count=1) if "<head" in text else base + text
    text = text.replace("</body>", BOX_JS + "</body>") if "</body>" in text else text + BOX_JS
    tmp = Path(workdir) / "page.html"
    tmp.write_text(text, encoding="utf-8")
    png = Path(workdir) / "screen.png"
    common = [chrome_bin(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
              f"--window-size={width},{height}", "--virtual-time-budget=6000"]
    subprocess.run(common + [f"--screenshot={png}", tmp.as_uri()], capture_output=True, timeout=120)
    dom = subprocess.run(common + ["--dump-dom", tmp.as_uri()], capture_output=True, text=True, timeout=120).stdout
    m = re.search(r'<script type="application/json" id="__attn">(.*?)</script>', dom, re.S)
    if not png.exists() or not m:
        sys.exit("Render HTML lỗi (không có ảnh hoặc không đọc được vùng data-attn)")
    regions = json.loads(m.group(1))
    if not regions:
        sys.exit("HTML không có phần tử data-attn — đánh dấu vùng trước")
    return png, regions, 1.0


def load_regions(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    return d["regions"], float(d.get("scale", 1))


def weigh(img_path, regions, scale):
    g = Image.open(img_path).convert("L").filter(ImageFilter.GaussianBlur(BLUR_PX * scale))
    dark = 1 - np.asarray(g, dtype=float) / 255
    H, W = dark.shape
    for r in regions:
        x, y, w, h = [int(round(v * scale)) for v in r["box"]]
        x, y = max(0, x), max(0, y)
        sub = dark[y:min(H, y + h), x:min(W, x + w)]
        ys, xs = np.where(sub > INK_THR)
        if len(ys):
            sub = sub[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        r["weight"] = round(float(sub.mean()) if sub.size else 0.0, 3)
    return g


def hotgaze(img_path, regions, scale):
    """Tín hiệu phụ (INFO): HotGaze fast — mật độ chú ý = % chú ý / % diện tích."""
    hg = os.environ.get("HOTGAZE_BIN") or shutil.which("hotgaze")
    if not hg:
        return "HotGaze không cài — bỏ qua (pip install hotgaze, hoặc đặt HOTGAZE_BIN)"
    args = [hg, "score", str(img_path), "--backend", "fast", "--json"]
    for r in regions:
        x, y, w, h = [int(round(v * scale)) for v in r["box"]]
        args += ["--region", f'{r["name"]}:{x},{y},{w},{h}']
    p = subprocess.run(args, capture_output=True, text=True)
    try:
        d = json.loads(p.stdout)
    except ValueError:
        return "HotGaze lỗi: " + (p.stderr.strip().splitlines() or ["?"])[-1]
    W, H = d["image"]["size"]["width"], d["image"]["size"]["height"]
    by = {x["name"]: x for x in d["regions"]}
    for r in regions:
        h = by.get(r["name"])
        if h:
            b = h["box"]
            r["hotgaze_density"] = round(h["share"] / max(1e-9, b["w"] * b["h"] / (W * H)), 2)
    return None


def check(regions):
    out = []
    bad = [r for r in regions if r["role"] not in ROLES]
    for r in bad:
        out.append(("WARN", "K0", f'vùng "{r["name"]}" role "{r["role"]}" không thuộc {"/".join(ROLES)}'))
    titles = [r for r in regions if r["role"] == "tieu-de"]
    if not titles:
        out.append(("WARN", "K0", "không có vùng tieu-de — không chấm được K1"))
        return out
    t = max(titles, key=lambda r: r["weight"])
    for r in regions:
        if r["role"] != "khung" or not t["weight"]:
            continue
        ratio = r["weight"] / t["weight"]
        r["ratio_title"] = round(ratio, 2)
        lvl = "FAIL" if ratio > K1_FAIL else "WARN" if ratio > K1_WARN else None
        if lvl:
            out.append((lvl, "K1", f'khung "{r["name"]}" nặng {ratio:.2f} × tiêu đề "{t["name"]}" '
                                   f'(ngưỡng WARN > {K1_WARN}, FAIL > {K1_FAIL}) — hạ cỡ / độ đậm / màu chữ'))
    return out


def overlay(img_path, regions, scale, path):
    im = Image.open(img_path).convert("RGB")
    d = ImageDraw.Draw(im)
    col = {"khung": (217, 45, 32), "tieu-de": (31, 79, 184), "chinh": (27, 117, 66), "hanh-dong": (138, 83, 0), "phu": (115, 115, 115)}
    for r in regions:
        x, y, w, h = [v * scale for v in r["box"]]
        c = col.get(r["role"], (0, 0, 0))
        d.rectangle([x, y, x + w, y + h], outline=c, width=max(2, int(2 * scale)))
        label = f'{r["name"]} {r["weight"]:.3f}'
        d.rectangle([x, y, x + 7 * len(label) * scale, y + 14 * scale], fill=c)
        d.text((x + 3, y + 1), label, fill="white")
    im.save(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--html")
    ap.add_argument("--image")
    ap.add_argument("--regions")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=800)
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--hotgaze", action="store_true")
    a = ap.parse_args()
    if not a.html and not (a.image and a.regions):
        ap.error("cần --html, hoặc --image + --regions")

    with tempfile.TemporaryDirectory() as tmp:
        if a.html:
            img, regions, scale = render_html(a.html, a.width, a.height, tmp)
        else:
            img, (regions, scale) = Path(a.image), load_regions(a.regions)
        squint = weigh(img, regions, scale)
        note = hotgaze(img, regions, scale) if a.hotgaze else None
        issues = check(regions)
        if a.out:
            out = Path(a.out)
            out.mkdir(parents=True, exist_ok=True)
            shutil.copy(img, out / "screen.png")
            squint.save(out / "squint.png")
            overlay(img, regions, scale, out / "overlay.png")

    report = {"source": a.html or a.image, "thresholds": {"K1_WARN": K1_WARN, "K1_FAIL": K1_FAIL, "BLUR_PX": BLUR_PX},
              "regions": sorted(regions, key=lambda r: -r["weight"]),
              "issues": [{"level": l, "code": c, "msg": m} for l, c, m in issues]}
    if a.out:
        (Path(a.out) / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"A7 thứ tự chú ý — {report['source']}")
        print("Thứ tự nheo mắt (nặng → nhẹ):")
        for i, r in enumerate(report["regions"], 1):
            extra = f'  ×{r["ratio_title"]} tiêu đề' if "ratio_title" in r else ""
            hg = f'  · HotGaze fast mật độ ×{r["hotgaze_density"]}' if "hotgaze_density" in r else ""
            print(f'  {i}. {r["name"]:<16} [{r["role"]}] {r["weight"]:.3f}{extra}{hg}')
        if note:
            print("INFO", note)
        fails = sum(1 for l, *_ in issues if l == "FAIL")
        warns = sum(1 for l, *_ in issues if l == "WARN")
        for l, c, m in issues:
            print(f"{l} {c} {m}")
        print(f"Kết quả: {fails} FAIL / {warns} WARN")
        print("Giới hạn: đo độ nặng thị giác (nheo mắt), không phải eye-tracking; bảng/vùng nhiều khoảng trắng "
              "luôn nhẹ — chỉ so khung với tiêu đề trang.")
    sys.exit(1 if any(l == "FAIL" for l, *_ in issues) else 0)


if __name__ == "__main__":
    main()
