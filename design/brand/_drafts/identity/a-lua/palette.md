# Hướng A · Lụa — bảng màu

Nguyên tắc: xanh cobalt ngả tím (hue ~233°) làm chủ đạo, tránh vùng azure 206–217° đối thủ đang đông. Nền giấy ấm thay trắng lạnh. Gradient chiến dịch có hạt nhiễu, vệt có hướng, luôn neo về xanh.

## Màu chủ đạo và trung tính

| Vai trò | Tên | Hex |
|---|---|---|
| Chủ đạo (logo, nút, nhấn) | Cobalt | `#2F43DB` |
| Chữ chính, nền tối | Mực chàm | `#0E1442` |
| Nền tối sâu (splash, reverse) | Chàm đêm | `#0B1033` |
| Đáy gradient ký hiệu | Chàm đậm | `#17206F` |
| Đầu sáng gradient, chữ trên nền tối | Periwinkle | `#97A6FF` (nhạt hơn `#C4CDFF`) |
| Nền phụ, thẻ | Xanh khói | `#E6EAF8` |
| Nền chính | Giấy ấm | `#FAF8F4` |
| Chữ phụ | Xám chàm | `#4A5380` |

## Dải gradient chiến dịch (rực nhiều sắc, neo về xanh)

Thứ tự: `#0E1442` mực chàm → `#2F43DB` cobalt → `#7B55FF` tím → `#E24C9A` hồng → `#FF7A59` san hô. Phụ trợ: `#97A6FF` periwinkle, `#FFD3C0` đào nhạt (vệt sáng), `#FFB547` hổ phách (chỉ điểm nhấn nhỏ, tránh phủ lên nền navy vì ra màu nâu bẩn). Hai phần ba diện tích gradient phải là xanh. Cách làm: 3–4 vệt elip dài xoay khoảng -31°, làm mờ 30–60px, phủ lớp hạt nhiễu (`feTurbulence`, soft-light) — xem `_build_apps.py`.

## Tương phản (python3 _tools/contrast.py)

| Chữ / nền | Tỉ lệ | Kết luận |
|---|---|---|
| `#0E1442` / `#FAF8F4` | 16.53:1 | AA thường đạt |
| `#2F43DB` / `#FAF8F4` | 6.72:1 | AA thường đạt |
| `#2F43DB` / `#FFFFFF` | 7.13:1 | AA thường đạt |
| `#FFFFFF` / `#2F43DB` | 7.13:1 | AA thường đạt |
| `#4A5380` / `#FAF8F4` | 6.97:1 | AA thường đạt |
| `#0E1442` / `#E6EAF8` | 14.61:1 | AA thường đạt |
| `#2F43DB` / `#E6EAF8` | 5.94:1 | AA thường đạt |
| `#FFFFFF` / `#0B1033` | 18.48:1 | AA thường đạt |
| `#97A6FF` / `#0B1033` | 8.11:1 | AA thường đạt |
| `#C4CDFF` / `#0B1033` | 11.90:1 | AA thường đạt |
| `#8B93B8` / `#0B1033` | 6.13:1 | AA thường đạt |
| `#FFFFFF` / `#17206F` | 14.26:1 | AA thường đạt |

Chữ trắng đặt trực tiếp lên vùng gradient có sắc hồng/san hô/periwinkle sáng chưa đo được (nền đổi liên tục): dùng chip kính mờ hoặc thẻ nền sáng cho chữ nhỏ, chỉ để tiêu đề lớn trên gradient.
