---
type: brand-palette
direction: c-hoi-tu
status: draft
updated: 2026-10-14
---

# Hướng C · Hội tụ — bảng màu

Neo ở vùng 1 của nghiên cứu (cobalt ngả tím, hue ~237°), không dùng azure 206–217°. Logo chỉ một sắc xanh chủ đạo; sắc ấm (san hô, hổ phách) nằm trong gradient, không đứng cạnh navy thành cặp phẳng "navy + cam".

## Chủ đạo

| Tên | Hex | HSL | Vai trò |
|---|---|---|---|
| Cobalt | `#1a23d1` | 237° · 78% · 46% | Chữ logo, nút chính, nền khối nhấn |
| Cobalt sâu | `#0f14b3` | 238° · 85% · 38% | Chấm hội tụ, nền gradient tối |
| Mực chàm | `#0f1433` | 232° · 55% · 13% | Chữ thân bài, nền logo đảo màu |

## Trung tính

| Tên | Hex | Vai trò |
|---|---|---|
| Giấy ấm | `#fbf9f5` | Nền tài liệu, web (không dùng trắng lạnh) |
| Xanh khói | `#a2b5cd` | Đường kẻ, nền phụ, chữ phụ trên nền tối |
| Thép | `#4b6d9b` | Chữ phụ trên nền giấy |
| Mực xám | `#5b6a8c` | Dòng "by innvie", chú thích |

## Dải gradient chiến dịch (banner, bìa, splash)

| Điểm dừng | Hex | Ghi chú |
|---|---|---|
| Cobalt sáng | `#2f4dff` | Neo xanh, chiếm ≥ 50% diện tích |
| Chàm đêm | `#0a0d62` | Vùng tối để chữ trắng đứng được |
| Tím | `#7a4dff` | Vệt thứ hai |
| San hô | `#ff6b5e` | Vệt chính có hướng (rotate −30° … −38°) |
| Hổ phách | `#ffa24d` | Vệt mảnh, ít diện tích |

Cách làm: 4–5 mảng elip mờ (blur 40–70px) xoay −30° đến −38° + lớp hạt nhiễu `feTurbulence` (overlay ~40%). Luôn chừa góc tối để đặt chữ. Tránh: tím→xanh mượt có vòng rỗng; nền đen + quầng sáng.

Gradient trong ký hiệu: nét trái tím `#7a4dff` → cobalt; nét phải san hô `#ff6b5e` → cobalt; chấm `#0f14b3` đặc.

## Tương phản (contrast.py)

| Cặp | Kết quả |
|---|---|
| Cobalt `#1a23d1` trên giấy `#fbf9f5` | 9.06:1 · thường AA đạt |
| Mực `#0f1433` trên giấy `#fbf9f5` | 17.10:1 · đạt |
| Trắng trên cobalt `#1a23d1` | 9.52:1 · đạt |
| Trắng trên cobalt sâu `#0f14b3` | 11.86:1 · đạt |
| Trắng trên mực `#0f1433` | 17.98:1 · đạt |
| Mực xám `#5b6a8c` trên giấy | 5.14:1 · đạt |
| Thép `#4b6d9b` trên giấy | 5.04:1 · đạt |
| Xanh khói `#a2b5cd` trên mực | 8.58:1 · đạt |
| San hô `#ff6b5e` trên mực | 6.43:1 · đạt (chỉ làm điểm nhấn, không làm chữ thân) |
| Tím `#7a4dff` trên trắng | 4.85:1 · đạt |

Chữ trắng đặt trên vùng gradient: đo ở vùng tối; không đặt chữ nhỏ lên vệt san hô/hổ phách (chưa đo, trắng trên `#ff6b5e` dưới 3:1).
