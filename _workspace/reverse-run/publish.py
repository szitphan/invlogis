#!/usr/bin/env python3
"""Chép bộ reverse đã ghép + đã qua gate (staging/{feature}/_final/) sang docs/_reverse/{feature}/,
ghi changelog cho từng file .md qua hook auto-changelog.sh, đánh dấu feature done trong reverse-plan.json.

CHỈ chạy sau khi người dùng duyệt L1. Từ chối ghi đè thư mục đích đã có (lần chạy lại phải qua L2 riêng).

Usage: python3 _workspace/reverse-run/publish.py <feature> [--author @szitphan]
"""
import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
PLAN_P = ROOT / "docs/_reverse/reverse-plan.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("feature")
    ap.add_argument("--author", default="@szitphan")
    a = ap.parse_args()
    src = RUN / "staging" / a.feature / "_final"
    dst = ROOT / "docs/_reverse" / a.feature
    if not src.exists():
        raise SystemExit(f"Chưa có {src.relative_to(ROOT)} — chạy assemble.py trước.")
    if dst.exists():
        raise SystemExit(f"{dst.relative_to(ROOT)} đã có — không ghi đè. Cập nhật phải qua L2 riêng.")
    r = subprocess.run(["python3", str(RUN / "gates.py"), a.feature, "--no-mermaid"], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("Gate chưa qua — không chép:\n" + r.stdout)
    shutil.copytree(src, dst)
    env = dict(os.environ, CLAUDE_SKILL_NAME="/reverse-doc", CLAUDE_CHANGELOG_AUTHOR=a.author,
               CLAUDE_CHANGELOG_NOTE=f"reverse SRS cũ (SRC-22/23) feature {a.feature}")
    files = sorted(dst.rglob("*.md"))
    for p in files:
        subprocess.run(["bash", str(ROOT / ".claude/hooks/auto-changelog.sh"), str(p)], env=env, cwd=ROOT)
    plan = json.loads(PLAN_P.read_text(encoding="utf-8"))
    for f in plan["features"]:
        if f["slug"] == a.feature:
            f["status"] = "done"
            for p in f["parts"]:
                p["status"] = "done"
    PLAN_P.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ {len(files)} file → {dst.relative_to(ROOT)} · changelog ghi · plan: {a.feature} done")


if __name__ == "__main__":
    main()
