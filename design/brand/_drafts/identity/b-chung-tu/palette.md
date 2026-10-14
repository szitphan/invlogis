# Hướng B · Chứng từ — bảng màu

Kết quả đo bằng `_tools/contrast.py`. Màu chủ đạo nằm trong vùng xanh còn trống theo nghiên cứu đối thủ: cobalt ngả tím (hue 234–247°) và navy mực ngả chàm (hue 235°); tránh azure 206–217° nơi đối thủ đông.

## Chủ đạo

| Tên | Hex | Hue | Vai trò | Tương phản |
|---|---|---|---|---|
| Navy mực | `#12163F` | 235° | chữ, logo, nền sâu | trên trắng 17,32:1 · trên giấy ấm 16,02:1 · trên sương 14,95:1 |
| Navy sâu | `#0B0E2B` | 234° | nền splash, nền tối | chữ xanh khói `#9AA8CC` trên đó 7,96:1 |
| Cobalt điện | `#3B4EF2` | 234° | nhấn, vệt quét, liên kết, nút | trắng trên cobalt 5,90:1 · cobalt trên trắng 5,90:1 · trên giấy ấm 5,46:1 |
| Tím chàm | `#5B47F5` | 247° | đầu vệt quét, nhấn phụ | trắng trên tím chàm 5,73:1 |
| Xanh khói | `#9AA8CC` | 223° | viền, chữ phụ trên nền tối | — |
| Xanh sáng (cuối vệt) | `#7AA7FF` | 220° | cuối vệt quét, chỉ dùng làm điểm nhấn nhỏ | không dùng cho chữ |

Lưu ý: navy mực trên cobalt chỉ 2,93:1 (trượt), không đặt chữ navy lên nền cobalt; dùng chữ trắng.

## Trung tính

| Tên | Hex | Vai trò | Tương phản |
|---|---|---|---|
| Trắng | `#FFFFFF` | nền chính (nhiều nền trắng) | — |
| Giấy ấm | `#F7F6F2` | nền ấm cho slide, bài đăng (thực tế dùng `#FAFAF7` ở bản mẫu) | xám chàm trên đó 5,46:1 |
| Sương | `#ECEEF6` | nền khối, thẻ | navy trên sương 14,95:1 |
| Viền | `#D5D9EA` | đường kẻ mảnh, viền thẻ | chỉ trang trí |
| Xám chàm | `#5B6190` | chữ phụ, nhãn | trên trắng 5,90:1 · trên giấy ấm 5,46:1 |

## Vệt quét (gradient của ký hiệu)

`#5B47F5` → `#3B4EF2` (55%) → `#7AA7FF`, góc −38°. Bản đảo trên nền tối: `#A99CFF` → `#8294FF` → `#A6C4FF`.

## Dải gradient chiến dịch (rực, nhiều sắc, neo về xanh)

| Điểm | Hex | Ghi chú |
|---|---|---|
| 0% | `#0E1250` | navy, neo |
| 28% | `#3B4EF2` | cobalt, neo |
| 48% | `#8B5CF6` | tím |
| 68% | `#F062B4` | hồng |
| 86% | `#FF8F63` | cam san hô |
| 100% | `#FFC774` | vàng hổ phách (tỉ lệ nhỏ) |

Cách dùng: các vệt mờ dài cùng hướng −38° (không phải vòng tròn rỗng, không phải gradient tím→xanh phổ thông), phủ **hạt nhiễu** mịn (feTurbulence, soft-light, ~30%), luôn để một phần nền trở về cobalt/navy. Chữ đặt lên gradient dùng trắng trong ô kính mờ hoặc thẻ trắng; chữ navy trên hồng 5,87:1 và trên cam 7,72:1 vẫn đạt.

Tránh: nền đen + glow, gradient tím→xanh kèm vòng rỗng, ảnh stock.
