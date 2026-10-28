---
type: design-review
status: draft
updated: 2026-10-27
links:
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/v2/icons.md
  - design/_ref/untitled-ui/README.md
  - design/v2/_review/agent-brief-base.md
---

# Giao việc agent dựng trang Foundations trên Figma (DS v2 theo Untitled UI)

> User yêu cầu 27/10: dựng lại Foundations trên Figma, chia như Untitled UI — Colors, Typography, Logos, Icons,
> Misc icons, Effect styles, Spacing, radius & grids — theo bản DS v2 hiện tại (DEC-260: giữ nền tảng v2, xám neutral Untitled).

## 1. Nơi vẽ

- File `[innvie] invlogis v0.3`. Mỗi mục một trang đã tạo sẵn dưới `❖ FOUNDATIONS`: `↳ Colors` (6681:222301),
  `↳ Typography` (6681:222302), `↳ Logos` (6681:222303), `↳ Icons` (6681:222304), `↳ Misc icons` (6681:222305),
  `↳ Effect styles` (6681:222306), `↳ Spacing, radius & grids` (6681:222307). Chỉ vẽ trên trang được giao.
- Reqwise `figma_write` (`file: "invlogis v0.3"`, `page: "<tên trang>"`), **sessionId riêng** theo tên agent.
  Đọc `figma_docs(section="api", level="cheat")` + `figma_docs(section="recipes")` trước. Figma chậm: batch ≤ 20.
- Trang cũ `DS · Foundations` (5938:221) và `DS · Icons` (5961:221) là **nguồn tham khảo**: đọc, chụp, sao chép cách
  làm; KHÔNG xoá, KHÔNG sửa (trừ agent Icons được giao chuyển component).

## 2. Khuôn trang (giống Untitled)

- Đầu trang: khung `Design system header` rộng 1440: dòng nhỏ `Foundations → <Tên mục>`, tiêu đề lớn tên mục
  (Cal Sans, `type/display`), 1–2 câu mô tả tiếng Việt. Dựng component `_Design system header` một lần ở trang
  `↳ Colors` (agent Colors làm), các trang khác dùng instance của nó (chờ nếu chưa có, hoặc dựng khối tạm rồi ghi lại).
- Thân trang: các khối nội dung rộng 1440, xếp dọc, mỗi khối có tiêu đề (`type/title-2`) + mô tả 1 câu.
- **Web và Mobile hai khối riêng** khi giá trị khác theo `Platform`; **Light và Dark** hai cột khi giá trị khác theo mode.
- Mọi màu, số đo, chữ trong mẫu **gắn biến/style thật** (gắn bằng VariableID, không gắn biến tên `zz-old/…`; màu bằng
  `applyVariable`). Nhãn mẫu ghi **tên token** (vd `color/text/secondary`) + giá trị (hex, px) + tương phản khi là màu chữ/nền.
- Chữ trên trang tiếng Việt, tên token giữ nguyên. Không viết khung "Notes and documentation" lúc này (viết sau cùng).

## 3. Nguồn sự thật

- `design/v2/tokens.json` (máy, thắng khi lệch) + `design/v2/foundations.md` (luật) + `_workspace/decisions.md` (DEC).
- Mẫu Untitled để học bố cục: `design/_ref/untitled-ui/0*-*.md` (mỗi file mô tả trang Foundations tương ứng của Untitled).

## 4. Kiểm và báo cáo

- `layoutAudit` mọi khối; `a11y_audit` cho khối có chữ; một screenshot trang cuối.
- Báo cáo ≤ 250 từ: node id các khối, số mẫu đã dựng, token thiếu/lệch giữa `tokens.json` và biến Figma, câu hỏi cho user.
