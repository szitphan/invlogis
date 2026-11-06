---
name: ds-antd-component
description: Dùng khi cần dựng một component mới (hoặc làm lại theo chuẩn) cho bộ thử DS Ant Design — nguồn shadcnuikit + API ng-zorro → trang chọn biến thể → spec → Figma 3 tầng L0/L1/L2 → trang duyệt. `/ds-antd-component <tên> [--from <bước>]`. DS v2 thì dùng `/figma-component`.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, Skill, AskUserQuestion, ToolSearch, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_write, mcp__claude_ai_Figma__create_session, mcp__claude_ai_Figma__use_figma, mcp__claude_ai_Figma__get_screenshot, mcp__claude_ai_Figma__get_metadata, mcp__claude_ai_Figma__get_variable_defs, mcp__claude-artifacts__guide, mcp__claude-artifacts__publish_version, mcp__claude-artifacts__publish_files, mcp__claude-artifacts__declare_capabilities, mcp__claude-artifacts__db_list, mcp__claude-artifacts__db_get, mcp__claude-artifacts__read_comments
user-invocable: true
argument-hint: "<tên component ng-zorro, vd switch | date-picker> [--from nguon|chon|cautruc|spec|figma|trinhbay|kiem|duyet|chot]"
---

# /ds-antd-component — một component của bộ thử AntD, từ nguồn tới Figma đã duyệt

Quy trình chuẩn hoá từ ba lần làm Button, Input, Select (06–07/11). Áp cho 13 trang còn lại và 28 component
đợt tới (BL-499). **Một component mỗi lần chạy.** Bộ thử độc lập với DS v2 (`design-system/`) và DS cũ (`design/`):
không đọc, không sửa hai bộ đó.

## Đầu vào cố định

| Thứ | Ở đâu |
|---|---|
| File Figma bộ thử | `ElvhTYV3unixPkXky2oKIY` (Invlogis DS · AntD pilot) — mỗi component một trang |
| Nguồn giao diện | shadcnuikit.com/components/{k} (ví dụ đánh số `web-NN`) + Figma kit `uSGI07mEcItaHEVre2RwFq` (chỉ xem, đọc qua Chrome) |
| Nguồn thuộc tính | API ng-zorro-antd 22.x (`nz…`), biến Less `components/style/themes/default.less` |
| Foundation | `design-system-antd/foundations/foundations.md` · `token-mapping.md` (bảng duy nhất) |
| Mẫu đã chốt | `design-system-antd/components/input.md` + trang Input `47:2` (khuôn đầy đủ nhất) · `button.md` · `select.md` |
| Danh sách việc | BL-499 (28 component, trang chọn component db `picks`) · BL-497 (7 tab dựng tạm) |

## Constraints

### Hard rules

1. **Biến thể và thuộc tính bám API ng-zorro**; shadcnuikit chỉ quyết giao diện. Không chép số thô — mọi con số gắn
   Figma variable. Số không gắn được → hỏi user, chốt rồi thêm token vào `token-mapping.md` (1:1 · Ghi đè · Thêm mới).
2. **Ba tầng, ba section trái → phải** trên trang component:

   | Tầng | Tên component | Là gì | Chữ mẫu |
   |---|---|---|---|
   | `L0 · Element` | `_{Comp}/Element/{Phần}` (gạch dưới = ẩn khỏi thư viện, khoá) | Chi tiết bên trong, không dùng riêng: addon, khối, nhãn, icon nút… Phép thử: đặt một mình trên màn có đủ nghĩa không — không thì là L0 | Trung tính |
   | `L1 · Base` | `{Comp}/Base` (+ `{Comp}/Base/{Khung}`) | Khung gốc không ngữ cảnh: trục ng-zorro `Kiểu × Cỡ × Trạng thái` + **khe** bật tắt (exposed instance L0) + trục `Loại` cho các tổ hợp khe chính | Trung tính ("Nhãn", "Placeholder") |
   | `L2 · Content` | `{Comp}` | Ma trận `Loại` (tên nghiệp vụ) × `Trạng thái` vòng đời, ghép từ instance L1 | Ngữ cảnh thật |

3. **Component hoá chi tiết bên trong** (kiểu kit shadcn Input Group): phần khác nhau giữa các "kiểu ô" thành L0 có
   biến thể + khe trên L1, KHÔNG thêm trục variant khổng lồ (bài học Input 468 biến thể).
4. **Đặt tên** (user chốt 07/11): tên component tiếng Anh theo ng-zorro; trục và giá trị tiếng Việt thống nhất
   `Loại` · `Kiểu` · `Cỡ` · `Trạng thái` · `Vị trí` (không dùng Type/Bố cục); thuộc tính bật tắt = danh từ;
   chữ = `{tên} · chữ`; icon = `{tên} · icon`.
5. **Ví dụ là biến thể, không phải instance rời**: mỗi mẫu shadcn được giữ rơi vào đúng một trong 4 nhóm (Bước 2);
   không giữ component "mẫu ghép" song song.
6. **Công cụ Figma**: `figma_write` (reqwise) là đường chính. Figma MCP `use_figma` chỉ cho việc reqwise không làm
   được — gắn biến, exposed instance, set >50 biến thể, mổ/sửa cấu trúc hàng loạt — và **báo user mỗi lần dùng**.
   Trước lần `use_figma` đầu tiên: nạp skill `figma:figma-use` + `create_session`.
7. **Không xoá node** khi user chưa xác nhận (auto mode chặn): đổi tên section cũ thành `… — chờ xoá`, dời sang phải,
   ghi vào báo cáo.
8. **Duyệt trên trang artifact, không rải trong chat**: mọi điểm cần user quyết gom lên 1 trang có ô chọn + ô ghi chú
   (db), style innvie-v1 (band #0036B5 + logo, Cal Sans/Inter), có preview thật dựng từ token (Light/Dark).
9. Approval gate: L1 trước khi ghi file repo, L2 (bảng Trước → Sau) khi sửa file đã có. Figma: trình kế hoạch dựng
   (danh sách set, số biến thể, biến mới) và chờ Y trước Bước 5.
10. Không commit. Main thread tự làm; việc quét/sửa nhỏ đơn giản mới giao agent `sonnet`.

### Pitfalls Figma (đã dính, phải phòng)

| Việc | Lỗi | Cách đúng |
|---|---|---|
| `clone()` biến thể rồi append vào set | Lớp con mất `componentPropertyReferences` | Gắn lại theo đường dẫn tên từ biến thể gốc |
| Gắn `componentPropertyReferences` / exposed | Lỗi nếu node chưa nằm trong component; không gắn được lên lớp con trong instance | Append vào component trước rồi mới gắn |
| Thuộc tính TEXT gắn vào lớp chữ | Mọi biến thể nhận chung một default | Đặt default theo biến thể sau khi gắn, kiểm từng biến thể |
| Ghi đè chữ L2 bằng đúng giá trị gốc | Không thành override → đổi gốc là L2 đổi theo | Đổi chữ gốc (trung tính) trước, rồi mới đặt giá trị L2 |
| Kéo biến thể ra khỏi set | Mất tên trục | Đặt lại tên `Trục=Giá trị` |
| `resize()` sau khi đặt AUTO | Hug thành Fixed | Resize trước, đặt sizing sau; instance trong auto-layout đặt HUG |
| Swap icon về chính icon mặc định / đổi icon bằng swap | Mất override màu nét | Chỉ bật boolean; swap xong tô lại màu |
| Sửa nét icon ẩn trong instance | Không thấy node | `figma.skipInvisibleInstanceChildren = false` |
| `use_figma` lỗi giữa chừng | Hoàn tác cả lượt | Chia lượt nhỏ, mỗi lượt một set |
| Chữ tiếng Việt lỗi dấu (Geist) | Glyph sai | Gán lại bằng `deleteCharacters` + `insertCharacters`; kiểm bằng `get_screenshot` |
| Vòng focus (lớp `Focus ring` tuyệt đối ngoài ô) | Bị cắt khi bọc/ghép | Tắt clip mọi khung chứa ô; chụp kiểm đủ 4 cạnh |
| Thêm dòng gợi ý dưới ô | Instance đổi cỡ | Bọc ô vào khung dọc `Ô` (chép layout/fill/bo/biến), root VERTICAL gap 6 hug |
| Ô ghép nhiều input báo lỗi | Viền từng ô rời | Viền 1px + vòng 3px quanh **cả khối**, câu báo dưới khối |
| Đổi master | Mẫu cũ dùng instance cũng đổi theo | Chụp ảnh "trước" TRƯỚC khi sửa master |
| Ảnh chụp | `figma_read`/`node.screenshot()` có lúc trả bản cache hoặc mất dấu | Kết luận bằng `get_screenshot` (bản dựng server) |
| Bo lồng nhau | Lệch góc | r trong = R ngoài − padding, padding đều |

## Approach

Gọi `--from <bước>` để làm tiếp từ một bước (đọc trạng thái trong spec + handoff, không làm lại bước đã xong).

### Bước 0 — Khởi động

1. `figma_status` (plugin kết nối, đúng file). Đọc `foundations.md`, `token-mapping.md`, `input.md` (khuôn), spec
   `components/{k}.md` nếu đã có (tạm dựng → chế độ **làm lại theo chuẩn**).
2. Tra trang `{Comp}` trên Figma (đã có thì liệt kê set, node, section mẫu ghép cũ, số instance ở trang khác dùng nó).
3. Component phụ thuộc component chưa dựng (vd Combobox cần Popover) → báo, đề xuất thứ tự.

### Bước 1 — Thu nguồn (`nguon`)

1. shadcnuikit.com/components/{k}: liệt kê mọi ví dụ `web-NN` (+ nhóm khác nếu trang có, vd `kbd-NN`, `cbx-NN`),
   chụp từng ví dụ, đo số thật bằng computed style qua Chrome (có `antialiased`). Không lấy shadcn/ui gốc.
2. Kit Figma: đọc trang component qua Chrome (MCP không có quyền) — anatomy, ma trận trạng thái, playground.
3. ng-zorro 22.x: API (`nzSize`, `nzType`, `nzStatus`, `nzDisabled`…) → bảng thuộc tính + biến Less liên quan.
4. Lưu `scratchpad/{k}/sources.json` + ảnh. Không ghi repo ở bước này.

### Bước 2 — Trang chọn biến thể (`chon`) — Cửa duyệt 1

Một trang artifact (đọc `guide` trước lần đăng đầu phiên; `declare_capabilities {db, user}` rồi `db_list` kiểm db hoạt động):

- Khối **lưới trạng thái** dựng lại từ token (Light/Dark): `Kiểu × Trạng thái`, `Kiểu × Cỡ` theo ng-zorro.
- Mỗi ví dụ `web-NN`: ảnh nguồn + preview token + **đề xuất** Giữ/Bỏ + nhóm + nơi đến + ô ghi chú. Bốn nhóm:

  | Nhóm | Nghĩa | Về đâu |
  |---|---|---|
  | 1 | Cần **thuộc tính bật tắt mới** trên set có sẵn (không thêm trục) | Khe/thuộc tính L1 |
  | 2 | Thực ra là **component khác** | Task backlog / danh sách 28 |
  | 3 | **Cách ghép** nhiều component | Biến thể L2 (Loại) hoặc chỉ ví dụ màn |
  | 4 | **Trùng** biến thể/thuộc tính đã có | Biến thể L1/L2 có sẵn |

- Câu hỏi cấu trúc chốt sẵn đề xuất (phương án 0 = đề xuất): trục giữ, Cỡ nào, có tách component con nào, có xoá mẫu cũ.
- db: `{comp}-{code}` `{choice 0 đồng ý / 1 sửa, grp, note}`; `q-*` cho câu hỏi; `gnote` ghi chú chung.
- Chờ user báo xong → `db_list` đọc hết → tóm tắt cách hiểu, hỏi lại chỗ ghi chú mơ hồ (không đoán).

### Bước 3 — Thiết kế cấu trúc (`cautruc`)

Từ kết quả Bước 2, lập bảng trình user (AskUserQuestion khi còn lựa chọn thật):

1. **L0**: phần nào thành `_{Comp}/Element/{Phần}`, mỗi phần trục gì.
2. **L1**: trục ng-zorro + khe; `Loại` = `Cơ bản` (đủ Kiểu × Cỡ × Trạng thái) + các Loại theo khe chính
   (chỉ Kiểu/Cỡ mặc định × Trạng thái — **hỏi user nhân đủ hay thưa**). Khe tương ứng bật sẵn trong biến thể Loại đó.
3. **L2**: danh sách `Loại` nghiệp vụ × trạng thái vòng đời của từng Loại (mỗi Loại có bộ trạng thái riêng, không ép cột chung).
4. Số biến thể từng set, biến mới cần tạo, nhóm 2 thành task nào.

### Bước 4 — Spec + token (`spec`)

L1 → ghi `design-system-antd/components/{k}.md` theo khuôn `input.md`: đầu trang (nguồn, ngày chốt, link trang duyệt),
Mục 1 Thuộc tính (ng-zorro ↔ Figma property ↔ giá trị ↔ ghi chú), Trạng thái + token, Cấu trúc L0/L1/L2, bảng node
(điền ở Bước 9). Token mới → `token-mapping.md` (L2). Không meta-text trong doc.

### Bước 5 — Dựng Figma (`figma`)

Trình kế hoạch dựng → Y → làm theo thứ tự, mỗi set một lượt:

1. Biến mới (Light/Dark nếu là màu; code syntax WEB = tên biến Less).
2. L0 (khoá, mô tả từng set) → 3. L1 (khe = exposed instance L0, thuộc tính, `Loại`) → 4. L2 (instance L1, ghi đè ngữ cảnh).
5. Mọi màu/khoảng cách/bo/chữ gắn biến và text style; tương tác cần thiết (vd Chép → Đã chép) bằng prototype.
6. Section mẫu ghép/bản cũ → đổi tên `— chờ xoá` (Hard rule 7).

### Bước 6 — Trình bày trang (`trinhbay`)

- Ba section `L0 · Element` · `L1 · Base` · `L2 · Content` trái → phải; khung tài liệu (1536) bên trái.
- **Set ≥ 2 trục → ma trận**: cột = Trạng thái, hàng = tổ hợp trục còn lại; tiêu đề cột trên cùng, nhãn hàng tím bên
  trái, mô tả theo hàng bên phải, lưới nét đứt tím dọc + ngang (`Lưới …`, khoá). Set 1 trục → danh sách dọc, nhãn tím trái,
  mô tả phải. Tiêu đề set `❖ {Tên}`, viền nét đứt tím.
- L2: **mỗi hàng một Loại**, trạng thái trái → phải theo vòng đời, nhãn trạng thái tím trên từng ô, lưới ngang giữa hàng.
- Khung tài liệu 4 khối cố định: `1 · Mô tả` (tên, mô tả, link spec) · `2 · Playground` (mỗi Loại L2 một case, kèm chú
  thích `Loại · Trạng thái`; Light | Dark **ngang hàng**) · `3 · Ví dụ` = trỏ tới L2 (không instance rời) · `4 · Thuộc tính`
  (bảng ng-zorro ↔ Figma + bảng token).

### Bước 7 — Tự kiểm (`kiem`)

Chạy hết trước khi trình, báo theo từng mục (không gộp "PASS"):

| Kiểm | Cách |
|---|---|
| Số thô chưa gắn biến | Quét fill/stroke/padding/gap/radius/font không có bound variable trong 3 section |
| Chữ mẫu | L0/L1 không còn chữ ngữ cảnh; L2 không còn chữ trung tính lọt |
| Vòng focus đủ 4 cạnh, không clip | `get_screenshot` từng trạng thái Focus/Lỗi/Cảnh báo |
| Chiều cao ô theo Cỡ ở mọi trạng thái | Viền không tính layout; Lỗi/Cảnh báo cùng cao với Mặc định |
| Override còn giữ | Instance ở trang khác dùng component này (Trường form, Popover, Card…) — liệt kê cái mất override |
| Bo lồng nhau, padding đều | Đo trên hình so với spec |
| Khớp nguồn | So ảnh biến thể với ảnh shadcn đã chọn (kích thước, khoảng cách); lệch → ghi lý do |

### Bước 8 — Trang duyệt (`duyet`) — Cửa duyệt 2

Một trang artifact gom mọi điểm: ảnh từng set (Light/Dark), mỗi điểm Đồng ý / Sửa + ghi chú, câu hỏi còn mở (xoá
section cũ, trạng thái nào thừa…). User sửa bằng comment → chỉ sửa đúng phần tử được comment (và bản lặp của nó).
Đề xuất đổi giao diện đã duyệt → hỏi trước, không tự áp. Áp xong chụp lại, đăng bản mới cùng trang.

### Bước 9 — Chốt (`chot`)

1. Spec `{k}.md` (L2): bảng node (trang, section, set, biến thể), khối "Mapping trên Figma".
2. `token-mapping.md` khớp biến thật trên Figma.
3. Backlog: thêm task cho nhóm 2, việc chờ xoá, override cần rà (Xong khi máy kiểm được); đóng task component này nếu xong.
4. Báo cáo cuối: số set/biến thể, biến mới, lần dùng `use_figma` và vì sao, việc còn chờ user.

## Output

- Figma: trang `{Comp}` với 3 section L0/L1/L2 + khung tài liệu.
- Repo: `design-system-antd/components/{k}.md`, dòng mới trong `token-mapping.md`, 2 file nguồn trang duyệt trong
  `design-system-antd/_review/` (`{k}-pick.src.html`, `{k}-review.src.html`).

References:
- @.claude/rules/approval-gate.md
- @.claude/rules/backlog.md
- `design-system-antd/README.md` · `foundations/foundations.md` · `token-mapping.md` · `components/input.md`
