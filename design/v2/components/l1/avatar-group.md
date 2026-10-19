---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
  - design/v2/components/l1/avatar.md
---

# Base / Avatar Group

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Avatar Group` (6408:82080, trang L1 · Base),
> khung tài liệu 6415:21043 (hình nên / không nên, cấu tạo phóng 2×) · DEC-205 · ghép từ [Avatar](avatar.md)

## Khi dùng

Nhiều người cùng gắn với một bản ghi, chỗ hẹp: người phụ trách của lệnh, nhóm lái xe của một chuyến, người đã xem.

- **Size:** SM 24 trong hàng bảng web · MD 36 trong dòng danh sách, thẻ · LG 48 ở đầu trang, sheet. Cùng cỡ với Avatar.
- **Count:** hiện tối đa **4** avatar (2 · 3 · 4). Nhiều hơn thì hiện 4 avatar đầu + ô **"+n"** với n = số còn lại
  (6 người → 4 avatar + "+2"). Đủ để nhận ra ai mà vẫn gọn trong một dòng bảng (DEC-205).
- **Overflow:** bật/tắt ô "+n"; sửa chữ ở `Overflow text`. Ô "+n" bấm được thì mở danh sách đủ người.
- Mỗi avatar có viền trắng 2 để tách nhau, avatar sau lùi đè avatar trước **¼ đường kính** (SM 6 · MD 8 · LG 12).
  Đổi từng avatar (ảnh, chữ viết tắt, icon) trên instance con.

## Nên và không nên

Hình minh hoạ ở khung tài liệu cạnh component trên Figma.

1. **Nên:** 4 avatar + "+2" khi có 6 người. **Không nên:** xếp đủ 5–6 avatar làm dòng tràn, đè lên cột kế bên.
2. **Nên:** web bật Tooltip từng avatar để rê chuột thấy tên. **Không nên:** để nhóm avatar không có cách nào biết tên
   (mobile: bấm vào nhóm mở danh sách).

## Trạng thái

Không có trạng thái riêng. Avatar con giữ trạng thái của [Avatar](avatar.md) (Status, Tooltip). Không bật Edit trong
nhóm.

## Chữ

Ô "+n": dấu cộng và số, không khoảng trắng ("+3").

## Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | Kết quả |
|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ "+n" `text/secondary` trên `bg/muted`: 4,92 · chữ viết tắt như Avatar ≥ 8,30 |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | Lưu ý: nền ô "+n" so với nền trắng chỉ 1,10; ô vẫn nhận ra nhờ chữ "+n" (giống nền nút Secondary) |
| 1.1.1 Thay thế ảnh | ✓ cả nhóm có một `aria-label` liệt kê tên ("Nguyễn An, Trần Bình và 2 người khác"); từng avatar `aria-hidden` |
| 4.1.2 Tên, vai trò | ✓ ô "+n" bấm được là nút có tên ("Xem thêm 2 người") |
| **Điểm** | **3/4 đạt** · 1 lưu ý: nền ô "+n" |

## Dùng ở đâu

Cột người phụ trách trong bảng lệnh vận tải (web); thẻ chuyến có nhiều lái xe; danh sách người đã xem, đã duyệt.

## Tên trong code

`<AvatarGroup size="sm|md|lg" max={4} people={[{ name, src, status }]} />` — tự tính "+n" khi `people.length > max`
(hiện `max` avatar + ô "+n"); biến CSS `--avatar-ring`, `--avatar-group-overlap-*`, `--avatar-overflow-*`.

## Phần phụ (máy không đọc)

| Phần | SM | MD | LG | Token |
|---|---|---|---|---|
| Lùi đè (khoảng giữa âm) | −6 | −8 | −12 | `avatar/group-overlap/*` (máy ghi số âm ở Khoảng giữa) |
| Ô "+n" | 24 | 36 | 48 | `avatar/size/*`, nền `avatar/overflow/bg`, chữ `avatar/overflow/fg` |

Bảng máy dưới đây: **Nền** = viền trắng quanh từng avatar (`color/bg/surface`), **Chữ** = chữ ô "+n"; lề = độ dày viền.

## Cấu tạo, thuộc tính, token

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Avatar Group` (6408:82080) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Overflow | Bật tắt | bật | — |
| Overflow text | Chữ | +3 | — |
| Size | Biến thể | SM | SM · MD · LG |
| Count | Biến thể | 2 | 2 · 3 · 4 |

9 biến thể · trục Size × Count.

### Màu theo phần (token)

| Nền | Chữ |
|---|---|
| `color/bg/surface` | `avatar/overflow/fg` |

### Số đo theo phần (token)

| Size | Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo |
|---|---|---|---|---|---|---|---|---|
| SM | 28 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | -6 | `radius/chip` |
| MD | 40 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | -8 | `radius/chip` |
| LG | 52 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | -12 | `radius/chip` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Initials (SM) | `type/caption-strong` |
| Initials (MD) | `type/label` |
| Initials (LG) | `type/title-3` |
| Số còn lại (SM) | `type/caption-strong` |
| Số còn lại (MD) | `type/label` |
| Số còn lại (LG) | `type/title-3` |

<!-- auto:end -->
