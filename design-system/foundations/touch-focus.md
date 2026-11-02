---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Vùng chạm và focus

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (9.x) để các DEC và spec trích "foundations mục 9…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 9. Vùng chạm và focus (DEC-97, DEC-138, DEC-139, DEC-241)

- **App:** vùng chạm tối thiểu 44×44 cho mọi app (ưu tiên iOS). Nút nhìn: 52 ở chân màn, 42 cho nút nhỏ và nút icon;
  phần thiếu là vùng bấm vô hình quanh nút. Hai nút icon cạnh nhau cách nhau đủ để vùng bấm không chồng
  (ghi chú câu 10, trang phỏng vấn).
  Lưu ý: dưới mức 48dp Android khuyên.
- **Web:** đích bấm tối thiểu 24×24 (WCAG 2.2 AA, mục 2.5.8).
- **Focus:** vòng 2px, cách mép 2px, màu `color/focus/ring` (than chì) cho mọi khách, không theo dải màu khách
  (DEC-170). Nút Danger: vòng focus màu danger (`color/focus/ring_error`, DEC-198, DEC-318). Ô nhập
  đang gõ: viền 2px cùng màu than chì.
- **Khe focus (DEC-327, thay phần khe của DEC-241, DEC-258):** web dùng `outline` 2px, `outline-offset` 2px, khe trong suốt nên đúng trên
  mọi nền (nền phụ, dòng chọn, cảnh báo), không có token khe. Trên Figma khung vòng `.focus / Ring` không tô nền. Không dùng `box-shadow`
  để vẽ vòng; không thêm style focus-ring gộp bóng của Untitled, vòng là lớp riêng nên bóng thẻ giữ nguyên.

