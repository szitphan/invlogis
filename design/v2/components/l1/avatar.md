---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Avatar

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Avatar` (6397:825, trang L1 · Base), xem nhanh
> 6407:82466, khung tài liệu 6403:2291 (hình nên / không nên, cấu tạo phóng 2×) · chấm trạng thái `.avatar / Status`
> (6405:288, trang L0) · DEC-164, DEC-201…206 · đi cùng [Avatar Group](avatar-group.md), [Tooltip](tooltip.md)

## Khi dùng

- **Initials:** mặc định khi chưa có ảnh. 2 chữ cái: chữ đầu của họ và chữ đầu của tên ("Nguyễn An" → "NA").
- **Image:** có ảnh đại diện; ảnh phủ kín, cắt tròn.
- **Icon:** không có tên, ảnh (tài khoản hệ thống, đối tác). Mặc định `user-round`; đổi icon thì chọn đúng cỡ
  (SM 14 · MD 20 · LG, XL, XXL 24; thư viện icon chỉ có tới cỡ 24).
- **Upload:** ô trống viền đứt để tải ảnh lên trong form tạo hồ sơ (lái xe, nhân viên).
- **Size:** SM 24 cho bảng web, bình luận, chỗ dày · MD 36 cho dòng danh sách, trong ô đầu dòng 36, chữ ở K4 80
  (DEC-164) · LG 48 cho đầu thẻ, sheet · XL 64 cho ảnh đổi được trong form, trang cài đặt tài khoản · XXL 88 cho đầu
  trang hồ sơ (DEC-203). Cỡ giống nhau ở Web và Mobile.
- **Status:** chấm trạng thái của người, 4 loại (DEC-204): **Online** xanh (đang trực tuyến, lái xe đang ca) ·
  **Busy** cam (đang bận, đang chạy lệnh) · **Away** vàng (vắng mặt, lâu không thao tác) · **Offline** chấm rỗng viền xám.
  Bật `Status` trên avatar, chọn `Type` ở instance con `.avatar / Status`.
- **Edit:** nút đổi ảnh tròn kiểu Button Primary, viền trắng 2, sát góc dưới phải; chỉ ở hồ sơ của chính người đó,
  từ MD trở lên (MD 20 · LG 24 · XL 28 · XXL 32). Không bật Status và Edit cùng lúc: cùng nằm ở góc dưới phải.
- **Tooltip:** chỉ web. Hiện tên người khi rê chuột hoặc focus, dùng khi avatar đứng một mình không kèm tên (Avatar
  Group, cột người phụ trách trong bảng). Tooltip nổi phía trên avatar (DEC-206).

## Nên và không nên

Hình minh hoạ ở khung tài liệu cạnh component trên Figma.

1. **Nên:** dòng danh sách dùng MD 36 trong ô đầu dòng, tên canh ở K4. **Không nên:** trộn nhiều cỡ avatar trong một
   danh sách.
2. **Nên:** chấm trạng thái kèm chữ "Đang trực tuyến" ở dòng phụ hoặc tooltip. **Không nên:** chỉ có chấm màu để báo
   trạng thái.

## Trạng thái

| State | Áp cho | Trông thế nào |
|---|---|---|
| Default | mọi Content | như bảng màu bên dưới |
| Uploading | Initials, Image | lớp phủ `avatar/scrim` (đen 50%) + vòng quay trắng ở giữa; chữ viết tắt ẩn để không bị vòng quay đè; nút đổi ảnh chuyển kiểu tắt |
| Disabled | Initials, Image | nút đổi ảnh kiểu tắt xám (như Button Disabled, DEC-174); ảnh, chữ giữ nguyên |

Avatar không bấm được, trừ khi có Edit hoặc Upload: khi đó cả avatar là vùng bấm để chọn hoặc chụp ảnh. Ảnh lỗi hoặc
chưa tải xong thì hiện Initials. Bản 0.1.0 có vòng tiến độ quanh avatar khi tải ảnh, nay bỏ (DEC-203).

## Chữ

2 chữ cái viết hoa, giữ dấu của chữ cái ("Đỗ Trung" → "ĐT"). Cỡ chữ theo cỡ avatar: SM `caption-strong` · MD `label` ·
LG `title-3` · XL `title-2` · XXL `title-1`.

## Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | Kết quả |
|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ chữ viết tắt `brand/800` trên `brand/100`: 8,30 (Xanh lá) – 12,69 (Than chì) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ chấm trên viền trắng: Online 5,72 · Busy 5,18 · Away 6,33 · Offline 7,78 · viền đứt và icon ô Upload 5,43 · nút Edit 15,13 |
| 1.1.1 Thay thế ảnh | ✓ ảnh có `alt` là tên người; tên đã hiện ngay cạnh thì avatar `aria-hidden` |
| 1.4.1 Không chỉ dùng màu | Lưu ý: 4 chấm khác nhau chủ yếu ở màu (Offline khác thêm ở hình rỗng) → phải kèm chữ, hoặc tooltip và `aria-label` ("Nguyễn An, đang bận") |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ tooltip: Esc đóng được, rê chuột lên tooltip không tắt, chỉ tắt khi rời đi (xem [Tooltip](tooltip.md)) |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ khi cả avatar là vùng chạm; nút Edit 20 đứng riêng ở MD thì chưa đủ → vùng chạm là cả avatar |
| 4.1.2 Tên, vai trò | ✓ Upload, Edit là nút có tên ("Tải ảnh lên", "Đổi ảnh đại diện"); Uploading đặt `aria-busy` |
| **Điểm** | **6/7 đạt** · 1 lưu ý: chấm trạng thái |

## Dùng ở đâu

Dòng danh sách lái xe, nhân viên; đầu thẻ, sheet; đầu trang hồ sơ; bình luận, lịch sử; form tạo hồ sơ; Avatar Group.

## Tên trong code

`<Avatar size="sm|md|lg|xl|xxl" name="Nguyễn An" src={…} icon={…} status="online|busy|away|offline" editable
uploading disabled tooltip />`; biến CSS `--avatar-*` (màu, cỡ, chấm, nút đổi ảnh, lớp phủ, viền), `--radius-chip`.

## Phần phụ (đặt tự do, máy không đọc)

| Phần | SM | MD | LG | XL | XXL | Token |
|---|---|---|---|---|---|---|
| Chấm trạng thái (chưa tính viền 2) | 6 | 10 | 12 | 14 | 16 | `avatar/status-size/*`, màu `avatar/status/online·busy·away·offline`, viền `avatar/ring` |
| Nút đổi ảnh | — | 20 | 24 | 28 | 32 | `avatar/edit-size/*`, `avatar/edit/bg·fg`, viền `avatar/ring`; icon camera 12 · 14 · 16 · 16 |
| Lớp phủ Uploading | phủ kín | | | | | `avatar/scrim`, vòng quay trắng |
| Tooltip | nổi trên, cách 4 | | | | | instance `Base / Tooltip` Placement=Top |

## Cấu tạo, thuộc tính, token

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
| State | Biến thể | Default | Default · Uploading · Disabled |

40 biến thể · trục Content × Size × State.

### Màu theo phần (token)

| Content | Nền | Viền | Chữ | Icon |
|---|---|---|---|---|
| Initials | `avatar/bg` | — | `avatar/fg` | — |
| Image | ảnh (phủ kín) | — | — | — |
| Icon | `avatar/bg` | — | — | `avatar/fg` |
| Upload | trong suốt | `avatar/upload/border` | — | `avatar/upload/fg` |

### Số đo theo phần (token)

| Size | Cao | Rộng | Bo | Cỡ icon |
|---|---|---|---|---|
| SM | `avatar/size/sm` | `avatar/size/sm` | `radius/chip` | 14 |
| MD | `avatar/size/md` | `avatar/size/md` | `radius/chip` | 20 |
| LG | `avatar/size/lg` | `avatar/size/lg` | `radius/chip` | 24 |
| XL | `avatar/size/xl` | `avatar/size/xl` | `radius/chip` | 24 |
| XXL | `avatar/size/xxl` | `avatar/size/xxl` | `radius/chip` | 24 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Initials (SM) | `type/caption-strong` |
| Initials (MD) | `type/label` |
| Initials (LG) | `type/title-3` |
| Initials (XL) | `type/title-2` |
| Initials (XXL) | `type/title-1` |

<!-- auto:end -->
