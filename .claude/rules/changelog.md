---
paths:
  - "docs/**/*.md"
  - ".claude/hooks/**"
---

# Changelog Convention‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

> Lịch sử thay đổi của TOÀN BỘ vault sống ở **một file duy nhất**: `_workspace/changelog.md` (append-only, **bảng Markdown**). Doc KHÔNG mang `changelog:` trong frontmatter. Không còn routing table, không còn prefix, không còn echo 1 sự kiện vào nhiều file.
>
> **Ghi theo mảnh (2026-10-13):** hook ghi vào `_workspace/changelog.d/{YYYY-MM-DD}--{branch}.md`; `_workspace/changelog.md` là **file sinh ra** (gitignore) do `_scripts/logbook.py` dựng lại từ các mảnh — để nhiều worktree ghi song song không xung đột. Đọc vẫn đọc file tổng như cũ. Xem `.claude/rules/worktree.md` Mục 3.

## Vì sao 1 log tập trung‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Kiến trúc cũ (changelog YAML per review-unit + routing file con → file cha) tạo ra: 49 file mang changelog, 1 sự kiện CR apply chép vào 11 file, bảng routing tồn tại 3 bản sao (rule + hook + SKILL.md) từng lệch nhau, hook phải rewrite YAML + dedupe mỗi lần Write. Log tập trung xoá cả 4 vấn đề: **path của file được sửa chính là thông tin routing** — không cần bảng nào nữa.

## Format‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

File là **bảng Markdown 5 cột** (render được trong Obsidian/GitHub), mở đầu bằng tiêu đề + blockquote mô tả, rồi header bảng:

```markdown
# Activity Log

> Lịch sử thay đổi toàn vault — append-only, mới nhất ở cuối. Writer duy nhất: hook `auto-changelog.sh`.

| Ngày | Skill | Người | File | Ghi chú |
|---|---|---|---|---|
| 2026-07-12 | /srs | @ba | `docs/payment/srs/payment-spec.md` | initial spec 12 FR + 9 error |
| 2026-07-12 | /erd | @ba | `docs/payment/srs/payment-erd.md` | 5 entities, 4 relationships |
| 2026-07-13 | /cr | @ba | `docs/payment/srs/payment-spec.md` | applied CR-20260713-001: FR-payment-013 thêm |
| 2026-07-13 | /jira | @ba | `docs/payment/userstories/payment-story-index.md` | pushed 7 US → KAN-127..133 |
```

* 1 dòng bảng = 1 sự kiện. Append cuối file (mới nhất ở cuối, giống `staleness.md`).
* **Ngày**: ISO `YYYY-MM-DD`.
* **Skill**: `/urd`, `/sequence`, `/cr`, `/jira`, ... hoặc `manual` (edit tay ngoài skill).
* **Người**: @handle người chạy — resolve từ memory `user-identity` key `current_user` (xem `ba-conventions.md` Mục 1). Hook fallback: env `CLAUDE_CHANGELOG_AUTHOR` → `git config user.name`.
* **File**: project-relative path của file vừa Write/Edit, **bọc backtick** (vd `` `docs/payment/srs/payment-spec.md` ``). Parser gỡ backtick khi đọc.
* **Ghi chú**: what changed — imperative/past-tense, factual, ≤80 chars, tiếng Việt hoặc Anh.

**Ký tự `|` trong Ghi chú** được hook escape thành `\|` để không phá cấu trúc cột; parser khôi phục lại khi đọc. Không cần tự escape khi set `CLAUDE_CHANGELOG_NOTE`.

**Bootstrap:** file chưa tồn tại (hoặc rỗng) → hook tự ghi tiêu đề + header + separator trước dòng dữ liệu đầu tiên.

## Cơ chế ghi — hook là writer duy nhất‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Skill KHÔNG tự ghi changelog.md. Trước mỗi Write/Edit, skill set env vars (như cũ):

* `CLAUDE_SKILL_NAME` — tên skill đang chạy
* `CLAUDE_CHANGELOG_NOTE` — note cho sự kiện
* `CLAUDE_CHANGELOG_AUTHOR` — @handle (thường skill resolve 1 lần đầu session)

Hook `auto-changelog.sh` (PostToolUse Write|Edit) đọc env + path vừa sửa → append 1 dòng bảng vào mảnh của branch hiện tại, rồi dựng lại file tổng. Thiếu env → fallback `manual | {git user.name} | manual edit`. Một writer duy nhất = không race khi /srs chạy sub-agent song song (append-only O_APPEND an toàn).

> **Vì sao bảng Markdown mà vẫn append được an toàn:** mỗi sự kiện vẫn là **đúng 1 dòng thêm vào cuối file** — không cần đọc-sửa-ghi lại, không cần chèn vào giữa. Bảng chỉ đổi cách trình bày, KHÔNG đổi mô hình ghi.‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Dedupe‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Bỏ qua nếu dòng **giống hệt** (cùng date + skill + path + note) đã tồn tại — tránh double-fire khi 1 skill Write cùng file 2 lần với cùng note. Khác note → ghi bình thường (nhiều sự kiện/ngày/file là hợp lệ).

## Files excluded

Hook skip (không log):
* `docs/_shared/*` (gồm chính changelog.md — tránh đệ quy)
* `docs/exports/*` (regenerated)
* `docs/inbox/*` (raw capture)
* `docs/feature-list.md`, `docs/README.md` (auto-gen)

## Đọc lịch sử

* Mở thẳng `_workspace/changelog.md` trong Obsidian/GitHub — render thành bảng, sort/scan bằng mắt được.
* Lịch sử 1 feature: `grep "docs/payment/" _workspace/changelog.md`
* Lịch sử 1 file: `grep "docs/payment/srs/payment-spec.md" _workspace/changelog.md`
* Stakeholder-facing: `/export` render section "Lịch sử thay đổi" từ log (lọc theo feature) khi cần — KHÔNG nhét lịch sử vào doc.
* `/dashboard`, KG engine ingest log như event stream (cùng cách đọc `staleness.md`).

> **KG loại 2 file này khỏi walk-scope** (`MACHINE_LOG_FILES` trong `kg-build.mjs`): chúng là event stream có parser riêng (`parseActivityLog`/`parseStalenessLog`), KHÔNG phải nguồn evidence nghiệp vụ. Không loại thì ID nhắc trong cột Ghi chú (vd "applied CR-...") bị bắt thành dangling-ref.

## Note style

* Good: `added refund webhook sequence`, `AC for invalid password updated`, `applied CR-20260512-001: added OTP requirement`.
* Bad: `updated stuff`, `fixed things`, `per Hoang's request` (người đã có ở field @author).

## Backward-compat

Docs demo cũ còn `changelog:` frontmatter → **giữ nguyên, không migrate** (docs demo sẽ bỏ khi rebuild). Parser/reader gặp field `changelog:` trong frontmatter hiểu là di sản, bỏ qua. Không tạo entry mới vào frontmatter trong bất kỳ trường hợp nào.‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
