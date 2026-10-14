# Hướng B · Chứng từ — chữ

## Cặp font (cả hai Google Fonts, OFL, có tiếng Việt)

| Vai trò | Font | Độ đậm | Dùng cho |
|---|---|---|---|
| Chữ logo, tiêu đề, nội dung | **Manrope** | 500 (logo, tiêu đề), 600 (tiêu đề thẻ), 400 (đoạn văn) | chữ không chân, chính xác, hơi hình học |
| Nhãn chứng từ, mã, số liệu nhỏ | **JetBrains Mono** | 500 | `[eDO]` `[EIR]` `[Booking Note]`, mã chứng từ, ghi chú kỹ thuật |

Chữ "Invlogis" viết hoa chữ đầu, Manrope 500, tracking −10 (thousandths em), đã chuyển thành nét vector trong SVG (không phụ thuộc font). File: `_drafts/fonts/Manrope-{400,500,600}.ttf`, `JetBrainsMono-500.ttf`.

## Kiểm dấu tiếng Việt (`_tools/vn_glyphs.py`)

```
ĐỦ · Manrope-400.ttf
ĐỦ · Manrope-500.ttf
ĐỦ · Manrope-600.ttf
ĐỦ · JetBrainsMono-500.ttf
```

Đã dựng thật các câu có dấu (ắ ằ ẳ ẵ ặ ế ề ể ễ ệ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ứ ừ ử ữ ự đ) trong 3 ứng dụng mẫu: kết quả hiển thị đúng, dấu xếp chồng không đè lên nhau ở cỡ lớn.

## Cỡ mẫu

| Dịp | Mẫu |
|---|---|
| Tiêu đề bìa deck (1920) | Manrope 500 · 88px · dòng 1,06 · tracking −0,025em |
| Tiêu đề bài mạng xã hội (1080) | Manrope 500 · 104px · dòng 1,02 · tracking −0,03em |
| Đoạn dẫn | Manrope 400 · 27–30px · dòng 1,45–1,5 · xám chàm |
| Tiêu đề thẻ chứng từ | Manrope 600 · 17px |
| Nhãn, mã, chip | JetBrains Mono 500 · 10–16px · tracking +0,02em · chữ hoa cho khoá trường |
| Splash (390) | Manrope 500 · 40px (tên), JetBrains Mono 11px (nhãn) |

Quy tắc: tiêu đề mảnh, thoáng, tracking âm nhẹ (đừng quá −0,03em vì dấu tiếng Việt dễ dính chữ), chữ nhấn bằng màu cobalt thay vì đậm hơn; chi tiết kỹ thuật luôn đặt trong ngoặc vuông bằng chữ mono.
