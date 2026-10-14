---
type: brand-type
direction: c-hoi-tu
status: draft
updated: 2026-10-14
---

# Hướng C · Hội tụ — chữ

| Vai trò | Font (Google Fonts, OFL) | Độ đậm | Dùng cho |
|---|---|---|---|
| Wordmark, tiêu đề lớn | **Lexend** | 600 (logo), 300 + 600 xen kẽ (tiêu đề) | Chữ không chân hình học, mở rộng, đậm hơn hướng A |
| Thân bài | Lexend | 300–400 | Đoạn văn, phụ đề |
| Nhãn chứng từ | **Geist Mono** | 400 | `[Booking Note]`, `[ ĐÃ ĐỌC ]`, địa chỉ web, chân trang |

Lý do: Lexend có hình học tròn, chữ "o/g/s" mở, đủ dấu Việt, đọc dễ; cặp 300/600 cho kiểu tiêu đề "nhẹ rồi đậm" (một cụm in đậm làm trọng tâm). Geist Mono làm nhãn ngoặc vuông kiểu nhãn chứng từ, thay cho họ pixel (đã bỏ theo brief).

## Cỡ mẫu (deck 1920×1080)

| Cấp | Cỡ | Đậm | Giãn |
|---|---|---|---|
| Tiêu đề bìa | 108px / dòng 1.06 | 300 + 600 | −0.035em |
| Phụ đề | 30px / dòng 1.5 | 300 | 0 |
| Nhãn mono | 20–22px | 400 | +0.04em, HOA |
| Chip chứng từ | 20px | 400 | 0 |

Mạng xã hội 1080×1350: tiêu đề 104px; điện thoại 390×844: nhãn 11px, chân trang 13px.

## Kiểm dấu tiếng Việt (vn_glyphs.py)

```
ĐỦ · Lexend-300.ttf
ĐỦ · Lexend-400.ttf
ĐỦ · Lexend-600.ttf
ĐỦ · GeistMono-400.ttf
```

Bàn giao logo: chữ "invlogis" đã đổi sang nét vector (HarfBuzz, kerning giữ nguyên), chữ "v" vẽ tay thay glyph; SVG không phụ thuộc font.
