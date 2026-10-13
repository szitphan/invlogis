> **Bản cho Codex — máy sinh từ `CLAUDE.md` bởi `_scripts/codex-sync.py`. KHÔNG sửa tay file này.**
> Skill của Codex nằm ở `.agents/skills/` (bản sao của `.claude/skills/`), agent ở `.codex/agents/*.toml`
> (bản chuyển của `.claude/agents/*.md`). Rules, hooks, scripts, templates dùng chung — đường dẫn
> `.claude/rules/...`, `.claude/scripts/...` bên dưới là file thật, đọc trực tiếp.
> Muốn đổi skill/agent/hướng dẫn: sửa bản trong `.claude/` hoặc `CLAUDE.md`, rồi chạy
> `python3 _scripts/codex-sync.py`.

# Invlogis — BA Workspace‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
> Mọi doc per-feature dưới `docs/{feature}/`. URD/BRD/PRD/SRS đều scope feature (không còn singleton). File tên-cố-định mang prefix `{feature}-` (vd `{feature}-spec.md`) — tránh trùng basename giữa features. Frontmatter tối giản: `type`/`feature`/`status`/`updated`/`links` (KHÔNG created/owner/changelog). Lịch sử thay đổi sống ở `_workspace/changelog.md` (1 log tập trung).

## What lives here‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Path | Purpose |
|------|---------|
| `docs/` | All BA deliverables (URD, BRD, PRD, SRS, user stories, use cases, meetings, wireframes, exports) |
| `.claude/skills/` | User-invocable `/commands` (`/prd`, `/urd`, `/brd`, `/prd-epic`, `/srs`, `/sequence`, `/erd`, `/user-flow`, `/wireframe-ascii`, ...) |
| `.claude/agents/` | Specialized review personas (`@senior-ba`, `@uxui-reviewer`, ...) — Phase 4+ |
| `.claude/hooks/` | Auto-changelog, session-init, status-transition (Phase 4+), post-edit-stale (Phase 6+) |
| `.claude/rules/` | Naming, status lifecycle, changelog, approval-gate, agent conventions, __diagram-correctness__ (gate "vẽ đúng" cho 11 skill diagram) |
| `docs-input/` | Tài liệu khách gửi. Sổ nguồn `README.md` + backlog `_workspace/backlog.md` tự đồng bộ (`_scripts/intake-sync.py`, rule `backlog.md`) |
| `_templates/` | Note templates referenced by skills |

## Folder structure‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

```
docs/
├── _shared/        project-profile, object-map, definitions, conventions, system-overview, traceability
├── _product/       prd.md (PRD sản phẩm + Feature Map), roadmap.md
├── _research/      output /discover
├── _reverse/{feature}/  bộ SRS tái lập (/reverse-doc, /code-to-srs) — status draft cứng
├── {feature}/
│   ├── brainstorms/   {feature}-urd|brd|prd.md   {feature}-object-map.md
│   ├── srs/           {feature}-spec|flows|states|erd|userflow.md
│   ├── usecases/      {feature}-usecase-index.md (gồm ma trận truy vết) + uc-{slug}.md + diagram .puml/.svg
│   ├── ascii-wireframe/ · html-wireframe/ · html-design/ (prototype HTML)
│   ├── screens/       bảng 5 cột + ảnh Figma sau khi lên Figma (/figma-sync, thay wireframe)
│   ├── userstories/   {feature}-story-index.md + us-{NNN}.md
│   └── bpmn/ · d2*/ · dbdiagram/ · integration/ · test/
├── meetings/ (+decks/) · inbox/ · cr/ · exports/ · userguide/ · reports/
design/       design.md (nguồn design system) · design-tokens.css · ui-common/ · brand/ · _lab/
docs-input/   tài liệu khách gửi (sổ nguồn README.md)
_workspace/   changelog.d/ (→ changelog.md sinh ra) · backlog.md · kg/
prototype/    app Next.js (/prototype-next)
```

- Đường dẫn + tên file chi tiết từng loại doc: `.claude/rules/naming-conventions.md`.
- Cây đầy đủ kèm chú thích từng file: `_guides/claude-reference.md`.

## Status lifecycle‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Every doc has frontmatter `status` field. Transitions:

```
draft → in-review → revisions → approved → shipped
```

| Transition | Hook trigger |
|------------|--------------|
| `* → in-review` | (future) Notify reviewer agent |
| `* → approved` | Xem tổng hợp qua `/dashboard` (KHÔNG còn `docs/feature-list.md`) |
| `* → shipped` | (future) Trigger `@gap-analyst` consistency check |

See `.claude/rules/status-lifecycle.md` for details.

## Changelog convention‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Lịch sử thay đổi TOÀN vault đọc ở __một file duy nhất__: `_workspace/changelog.md` — __bảng Markdown__, hook `auto-changelog.sh` là writer duy nhất. Doc KHÔNG mang `changelog:` frontmatter. File tổng là __file sinh ra__ (gitignore): hook ghi mảnh `_workspace/changelog.d/{ngày}--{branch}.md`, `_scripts/logbook.py` dựng lại.

```markdown
| Ngày | Skill | Người | File | Ghi chú |
|---|---|---|---|---|
| 2026-07-12 | /srs | @ba | `docs/payment/srs/payment-spec.md` | initial spec 12 FR |
| 2026-07-13 | /cr | @ba | `docs/payment/srs/payment-spec.md` | applied CR-20260713-001 |
```

1 dòng bảng = 1 sự kiện, append cuối file. Skill set env `CLAUDE_SKILL_NAME`/`CLAUDE_CHANGELOG_NOTE`/`CLAUDE_CHANGELOG_AUTHOR` trước Write/Edit; hook append (tự escape `|` trong Ghi chú, tự dựng header khi file chưa có). Lịch sử 1 feature = `grep "docs/{feature}/" _workspace/changelog.md`. See `.claude/rules/changelog.md`.

## Approval gate (HITL)

Mọi skill phải tuân `.claude/rules/approval-gate.md`:

- __L1 Plan preview__ trước Write/Edit ≥1 file: show table `path | action | summary`, user Y/n/select.
- __L2 Diff confirm__ trước Edit file đã tồn tại: show unified diff, user Y/n/edit-prompt.
- __L3 Iterate__ cho output sáng tạo (ASCII wireframe, mermaid diagrams): render → "Đồng ý / Sửa / Hủy", max 3 vòng.

Skill KHÔNG được auto-pick file im lặng. KHÔNG được skip L1 với cớ "đã confirm trước đó".

## Skills

73 skill `/command` trong `.claude/skills/` (+ vài reference skill `user-invocable: false`). Nguồn sự thật là từng `SKILL.md`; bảng mô tả đầy đủ từng skill ở `_guides/claude-reference.md` mục "Skills shipped" — khi thêm/bớt skill, cập nhật bảng đó.

__Luồng chính:__ `/prd` → `/object-map` → `/roadmap` → `/discover` → `/brainstorm` → `/urd` `/brd` `/prd-epic` → `/srs` → `/user-flow` → `/wireframe-ascii` | `/wireframe-html` → `/figma-screen` / `/prototype-html` → `/usecase` `/userstory` `/ac` → `/test-checklist` → `/test-cases` → `/playwright-gen`. Figma sửa → `/figma-sync` (bảng 5 cột + userflow; `--done` đưa Figma vào SRS). Thay đổi qua `/cr`. Tích hợp API theo họ `/api-*` (`.claude/rules/api-integration.md`). Tài liệu khách mới: `/intake`.

__Quy tắc vận hành:__

- `context: fork` CHỈ cho skill không có HITL (`/preview`). Skill có L1/L2/AskUserQuestion/HARD STOP KHÔNG fork (fork = mọi prompt bị auto-skip — bug CR-20260612-001). Skill gọi AskUserQuestion phải khai trong `allowed-tools`. Phân tích nặng delegate qua sub-agent, sub-agent không ghi file đích trước approval.
- No-arg = picker feature; auto-detect upstream + confirm, KHÔNG silent pick; thiếu upstream = soft gate (warn + proceed), trừ `/jira --push` (hard gate khi stale).
- Diagram: "có ra ảnh" KHÔNG phải verify — gate theo `.claude/rules/diagram-correctness.md`; sửa gate xong chạy `bash .claude/scripts/diagram-gates-selftest.sh`.
- Hooks: `auto-changelog.sh`, `status-transition.sh`, `post-edit-stale.sh`, `intake-sync.sh` (PostToolUse Write/Edit); `session-init.sh` (SessionStart). Commit git thủ công.
- __Song song nhiều feature:__ 1 feature = 1 worktree (`_scripts/wt.sh new|sync|ready|land|drop|list`, branch `feat/<slug>`). Xong → `wt.sh ready` sinh task 🔍 trong backlog; land (squash) + drop CHỈ chạy sau khi người dùng review + duyệt task đó. Trong worktree chỉ sửa `docs/<feature>/**`; đồ dùng chung (`_shared`, `_product`, `design`, `.claude`, backlog) sửa trên `main` rồi `wt.sh sync`. Chi tiết: `.claude/rules/worktree.md`.
- __AI tự chạy + hàng đợi:__ `/run-task <feature> "<mục tiêu>" [--bg]` — duyệt run card 1 lần, AI tự chạy chuỗi skill trong worktree (chế độ chạy: `approval-gate.md`), chỉ dừng khi cần bạn quyết. `/queue` = việc đang chờ bạn (duyệt land / câu hỏi chặn / card chờ duyệt / đang chạy), nguồn `_scripts/queue.py`. `/board` = cùng dữ liệu trên board kéo-thả (artifact, mở được trên điện thoại): kéo card sang Đang chạy = duyệt + chạy; kéo 🔍 sang Xong = duyệt land; phiên điều phối `/loop 5m /board sync`.

## Rule nạp theo vùng file

Luôn nạp: `approval-gate.md`, `backlog.md`. Các rule còn lại trong `.claude/rules/` chỉ tự nạp khi đụng file khớp `paths:` ở đầu rule. __Khi chạy skill, đọc các rule mà SKILL.md tham chiếu (Constraints/References) nếu chưa có trong ngữ cảnh__ — đừng giả định rule đã được nạp.

## Conventions

- __Filenames__: kebab-case slug (`user-login`, `payment-checkout`, NOT `User_Login`)
- __Wikilinks__: `[[docs/payment/srs/spec|Payment SRS]]` — full path từ vault root, Obsidian + GitHub render
- __Dates__: ISO `YYYY-MM-DD`
- __Mermaid diagrams__: inline ` ```mermaid ` blocks
- __Frontmatter__: YAML tối giản — doc per-feature có `type`, `feature`, `status`, `updated`, `links` (flat list). KHÔNG có `created`/`owner`/`changelog` (diet 2026-07-12 — lịch sử + tác giả sống ở `_workspace/changelog.md`)
- __IDs feature-prefixed__ cho cross-aggregate: `FR-{feature}-NNN`, `NFR-{feature}-NNN`, `BR-{feature}-NNN`, `E-{feature}-NNN`, `BO-{feature}-NN`, `CAP-{feature}-NN`. US/AC scope qua path (no feature prefix in ID). See `.claude/rules/naming-conventions.md` Mục ID conventions.
- __Bản Codex__ (`.agents/skills/`, `.codex/agents/*.toml`, `AGENTS.md`) là máy sinh — KHÔNG sửa tay. Sửa `.claude/skills|agents` hoặc `CLAUDE.md` rồi chạy `python3 _scripts/codex-sync.py` (`--check` để kiểm lệch) trước khi commit.
- __Language__: Vietnamese-first; tiếng Anh cũng support; auto-detect từ seed.

## How Claude Code uses this

1) Session start: `.claude/hooks/session-init.sh` → set `$TODAY`, `$PROJECT_NAME`, in status counts (stale items, open CRs, stuck reviews >7d).
2) User invokes skill (vd `/urd payment`) → Claude đọc `.claude/skills/urd/SKILL.md` → tuân Goal + Constraints (Hard rules / Pitfalls) + Approach.
3) Skill scan upstream candidates, ask user pick, ask clarifying questions (numbered list, wait reply).
4) Skill synthesize content → __L1 plan preview__ → user Y/n/select → Write file with frontmatter chuẩn (hook ghi changelog.md).
5) Sau Write/Edit, hooks chạy: `auto-changelog.sh` (fallback), `status-transition.sh`, `post-edit-stale.sh` (Phase 6). Commit git làm thủ công (không còn auto-commit).



<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền ai4ba.com</sub>
