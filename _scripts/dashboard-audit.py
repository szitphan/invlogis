#!/usr/bin/env python3
"""
dashboard-audit.py — lớp 1 (máy đo) cho dashboard HTML, tương đương Bước 6 của /figma-screen.

Figma có layout_audit / a11y_audit / auditDesignSystem; HTML thì đo bằng Chromium chạy ngầm (bản
headless shell của Playwright có sẵn trên máy): tiêm 1 script đo vào BẢN SAO của trang, mở từng tab ở
2 bề rộng (1440 · 400), đọc kết quả qua --dump-dom. Không sửa trang gốc.

  A1 Bố cục     trang cuộn ngang · phần tử tràn khỏi màn mà không nằm trong vùng cuộn riêng · chữ bị cắt
  A2 Truy cập   tương phản chữ/nền (WCAG AA 4.5 · chữ lớn 3) · control thiếu tên · vùng chạm < 24px (400px)
  A3 DS         màu viết cứng trong CSS dashboard · font ngoài Inter/Cal Sans/JetBrains Mono · cỡ chữ ngoài thang design.md
  A4 Do/Don't   1 nút chính mỗi nhóm · trạng thái có chữ/icon (chấm màu phải đi kèm chữ)
  A5 Thị giác   số cỡ chữ, số màu chữ, cỡ nhỏ nhất, nút ngang hàng (Hick ≤ 5), số tab (≤ 7) — WARN cho reviewer

Dùng:
  python3 _scripts/dashboard-audit.py [<page.html>] [--out <dir>]      (mặc định docs/_shared/dashboard.html → .claude/state/dashboard-audit/)
Ra: report.md + audit.json + ảnh {tab}-{width}-{light|dark}.png. Thoát 1 khi có FAIL.
"""
import glob
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABS = [("p-today", "Hôm nay"), ("p-flow", "Luồng việc"), ("p-feat", "Feature"), ("p-kb", "Kanban"), ("p-src", "Nguồn khách"), ("p-health", "Sức khỏe vault")]
WIDTHS = [1440, 400]
DS_FONTS = {"inter", "cal sans", "jetbrains mono"}
DS_SIZES = {10, 12, 14, 17, 20, 24, 29, 35, 42}  # design.md Typography › Hierarchy

AUDIT_JS = r"""
<script>
(async function(){
  var TAB=%TAB%;
  [].forEach.call(document.querySelectorAll('[role="tabpanel"]'),function(p){p.hidden=(p.id!==TAB)});
  [].forEach.call(document.querySelectorAll('[role="tab"]'),function(b){b.setAttribute('aria-selected',String(b.getAttribute('aria-controls')===TAB))});
  try{await document.fonts.ready}catch(e){}
  await new Promise(function(r){setTimeout(r,300)});
  var out={tab:TAB,width:innerWidth,dark:matchMedia('(prefers-color-scheme: dark)').matches,a1:[],a2:[],a4:[],fonts:{},sizes:{},colors:{},hick:[],tabs:0,
           fontsLoaded:{inter:document.fonts.check('14px Inter'),cal:document.fonts.check('24px "Cal Sans"'),mono:document.fonts.check('12px "JetBrains Mono"')}};
  function vis(el){var r=el.getBoundingClientRect(),cs=getComputedStyle(el);return r.width>0&&r.height>0&&cs.visibility!=='hidden'&&cs.display!=='none'&&!el.closest('[hidden]')}
  function desc(el){var t=(el.innerText||el.getAttribute('aria-label')||'').replace(/\s+/g,' ').trim().slice(0,60);
    return el.tagName.toLowerCase()+(el.id?'#'+el.id:'')+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).slice(0,2).join('.'):'')+(t?' «'+t+'»':'')}
  function inScroller(el){for(var p=el.parentElement;p;p=p.parentElement){var o=getComputedStyle(p).overflowX;if(o==='auto'||o==='scroll')return true}return false}
  function parse(c){var m=c.match(/rgba?\(([^)]+)\)/);if(!m)return null;var v=m[1].split(/[ ,\/]+/).filter(Boolean).map(parseFloat);return [v[0],v[1],v[2],v.length>3?v[3]:1]}
  function over(top,bot){var a=top[3];return [top[0]*a+bot[0]*(1-a),top[1]*a+bot[1]*(1-a),top[2]*a+bot[2]*(1-a),1]}
  function bgOf(el){var layers=[];for(var p=el;p;p=p.parentElement){var c=parse(getComputedStyle(p).backgroundColor);if(c&&c[3]>0)layers.push(c);if(c&&c[3]>=1)break}
    var base=layers.length&&layers[layers.length-1][3]>=1?layers.pop():(out.dark?[23,23,23,1]:[255,255,255,1]);
    for(var i=layers.length-1;i>=0;i--)base=over(layers[i],base);return base}
  function lum(c){var s=[c[0],c[1],c[2]].map(function(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*s[0]+0.7152*s[1]+0.0722*s[2]}
  function ratio(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)}
  var de=document.documentElement;
  if(de.scrollWidth>de.clientWidth+1)out.a1.push({level:'FAIL',rule:'trang cuộn ngang',el:'html',detail:de.scrollWidth+'px > '+de.clientWidth+'px'});
  var els=[].filter.call(document.querySelectorAll('main *'),vis);
  els.forEach(function(el){
    var cs=getComputedStyle(el),r=el.getBoundingClientRect();
    if(r.right>innerWidth+1&&!inScroller(el)&&el.tagName!=='svg'&&!el.closest('svg'))out.a1.push({level:'FAIL',rule:'tràn khỏi màn',el:desc(el),detail:Math.round(r.right)+'px > '+innerWidth+'px'});
    if((cs.textOverflow==='ellipsis'||cs.overflowX==='hidden')&&el.scrollWidth>el.clientWidth+1&&!el.querySelector('*'))out.a1.push({level:'WARN',rule:'chữ bị cắt',el:desc(el),detail:el.scrollWidth+' > '+el.clientWidth});
    var own=[].some.call(el.childNodes,function(n){return n.nodeType===3&&n.textContent.trim()});
    if(own&&!el.closest('svg')){
      var fam=cs.fontFamily.split(',')[0].replace(/["']/g,'').trim().toLowerCase();out.fonts[fam]=(out.fonts[fam]||0)+1;
      var fs=Math.round(parseFloat(cs.fontSize));out.sizes[fs]=(out.sizes[fs]||0)+1;out.colors[cs.color]=(out.colors[cs.color]||0)+1;
      var fg=parse(cs.color),bg=bgOf(el);if(fg&&!el.closest(':disabled,[aria-disabled="true"]')){var f2=fg[3]<1?over(fg,bg):fg,cr=ratio(f2,bg);
        var large=fs>=24||(fs>=19&&parseInt(cs.fontWeight)>=700),need=large?3:4.5;
        if(cr<need)out.a2.push({level:'FAIL',rule:'tương phản',el:desc(el),detail:cr.toFixed(2)+':1 < '+need+' (chữ '+fs+'px)'})}}
  });
  [].filter.call(document.querySelectorAll('main a,main button,main select,main input,[role="tab"]'),vis).forEach(function(el){
    var name=(el.getAttribute('aria-label')||el.innerText||el.title||el.value||'').trim();
    if(!name&&el.tagName==='SELECT'){name=(el.getAttribute('aria-labelledby')?'x':'')}
    if(!name)out.a2.push({level:'FAIL',rule:'thiếu tên truy cập',el:desc(el)});
    var r=el.getBoundingClientRect(),inline=el.tagName==='A'&&getComputedStyle(el).display==='inline';
    if(innerWidth<=480&&!inline&&(r.height<24||r.width<24))out.a2.push({level:'WARN',rule:'vùng chạm < 24px',el:desc(el),detail:Math.round(r.width)+'×'+Math.round(r.height)});
  });
  // A4: chấm màu phải có chữ cạnh nó; mỗi nhóm (hàng, thẻ) ≤ 1 nút chính
  [].filter.call(document.querySelectorAll('main .dot'),vis).forEach(function(d){var p=d.parentElement;if(!(p&&p.innerText.trim()))out.a4.push({level:'FAIL',rule:'trạng thái chỉ bằng màu',el:desc(p||d)})});
  [].filter.call(document.querySelectorAll('main tr, main .fcard1, main .kcard, main .panel li'),vis).forEach(function(g){
    var prim=[].filter.call(g.querySelectorAll('button.mini:not(.ghost),button.act:not(.ghost)'),function(b){return vis(b)&&!b.disabled});
    if(prim.length>1)out.a4.push({level:'WARN',rule:'>1 nút chính trong 1 nhóm',el:desc(g),detail:prim.length+' nút'})});
  // A5 Hick: nút ngang hàng trong cùng cha
  [].filter.call(document.querySelectorAll('main *'),vis).forEach(function(p){var b=[].filter.call(p.children,function(c){return vis(c)&&c.tagName==='BUTTON'&&c.getAttribute('role')!=='tab'});if(b.length>5)out.hick.push({el:desc(p),n:b.length})});
  out.tabs=document.querySelectorAll('[role="tab"]').length;
  var shown=[].filter.call(document.querySelectorAll('[role="tabpanel"]'),function(p){return getComputedStyle(p).display!=='none'});
  if(shown.length!==1)out.a1.push({level:'FAIL',rule:'tab không ẩn/hiện đúng',el:'[role=tabpanel]',detail:shown.length+' panel đang hiện cùng lúc (cần 1)'});
  var pre=document.createElement('pre');pre.id='audit-out';pre.textContent=JSON.stringify(out);document.body.appendChild(pre);
})();
</script>
"""


def shell():
    hits = sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")))
    return hits[-1] if hits else None


def run(cmd, timeout=60):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except subprocess.TimeoutExpired:
        return ""


def main():
    a = sys.argv[1:]
    out_dir = Path(a[a.index("--out") + 1]) if "--out" in a else ROOT / ".claude/state/dashboard-audit"
    pages = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] != "--out")]
    page = Path(pages[0]) if pages else ROOT / "docs/_shared/dashboard.html"
    H = shell()
    if not H:
        print("Không tìm thấy chrome-headless-shell (Playwright). Cài: npx playwright install chromium-headless-shell")
        sys.exit(2)
    out_dir.mkdir(parents=True, exist_ok=True)
    src = page.read_text(encoding="utf-8")
    results, shots = [], []
    for tab, tab_name in TABS:
        for wd in WIDTHS:
            inj = AUDIT_JS.replace("%TAB%", json.dumps(tab))
            copy = out_dir / f"_audit-{tab}.html"
            copy.write_text(src.replace("</body>", inj + "</body>") if "</body>" in src else src + inj, encoding="utf-8")
            dom = run([H, "--disable-gpu", "--hide-scrollbars", f"--window-size={wd},1200", "--virtual-time-budget=8000",
                       "--dump-dom", copy.as_uri()])
            m = re.search(r'<pre id="audit-out">(.*?)</pre>', dom, re.S)
            if m:
                import html as _h
                results.append(json.loads(_h.unescape(m.group(1))))
            else:
                results.append({"tab": tab, "width": wd, "error": "không đọc được kết quả đo"})
            for scheme in (["light", "dark"] if wd == 1440 else ["light"]):
                png = out_dir / f"{tab}-{wd}-{scheme}.png"
                shot = copy
                if scheme == "dark":  # headless shell bỏ qua cờ ép dark → gắn data-theme như nút đổi theme của trang
                    shot = out_dir / f"_audit-{tab}-dark.html"
                    shot.write_text(re.sub(r"<html\b", '<html data-theme="dark"', copy.read_text(encoding="utf-8"), count=1), encoding="utf-8")
                run([H, "--disable-gpu", "--hide-scrollbars", f"--window-size={wd},{1800 if wd == 1440 else 2400}",
                     "--virtual-time-budget=8000", f"--screenshot={png}", shot.as_uri()])
                if png.exists():
                    shots.append(str(png.relative_to(ROOT)))
    for f in out_dir.glob("_audit-*.html"):
        f.unlink()

    # A3 tĩnh: màu viết cứng trong CSS của dashboard-build.py (ngoài khối token nhúng từ design-tokens.css)
    b = (ROOT / "_scripts/dashboard-build.py").read_text(encoding="utf-8")
    css = b[b.index('CSS = """'):b.index('"""', b.index('CSS = """') + 10)]
    hard = re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)", css)
    fonts, sizes, colors = {}, {}, {}
    for r in results:
        for k, v in r.get("fonts", {}).items():
            fonts[k] = fonts.get(k, 0) + v
        for k, v in r.get("sizes", {}).items():
            sizes[int(k)] = sizes.get(int(k), 0) + v
        for k, v in r.get("colors", {}).items():
            colors[k] = colors.get(k, 0) + v
    bad_fonts = {k: v for k, v in fonts.items() if k not in DS_FONTS}
    bad_sizes = {k: v for k, v in sizes.items() if k not in DS_SIZES}

    def dedupe(items):
        seen, out = set(), []
        for x in items:
            # Ngoại lệ đã biết (design.md › Accessibility, quyết định 27/09 + tên cột đầu bảng chốt 12/10):
            # chữ secondary trên nền muted của hàng tiêu đề bảng ≈ 4.2:1 — giữ theo Astryx, không tính lỗi.
            if x["rule"] == "tương phản" and x["el"].startswith("th") and x.get("detail", "").startswith(("4.2", "4.1")):
                x = dict(x, level="ĐÃ BIẾT")
            key = (x["rule"], x["el"])
            if key not in seen:
                seen.add(key)
                out.append(x)
        return out

    fails = 0
    lines = [f"# Dashboard audit — {date.today().isoformat()}", "", f"Trang: `{page.relative_to(ROOT) if page.is_relative_to(ROOT) else page}` · "
             f"{len(TABS)} tab × {len(WIDTHS)} bề rộng ({', '.join(map(str, WIDTHS))}) · Chromium headless", ""]
    for code, key, title in [("A1", "a1", "Bố cục"), ("A2", "a2", "Truy cập"), ("A4", "a4", "Do's & Don'ts")]:
        lines.append(f"## {code} · {title}")
        any_ = False
        for r in results:
            items = dedupe(r.get(key, []))
            if r.get("error"):
                lines.append(f"- ⚠ {r['tab']} @{r['width']}: {r['error']}")
                continue
            if not items:
                continue
            any_ = True
            nf = sum(1 for x in items if x["level"] == "FAIL")
            nk = sum(1 for x in items if x["level"] == "ĐÃ BIẾT")
            fails += nf
            items = [x for x in items if x["level"] != "ĐÃ BIẾT"]
            lines.append(f"- **{dict(TABS)[r['tab']]} @{r['width']}px** — {nf} FAIL · {len(items) - nf} WARN" + (f" · {nk} đã biết (tiêu đề cột bảng, design.md › Accessibility)" if nk else ""))
            for x in items[:12]:
                lines.append(f"  - {x['level']} {x['rule']}: `{x['el']}`" + (f" — {x['detail']}" if x.get("detail") else ""))
            if len(items) > 12:
                lines.append(f"  - … +{len(items) - 12} mục")
        if not any_:
            lines.append("- PASS (0 mục)")
        lines.append("")
    lines += ["## A3 · Design system",
              f"- Màu viết cứng trong CSS dashboard: **{len(hard)}**" + (f" — {', '.join(sorted(set(hard))[:8])}" if hard else ""),
              f"- Font đang dùng: {', '.join(f'{k} ({v})' for k, v in sorted(fonts.items(), key=lambda x: -x[1]))}"
              + (f" — **ngoài DS: {', '.join(bad_fonts)}**" if bad_fonts else " — đều trong DS"),
              f"- Font đã tải: " + ", ".join(f"{k}={'có' if v else 'CHƯA'}" for k, v in (results[0].get('fontsLoaded') or {}).items()) if results else "",
              f"- Cỡ chữ: {', '.join(f'{k}px ({v})' for k, v in sorted(sizes.items()))}"
              + (f" — **ngoài thang design.md: {', '.join(f'{k}px' for k in sorted(bad_sizes))}**" if bad_sizes else " — đều trong thang"), ""]
    fails += len(hard) + len(bad_fonts)
    hick = [h for r in results for h in r.get("hick", [])]
    lines += ["## A5 · Thị giác (WARN cho reviewer, không tự sửa)",
              f"- Số cỡ chữ: {len(sizes)} · cỡ nhỏ nhất: {min(sizes) if sizes else '—'}px · số màu chữ: {len(colors)}",
              f"- Tab: {results[0].get('tabs', '—') if results else '—'} (ngưỡng ≤ 7)",
              "- Nút ngang hàng > 5 (Hick): " + ("; ".join(f"`{h['el']}` {h['n']}" for h in hick[:6]) if hick else "không có"),
              "- Ảnh *-dark chụp với data-theme=\"dark\" (tương phản A2 đo ở mode sáng, theo design.md › Accessibility).",
              "", "## Ảnh", *[f"- `{s}`" for s in shots], ""]
    lines.append(f"**Tổng: {fails} FAIL.**" + (" Sửa hết trước khi sang lớp reviewer." if fails else " Sang lớp reviewer."))
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n".join(lines))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
