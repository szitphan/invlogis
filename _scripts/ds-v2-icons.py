#!/usr/bin/env python3
"""DS v2 — icon: lấy SVG theo tên, sinh mã dựng component icon trên Figma (design/v2/icons.md).

  python3 _scripts/ds-v2-icons.py check <tên>...     # có SVG không (tự vẽ / Lucide), có bản tô, có nghĩa chưa
  python3 _scripts/ds-v2-icons.py payload <tên>...   # in JSON dữ liệu dựng (SVG, nghĩa, mô tả)
  python3 _scripts/ds-v2-icons.py figma <tên>...     # in mã JS để chạy qua use_figma (Figma MCP)
        [--page ID] [--library ID]                   #   mặc định: trang ✦ DS · Icons, khung "Thư viện icon · DS v2"

Mã `figma` thêm mỗi icon thành component set `icon/<tên>` với 5 biến thể Size=12 · 14 · 16 · 20 · 24, nét 1.8 trên
khung 24 co theo cỡ (DEC-142, DEC-147), màu gắn biến `color/icon/primary`, đặt vào cuối "Lưới icon".
Icon đã có trên trang thì bỏ qua. Chạy với fileKey FIGMA_FILE bên dưới.

Nguồn bản viền: design/v2/icons/<tên>.svg nếu có (icon tự vẽ, DEC-145), không thì Lucide 1.58.0 tải từ unpkg
(DEC-156). Có design/v2/icons/<tên>-fill.svg thì thêm trục Fill=Off · On. Bản tô không tự sinh: vẽ tay trên Figma
theo icons.md mục 4 rồi xuất SVG vào file đó. Nghĩa lấy từ bảng nghĩa icons.md mục 7 (DEC-146).
Figma tái cấu trúc (vòng 6) thì sửa PAGE, LIBRARY, COLLECTION.
"""
import argparse
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "design/v2/icons.md"
LOCAL = ROOT / "design/v2/icons"
LUCIDE = "1.58.0"
LUCIDE_URL = "https://unpkg.com/lucide-static@{ver}/icons/{name}.svg"

FIGMA_FILE = "FifpyOMpZk9OP8qyNzbRVJ"
PAGE = "5961:221"                               # trang ✦ DS · Icons
LIBRARY = "5968:221"                            # khung "Thư viện icon · DS v2", có con "Lưới icon"
COLLECTION = "VariableCollectionId:5938:223"    # Semantic, chứa color/icon/primary
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
WARN_LEN = 45_000                               # mã dài hơn thì nên chia nhiều lần chạy


def inner_markup(svg: str) -> str:
    """Các phần tử con của <svg>, gộp một dòng: bỏ chú thích, bỏ khoảng trắng giữa thẻ."""
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    m = re.search(r"<svg\b[^>]*>(.*)</svg>", svg, flags=re.S)
    if not m:
        raise ValueError("không thấy thẻ <svg>")
    s = re.sub(r"\s+", " ", m.group(1))
    s = re.sub(r"\s*/>", "/>", s)
    return re.sub(r">\s*<", "><", s).strip()


def http_get(url: str):
    """(mã HTTP, nội dung). Python cài từ python.org trên macOS hay thiếu chứng chỉ gốc → lỗi SSL thì dùng curl."""
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except urllib.error.URLError as e:
        if not isinstance(e.reason, ssl.SSLError):
            sys.exit(f"Không tải được {url}: {e.reason}")
    try:
        p = subprocess.run(["curl", "-sSL", "--max-time", "20", "-w", "\n%{http_code}", url],
                           capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError) as e:
        sys.exit(f"Không tải được {url}: Python lỗi chứng chỉ SSL, curl cũng lỗi ({e})")
    body, _, code = p.stdout.rpartition("\n")
    return int(code), body


def fetch_lucide(name: str):
    url = LUCIDE_URL.format(ver=LUCIDE, name=name)
    code, text = http_get(url)
    if code == 404:
        return None
    if code != 200:
        sys.exit(f"Tải {url} lỗi HTTP {code}")
    return text if "<svg" in text else None


def section(title: str) -> str:
    """Thân mục `## n. {title}…` của icons.md, tới mục `##` kế tiếp."""
    text = DOC.read_text(encoding="utf-8")
    m = re.search(rf"^## \d+\. {re.escape(title)}.*?(?=^## )", text, flags=re.S | re.M)
    return m.group(0) if m else ""


def custom_decs() -> dict:
    """Bảng icon tự vẽ icons.md mục 6 → {tên: 'DEC-…'}."""
    rows = re.findall(r"^\|\s*`icon/([a-z0-9-]+)`\s*\|[^|]*\|\s*(DEC-\d+)", section("Icon nghiệp vụ tự vẽ"), flags=re.M)
    return dict(rows)


def meanings() -> dict:
    """Bảng nghĩa icons.md mục 7 → {tên: nghĩa}; một icon mang vài nghĩa thì nối bằng ' · '."""
    found, group = {}, ""
    for line in section("Bảng nghĩa").splitlines():
        if line.startswith("### "):
            group = line[4:]
            continue
        row = re.match(r"\|\s*([^|`]+?)\s*\|\s*`icon/([a-z0-9-]+)`", line)
        if row:
            label = ("trạng thái " if group.startswith("Trạng thái") else "") + row.group(1)
            found.setdefault(row.group(2), []).append(label)
    out = {}
    for k, v in found.items():
        s = " · ".join(v)
        out[k] = s[:1].upper() + s[1:]
    return out


def load(name: str, mean: dict, decs: dict):
    """Dữ liệu dựng 1 icon, hoặc None nếu không có SVG ở cả hai nguồn. Mô tả, nhãn theo mẫu đã dựng trên Figma."""
    own, fill = LOCAL / f"{name}.svg", LOCAL / f"{name}-fill.svg"
    if own.exists():
        svg, source = own.read_text(encoding="utf-8"), "tự vẽ"
    else:
        svg, source = fetch_lucide(name), f"Lucide {LUCIDE}"
        if svg is None:
            return None
    m, has_fill = mean.get(name), fill.exists()
    if source == "tự vẽ":
        tag = ", ".join(x for x in ("tự vẽ", decs.get(name)) if x)
        full = f"{m or 'Chưa có nghĩa chuẩn'} ({tag})"
        short, tail = full, "Lưới và nét Lucide 1.8 trên khung 24."
    else:
        full = f"{m} (bảng nghĩa DEC-146)" if m else None
        short, tail = m or "Chưa có nghĩa chuẩn", f"{source} · nét 1.8 trên khung 24."
    desc = (f"Nghĩa: {full}. " if full else "Chưa có trong bảng nghĩa (DEC-146). ")
    if has_fill:
        desc += "Có bản tô (Fill=On) cho cảnh báo, lỗi, trạng thái bật (DEC-141). "
    return {
        "source": source,
        "outline": inner_markup(svg),
        "fill": inner_markup(fill.read_text(encoding="utf-8")) if has_fill else None,
        "meaning": m,
        "description": desc + tail,
        "label": f"{full or short} · viền và tô" if has_fill else short,
    }


def collect(names):
    mean, decs, data, missing = meanings(), custom_decs(), {}, []
    for raw in names:
        name = raw.removeprefix("icon/")
        if not NAME.match(name):
            sys.exit(f"Tên không hợp lệ: {raw!r} (viết thường, nối bằng '-', vd circle-alert)")
        d = load(name, mean, decs)
        if d is None:
            missing.append(name)
        else:
            data[name] = d
    return data, missing


JS = r"""// ds-v2-icons.py figma __NAMES__
// Chạy qua use_figma: fileKey __FILE__, skillNames "figma-use,figma-generate-library". Icon đã có trên trang thì bỏ qua.
const page=await figma.getNodeByIdAsync('__PAGE__');await figma.setCurrentPageAsync(page);
await Promise.all([['Inter','Regular'],['JetBrains Mono','Regular']].map(([f,s])=>figma.loadFontAsync({family:f,style:s})));
const ICONS=__DATA__;
const SIZES=[12,14,16,20,24];
const iconVar=(await figma.variables.getLocalVariablesAsync('COLOR')).find(v=>v.name==='color/icon/primary'&&v.variableCollectionId==='__COLLECTION__');
if(!iconVar)throw new Error('Không thấy biến color/icon/primary trong collection __COLLECTION__');
const P=()=>figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',iconVar);
const GREY={r:95/255,g:107/255,b:122/255},INK={r:18/255,g:24/255,b:38/255};
const T=(s,size,col,fam)=>{const t=figma.createText();t.fontName={family:fam||'Inter',style:'Regular'};t.fontSize=size;t.lineHeight={unit:'PIXELS',value:Math.round(size*1.4)};t.characters=s;t.fills=[{type:'SOLID',color:col}];return t};
const lib=await figma.getNodeByIdAsync('__LIBRARY__');const grid=lib&&lib.findChild(n=>n.name==='Lưới icon');
if(!grid)throw new Error('Không thấy "Lưới icon" trong khung __LIBRARY__');
const outline=inner=>`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#121826" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${inner}</svg>`;
const filled=inner=>`<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">${inner.replaceAll('currentColor','#121826')}</svg>`;
function variant(svg,name,s,fill){const c=figma.createComponentFromNode(figma.createNodeFromSvg(svg));c.name=name;c.fills=[];
 if(fill){const body=c.children.filter(n=>'fills' in n&&n.fills.length&&!n.strokes.length);if(body.length)(body.length>1?figma.flatten(body,c,0):body[0]).name='Hình tô'}
 c.rescale(s/24);
 c.findAll(()=>true).forEach(n=>{if('fills' in n&&Array.isArray(n.fills)&&n.fills.length)n.fills=[P()];if('strokes' in n&&n.strokes.length)n.strokes=[P()]});return c}
const made=[],skipped=[];
for(const [name,d] of Object.entries(ICONS)){
 if(page.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='icon/'+name)){skipped.push(name);continue}
 const cell=figma.createAutoLayout('VERTICAL');cell.name='Ô · '+name;cell.fills=[{type:'SOLID',color:{r:249/255,g:250/255,b:252/255}}];cell.cornerRadius=12;cell.paddingLeft=cell.paddingRight=cell.paddingTop=cell.paddingBottom=12;cell.itemSpacing=6;grid.appendChild(cell);cell.resize(226,10);cell.primaryAxisSizingMode='AUTO';cell.counterAxisSizingMode='FIXED';
 const comps=SIZES.map(s=>variant(outline(d.outline),d.fill?`Size=${s}, Fill=Off`:`Size=${s}`,s));
 if(d.fill)comps.push(...SIZES.map(s=>variant(filled(d.fill),`Size=${s}, Fill=On`,s,true)));
 const set=figma.combineAsVariants(comps,cell);set.name='icon/'+name;set.description=d.description;
 set.layoutMode='HORIZONTAL';set.itemSpacing=14;set.paddingLeft=set.paddingRight=set.paddingTop=set.paddingBottom=10;set.counterAxisAlignItems='CENTER';
 if(d.fill){set.layoutWrap='WRAP';set.counterAxisSpacing=10;set.resize(163,10);set.primaryAxisSizingMode='FIXED';set.counterAxisSizingMode='AUTO'}
 else{set.primaryAxisSizingMode='AUTO';set.counterAxisSizingMode='AUTO'}
 for(const t of [T('icon/'+name,11,INK,'JetBrains Mono'),T(d.label,12,GREY)]){cell.appendChild(t);t.layoutSizingHorizontal='FILL';t.textAutoResize='HEIGHT'}
 made.push({name,id:set.id,variants:comps.length})}
return {made,skipped,totalSets:page.findAll(n=>n.type==='COMPONENT_SET'&&n.name.startsWith('icon/')).length};
"""


def figma_js(data: dict, page: str, library: str) -> str:
    slim = {k: {"outline": d["outline"], "fill": d["fill"], "description": d["description"], "label": d["label"]}
            for k, d in data.items()}
    return (JS.replace("__NAMES__", " ".join(data)).replace("__FILE__", FIGMA_FILE)
            .replace("__PAGE__", page).replace("__LIBRARY__", library).replace("__COLLECTION__", COLLECTION)
            .replace("__DATA__", json.dumps(slim, ensure_ascii=False)))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("cmd", choices=["check", "payload", "figma"])
    ap.add_argument("names", nargs="+")
    ap.add_argument("--page", default=PAGE)
    ap.add_argument("--library", default=LIBRARY)
    a = ap.parse_args()
    data, missing = collect(a.names)

    if a.cmd == "check":
        print(f"{'Tên':<24}{'Bản viền':<16}{'Bản tô':<9}Nghĩa (icons.md mục 7)")
        for name in [n.removeprefix("icon/") for n in a.names]:
            d = data.get(name)
            if d is None:
                print(f"{name:<24}{'KHÔNG CÓ':<16}{'—':<9}—")
            else:
                print(f"{name:<24}{d['source']:<16}{'có' if d['fill'] else '—':<9}{d['meaning'] or 'chưa có'}")
        sys.exit(1 if missing else 0)

    if missing:
        sys.exit(f"Không có SVG cho: {', '.join(missing)} (không có trong design/v2/icons/ và Lucide {LUCIDE})")
    if a.cmd == "payload":
        print(json.dumps(data, ensure_ascii=False, indent=1))
        return
    js = figma_js(data, a.page, a.library)
    print(js)
    note = ", ".join(f"{k} ({d['source']}{', có bản tô' if d['fill'] else ''})" for k, d in data.items())
    print(f"[ds-v2-icons] {len(data)} icon: {note} · mã {len(js):,} ký tự", file=sys.stderr)
    if len(js) > WARN_LEN:
        print("[ds-v2-icons] mã dài, nên chia thành nhiều lần chạy", file=sys.stderr)


if __name__ == "__main__":
    main()
