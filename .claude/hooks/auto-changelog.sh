#!/bin/bash
# Ghi 1 dòng sự kiện vào log toàn vault sau mỗi Write/Edit doc file.
#
# Contract (per .claude/rules/changelog.md): lịch sử thay đổi sống ở MỘT log
# toàn vault — KHÔNG ghi changelog: vào frontmatter, KHÔNG routing file con → file cha.
# Hook ghi vào file mảnh theo branch; _workspace/changelog.md dựng lại từ mảnh.
#
# Format: bảng Markdown 5 cột, 1 dòng = 1 sự kiện, append cuối file:
#   | {date} | {skill} | {@author} | `{file-path}` | {note} |
# Skill set env CLAUDE_SKILL_NAME / CLAUDE_CHANGELOG_NOTE / CLAUDE_CHANGELOG_AUTHOR
# trước khi Write/Edit; thiếu env → fallback "manual | git user.name | manual edit".
#
# Ký tự "|" trong note bị escape thành "\|" để không phá cấu trúc cột khi render.

set -u

FILE="${1:-}"
if [ -z "$FILE" ] && [ ! -t 0 ]; then
    if command -v jq >/dev/null 2>&1; then
        FILE="$(cat | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null)"
    else
        echo "auto-changelog.sh: jq không có trong PATH, không đọc được tool input qua stdin — hook bỏ qua." >&2
        cat >/dev/null
    fi
fi

# Claude Code có thể truyền absolute path — chuẩn hóa về path tương đối project root.
PROJECT_PATH="${PROJECT_PATH:-$(pwd)}"
FILE="${FILE#$PROJECT_PATH/}"

[ "${AUTO_CHANGELOG:-true}" != "true" ] && exit 0
[[ ! "$FILE" =~ ^(docs|design)/.+\.md$ ]] && exit 0
[[ "$FILE" =~ feature-list\.md$ ]] && exit 0
[[ "$FILE" =~ README\.md$ ]] && exit 0
[[ "$FILE" =~ /_shared/ ]] && exit 0
[[ "$FILE" =~ /exports/ ]] && exit 0
[[ "$FILE" =~ /inbox/ ]] && exit 0
[[ "$FILE" =~ /_runs/ ]] && exit 0   # run card /run-task: nhật ký chạy riêng, không log từng bước
[ ! -f "$FILE" ] && exit 0

DATE=$(date +%Y-%m-%d)
SKILL="${CLAUDE_SKILL_NAME:-manual}"
NOTE="${CLAUDE_CHANGELOG_NOTE:-manual edit}"
AUTHOR="${CLAUDE_CHANGELOG_AUTHOR:-}"
[ -z "$AUTHOR" ] && AUTHOR="$(git config user.name 2>/dev/null || true)"
AUTHOR="${AUTHOR:-unknown}"

# Escape cell tự do (note, author, skill) — giữ nguyên cấu trúc bảng:
# newline/CR → space (1 sự kiện PHẢI là đúng 1 dòng bảng), "|" → "\|".
escape_cell() { printf '%s' "$1" | tr '\r\n' '  ' | sed 's/|/\\|/g'; }
SKILL="$(escape_cell "$SKILL")"
NOTE="$(escape_cell "$NOTE")"
AUTHOR="$(escape_cell "$AUTHOR")"

LINE="| $DATE | $SKILL | $AUTHOR | \`$FILE\` | $NOTE |"

# Ghi vào file mảnh của branch hiện tại (_workspace/changelog.d/{ngày}--{branch}.md) rồi dựng lại
# _workspace/changelog.md (file sinh ra, gitignore). Nhiều worktree ghi song song không xung đột.
# logbook.py tự dedupe + append O_APPEND. Xem .claude/rules/changelog.md.
python3 "$PROJECT_PATH/_scripts/logbook.py" add changelog "$LINE"

exit 0
