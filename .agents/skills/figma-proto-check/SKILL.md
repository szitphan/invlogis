---
name: figma-proto-check
description: Dùng khi cần đối chiếu prototype HTML đã duyệt với Figma, đi từng màn theo flow, bằng số đo (chữ, khoảng cách, padding, bo góc, màu) → trang duyệt tương tác báo chỗ Mới / Lệch và nơi sửa (màn hay component). `--before` trước khi vẽ (so với design system), `--after` sau khi vẽ.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, AskUserQuestion, Skill, mcp__claude_ai_Figma__use_figma, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__get_metadata, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_write, Artifact, ArtifactData
user-invocable: true
argument-hint: "<feature> [<flow-slug>] [--before | --after]"
---

# /figma-proto-check — prototype đã duyệt ↔ Figma, đo bằng số

## Mục tiêu

Biết **chính xác** Figma khác prototype đã duyệt ở đâu, trước khi user phải tự soi. Mỗi chỗ khác là
một dòng có số đo hai bên và nơi sửa, để user chọn theo prototype hay giữ cách khác.

**Chuẩn để so = bản prototype đã duyệt về mặt nhìn**, không phải chuẩn vĩnh viễn. Prototype chưa theo
luật design system, nên:

| Chế độ | Khi nào | So gì với gì | User chọn mỗi dòng |
|---|---|---|---|
| `--before` | Trước `/figma-screen` của flow | Prototype ↔ component design system sẽ dùng (+ frame Figma cũ nếu có) | Theo prototype / Theo DS / Dựng component mới |
| `--after` (mặc định khi flow đã có frame) | Sau `/figma-screen`, hoặc khi user thấy Figma "lệch" | Figma ↔ prototype | Theo prototype / Giữ Figma / Sửa component DS |

- Sửa luôn **trên Figma**, KHÔNG bao giờ quay lại sửa prototype.
- Flow đã chốt (`/figma-sync --done`, Status `approved` trong `screens/{feature}-screen-index.md`) → Figma
  là chuẩn, dừng với flow đó, báo 1 dòng.
- Quyết định nằm ở **sổ** `docs/{feature}/html-design/{feature}-proto-check.md`. Lần chạy sau không báo lại
  dòng đã chốt Theo DS / Giữ Figma / Bỏ qua; dòng chốt Theo prototype mà Figma vẫn lệch thì báo lại.

## Vì sao phải đo, không nhìn

Sự cố 16/10/2026 (account-access): ba reviewer + bước đối chiếu bằng cách đọc vẫn sót padding thẻ
20/24 → 32, checkbox 16 → 22, link mất gạch chân, dấu `*` mất màu đỏ. Lý do:
- reviewer so với bảng 5 cột / DS / heuristic, `visual-audit.py` so Figma với chính nó, **không bước nào so với prototype**;
- ảnh 1024px của frame 1920 làm thẻ chỉ còn ~200px — lệch 4px không thấy;
- `figma_read` của reqwise không có `fontWeight` / `textDecoration` (`ui-review.md` Mục 2) → mù độ đậm;
- prototype mở thẳng `#slug` là state mặc định, khác state của frame.

Nên: số đo lấy từ trình duyệt (style thật) và Plugin API Figma thật; ảnh chỉ để người xem.

## Constraints

- **Approval:** đọc + đo không cần duyệt. Ghi sổ, sửa Figma, sửa thư viện → L1 (+ L2 bảng Trước → Sau
  khi sửa file đã có, theo memory "l2-before-after-table"). Per `.claude/rules/approval-gate.md`.
- **Không fork** — skill có AskUserQuestion và trang duyệt.
- **Sửa thư viện (component Astryx / innvie):** hỏi trước, nêu số instance bị ảnh hưởng
  (`figma_read find_instances`). Sửa main component trực tiếp. Component còn ở trang `Astryx · Library`
  → chuyển main component sang `innvie · Components` đúng hàng/nhóm theo `design/setup-figma.md` mục
  *Design system: innvie và Astryx tách riêng*, rồi sửa vị trí ghi trong `design/design.md` cùng lượt (L2).
- **Thay đổi nhìn đã duyệt trên Figma** (memory "keep-approved-look"): dòng nào đổi một thứ user đã duyệt
  trên Figma → hỏi, không tự áp.
- **Chữ mới / phần tử mới** (prototype có, bảng 5 cột chưa có) → không sửa tài liệu ở đây; ghi task
  backlog `/figma-sync {feature}` với Xong khi `grep:` vào `screens/{flow}.md` (rule `backlog.md`).
- Feature chưa có `html-design/{feature}-prototype.html` → refuse + route `/prototype-html` (nhóm B,
  `feature-bootstrap.md`).
- Làm việc trên worktree của feature khi có (`.claude/rules/worktree.md`): sổ là file trong `docs/{feature}/`.

## Bước 1 — đọc

1. `figma_status` (đúng file, plugin nối). Nạp skill `figma:figma-use` một lần (bắt buộc trước `use_figma`).
2. Prototype `docs/{feature}/html-design/{feature}-prototype.html`. Kiểm có `PROTO_STATES` (quy ước
   `/prototype-html`). Thiếu → báo: "chỉ so được state mặc định; state khác cần thêm PROTO_STATES" và hỏi
   có thêm không (sửa prototype là việc của `/prototype-html`, qua L2).
3. `srs/{feature}-userflow.md` Mục 2 (màn + cột Trạng thái) + Mục 3.5 (thứ tự đi) → **danh sách màn
   theo flow**. Có `[flow-slug]` → chỉ flow đó.
4. Frame Figma: `figma_read search_nodes` theo `screenId` (`1.3 · web`), tách tên theo ` · ` như
   `/prototype-html` Mode Figma. Phần thứ 4 = state. Màn không có frame → dòng "Figma chưa có màn".
   Frame không có trong userflow → dòng "Figma có màn ngoài userflow".
5. Sổ `docs/{feature}/html-design/{feature}-proto-check.md` nếu có.
6. `--before`: thêm `design/design.md` theo `.claude/rules/design-system.md` (mục của `/figma-screen`) +
   `design/components.md` Bảng chọn nhanh + `design/ba-crosswalk.md` để biết control nào → component nào.

## Bước 2 — ghép cặp màn

Bảng ghép (in ra trước khi đo, không cần duyệt):

```
# | Màn (screenId · State)        | Prototype                         | Figma
1 | 1.3 · web                      | #sign-in                          | 5828:155111
2 | 1.3 · web · Field error        | #sign-in?state=Field error        | 5831:15428
3 | 1.4 · web                      | #channel-denied                   | 5835:72028
```

Slug prototype = slug màn (userflow Mục 2). Thiết bị: `web` → `device=web`, `mob` → `device=app`.

## Bước 3 — đo

Thư mục làm việc `_workspace/proto-check/{feature}/` (không commit; xoá được).

1. **Prototype**, mỗi cặp:
   `python3 _scripts/proto-figma-diff.py probe <prototype.html> --screen <slug> [--state "<State>"] [--device web|app] --out _workspace/proto-check/{feature}`
   → `proto-<slug>[--<state>].json` + `.png` (2x, đã cắt theo khung màn). Cảnh báo "chưa vào state" → ghi
   vào báo cáo, không coi kết quả state đó là chắc chắn.
2. **Figma**, mỗi frame: dán `references/figma-probe.js` vào `use_figma` (thay `__FRAME_ID__`, `skillNames:
   "figma-use"`). **Một frame mỗi lần gọi** (giới hạn 20 KB); các frame độc lập gọi song song trong một
   lượt. Lưu kết quả nguyên văn ra `figma-<screenId-slug>[--<state>].json`. Vượt 20 KB → đo từng khối con
   (frame con lớn nhất) rồi ghép, ghi rõ trong báo cáo.
3. **Ảnh Figma 2x:** `get_screenshot` `maxDimension` = 2 × cạnh dài của frame (1920 → 3840), tải về
   `figma-<…>.png` bằng curl.
4. **So:**
   `python3 _scripts/proto-figma-diff.py diff --proto <p.json> --figma <f.json> --screen "<screenId>" [--state "<State>"] --ledger docs/{feature}/html-design/{feature}-proto-check.md --proto-png <p.png> --figma-png <f.png> --crop-out _workspace/proto-check/{feature}/crops --out <diff.json>`
5. **Gộp:** `python3 _scripts/proto-figma-diff.py report <diff1.json> … --out _workspace/proto-check/{feature}/report.md`
   theo đúng thứ tự Bước 2.

**`--before`:** không có frame màn. Với mỗi control trên prototype, lấy component + biến thể DS sẽ dùng
(crosswalk → components.md → node main component trong `innvie · Components` hoặc `Astryx · Library`),
đo node đó bằng `figma-probe.js`, rồi `diff` với `--proto-within "<chữ của control>"` (và
`--figma-within` nếu component có chữ). Khung trang / bố cục không có chuẩn DS → so với mẫu P/M trong
`design.md` bằng mắt, ghi "so tay". Nếu flow đã có frame cũ → chạy thêm như `--after`.

Máy đo những gì, bỏ sót những gì: đầu file `_scripts/proto-figma-diff.py` (icon chưa so, bóng/ảnh/gradient
không so). In phần "Máy không kiểm" ở báo cáo, không giấu.

## Bước 4 — tự soát trước khi trình

Máy ghép theo chữ, nên đọc lại `report.md` và **xem ảnh crop** của từng màn:
- Gộp dòng là hệ quả của một nguyên nhân (vd padding thẻ đổi → mọi khoảng cách bên trong đổi) thành 1 dòng
  "nguyên nhân" + ghi các dòng kéo theo, để user không phải duyệt 6 lần cùng một việc.
- Thêm dòng máy không bắt được nhưng nhìn thấy trên ảnh (icon khác, bóng đổ, khối tự dựng). Ghi
  `Khoá` = `m-<số>` (tay) để phân biệt với khoá máy `k-…`.
- Chỗ lệch nằm trong component dùng ở nhiều màn → gộp thành 1 dòng cấp component, liệt kê các màn.

## Bước 5 — trang duyệt

Trang artifact tương tác (memory "review-pages-interactive", "questions-full-context"): nạp skill
`artifact-capabilities` (cần `db`) + `artifact-design` trước khi viết trang.

- Đầu trang: tổng số Mới / Lệch / đã chốt; chú thích Màn / Component / DS thiếu bằng lời thường.
- Mỗi màn theo thứ tự flow: ảnh crop prototype | Figma đặt cạnh nhau (cùng tỷ lệ), dưới là bảng dòng.
- Mỗi dòng: phần tử · thuộc tính · prototype · Figma · sửa ở đâu (kèm tên component + trang) · lựa chọn
  (`--after`: Theo prototype (mặc định) / Giữ Figma / Sửa component DS; `--before`: Theo prototype / Theo DS
  / Dựng component mới) · ô ghi chú.
- Dòng cấp component: ghi các màn bị ảnh hưởng + số instance.
- Nút "Gửi" ghi lựa chọn vào db. Đọc lại bằng `ArtifactData` khi user báo đã chọn xong.

Báo user link trang + tóm tắt 3 dòng. Chờ user chọn.

## Bước 6 — ghi sổ + áp

1. **L1** gồm: ghi sổ, các sửa Màn, các sửa Component (tên + số instance), task backlog cho chữ mới.
2. **Sổ** `docs/{feature}/html-design/{feature}-proto-check.md` (frontmatter `type: proto-check`,
   `feature`, `status: draft`, `updated`, `links: [prototype, userflow]`). Bảng duy nhất, thêm dòng mới,
   sửa cột Quyết định của dòng cũ:

   ```
   | Khoá | Màn | Phần tử | Thuộc tính | Prototype | Figma/DS | Sửa ở | Quyết định | Ngày | Ghi chú |
   ```
   Quyết định: `Theo prototype` · `Theo DS` · `Giữ Figma` · `Bỏ qua` · `Dựng component mới`.
3. **Sửa Màn** (`--after`, dòng Theo prototype, Sửa ở = Màn): `figma_write modify` trên node id trong
   `diff.json` (`figmaNode`), gắn token theo tên (không hex rời). Sau mỗi màn: `figma_read layout_audit`.
4. **Sửa Component:** theo Constraints (hỏi, đếm instance, sửa main component, chuyển trang nếu còn ở
   Astryx · Library, cập nhật `design.md` qua L2). Ghi `/figma-component` nếu cần thêm biến thể thay vì sửa
   biến thể đang dùng ở nơi khác.
5. **`--before`:** không sửa Figma; sổ là đầu vào của `/figma-screen` (đọc ở Bước 1 của skill đó).
6. **Đo lại** các màn đã sửa (Bước 3 chỉ cho các màn đó). Còn lệch dòng Theo prototype → báo.
7. Đụng Figma xong → gọi `/figma-sync {feature} --flow {flow}` inline (rule `screen-source.md` Mục 5) nếu
   có đổi chữ/element; chỉ khoảng cách/màu thì chỉ cập nhật mốc.

## Bước 7 — báo

```
Đối chiếu prototype ↔ Figma · account-access · Flow 1 (web) · --after
Màn: 6 cặp đã đo · 1 Figma chưa có · 0 state chưa vào được
Kết quả: 2 mới · 17 lệch (Màn 9 · Component 8 → 4 component) · 3 đã chốt trong sổ trước
Đã áp: 9 sửa Màn · 2 component (Checkbox, Link — đã chuyển sang innvie · Components) · 3 giữ Figma
Đo lại: 0 còn lệch | 1 còn lệch: <…>
Máy không kiểm: icon · bóng đổ · ảnh · khối tự dựng chỉ so được qua ảnh
Sổ: docs/account-access/html-design/account-access-proto-check.md (+12 dòng)
Task: BL-NNN /figma-sync account-access (2 chữ mới) | không có
Trang duyệt: <link>
```

## References

- @.claude/rules/approval-gate.md
- @.claude/rules/design-system.md
- @.claude/rules/ui-review.md
- @.claude/rules/screen-source.md
- @.claude/rules/naming-conventions.md (mục Màn hình & flow)
- @.claude/rules/feature-bootstrap.md
- @.claude/rules/worktree.md
- @.claude/rules/backlog.md
- `design/setup-figma.md` mục *Design system: innvie và Astryx tách riêng*
- `_scripts/proto-figma-diff.py`, `_scripts/proto-probe.js`, `references/figma-probe.js`
