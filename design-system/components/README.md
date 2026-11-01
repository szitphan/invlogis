---
type: design-component-guide
status: draft
updated: 2026-10-30
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/tokens.json
  - _workspace/decisions.md
  - _scripts/check-mat-hinh.js
  - _scripts/ds-v2-component-doc.py
  - _scripts/figma-component-export.js
---

# Component DS v2 — thư mục và cách ghi

> Từ 26/10/2026 DS v2 dựng lại theo Untitled UI v8, chia **Base** rồi **Application** (DEC-260); khuôn tài liệu cũ theo cấp
> L0/L1/L2 và ma trận `DS · Components · L0–L3` đã bỏ cùng thư mục `l1/` (DEC-312). Kiến trúc: [architecture.md](../architecture.md)
> mục 4 và 9. Token: [foundations.md](../foundations.md) mục 2 (token component chỉ trỏ Semantic, DEC-313).

## 1. Thư mục

| Đường dẫn | Chứa |
|---|---|
| `base/{slug}.md` | Spec component Base (Buttons, Badges, Avatars, Tooltips…) |
| `application/{slug}.md` | Spec component Application (điều hướng, upload, khối phương tiện, tổ hợp…) |
| `_work/{slug}/` | Trang brainstorm của `/figma-component --html`: `page.json`, `answers.json`, `state.json`, ảnh xem trước. Chốt xong mới ghi md |
| `_deps.json` | Cha dùng con nào, foundation nào, mốc `built` — máy dò bằng `_scripts/ds-deps.py`, không khai tay (`.claude/rules/ds-stale.md`) |
| `platform-names.json` | Tên Angular / Flutter của từng mã (tay viết, DEC-255) |

## 2. Md của một component

- Frontmatter: `type`, `status` (draft · in-review · approved · shipped, hoặc `stale` do máy đánh), `updated`, `links`.
- Dòng meta đầu bài: nhóm · phiên bản · trạng thái · Figma set ID · trang duyệt · DEC.
- Khối **Web** rồi khối **Mobile** (component nhóm C một nền tảng thì một khối, DEC-279): tổng quan, cấu tạo, biến thể,
  trạng thái, kích thước, token (tên token kèm số theo mode), trợ năng, nên / không nên.
- Phần máy sinh từ Figma bằng `_scripts/ds-v2-component-doc.py` giữa `<!-- auto:begin web -->` … `<!-- auto:end web -->`.
- Mục "Thành phần lồng" và "Được dùng trong" khớp `_deps.json`.
- Số đo, màu chỉ ghi bằng tên token (`space/md`, `color/text/tertiary`); không mã màu trần, không gọi Primitive.

## 3. Luật nền ô mẫu (chống mất hình)

- Mọi hình component mẫu (biến thể, trạng thái, kích thước, cảnh nên/không nên, hình "được dùng trong") nằm trong một
  **ô mẫu**: FRAME tên bắt đầu `Ô mẫu · ` (vd `Ô mẫu · Primary · Hover`, `Ô mẫu · Biến thể · Ghost · Label`,
  `Ô mẫu · Kích thước · Primary · Label · SM`, `Ô mẫu · Cảnh · Nên`).
- Ô mẫu có **nền thật nơi component sống** + LUÔN có viền 1 `color/border/secondary` + bo 12, canh giữa,
  `clipsContent = false` (để vòng focus không bị cắt). Nền ô KHÔNG bao giờ trong suốt (không "mượn" nền khối). Ô nền
  trắng trên khối trắng vẫn giữ viền để thấy ranh giới; ô nền xám (vd Outline) vẫn nền xám.
- Thẻ Nên / Không nên không có nền (viền xanh / đỏ 2); cảnh bên trong là ô mẫu nền thật có viền.
- Bảng nền thật (thêm dòng khi gặp component mới, lấy từ mục "Khi dùng" của md):

| Component / kiểu | Nền ô |
|---|---|
| Mặc định (nút, chip, ô nhập web, dòng, thẻ trong sheet) | `color/bg/primary` (trắng) |
| Button Outline ("nút phụ trên nền xám") | `color/bg/primary` (#F2F4F7) |
| Thẻ đặt trên nền màn app | `color/bg/primary` |
| Thẻ Surface, Dashed, Record Card, Summary Card (Web và Mobile) | `color/bg/primary`, Context = Canvas |
| Thẻ Muted, Selectable Card | `color/bg/primary` |
| Ô nhập app (nền xám cũ) | `color/bg/primary` |

- **Ô mẫu của thẻ** (mọi component ráp trên Base / Card: Card, Selectable, Record, Summary, Status Row khi cảnh có thẻ) có nền
  `color/bg/primary` cả **Web và Mobile**, đặt Variable mode `Context = Canvas` cho ô, không chỉ ở Mobile. Ngoại lệ: thẻ Muted và
  thẻ chọn một (Selectable) đặt trên nền trắng `color/bg/primary` (Muted mất ranh giới trên nền xám). Lý do: thẻ trắng đặt trên
  nền màn xám cả ở web lẫn app; đặt ô trắng thì không chứng minh được ranh giới thẻ (1,10:1 trên xám) và khe vòng focus
  (`focus/gap`) không theo Context.
- Cỡ ô: đều nhau trong một lưới. Cao ô = cao mẫu lớn nhất + 2 × 12 (Button MD: web 56, app 66; lưới Kích thước:
  web 56, app 76). Ô trống (tổ hợp không có) tên `Ô trống · …`, không nền, viền chấm 4/4, chữ "không có" 12
  `color/text/disabled`.
- Đầu cột: tên Semi Bold 13 + ghi chú nền ô 11/14 (vd "trên xám bg/canvas"); `primaryAxisSizingMode = AUTO` (không thì
  ghi chú bị cắt). Đầu hàng rộng 110 (lưới Kích thước 96).
- Mobile: mẫu thấp hơn `touch/min` thì bọc trong khung `Vùng chạm · touch/min` viền chấm tím 3/3, ngoài nút, bo tròn,
  rộng = max(rộng nút, 44), cao 44.
- **Nền xám → mode Context** (collection `Context`: Surface | Canvas): khung hoặc ô nền xám (`color/bg/primary`) đặt
  Variable mode Context = Canvas; nền trắng (`color/bg/primary`) giữ mặc định Surface. Khe vòng focus (`focus/gap`) và ruột
  nút Outline / Ghost khi Focus tự theo nền; thẻ trắng nằm trên nền xám đã tự đặt lại Surface cho nút bên trong (Slot
  Content và Footer), không cần làm gì thêm. Tài liệu component có vòng focus ghi: "khe focus theo `focus/gap`, đặt
  Context=Canvas khi nằm trên nền xám".

## 4. Số liệu — chỉ đọc từ biến

- Mọi con số in ra đọc từ giá trị của biến theo mode của khối đã đặt (đọc biến bằng Plugin API qua `figma_write`/`use_figma`), không gõ tay, không lấy từ trí nhớ.
- Bảng Token · số đo: cột SM · MD · LG (hoặc trục cỡ của component), dòng: cao, lề, lề phía icon, khoảng, cỡ icon, bo,
  chữ (cỡ/dòng, nét), vòng focus, vùng chạm (`touch/min`, ghi "+n/phía" khi thiếu).
- Màu lấy từ collection Component, ghi một lần "một bộ màu cho web và app" nếu không có mode màu theo nền tảng.
- Trợ năng: tương phản tính bằng công thức WCAG trên mã màu token; giữ số đã chấm trong md cũ nếu màu không đổi. Mỗi
  khối chỉ chấm tiêu chí áp cho nền tảng, điểm ghi riêng "Điểm web: n/m", "Điểm app: n/m" (! = đạt có điều kiện, tính
  là đạt):
  - Web: 1.4.3 (+ ngoại lệ Disabled), 1.4.11, 2.4.7 · 2.4.13, 2.5.8 (≥ 24), 4.1.2 (`aria-label`, `aria-busy`), 2.1.1
    (Enter, Space, thứ tự Tab), 1.4.13 nếu có tooltip/nội dung hiện khi rê, 2.3.3. Không chấm 2.5.5.
  - Mobile (user chấp nhận 20/10): 1.4.3 (+ ngoại lệ), 1.4.11, 2.4.7 · 2.4.13 ghi "focus khi có bàn phím ngoài hoặc công
    cụ trợ năng", 2.5.8, 2.5.5 (≥ 44: thiếu thì "!" + code thêm vùng chạm vô hình), 4.1.2 ghi "nhãn trợ năng (như
    aria-label)", 2.1.1 ghi "khi có bàn phím ngoài: Enter, Space; theo thứ tự focus", 2.3.3. Không chấm 1.4.13 khi app
    không có tooltip. Trạng thái Focus của app mô tả "khi điều hướng bằng bàn phím ngoài hoặc trợ năng".

## 5. Kiểm máy "mất hình" (bắt buộc trước khi chụp ảnh trình)

Script: [`_scripts/check-mat-hinh.js`](../../../_scripts/check-mat-hinh.js) (chỉ đọc, không sửa node).

- **Cách chạy:** đọc file, thay `__FRAME_ID__` (dòng `const FRAME_ID`) bằng ID khung tài liệu hoặc khung ô mẫu của component, gửi toàn văn làm
  `code`. Script viết bằng Plugin API gốc (`getNodeByIdAsync`, `setCurrentPageAsync`, `variables…resolveForConsumer`,
  `findAll`): chạy qua `figma_write` nếu proxy hỗ trợ các hàm đó (thử trước bằng một lệnh đọc nhỏ), không được thì
  `use_figma` (chỉ đọc). Ghi vào báo cáo đường nào đã dùng.
- **Nhận diện:** khối qua tên `Khối · Web` / `Khối · Mobile`, ô qua tiền tố `Ô mẫu · `. Mẫu = instance nằm trong ô mà giữa
  nó và ô không có instance nào khác.
- **Đầu ra:** `{ soO, soMau, soCo, co[], satNguong[], soCoLopCon, coLopCon[], satNguongLopCon[], tomTatLop, bang[] }`.
  Mỗi cờ `{ khoi, o, luat, muc, loi }`; `bang[]` là mọi mẫu kèm nền ô, nền thân, tương phản, viền, khe và vòng focus.

Luật, ngưỡng 1,1:1 tương phản WCAG:

| Luật | Kiểm | Cờ |
|---|---|---|
| A | Ô mẫu có nền riêng, khác nền khối hoặc có viền | ✕ lỗi khung → sửa khung |
| B | Nền thân mẫu so với nền ô < 1,1 | ✕ MẤT HÌNH nếu không còn viền ≥ 1,1 và không có vòng focus ≥ 3; ⚠ NỀN CHÌM nếu viền/vòng còn giữ hình. Thân không fill (Ghost, Outline) → "không nền", không cờ |
| C | Khe vòng focus (bóng lan nhỏ nhất) khác nền ô (> 1,01) | ✕ KHE LỘ |
| D | Cùng lưới, cùng Type: Hover / Pressed so với Default < 1,1 | ✕ GIỐNG DEFAULT |

- **Lớp con:** mẫu mà lớp ngoài không có nền (Tooltip: nền ở lớp `Bóng`; Text Field: nền ở khung `Field`) → script đo thêm
  lớp con ĐẦU TIÊN (thứ tự cây, bỏ chữ / vector / lớp ẩn) có nền SOLID. Cờ B và D của lớp con nằm ở `coLopCon[]` (tách
  khỏi `co[]`), sát ngưỡng ở `satNguongLopCon[]`, `tomTatLop` đếm mẫu theo lớp đo. Ghi trong md dạng "⚠ Nền chìm (lớp
  "{tên lớp}")".
- Lỗi luật A là lỗi khung: sửa ngay, chạy lại tới khi A = 0. Cờ B–D trên nền thật là sự thật của component: KHÔNG sửa
  component, KHÔNG đổi nền ô cho đẹp, tài liệu giữ nguyên hình hiện tại; ghi vào báo cáo "Cần user quyết".
- **Không đặt hộp kết quả kiểm máy trên Figma** (user chốt 20/10). Kết quả ghi trong md: mục `### Kiểm máy` ở CUỐI mỗi
  phần `## Web` và `## Mobile` — bảng `Mức | Ô mẫu | Kết quả` gồm dòng Khung (số ô, số mẫu, số lỗi A), từng cờ ✕ / ⚠
  của nền tảng đó (cả lớp ngoài và lớp con), và dòng "Sát ngưỡng" (1,10–1,15). 

## 6. Giới hạn script đã biết

- `figma-component-export.js` đọc thân component ở FRAME có nền; component ráp từ instance phần con thì cột Nền, Viền, Chữ ra trống hoặc nhầm sang cột Icon, "Cỡ icon" lấy rộng của instance phần con, "Viền" luôn 1 (mặc định
  của Figma, không phải nét thật), "Rộng" ghi "ôm nội dung" cho khung dọc (AUTO là chiều cao). Khi gặp: làm sạch JSON xuất ra
  (bỏ cột nhiễu, sửa rộng theo biến thật) trước khi chạy `ds-v2-component-doc.py`, hoặc giữ khối máy lần xuất đọc được; số
  Web/Mobile luôn lấy ở bảng Token của từng phần (mục 4).
- Slot, Instance swap: tên preferred value chỉ tra được trong cùng trang; icon ở trang `✦ DS · Icons` ra mã 8 ký tự, thay bằng tên icon
  trước khi render.
- Phần máy không có số theo mode: số Web/Mobile chỉ nằm ở bảng Token của từng phần (dựng bằng mục 4).

## Hỏi user khi

- Nền thật của component chưa ghi trong md ("Khi dùng" không nói đặt trên nền gì).
- Kiểm máy có cờ B ✕, C, D (đó là quyết định về look đã duyệt, không tự sửa).
- Component có trục chưa có biến theo nền tảng (số không đọc được từ biến).
