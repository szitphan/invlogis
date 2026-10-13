#!/bin/bash
# PreToolUse Write|Edit — máy chặn cho .claude/rules/worktree.md Mục 2.
#
# Vùng ghi xét theo VỊ TRÍ FILE (không theo cwd — phiên ở main vẫn ghi được path tuyệt đối vào worktree):
#   1. File nằm trong worktree feature (repo của file ở branch feat/<slug> và có docs/<slug>/)
#      → chỉ được ghi trong docs/<slug>/**.
#   2. Phiên đang đứng trong worktree feature (cwd ở branch feat/<slug>) → không được ghi ra ngoài
#      chính worktree đó (vd sang checkout chính hay worktree khác).
# Worktree không gắn feature (feat/skill-x, không có docs/skill-x/) → không chặn.
# Hook script (logbook, stale, kg) ghi bằng shell, không qua Write/Edit → không bị chặn.

set -u
command -v jq >/dev/null 2>&1 || { cat >/dev/null; exit 0; }
. "$(dirname "$0")/lib-root.sh"
IN="$(cat)"
FILE="$(printf '%s' "$IN" | jq -r '.tool_input.file_path // .tool_input.path // empty')"
CWD="$(printf '%s' "$IN" | jq -r '.cwd // empty')"
[ -z "$FILE" ] && exit 0
CWD="${CWD:-$(pwd)}"

deny() {
    echo "worktree-guard: $1 Ghi vào run card mục 'Cần sửa trên main' (hoặc báo người dùng), sửa trên main rồi wt.sh sync. Rule: .claude/rules/worktree.md Mục 2." >&2
    exit 2
}
# feature slug của 1 repo root nếu là worktree feature, rỗng nếu không
feature_of() {
    local br; br="$(branch_of "$1")"
    case "$br" in feat/*) [ -d "$1/docs/${br#feat/}" ] && printf '%s' "${br#feat/}" ;; esac
}

ABS="$(abs_phys "$FILE" "$CWD")"
case "$ABS" in */../*|*/..) deny "đường dẫn chứa '..' chưa resolve được: $FILE." ;; esac

# Luật 1 — theo repo chứa file
FROOT="$(root_of "$ABS")"
if [ -n "$FROOT" ]; then
    FROOT="$(cd "$FROOT" && pwd -P)"
    FSLUG="$(feature_of "$FROOT")"
    if [ -n "$FSLUG" ]; then
        case "$ABS" in
            "$FROOT/docs/$FSLUG/"*) ;;
            *) deny "worktree feat/$FSLUG chỉ được ghi trong docs/$FSLUG/** — chặn ghi ${ABS#$FROOT/}." ;;
        esac
    fi
fi

# Luật 2 — phiên đứng trong worktree feature không ghi ra ngoài worktree của mình
CROOT="$(git -C "$CWD" rev-parse --show-toplevel 2>/dev/null || true)"
if [ -n "$CROOT" ]; then
    CROOT="$(cd "$CROOT" && pwd -P)"
    CSLUG="$(feature_of "$CROOT")"
    if [ -n "$CSLUG" ] && [ "$FROOT" != "$CROOT" ]; then
        deny "phiên đang ở worktree feat/$CSLUG — không ghi ra ngoài worktree: $ABS."
    fi
fi
exit 0
