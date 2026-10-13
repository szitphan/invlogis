#!/bin/bash
# KG dirty-flag hook (Phase 2 KG plan Mục 3.5)
#
# Khi doc trong docs/ được Write/Edit → touch cờ _workspace/kg/.dirty.
# kg-query.mjs thấy cờ → tự rebuild graph trước khi trả lời (lazy rebuild, <1s).
# Hook KHÔNG tự build (giữ hook nhanh + không đệ quy khi build ghi graph.json).

set -u
FILE="${1:-}"
if [ -z "$FILE" ] && [ ! -t 0 ]; then
    if command -v jq >/dev/null 2>&1; then
        FILE="$(cat | jq -r '.tool_input.file_path // .tool_input.path // empty' 2>/dev/null)"
    else
        cat >/dev/null
        exit 0
    fi
fi

# Chỉ quan tâm nguồn KG ingest — MIRROR walk scope của kg-build.mjs:
# docs/**.md + bpmn *.ir.json (mọi độ sâu) + dbdiagram *.dbml + sync-state.yaml.
case "$FILE" in
    *_workspace/kg/*) exit 0 ;;  # graph.json/.dirty tự ghi — tránh đệ quy
    *docs/*/_runs/*|*docs/exports/*|*docs/inbox/*|*docs/reports/*|*docs/_regen-sample/*|*docs/guides/*) exit 0 ;;
    *docs/*.md|*design/*.md|*docs/*bpmn/*.ir.json|*docs/*/dbdiagram/*.dbml|*.claude/state/atlassian/sync-state.yaml) ;;
    *) exit 0 ;;
esac

PROJECT_PATH="${PROJECT_PATH:-$(pwd)}"
mkdir -p "$PROJECT_PATH/_workspace/kg"
touch "$PROJECT_PATH/_workspace/kg/.dirty"
exit 0
