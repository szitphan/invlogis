#!/usr/bin/env python3
"""build-deck.py — deck.md → 1 file HTML trình chiếu (self-contained, chạy offline).

Dùng:
  python3 .claude/skills/deck/engine/build-deck.py <deck.md> [--out <file.html>]
          [--lint-only] [--verify] [--shots <dir>] [--force]

Thứ tự: parse → LINT (gate) → render → (verify bằng Chrome headless).
Exit: 0 OK · 1 lint/verify có lỗi (KHÔNG ghi HTML, trừ khi --force) · 2 lỗi dùng/parse.

Định dạng deck.md: xem ../references/deck-format.md. AI viết deck.md; script này là
bên DUY NHẤT sinh HTML — không tự viết HTML tay.
"""
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

try:
    import yaml
except ImportError:  # pragma: no cover
    print("Thiếu PyYAML — pip3 install pyyaml", file=sys.stderr)
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "deck-template.html")

LAYOUTS = {"title", "section", "bullets", "agenda", "goal", "oq", "recap", "end"}
DELIVERIES = {"meeting", "async"}   # meeting = chiếu trong buổi họp · async = gửi khách tự trả lời

# ---- ngưỡng mật độ (ký tự hiển thị, không tính ghi chú) ----
LIMITS = {
    "title": 260, "section": 260, "end": 260, "recap": 200,
    "bullets": 620, "agenda": 620, "goal": 620, "oq": 900,
}
MAX_BULLETS = 7
MAX_OPTIONS = 4
MAX_PRO_CON = 3          # mỗi loại (+ / −) trên 1 phương án
MAX_OPTION_CHARS = 260   # tổng chữ trong 1 thẻ phương án
MAX_QUESTION = 170
MAX_CONTEXT = 300

# mã nội bộ KHÔNG được lộ lên slide khách (chỉ ở ghi chú / directive)
INTERNAL_ID = re.compile(
    r"\b(?:FR|NFR|BR|E|BO|CAP)-[a-z][a-z0-9-]*-\d{2,3}\b"   # FR-payment-001, E-common-003
    r"|\b(?:OQ|SRC|BL|CMP|GR)-\d+\b"                          # OQ-3, CMP-03
    r"|\b(?:US|AC|TC|CHK)-\d{2,}\b"                           # US-001, AC-002
    r"|\bUC-[a-z][a-z0-9-]*\b|\bOBJ-[a-z][a-z0-9-]*\b"           # UC-checkout, OBJ-don-hang
    r"|\bCR-\d{8}-\d{3}\b")
INTERNAL_PATH = re.compile(r"\bdocs(?:-input)?/[\w./-]*|\b[\w-]+\.md\b")

SLIDE_SEP = re.compile(r"^-{3,}\s*$")
DIRECTIVE = re.compile(r"^<!--\s*(.*?)\s*-->\s*$")
OPTION_H = re.compile(r"^###\s+([A-Z])[.)]\s*(.+)$")
DOC_LABEL = "Tài liệu"  # dòng nguồn cho khách: tên tài liệu khách gửi + mục, không đường dẫn
LABELED = re.compile(r"^\*\*([^*]{1,40}?):\*\*\s*(.*)$")


# ----------------------------------------------------------------- inline md
def inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def plain(text):
    t = re.sub(r"`([^`]+)`", r"\1", text)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return t.strip()


def delivery_of(fm):
    return str(fm.get("delivery") or "meeting").strip().lower()


def dmy(iso):
    d = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", str(iso or ""))
    return f"{d.group(3)}/{d.group(2)}/{d.group(1)}" if d else str(iso or "")


# ----------------------------------------------------------------- parse
class ParseError(Exception):
    pass


def split_frontmatter(src):
    if not src.startswith("---"):
        raise ParseError("deck.md phải mở đầu bằng frontmatter YAML (---)")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", src, re.S)
    if not m:
        raise ParseError("frontmatter không đóng (thiếu dòng --- thứ hai)")
    fm = yaml.safe_load(m.group(1)) or {}
    # YAML đọc ngày thành datetime.date → chuẩn hoá về chuỗi ISO + bản hiển thị dd/mm/yyyy
    for k, v in list(fm.items()):
        if hasattr(v, "isoformat") and not isinstance(v, str):
            fm[k] = v.isoformat()
    d = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", str(fm.get("date", "")))
    if d and not fm.get("date_display"):
        fm["date_display"] = f"{d.group(3)}/{d.group(2)}/{d.group(1)}"
    return fm, m.group(2)


def split_slides(body):
    chunks, cur, in_notes = [], [], False
    for ln in body.split("\n"):
        s = ln.strip()
        if s.startswith(":::"):
            in_notes = (s != ":::")
        if SLIDE_SEP.match(ln) and not in_notes:
            chunks.append(cur)
            cur = []
            continue
        cur.append(ln)
    chunks.append(cur)
    return [c for c in chunks if any(x.strip() for x in c)]


def parse_directive(line):
    d = {}
    for part in line.split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            d[k.strip().lower()] = v.strip()
    return d


def parse_slide(lines, idx):
    s = {"n": idx + 1, "dir": {}, "h1": None, "h2": None, "ctx": [], "labeled": [],
         "items": [], "paras": [], "options": [], "notes": [], "order": []}
    in_notes = False
    opt = None
    first_content = True
    for raw in lines:
        ln = raw.rstrip()
        st = ln.strip()
        if in_notes:
            if st == ":::":
                in_notes = False
            else:
                s["notes"].append(ln)
            continue
        if st.startswith("::: notes") or st == ":::notes":
            in_notes = True
            continue
        if not st:
            continue
        m = DIRECTIVE.match(st)
        if m and first_content and not s["dir"]:
            s["dir"] = parse_directive(m.group(1))
            continue
        if m:
            continue  # comment khác: bỏ qua
        first_content = False
        om = OPTION_H.match(st)
        if om:
            opt = {"letter": om.group(1), "title": om.group(2).strip(), "desc": [], "pros": [], "cons": []}
            s["options"].append(opt)
            continue
        if opt is not None:
            if st.startswith("+ "):
                opt["pros"].append(st[2:].strip()); continue
            if st.startswith("- ") or st.startswith("− "):
                opt["cons"].append(st[2:].strip()); continue
            if not st.startswith(("#", ">", "**")):
                opt["desc"].append(st); continue
            opt = None  # gặp khối khác → hết thẻ phương án
        if st.startswith("# "):
            s["h1"] = st[2:].strip(); continue
        if st.startswith("## "):
            s["h2"] = st[3:].strip(); continue
        if st.startswith(">"):
            s["ctx"].append(st.lstrip(">").strip()); s["order"].append("ctx"); continue
        lm = LABELED.match(st)
        if lm:
            s["labeled"].append((lm.group(1).strip(), lm.group(2).strip())); s["order"].append("lab"); continue
        if re.match(r"^([-*]|\d+[.)])\s+", st):
            s["items"].append(re.sub(r"^([-*]|\d+[.)])\s+", "", st)); s["order"].append("li"); continue
        s["paras"].append(st); s["order"].append("p")
    layout = s["dir"].get("layout")
    if not layout:
        layout = "title" if (idx == 0 and s["h1"]) else ("oq" if s["options"] else "bullets")
    s["layout"] = layout
    return s


# ----------------------------------------------------------------- lint
def visible_texts(s):
    """Toàn bộ chữ khách nhìn thấy trên slide (KHÔNG gồm ghi chú, directive)."""
    out = []
    for k in ("h1", "h2"):
        if s[k]:
            out.append(s[k])
    out += s["ctx"] + s["items"] + s["paras"]
    out += [f"{a}: {b}" for a, b in s["labeled"]]
    for o in s["options"]:
        out += [o["title"]] + o["desc"] + o["pros"] + o["cons"]
    return [plain(x) for x in out]


def lint(fm, slides):
    errs, warns = [], []
    for k in ("type", "meeting", "title", "date"):
        if not fm.get(k):
            warns.append(f"frontmatter thiếu `{k}`")
    if fm.get("type") and fm.get("type") != "meeting-deck":
        warns.append(f"frontmatter type = `{fm.get('type')}` (chuẩn: meeting-deck)")
    dlv = delivery_of(fm)
    if dlv not in DELIVERIES:
        errs.append(f"frontmatter delivery = `{fm.get('delivery')}` — dùng `meeting` (chiếu khi họp) hoặc `async` (gửi khách tự trả lời)")
    if dlv == "async":
        if fm.get("reply_by") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(fm["reply_by"])):
            errs.append("frontmatter reply_by phải là ngày ISO YYYY-MM-DD")
        if not fm.get("reply_to"):
            warns.append("delivery: async nhưng thiếu `reply_to` — slide hướng dẫn sẽ ghi \"gửi lại cho người đã gửi file này\"")
        if any(s["layout"] == "guide" for s in slides):
            errs.append("không viết slide hướng dẫn tay — delivery: async thì build tự chèn")
    has_oq = has_recap = False
    oq_ids = {}
    for s in slides:
        n, lay = s["n"], s["layout"]
        tag = f"slide {n} ({lay})"
        if lay not in LAYOUTS:
            errs.append(f"{tag}: layout không hợp lệ — dùng một trong {sorted(LAYOUTS)}")
            continue
        vis = visible_texts(s)
        for t in vis:
            for m in INTERNAL_ID.finditer(t):
                errs.append(f"{tag}: lộ mã nội bộ `{m.group(0)}` trên slide khách — chuyển vào directive `id:`/`refs:` hoặc ghi chú")
            pm = INTERNAL_PATH.search(t)
            if pm:
                errs.append(f"{tag}: lộ đường dẫn/tên file nội bộ `{pm.group(0)}` — chuyển vào directive `src:` hoặc ghi chú")
        total = sum(len(t) for t in vis)
        lim = LIMITS.get(lay, 600)
        if total > lim:
            errs.append(f"{tag}: quá dày — {total} ký tự hiển thị (tối đa {lim}). Tách slide hoặc chuyển chi tiết vào ghi chú")
        if len(s["items"]) > MAX_BULLETS:
            errs.append(f"{tag}: {len(s['items'])} gạch đầu dòng (tối đa {MAX_BULLETS}) — tách slide")
        if lay == "oq":
            has_oq = True
            q = s["h2"] or s["h1"]
            if not q:
                errs.append(f"{tag}: thiếu câu hỏi (dòng `## …`)")
            elif len(plain(q)) > MAX_QUESTION:
                errs.append(f"{tag}: câu hỏi dài {len(plain(q))} ký tự (tối đa {MAX_QUESTION}) — rút gọn, bối cảnh đưa xuống dòng `>`")
            if sum(len(plain(c)) for c in s["ctx"]) > MAX_CONTEXT:
                errs.append(f"{tag}: bối cảnh dài quá {MAX_CONTEXT} ký tự — đưa chi tiết vào ghi chú")
            ops = s["options"]
            if len(ops) > MAX_OPTIONS:
                errs.append(f"{tag}: {len(ops)} phương án (tối đa {MAX_OPTIONS})")
            letters = [o["letter"] for o in ops]
            if len(set(letters)) != len(letters):
                errs.append(f"{tag}: trùng chữ cái phương án {letters}")
            for o in ops:
                if len(o["pros"]) > MAX_PRO_CON or len(o["cons"]) > MAX_PRO_CON:
                    errs.append(f"{tag}: phương án {o['letter']} có quá {MAX_PRO_CON} ý +/−")
                oc = sum(len(plain(x)) for x in [o["title"]] + o["desc"] + o["pros"] + o["cons"])
                if oc > MAX_OPTION_CHARS:
                    errs.append(f"{tag}: phương án {o['letter']} dài {oc} ký tự (tối đa {MAX_OPTION_CHARS})")
            rec = s["dir"].get("recommend")
            if rec and rec not in letters:
                errs.append(f"{tag}: recommend `{rec}` không khớp phương án nào {letters}")
            if len(ops) == 1:
                warns.append(f"{tag}: chỉ 1 phương án — hoặc thêm phương án thứ hai, hoặc bỏ hẳn để khách tự trả lời")
            oid = s["dir"].get("id")
            if not oid:
                warns.append(f"{tag}: thiếu `id:` — kết quả họp sẽ không truy được về câu hỏi gốc")
            elif oid in oq_ids:
                errs.append(f"{tag}: trùng id `{oid}` với slide {oq_ids[oid]}")
            else:
                oq_ids[oid] = n
            if not s["dir"].get("src"):
                warns.append(f"{tag}: thiếu `src:` — /deck import không biết cập nhật về file nào")
            if not any(a.lower() == DOC_LABEL.lower() for a, _ in s["labeled"]):
                warns.append(f"{tag}: thiếu dòng `**{DOC_LABEL}:**` — khách không biết đọc lại ở tài liệu nào của họ"
                             f" (câu không có tài liệu gốc thì ghi `**Tài liệu:** chưa có trong tài liệu {fm.get('client') or 'khách'} gửi`)")
        if lay == "recap":
            has_recap = True
        if s["dir"].get("time"):
            try:
                float(s["dir"]["time"])
            except ValueError:
                errs.append(f"{tag}: `time:` phải là số phút")
    if has_oq and not has_recap:
        if dlv == "async":
            errs.append("delivery: async mà không có slide `recap` — khách không có nút tải câu trả lời để gửi lại")
        else:
            warns.append("có slide câu hỏi nhưng không có slide `recap` — thiếu chỗ tổng kết + nút xuất kết quả")
    return errs, warns


# ----------------------------------------------------------------- slide hướng dẫn (async)
def guide_slide(fm, has_open_q):
    """Slide hướng dẫn cho khách tự trả lời — máy sinh, câu chữ cố định (AI không viết)."""
    who = str(fm.get("reply_to") or "").strip() or "người đã gửi file này cho anh/chị"
    by = f" **trước ngày {dmy(fm['reply_by'])}**" if fm.get("reply_by") else ""
    steps = [
        "Lưu file về máy rồi mở bằng trình duyệt (Chrome, Edge, Safari) — không mở trong khung xem trước của email hay Zalo",
        "Chuyển trang bằng nút **‹ ›** ở góc dưới bên phải, hoặc phím mũi tên ← →",
        "Mỗi trang là một câu hỏi: bấm vào **thẻ phương án** anh/chị chọn (nhãn *Đề xuất* là gợi ý của đội dự án). "
        "Chưa phù hợp → bấm **Khác** và ghi ý kiến; chưa quyết được → bấm **Cần trao đổi thêm**"
        + ("; câu không có phương án thì gõ câu trả lời vào ô lớn" if has_open_q else ""),
        "Câu trả lời tự lưu — đóng file rồi mở lại vẫn còn, miễn là **cùng máy, cùng trình duyệt**",
        f"Trang **Tổng kết** ở cuối: ghi tên người trả lời, bấm **Tải câu trả lời** rồi gửi file vừa tải cho {who}{by}. "
        "Hoặc bấm **Copy để dán vào email** rồi dán thẳng vào email/Zalo — nội dung đã soạn sẵn thành thư trả lời",
    ]
    return {"n": 0, "dir": {"layout": "guide"}, "h1": None, "h2": "Hướng dẫn trả lời", "ctx": [], "labeled": [],
            "items": steps, "paras": [], "options": [], "notes": [], "order": ["li"] * len(steps), "layout": "guide"}


def with_guide(fm, slides):
    """async: chèn slide hướng dẫn ngay sau bìa (hoặc đầu deck nếu không có bìa), đánh số lại."""
    if delivery_of(fm) != "async":
        return slides
    has_open_q = any(s["layout"] == "oq" and not s["options"] for s in slides)
    at = 1 if slides and slides[0]["layout"] == "title" else 0
    out = slides[:at] + [guide_slide(fm, has_open_q)] + slides[at:]
    for i, s in enumerate(out):
        s["n"] = i + 1
    return out


# ----------------------------------------------------------------- render
def render_block_list(items, cls=""):
    if not items:
        return ""
    c = f' class="{cls}"' if cls else ""
    return f"<ul{c}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"


def render_flow(s):
    """Nội dung theo đúng thứ tự viết (ctx / lab / li / p)."""
    out, i_ctx, i_lab, i_li, i_p = [], 0, 0, 0, 0
    pending_li = []
    order = s["order"] + ["_end"]
    for kind in order:
        if kind != "li" and pending_li:
            out.append(render_block_list(pending_li)); pending_li = []
        if kind == "ctx":
            out.append(f'<div class="ctx"><p>{inline(s["ctx"][i_ctx])}</p></div>'); i_ctx += 1
        elif kind == "lab":
            a, b = s["labeled"][i_lab]; i_lab += 1
            cls = "lab srcdoc" if a.lower() == DOC_LABEL.lower() else "lab"
            out.append(f'<p class="{cls}"><b>{inline(a)}:</b> {inline(b)}</p>')
        elif kind == "li":
            pending_li.append(s["items"][i_li]); i_li += 1
        elif kind == "p":
            out.append(f"<p>{inline(s['paras'][i_p])}</p>"); i_p += 1
    # gộp các ctx liền nhau thành 1 khối
    return "".join(out).replace('</p></div><div class="ctx"><p>', "</p><p>")


def render_slide(s, fm, oq_pos, oq_total, n_total):
    lay = s["layout"]
    cls = {"agenda": "bullets", "goal": "bullets"}.get(lay, lay)
    asy = delivery_of(fm) == "async"
    parts = []
    if lay == "guide":
        parts.append(f"<h2>{inline(s['h2'])}</h2>")
        parts.append("<ol>" + "".join(f"<li>{inline(i)}</li>" for i in s["items"]) + "</ol>")
    elif lay == "title":
        parts.append(f"<h1>{inline(s['h1'] or s['h2'] or fm.get('title', ''))}</h1>")
        parts.append(render_flow(s))
        reply = f"Hạn trả lời {dmy(fm['reply_by'])}" if asy and fm.get("reply_by") else None
        meta = " · ".join(str(x) for x in [fm.get("client"), fm.get("date_display") or fm.get("date"), fm.get("presenter"), reply] if x)
        if meta:
            parts.append(f'<p class="meta">{inline(str(meta))}</p>')
    elif lay == "oq":
        q = s["h2"] or s["h1"] or ""
        group = s["dir"].get("group", "")
        top_l = f"Câu hỏi {oq_pos}/{oq_total}" + (f" · {inline(group)}" if group else "")
        parts.append(f'<div class="oq-top"><span>{top_l}</span><span class="chip" data-s="open">Chưa chốt</span></div>')
        parts.append(f"<h2>{inline(q)}</h2>")
        parts.append(render_flow(s))
        rec = s["dir"].get("recommend")
        if s["options"]:
            cards = []
            for o in s["options"]:
                r = o["letter"] == rec
                body = "".join(f"<p>{inline(d)}</p>" for d in o["desc"])
                lis = "".join(f'<li class="pro">{inline(x)}</li>' for x in o["pros"]) + \
                      "".join(f'<li class="con">{inline(x)}</li>' for x in o["cons"])
                cards.append(
                    f'<div class="opt{" rec" if r else ""}" data-l="{o["letter"]}">'
                    + ('<span class="rtag">Đề xuất</span>' if r else "")
                    + f'<div class="ot"><span class="lt">{o["letter"]}</span><span>{inline(o["title"])}</span></div>'
                    + body + (f"<ul>{lis}</ul>" if lis else "") + "</div>")
            parts.append('<div class="opts">' + "".join(cards) + "</div>")
        btns = "".join(f'<button data-c="{o["letter"]}">{o["letter"]}</button>' for o in s["options"])
        btns += '<button data-c="other">Khác</button>' + \
            f'<button data-c="defer">{"Cần trao đổi thêm" if asy else "Hoãn"}</button>'
        if asy:
            ph = "Ý kiến thêm (nếu có)…" if s["options"] else "Câu trả lời của anh/chị…"
        else:
            ph = "Ghi chú quyết định / câu trả lời của khách…" if s["options"] else "Câu trả lời của khách…"
        field = (f'<textarea class="note" placeholder="{ph}"></textarea>' if not s["options"]
                 else f'<input class="note" type="text" placeholder="{ph}">')
        parts.append(f'<div class="decide"><span class="dl">{"Trả lời" if asy else "Quyết định"}</span>{btns}{field}</div>')
        if not s["options"]:
            cls += " noopts"
    elif lay == "recap":
        parts.append(f"<h2>{inline(s['h2'] or s['h1'] or ('Tổng kết câu trả lời' if asy else 'Tổng kết quyết định'))}</h2>")
        parts.append('<p class="sum"></p>')
        parts.append('<div class="wrapr"><table class="recap"><thead><tr><th>#</th><th>Câu hỏi</th>'
                     f'<th>{"Trả lời" if asy else "Quyết định"}</th><th>Ghi chú</th></tr></thead><tbody></tbody></table></div>')
        parts.append(render_flow(s))
        if asy:
            parts.append('<div class="tools"><input class="who" type="text" placeholder="Họ tên người trả lời">'
                         '<button data-act="download">Tải câu trả lời</button><button class="sec" data-act="copy">Copy để dán vào email</button>'
                         '<button class="sec" data-act="reset">Xoá câu trả lời</button></div>')
        else:
            parts.append('<div class="tools"><button data-act="download">Tải kết quả (.md)</button><button class="sec" data-act="copy">Copy</button><button class="sec" data-act="reset">Xoá để chạy lại</button></div>')
    else:
        if s["h1"]:
            parts.append(f"<h1>{inline(s['h1'])}</h1>")
        if s["h2"]:
            parts.append(f"<h2>{inline(s['h2'])}</h2>")
        parts.append(render_flow(s))
    pct = round(100 * s["n"] / n_total, 2)
    foot = (f'<div class="foot"><span class="fl"><i class="brand-logo"></i><span>{inline(fm.get("footer") or fm.get("title", ""))}</span></span>'
            f'<span>{s["n"]} / {n_total}</span></div>')
    deco = ""
    if lay == "title":
        deco = '<i class="brand-logo"></i><i class="brand-mark"></i>'
    elif lay == "section":
        deco = '<i class="brand-mark"></i>'
    elif lay == "end":
        deco = '<i class="brand-logo"></i>'
    return (f'<section class="slide l-{cls}" data-n="{s["n"]}">{deco}<div class="fit">' + "".join(parts) +
            f'</div>{foot}<div class="bar" style="width:{pct}%"></div></section>')


def notes_html(lines):
    if not lines:
        return ""
    out, items = [], []
    for ln in lines:
        st = ln.strip()
        if not st:
            continue
        if re.match(r"^[-*]\s+", st):
            items.append(re.sub(r"^[-*]\s+", "", st)); continue
        if items:
            out.append(render_block_list(items)); items = []
        out.append(f"<p>{inline(st)}</p>")
    if items:
        out.append(render_block_list(items))
    return "".join(out)


def find_tokens(deck_path):
    d = os.path.dirname(os.path.abspath(deck_path))
    for _ in range(8):
        p = os.path.join(d, "design", "design-tokens.css")
        if os.path.isfile(p):
            return p
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    p = os.path.join(os.getcwd(), "design", "design-tokens.css")
    return p if os.path.isfile(p) else None


def find_brand_root(deck_path):
    d = os.path.dirname(os.path.abspath(deck_path))
    for _ in range(8):
        p = os.path.join(d, "design", "brand")
        if os.path.isdir(p):
            return p
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    p = os.path.join(os.getcwd(), "design", "brand")
    return p if os.path.isdir(p) else None


def resolve_brand(fm, deck_path):
    """Trả (brand_dict|None, thông báo, lỗi). Frontmatter `brand: <slug>` | `none`.
    Không khai: đúng 1 brand trong design/brand/ → dùng brand đó; 0 hoặc nhiều → không brand."""
    want = fm.get("brand")
    if isinstance(want, str) and want.strip().lower() in ("none", "off", "false", ""):
        return None, "tắt (brand: none)", None
    if want is False:
        return None, "tắt (brand: false)", None
    root = find_brand_root(deck_path)
    cands = sorted(x for x in os.listdir(root) if os.path.isfile(os.path.join(root, x, "brand.yml"))) if root else []
    if want:
        if want not in cands:
            return None, None, f"brand `{want}` không có design/brand/{want}/brand.yml (có: {cands or 'không có brand nào'})"
        slug = want
    elif len(cands) == 1:
        slug = cands[0]
    else:
        msg = "không có (chưa có design/brand/*/brand.yml)" if not cands else f"không dùng — có {len(cands)} brand {cands}, khai `brand:` trong frontmatter để chọn"
        return None, msg, None
    bdir = os.path.join(root, slug)
    try:
        b = yaml.safe_load(open(os.path.join(bdir, "brand.yml"), encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return None, None, f"design/brand/{slug}/brand.yml lỗi YAML: {e}"
    b["_dir"], b["_slug"] = bdir, slug
    missing = [f for grp in ("logo", "mark") for f in (b.get(grp) or {}).values()
               if not os.path.isfile(os.path.join(bdir, f))]
    if missing:
        return None, None, f"design/brand/{slug}: thiếu file {missing}"
    note = f"{b.get('name', slug)} (design/brand/{slug}/" + (")" if want else ", tự chọn vì là brand duy nhất)")
    return b, note, None


def brand_css(b):
    import base64
    c = b.get("colors") or {}
    v = []
    if c.get("primary"):
        v.append(f"--d-accent: {c['primary']};")
        v.append(f"--d-hl-text: {c['primary']};")
    if c.get("on-primary"):
        v.append(f"--d-on-accent: {c['on-primary']};")
    if c.get("accent"):
        v.append(f"--d-bar: {c['accent']};")
        v.append(f"--d-hl-border: {c['accent']};")
        v.append(f"--d-hl-bg: color-mix(in srgb, {c['accent']} 28%, #ffffff);")
    for grp in ("logo", "mark"):
        for k, f in (b.get(grp) or {}).items():
            data = base64.b64encode(open(os.path.join(b["_dir"], f), "rb").read()).decode()
            mime = "image/svg+xml" if f.lower().endswith(".svg") else "image/png"
            v.append(f'--brand-{grp}-{k}: url("data:{mime};base64,{data}");')
    return ":root {\n  " + "\n  ".join(v) + "\n}"


def render(fm, slides, deck_path, brand=None):
    """async: KHÔNG nhúng ghi chú / nguồn / refs vào HTML — file đi thẳng tới khách, mở mã nguồn
    là đọc được. Chỉ giữ `id` (khoá ghép câu trả lời); /deck import tra `src` từ deck.md theo `id`."""
    asy = delivery_of(fm) == "async"
    slides = with_guide(fm, slides)
    oq_total = sum(1 for s in slides if s["layout"] == "oq")
    pos, out, data = 0, [], []
    for s in slides:
        if s["layout"] == "oq":
            pos += 1
        out.append(render_slide(s, fm, pos, oq_total, len(slides)))
        item = {"n": s["n"], "layout": s["layout"], "notes": "" if asy else notes_html(s["notes"])}
        if s["dir"].get("time") and not asy:
            item["time"] = float(s["dir"]["time"])
        refs = [r.strip() for r in s["dir"].get("refs", "").split(",") if r.strip()]
        if refs and not asy:
            item["refs"] = refs
        if s["layout"] == "oq":
            item["oq"] = {
                "id": s["dir"].get("id", ""), "src": "" if asy else s["dir"].get("src", ""),
                "recommend": "" if asy else s["dir"].get("recommend", ""),
                "question": plain(s["h2"] or s["h1"] or ""),
                "options": [{"letter": o["letter"], "title": plain(o["title"])} for o in s["options"]],
            }
        data.append(item)
    stem = os.path.splitext(os.path.basename(deck_path))[0]
    base = stem[:-5] if stem.endswith("-deck") else stem
    rel = os.path.relpath(os.path.abspath(deck_path), os.getcwd())
    meta = {
        "id": fm.get("id") or stem, "title": fm.get("title", stem), "meeting": fm.get("meeting", ""),
        "date": str(fm.get("date", "")), "duration": None if asy else fm.get("duration"), "source": rel,
        "delivery": delivery_of(fm), "client": str(fm.get("client") or ""),
        "resultName": f"{base}-tra-loi.md" if asy else f"{base}-ket-qua.md", "slides": data,
    }
    tok_path = find_tokens(deck_path)
    tokens = ""
    if tok_path:
        tokens = open(tok_path, encoding="utf-8").read()
        tokens = re.sub(r"^@import[^;]*;\s*$", "", tokens, flags=re.M)  # bỏ font online → chạy offline
    tpl = open(TEMPLATE, encoding="utf-8").read()
    page = (tpl.replace("{{TITLE}}", html.escape(str(fm.get("title", stem))))
               .replace("{{TOKENS}}", tokens)
               .replace("{{BRAND}}", brand_css(brand) if brand else "")
               .replace("{{BODY_CLASS}}", " ".join(c for c in ["branded" if brand else "", "async" if asy else ""] if c))
               .replace("{{SLIDES}}", "\n".join(out))
               .replace("{{DATA}}", json.dumps(meta, ensure_ascii=False).replace("</", "<\\/")))
    return page, tok_path


# ----------------------------------------------------------------- verify (Chrome headless)
def find_chrome():
    """Ưu tiên chrome-headless-shell (Playwright cache) — nhẹ, không cần dịch vụ hệ thống;
    sau đó Chrome for Testing (puppeteer cache của mmdc); cuối cùng Chrome cài trên máy."""
    import glob
    home = os.path.expanduser("~")
    pats = [
        f"{home}/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-*/chrome-headless-shell",
        f"{home}/.cache/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-*/chrome-headless-shell",
        f"{home}/.puppeteer-cache/chrome/*/chrome-mac-*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing",
        f"{home}/.cache/puppeteer/chrome/*/chrome-*/chrome",
    ]
    for p in pats:
        found = sorted(glob.glob(p))
        if found:
            return found[-1]
    for c in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome") or "", shutil.which("chromium") or ""):
        if c and os.path.exists(c):
            return c
    return None


def chrome_args(chrome, prof):
    a = [chrome, "--no-sandbox", "--disable-gpu", f"--user-data-dir={prof}", "--hide-scrollbars",
         "--window-size=1280,720"]
    if "headless-shell" not in chrome:
        a.insert(1, "--headless=new")
    return a


def export_pdf(out_path, pdf_path):
    """In HTML (?pdf) ra PDF bằng Chrome headless — mỗi slide 1 trang. Trả (số trang | None, ghi chú)."""
    chrome = find_chrome()
    if not chrome:
        return None, "Không tìm thấy Chrome — KHÔNG xuất được PDF"
    url = "file://" + os.path.abspath(out_path) + "?pdf=1"
    with tempfile.TemporaryDirectory() as prof:
        cmd = chrome_args(chrome, prof) + ["--virtual-time-budget=3000", "--no-pdf-header-footer",
                                           f"--print-to-pdf={os.path.abspath(pdf_path)}", url]
        try:
            subprocess.run(cmd, capture_output=True, timeout=120)
        except subprocess.TimeoutExpired:
            return None, f"Chrome treo quá 120s ({os.path.basename(chrome)})"
    if not os.path.exists(pdf_path):
        return None, "Chrome không ghi ra file PDF"
    data = open(pdf_path, "rb").read()
    return len(re.findall(rb"/Type\s*/Page[^s]", data)), ""


def verify(out_path, n_slides, shots_dir=None):
    chrome = find_chrome()
    if not chrome:
        return None, ["Không tìm thấy Chrome — bỏ qua verify (KHÔNG coi là PASS)"]
    url = "file://" + os.path.abspath(out_path)
    with tempfile.TemporaryDirectory() as prof:
        cmd = chrome_args(chrome, prof) + ["--virtual-time-budget=3000", "--dump-dom", url + "?verify=1"]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        except subprocess.TimeoutExpired:
            return None, [f"Chrome treo quá 60s ({os.path.basename(chrome)})"]
        m = re.search(r'<pre id="verify-result">(.*?)</pre>', r.stdout, re.S)
        if not m:
            return None, ["Chrome không trả kết quả đo — JS có thể lỗi khi chạy (mở file kiểm tay)"]
        res = json.loads(html.unescape(m.group(1)))
        if shots_dir:
            os.makedirs(shots_dir, exist_ok=True)
            for i in range(1, n_slides + 1):
                try:
                    subprocess.run(chrome_args(chrome, prof) + [
                        "--virtual-time-budget=1500",
                        f"--screenshot={os.path.join(shots_dir, f'slide-{i:02d}.png')}",
                        f"{url}#/{i}"], capture_output=True, timeout=60)
                except subprocess.TimeoutExpired:
                    pass
    return res, []


# ----------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="deck.md → HTML trình chiếu")
    ap.add_argument("deck")
    ap.add_argument("--out")
    ap.add_argument("--lint-only", action="store_true")
    ap.add_argument("--verify", action="store_true", help="đo tràn chữ từng slide bằng Chrome headless")
    ap.add_argument("--shots", help="chụp PNG từng slide vào thư mục này (kèm --verify)")
    ap.add_argument("--force", action="store_true", help="vẫn ghi HTML dù lint lỗi")
    ap.add_argument("--pdf", nargs="?", const="", metavar="PATH",
                    help="xuất thêm PDF bản đọc nhanh (bỏ hướng dẫn/tổng kết/nút trả lời); mặc định cạnh file HTML")
    a = ap.parse_args()

    try:
        src = open(a.deck, encoding="utf-8").read()
        fm, body = split_frontmatter(src)
        slides = [parse_slide(c, i) for i, c in enumerate(split_slides(body))]
    except (OSError, ParseError, yaml.YAMLError) as e:
        print(f"DECK-ERROR: {e}", file=sys.stderr)
        sys.exit(2)
    if not slides:
        print("DECK-ERROR: không có slide nào", file=sys.stderr)
        sys.exit(2)

    errs, warns = lint(fm, slides)
    brand, bnote, berr = resolve_brand(fm, a.deck)
    if berr:
        errs.append(berr)
    n_oq = sum(1 for s in slides if s["layout"] == "oq")
    asy = delivery_of(fm) == "async"
    n_out = len(slides) + (1 if asy else 0)
    print(f"[deck] {len(slides)} slide · {n_oq} câu hỏi · nguồn {a.deck}")
    print(f"  Hình thức:                      " + ("gửi khách tự trả lời (async) — tự chèn slide Hướng dẫn trả lời, KHÔNG nhúng ghi chú/nguồn" if asy else "chiếu trong buổi họp (meeting)"))
    print(f"  Mức 1 — Cú pháp deck.md:        PASS (parse được {len(slides)} slide)")
    print(f"  Mức 2 — Lint nội dung/mật độ:   {'FAIL' if errs else 'PASS'} ({len(errs)} lỗi, {len(warns)} cảnh báo)")
    for e in errs:
        print(f"    ✗ {e}")
    for w in warns:
        print(f"    ⚠ {w}")
    if a.lint_only:
        print("  (lint-only — không ghi HTML)")
        sys.exit(1 if errs else 0)
    if errs and not a.force:
        print("  → KHÔNG ghi HTML. Sửa deck.md rồi chạy lại (hoặc --force nếu chấp nhận).")
        sys.exit(1)

    page, tok = render(fm, slides, a.deck, brand)
    out = a.out or re.sub(r"\.md$", "", a.deck) + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"  Brand:                          {bnote}")
    print(f"  Design tokens:                  {os.path.relpath(tok) if tok else 'KHÔNG thấy design/design-tokens.css — dùng màu dự phòng trung tính'}")
    print(f"  HTML:                           {out} ({len(page.encode()) // 1024} KB)")

    bad = False
    if a.verify or a.shots:
        res, notes = verify(out, n_out, a.shots)
        if res is None:
            print(f"  Mức 3 — Hiển thị (Chrome):      SKIPPED — {'; '.join(notes)}")
        else:
            over = [r for r in res if r["overflow"]]
            shrunk = [r for r in res if r["scale"] < 1 and not r["overflow"]]
            print(f"  Mức 3 — Hiển thị (Chrome):      {'FAIL' if over else 'PASS'} ({len(res)} slide đo)")
            for r in over:
                print(f"    ✗ slide {r['n']}: tràn khung kể cả khi đã co chữ còn {int(r['scale'] * 100)}%")
            for r in shrunk:
                print(f"    ⚠ slide {r['n']}: phải co chữ còn {int(r['scale'] * 100)}% mới vừa — nên rút gọn")
            bad = bool(over)
            if a.shots:
                print(f"  Ảnh chụp:                       {a.shots}/slide-NN.png")
    else:
        print("  Mức 3 — Hiển thị (Chrome):      SKIPPED (chạy kèm --verify để đo tràn chữ)")
    if a.pdf is not None:
        pdf_path = a.pdf or re.sub(r"\.html$", "", out) + ".pdf"
        n_skip = sum(1 for s in slides if s["layout"] == "recap") + (1 if asy else 0)
        pages, note = export_pdf(out, pdf_path)
        if pages is None:
            print(f"  PDF đọc nhanh:                  FAIL — {note}")
            bad = True
        else:
            want = n_out - n_skip
            ok = pages == want
            print(f"  PDF đọc nhanh:                  {'PASS' if ok else 'FAIL'} — {pdf_path} ({pages} trang"
                  f"{'' if ok else f', cần {want}'}; bỏ hướng dẫn, tổng kết, nút trả lời)")
            bad = bad or not ok
    print("  Mức 4 — Nghiệp vụ:              CHƯA được máy kiểm — câu hỏi/phương án/đề xuất phải khớp nguồn, BA tự soi")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
