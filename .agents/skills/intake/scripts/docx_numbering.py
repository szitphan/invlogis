"""Dựng lại số thứ tự tự động của Word (1., 2.2, 3.1.1, a), I.…) thành chữ thật trong docx.

mammoth bỏ số tự động: đề mục "3.1.1 Lấy container" thành "Lấy container", danh sách a/b/c thành
gạch đầu dòng — mất cấu trúc và mất cách tài liệu tự tham chiếu ("xem mục 3.1.2"). Module này đọc
numbering.xml + styles.xml, tính số cho từng đoạn theo thứ tự tài liệu, chèn số vào đầu đoạn và tắt
numbering của đoạn đó (gạch đầu dòng thì giữ để mammoth vẫn ra danh sách "-").
Đề mục: đoạn có `w:outlineLvl` (cấp mục lục Word dùng) → Heading theo cấp; không có thì đoạn đánh số
thuộc danh sách phân cấp (cấp 2 dạng %1.%2) mà toàn bộ chữ in đậm → Heading theo cấp.

Sửa bằng thao tác chuỗi trên XML (không parse/ghi lại cả cây) để không làm hỏng namespace của Word.
"""
import re, zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ROMAN = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"),
         (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]


def roman(n):
    out = ""
    for v, s in ROMAN:
        while n >= v:
            out, n = out + s, n - v
    return out


def letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(97 + r) + s
    return s


def fmt(n, kind):
    return {"decimal": str(n), "decimalZero": f"{n:02d}", "lowerLetter": letter(n), "upperLetter": letter(n).upper(),
            "lowerRoman": roman(n), "upperRoman": roman(n).upper(), "none": ""}.get(kind, str(n))


def val(el, tag):
    x = el.find(W + tag) if el is not None else None
    return x.get(W + "val") if x is not None else None


def load_numbering(z):
    if "word/numbering.xml" not in z.namelist():
        return {}, {}
    root = ET.fromstring(z.read("word/numbering.xml"))
    absn = {}
    for a in root.findall(W + "abstractNum"):
        lv = {}
        for l in a.findall(W + "lvl"):
            lv[int(l.get(W + "ilvl"))] = dict(start=int(val(l, "start") or 1), fmt=val(l, "numFmt") or "decimal",
                                             text=val(l, "lvlText") or "",
                                             lgl=l.find(f"{W}isLgl") is not None)
        absn[a.get(W + "abstractNumId")] = lv
    nums = {}
    for n in root.findall(W + "num"):
        ov = {}
        for o in n.findall(W + "lvlOverride"):
            s = o.find(W + "startOverride")
            if s is not None:
                ov[int(o.get(W + "ilvl"))] = int(s.get(W + "val"))
        nums[n.get(W + "numId")] = (val(n, "abstractNumId"), ov)
    return absn, nums


def load_style_num(z):
    """{styleId: (numId, ilvl)} kể cả kế thừa basedOn."""
    if "word/styles.xml" not in z.namelist():
        return {}
    root = ET.fromstring(z.read("word/styles.xml"))
    direct, based = {}, {}
    for s in root.findall(W + "style"):
        sid = s.get(W + "styleId")
        based[sid] = val(s, "basedOn")
        np_ = s.find(f"{W}pPr/{W}numPr")
        if np_ is not None:
            direct[sid] = (val(np_, "numId"), int(val(np_, "ilvl") or 0))
    out = {}
    for sid in based:
        cur, seen = sid, set()
        while cur and cur not in direct and cur not in seen:
            seen.add(cur)
            cur = based.get(cur)
        if cur in direct:
            out[sid] = direct[cur]
    return out


P_RE = re.compile(r"<w:p\b[^>]*?(?:/>|>.*?</w:p>)", re.S)


def number_docx(src, dst):
    """Ghi bản docx đã chèn số vào dst. Trả (số đoạn được đánh số, số đề mục đổi thành heading)."""
    zin = zipfile.ZipFile(src)
    absn, nums = load_numbering(zin)
    style_num = load_style_num(zin)
    doc = zin.read("word/document.xml").decode("utf8")
    counters, started = {}, set()
    n_num = n_head = 0

    def repl(m):
        nonlocal n_num, n_head
        p = m.group(0)
        if p.endswith("/>") and "</w:p>" not in p:
            return p
        ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
        ppr_s = ppr.group(0) if ppr else ""
        npm = re.search(r"<w:numPr>.*?</w:numPr>", ppr_s, re.S)
        if npm:
            nid = re.search(r'<w:numId w:val="(\d+)"', npm.group(0))
            ilv = re.search(r'<w:ilvl w:val="(\d+)"', npm.group(0))
            nid, ilvl = (nid.group(1) if nid else None), int(ilv.group(1)) if ilv else 0
        else:
            st = re.search(r'<w:pStyle w:val="([^"]+)"', ppr_s)
            nid, ilvl = style_num.get(st.group(1), (None, 0)) if st else (None, 0)
        olv = re.search(r'<w:outlineLvl w:val="(\d)"', ppr_s)
        if (not nid or nid == "0" or nid not in nums) and olv and ppr and int(olv.group(1)) < 6:
            n_head += 1  # đề mục không đánh số
            new_ppr = re.sub(r'<w:pStyle w:val="[^"]+"/>', "", ppr_s).replace(
                "<w:pPr>", f'<w:pPr><w:pStyle w:val="Heading{int(olv.group(1)) + 1}"/>', 1)
            return p.replace(ppr_s, new_ppr, 1)
        if not nid or nid == "0" or nid not in nums:
            return p
        aid, ov = nums[nid]
        lv = absn.get(aid, {})
        if ilvl not in lv:
            return p
        if lv[ilvl]["fmt"] == "bullet":
            return p  # để mammoth giữ gạch đầu dòng
        c = counters.setdefault(aid, {})
        if nid not in started:  # num mới có startOverride → bắt đầu lại
            started.add(nid)
            for k, s in ov.items():
                c[k] = s - 1
        c[ilvl] = c.get(ilvl, lv[ilvl]["start"] - 1) + 1
        for k in list(c):
            if k > ilvl and k not in ov:
                c.pop(k)
        text = lv[ilvl]["text"]
        for k in range(9):
            if f"%{k + 1}" in text:
                d = lv.get(k, {"start": 1, "fmt": "decimal"})
                # isLgl ("legal numbering"): Word hiện mọi cấp bằng số Ả Rập → III + 1.1 thành 3.1.1
                kind = "decimal" if lv[ilvl].get("lgl") else d["fmt"]
                text = text.replace(f"%{k + 1}", fmt(c.get(k, d["start"]), kind))
        if not text.strip():
            return p
        n_num += 1
        off = '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="0"/></w:numPr>'
        if ppr:
            new_ppr = ppr_s.replace(npm.group(0), off) if npm else ppr_s.replace("<w:pPr>", "<w:pPr>" + off, 1)
        else:
            new_ppr = f"<w:pPr>{off}</w:pPr>"
        # đề mục: danh sách nhiều cấp + mọi run có chữ đều in đậm → Heading theo cấp
        runs = re.findall(r"<w:r\b.*?</w:r>", p, re.S)
        texted = [r for r in runs if re.search(r"<w:t\b[^>]*>[^<]*\S", r)]
        multi = "%1" in lv.get(1, {}).get("text", "") and "%2" in lv.get(1, {}).get("text", "")
        level = int(olv.group(1)) if olv and int(olv.group(1)) < 6 else None
        if level is None and multi and texted and all(re.search(r"<w:b/>|<w:b w:val=\"(1|true)\"/>", r) for r in texted) \
                and sum(len("".join(re.findall(r"<w:t\b[^>]*>([^<]*)</w:t>", r))) for r in texted) < 160:
            level = ilvl
        if level is not None:
            new_ppr = re.sub(r'<w:pStyle w:val="[^"]+"/>', "", new_ppr)
            new_ppr = new_ppr.replace("<w:pPr>", f'<w:pPr><w:pStyle w:val="Heading{min(level + 1, 6)}"/>', 1)
            n_head += 1
        run = f'<w:r><w:t xml:space="preserve">{text} </w:t></w:r>'
        if ppr:
            return p.replace(ppr_s, new_ppr + run, 1)
        return re.sub(r"(<w:p\b[^>]*>)", r"\1" + new_ppr + run, p, count=1)

    body = re.search(r"<w:body>.*</w:body>", doc, re.S)
    new_body = P_RE.sub(repl, body.group(0))
    doc = doc[:body.start()] + new_body + doc[body.end():]
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            data = doc.encode("utf8") if it.filename == "word/document.xml" else zin.read(it.filename)
            zout.writestr(it, data)
    return n_num, n_head
