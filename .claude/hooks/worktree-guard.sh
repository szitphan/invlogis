#!/bin/bash
# PreToolUse Write|Edit — máy chặn cho .claude/rules/worktree.md Mục 2.
#
# Phiên/agent đang ở worktree feature (branch feat/<slug> VÀ có docs/<slug>/) chỉ được ghi trong
# docs/<slug>/**. Ghi ra ngoài (đồ dùng chung, feature khác, checkout chính) → chặn (exit 2), lý do
# trả về cho Claude để ghi thành "cần sửa trên main" thay vì sửa tạm.
# Worktree không gắn feature (vd feat/skill-x, không có docs/skill-x/) → không chặn.
# Hook script (logbook, stale, kg) ghi file bằng shell, không qua Write/Edit → không bị chặn.

set -u
command -v jq >/dev/null 2>&1 || { cat >/dev/null; exit 0; }
IN="$(cat)"
FILE="$(printf '%s' "$IN" | jq -r '.tool_input.file_path // .tool_input.path // empty')"
CWD="$(printf '%s' "$IN" | jq -r '.cwd // empty')"
[ -z "$FILE" ] && exit 0
CWD="${CWD:-$(pwd)}"

BR="$(git -C "$CWD" rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
case "$BR" in feat/*) ;; *) exit 0 ;; esac
SLUG="${BR#feat/}"
TOP="$(git -C "$CWD" rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$TOP" ] && [ -d "$TOP/docs/$SLUG" ] || exit 0

case "$FILE" in /*) ABS="$FILE" ;; *) ABS="$CWD/$FILE" ;; esac
# Chuẩn hoá: thư mục cha có thể chưa tồn tại (Write file mới) → resolve phần đã có.
DIR="$(dirname "$ABS")"; REST="$(basename "$ABS")"
while [ ! -d "$DIR" ] && [ "$DIR" != "/" ]; do REST="$(basename "$DIR")/$REST"; DIR="$(dirname "$DIR")"; done
ABS="$(cd "$DIR" && pwd -P)/$REST"
TOP="$(cd "$TOP" && pwd -P)"

case "$ABS" in
    "$TOP/docs/$SLUG/"*) exit 0 ;;
esac

REL="${ABS#$TOP/}"
[ "$REL" = "$ABS" ] && REL="$ABS (ngoài worktree)"
echo "worktree-guard: worktree feat/$SLUG chỉ được ghi trong docs/$SLUG/** — chặn ghi $REL. Ghi vào run card mục 'Cần sửa trên main' (hoặc báo người dùng), sửa trên main rồi wt.sh sync. Rule: .claude/rules/worktree.md Mục 2." >&2
exit 2
