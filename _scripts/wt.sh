#!/bin/bash
# Worktree theo feature — chạy song song nhiều feature, mỗi feature 1 thư mục + 1 branch riêng.
# Quy ước: .claude/rules/worktree.md
#
#   _scripts/wt.sh new  <slug>     tạo ../{repo}-wt/<slug> trên branch feat/<slug> (từ main)
#   _scripts/wt.sh list            liệt kê worktree + số commit chưa land + file chưa commit
#   _scripts/wt.sh sync <slug>     kéo main mới nhất vào feat/<slug> (merge thường, chạy trong worktree)
#   _scripts/wt.sh land <slug>     từ main: squash feat/<slug> vào index của main — KHÔNG tự commit
#   _scripts/wt.sh drop <slug>     xoá worktree + branch (từ chối nếu còn thay đổi chưa land; --force để bỏ qua)
#
# Script không bao giờ commit hay push thay người dùng (commit thủ công, block-push.sh chặn push).

set -euo pipefail

MAIN_DIR="$(git rev-parse --path-format=absolute --git-common-dir)"; MAIN_DIR="${MAIN_DIR%/.git}"
REPO="$(basename "$MAIN_DIR")"
WT_ROOT="$(dirname "$MAIN_DIR")/${REPO}-wt"

die() { echo "wt: $*" >&2; exit 1; }
need_slug() {
    [ -n "${1:-}" ] || die "thiếu <slug>"
    [[ "$1" =~ ^[a-z0-9][a-z0-9-]{0,49}$ ]] || die "slug phải kebab-case ASCII ≤50 ký tự: $1"
}
on_main_checkout() {
    [ "$(git -C "$MAIN_DIR" rev-parse --abbrev-ref HEAD)" = "main" ] || die "checkout chính ($MAIN_DIR) phải đang ở main"
}
# Dọn file sinh ra + làm tươi sổ dùng chung sau khi nội dung đổi (land/sync).
refresh() {
    local dir="$1"
    python3 "$dir/_scripts/logbook.py" build >/dev/null
    mkdir -p "$dir/_workspace/kg" && touch "$dir/_workspace/kg/.dirty"
    if [ "$(git -C "$dir" rev-parse --abbrev-ref HEAD)" = "main" ] && [ -f "$dir/_scripts/intake-sync.py" ]; then
        (cd "$dir" && python3 _scripts/intake-sync.py --quiet) || true
    fi
}
# File branch đã đổi so với điểm tách khỏi main mà nội dung vẫn khác main → chưa land.
unlanded() {
    local br="$1" base files
    base="$(git -C "$MAIN_DIR" merge-base main "$br")"
    files="$(git -C "$MAIN_DIR" diff --name-only "$base" "$br")"
    [ -z "$files" ] && return 0
    # shellcheck disable=SC2086
    git -C "$MAIN_DIR" diff --name-only main "$br" -- $files
}

cmd="${1:-list}"; slug="${2:-}"
case "$cmd" in
  new)
    need_slug "$slug"; on_main_checkout
    dir="$WT_ROOT/$slug"; br="feat/$slug"
    [ -e "$dir" ] && die "đã có $dir"
    git -C "$MAIN_DIR" show-ref --quiet "refs/heads/$br" && die "branch $br đã tồn tại"
    if [ -n "$(git -C "$MAIN_DIR" status --porcelain)" ]; then
        echo "⚠ main còn thay đổi chưa commit — worktree tạo từ commit main gần nhất, KHÔNG mang theo các thay đổi đó."
    fi
    mkdir -p "$WT_ROOT"
    git -C "$MAIN_DIR" worktree add -q -b "$br" "$dir" main
    # File local không track nhưng cần để chạy phiên Claude giống checkout chính.
    [ -f "$MAIN_DIR/.claude/settings.local.json" ] && cp "$MAIN_DIR/.claude/settings.local.json" "$dir/.claude/"
    refresh "$dir"
    echo "✓ $dir  (branch $br)"
    echo "  Mở phiên Claude tại thư mục đó. Xong việc: commit trong worktree → từ main chạy: _scripts/wt.sh land $slug"
    ;;
  list)
    git -C "$MAIN_DIR" worktree list --porcelain | awk '/^worktree /{d=$2} /^branch /{sub("refs/heads/","",$2); print d"\t"$2}' |
    while IFS=$'\t' read -r d br; do
        [ "$br" = "main" ] && { printf '%-28s %s\n' "main" "$d"; continue; }
        ahead="$(git -C "$MAIN_DIR" rev-list --count "main..$br" 2>/dev/null || echo ?)"
        dirty="$(git -C "$d" status --porcelain 2>/dev/null | wc -l | tr -d ' ')"
        pending="$(unlanded "$br" | grep -c . || true)"
        printf '%-28s %s  · %s commit · %s file chưa commit · %s file chưa land\n' "$br" "$d" "$ahead" "$dirty" "$pending"
    done
    ;;
  sync)
    need_slug "$slug"; dir="$WT_ROOT/$slug"
    [ -d "$dir" ] || die "không có worktree $dir"
    [ -z "$(git -C "$dir" status --porcelain)" ] || die "worktree còn thay đổi chưa commit — commit trước khi sync"
    git -C "$dir" merge --no-edit main
    refresh "$dir"
    echo "✓ feat/$slug đã có main mới nhất"
    ;;
  land)
    need_slug "$slug"; on_main_checkout
    dir="$WT_ROOT/$slug"; br="feat/$slug"
    git -C "$MAIN_DIR" show-ref --quiet "refs/heads/$br" || die "không có branch $br"
    [ ! -d "$dir" ] || [ -z "$(git -C "$dir" status --porcelain)" ] || die "worktree $dir còn thay đổi chưa commit"
    [ -z "$(git -C "$MAIN_DIR" diff --cached --name-only)" ] || die "index của main đang có file staged — commit/unstage trước khi land"
    if ! git -C "$MAIN_DIR" merge --squash "$br"; then
        echo "✗ xung đột khi squash — xử lý trong $MAIN_DIR rồi commit, hoặc 'git -C $MAIN_DIR merge --abort'." >&2
        exit 1
    fi
    refresh "$MAIN_DIR"
    echo "✓ đã squash $br vào index của main (CHƯA commit). Xem: git diff --cached --stat"
    echo "  Commit xong → _scripts/wt.sh drop $slug"
    ;;
  drop)
    need_slug "$slug"; dir="$WT_ROOT/$slug"; br="feat/$slug"
    if [ "${3:-}" != "--force" ]; then
        [ ! -d "$dir" ] || [ -z "$(git -C "$dir" status --porcelain)" ] || die "worktree còn thay đổi chưa commit (--force để bỏ)"
        if git -C "$MAIN_DIR" show-ref --quiet "refs/heads/$br"; then
            left="$(unlanded "$br")"
            [ -z "$left" ] || die "feat/$slug còn file chưa land vào main:
$left
(land + commit trước, hoặc --force để bỏ)"
        fi
    fi
    [ -d "$dir" ] && git -C "$MAIN_DIR" worktree remove ${3:+--force} "$dir"
    git -C "$MAIN_DIR" show-ref --quiet "refs/heads/$br" && git -C "$MAIN_DIR" branch -D "$br" >/dev/null
    git -C "$MAIN_DIR" worktree prune
    echo "✓ đã xoá $dir + $br"
    ;;
  *) sed -n '2,12p' "$0"; exit 1 ;;
esac
