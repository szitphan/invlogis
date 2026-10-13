#!/bin/bash
# Đồng bộ sổ nguồn docs-input/README.md + backlog _workspace/backlog.md.
# Dùng: intake-sync.sh session   (SessionStart — in task đang mở)
#       intake-sync.sh prompt    (UserPromptSubmit — chỉ in khi có thay đổi, vd file mới thả vào docs-input)
#       intake-sync.sh edit      (PostToolUse Write|Edit — im lặng trừ khi có thay đổi)
cd "${CLAUDE_PROJECT_DIR:-$(pwd)}" || exit 0
[ -f _scripts/intake-sync.py ] || exit 0
# Sổ nguồn + backlog là file dùng chung, chỉ ghi trên main (.claude/rules/worktree.md).
# Worktree/branch feature: chạy --dry-run (vẫn in tóm tắt, không ghi) → không sinh xung đột khi land.
RO=""
[ "$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" = "main" ] || RO="--dry-run"
case "${1:-edit}" in
  session) python3 _scripts/intake-sync.py --quiet --summary $RO ;;
  *)       cat >/dev/null 2>&1; python3 _scripts/intake-sync.py --quiet $RO ;;
esac
exit 0
