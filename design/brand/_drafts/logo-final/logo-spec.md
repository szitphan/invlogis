---
type: brand-logo
status: draft
updated: 2026-10-14
links:
  - design/brand/brand-brief.md
  - design/brand/_drafts/logo-final/v-options.md
---

# Quy chuẩn logo invlogis × innvie (bản nháp, chờ founder duyệt)

Hướng A · Lụa (DEC-072), chữ v theo phương án 1 · Gradient nhẹ (DEC-073, `v-options.md`). Trang tổng hợp: `logo-sheet.png`.

## 1. Cấu tạo

- **Chữ:** "invlogis" viết thường, Lexend trọng lượng 340, giãn chữ +20/1000 em. Mọi chữ đã đổi sang nét vector, file không chứa thẻ `<text>` và không phụ thuộc font.
  - Vì sao 340 mà không phải Light 300 như `type.md` cũ: nét 300 chỉ rộng 75/1000 em, đặt logo cao 24px thì nét chưa tới 2px nên trông mỏng manh. Nét 340 rộng 87/1000 em, vẫn thanh nhưng chắc hơn, gần tinh thần "chuyên gia điềm tĩnh". Nếu founder muốn quay về 300, đổi `WGHT` trong `_src/build.py` rồi dựng lại.
- **Chữ i lụa:** chữ cái đầu đồng thời là ký hiệu.
  - Thân i rộng đúng bằng nét chữ (87/1000 em), đầu trên cắt chéo 14°.
  - Chấm i là một mảnh lụa cùng bề rộng, hai cạnh song song với vết cắt, như phần dải lụa gấp ra sau. Chấm sáng hơn thân để gợi mặt sau của lụa.
  - Gradient trên nền sáng: thân `#3A4EE3 → #1B2491`, chấm `#5A6CF0 → #3D51E6`.
  - Gradient trên nền tối: thân `#A3B0FF → #5B6EF5`, chấm `#D6DCFF → #AEB9FF`.
- **Chữ v (phương án 1, DEC-073):** giữ nguyên dáng Lexend, tô chuyển màu dọc từ đầu cánh xuống đáy.
  - Nền sáng: mực chàm `#0E1442` → cobalt `#2F43DB`.
  - Nền tối: trắng → periwinkle `#A3B0FF`.
  - Bản đơn sắc (`mono-black`, `mono-white`) để v một màu, chấp nhận mất điểm nhấn ở bản này.
- **Các chữ còn lại:** màu mực chàm `#0E1442` (nền sáng) hoặc trắng (nền tối). Chữ i thứ hai trong "logis" giữ chấm tròn của Lexend.
- **Đơn vị đo `x`:** chiều cao chữ x. Một `x` bằng khoảng 0,52 chiều cao toàn logo, tính từ đỉnh chấm i tới đáy đuôi g.

## 2. Vùng an toàn và cỡ tối thiểu

| | Quy định |
|---|---|
| Vùng an toàn | Chừa trống ít nhất **1 x** ở cả bốn phía. Không có chữ, hình hay mép khung nào lọt vào. Thanh điều hướng chật thì tối thiểu 0,5 x. |
| Logo chữ, màn hình | Cao ≥ **20px** (khoảng 72px ngang), tính chiều cao toàn logo. Ở 16px vẫn đọc được (đã thử trong sheet) nhưng chỉ dùng khi bắt buộc. |
| Logo chữ, bản in | Cao ≥ **6 mm** (khoảng 22 mm ngang) |
| Ký hiệu `invlogis-symbol.svg` | Cao ≥ **48px** / 8 mm. Nhỏ hơn thì dùng bản favicon (thân dày hơn, vẽ khớp lưới điểm ảnh). |
| Lockup "by innvie" | Logo chính cao ≥ **48px** / 12 mm, để chữ "innvie" không nhỏ quá 6px x |
| Lockup có khẩu hiệu | Logo chính cao ≥ **64px** / 16 mm |

## 3. Dùng biến thể nào, khi nào

| File | Khi nào dùng |
|---|---|
| `invlogis-primary.svg` | Mặc định trên nền sáng: giấy ấm `#FAF8F4`, trắng, xanh khói `#E6EAF8` |
| `invlogis-reverse.svg` | Nền tối: chàm đêm `#0B1033`, mực chàm `#0E1442`, chàm đậm `#17206F`, và vùng tối của gradient chiến dịch |
| `invlogis-mono-black.svg` | In một màu, fax, đóng dấu, khắc. Dùng khi không in được màu. |
| `invlogis-mono-white.svg` | Trên nền cobalt `#2F43DB`, trên ảnh tối hoặc vùng gradient sáng (chỗ mà gradient của chữ i bị chìm) |
| `invlogis-symbol.svg` / `-reverse` / `-mono` | Ảnh đại diện mạng xã hội, hình chìm, điểm nhấn trong slide. Dùng khi chữ "invlogis" đã xuất hiện gần đó. |
| `invlogis-stacked.svg` | Khung vuông hoặc dọc: splash, bìa dọc, gian hàng. Chữ i trong tên tô màu mực để không lặp lụa hai lần. |
| `invlogis-by-innvie.svg` (+ `-reverse`) | Chân trang web, trang cuối deck, hợp đồng, báo giá, hoá đơn |
| `invlogis-tagline.svg` / `-tagline-en.svg` | Bìa deck, landing page, banner ra mắt. Khẩu hiệu: "Khai mở cách vận hành mới." / "Open a new way to operate." |
| `innvie-logo.svg` / `-mono` | Chỉ dùng cho pháp nhân: chữ ký, con dấu số, giấy tờ pháp lý |
| `favicon.svg` | Favicon chính. Tự đổi sang tông periwinkle khi trình duyệt ở chế độ tối. |
| `favicon-16/32/48.png` | Favicon dự phòng. Màu đặc được chọn để đạt ≥ 3:1 trên tab sáng và tab tối. |
| `apple-touch-icon-180.png`, `app-icon-1024.png` | Icon iOS / web app, phương án B "Lụa vắt" (`app-icon-options.png`). Chữ i lớn, lệch phải, thân là dải lụa vắt cong ra khỏi khung, nền lụa cobalt. Nền đầy, không trong suốt, hệ điều hành tự bo góc. |
| `android-foreground-432.png` + `android-background-432.png` | Adaptive icon, phương án B. Chấm i và đầu thân nằm trong vòng an toàn 66dp. Dải lụa cố ý vắt ra ngoài vùng 72dp, bị mặt nạ cắt cũng không sao. |

## 4. Cách đặt innvie

- Invlogis luôn đứng trước, innvie chỉ là chữ ký pháp nhân (brief Mục 2).
- Trong lockup, "by innvie" cao bằng 30% logo chính, căn phải theo chữ s, đặt dưới đuôi g một khoảng 0,1 x. Chữ "by" màu xám chàm `#4A5380`, chữ "innvie" màu mực, chấm i đầu màu cobalt.
- Khi innvie đứng riêng trên cùng một mặt với Invlogis (chân hợp đồng, slide cuối), logo innvie cao không quá **50%** logo Invlogis và đặt xa Invlogis.
- innvie dùng cùng hệ: Lexend 340, chữ i đầu có hình lụa nhưng không gradient. Không tạo ký hiệu riêng cho innvie.
- Splash hiện ghi "Được phát triển bởi innvie" (DEC-037). Lockup "by innvie" chỉ là đề xuất thay thế, founder duyệt rồi mới đổi.

## 5. Cấm

1. Kéo méo, nén, nghiêng, xoay, đổi khoảng cách giữa các chữ, gõ lại logo bằng font.
2. Đổi màu ngoài bảng (mực chàm, cobalt, gradient i đã định, trắng, đen), hoặc tô gradient chiến dịch (tím, hồng, san hô) lên chữ.
3. Thêm hiệu ứng: đổ bóng, viền, phát sáng, 3D, kính mờ lên chính logo.
4. Đặt logo lên nền làm mất tương phản: chữ mực trên nền tối, logo màu trên vùng periwinkle/hồng/san hô của gradient, ảnh rối. Gặp những trường hợp đó thì dùng `mono-white`, hoặc đặt logo trên thẻ nền giấy/kính đậm.
5. Đặt hai chữ i lụa cạnh nhau (bản màu cạnh bản đơn sắc, ký hiệu cạnh logo chữ). Hai chữ i liền nhau thành "hai vạch dọc", brief đã cấm.
6. Thêm hình lụa (vết cắt, nếp gấp, dải vắt) vào chữ v hoặc chữ i thứ hai. Chữ v chỉ có gradient dọc đã định ở Mục 1, không thêm chi tiết khác.
7. Đặt chữ i nhỏ ở giữa một hình tròn hoặc ô trơn (kiểu icon app phương án A/C cũ), vì dễ bị đọc thành biểu tượng "thông tin" ⓘ. Icon app luôn dùng phương án B. Favicon không có khung nên rủi ro thấp; khi bị đặt vào vòng tròn trắng (kết quả tìm kiếm Google) vẫn hơi giống ⓘ, cần theo dõi.

## 6. Tương phản (`_tools/contrast.py`)

Logo là đồ hoạ nên ngưỡng là 3:1 (WCAG 1.4.11). Phần chữ mực đạt cả ngưỡng 4.5:1 dành cho chữ thường.

| Phần / nền | Tỉ lệ | |
|---|---|---|
| Chữ mực `#0E1442` / giấy `#FAF8F4` | 16.53 | đạt |
| Chữ mực / xanh khói `#E6EAF8` | 14.61 | đạt |
| Chấm i, điểm sáng nhất `#5A6CF0` / giấy | 4.09 | đạt (≥ 3) |
| Chấm i `#5A6CF0` / xanh khói | 3.61 | đạt (≥ 3) |
| Thân i `#3A4EE3` / giấy · / xanh khói | 5.86 · 5.18 | đạt |
| Chữ trắng / chàm đêm `#0B1033` · / chàm đậm `#17206F` | 18.48 · 14.26 | đạt |
| Thân i tối, điểm tối nhất `#5B6EF5` / chàm đêm · / chàm đậm | 4.40 · 3.39 | đạt (≥ 3) |
| Chấm i tối `#D6DCFF` / chàm đêm | 13.68 | đạt |
| Đáy chữ v `#2F43DB` / giấy · / xanh khói | 6.72 · 5.94 | đạt |
| Đáy chữ v tối `#A3B0FF` / chàm đêm · / chàm đậm | 8.99 · 6.93 | đạt |
| Mono trắng / cobalt `#2F43DB` | 7.13 | đạt |
| Favicon PNG thân `#4F62EE` / tab sáng · / tab tối `#202124` | 4.59 · 3.31 | đạt (≥ 3) |
| Favicon PNG chấm `#6577F2` / tab sáng · / tab tối | 3.62 · 4.20 | đạt (≥ 3) |
| Khẩu hiệu `#4A5380` / giấy | 6.97 | đạt (AA chữ thường) |

## 7. Dựng lại

```bash
cd design/brand/_drafts/logo-final
python3 _src/build.py      # SVG logo + favicon
python3 _src/icons.py      # 3 phương án icon app (B là bản chính) → render icon-b.svg, android-fg-b.svg, android-bg-b.svg
python3 _src/iconboard.py && python3 ../_tools/render.py _src/app-icon-options.html app-icon-options.png --size 1600x1000
python3 _src/vopt.py && python3 ../_tools/render.py _src/v-options.html v-options.png --size 1600x900
python3 _src/sheet.py && python3 ../_tools/render.py _src/logo-sheet.html logo-sheet.png --size 1600x2000
```

Font gốc: `_src/LexendVF.ttf` (Lexend có trục độ đậm, OFL, lấy từ google/fonts) và `_src/BeVietnamPro-400/500.ttf` (OFL). Cả hai đủ dấu tiếng Việt (`vn_glyphs.py`).
