#!/bin/bash
# Khoá Figma cho chế độ chạy — plugin Figma chỉ có 1 kết nối, nên mỗi lúc chỉ 1 lần chạy được vẽ.
# Khoá nằm trong thư mục .git CHUNG (git-common-dir) → mọi worktree cùng thấy, không bị commit.
#
#   _scripts/figma-lock.sh acquire <feature>   lấy khoá; đang bị giữ → exit 1 + in ai giữ
#   _scripts/figma-lock.sh release <feature>   trả khoá (chỉ người giữ trả được; --force để gỡ khoá treo)
#   _scripts/figma-lock.sh status              in người giữ hoặc "rảnh"
# Khoá quá 3 giờ coi là treo (phiên chết) → acquire được, in cảnh báo.
set -u
LOCK="$(git rev-parse --path-format=absolute --git-common-dir)/figma-run.lock"
STALE_SEC=$((3 * 3600))
who() { cat "$LOCK" 2>/dev/null; }
age() { echo $(( $(date +%s) - $(stat -f %m "$LOCK" 2>/dev/null || stat -c %Y "$LOCK") )); }

case "${1:-status}" in
  acquire)
    f="${2:?thiếu <feature>}"
    if [ -f "$LOCK" ]; then
        cur="$(who)"
        if [ "${cur%% *}" = "$f" ]; then echo "đã giữ: $cur"; exit 0; fi
        if [ "$(age)" -lt "$STALE_SEC" ]; then echo "Figma đang bận: $cur" >&2; exit 1; fi
        echo "⚠ khoá treo quá 3 giờ ($cur) — lấy lại" >&2
    fi
    echo "$f $(date '+%Y-%m-%d %H:%M')" > "$LOCK"; echo "✓ giữ khoá Figma: $f" ;;
  release)
    f="${2:?thiếu <feature>}"
    [ -f "$LOCK" ] || { echo "khoá đang rảnh"; exit 0; }
    cur="$(who)"
    if [ "${cur%% *}" != "$f" ] && [ "${3:-}" != "--force" ]; then echo "khoá do '$cur' giữ, không phải $f (--force để gỡ)" >&2; exit 1; fi
    rm -f "$LOCK"; echo "✓ đã trả khoá Figma" ;;
  status) [ -f "$LOCK" ] && echo "giữ bởi: $(who)" || echo "rảnh" ;;
  *) sed -n '2,9p' "$0"; exit 1 ;;
esac
