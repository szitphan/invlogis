#!/bin/bash
# Thư viện dùng chung cho hook — xác định repo/branch theo VỊ TRÍ FILE, không theo cwd.
#
# Vì sao: phiên ở checkout chính (cwd = main) vẫn có thể ghi đường dẫn tuyệt đối vào
# .claude/worktrees/<feature>/… (agent, skill dùng path tuyệt đối). Hook xét theo cwd sẽ
# hiểu nhầm là main → guard không chặn, changelog bỏ qua, stale quét nhầm repo.
# Nguồn: .claude/rules/worktree.md Mục 2.
#
# Dùng:  . "$(dirname "$0")/lib-root.sh"
#        ABS="$(abs_phys "$FILE")"     # đường dẫn tuyệt đối, đã resolve symlink phần đã tồn tại
#        ROOT="$(root_of "$ABS")"      # toplevel repo/worktree chứa file ("" nếu ngoài git)

# abs_phys PATH [BASE] — tuyệt đối + vật lý; thư mục cha chưa tồn tại (Write file mới) vẫn ra đúng.
abs_phys() {
    local p="$1" base="${2:-$(pwd)}" dir rest
    case "$p" in /*) ;; *) p="$base/$p" ;; esac
    dir="$(dirname "$p")"; rest="$(basename "$p")"
    while [ ! -d "$dir" ] && [ "$dir" != "/" ]; do rest="$(basename "$dir")/$rest"; dir="$(dirname "$dir")"; done
    printf '%s/%s\n' "$(cd "$dir" && pwd -P)" "$rest" | sed 's#//*#/#g; s#/\./#/#g'
}

# root_of ABS_PATH — toplevel của repo/worktree chứa file.
root_of() {
    local d; d="$(dirname "$1")"
    while [ ! -d "$d" ] && [ "$d" != "/" ]; do d="$(dirname "$d")"; done
    git -C "$d" rev-parse --show-toplevel 2>/dev/null
}

# branch_of ROOT
branch_of() { git -C "$1" rev-parse --abbrev-ref HEAD 2>/dev/null; }
