#!/usr/bin/env python3
"""Gate "mọi dòng sai lệch phải soi được trên hình" cho trang duyệt /figma-component --html (user 29/10).

Mở {slug}-review.html bằng Chromium headless (Playwright headless shell có sẵn trên máy), sang tab 3 Foundation,
bấm Soi từng dòng của check.json (đúng hàm fxSoi của trang: màn đang xem → bảng biến thể → từng màn × trạng thái)
và đếm phần tử được tô viền đang hiện. Dòng nào không ra phần tử nào → FAIL.

`ds-foundation-check.py` đã chặn tĩnh (sel không trỏ tới phần tử đang hiện ở tổ hợp chốt); gate này chạy trên
trang thật nên bắt cả chỗ máy tĩnh đoán sai (CSS ẩn, khung 0px, trạng thái màn).

Dùng: python3 _scripts/ds-soi-check.py <slug> [--all]   (--all: cả dòng ✅ Khớp; mặc định chỉ dòng cần quyết)
Exit 1 khi còn dòng không soi được.
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROBE = r"""<script>
setTimeout(async()=>{const out={rows:[]};
 try{showTab("foundation"); await new Promise(r=>setTimeout(r,500));
  const ALL=__ALL__;
  for(const r of ROWS()){ if(!ALL&&!r.must) continue; fFlash=null;
   if(!r.sel&&!r.at){out.rows.push({id:r.id,part:r.part,prop:r.prop,platform:r.platform,cat:r.cat,sel:"",hit:"nosel",vis:-1}); continue;}
   let hit; try{hit=await fxSoi(r.id);}catch(e){hit="ERR "+e}
   await new Promise(q=>setTimeout(q,20));
   const S=soiSel(scopeSel(r.at||selStr(r),r)); let vis=0;
   document.querySelectorAll("#p-foundation .pvhost").forEach(h=>{if(!h.shadowRoot) return;
     try{h.shadowRoot.querySelectorAll(S).forEach(e=>{const b=e.getBoundingClientRect();
       if(b.width>0&&b.height>0&&getComputedStyle(e).visibility!=="hidden") vis++;});}catch(e){}});
   out.rows.push({id:r.id,part:r.part,prop:r.prop,platform:r.platform,cat:r.cat,sel:selStr(r),hit:String(hit),vis});}
  fFlash=null;
 }catch(e){out.err=String(e)}
 document.body.setAttribute("data-soi",encodeURIComponent(JSON.stringify(out)));},2500);
</script>"""


def chrome():
    hits = sorted(glob.glob(os.path.expanduser(
        "~/Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")))
    return hits[-1] if hits else None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    slug = args[0]
    page = ROOT / f"design-system/components/_work/{slug}/{slug}-review.html"
    if not page.exists():
        print(f"Không thấy {page.relative_to(ROOT)} — chạy _scripts/ds-component-page.py {slug} trước")
        sys.exit(2)
    ch = chrome()
    if not ch:
        print("Không tìm thấy chrome-headless-shell (Playwright). Cài: npx playwright install chromium-headless-shell")
        sys.exit(2)
    html = page.read_text() + PROBE.replace("__ALL__", "true" if "--all" in sys.argv else "false")
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "p.html"
        f.write_text(html)
        dom = subprocess.run([ch, "--headless", "--disable-gpu", "--virtual-time-budget=120000",
                              "--window-size=1440,900", "--dump-dom", f.as_uri()],
                             capture_output=True, text=True, timeout=300).stdout
    m = re.search(r'data-soi="([^"]*)"', dom)
    if not m:
        print("Trang không trả kết quả soi (lỗi JS hoặc trang chưa có tab Foundation)")
        sys.exit(2)
    from urllib.parse import unquote
    out = json.loads(unquote(unescape(m.group(1))))
    if out.get("err"):
        print("Lỗi khi soi:", out["err"])
        sys.exit(2)
    rows = out["rows"]
    nosel = [r for r in rows if r["hit"] == "nosel"]
    rows = [r for r in rows if r["hit"] != "nosel"]
    bad = [r for r in rows if r["vis"] == 0 or r["hit"] in ("miss", "null", "None")]
    print(f"Soi trên hình — {slug}: {len(rows) - len(bad)}/{len(rows)} dòng ra phần tử"
          + (" (cả dòng Khớp)" if "--all" in sys.argv else " (dòng cần quyết)"))
    for r in bad:
        print(f"  ✗ {r['id']}: {r['part']} · {r['prop']} ({r['platform'] or 'mọi nền tảng'}) — sel {r['sel']}")
    if nosel:
        print(f"  ℹ {len(nosel)} dòng không gắn sel (noOverride — giá trị không vẽ lại được trên hình): "
              + ", ".join(r["id"] for r in nosel[:8]) + (" …" if len(nosel) > 8 else ""))
    if bad:
        print("Sửa: platform/sel của dòng values, hoặc thêm ô vào bảng biến thể / trạng thái màn demo có phần tử đó.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
