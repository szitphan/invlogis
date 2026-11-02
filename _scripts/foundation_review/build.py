#!/usr/bin/env python3
"""Dựng + kiểm trang review foundation: python3 _scripts/foundation_review/build.py <slug> [--no-render] [--urls file.json]

Kiểm SPEC (cổng tĩnh) → ghi design-system/_review/foundations/<slug>.html → mở bằng Chrome không giao diện, đọc kết quả tự kiểm
của trang (lỗi JS, biến rỗng, tràn khung, tương phản rớt), chụp ảnh web + mobile vào _shots/. Có FAIL → exit 1.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import kit  # noqa: E402

ROOT = kit.ROOT
OUT = ROOT / "design-system/_review/foundations"
SHOTS = OUT / "_shots"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TOK = set(re.findall(r"(--[\w-]+)\s*:", kit.TCSS))
DECS = set(re.findall(r"^\| (DEC-\d+) ", (ROOT / "_workspace/decisions.md").read_text(), flags=re.M))
TJ = json.loads((ROOT / "design-system/tokens.json").read_text())
# tiền tố token viết trong <code>: có dấu / thì phải tồn tại, trừ khi item khai là token đề xuất
TOKEN_RE = re.compile(r"<code>((?:color|space|radius|layout|shadow|icon|size|control|width|type|font-size|line-height|focus|backdrop-blur|grid|container|invlogis|innvie)/[\w/.\-]+)</code>")
UNTITLED_NS = re.compile(r"^(spacing|radius|shadow|focus-ring|backdrop-blur|container|width|font)-")


def load(slug):
    p = HERE / f"{slug}.py"
    sp = importlib.util.spec_from_file_location(f"frv_{slug}", p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m.SPEC


def walk(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for x in o.values():
            yield from walk(x)
    elif isinstance(o, (list, tuple)):
        for x in o:
            yield from walk(x)


def check_spec(spec, html_):
    fail, warn = [], []
    for k in ("slug", "short", "title", "subtitle", "lead", "kpis", "sections", "items", "final"):
        if not spec.get(k):
            fail.append(f"thiếu khoá SPEC '{k}'")
    if len(spec.get("items", [])) < 3:
        warn.append("ít hơn 3 mục cần chọn, xem lại có sót không")
    if not spec.get("screens"):
        fail.append("thiếu screens (màn thật), trừ khi trang logo khai screens riêng")
    secs = " ".join(s["title"] for s in spec.get("sections", []))
    if not any(x["title"].startswith("Bảng đối chiếu") and "Untitled ↔ mình" in x["title"] for x in spec.get("sections", [])):
        fail.append("thiếu section 'Bảng đối chiếu … Untitled ↔ mình'")
    if not any(x["title"].startswith("Đã chốt, không mở lại") for x in spec.get("sections", [])):
        fail.append("thiếu section 'Đã chốt, không mở lại' (DEC đang hiệu lực của mục này)")
    if not any(x["title"].startswith("Bộ chung đề xuất") for x in spec.get("sections", [])):
        fail.append("thiếu section 'Bộ chung đề xuất'")
    if not all(k in spec.get("final", "") for k in ("tokens.json", "tokens.css", "Figma", "DEC")):
        fail.append("câu final phải nêu tokens.json, tokens.css, biến Figma, ghi DEC")
    ids = [i["id"] for i in spec.get("items", [])]
    if len(ids) != len(set(ids)):
        fail.append("trùng id mục")
    new_tokens = set()
    for it in spec.get("items", []):
        new_tokens |= {a for a, _, _ in it.get("tokens", [])}
    for it in spec.get("items", []):
        for k in ("id", "grp", "title", "why", "untitled", "ours", "astryx", "opts"):
            if not it.get(k):
                fail.append(f"{it.get('id')}: thiếu '{k}'")
        if not it.get("pv") and not it.get("pv_none"):
            fail.append(f"{it['id']}: không có xem thử (pv) và không khai lý do (pv_none)")
        recs = [o for o in it.get("opts", []) if o[2]]
        if len(recs) != 1:
            fail.append(f"{it['id']}: phải có đúng 1 phương án khuyến nghị (đang {len(recs)})")
        if len(it.get("opts", [])) < 2:
            fail.append(f"{it['id']}: cần ít nhất 2 phương án")
        if len({o[0] for o in it.get("opts", [])}) != len(it.get("opts", [])):
            fail.append(f"{it['id']}: trùng khoá phương án")
    text = "\n".join(walk({k: v for k, v in spec.items() if k not in ("screens", "css", "js")}))
    # token viện dẫn phải có thật
    for m in TOKEN_RE.finditer(text):
        n = m.group(1).rstrip(".")
        if n in new_tokens:
            continue
        if "--" + n.replace("/", "-") not in TOK and n.split("/")[0] not in ("type",) and "*" not in n:
            fail.append(f"token không tồn tại (khai vào tokens của mục nếu là đề xuất): {n}")
    # DEC viện dẫn phải có thật
    for d in set(re.findall(r"DEC-\d+", text)):
        if d not in DECS:
            fail.append(f"{d} không có trong decisions.md")
    # đường dẫn viện dẫn phải có thật
    for m in re.finditer(r"<code>((?:design-system|design|_scripts|docs)/[\w./\-]+\.\w+)</code>", text):
        if not (ROOT / m.group(1)).exists():
            fail.append(f"đường dẫn không tồn tại: {m.group(1)}")
    # var() trong preview và css phải có thật, hoặc khai bằng --x: trong chính trang
    own = set(re.findall(r"(--[\w-]+)\s*:", kit.PAGE_CSS + spec.get("css", "") + (spec.get("screens") or {}).get("proposal_css", "") + " ".join(walk(spec.get("items", [])))))
    ok_vars = TOK | own | {"--ic", "--d-logo"}
    for m in set(re.findall(r"var\((--[\w-]+)", html_)):
        if m not in ok_vars:
            fail.append(f"var({m}) không có trong tokens.css hay trang")
    # không số trần màu trong xem thử: hex/rgb trong pv
    for it in spec.get("items", []):
        pv = it.get("pv") or ""
        pv2 = re.sub(r"<svg.*?</svg>", "", pv, flags=re.S)
        if re.search(r"#[0-9a-fA-F]{3,8}\b(?![^<]*</(?:code|b|td))|rgba?\(", re.sub(r"<[^>]*(?:data-raw)[^>]*>", "", pv2)) and not it.get("pv_raw_ok"):
            warn.append(f"{it['id']}: xem thử có mã màu trần (khai pv_raw_ok='lý do' nếu là số Untitled để so)")
    # văn phong: không ghi mã nhị phân kiểu lệnh, không để chữ TODO
    if re.search(r"TODO|FIXME|lorem", text, flags=re.I):
        fail.append("còn TODO/FIXME/lorem")
    # mọi đề xuất có số Untitled: phải nêu tên biến Untitled (kiểm nhẹ)
    for it in spec.get("items", []):
        if "<code>" not in it.get("untitled", "") and not it.get("untitled_none"):
            warn.append(f"{it['id']}: ô Untitled không trích tên biến/mục (thêm <code>…</code> hoặc untitled_none='lý do')")
        if "<code>" not in it.get("ours", ""):
            warn.append(f"{it['id']}: ô Mình đang có không trích token/file")
    return fail, warn


def chrome(url, *args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--virtual-time-budget=5000", *args, url],
                          capture_output=True, text=True, timeout=120)


def render_check(path, slug):
    fail, warn = [], []
    r = chrome(path.as_uri(), "--dump-dom", "--window-size=1280,1000")
    m = re.search(r'<pre id="__selfcheck"[^>]*>(.*?)</pre>', r.stdout, flags=re.S)
    if not m:
        return [f"trang không chạy xong JS (không thấy __selfcheck). stderr: {r.stderr[-300:]}"], warn
    import html as H
    d = json.loads(H.unescape(m.group(1)))
    for e in d["errors"]:
        fail.append(f"lỗi JS: {e}")
    for v in d["emptyVars"]:
        fail.append(f"biến rỗng khi chạy: {v}")
    for o in d["overflow"]:
        fail.append(f"tràn khung: {o}")
    for c in d["crFail"]:
        warn.append(f"tương phản dưới ngưỡng (nêu trong câu chữ nếu cố ý): {c}")
    SHOTS.mkdir(exist_ok=True, parents=True)
    chrome(path.as_uri(), f"--screenshot={SHOTS / f'{slug}-web.png'}", "--window-size=1280,5000")
    # Chrome không giao diện không hẹp dưới 500px: bản mobile chụp qua iframe rộng 390
    fr = SHOTS / f"{slug}-frame.html"
    fr.write_text(f'<!DOCTYPE html><body style="margin:0"><iframe src="{path.as_uri()}" style="width:390px;height:5000px;border:0"></iframe>')
    chrome(fr.as_uri(), f"--screenshot={SHOTS / f'{slug}-mobile.png'}", "--window-size=500,5000")
    fr.unlink()
    return fail, warn


def main():
    slug = sys.argv[1]
    urls = {}
    if "--urls" in sys.argv:
        urls = json.loads(Path(sys.argv[sys.argv.index("--urls") + 1]).read_text())
    spec = load(slug)
    html_ = kit.render(spec, urls)
    fail, warn = check_spec(spec, html_)
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / f"{slug}.html"
    p.write_text(html_, encoding="utf-8")
    if "--no-render" not in sys.argv:
        f2, w2 = render_check(p, slug)
        fail += f2
        warn += w2
    print(f"{slug}: {len(spec['items'])} mục · {len(html_) // 1024} KB · {p.relative_to(ROOT)}")
    for x in warn:
        print("  WARN", x)
    for x in fail:
        print("  FAIL", x)
    print("KẾT QUẢ:", "FAIL" if fail else "PASS", f"({len(fail)} fail, {len(warn)} warn)")
    print(f"ảnh: {SHOTS}/{slug}-web.png, {slug}-mobile.png (chỉ đọc khung trên 5000px; màn thật đầu trang)")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
