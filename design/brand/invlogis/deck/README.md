---
type: brand-deck
status: draft
updated: 2026-10-14
links:
  - design/brand/brand-brief.md
  - design/brand/_drafts/strategy/brand-strategy.md
  - design/brand/invlogis/README.md
---

# Deck bán hàng Invlogis (việc 3.1, Mốc 3) — bản nháp

16 slide 1920x1080, giọng "chúng tôi – bạn". Khách tham chiếu chỉ ghi ẩn danh ("một doanh nghiệp vận tải container khoảng 110.000 lô/năm", DEC-060); số 110.000 không gắn vào AI.

## Có gì

| File | Nội dung |
|---|---|
| `invlogis-sales-deck.html` | Deck trình chiếu: ← → / Space / Home / End, bấm chuột, vuốt, `F` toàn màn hình; mở `#7` nhảy tới slide 7. Phông và ảnh nền dùng đường dẫn tương đối trong `assets/` |
| `invlogis-sales-deck.pptx` | Cùng nội dung, hộp chữ sửa được, nền là ảnh, ghi chú nguồn mỗi slide. Dựng trên layout của `invlogis-template.pptx`: mọi slide dùng layout thật, nhãn mục / tiêu đề / phụ đề / ô số lớn nằm trong placeholder (đổi layout và gõ lại chữ được). Bản đồ: 1 Bìa · 3 Ngăn mục · 2,4,5,8,10,12 Tiêu đề + nội dung · 7,11,13,14 Tiêu đề + nội dung (nền tối) · 6 Sản phẩm trên thiết bị · 9 Số lớn · 15 Trích dẫn · 16 Kết. Phần còn lại (thẻ, ô giữ chỗ vẽ bằng khối, chip, số trang) là hình và hộp chữ tự do, không đổi theo layout |
| `invlogis-sales-deck.pdf` | 16 trang, in từ HTML |
| `invlogis-template.pptx` | Bộ layout: Bìa, Ngăn mục, Tiêu đề + nội dung, Hai cột, Số lớn, Trích dẫn, Sản phẩm trên thiết bị (2 ô chèn ảnh), Kết; kèm 8 slide mẫu giải thích cách dùng |
| `previews/` | `slide-01..16.png` + `contact-sheet.png` |
| `assets/` | Phông (OFL), logo SVG + PNG, nền JPG/PNG đã duyệt Mốc 2 |
| `slides.py` · `lib.py` · `build.py` · `build_template.py` | Nguồn và script dựng |

## Dựng lại

```bash
cd design/brand/_drafts/m3/deck
python3 build.py --render     # HTML + PPTX + kiểm tra + previews + PDF (cần Chrome)
python3 build_template.py     # invlogis-template.pptx
```

Vòng sửa R4a (14/10): dữ liệu mẫu hiển nhiên giả (`MSKU 000000-0`, `VD-0000`, `00/00/0000`, `00.000 kg`) + nhãn "Dữ liệu minh hoạ"; slide 3 vẽ thẻ chứng từ bằng khối thay ảnh nền có số trông thật; slide Hiện trạng theo 4 thẻ Vấn đề của landing page; "ba bước" như web; thêm slide 5 (một lô từ eDO đến công nợ) và 14 (thử trên lô của bạn); nhãn mục = số trang; chuyện tên có "khai mở"; đích dài hạn nói là điều hướng tới; **Cây dầu và Nhân sự bỏ khỏi deck vì còn mở (PRD OQ-13)**, module chỉ còn Điều phối, Phương tiện, App lái xe, Công nợ, Nền dùng chung, Xưởng (gói).

Sửa nội dung ở `slides.py` (toạ độ px trên khung 1920x1080), rồi dựng lại; HTML và PPTX cùng sinh từ một nguồn nên không lệch. `build.py` tự in cảnh báo chữ tràn hộp (đo bằng phông thật) và tương phản chữ trên nền thật (4,5:1; chữ ≥36px 3:1). Lần cuối: 0 cảnh báo, thấp nhất 4,61:1. Mẫu nay có 10 layout (thêm "9 Tiêu đề + nội dung (nền tối)" và "10 Trống"). Nền slide đặt ở cấp slide nên đổi layout vẫn giữ nền; muốn nền của layout thì bấm Reset/Format Background > Reset.

## Quy tắc đã áp

- Nền hằng ngày n1–n6 và `doc-hero-n3`; không dùng nền rực r1–r3 (chỉ ra mắt). Chữ trắng trên n1/n2/n3/n6, chữ mực trên n4/n5 đúng cột `mode` của `_contrast.json`, nên không có chữ rơi vào vùng cấm 56–70% của gradient chiến dịch.
- Màn hình sản phẩm là giao diện vẽ bằng khối theo phong cách thương hiệu, số liệu mẫu (HDMU 7305 2214…, ghi "Dữ liệu minh hoạ"); không ảnh stock, không gọi API ảnh, không tên hay logo khách.
- Chỗ chưa có dữ kiện hiện chữ `[chờ: …]`: liên hệ, pháp nhân, nhận xét khách, số liệu AI đọc, lộ trình, bảo mật, SLA, giá, hình thức demo.

## Lưu ý khi mở PPTX

Máy phải cài Lexend (Light, Regular, SemiBold), Be Vietnam Pro (Light, Regular, Medium, SemiBold), JetBrains Mono: lấy ở `assets/fonts/`. Không cài thì PowerPoint thay phông và chữ có thể tràn. Hiệu ứng làm mờ nền kính (`backdrop-filter`) chỉ có ở HTML/PDF; PPTX dùng nền bán trong suốt.

## Chưa làm được / chưa kiểm

- Chưa mở PPTX trong PowerPoint để so với HTML (máy không có LibreOffice; Quick Look chỉ cho xem slide 1 của mẫu: layout, nền, logo đúng). Cần người mở thử, nhất là xuống dòng.
- Logo trong PPTX là PNG trong suốt (từ SVG gốc); bản vector ở `assets/logo/*.svg`.

## Câu hỏi mở

1. Kênh nhận chứng từ ở slide 4 ("tải lên hoặc chụp trên app"): có nhận PDF/email/eDO trực tiếp không? PRD chỉ nói AI đọc chứng từ khách và lái xe chụp chứng từ.
2. Slide 11 ghi "bạn duyệt hồ sơ trước khi dữ liệu đi tiếp" (theo câu định vị): xác nhận luồng duyệt có thật trong sản phẩm.
3. Cây dầu và Nhân sự: khi OQ-13 chốt thì đưa lại vào slide 7 và 10.
4. Câu chuyện tên Na Uy ("cống hiến và khánh thành", DEC-072): strategy Mục 4 đề nghị người bản ngữ kiểm trước khi in.
5. Khi nào có: nhận xét khách tham chiếu (BL-056), số liệu AI đọc, bảng giá, SLA, tên pháp nhân + MST, email/sđt/website, lộ trình "Tiếp theo".
6. Hình thức CTA ở slide 16 ("mang vài chứng từ thật, xem hồ sơ hiện ra"): demo hay chạy thử, có tính phí không?
7. Slide 9: dùng "~110.000" hay "khoảng 110.000" (hiện dấu ~ để gọn).
