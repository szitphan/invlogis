#!/usr/bin/env python3
"""Dựng lại số liệu trang "Token Invlogis 30 ngày" (artifact 9870c7fb-…) từ transcript Claude Code.

Đọc ~/.claude/projects/-Users-…-invlogis*/ (phiên chính + agent con trong {sid}/subagents/, gồm cả worktree),
tính tiền theo bảng giá ghi ở chân trang, rồi thay khối `const D = {...}` trong HTML.

  python3 _scripts/token-usage.py --html <trang.html> [--out <ra.html>] [--days 30] [--json <D.json>]
"""
import argparse, glob, json, os, re
from collections import defaultdict
from datetime import datetime, timedelta, timezone

ROOT = os.path.expanduser("~/.claude/projects")
PREFIX = "-Users-szit-Desktop-szit-AI-Projects-invlogis"
# $/1 triệu token: vào, ra, đọc cache — ghi cache = 1,25× vào (5 phút) hoặc 2× (1 giờ)
PRICE = {"opus": (4, 20, 0.20), "sonnet": (2, 10, 0.20), "fable": (10, 50, 1.0), "haiku": (0.10, 0.50, 0.01)}
BUILTIN = {"clear", "compact", "model", "context", "cost", "config", "resume", "mcp", "help", "init", "login",
           "logout", "status", "memory", "fast", "effort", "rewind", "exit", "doctor", "permissions", "agents"}
BANDS = [("< 50K", 50e3), ("50–100K", 100e3), ("100–200K", 200e3), ("200–400K", 400e3), ("> 400K", float("inf"))]


def price(model):
    for k, p in PRICE.items():
        if k in (model or ""):
            return p
    return None


def tool_name(n):
    if n.startswith("mcp__"):
        parts = n.split("__")
        return f"{parts[1]}:{'__'.join(parts[2:])}"
    return n


def text_of(content):
    if isinstance(content, str):
        return content
    return " ".join(c.get("text", "") for c in content or [] if isinstance(c, dict) and c.get("type") == "text")


def read_calls(path, since):
    """Trả (calls, user_texts). Mỗi call gộp theo message.id (1 lượt API ghi nhiều dòng, usage lặp lại)."""
    calls, order, users = {}, [], []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") == "user" and not d.get("isMeta"):
                users.append(text_of((d.get("message") or {}).get("content")))
                continue
            if d.get("type") != "assistant":
                continue
            m = d.get("message") or {}
            u, mid = m.get("usage"), m.get("id") or d.get("requestId")
            if not u or not mid or not price(m.get("model")):
                continue
            ts = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00"))
            if ts < since:
                continue
            c = calls.get(mid)
            if c is None:
                c = calls[mid] = {"model": m["model"], "ts": ts, "u": u, "tools": []}
                order.append(mid)
            c["u"] = u  # dòng sau cùng có usage đầy đủ nhất
            for b in m.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    c["tools"].append(tool_name(b.get("name", "?")))
    return [calls[k] for k in order], users


def cost_of(c):
    pin, pout, pread = price(c["model"])
    u = c["u"]
    cc = u.get("cache_creation") or {}
    w1h = cc.get("ephemeral_1h_input_tokens", 0) or 0
    w5m = cc.get("ephemeral_5m_input_tokens", 0) or 0
    wtot = u.get("cache_creation_input_tokens", 0) or 0
    if w1h + w5m < wtot:
        w5m += wtot - w1h - w5m
    parts = {
        "input": (u.get("input_tokens", 0) or 0) * pin,
        "write": (w5m * 1.25 + w1h * 2) * pin,
        "read": (u.get("cache_read_input_tokens", 0) or 0) * pread,
        "output": (u.get("output_tokens", 0) or 0) * pout,
    }
    return {k: v / 1e6 for k, v in parts.items()}, wtot


def session_meta(users):
    title, skills = "", []
    for t in users:
        for s in re.findall(r"<command-name>/?([\w:.-]+)</command-name>", t):
            if s not in BUILTIN and s not in skills:
                skills.append(s)
        if not title:
            if "<command-name>" in t:
                cmd = re.search(r"<command-name>([^<]+)</command-name>", t)
                args = re.search(r"<command-args>([^<]*)</command-args>", t)
                if cmd and cmd.group(1).lstrip("/") not in BUILTIN:
                    title = f"{cmd.group(1)} {args.group(1) if args else ''}".strip()
                continue
            clean = re.sub(r"<([\w-]+)[^>]*>.*?</\1>", " ", t, flags=re.S)
            clean = re.sub(r"<[^>]+>", " ", clean)
            clean = re.sub(r"\s+", " ", clean).strip()
            if clean and not clean.startswith("Caveat:") and not clean.startswith("This session is being continued"):
                title = clean
    return (title or "(không có lời nhắn)")[:90], skills


def build(days):
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=days)).replace(microsecond=0)
    dirs = [d for d in glob.glob(os.path.join(ROOT, PREFIX + "*"))
            if os.path.basename(d) == PREFIX or os.path.basename(d).startswith(PREFIX + "--claude-worktrees-")]
    tot = {"input": 0.0, "write": 0.0, "read": 0.0, "output": 0.0}
    tok = {"inp": 0, "write": 0, "read": 0, "out": 0}
    by_day, by_model, by_tool = defaultdict(float), defaultdict(lambda: [0, 0.0, 0]), defaultdict(lambda: [0, 0.0])
    bands = [[b[0], 0, 0.0] for b in BANDS]
    main_sub = {"main": 0.0, "sub": 0.0}
    rewrite = {"n": 0, "cost": 0.0, "tokens": 0}
    sessions, ncalls = [], 0

    for d in dirs:
        for f in glob.glob(os.path.join(d, "*.jsonl")):
            if os.path.getmtime(f) < since.timestamp():
                continue
            sid = os.path.basename(f)[:-6]
            main, users = read_calls(f, since)
            subs = []
            for sf in glob.glob(os.path.join(d, sid, "subagents", "*.jsonl")):
                subs += read_calls(sf, since)[0]
            if not main and not subs:
                continue
            s = {"cost": 0.0, "sub": 0.0, "read": 0.0, "ctx": [], "sctx": [], "first": None}
            for c, is_sub in [(c, False) for c in main] + [(c, True) for c in subs]:
                parts, wtot = cost_of(c)
                cost = sum(parts.values())
                u = c["u"]
                ctx = (u.get("input_tokens", 0) or 0) + (u.get("cache_read_input_tokens", 0) or 0) + wtot
                ncalls += 1
                for k, v in parts.items():
                    tot[k] += v
                tok["inp"] += u.get("input_tokens", 0) or 0
                tok["write"] += wtot
                tok["read"] += u.get("cache_read_input_tokens", 0) or 0
                tok["out"] += u.get("output_tokens", 0) or 0
                by_day[c["ts"].astimezone().strftime("%Y-%m-%d")] += cost
                bm = by_model[c["model"]]
                bm[0] += 1; bm[1] += cost; bm[2] += ctx + (u.get("output_tokens", 0) or 0)
                for i, (_, hi) in enumerate(BANDS):
                    if ctx < hi:
                        bands[i][1] += 1; bands[i][2] += cost
                        break
                tools = c["tools"] or ["(trả lời chữ)"]
                for t in tools:
                    by_tool[t][0] += 1; by_tool[t][1] += cost / len(tools)
                main_sub["sub" if is_sub else "main"] += cost
                if wtot >= 100e3:
                    rewrite["n"] += 1; rewrite["cost"] += parts["write"]; rewrite["tokens"] += wtot
                s["cost"] += cost; s["read"] += parts["read"]
                if is_sub:
                    s["sub"] += cost; s["sctx"].append(ctx)
                else:
                    s["ctx"].append(ctx)
                if s["first"] is None or c["ts"] < s["first"]:
                    s["first"] = c["ts"]
            title, skills = session_meta(users)
            s["ctx"] = s["ctx"] or s["sctx"]  # lượt / hội thoại TB tính theo phiên chính
            sessions.append({
                "sid": sid[:8], "day": s["first"].astimezone().strftime("%Y-%m-%d"), "title": title, "skills": skills,
                "calls": len(s["ctx"]), "cost": round(s["cost"], 2),
                "avg_ctx": round(sum(s["ctx"]) / len(s["ctx"]), 2), "max_ctx": max(s["ctx"]),
                "sub_cost": round(s["sub"], 2), "read_share": round(s["read"] / s["cost"], 2) if s["cost"] else 0,
            })

    sessions.sort(key=lambda r: -r["cost"])
    by_skill = defaultdict(lambda: [0, 0.0])
    for r in sessions:
        k = r["skills"][0] if r["skills"] else "(không gọi skill)"
        by_skill[k][0] += 1; by_skill[k][1] += r["cost"]
    return {
        "calls": ncalls, "cost": sum(tot.values()), "by_type": tot, "tok_type": tok,
        "by_day": sorted([k, v] for k, v in by_day.items()),
        "by_model": sorted([[k, *v] for k, v in by_model.items()], key=lambda r: -r[2]),
        "main_sub": main_sub, "bands": bands,
        "by_tool": sorted([[k, *v] for k, v in by_tool.items()], key=lambda r: -r[2])[:15],
        "sessions": sessions, "n_sessions": len(sessions),
        "by_skill": sorted([[k, *v] for k, v in by_skill.items()], key=lambda r: -r[2]),
        "rewrite": rewrite, "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "since": since.astimezone().strftime("%Y-%m-%d"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True, help="trang cũ (có khối const D = {...})")
    ap.add_argument("--out", help="ghi trang mới (mặc định đè --html)")
    ap.add_argument("--json", help="ghi thêm D ra file JSON")
    ap.add_argument("--days", type=int, default=30)
    a = ap.parse_args()
    D = build(a.days)
    html = open(a.html, encoding="utf-8").read()
    i = html.index("const D = ") + len("const D = ")
    _, end = json.JSONDecoder().raw_decode(html[i:])
    html = html[:i] + json.dumps(D, ensure_ascii=False) + html[i + end:]
    open(a.out or a.html, "w", encoding="utf-8").write(html)
    if a.json:
        json.dump(D, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{D['since']} → {D['generated']} · {D['n_sessions']} phiên · {D['calls']:,} lượt · ${D['cost']:,.0f}")


if __name__ == "__main__":
    main()
