---
name: figma-sync
description: Dùng khi giao diện trên Figma vừa được vẽ hoặc sửa và cần cập nhật lại tài liệu — bảng mô tả màn 5 cột (screens/{flow}.md) và userflow nếu đổi luồng; `--done` để chốt flow, xuất ảnh Figma và đưa vào SRS thay cho wireframe.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_read, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__download_assets
user-invocable: true
argument-hint: "<feature> [--flow <flow-slug>] [--done]"
---

# /figma-sync — Figma đổi thì tài liệu đổi theo

## Mục tiêu

Figma không báo cho repo khi có người sửa. Skill này đối chiếu Figma hiện tại với **mốc** lần đồng bộ trước,
phân loại từng thay đổi, rồi đề xuất sửa đúng chỗ trong tài liệu:

* bảng mô tả màn 5 cột — `docs/{feature}/screens/{flow}.md`;
* userflow — `docs/{feature}/srs/{feature}-userflow.md` khi thêm màn hoặc đổi đường đi;
* nháp `/cr` khi thay đổi chạm quy tắc nghiệp vụ.

`--done` chốt một flow: xuất ảnh Figma, đánh dấu `approved`, sinh lại **Mục 10 Screens** của SRS (danh mục màn
+ ảnh + bảng 5 cột, thay cho wireframe).

Rule nền: `.claude/rules/screen-source.md` (vòng đời, định dạng `screens/`, mốc, bảng phân loại Mục 7).
Đọc rule đó trước nếu chưa có trong ngữ cảnh.

## Khi nào chạy

* **Được gọi inline** ở cuối `/figma-screen` (Bước 7), `/figma-userflow`, `/figma-component` khi đụng màn của
  feature có trong repo — không cần user gõ.
* User gõ sau khi designer sửa tay trên Figma.
* Hook in `[figma-sync] … chốt tay` (task backlog "Chốt giao diện Figma …" vừa đóng) → chạy `--done`.

## Constraints

### Luật cứng

* **Không sửa tài liệu khi chưa qua L1 + L2.** L2 trình dạng bảng **Trước → Sau** theo từng row, không dùng
  unified diff (thói quen duyệt của user).
* **Quy tắc nghiệp vụ không sửa thẳng.** Đổi validation, điều kiện hiện nút, quyền, mã lỗi mới, con số chính
  sách → chỉ sinh nháp `docs/cr/CR-{YYYYMMDD}-{NNN}.md` (theo `/cr`), không đụng spec/UC. Chữ trên Figma đổi
  một con số (vd "24 giờ" → "48 giờ") là đổi quy tắc, không phải đổi chữ.
* **Không bịa nội dung row mới.** Element mới trên Figma → row mới với Items, Control type (tra ngược
  `design/ba-crosswalk.md`), Data type; cột Description chỉ ghi phần thấy được (chữ, trạng thái) và đánh dấu
  `• Cần bổ sung: mục đích, validation, lỗi` rồi hỏi user. Không suy validation từ hình.
* **Xung đột không tự chọn.** Cùng row đổi cả trên Figma lẫn trong `screens/` kể từ mốc → hỏi từng chỗ.
* **Không ghi lên Figma.** Skill chỉ đọc Figma. Tài liệu đúng mà Figma sai → báo, đề nghị `/figma-screen`.
* **Wireframe cũ chỉ xoá sau khi bảng đã sang `screens/` đủ row** (script đếm khớp) và user Y ở L1. Xoá bằng
  `git rm` (lịch sử còn trong git). Không xoá file đang có thay đổi chưa commit — hỏi trước.
* **Mốc chỉ cập nhật sau khi ghi tài liệu thành công.** User bỏ qua một thay đổi → mốc giữ giá trị cũ cho phần
  đó, lần sau còn báo lại (trừ khi user chọn "bỏ qua vĩnh viễn" → ghi vào `ignored` của mốc).
* Không Task sub-agent (skill có HITL).

### Pitfalls

* **Đổi tên layer ≠ đổi nội dung.** So theo `nodeId` trong mốc, không theo tên layer.
* **Instance đổi biến thể** (vd Button `Primary` → `Secondary`) là đổi control/trạng thái mặc định → row
  Description; đổi `Size` hay icon trang trí → chỉ mốc.
* **Dữ liệu mẫu** (tên khách, mã phiếu, số tiền trong bảng mẫu) đổi → không phải đổi tài liệu. Chỉ nhãn cố
  định, tiêu đề, placeholder, câu thông báo, nhãn nút mới là "chữ của sản phẩm". Không chắc → hỏi.
* Frame có tên không theo luật `<[#]> · <web|mob> · <slug>` → không đoán màn; liệt kê ở "Frame không nhận ra".
* Màn dùng chung nhiều flow (vd `record-detail` của 2 flow) → sửa ở file flow chứa màn đó (Mục 2 userflow, cột
  Thuộc flow); nhiều file cùng có block → sửa tất cả trong cùng L2.

## Bước 0 — chọn phạm vi

* No-arg → liệt kê feature có `screens/` hoặc có link Figma trong wireframe index, hỏi chọn. Feature chưa có
  link Figma nào → refuse + route `/figma-screen` (nhóm B, `feature-bootstrap.md`).
* `--flow` không có → mọi flow có link Figma của feature.
* Đọc `srs/{feature}-userflow.md` (Mục 2, 3, 3.5, 3.6), `screens/{feature}-screen-index.md` + file flow,
  `.claude/state/figma/{feature}.json`.

## Bước 1 — kết nối và đọc Figma

1. `figma_status`. Plugin đang mở đúng file → đọc bằng `figma_read`. Không có plugin → Figma MCP chính thức
   (`get_metadata`) với `fileKey` lấy từ link trong index; không có cả hai → dừng, báo cách mở plugin.
2. Liệt kê frame của flow: `figma_read get_page_model` trên trang module; tách tên theo ` · ` (luật *Tên frame*
   của `design/setup-figma.md`) → frame chính 3 phần, trạng thái/modal 4 phần.
3. Mỗi frame: `figma_read scan_text_nodes {nodeId}` (chữ), `get_design_context {nodeId, detail: "compact"}`
   (instance + biến thể, tên layer), liên kết prototype nếu tool trả về `reactions`.
   **Tool không trả liên kết prototype** → ghi "Kênh liên kết: không đọc được" trong báo cáo, không suy từ hình.
4. Lấy `fileKey` + `nodeId` từng frame (link dạng `https://www.figma.com/design/{fileKey}/?node-id={id ':'→'-'}`).

## Bước 2 — lần đầu của flow: chuyển bảng sang `screens/`

Flow chưa có `screens/{flow}.md`:

1. `python3 _scripts/screens-md.py migrate {feature} {flow}` (dry-run) → đọc số row nguồn/đích, link thiếu.
   Lệch row → dừng, báo; không tự sửa script output.
2. Gộp vào L1 (Bước 5): tạo `screens/{flow}.md`, tạo/cập nhật `screens/{feature}-screen-index.md`, xoá
   `html-wireframe/{flow}.html` (hoặc `ascii-wireframe/{flow}.md`).
3. Flow cuối cùng của feature rời `html-wireframe/` → xoá luôn `{feature}-wireframe.html` + `{feature}-wireframe-html-index.md`
   (cùng L1). Tương tự `ascii-wireframe/` + index ASCII. Link tới các file này trong `docs/` (spec, UC
   index, story) → đổi sang `screens/` trong cùng lượt (L2).
4. Chưa có mốc → chụp mốc từ Figma hiện tại (Bước 1) + bản đồ row ↔ node theo tên layer (luật đặt tên layer
   mục 7 Bước 4 `/figma-screen`); row không khớp được node → ghi `nodeId: null`, báo "row chưa gắn node".
   Lần đầu không báo thay đổi nào ngoài việc chuyển bảng.

## Bước 3 — so với mốc, phân loại

Với mỗi màn: so Figma hiện tại ↔ mốc ↔ `screens/{flow}.md`, phân loại theo bảng Mục 7 của `screen-source.md`:

| Phát hiện | Loại | Đích |
|---|---|---|
| Chữ của node gắn row đổi | Chữ | Items / Description của row đó (thay đúng cụm trong ngoặc kép hoặc nhãn) |
| Node gắn row biến mất | Bỏ element | Đề xuất xoá row (hỏi — có thể designer chỉ gộp) |
| Layer/instance mới không gắn row nào | Thêm element | Row mới, Description đánh dấu cần bổ sung |
| Instance đổi component/biến thể | Đổi control | Control type / Description |
| Frame 4 phần mới / mất | Trạng thái | Block `### Trạng thái` + userflow Mục 2 cột Trạng thái |
| Frame 3 phần mới với số chưa có ở Mục 2 | Màn mới | userflow Mục 2 + 3 + block `## Screen:` mới |
| Liên kết prototype mới / đổi đích / mất | Luồng | userflow Mục 3.5 (+ Mục 1 sơ đồ, + Mục 3.6 nếu đổi số bước tác vụ) |
| Chữ đổi chạm con số, điều kiện, quyền, mã lỗi | Quy tắc | Nháp `/cr` |
| Chỉ vị trí, màu, khoảng cách, dữ liệu mẫu | Hình | Chỉ cập nhật mốc |
| Row đổi trong `screens/` từ mốc và node cũng đổi | Xung đột | Hỏi |

## Bước 4 — hỏi phần chưa rõ

Gộp một lượt `AskUserQuestion`: xung đột, row mới cần mục đích/validation, node mất (xoá row hay gộp),
chữ đổi không rõ là sản phẩm hay dữ liệu mẫu. Không hỏi lại điều userflow/spec đã trả lời.

## Bước 5 — L1, rồi L2, rồi ghi

**L1** (prose BA, `ba-conventions.md` Mục 5):

> Em sẽ cập nhật tài liệu theo Figma cho **Liên quy trình**:
> - Bảng mô tả `view-process`: 3 chỗ đổi chữ (nút "Mở chi tiết", câu lỗi tải sơ đồ, tiêu đề panel), 1 element mới (nút Sao chép mã — cần anh bổ sung mục đích)
> - Userflow: thêm trạng thái `Tooltip` cho màn [1.2]; thêm chuyển màn [1.3] → [1.7]
> - Nháp CR: ngưỡng hiển thị lịch sử đổi 5 → 10 dòng (quy tắc, không sửa thẳng)
> - Lần đầu: chuyển bảng sang `screens/view-process.md` (54/54 row), xoá `html-wireframe/view-process.html`
> - Chỉ đổi hình (không sửa tài liệu): 12 chỗ
>
> Apply? (Y / sửa / chọn mục)

**L2** từng file: bảng `Row | Trước | Sau` (userflow: `Mục | Trước | Sau`). Diff > 50 dòng → hỏi xem
đầy đủ hay tóm tắt.

**Ghi:** trước mỗi Write/Edit set `CLAUDE_SKILL_NAME=/figma-sync`, `CLAUDE_CHANGELOG_NOTE` (vd "sync Figma:
3 chữ, 1 row mới"), `CLAUDE_CHANGELOG_AUTHOR` (memory `user-identity`). Chuyển bảng lần đầu:
`python3 _scripts/screens-md.py migrate {feature} {flow} --write` rồi `git rm` wireframe cũ. Cuối cùng ghi mốc
`.claude/state/figma/{feature}.json` (`mkdir -p .claude/state/figma` lần đầu).
Màn chưa có dòng `- **Mô tả:**` (màn mới, hoặc chuyển bảng lần đầu) → tự viết 1–2 câu từ bảng 5 cột, đặt ngay
sau dòng **Figma**; không cần duyệt riêng (user chốt 13/10), chỉ liệt kê trong báo cáo. Đây là cột Mô tả của
danh mục màn SRS Mục 10 (rule `screen-source.md` Mục 8).

Sửa userflow → hook stale tự đánh dấu tài liệu phía sau; nhắc `/figma-userflow` vẽ lại sơ đồ trên Figma nếu
có. Sửa `screens/` của flow đã `approved` → flow về `draft` trong index, Mục 10 của SRS cần sinh lại (báo).

## Bước 6 — `--done`: chốt flow, đưa vào SRS

Điều kiện: flow đã có `screens/{flow}.md`, Bước 3 không còn thay đổi chưa xử lý (chạy sync trước nếu cần).
Không chạy `--done` khi còn xung đột hoặc row "cần bổ sung".

1. Hỏi xác nhận nếu user chưa nói rõ: "Chốt giao diện flow {flow}? (done / chưa)". Gọi từ hook (task backlog
   đã ✅) thì coi là đã xác nhận.
2. Xuất ảnh mỗi frame **chính** (frame trạng thái: hỏi 1 lần "kèm ảnh trạng thái?", mặc định không):
   `download_assets {fileKey, nodeId, defaultFormat: "png", defaultScale: 2}` → `curl -sSfL -o
   docs/{feature}/screens/images/{n-m}-{web|mob}-{slug}.png "<export url>"` (URL tạm, tải ngay). Plugin không
   có MCP chính thức → `figma_read export_node {nodeId, format: "PNG", scale: 2}`. Ảnh < 5KB hoặc lỗi → báo,
   không chèn.
3. L1 gộp: thêm dòng ảnh `![{screenId} · {slug}](images/….png)` sau dòng **Figma** của mỗi màn, index cột
   Status → `approved` + Updated, sinh lại danh mục + chi tiết màn trong spec Mục 10
   (`python3 _scripts/screens-md.py appendix {feature} --write`). Spec chưa có 2 cặp marker `screens-catalog` /
   `screens` (spec cũ, còn bảng tay hoặc "Phụ lục B") → L2 đặt marker theo `_templates/srs-spec.md` Mục 10
   trước; 2 khối máy sinh thì chỉ báo số flow/màn.
4. Kiểm: `python3 _scripts/screens-md.py appendix {feature} --check` → exit 0. Khác 0 → báo nguyên văn.
5. Task backlog "Chốt giao diện Figma {feature} · {flow}" tự đóng (Xong khi grep `approved`).

## Bước 7 — báo cáo

```
Đồng bộ Figma — Liên quy trình (file <tên>, mốc 2026-10-12 → 2026-10-13)
view-process     3 chữ · 1 row mới (cần bổ sung) · 1 trạng thái mới · 12 chỉ đổi hình
search-process   không đổi
Userflow: Mục 2 (+1 trạng thái), Mục 3.5 (+1 chuyển màn) | không đổi
CR nháp: CR-20261013-002 — lịch sử 5 → 10 dòng | không có
Chuyển bảng lần đầu: view-process 54/54 row, đã xoá html-wireframe/view-process.html
Kênh liên kết prototype: đã đọc | không đọc được — <lý do>
Frame không nhận ra: <liệt kê> | không có
Done: view-process approved · 15 ảnh · Mục 10 khớp | —
Bước tiếp: /figma-userflow (sơ đồ Figma lệch Mục 3.5) · /cr CR-… · /figma-sync --done view-process
```

## Những gì máy KHÔNG kiểm

* **[Cao]** Element mới trên Figma có đúng nghiệp vụ không — skill chỉ ghi nó tồn tại.
* **[Cao]** Chữ đổi có làm sai câu trong spec/UC không (spec không bị sửa, chỉ bảng 5 cột) — rà khi duyệt CR.
* **[Trung]** Liên kết prototype là kênh duy nhất cho luồng; designer đổi luồng mà không nối prototype thì
  skill không thấy.

## References

- `.claude/rules/screen-source.md` — vòng đời, định dạng, mốc, phân loại, done.
- `.claude/rules/approval-gate.md` — L1/L2.
- `.claude/rules/ba-conventions.md` — Mục 5 (L1 cho BA), Mục 6 (độ sâu Description).
- `.claude/rules/ui-common-rules-components.md` — chữ trùng E-common/CMP ghi theo mã.
- `.claude/rules/naming-conventions.md` — screenId, slug, tên frame.
- `.claude/rules/feature-bootstrap.md` — nhóm B.
- `.claude/rules/backlog.md` — task "Chốt giao diện Figma".
- `_scripts/screens-md.py` — `migrate`, `appendix` (sinh Mục 10 Screens của SRS).
- `design/setup-figma.md` › *Tên frame*; `design/ba-crosswalk.md` (control → component, tra ngược).
