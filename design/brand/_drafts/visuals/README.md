# Invlogis · Nền gradient lụa + hoạ tiết chứng từ (hướng A · Lụa, DEC-072)

Dựng bằng code (CSS blur + `feTurbulence` hạt nhiễu), không gọi API ảnh. Sinh lại: `python3 generate.py [--only bg|doc|dev|sheet] [--grain 0.42] [--angle -31]`.

## File
| File | Nội dung |
|---|---|
| `gradients.html` | Xem + chọn 9 nền, bật khung vùng đặt chữ, đổi 5 cỡ, hiện tỉ lệ tương phản |
| `generate.py` | Nguồn sinh tất cả (bảng `BG` = nền; `zone()` = vùng chữ; `card()` = thẻ chứng từ) |
| `png/bg-{mã}_{cỡ}.png` | 9 nền × 5 cỡ: 1920x1080, 1080x1350, 1080x1080, 1500x500, 2560x1440 |
| `doc-motifs.html/.png` | 5 thẻ chứng từ (Booking Note, eDO, EIR, Phiếu cân, Tờ khai QR), 3 trạng thái: chờ đọc, vệt quét, trường sáng + nhãn `[..]` |
| `png/doc-hero-*.png` | 3 bố cục thẻ trên nền |
| `device-frames.html/.png` | Khung điện thoại + laptop (CSS), `png/device-*.png` |
| `visuals-sheet.png` | Tổng hợp 1600x2000 |
| `_contrast.json` | Số đo tương phản từng nền × cỡ |

Mã nền: `n1-chamdem`, `n2-cobalt`, `n3-chamtim`, `n4-periwinkle`, `n5-giay-lua`, `n6-muc-cobalt` (neo); `r1-tim-hong`, `r2-lam-tim`, `r3-nang` (rực, ra mắt).

## Luật đặt chữ
- Vùng chữ an toàn (tỉ lệ khung): ngang 16:9 = x 6–52%, y 20–80%; cover 3:1 = x 5–50%, y 18–82%; dọc/vuông = x 8–92%, y 56–92% (đáy). Phần sáng của gradient luôn dồn về phía xa vùng này.
- Nền tối (n1, n2, n3, n6, r1–r3): chữ trắng `#FFFFFF`. Nền sáng (n4, n5): chữ mực `#0E1442`. Không đổi chiều.
- Đo bằng điểm xấu nhất (p99.5) trong vùng, công thức `_tools/contrast.py`: tất cả 45 ảnh đạt chữ thường AA (min 5,5:1, nền r3 ngang). Ngoài vùng: chỉ tiêu đề lớn hoặc đặt chip/thẻ nền đặc.
- Nhãn mono nhỏ trên gradient: dùng chip nền đặc, không đặt thẳng lên vệt sáng.
- Thẻ chứng từ giữ ngoài vùng chữ (nửa phải ngang, nửa trên dọc).

## Thay ảnh màn hình trong khung
Đặt `background-image:url(...)` cho `.scr` (`#screen-phone`, `#screen-laptop`) và xoá khối `.ui` bên trong; hoặc sửa `ui_phone()`/`ui_lap()`.

## Luật chung
Giữ 2/3 diện tích là xanh. Hổ phách chỉ điểm nhỏ trên nền cobalt, không phủ nền chàm. Không dùng xe tải, container, địa cầu, mũi tên, mạch điện, robot.
