---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/logo.md
  - design-system/components/base/logo.md
  - design-system/tokens.json
  - design-system/components/_work/sidebar-navigation/page.json
  - design/ui-common/screen-patterns.md
  - docs/_reverse/account-access/account-access-reverse-spec.md
  - _workspace/decisions.md
---

# Sidebar Navigation · phạm vi làm việc

> Application · phiên bản 0.3.0 · Nháp · người phụ trách @szitphan · Figma: trang DS · Application components, Section
> `Sidebar navigation` — `Sidebar navigation` 6768:194161 (Width=64 6896:206354) · `_Nav item` 6768:192076 ·
> `_Nav tenant switch` 6768:193758 · `_Module tile` 6896:204887 · `_Nav scope card` 6896:205467 · `_Scope option`
> 6896:205515 · `Scope dialog` 6896:206071 · khung tài liệu `Phạm vi làm việc` 6896:212951 · demo `Danh sách lệnh vận tải /
> Web / Phạm vi` 6896:212160 (Section Demo 6768:204061) · DEC-288, DEC-289 · trang duyệt
> https://claude.ai/artifact/8BtztH3oHrmpHCfpfAMZbT · ảnh mốc `_work/sidebar-navigation/preview-web.png`,
> `preview-web-dialog.png`

Menu trái của màn web (CMP-11) và cách chọn **phạm vi làm việc**: chi nhánh → module → cơ sở. Nhóm C (DEC-279): web là
menu trái + hộp thoại; app khác cách thao tác (tab dưới), **chưa dựng** — xem mục Mobile. Bản này bổ sung phần phạm vi
vào bộ `Sidebar navigation` dựng theo Untitled; các Type khác của bộ (Dual Tier, Slim…) giữ nguyên.

Mô hình tổ chức: Công ty → Chi nhánh → Cơ sở. Cơ sở chỉ có ở module chia theo cơ sở (Bảo dưỡng sửa chữa: Xưởng;
Quản lý dầu: Cây dầu, thêm "Ngoài cơ sở"). Danh mục, Quản trị hệ thống là cấp công ty. Công ty mẹ chỉ hiện với người
có quyền xem tổng (SRS cũ tr.197–199, PRD 7.6, FR-account-access-012).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Đầu menu:** logo + tên đơn vị, dòng dưới là **chi nhánh** đang làm (Công ty → Chi nhánh). Người có quyền xem tổng
  chọn công ty mẹ thì dòng này ghi "Toàn tổ chức".
- **Thẻ phạm vi ở chân menu** (D1 D): dòng 1 là module, dòng 2 là cơ sở (D2 A) — "Xưởng Cát Lái", "Tất cả xưởng",
  "Ngoài cơ sở", "Không chia cơ sở" (module không chia), "Toàn công ty" (module cấp công ty). Thay nút chi nhánh ở thanh
  trên và `.Chân menu` cũ.
- **Bấm thẻ → hộp thoại "Đổi phạm vi làm việc"** 3 cột (D4 C): 1 · Chi nhánh (có tìm) · 2 · Module (D3 A — đổi module
  ngay đây, không phải về Trang chủ) · 3 · Cơ sở của module. Chọn theo thứ tự rồi bấm **Chọn** mới chuyển. Chân hộp
  thoại nhắc lại "Đang chọn: {module} · {chi nhánh}".
- Chỉ một phạm vi (1 chi nhánh, 1 module, không chia cơ sở) → thẻ ở trạng thái Read-only, không chevron, không bấm được.
- Đổi phạm vi khi form chưa lưu → hỏi xác nhận trước khi chuyển (GR-13, CMP-03): "Rời trang khi chưa lưu?" · nút chính
  "Ở lại" · nút đỏ "Rời trang và chuyển". Đang chuyển → nút Chọn "Đang chuyển…", vùng nội dung hiện khung chờ, menu giữ
  nguyên.
- Dòng chi nhánh ở đầu menu chỉ để đọc; đổi chi nhánh qua thẻ phạm vi (DEC-289). Thẻ tài khoản ở chân menu không viền,
  nhẹ hơn thẻ phạm vi.
- Chọn công ty mẹ trong hộp thoại → cột 2 báo "Tính năng đang phát triển · Xem dữ liệu toàn tổ chức sẽ có ở bản sau.",
  cột 3 trống, nút Chọn tắt (DEC-289).
- Tìm chi nhánh không ra → giữa cột 1 "Không tìm thấy chi nhánh · Thử tên hoặc tỉnh thành khác.". Tải danh sách lỗi →
  giữa cột "Không tải được danh sách · Kiểm tra kết nối rồi thử lại." + nút Thử lại.
- Thẻ Read-only có tooltip "Chỉ có một phạm vi làm việc"; thẻ thu gọn và thẻ chữ dài có tooltip đủ "{module} · {cơ sở}
  · {chi nhánh}".
- Nhớ phạm vi dùng gần nhất; lần đăng nhập sau vào thẳng phạm vi đó (dòng chi nhánh ghi "Dùng gần nhất" trong hộp thoại).
- Nhóm mục có nhãn chữ hoa (D5 A); mục đang chọn nền xám, chữ đậm (D6 A); số đếm nền xanh nhạt (duyệt preview).

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Khung menu | nền `color/bg/primary`, viền phải `color/border/secondary`, lề `space/lg` | rộng 240; thu gọn 64 (`nav/height`), lề ngang thu gọn 10 |
| Đầu menu | `Logo` (`base/logo.md`, `foundations/logo.md`) Size 24 (`size/3xl`, DEC-326), logo thật không tô ô, không bo; thu gọn 64 dùng Symbol 24; tên `type/heading` nét 600, cao dòng `type/title-3/line-height`, `color/text/primary`; chi nhánh `type/caption` (12/16) `color/text/tertiary`; nút thu gọn `control/height/md` icon 20 | cao tối thiểu 36, khoảng 8, cách nội dung 12 |
| Nhãn nhóm | `type/caption-caps`, `color/text/tertiary` | 12/16, lề trên 16, dưới 6, ngang 10 |
| `_Nav item` | cao 36, lề ngang 10, khoảng 10, bo `radius/control`; chữ `type/body` nét 500 `color/text/tertiary`… đang chọn nền `color/bg/selected`, chữ `color/text/primary` nét 600; icon 20 `color/fg/tertiary` | giữa các mục 2 |
| Số đếm | `Badge` Color Blue: nền `color/utility/blue/50`, chữ `color/utility/blue/700`, `radius/full` | 12/18, lề ngang 8; trên 99 ghi "99+" |
| `_Nav scope card` | nền `color/bg/primary`, viền `color/border/secondary`, bóng `shadow/xs`, bo `radius/md`, lề `space/md`, khoảng `space/lg`; hover `color/bg/primary_hover`, đang mở `color/bg/selected`; dòng 2 trên hai nền đó `color/text/tertiary_strong` | cao 52 (thu gọn 40); chevron lên xuống 16 `color/fg/tertiary` |
| `_Module tile` | nền `color/chip/{tone}/bg`, icon `color/chip/{tone}/fg`, bo `radius/inner`; thẻ thu gọn bo `radius/xs` (ngoại lệ, DEC-328) | 32 (thẻ) · 28 (hộp thoại); icon 20 / 16 |
| Dòng module / cơ sở | `type/heading` nét 600 `color/text/primary` · `type/hint` (12/18) `color/text/tertiary` | 1 dòng, cắt "…", tooltip đủ tên |
| `Scope dialog` | nền `color/bg/primary_alt`, viền `shadow/xl-border`, bo `radius/overlay`, bóng `shadow/xl`, lớp phủ `color/bg/overlay` + `backdrop-blur/lg`; tiêu đề `type/title-3` nét 600 | Bản hộp thoại cũ: chọn phạm vi đã đổi về popover 2 cột (DEC-299), không còn dùng rộng 960; đầu lề 20 / 16; cột lề 8, chia bằng viền `color/border/secondary` |
| Tiêu đề cột | `type/caption` nét 600 `color/text/tertiary` | "1 · Chi nhánh" · "2 · Module" · "3 · {Xưởng / Cây dầu}" |
| `_Scope option` | lề 8, khoảng 10, bo `radius/control`; ô icon 28 nền `color/bg/secondary`; tên `type/body` nét 500; dòng phụ `type/caption` `color/text/tertiary`; chọn: nền `color/bg/selected` + dấu ✓ 16 `color/text/primary`; dòng phụ khi Hover/Selected `color/text/tertiary_strong`; Focus vòng 2px `color/focus/ring` | vùng bấm ≥ 44 |
| Ô tìm | `Input` cao `control/height/md`, viền `color/border/input`, bo `radius/control` | 32, lề ngang 10 |
| Chân hộp thoại | `Button` Secondary "Huỷ" + Primary "Chọn" Size LG (`control/height/lg`), lề 16 / 12, khoảng 8 | 40 |

Màu ô module theo module (cùng tone ở mọi màn): Điều phối vận tải Blue · Quản lý phương tiện Teal · Bảo dưỡng sửa chữa
Yellow · Quản lý dầu Green · Nhân sự Purple · Danh mục, Quản trị hệ thống Gray (`color/chip/gray/*`, DEC-288).
Danh sách module và màu là cấu hình theo khách `[Lõi] [Cấu hình]` — mỗi khách bật module khác nhau.

### Biến thể

- `_Nav scope card`: State = Default · Hover · Focus · Open · Read-only × Collapsed = False · True (Collapsed chỉ ô module 32).
- `_Module tile`: Tone = Blue · Teal · Yellow · Green · Purple · Gray × Size = 32 · 28.
- `_Scope option`: State = Default · Hover · Selected · Focus. Kiểu dòng hệ thống ("Tất cả xưởng", "Ngoài cơ sở", công ty mẹ)
  dùng cùng phần, icon trung tính và vạch chia dưới nhóm.
- `Scope dialog`: Facility = Has · None (cột 3 báo "{Module} không chia cơ sở · Dữ liệu xem theo cả chi nhánh."). Khối
  ẩn bật bằng visible ở instance: `No result` (cột 1), `In development` (cột 2), `Load error` (cột 3).
- `Sidebar navigation`: thêm Width = 64 (thu gọn của Type Sections Subheadings, dựng từ Slim); `Has Scope Card` (bật),
  `Branch`, `Tenant Name`, `Has Tenant Name` (tắt khi logo là logo chữ). `Has Tenant Switch` mặc định tắt. Đầu menu tự
  xuống dòng khi logo rộng (chi nhánh nằm dưới logo). Logo rộng quá 176 thì hạ cao, không dưới 20; Width 64 dùng `P-logo-vuong`,
  thiếu thì chữ cái đầu trên ô (DEC-326).

### Trạng thái

Default · Hover · Focus · Open (hộp thoại đang mở) · Read-only (một phạm vi) · Thu gọn (64, thẻ còn ô module, mục còn icon +
tooltip) · Đang chuyển (vùng nội dung khung chờ) · Đổi khi chưa lưu (hộp thoại xác nhận) · Tất cả cơ sở · Chữ dài ·
Tìm không ra · Lỗi tải (Thử lại) · Chọn công ty mẹ (đang phát triển) · Focus dòng chọn. Mọi trạng thái có hình ở khung
tài liệu `Phạm vi làm việc`.

### Kích thước

Một cỡ: menu 240 / 64, hộp thoại 960. Dưới 1280 menu thu gọn mặc định; dưới 768 dùng bản app (chưa dựng).

### Nên và không nên

- Nên: luôn hiện đủ module + cơ sở ở chân menu và chi nhánh ở đầu menu — nhìn một lần biết đang làm ở đâu.
- Nên: dữ liệu tạo mới tự gắn phạm vi đang chọn và nói ra trên form ("Lệnh mới tự gắn CN Hồ Chí Minh · Xưởng Cát Lái").
- Không: đổi phạm vi ngay khi bấm một dòng — phải bấm Chọn (tránh chuyển nhầm giữa chừng).
- Không: đặt nút chi nhánh ở thanh trên song song với thẻ phạm vi (hai nơi cùng nghĩa).
- Không: dùng màu ô module làm cách duy nhất để nhận module — luôn có tên.

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: tên, mục 17,7:1; dòng phụ, nhãn nhóm `text/tertiary` trên nền trắng 4,74:1; trên nền hover/đang chọn dùng
  `text/tertiary_strong` 7,49:1 / 7,17:1 (`text/tertiary` ở đó chỉ 4,35:1, DEC-289); số đếm blue/700 trên blue/50 ≥ 4,5:1.
- 1.4.11: ô tìm viền `border/input` ≥ 3:1 (vòng 3 sửa từ #D4D4D4); thẻ phạm vi tách nền bằng viền + bóng, bấm được nhờ chevron.
- 2.4.7 / 2.4.11: focus vòng 2px (`focus/width`) cách 2px `color/focus/ring` trên thẻ, mục, dòng chọn (`_Scope option`
  State=Focus).
- 2.5.8: mục 36, thẻ 52 (thu gọn 40), dòng chọn ≥ 44, nút 40, ô tìm 32, nút đóng 28 — đều ≥ 24.
- 2.1.2 / 2.4.3: focus giữ trong hộp thoại; thứ tự Tab: ô tìm → cột 1 → cột 2 → cột 3 → Huỷ → Chọn → Đóng; mở hộp thoại
  focus vào dòng đang chọn của cột 1.
- 3.3.2 / 1.3.1: ô tìm gắn nhãn bằng tiêu đề cột "1 · Chi nhánh" (aria-labelledby), không dựa vào placeholder.
- 1.4.10: dưới 768 px CSS (gồm zoom 400%) dùng bản app (màn toàn trang), không ép 3 cột.
- 1.4.13: tooltip hiện cả khi focus, đóng được bằng Esc, rê chuột vào tooltip không mất.
- 4.1.2: thẻ phạm vi là nút `aria-haspopup="dialog"`, tên đọc "Phạm vi làm việc: {module}, {cơ sở}, {chi nhánh}. Đổi";
  hộp thoại `role="dialog"` có tiêu đề; mỗi cột là `radiogroup` có nhãn cột; mục đang mở `aria-current="page"`; nút đóng
  tên "Đóng"; thẻ Read-only là phần tử tĩnh (không phải nút) vẫn đọc đủ phạm vi; thẻ thu gọn có tên đọc như thẻ mở rộng.
- 2.1.1: Tab giữa 3 cột và chân hộp thoại, mũi tên lên xuống trong cột, Enter chọn dòng, Esc đóng và trả focus về thẻ.
- 4.1.3: đổi xong đọc "Đã chuyển sang {module} · {cơ sở}" (vùng thông báo lịch sự); cột 3 đổi danh sách khi đổi chi
  nhánh / module và chân "Đang chọn: …" là vùng `aria-live="polite"`.
- 1.3.1: thu gọn — mục còn icon có tên đọc = nhãn, rê chuột / focus hiện tooltip.

### Thuộc tính

`_Nav scope card`: `Module`, `Scope` (dòng 2), `Tile` (instance `_Module tile`). `_Scope option`: `Title`, `Subtitle`,
`Has Subtitle`, `Has Lead Icon` (ô icon), `Has Module Tile` (`_Module tile`, đã expose). `_Module tile`: đổi icon bằng
instance swap trên lớp `Icon` (không có thuộc tính swap — gắn thuộc tính làm mọi biến thể về một icon). `Scope dialog`:
`Selection` (chữ chân hộp thoại; một giá trị mặc định cho cả hai biến thể, instance ghi đè). `Sidebar navigation`:
`Branch`, `Tenant Name`, `Has Tenant Name`, `Has Scope Card` + các thuộc tính đã có (`Has Tenant Switch` mặc định tắt).

### Thành phần lồng

`_Nav item`, `Badge` (Blue), `_Nav scope card`, `_Module tile`, `_Scope option`, `Input`, `Button` (Secondary, Primary LG),
`Close button`, `Tooltip`, icon Lucide.

### Được dùng trong

CMP-11 Sidebar Menu (mọi màn web trong module) · account-access FR-account-access-012 (đổi chi nhánh trong phiên) ·
common-workspace UC00.00.06 (đổi module, cơ sở — không còn phải về Trang chủ).

### Token

Số đo theo mode ở bảng Cấu tạo; màu ở Phần máy. Đối chiếu đủ 127 giá trị: `_work/sidebar-navigation/check.json`.

### Kiểm máy

Chạy 28/10 sau khi dựng (vòng 4) và sau khi sửa theo review (vòng 5):

- **layout_audit** 4 bộ mới, `Sidebar navigation`, khung tài liệu: 0 lỗi chặn. Vòng focus tràn khung là có chủ đích (lớp
  tuyệt đối, như `_Nav item`). Chữ "Label" bị cắt ở chân menu các Type cũ: có từ trước, ngoài phạm vi.
- **a11y_audit** (sau sửa): dòng phụ đạt nhờ `text/tertiary_strong`; vùng bấm đều ≥ 24. Còn placeholder Base `Input`
  2,52:1 — component Base, ngoài phạm vi.
- **auditDesignSystem**: không có giá trị gõ cứng trên node của bộ (compliance 0,97–1,00, phần còn lại ở lớp trong icon).
  Ngoại lệ có chủ đích: lề ngang thu gọn 10 (không có token 10 cho lề), lề đầu hộp thoại `space/20` (primitive).
- **Kiểm tên** (DEC-264): đạt sau khi đổi tên demo; giá trị Type "Sections Subheadings", "Sections Dividers" dài hơn 16 —
  có từ trước, giữ (DEC-289).
- **Dark**: bỏ (giá trị Dark DS v2 chưa điền, architecture Mục 7).
- **Kiểm mất hình** (`check-mat-hinh.js`): không áp — Section dựng trước khuôn README (không có `Khối · Web` / `Ô mẫu ·`).
  Thẻ phạm vi trên nền trắng giữ hình bằng viền + bóng.
- **3 agent review** (visual, UX/UI, accessibility): 20 điểm; sửa R1–R4, R6–R13; giữ R5, R14–R19; R20 mở việc riêng
  (DEC-289).

### Chuyển động

Thu gọn 240 ↔ 64 chạy bề rộng `duration/medium` + `easing/standard`, không lò xo; chevron xoay `duration/fast`. `Scope dialog`: vào `duration/medium` + `easing/standard`, phóng 95; ra `duration/exit` + `easing/exit`; thôi chặn bấm ngay khi đóng. Luật chung: `foundations/motion.md` (DEC-333).

## Mobile

Chưa dựng (duyệt preview 28/10: "Chưa cần dựng bản mobile app"). Lựa chọn đã chốt để dùng khi dựng (D7 C + ghi chú):
giữ 4 tab dưới (Trang chủ · Lịch nhắc · Thông báo · Tài khoản), **thẻ phạm vi + chức năng của module nằm ở tab Tài
khoản**; chạm thẻ mở màn toàn trang "Đổi phạm vi làm việc" (bản app của hộp thoại 3 cột, nút Chọn ở chân); Trang chủ
chỉ có một dòng phạm vi để đọc. Bản nháp: tab 2 của trang duyệt, bản 1.

## Đối chiếu Astryx

| Astryx (`Khung trang`) | Bản này | Vì sao |
|---|---|---|
| Chi nhánh là nút trên Thanh trên 44 | Chi nhánh dưới tên đơn vị, đổi trong hộp thoại | Ba cấp ở hai góc màn dễ thao tác nhầm (D1) |
| `.Chân menu`: module + cơ sở tách hai dòng nút | Một thẻ 2 dòng, một nút | Một chỗ bấm cho cả ba cấp (D2) |
| Đổi module phải về Home (UC00.00.06) | Đổi trong hộp thoại | Bớt một lần chuyển màn (D3) |
| Modal Chọn cơ sở | Hộp thoại 3 cột, dùng lại cho lúc đăng nhập | Giữ quen thuộc, thêm chi nhánh + module (D4) |
| Mục 34, menu 240 / 64, nhãn nhóm chữ hoa, mục chọn nền muted | Mục 36, 240 / 64, giữ nhãn và nền | 36 theo `_Nav item` DS v2 |

## Phần máy (chung Web và Mobile)

### `_Nav scope card`

<!-- auto:begin scope-card -->
<!-- Máy sinh từ Figma `_Nav scope card` (6896:205467) · khối `scope-card` ngày 2026-10-28 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Module | Chữ | Bảo dưỡng sửa chữa | — |
| Scope | Chữ | Xưởng Cát Lái | — |
| State | Biến thể | Default | Default · Hover · Focus · Open · Read-only |
| Collapsed | Biến thể | False | False · True |

10 biến thể · trục State × Collapsed.

### Màu theo phần (token)

| State | Collapsed | Nền | Viền | Chữ | Icon | Bóng |
|---|---|---|---|---|---|---|
| Default | False | `color/bg/primary` | `color/border/secondary` | `color/text/primary` | `color/utility/yellow/700` | `elev/1` |
| Default | True | trong suốt | — | — | `color/utility/yellow/700` | — |
| Hover | False | `color/bg/primary_hover` | `color/border/secondary` | `color/text/primary` | `color/utility/yellow/700` | `elev/1` |
| Hover | True | `color/bg/primary_hover` | — | — | `color/utility/yellow/700` | — |
| Focus | False | `color/bg/primary` | `color/border/secondary` | `color/text/primary` | `color/utility/yellow/700` | `elev/1` |
| Focus | True | trong suốt | — | — | `color/utility/yellow/700` | — |
| Open | False | `color/bg/selected` | `color/border/secondary` | `color/text/primary` | `color/utility/yellow/700` | `elev/1` |
| Open | True | `color/bg/selected` | — | — | `color/utility/yellow/700` | — |
| Read-only | False | `color/bg/primary` | `color/border/secondary` | `color/text/primary` | `color/utility/yellow/700` | — |
| Read-only | True | trong suốt | — | — | `color/utility/yellow/700` | — |

### Số đo theo phần (token)

| Collapsed | Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo | Viền | Cỡ icon |
|---|---|---|---|---|---|---|---|---|---|---|
| False | 52 | 216 | `space/md` | `space/md` | `space/md` | `space/md` | `space/lg` | `radius/lg` | 1 | 32 |
| True | 40 | 40 | `space/xs` | `space/xs` | `space/xs` | `space/xs` | `space/lg` | `radius/control` | 1 | 32 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Module | `type/heading` |
| Scope | `type/caption` |

<!-- auto:end scope-card -->

### `_Module tile`

<!-- auto:begin module-tile -->
<!-- Máy sinh từ Figma `_Module tile` (6896:204887) · khối `module-tile` ngày 2026-10-28 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Tone | Biến thể | Blue | Blue · Teal · Yellow · Green · Purple · Gray |
| Size | Biến thể | 32 | 32 · 28 |

12 biến thể · trục Tone × Size.

### Màu theo phần (token)

| Tone | Nền | Icon |
|---|---|---|
| Blue | `color/utility/blue/50` | `color/utility/blue/700` |
| Teal | `color/utility/teal/50` | `color/utility/teal/700` |
| Yellow | `color/utility/yellow/50` | `color/utility/yellow/700` |
| Green | `color/utility/green/50` | `color/utility/green/700` |
| Purple | `color/utility/purple/50` | `color/utility/purple/700` |
| Gray | `color/utility/neutral/100` | `color/utility/neutral/600` |

### Số đo theo phần (token)

| Size | Cao | Rộng | Bo | Viền | Cỡ icon |
|---|---|---|---|---|---|
| 32 | 32 | 32 | `radius/control` | 1 | 20 |
| 28 | 28 | 28 | `radius/control` | 1 | 16 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|

<!-- auto:end module-tile -->

### `_Scope option`

<!-- auto:begin scope-option -->
<!-- Máy sinh từ Figma `_Scope option` (6896:205515) · khối `scope-option` ngày 2026-10-28 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Title | Chữ | CN Hồ Chí Minh | — |
| Subtitle | Chữ | TP. Hồ Chí Minh · Dùng gần nhất | — |
| Has Subtitle | Bật tắt | bật | — |
| Has Lead Icon | Bật tắt | bật | — |
| Has Module Tile | Bật tắt | tắt | — |
| State | Biến thể | Default | Default · Hover · Selected · Focus |

4 biến thể · trục State.

### Màu theo phần (token)

| State | Nền | Chữ | Icon |
|---|---|---|---|
| Default | `color/bg/secondary` | `color/text/primary` | `color/fg/tertiary` |
| Hover | `color/bg/primary_hover` | `color/text/primary` | `color/fg/tertiary` |
| Selected | `color/bg/selected` | `color/text/primary` | `color/text/primary` |
| Focus | `color/bg/secondary` | `color/text/primary` | `color/fg/tertiary` |

### Số đo theo phần (token)

| Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo | Viền | Cỡ icon |
|---|---|---|---|---|---|---|---|---|---|
| 52 | 304 | `space/md` | `space/md` | `space/md` | `space/md` | `space/lg` | `radius/control` | 1 | 16 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Title | `type/label` |
| Subtitle | `type/caption` |

<!-- auto:end scope-option -->

### `Scope dialog`

<!-- auto:begin scope-dialog -->
<!-- Máy sinh từ Figma `Scope dialog` (6896:206071) · khối `scope-dialog` ngày 2026-10-28 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Selection | Chữ | Đang chọn: Bảo dưỡng sửa chữa · CN Hồ Chí Minh | — |
| Facility | Biến thể | Has | Has · None |

2 biến thể · trục Facility.

### Màu theo phần (token)

| Nền | Chữ | Icon | Bóng |
|---|---|---|---|
| `color/bg/primary` | `color/text/primary` | `color/fg/tertiary` | `elev/3` |

### Số đo theo phần (token)

| Cao | Rộng | Bo | Viền | Cỡ icon |
|---|---|---|---|---|
| 546 | ôm nội dung | `radius/card` | 1 | `control/height/sm` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Title (Has) | `type/label` |
| Title (None) | `type/label` |
| Label (Has) | `type/label` |
| Label (None) | `type/label` |
| Placeholder | `type/body` |
| Subtitle | `type/caption` |
| Selection | `type/caption` |
| Empty title | `type/heading` |
| Empty body | `type/body` |

<!-- auto:end scope-dialog -->

### `Sidebar navigation`

<!-- auto:begin sidebar -->
<!-- Máy sinh từ Figma `Sidebar navigation` (6768:194161) · khối `sidebar` ngày 2026-10-28 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Has Tenant Switch | Bật tắt | tắt | — |
| Has Search | Bật tắt | bật | — |
| Has Featured Card | Bật tắt | tắt | — |
| Has Panel | Bật tắt | tắt | — |
| Account Label | Chữ | Tài khoản | — |
| Panel Title | Chữ | Title | — |
| Has Scope Card | Bật tắt | bật | — |
| Branch | Chữ | CN Hồ Chí Minh | — |
| Tenant Name | Chữ | Delta Logistics | — |
| Has Tenant Name | Bật tắt | bật | — |
| Type | Biến thể | Sections Subheadings | Sections Subheadings · Sections Dividers · Dual Tier · Slim |
| Width | Biến thể | 280 | 280 · 240 · 68 · 64 |

8 biến thể · trục Type × Width.

### Màu theo phần (token)

| Width | Nền | Chữ | Icon |
|---|---|---|---|
| 280 | `color/bg/primary` | `color/text/primary` | `color/utility/blue/700` |
| 240 | `color/bg/primary` | `color/text/primary` | `color/utility/blue/700` |
| 68 | `color/bg/primary` | — | `color/accent/fg` |
| 64 | `color/bg/primary` | — | `color/accent/fg` |

### Số đo theo phần (token)

| Type | Width | Cao | Rộng | Viền | Cỡ icon |
|---|---|---|---|---|---|
| Sections Subheadings | 280 | 900 | 280 | 1 | 32 |
| Sections Subheadings | 240 | 900 | 240 | 1 | 32 |
| Sections Subheadings | 64 | 900 | 64 | 1 | 32 |
| Sections Dividers | 280 | 900 | 280 | 1 | 169 |
| Sections Dividers | 240 | 900 | 240 | 1 | 169 |
| Dual Tier | 280 | 900 | 536 | 1 | 169 |
| Dual Tier | 240 | 900 | 496 | 1 | 169 |
| Slim | 68 | 900 | ôm nội dung | 1 | 32 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Tenant name | `type/heading` |
| Branch | `type/caption` |
| Placeholder | `type/body` |
| Label (Sections Subheadings · 280) | `type/label` |
| Label (Dual Tier · 280) | `type/label` |
| Label (Dual Tier · 240) | `type/label` |
| Label (Sections Dividers · 280) | `type/label` |
| Label (Sections Dividers · 240) | `type/label` |
| Label (Sections Subheadings · 240) | `type/label` |
| Count only | `type/chip-sm-strong` |
| Initials (Sections Subheadings · 280) | `type/label` |
| Initials (Dual Tier · 280) | `type/label` |
| Initials (Slim · 68) | `type/label` |
| Initials (Sections Subheadings · 64) | `type/label` |
| Initials (Dual Tier · 240) | `type/label` |
| Initials (Sections Dividers · 280) | `type/label` |
| Initials (Sections Dividers · 240) | `type/label` |
| Initials (Sections Subheadings · 240) | `type/label` |
| Title (Sections Subheadings · 280) | `type/label` |
| Title (Dual Tier · 280) | `type/heading` |
| Title (Dual Tier · 240) | `type/heading` |
| Title (Sections Dividers · 280) | `type/label` |
| Title (Sections Dividers · 240) | `type/label` |
| Title (Sections Subheadings · 240) | `type/label` |
| Subtitle | `type/body` |
| Module | `type/heading` |
| Scope | `type/caption` |
| Tên công ty | `type/title-3` |

<!-- auto:end sidebar -->
