#!/bin/bash
# DS v2 stale hook (DEC-302, .claude/rules/ds-stale.md)
#
# Sửa foundation (foundations.md, icons.md, tokens.css/json) hoặc component (md, _work/<slug>/page.json|answers.json)
# → chạy `ds-deps.py check --write --backlog`: component có con lồng trong nó (bắc cầu, tra qua `kg impact`) hoặc
# foundation nó dùng đổi phiên bản so với mốc `built` bị đánh `status: stale` + task backlog.
# Chỉ trên main (sổ + backlog là đồ dùng chung, .claude/rules/worktree.md). Im lặng khi không có gì stale.
set -u
FILE="${1:-}"
if [ -z "$FILE" ] && [ ! -t 0 ]; then
    if command -v jq >/dev/null 2>&1; then
        FILE="$(cat | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null)"
    else
        cat >/dev/null; exit 0
    fi
fi
case "$FILE" in
    */design-system/foundations/*.md|*/design-system/tokens.css|*/design-system/tokens.json) ;;
    */design-system/components/_deps.json) ;;
    */design-system/components/_work/*/page.json|*/design-system/components/_work/*/answers.json) ;;
    */design-system/components/_*) exit 0 ;;
    */design-system/components/*/*.md) ;;
    *) exit 0 ;;
esac
cd "${CLAUDE_PROJECT_DIR:-$(pwd)}" || exit 0
[ -f _scripts/ds-deps.py ] || exit 0
[ "$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" = "main" ] || exit 0
OUT="$(python3 _scripts/ds-deps.py check --write --backlog 2>/dev/null | grep -E '^(⚠|Thêm)')"
[ -n "$OUT" ] && printf '[ds-stale]\n%s\n' "$OUT"
exit 0
