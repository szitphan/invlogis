---
type: brand-logo
status: approved
updated: 2026-11-02
links:
  - docs/_product/tenant-parameters.md
  - design-system/foundations/logo.md
  - design/brand/invlogis/logo/logo-spec.md
---

# Quy chuẩn bộ logo Delta

Dựng theo khuôn bộ logo Invlogis, dùng làm giá trị Delta của `P-logo` (DEC-325). Trang tổng hợp: `logo-sheet.png`. Figma: file invlogis, DS · Foundations › Logos › Logo khách, component `Delta logo`.
Innvie đã duyệt; Delta đã đồng ý ngày 02/11/2026 (BL-351).

## 1. Cấu tạo

- **Nguồn:** `../delta-logo-moi-goc.svg`, file này chỉ bọc ảnh PNG 900×248. Mọi nét trong bộ được vẽ lại bằng vector theo số đo trên ảnh, trùng 97,8% (IoU, `_src/diff.png`).
- **Chữ DELTA:** E và L liền một khối, chữ E có cạnh vát. Màu mực `#1E1915`.
- **Thanh xanh:** nằm trong hốc chữ E, sát cạnh trái, cách trên, dưới, phải một khe trống. Màu `#0A9849`, đo trên ảnh.
- **Dấu ®:** chữ R lấy từ font STIX Bold, không phải nét gốc. Có file vector gốc của Delta thì thay.
- **Ký hiệu:** chữ D của logo, thanh xanh đặt trong lòng chữ theo đúng luật khe trống của chữ E. Hình này do innvie dựng, logo gốc không có.
- **Đơn vị đo `H`:** chiều cao chữ DELTA.

## 2. Vùng an toàn và cỡ tối thiểu

| | Quy định |
|---|---|
| Vùng an toàn | Chừa trống ít nhất **0,5 H** bốn phía. Thanh điều hướng chật thì tối thiểu 0,25 H. |
| `delta-primary`, `delta-reverse` | Cao ≥ **20px** / 6 mm |
| `delta-small`, `delta-small-reverse` | Dùng khi cao dưới 20px, ít nhất **16px**. Bản này không có ®, vì vòng ® khi đó nhỏ hơn 8px và nhoè. |
| `delta-symbol` | Cao ≥ **20px** / 6 mm. Nhỏ hơn dùng favicon. |
| `delta-stacked` | Cao ≥ **64px** / 16 mm |

## 3. Dùng biến thể nào, khi nào

| File | Khi nào dùng |
|---|---|
| `delta-primary.svg` | Mặc định trên nền sáng, trong phần mềm: đầu menu, đăng nhập, màn chủ app. ® nhỏ cạnh chữ A nên chữ chiếm đủ chiều cao khung. |
| `delta-reverse.svg` | Nền Tối. Chữ trắng, thanh xanh giữ nguyên. |
| `delta-mono-black.svg` | In một màu, đóng dấu. |
| `delta-mono-white.svg` | Trên nền xanh `#1B7B46`, trên ảnh tối. |
| `delta-small.svg`, `delta-small-reverse.svg` | Cao dưới 20px. |
| `delta-symbol.svg`, `-reverse`, `-mono` | Menu thu gọn 64, ảnh đại diện, chỗ không đủ rộng cho cả chữ. |
| `delta-stacked.svg`, `-reverse` | Khung vuông hoặc dọc: splash. |
| `delta-original.svg` | ® to như logo gốc. Dùng khi in ấn, chứng từ cần giữ đúng bản Delta. |
| `favicon.svg` | Favicon chính, tự đổi chữ trắng khi trình duyệt ở chế độ tối. |
| `favicon-16/32/48.png` | Favicon dự phòng, đặt trên ô trắng để đọc được ở cả tab sáng và tab tối. |
| `app-icon-1024.png`, `apple-touch-icon-180.png` | Icon iOS / web app, nền trắng. Nền đầy, hệ điều hành tự bo góc. |
| `android-foreground-432.png` + `android-background-432.png` | Adaptive icon. Ký hiệu nằm trong vòng an toàn 66dp. |

Không có trong bộ: bản khẩu hiệu (không có khẩu hiệu của Delta), bản "International" và bản "Vận hành trên invlogis" (DEC-325).

## 4. Cấm

1. Kéo méo, nén, xoay, đổi khoảng cách chữ, gõ lại logo bằng font.
2. Đổi màu ngoài bảng: mực `#1E1915`, xanh `#0A9849`, trắng, đen.
3. Thêm đổ bóng, viền, phát sáng, gradient.
4. Đặt bản chữ đen lên nền tối: tương phản chỉ 1,01:1 trên nền Tối `#191919`. Dùng `delta-reverse`.
5. Tách thanh xanh khỏi chữ E, hoặc đổi vị trí thanh.
6. Dùng `delta-logo-trong.png` hoặc `delta-logo-goc.jpg` cho chỗ mới. Hai file đó chỉ giữ làm lịch sử.

## 5. Tương phản

Logo là đồ hoạ nên ngưỡng là 3:1 (WCAG 1.4.11).

| Phần / nền | Tỉ lệ | |
|---|---|---|
| Chữ `#1E1915` / trắng | 17,43 | đạt |
| Thanh xanh `#0A9849` / trắng | 3,75 | đạt |
| Chữ trắng / nền Tối `#191919` | 17,58 | đạt |
| Thanh xanh / nền Tối | 4,69 | đạt |
| Chữ trắng / ô xanh `#1B7B46` | 5,29 | đạt |

## 6. Dựng lại

```bash
cd design/brand/delta/logo/_src
python3 build.py   # SVG, favicon, icon, logo-sheet.png
python3 chk.py     # đo độ trùng với ảnh gốc new.png, sinh diff.png
```

Cần Google Chrome (xuất PNG) và font STIX của macOS (chữ R). SVG đã đổi hết thành nét, không phụ thuộc font.
