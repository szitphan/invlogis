#!/usr/bin/env bash
# Tải (hoặc cập nhật) code React của Untitled UI vào design/_ref/untitled-ui/react/ — nguồn tham chiếu cấu tạo cho
# /figma-component --html (vòng 0). Thư mục này gitignore: chỉ đọc, không sửa, không commit.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/design/_ref/untitled-ui/react"
REPO="https://github.com/untitleduico/react.git"
if [ -d "$DEST/.git" ]; then
  git -C "$DEST" pull --ff-only --quiet
  echo "Đã cập nhật $DEST ($(git -C "$DEST" rev-parse --short HEAD))"
else
  git clone --depth 1 --quiet "$REPO" "$DEST"
  echo "Đã tải $DEST ($(git -C "$DEST" rev-parse --short HEAD))"
fi
ls "$DEST/components"
