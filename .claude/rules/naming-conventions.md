---
paths:
  - "docs/**"
  - "_templates/**"
  - ".claude/skills/**"
  - "_scripts/**"
---

# Naming Conventions‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Slugs (folder & file names)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

- All lowercase, kebab-case
- ASCII only (avoid Vietnamese diacritics — use English/transliteration)
- No spaces, no underscores, no special chars
- Strip leading/trailing dashes
- Max 50 chars

| Input | Slug |
|-------|------|
| "User Login" | `user-login` |
| "Forgot Password (v2)" | `forgot-password-v2` |
| "Thanh toán đơn hàng" | `payment-checkout` (preferred) |
| "2FA / OTP" | `two-factor-auth` |

## File path patterns‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

> **Nguyên tắc prefix (2026-07-12):** MỌI file per-feature có **tên cố định** (không phải slug nghiệp vụ) mang prefix `{feature}-` — lý do: tên trần (`spec.md`, `flows.md`, `preview.html`...) trùng basename giữa các feature (đo thật: `preview.html` ×8, `spec.md` ×4), không phân biệt được khi search/mở tab Obsidian/IDE. Đây là mở rộng của quyết định đã làm cho index files (`_index.md` ×18 → `{feature}-{domain}-index.md`). File có **slug nghiệp vụ tự khác nhau** (uc-{slug}.md, us-{NNN}.md, {flow-slug}.md, checklist-{slug}.md, brainstorms/{idea}.md, {process}.bpmn) KHÔNG prefix — slug đã đủ phân biệt, thêm prefix chỉ làm dài tên.

| Loại | Path |
|---|---|
| Project-level | `docs/_product/{prd,roadmap}.md` · `docs/_shared/{project-profile,object-map,traceability,…}.md` · `docs/_research/{date}-{slug}.md` |
| Yêu cầu | `docs/{feature}/{feature}-{urd,brd,prd,object-map}.md` · `brainstorms/{idea}.md` |
| SRS | `docs/{feature}/srs/{feature}-{spec,flows,states,erd,userflow}.md` |
| Use case | `usecases/{feature}-usecase-index.md` + `uc-{slug}.md` + `{feature}-usecase-diagram.{puml,svg}` |
| Màn hình | `ascii-wireframe/{feature}-wireframe-index.md` + `{flow-slug}.md` · `html-wireframe/{feature}-wireframe{.html,-html-index.md}` + `{flow-slug}.html` · `html-design/{feature}-prototype.html` |
| Story | `userstories/{feature}-story-index.md` + `us-{NNN}.md` |
| Sơ đồ khác | `bpmn/` · `d2/` · `d2-erd/` · `d2-architect/` · `dbdiagram/` — mỗi folder có `{feature}-{domain}-index.md` |
| API / test | `integration/api-*.md` · `test/api/` · `test/checklist/` · `test/testcases/` · `test/e2e/` |
| Reverse | `docs/_reverse/{feature}/{feature}-reverse-spec.md` + `reverse-sources.md` + `reverse-gaps.md` |
| Khác | `docs/meetings/YYYY-MM-DD-{type}-{slug}.md` (+`decks/`) · `docs/cr/CR-{YYYYMMDD}-{NNN}.md` · `docs/exports/` · `docs/userguide/` · `docs/reports/` · `prototype/` (ngoài `docs/`) |

> **Bảng đầy đủ** (từng loại doc + ghi chú: file zero-frontmatter, bản .svg/.sql đi kèm, ngoại lệ) và **bảng giá trị `type:`**: `.claude/reference/naming-paths.md`. __Đọc file đó trước khi tạo loại file mới, đặt `type:` cho doc mới, hoặc khi chưa chắc path.__

> **Quy ước đặt tên file index:** mọi file "master metadata" trong 1 folder domain (usecases, userstories, ascii-wireframe, html-wireframe, bpmn, test/checklist, test/testcases) dùng pattern `{feature}-{domain}-index.md` thay vì `_index.md` trơn. Từ 2026-07-12 nguyên tắc prefix áp dụng cho **mọi file tên-cố-định** (xem đầu bảng) — gồm cả `{feature}-usecase-diagram.*`, `{feature}-prototype.html`, `{feature}-preview.html`.
>
> **Ngoại lệ có chủ đích — họ API dùng BARE NAME**, không prefix: `integration/api-assess.md`, `api-summary.md`, `api-design.md`, `api-map.md`, `api-readiness.md` và `test/api/api-checklist.md`, `api-tests.md`. Lý do: folder `integration/` + `test/api/` đã nằm dưới `docs/{feature}/` nên path đã phân biệt đủ; thêm prefix chỉ làm dài tên. Xem bảng path ở trên + `.claude/rules/api-integration.md`.

## Màn hình & flow

> Áp cho userflow Mục 1–3.6, wireframe ASCII/HTML, prototype và frame Figma. Nguồn số + slug duy nhất: `srs/{feature}-userflow.md` Mục 2.

| Thứ | Quy ước | Ví dụ |
|---|---|---|
| Số màn `[#]` | `{flow#}.{màn#}`: `flow#` = thứ tự flow ở userflow Mục 3, `màn#` = thứ tự màn trong flow. Màn dùng chung nhiều flow lấy số của flow đầu tiên chứa nó. Màn thêm sau lấy số kế tiếp trong flow; không đánh lại số đã dùng | `1.1`, `1.2`, `2.1` |
| `screenId` | `{[#]} · {web\|mob}`, ngăn bằng ` · ` (có dấu cách hai bên). Desktop, Tablet, Responsive = `web`; Mobile = `mob` | `1.1 · web`, `1.1 · mob` |
| Web ↔ mobile | Cùng một màn thì chung `[#]` và chung slug, chỉ khác thiết bị. Màn chỉ có trên mobile đánh số trong flow mobile | `1.1 · web` ↔ `1.1 · mob` |
| Slug màn | Tiếng Anh, kebab-case, ASCII, ≤ 40 ký tự. Không tiền tố/hậu tố thiết bị (không `m-`) | `process-line` |
| Slug flow | Tiếng Anh, kebab-case. Không chứa đuôi file (`/wireframe-html` tự thêm `.html` khi ghi file) | `view-process` |
| Trạng thái có số riêng | Chỉ khi có chuyển màn riêng ở userflow Mục 3.5 (đi tới hoặc rời đi theo đường mà màn gốc không có) **và** có nội dung + hành động riêng (panel, popup chặn, màn mới). Chuyển *Tải xong / Thử lại / Tải lại / Xoá bộ lọc / Đóng* là vòng đời chuẩn của trạng thái, không tính. Slug `{slug gốc}-{trạng thái}` hoặc tên theo nội dung | `1.3` · `step-not-created` |
| Trạng thái không có số riêng | Ghi ở cột *Trạng thái* của Mục 2 bằng tên tiếng Anh theo bảng từ vựng `design/setup-figma.md`. Mục 3.5 ghi `[1.1] · Loading` | `Loading, Load error, Empty` |
| Tên hiển thị | Tiếng Việt: cột *Màn hình* (Mục 2), *Tên flow* (Mục 3), nhãn sơ đồ Mục 1, cột Từ màn/Đến màn Mục 3.5, SRS/UC/story (không dùng slug), thanh title nhóm trên Figma. Slug UC (`uc-…`) không thuộc quy ước này | Màn chi tiết bản ghi có dòng quy trình |

Tên frame Figma (frame chính 3 phần, trạng thái/modal 4 phần, title nhóm): `design/setup-figma.md` mục *Tên frame*.

## Wikilinks‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Format: `[[docs/payment/srs/payment-spec.md|Payment SRS]]`

- Use full path from project root (Obsidian + GitHub render correctly)
- Optional display text after `|`‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
- Don't use `[[Login Feature]]` (Obsidian-only style) — breaks on GitHub

## Frontmatter requirements‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

Every doc-type file MUST have YAML frontmatter at the top:

```yaml
---
type: srs                   # see types below
feature: payment            # feature slug = folder name
status: draft               # see status-lifecycle.md
updated: 2026-05-09         # ISO date
links:                      # flat list full path (nguồn reverse-graph stale hook)
  - docs/payment/brainstorms/checkout-idea.md
---
```

Recommended optional fields:
- `priority`: P0 / P1 / P2
- `version`: semver (e.g. `0.1.0`)

**Các field ĐÃ BỎ (không thêm lại):** `lang`/`tags`/`stale_reason` (diet đợt 1, 2026-07-11); `created` (git biết), `owner` (người thực hiện ghi per-event trong `_workspace/changelog.md`), `changelog` (lịch sử sống ở `changelog.md` — xem `.claude/rules/changelog.md`) — diet đợt 2, 2026-07-12.

## Doc type values

Giá trị `type:` trùng tên loại doc (`srs`, `srs-flows`, `urd`, `screen-index`, `usecase-index`, `userstory-index`, `meeting`, `change-request`…). Bảng đầy đủ + loại đã bỏ: `.claude/reference/naming-paths.md` mục "Doc type values".

## ID conventions (cross-doc references)

Mọi ID trong frontmatter `links:` hoặc body phải tuân format dưới. Format này đảm bảo `/gap` traceability matrix không collision khi cross-aggregate cross-feature.

### Format chung

| Loại | Format | Ví dụ | Scope |
|------|--------|-------|-------|
| Business Objective | `BO-{feature}-{NNN}` | `BO-payment-01` | Per-feature, trong `{feature}-brd.md` Mục Business Objectives & Success Measures |
| PRD Capability | `CAP-{feature}-{NNN}` | `CAP-payment-01` | Per-feature, trong `{feature}-prd.md` Mục Capabilities |
| Functional Requirement | `FR-{feature}-{NNN}` | `FR-payment-001` | Per-feature, trong `srs/{feature}-spec.md` Mục 2 |
| Non-Functional Requirement | `NFR-{feature}-{NNN}` | `NFR-payment-001` | Per-feature, trong `srs/{feature}-spec.md` Mục 3 |
| Business Rule | `BR-{feature}-{NNN}` | `BR-payment-001` | Per-feature, trong `srs/{feature}-spec.md` Mục 4 |
| Error Code | `E-{feature}-{NNN}` | `E-payment-001` | Per-feature, trong `srs/{feature}-spec.md` Mục 5 |
| User Story | `US-{NNN}` | `US-001` | Per-feature folder (`docs/payment/userstories/us-001.md`) — feature ngầm hiểu qua path |
| Use Case | `UC-{slug}` | `UC-checkout` | Per-feature folder, slug human-readable |
| Acceptance Criterion | `AC-{NNN}` | `AC-001` | Per-user-story (scope trong file `us-{NNN}.md`) |
| Change Request | `CR-{YYYYMMDD}-{NNN}` | `CR-20260512-001` | Project-wide (`docs/cr/`) |
| Object | `OBJ-{slug}` | `OBJ-don-hang` | Toàn vault — khai ở `docs/_shared/object-map.md` hoặc `{feature}-object-map.md`, không trùng |

### Rules

- **Feature prefix bắt buộc** cho BO/CAP/FR/NFR/BR/E. Mục đích: tránh collision khi `/gap` cross-feature aggregate (vd `FR-001` ambiguous khi 2 features).
- **US/AC/UC scope qua path** (không cần feature prefix trong ID) vì luôn nằm trong folder feature.
- **NNN = 3 digit zero-pad** cho BO/CAP/FR/NFR/BR/E (vd `001`, `042`). NN cũng OK cho BO/CAP (`01`, `02`) vì thường ít hơn.
- **CR/D/B prefix date** vì là sự kiện theo thời gian, ordering theo date.
- ID không reuse khi delete — luôn increment max + 1.
- Slug trong ID kebab-case, max 30 chars.

### Cross-references

Khi 1 doc reference ID của doc khác:
- Frontmatter `links:` flat list với full path: `links: [docs/payment/srs/payment-spec.md, docs/payment/userstories/us-001.md]`
- Body inline reference: `[[docs/payment/srs/payment-spec.md#FR-payment-001|FR-payment-001]]` (Obsidian-compatible anchor).
- `/gap` parse cả 2 dạng để build relationship graph.‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
