---
type: design-component
status: draft
updated: 2026-10-26
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
  - design/v2/components/l1/avatar-group.md
  - design/v2/components/l1/tooltip.md
---

# Base / Avatar

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Avatar` (6397:825, trang DS · Components ·
> L0–L3), khung tài liệu `Tài liệu · Avatar` (6474:23680, khối Web 6474:23687, khối Mobile 6474:23694) · L0
> `.avatar / Status` 6405:288, `.avatar / Edit` 6441:85386, `.avatar / Scrim` 6441:85407 · DEC-164, DEC-201…206, DEC-242 (cỡ icon
> theo biến, State Focus), DEC-246 · đi cùng [Avatar Group](avatar-group.md), [Tooltip](tooltip.md)

Một component cho cả web và app, không có biến thể Platform. Cỡ avatar, chấm trạng thái, nút đổi ảnh, viền đọc từ biến
collection Platform và có **cùng số ở hai mode**; cỡ chữ viết tắt đổi theo mode. Phần **Web** và phần **Mobile** dưới
đây mỗi phần tự đứng được: đọc phần của nền tảng mình làm là đủ. Màu (collection Component) giống nhau ở hai nền tảng;
`avatar/bg`, `avatar/fg` đi theo collection Brand (mặc định Than chì).

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Initials:** mặc định khi chưa có ảnh: chữ đầu của họ và chữ đầu của tên trong "Họ tên" (mặc định "NA").
- **Image:** có ảnh đại diện; ảnh phủ kín, cắt tròn. Ảnh lỗi hoặc chưa tải xong thì hiện Initials.
- **Icon:** không có tên, ảnh (tài khoản hệ thống, đối tác); mặc định `icon/user-round`.
- **Upload:** ô trống viền đứt để tải ảnh lên trong form tạo hồ sơ.
- **Cỡ web:** SM 24 bảng, bình luận, chỗ dày · MD 36 dòng danh sách, ô đầu dòng 36 (DEC-164) · LG 48 đầu thẻ, sheet ·
  XL 64 ảnh đổi được trong form · XXL 88 đầu trang hồ sơ (DEC-203). Kéo ra mặc định SM.
- **Chữ viết tắt web:** SM 12/16 · MD 14/20 Medium · LG 17/24 · XL 20/28 · XXL 24/32.
- **Chỉ có ở web:** Tooltip: tên người khi rê chuột hoặc focus, cho avatar đứng một mình không kèm tên (Avatar Group,
  cột người trong bảng); nổi phía trên, cách 4 (DEC-206).
- **Status:** chấm trạng thái 4 loại (DEC-204): Online xanh · Busy cam · Away vàng · Offline chấm rỗng viền xám. Bật
  `Status`, chọn `Type` ở instance con `.avatar / Status`.
- **Edit:** nút đổi ảnh tròn kiểu Button Primary, viền trắng, góc dưới phải; chỉ ở hồ sơ của chính người đó, từ MD trở
  lên. **Không bật Status và Edit cùng lúc:** cả hai nằm ở góc dưới phải.
- **Bấm được:** chỉ khi có Edit hoặc Upload: cả avatar là vùng bấm để chọn hoặc chụp ảnh. Chữ viết tắt: 2 chữ cái viết
  hoa, giữ dấu ("Đỗ Trung" → "ĐT").
- **Focus:** chỉ ở nút đổi ảnh (`.avatar / Edit`) và ô Upload (vòng `.focus / Ring`). Avatar Initials, Image không có
  Focus riêng vì nút đổi ảnh là phần tử nhận focus.

### Cấu tạo

Hình phóng 2× trên Figma: trái Initials · LG · Default bật Edit; phải Image · MD bật Status và Tooltip.

| Phần | Token | Giá trị web |
|---|---|---|
| Nền | Initials, Icon: `avatar/bg`; Image: ảnh phủ kín; Upload: không nền, viền đứt 1 `avatar/upload/border`; State=Focus: vòng `.focus / Ring` bao ô, giữ viền đứt | — |
| Chữ viết tắt | thuộc tính Initials; `type/caption-strong` · `type/label` · `type/title-3` · `title-2` · `title-1` (SM → XXL); màu `avatar/fg` | 12/16 · 14/20 Medium · 17/24 · 20/28 · 24/32 |
| Icon | thuộc tính Icon (DS · Icons), mặc định `icon/user-round`; cỡ `avatar/icon-size/*`; Upload: `icon/camera` cùng cỡ, màu `avatar/upload/fg` | 14 · 20 · 24 · 24 · 24 (SM → XXL) |
| Cỡ | `avatar/size/sm · md · lg · xl · xxl` | 24 · 36 · 48 · 64 · 88 |
| Bo | `radius/chip` | tròn hẳn (9999) |
| Chấm trạng thái | L0 `.avatar / Status`; `avatar/status-size/*`; viền `avatar/ring` màu `color/bg/surface`; màu `avatar/status/online · busy · away · offline` | 6 · 10 · 12 · 14 · 16; viền 2 |
| Nút đổi ảnh | L0 `.avatar / Edit` (MD trở lên); `avatar/edit-size/*`; nền `avatar/edit/bg`, icon camera cỡ `avatar/edit-icon-size/*` màu `avatar/edit/fg`; viền `avatar/ring`; Disabled `button/bg/disabled`; Focus: `.focus / Ring` bao nút (khe `focus/gap`), nền vòng `avatar/edit/bg` | 20 · 24 · 28 · 32; icon 12 · 14 · 16 · 16 |
| Lớp phủ | L0 `.avatar / Scrim` khi State=Uploading: `avatar/scrim` + vòng quay L0 `.button / Spinner` cỡ `avatar/spinner-size/*`, màu `color/text/inverse`; chữ viết tắt ẩn | vòng quay 12 · 16 · 20 · 24 · 28 |
| Tooltip | **Base / Tooltip · Top → xem [tài liệu Tooltip](tooltip.md)** (L1 lồng, không lặp token); nằm trong lớp `Tooltip wrap` tự canh giữa trên avatar, nổi trên cách 4 | bật bằng Tooltip (gắn vào wrap); chữ "Họ tên" đưa ra panel |

### Biến thể

Content × phần bật (Size MD, State Default): Mặc định · Status Online · Busy · Away · Offline · Edit. Upload chỉ dùng
mặc định. 45 biến thể = Initials 15 + Image 15 + Icon 5 + Upload 10 (Uploading, Disabled chỉ cho Initials, Image; Focus chỉ cho Upload).

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | như bảng màu |
| Uploading | lớp phủ `avatar/scrim` (đen 50%) + vòng quay trắng ở giữa; chữ viết tắt ẩn; nút đổi ảnh chuyển kiểu tắt |
| Disabled | nút đổi ảnh xám (như Button Disabled, DEC-174); ảnh, chữ giữ nguyên |
| Focus | vòng `.focus / Ring` (khe `focus/gap`, vòng `color/border/focus`) bao nút đổi ảnh (`.avatar / Edit` State=Focus, avatar bật Edit) hoặc bao ô Upload (Content=Upload State=Focus, giữ viền đứt) |
| Rê chuột | bật Tooltip: tên người "Họ tên" nổi phía trên (chỉ web) |

Icon chỉ có Default; Upload có Default và Focus. Không có Hover, Pressed. Focus chỉ ở nút đổi ảnh và ô Upload vì đó là
phần tử nhận focus: avatar Initials, Image chỉ hiển thị, không có Focus riêng (Figma: cột Focus ở lưới Trạng thái, hàng
Upload).

### Kích thước

| Size | Cỡ | Chữ viết tắt | Chấm | Nút đổi ảnh | Dùng khi |
|---|---|---|---|---|---|
| SM | 24 | 12/16 | 6 | — | bảng, bình luận, chỗ dày |
| MD | 36 | 14/20 Medium | 10 | 20 | dòng danh sách (ô đầu dòng 36) |
| LG | 48 | 17/24 | 12 | 24 | đầu thẻ, sheet |
| XL | 64 | 20/28 | 14 | 28 | ảnh đổi được trong form |
| XXL | 88 | 24/32 | 16 | 32 | đầu trang hồ sơ |

Mọi cỡ ≥ `touch/min` 24 khi bấm được (Upload, Edit).

### Nên và không nên

1. **Nên:** một cỡ MD cho cả danh sách, tên thẳng một đường. **Không nên:** trộn LG và SM trong một danh sách.
2. **Nên:** chấm trạng thái kèm chữ ở dòng phụ (hoặc tooltip và `aria-label`). **Không nên:** chỉ có chấm màu.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | chữ viết tắt `avatar/fg` trên `avatar/bg`: 12,69 (Than chì) · thấp nhất 8,30 (Xanh lá) qua 8 bộ Brand |
| 1.4.3 ngoại lệ — Disabled | ✓ | icon nút đổi ảnh tắt 2,34: được miễn |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | chấm trên viền trắng: Online 5,72 · Busy 5,18 · Away 6,33 · Offline 7,78 · viền đứt, icon ô Upload 5,43 · nút đổi ảnh 15,13 |
| 1.1.1 Nội dung không phải chữ | ✓ | ảnh có `alt` là tên người; tên đã hiện ngay cạnh thì avatar `aria-hidden` |
| 1.4.1 Không chỉ dùng màu | ! | 4 chấm khác nhau chủ yếu ở màu (Offline rỗng) → luôn kèm chữ, hoặc tooltip và `aria-label` ("Họ tên, đang bận") |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ | Tooltip: Esc đóng được, rê lên tooltip không tắt, chỉ tắt khi rời đi (xem [Tooltip](tooltip.md)) |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | State Focus ở nút đổi ảnh (`.avatar / Edit`) và ô Upload: khe 2 `focus/gap` + vòng 2 `color/border/focus` (15,13:1 trên trắng). Initials, Image không có Focus riêng — nút đổi ảnh là phần tử nhận focus |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | cả avatar là vùng bấm: SM 24 · MD 36 trở lên; nút đổi ảnh 20 không đứng riêng |
| 4.1.2 Tên, vai trò | ✓ | Upload, Edit là nút có tên ("Tải ảnh lên", "Đổi ảnh đại diện"); Uploading đặt `aria-busy` |
| 2.1.1 Bàn phím | ✓ | Edit, Upload: Enter, Space mở chọn ảnh; theo thứ tự Tab |
| 2.3.3 Chuyển động (AAA) | ✓ | vòng quay Uploading đứng yên khi bật giảm chuyển động |
| **Điểm web** | | **11/11 đạt** (1 có điều kiện !) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Content | Biến thể | Initials | Initials · Image · Icon · Upload |
| Size | Biến thể | SM | SM 24 · MD 36 · LG 48 · XL 64 · XXL 88 |
| State | Biến thể | Default | Default · Uploading · Disabled · Focus (Uploading, Disabled cho Initials, Image; Focus cho Upload) |
| Initials | Chữ | NA | 2 chữ cái viết hoa, giữ dấu |
| Icon | Đổi component | icon/user-round · Size=24 | mọi icon trong DS · Icons; dùng khi Content=Icon |
| Status | Bật tắt | tắt | chấm trạng thái góc dưới phải |
| Status › Type | Instance lồng | Online | Online · Busy · Away · Offline |
| Edit | Bật tắt | tắt | nút đổi ảnh, MD trở lên; không bật cùng Status; Focus chọn ở instance con `.avatar / Edit` (State=Focus) |
| Tooltip | Bật tắt | tắt | tên người khi rê chuột, focus (gắn vào lớp `Tooltip wrap`) |
| Tooltip › Text | Instance lồng | Họ tên | chữ tooltip, điền tên người |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Chấm trạng thái | `.avatar / Status` · L0 | Type Online · Busy · Away · Offline; Size theo avatar; bật bằng Status | Type (instance lồng) |
| Nút đổi ảnh | `.avatar / Edit` · L0 | MD trở lên; State Default, Disabled theo State avatar, Focus chọn ở instance con (State=Focus); bật bằng Edit | — |
| Lớp phủ | `.avatar / Scrim` · L0 (chứa `.button / Spinner` · L0) | chỉ State=Uploading; Size theo avatar | — |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon khi Content=Icon; Upload cố định icon/camera | Icon |
| Tooltip | `Base / Tooltip` · L1 → xem [tài liệu Tooltip](tooltip.md) | trong lớp `Tooltip wrap` (tự canh giữa); Placement=Top, nổi trên cách 4 | Tooltip (bật tắt) + chữ "Họ tên" |

### Được dùng trong

Kiểm `getInstancesAsync` 20/10 trên toàn file; bỏ instance trong khung tài liệu và instance mồ côi (cha đã xoá:
`.list-row / Leading · Avatar`, `.avatar-group / Item`, `.card / Header`, `.card / Party`…). Base / Tooltip lồng trong
Avatar xem phần Thành phần lồng.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Avatar Group | Avatar 1–4: khung viền trắng `avatar/ring` 2 (`color/bg/surface`), lùi đè ¼ đường kính | Size theo nhóm: SM 24 · MD 36 · LG 48; Image, Initials · Default; instance con đưa ra panel (Content, Initials, Icon, Status, Tooltip); không bật Edit |
| Base / Record Card | Đầu thẻ, ô trái; bật Has Avatar (mặc định tắt); cách tiêu đề `space/gap-md` = 12, canh giữa dọc | Initials · MD (36) · Default; instance đưa ra panel |
| Base / Selectable Card | Ô vòng icon cuối thẻ; bật Has Avatar (mặc định tắt, tắt Has Icon khi bật) | MD (36) · Default; instance đưa ra panel (DEC-236) |
| Base / List Item | Slot `Start Content` (tối đa 1) | gợi ý (preferred) cùng icon; đặt Avatar MD (36) hoặc Content=Icon cho icon trong vòng |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | SM | MD | LG | XL | XXL |
|---|---|---|---|---|---|---|
| Cỡ | `avatar/size/*` | 24 | 36 | 48 | 64 | 88 |
| Bo | `radius/chip` | tròn | tròn | tròn | tròn | tròn |
| Chữ viết tắt | `type/caption-strong` · `label` · `title-3` · `title-2` · `title-1` | 12/16 | 14/20 | 17/24 | 20/28 | 24/32 |
| Icon (Content=Icon) | `avatar/icon-size/*` | 14 | 20 | 24 | 24 | 24 |
| Icon Upload | `avatar/icon-size/*` (`icon/camera`) | 14 | 20 | 24 | 24 | 24 |
| Chấm | `avatar/status-size/*` | 6 | 10 | 12 | 14 | 16 |
| Viền chấm, nút | `avatar/ring` | 2 | 2 | 2 | 2 | 2 |
| Vòng focus (nút Edit, ô Upload) | `focus/width` · `focus/offset` · khe `focus/gap` | 2 · 2 | 2 · 2 | 2 · 2 | 2 · 2 | 2 · 2 |
| Nút đổi ảnh | `avatar/edit-size/*` | — | 20 | 24 | 28 | 32 |
| Icon nút đổi ảnh | `avatar/edit-icon-size/*` | — | 12 | 14 | 16 | 16 |
| Vòng quay | `avatar/spinner-size/*` | 12 | 16 | 20 | 24 | 28 |
| Vùng chạm (khi bấm được) | `touch/min` | 24 ✓ | 24 ✓ | 24 ✓ | 24 ✓ | 24 ✓ |

Chữ: caption-strong Inter Semi Bold, label Inter Medium, title Cal Sans Regular.

Màu (collection Component, một bộ cho web và app):

| Phần | Token | Giá trị |
|---|---|---|
| Nền Initials, Icon | `avatar/bg` | = color/brand/100 · #EBEBEB (Than chì) |
| Chữ, icon | `avatar/fg` | = color/brand/800 · #262626 |
| Viền đứt ô Upload | `avatar/upload/border` | = color/border/input · #5F6B7A |
| Icon ô Upload | `avatar/upload/fg` | = color/text/secondary · #5F6B7A |
| Chấm Online · Busy · Away · Offline | `avatar/status/online · busy · away · offline` | #1B7542 · #C2410C · #8A5300 · #495363 (= color/chip/{green·orange·yellow·gray}/fg) |
| Viền chấm, nút | `color/bg/surface` | #FFFFFF |
| Lớp phủ Uploading | `avatar/scrim` | = color/overlay/scrim · #070C16 50% |
| Nút đổi ảnh | `avatar/edit/bg` · `avatar/edit/fg` | = button/bg/primary #262626 · = button/fg/primary #FFFFFF |
| Nút đổi ảnh tắt | `button/bg/disabled` · `button/fg/disabled` | #F2F4F7 · #98A2B3 |

Tên trong code: `<Avatar size="sm|md|lg|xl|xxl" name="Họ tên" src={…} icon={…} status="online|busy|away|offline"
editable uploading disabled tooltip />`; biến CSS `--avatar-*` (màu, cỡ, chấm, nút đổi ảnh, cỡ icon, cỡ vòng quay, lớp phủ, viền), `--focus-*`,
`--radius-chip`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6474:23680 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 54 ô, 56 mẫu (khối Web; thêm cột Focus và hàng Upload ở lưới Trạng thái) | 0 lỗi A: ô nào cũng có nền thật và viền mảnh |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có ở lớp ngoài (ô Focus: khe `focus/gap` khớp nền ô, không lộ; không có Hover, Pressed) |
| ⚠ Nền chìm | — | không có: nền `avatar/bg` #EBEBEB trên ô trắng 1,19:1; Image, Upload, thẻ Record Card "không nền" ở gốc instance |
| Sát ngưỡng | — | không có ở lớp ngoài; lớp con: Avatar · Disabled [Edit] 1,10 |
| Lớp con (mở rộng script) | 8 cờ | 7 ✕ MẤT HÌNH: khung viền trắng `avatar/ring` của chấm Status (Image · Online, Busy, Away, Offline; Cảnh Nên, Không nên) và "Avatar 1" (Được dùng trong · Avatar Group) trắng trên ô trắng — viền trắng là trang trí, hình giữ nhờ ảnh, chấm màu; 1 ⚠ NỀN CHÌM: Upload · Focus, lớp "Vòng focus" trắng, hình giữ nhờ viền đứt 5,43:1 |

Ô Được dùng trong · Record Card (6474:88739) nền trắng như mọi ô (DEC-258 bỏ Context).

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Initials:** mặc định khi chưa có ảnh: chữ đầu của họ và chữ đầu của tên trong "Họ tên" (mặc định "NA").
- **Image:** có ảnh đại diện; ảnh phủ kín, cắt tròn. Ảnh lỗi hoặc chưa tải xong thì hiện Initials.
- **Icon:** không có tên, ảnh (tài khoản hệ thống, đối tác); mặc định `icon/user-round`.
- **Upload:** ô trống viền đứt để tải ảnh lên trong form tạo hồ sơ.
- **Cỡ app:** SM 24 · MD 36 dòng danh sách, ô đầu dòng 36, chữ cách avatar 12 (`space/gap-md`; bỏ đường K, DEC-259) · LG 48 đầu thẻ, sheet · XL 64 ảnh
  đổi được trong form · XXL 88 đầu trang hồ sơ (DEC-203). Kéo ra mặc định SM.
- **Chữ viết tắt app:** SM 13/18 · MD 15/20 Semi Bold · LG 17/22 · XL 22/28 · XXL 28/34.
- **Khác web:** không Tooltip, không Hover; cỡ avatar như web, chữ viết tắt theo mode Mobile; avatar bấm được (Edit,
  Upload) cần vùng chạm `touch/min` 44: SM, MD thêm vùng chạm vô hình.
- **Status, Edit, Bấm được:** như phần Web (Status 4 loại DEC-204; Edit MD trở lên; không bật Status và Edit cùng lúc;
  chữ viết tắt 2 chữ cái viết hoa, giữ dấu). Focus chỉ ở nút đổi ảnh và ô Upload (khi điều hướng bằng bàn phím ngoài hoặc trợ năng).

### Cấu tạo

Hình phóng 2× trên Figma: trái Initials · LG · Default bật Edit; phải Image · MD bật Status, vòng chấm tím = vùng chạm.

| Phần | Token | Giá trị app |
|---|---|---|
| Nền | Initials, Icon: `avatar/bg`; Image: ảnh phủ kín; Upload: không nền, viền đứt 1 `avatar/upload/border`; State=Focus: vòng `.focus / Ring` bao ô, giữ viền đứt | — |
| Chữ viết tắt | thuộc tính Initials; `type/caption-strong` · `type/label` · `type/title-3` · `title-2` · `title-1`; màu `avatar/fg` | 13/18 · 15/20 Semi Bold · 17/22 · 22/28 · 28/34 |
| Icon | như web; cỡ `avatar/icon-size/*` (Icon và Upload) | 14 · 20 · 24 · 24 · 24 (SM → XXL) |
| Cỡ | `avatar/size/*` | 24 · 36 · 48 · 64 · 88 |
| Bo | `radius/chip` | tròn hẳn (9999) |
| Chấm trạng thái | L0 `.avatar / Status`; `avatar/status-size/*`; viền `avatar/ring` | 6 · 10 · 12 · 14 · 16; viền 2 |
| Nút đổi ảnh | L0 `.avatar / Edit`; `avatar/edit-size/*`; icon camera `avatar/edit-icon-size/*`; Focus: `.focus / Ring` bao nút | 20 · 24 · 28 · 32; icon 12 · 14 · 16 · 16 |
| Lớp phủ | L0 `.avatar / Scrim` + `.button / Spinner` (`avatar/spinner-size/*`) | vòng quay 12 · 16 · 20 · 24 · 28 |
| Tooltip | Base / Tooltip · Top (trong lớp `Tooltip wrap`) → xem [tài liệu Tooltip](tooltip.md) | không dùng trên app, để tắt |
| Vùng chạm | `touch/min` | 44: khi bấm được, SM +10/phía, MD +4/phía vùng chạm vô hình, không đổi hình |

### Biến thể

Như web: Content × phần bật (Size MD, Default); 45 biến thể dùng chung (Upload thêm State Focus).

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | như bảng màu |
| Uploading | lớp phủ `avatar/scrim` + vòng quay; chữ viết tắt ẩn |
| Disabled | nút đổi ảnh xám (DEC-174) |
| Focus | khi điều hướng bằng bàn phím ngoài hoặc trợ năng: vòng `.focus / Ring` bao nút đổi ảnh (State=Focus của `.avatar / Edit`) hoặc bao ô Upload (Content=Upload State=Focus) |

App không dùng Hover, không Tooltip. Focus chỉ ở nút đổi ảnh và ô Upload; Initials, Image không có Focus riêng vì nút đổi
ảnh là phần tử nhận focus. Chưa có Pressed.

### Kích thước

| Size | Cỡ | Chữ viết tắt | Chấm | Nút đổi ảnh | Vùng chạm khi bấm được | Dùng khi |
|---|---|---|---|---|---|---|
| SM | 24 | 13/18 | 6 | — | +10/phía → 44 | chỗ dày |
| MD | 36 | 15/20 Semi Bold | 10 | 20 | +4/phía → 44 | dòng danh sách |
| LG | 48 | 17/22 | 12 | 24 | đủ | đầu thẻ, sheet |
| XL | 64 | 22/28 | 14 | 28 | đủ | ảnh đổi được trong form |
| XXL | 88 | 28/34 | 16 | 32 | đủ | đầu trang hồ sơ |

### Nên và không nên

1. **Nên:** một cỡ MD cho cả danh sách. **Không nên:** trộn LG và SM trong một danh sách.
2. **Nên:** chấm trạng thái kèm chữ ở dòng phụ (và nhãn trợ năng). **Không nên:** chỉ có chấm màu.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | cùng màu với web: 12,69 (Than chì) · thấp nhất 8,30 (Xanh lá) |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | chấm Online 5,72 · Busy 5,18 · Away 6,33 · Offline 7,78 · ô Upload 5,43 · nút đổi ảnh 15,13 |
| 1.1.1 Nội dung không phải chữ | ✓ | ảnh có nhãn là tên người; tên đã hiện cạnh thì ẩn avatar khỏi trình đọc |
| 1.4.1 Không chỉ dùng màu | ! | luôn kèm chữ hoặc nhãn trợ năng ("Họ tên, đang bận") |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | khi điều hướng bằng bàn phím ngoài hoặc trợ năng: State Focus ở nút đổi ảnh (`.avatar / Edit`) và ô Upload (khe 2 `focus/gap` + vòng 2 `color/border/focus`, 15,13:1 trên trắng). Initials, Image không có Focus riêng — nút đổi ảnh là phần tử nhận focus |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | SM 24 · MD 36 trở lên |
| 2.5.5 Kích thước đích (AAA, ≥ 44) | ! | khi bấm được: SM 24, MD 36 code thêm vùng chạm vô hình 44 (+10, +4/phía); LG 48 trở lên đạt |
| 4.1.2 Tên, vai trò | ✓ | Upload, Edit là nút có tên (nhãn trợ năng như `aria-label`); Uploading báo đang bận |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space mở chọn ảnh; theo thứ tự focus |
| 2.3.3 Chuyển động (AAA) | ✓ | vòng quay đứng yên khi bật giảm chuyển động |
| **Điểm app** | | **11/11 đạt** (2 có điều kiện !) |

### Thuộc tính

Như web; khác: `Tooltip` và `Tooltip › Text` không dùng trên app (để tắt).

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Chấm trạng thái | `.avatar / Status` · L0 | Type Online · Busy · Away · Offline; Size theo avatar | Type (instance lồng) |
| Nút đổi ảnh | `.avatar / Edit` · L0 | MD trở lên; State Default, Disabled theo State avatar, Focus chọn ở instance con | — |
| Lớp phủ | `.avatar / Scrim` · L0 (chứa `.button / Spinner` · L0) | chỉ State=Uploading | — |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon khi Content=Icon | Icon |
| Tooltip | `Base / Tooltip` · L1 → xem [tài liệu Tooltip](tooltip.md) | trong lớp `Tooltip wrap`; không dùng trên app | — |

### Được dùng trong

Như web (Base / Avatar Group: Avatar 1–4, SM 24 · MD 36 · LG 48; Base / Record Card: Đầu thẻ, MD 36, cách tiêu đề 12; Base / Selectable Card: ô vòng icon cuối thẻ; Base / List Item: Slot `Start Content`).

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | SM | MD | LG | XL | XXL |
|---|---|---|---|---|---|---|
| Cỡ | `avatar/size/*` | 24 | 36 | 48 | 64 | 88 |
| Bo | `radius/chip` | tròn | tròn | tròn | tròn | tròn |
| Chữ viết tắt | `type/caption-strong` · `label` · `title-3` · `title-2` · `title-1` | 13/18 | 15/20 | 17/22 | 22/28 | 28/34 |
| Icon (Content=Icon) | `avatar/icon-size/*` | 14 | 20 | 24 | 24 | 24 |
| Icon Upload | `avatar/icon-size/*` (`icon/camera`) | 14 | 20 | 24 | 24 | 24 |
| Chấm | `avatar/status-size/*` | 6 | 10 | 12 | 14 | 16 |
| Viền chấm, nút | `avatar/ring` | 2 | 2 | 2 | 2 | 2 |
| Vòng focus (nút Edit, ô Upload) | `focus/width` · `focus/offset` · khe `focus/gap` | 2 · 2 | 2 · 2 | 2 · 2 | 2 · 2 | 2 · 2 |
| Nút đổi ảnh | `avatar/edit-size/*` | — | 20 | 24 | 28 | 32 |
| Icon nút đổi ảnh | `avatar/edit-icon-size/*` | — | 12 | 14 | 16 | 16 |
| Vòng quay | `avatar/spinner-size/*` | 12 | 16 | 20 | 24 | 28 |
| Vùng chạm (khi bấm được) | `touch/min` | 44: +10/phía | 44: +4/phía | 44 ✓ | 44 ✓ | 44 ✓ |

Chữ: caption-strong Inter Semi Bold, label Inter Semi Bold, title Cal Sans Regular. Màu: như bảng màu phần Web.

Tên trong code: cùng component `Avatar` với web; không dùng `tooltip`; avatar bấm được bắt buộc nhãn trợ năng.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6474:23680 ngày 20/10.

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 52 ô, 54 mẫu (khối Mobile; thêm cột Focus và hàng Upload ở lưới Trạng thái) | 0 lỗi A |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có ở lớp ngoài (ô Focus: khe `focus/gap` khớp nền ô) |
| ⚠ Nền chìm | — | không có ở lớp ngoài: `avatar/bg` trên ô trắng 1,19:1 |
| Sát ngưỡng | — | không có ở lớp ngoài; lớp con: Avatar · Disabled [Edit] 1,10 |
| Lớp con (mở rộng script) | 8 cờ | như khối Web: 7 ✕ khung viền trắng `avatar/ring` (chấm Status, "Avatar 1") trắng trên ô trắng; 1 ⚠ Upload · Focus giữ hình nhờ viền đứt 5,43:1 |

Ô Được dùng trong · Record Card (6474:89470) nền trắng như mọi ô (DEC-258 bỏ Context).

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Avatar` (6397:825) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Initials | Chữ | NA | — |
| Icon | Đổi component | icon/user-round · Size=24 | — |
| Status | Bật tắt | tắt | — |
| Edit | Bật tắt | tắt | — |
| Tooltip | Bật tắt | tắt | — |
| Content | Biến thể | Initials | Initials · Image · Icon · Upload |
| Size | Biến thể | SM | SM · MD · LG · XL · XXL |
| State | Biến thể | Default | Default · Uploading · Disabled · Focus |

45 biến thể · trục Content × Size × State.

### Màu theo phần (token)

| Content | State | Nền | Viền | Chữ | Icon | Vòng focus |
|---|---|---|---|---|---|---|
| Initials | Default | `avatar/bg` | — | `avatar/fg` | — | — |
| Initials | Uploading | `avatar/bg` | — | — | — | — |
| Initials | Disabled | `avatar/bg` | — | `avatar/fg` | — | — |
| Image | Default | ảnh (phủ kín) | — | — | — | — |
| Image | Uploading | ảnh (phủ kín) | — | — | — | — |
| Image | Disabled | ảnh (phủ kín) | — | — | — | — |
| Icon | Default | `avatar/bg` | — | — | `avatar/fg` | — |
| Upload | Default | trong suốt | `avatar/upload/border` | — | `avatar/upload/fg` | — |
| Upload | Focus | trong suốt | `avatar/upload/border` | — | `avatar/upload/fg` | `color/border/focus · dày 2 · khe focus/gap · 2` |

### Số đo theo phần (token)

| Content | Size | Cao | Rộng | Bo | Viền | Cỡ icon |
|---|---|---|---|---|---|---|
| Initials | SM | `avatar/size/sm` | `avatar/size/sm` | `radius/chip` | — | — |
| Initials | MD | `avatar/size/md` | `avatar/size/md` | `radius/chip` | — | — |
| Initials | LG | `avatar/size/lg` | `avatar/size/lg` | `radius/chip` | — | — |
| Initials | XL | `avatar/size/xl` | `avatar/size/xl` | `radius/chip` | — | — |
| Initials | XXL | `avatar/size/xxl` | `avatar/size/xxl` | `radius/chip` | — | — |
| Image | SM | `avatar/size/sm` | `avatar/size/sm` | `radius/chip` | — | — |
| Image | MD | `avatar/size/md` | `avatar/size/md` | `radius/chip` | — | — |
| Image | LG | `avatar/size/lg` | `avatar/size/lg` | `radius/chip` | — | — |
| Image | XL | `avatar/size/xl` | `avatar/size/xl` | `radius/chip` | — | — |
| Image | XXL | `avatar/size/xxl` | `avatar/size/xxl` | `radius/chip` | — | — |
| Icon | SM | `avatar/size/sm` | `avatar/size/sm` | `radius/chip` | — | `avatar/icon-size/sm` |
| Icon | MD | `avatar/size/md` | `avatar/size/md` | `radius/chip` | — | `avatar/icon-size/md` |
| Icon | LG | `avatar/size/lg` | `avatar/size/lg` | `radius/chip` | — | `avatar/icon-size/lg` |
| Icon | XL | `avatar/size/xl` | `avatar/size/xl` | `radius/chip` | — | `avatar/icon-size/xl` |
| Icon | XXL | `avatar/size/xxl` | `avatar/size/xxl` | `radius/chip` | — | `avatar/icon-size/xxl` |
| Upload | SM | `avatar/size/sm` | `avatar/size/sm` | `radius/chip` | 1 | `avatar/icon-size/sm` |
| Upload | MD | `avatar/size/md` | `avatar/size/md` | `radius/chip` | 1 | `avatar/icon-size/md` |
| Upload | LG | `avatar/size/lg` | `avatar/size/lg` | `radius/chip` | 1 | `avatar/icon-size/lg` |
| Upload | XL | `avatar/size/xl` | `avatar/size/xl` | `radius/chip` | 1 | `avatar/icon-size/xl` |
| Upload | XXL | `avatar/size/xxl` | `avatar/size/xxl` | `radius/chip` | 1 | `avatar/icon-size/xxl` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Initials (SM) | `type/caption-strong` |
| Initials (MD) | `type/label` |
| Initials (LG) | `type/title-3` |
| Initials (XL) | `type/title-2` |
| Initials (XXL) | `type/title-1` |

<!-- auto:end -->
