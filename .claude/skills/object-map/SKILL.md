---
name: object-map
description: Dùng khi cần lập bản đồ đối tượng nghiệp vụ theo ORCA (đối tượng, quan hệ, hành động theo vai trò, thuộc tính) cho cả dự án hoặc phần bổ sung của 1 feature, làm xương sống cho user-flow, SRS, wireframe và ERD. `/object-map` (cấp dự án) · `/object-map <feature>`.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, AskUserQuestion
user-invocable: true
argument-hint: "[--project | <feature>]"
---

# /object-map — Bản đồ đối tượng (ORCA)

## Goal

Trả lời 3 câu mà pipeline luồng-trước (brainstorm → user-flow → wireframe) không trả lời: hệ thống có
**những đối tượng nghiệp vụ nào**, chúng **nối với nhau ra sao**, **vai trò nào được làm gì trên từng
đối tượng** — trước khi vẽ flow hay màn. Theo phương pháp ORCA (Object-Oriented UX) 4 vòng:
Objects → Relationships → CTAs → Attributes, cộng vòng Representation ở mức đề xuất.

2 chế độ:

| | Cấp dự án | Cấp feature |
|---|---|---|
| Gọi | `/object-map` · `/object-map --project` | `/object-map <feature>` |
| Output | `docs/_shared/object-map.md` | `docs/{feature}/{feature}-object-map.md` |
| Phạm vi | Đối tượng cốt lõi xuyên feature, đủ các bảng | Chỉ **delta**: đối tượng mới, quan hệ/hành động/thuộc tính feature thêm hoặc chạm tới |

Output là đầu vào cho `/user-flow` (đường điều hướng giữa màn chi tiết), `/srs` (FR + phân quyền),
`/wireframe-*` / `/figma-screen` (Items + mức hiển thị), `/erd` / `/state` (seed entity, transition),
`/gap` (hành động thiếu chiều ngược). Skill này KHÔNG thay `/erd`: không có khoá, FK, kiểu dữ liệu.

## Constraints (must follow)

### Hard rules — never violate

- **Approval L1** trước Write, prose BA-friendly theo `ba-conventions.md` Mục 5. **L2 diff** khi file đã tồn tại (update mode tự động).
- **2 checkpoint HITL** (Phase B, Phase E) — KHÔNG gộp, KHÔNG bỏ. Danh sách đối tượng sai thì mọi bảng sau sai theo.
- **Cột Vai trò = vai trò nghiệp vụ** (Người lập, Người duyệt, Thủ kho…), KHÔNG phải actor. Mỗi vai trò khai ở bảng "Vai trò nghiệp vụ" kèm cột "Thuộc actor" lấy đúng tên **Canonical** trong `docs/_shared/definitions.md` › Actor Registry.
- **Mã đối tượng `OBJ-{slug}`** kebab-case ASCII (transliterate tiếng Việt, ≤30 ký tự), không đổi khi đã dùng. Bảng 2/3/4 ghi **tên** đối tượng (đọc được); linter tự đối chiếu tên ↔ mã.
- **Định nghĩa trỏ link** sang `definitions.md` (`[[docs/_shared/definitions.md#{Tên}\|xem]]`), KHÔNG chép lại. Đối tượng chưa có trong glossary → viết 1 câu + gợi ý `/update-overview definitions` ở report.
- **Không bịa**: mỗi dòng có cột Nguồn = trích `file:dòng`, hoặc `🟡 Suy luận · OQ-n` trỏ tới câu hỏi mở có thật ở Mục 6. Ô chưa rõ trong dòng (vd vai trò) ghi `🟡 chưa rõ`.
- **Chế độ feature không khai lại** đối tượng đã có ở bản đồ cấp dự án — chỉ tham chiếu theo tên. Cần đổi đối tượng cấp dự án → chạy `/object-map --project` (L2), không sửa ở file feature.
- **Mục 0 do máy sinh** từ bảng Mục 2 (`object-map-lint.mjs --write-diagram`). KHÔNG viết tay mermaid trong Mục 0.
- **Linter phải PASS** (exit 0) trước khi báo xong — xem Phase F. Tên hành động theo thuật ngữ trong `docs/_shared/project-profile.md` (đọc trước, không hỏi lại).
- **IT-BA framing** (`ba-conventions.md` Mục 3): cột "Loại nghiệp vụ" dùng từ nghiệp vụ (tiền, ngày, mã định danh, danh mục, trạng thái, văn bản, tệp đính kèm) — KHÔNG kiểu DB.
- **Không sửa nguồn chung**: KHÔNG tự sửa `definitions.md`, `design/ui-common/`, `states.md`. Chỉ đề xuất ở report (`/update-overview`, `/state`).
- **Template sạch** (`ba-conventions.md` Mục 0): file output không có blockquote hướng dẫn, chỉ bảng + nội dung.

### Pitfalls — easy to get wrong

- **Đối tượng hay thuộc tính?** Danh từ chỉ có giá trị, không có vòng đời riêng, không ai thao tác độc lập → **thuộc tính** (vd "loại", "phân luồng", "trạng thái"). Danh từ có màn chi tiết riêng, có hành động riêng, được nhiều đối tượng khác trỏ tới → **đối tượng**. Danh sách giá trị cố định (danh mục) → thuộc tính kiểu "danh mục", trừ khi người dùng quản lý được danh mục đó (thêm/sửa/ngừng) thì là đối tượng.
- **Chứng từ con nằm trong chứng từ cha** (dòng chi tiết của đơn) — chỉ là đối tượng khi có hành động riêng trên từng dòng; không thì là thuộc tính dạng danh sách của cha.
- **Trạng thái không phải đối tượng** — đưa vào cột "Đổi trạng thái" của Mục 3.
- **Vai trò ≠ actor**: 1 actor (vd nhân viên nội bộ) thường gánh nhiều vai trò theo phân quyền. Ghi actor vào cột Vai trò làm ma trận vô nghĩa.
- **Quan hệ ghi 1 lần** theo chiều tự nhiên (cha → con); chiều ngược thể hiện ở cột "Đi được từ màn chi tiết" (`2 chiều` / `{Từ} → {Tới}` / `không`), KHÔNG ghi 2 dòng cho 1 quan hệ.
- **Hiện ở** chỉ 3 giá trị `Thẻ` / `Danh sách` / `Chi tiết`, ngăn bằng ` · `. Mỗi đối tượng nên có ít nhất 1 thuộc tính hiện ở Thẻ.
- **`mermaid-verify` cảnh báo "nhánh cụt"** ở đối tượng lá trên Mục 0 — bỏ qua: sơ đồ đối tượng không phải luồng, lá là bình thường. Chỉ lỗi cú pháp mới cần sửa.
- **Bản đồ cấp dự án phình to**: giữ đối tượng **xuyên ≥2 feature hoặc là trục nghiệp vụ**; đối tượng chỉ 1 feature dùng → để file feature.

## Inputs

```
/object-map                 # cấp dự án → docs/_shared/object-map.md
/object-map --project       # như trên, gọi tường minh
/object-map <feature>       # phần delta của 1 feature → docs/{feature}/{feature}-object-map.md
```

Muốn đổi mặc định, nói bằng lời: dùng nguồn khác → tag `@file`; chỉ làm lại 1 vòng (vd "chỉ cập nhật thuộc tính") → skill vào update mode, chỉ đụng bảng đó.

**Bootstrap** (`feature-bootstrap.md`):
- Cấp dự án: hành xử như nhóm C — chạy được khi chưa có feature nào.
- Cấp feature: nhóm B — `docs/{feature}/` chưa có → refuse + route `/brainstorm {feature}`. Chưa có `docs/_shared/object-map.md` → cảnh báo và đề nghị chạy cấp dự án trước (user có thể bỏ qua; khi đó file feature khai đủ đối tượng nó dùng).

## Context (dynamic)

Today: !`date +%Y-%m-%d`
Bản đồ cấp dự án: !`ls docs/_shared/object-map.md 2>/dev/null || echo "(chưa có)"`
Bản đồ feature: !`ls docs/*/*-object-map.md 2>/dev/null | head -20 || echo "(chưa có)"`
Features: !`ls -d docs/*/ 2>/dev/null | xargs -I{} basename {} | grep -v '^_' | head -20`

## Approach

**Phase A — Đọc nguồn**

1. Xác định chế độ + output path. File output đã tồn tại → update mode: Read toàn văn, giữ nguyên dòng người dùng đã sửa, chỉ bổ sung/đổi phần có fact mới (L2 ở Phase G).
2. Đọc (đúng thứ tự, file không có thì bỏ qua):
   - `docs/_shared/project-profile.md` (domain, thuật ngữ, cách gọi hành động) · `definitions.md` (Glossary + Actor Registry) · `system-overview.md` (subsystem, feature map) · `docs/_product/prd.md`.
   - Cấp dự án: tài liệu nguồn của khách trong `docs-input/` (SRS cũ, SOP, danh mục) — dùng `docs-input/README.md` để chọn. Hỏi user xác nhận danh sách nguồn trước khi đọc nếu >5 file.
   - Cấp feature: `docs/_shared/object-map.md` + `docs/{feature}/brainstorms/*`, `{feature}-urd.md`, `{feature}-prd.md`, `srs/{feature}-spec.md`, `srs/{feature}-states.md`. Dùng `kg facts {feature}` / `kg neighbors` để chọn file (`kg-usage.md`); kết luận từ prose đã Read.

**Phase B — Discovery (vòng O)**

3. Gom danh từ nghiệp vụ trong nguồn → phân loại mỗi danh từ: **đối tượng / thuộc tính / trạng thái / vai trò / danh mục**, theo Pitfalls. Ghi nhận nguồn `file:dòng` cho từng cái.
4. **⛔ Checkpoint 1** — trình trong chat:
   - Bảng đối tượng đề xuất: Mã · Tên · 1 câu định nghĩa · có trong glossary chưa · nguồn.
   - Bảng **đã loại** kèm lý do (danh từ nào thành thuộc tính / trạng thái / vai trò).
   - Danh sách vai trò nghiệp vụ đề xuất + actor tương ứng.
   - Hỏi: "Đồng ý / Sửa: … ". User chốt mới sang Phase C. Max 3 vòng (L3).

**Phase C — Quan hệ (vòng R)**

5. Với mỗi cặp đối tượng có liên hệ trong nguồn: quan hệ (động từ nghiệp vụ), bản số (`1–1` / `1–n` / `n–1` / `n–n`), đi được từ màn chi tiết theo chiều nào. Không có nguồn cho bản số → `🟡` + OQ.

**Phase D — Hành động (vòng C) + Thuộc tính (vòng A)**

6. Hành động: lấy từ FR/SOP/brainstorm. Mỗi dòng: đối tượng · hành động · vai trò · kênh (theo kênh dự án ghi trong profile/system-overview) · đổi trạng thái `{từ} → {tới}` (tên trạng thái lấy nguyên văn `states.md` nếu có) · nguồn.
7. Thuộc tính: chỉ thuộc tính có ý nghĩa nghiệp vụ, kèm loại nghiệp vụ, mức hiển thị, khả năng lọc/sắp.

**Phase E — Representation + checkpoint 2**

8. Đối tượng xuất hiện ở ≥2 feature (theo `definitions.md` "Appears in" hoặc bản đồ feature): điền Mục 5 — thẻ hiện gì, dòng danh sách hiện gì, gợi ý CMP. Đây chỉ là đề xuất; KHÔNG sửa `design/ui-common/`.
9. **⛔ Checkpoint 2** — trình tóm tắt: số đối tượng / quan hệ / hành động / thuộc tính, **liệt kê riêng mọi dòng 🟡** và OQ. User "Đồng ý / Sửa".

**Phase F — Dựng file nháp + lint**

10. Dựng nội dung theo `_templates/object-map.md` vào file nháp trong scratchpad (KHÔNG ghi đích trước approval).
11. Chạy:
    ```bash
    node .claude/skills/object-map/object-map-lint.mjs <nháp> --write-diagram [--project docs/_shared/object-map.md]
    node .claude/scripts/mermaid-verify.mjs --file <nháp>
    ```
    `--write-diagram` sinh Mục 0 từ Mục 2. Chế độ feature phải truyền `--project` (nháp nằm ngoài `docs/` nên linter không tự dò). Còn `✗` → sửa nháp, chạy lại, tối đa 2 vòng. Vẫn còn → báo user lỗi cụ thể, KHÔNG báo xong.
    Linter kiểm (R-số trỏ vào code): R1 đối tượng được khai · R2 vai trò/actor hợp lệ · R3 mã đúng mẫu, không trùng, feature không khai lại · R4 mồ côi (warn) · R5 tạo mà không có kết thúc (warn) · R6 không đi được từ màn chi tiết (warn) · R7 không có thuộc tính ở Thẻ (warn) · R8 trạng thái lệch `*-states.md` (warn; SKIPPED khi chưa có states) · R9 🟡 phải trỏ OQ có thật · R10 Mục 0 khớp Mục 2.

**Phase G — Ghi**

12. **L1** prose BA (`ba-conventions.md` Mục 5): ghi file nào, bao nhiêu đối tượng/quan hệ/hành động/thuộc tính, các đối tượng chính, số câu hỏi mở. Thêm dòng cho `project-profile.md` nếu Phase A phải hỏi thông tin cấp dự án mới.
13. File đã có → **L2** diff. Set env `CLAUDE_SKILL_NAME=object-map`, `CLAUDE_CHANGELOG_NOTE`, `CLAUDE_CHANGELOG_AUTHOR` rồi Write/Edit đích (copy nháp đã lint). Frontmatter: `type: object-map` · `feature` (chỉ chế độ feature) · `status: draft` · `updated` · `links` (nguồn đã dùng; file feature luôn có `docs/_shared/object-map.md`).
14. Chạy lại linter trên file đích (exit 0).

**Phase H — Report**

```
✅ docs/_shared/object-map.md — {N} đối tượng · {R} quan hệ · {C} hành động · {A} thuộc tính · {Q} câu hỏi mở
   Cấu trúc: PASS · Tham chiếu: PASS ({w} cảnh báo) · Ngữ pháp ORCA: PASS ({w} cảnh báo) · Mục 0 compile: PASS
   Nghiệp vụ: CHƯA KIỂM BẰNG MÁY — {liệt kê dòng 🟡 / cảnh báo đáng soi}

Đề xuất:
  · /update-overview definitions — {k} đối tượng chưa có trong glossary
  · /update-overview patterns — {m} đối tượng nên có thẻ dùng chung (Mục 5)
  · /state {Entity} — {đối tượng có ≥3 trạng thái mà chưa có states.md}
Bước tiếp: /brainstorm <feature> (cấp dự án) · /srs {feature} hoặc /user-flow {feature} (cấp feature)
```

Câu hỏi mở chặn tiến độ cấp dự án → thêm task backlog theo `backlog.md` (Xong khi: `grep:` mã OQ biến mất khỏi file).

## Output

| Chế độ | Path | type |
|---|---|---|
| Dự án | `docs/_shared/object-map.md` | `object-map` |
| Feature | `docs/{feature}/{feature}-object-map.md` | `object-map` |

Cấu trúc thân (cả 2 chế độ): Mục 0 Sơ đồ tổng quan (máy sinh, giữa marker `object-map:diagram`) · Vai trò nghiệp vụ · 1 Đối tượng · 2 Quan hệ · 3 Hành động theo vai trò · 4 Thuộc tính · 5 Đề xuất hiển thị dùng chung · 6 Câu hỏi mở. Header cột cố định theo template — linter tìm bảng theo header.

Sơ đồ Mục 0: đối tượng lấy từ bản đồ cấp dự án vẽ viền đứt (`:::project`).

Hook tự ghi 1 dòng vào `_workspace/changelog.md`; `post-edit-stale` đánh `stale` file feature khi bản đồ cấp dự án đổi (nhờ `links`).

## References

- @../../rules/ba-conventions.md
- @../../rules/approval-gate.md
- @../../rules/feature-bootstrap.md
- @../../rules/project-profile.md
- @../../rules/naming-conventions.md
- @../../rules/kg-usage.md
- @../../rules/changelog.md
- @../../rules/backlog.md
- @../../rules/diagram-correctness.md
- @../../rules/ui-common-rules-components.md
- @../../../_templates/object-map.md
- @./object-map-lint.mjs (gate Phase F)
- @./fixtures/ (`valid-*` phải PASS, `invalid-*` phải FAIL)
- @../../scripts/mermaid-verify.mjs (compile Mục 0)
