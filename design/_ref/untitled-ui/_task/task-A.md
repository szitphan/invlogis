# Task A — trích xuất Untitled UI từ repo (S2) + docs web (S3)

Spec đầy đủ: design/_ref/untitled-ui/_task/spec.md
ĐỌC HẾT spec trước (đặc biệt mục 5 Output, 6 Kiểm, 8 Không làm).

Thư mục làm việc: /Users/szit/Desktop/szit/AI/Projects/invlogis
Chỉ ghi vào `design/_ref/untitled-ui/`. Không đụng file nào khác. Không commit. Không mở Figma (S1 do phiên khác làm sau).

## Việc của bạn (chỉ S2 + S3)

1. Lấy SHA repo: `gh api repos/untitleduico/react/commits/main --jq .sha`.
2. Tải nguyên văn về `design/_ref/untitled-ui/raw/` (để đối chiếu, không sửa):
   `styles/theme.css`, `styles/typography.css`, `styles/globals.css`, `.storybook/colors.css`
   bằng `gh api repos/untitleduico/react/contents/<path> -H 'Accept: application/vnd.github.raw' > raw/<tên>`.
3. Tải docs S3 (introduction, theming, dark-mode, typography, icons, installation, cli, rtl, upgrade) từ
   https://www.untitledui.com/react/docs/<slug> bằng curl, rút phần chữ (bỏ HTML) vào `raw/docs-<slug>.txt`.
4. Viết các file 00–06 + tokens.untitled.json + README.md đúng khung mục 5 của spec, từ S2/S3:
   - Bảng token cột cố định: Token | Light | Dark | Cách dùng | Nguồn | Ghi chú. Light/Dark ghi alias, hex chỉ ở 01.
   - Dark lấy từ khối `.dark-mode` trong theme.css. Alias: lần theo `var(--color-…)` đến primitive.
   - Mọi dòng điền cột Nguồn = `S2` (hoặc `S3`). Thêm cột/ghi chú `S1: chưa đọc` — KHÔNG bịa giá trị Figma.
   - Mục 7 của spec ghi những gì đã thấy trên Figma — được phép dùng làm S1 nhưng chỉ đúng những gì mục 7 ghi.
   - Cách dùng: lời của bạn ≤25 từ, lấy từ comment trong CSS và docs. Không có thì để trống, không đoán.
   - Mỗi file có mục `## Luật dùng` liệt kê luật tìm thấy trong S2/S3 kèm nguồn.
   - Shadow: đủ từng lớp (x,y,blur,spread,màu,độ mờ). Typography: cỡ/dòng/độ đậm/letter-spacing.
   - Frontmatter mỗi .md: type: design-reference, status: draft, updated: 2026-10-26, links: [...].
   - 06-icons.md: thư viện icon, cỡ, nét, cách đặt tên — từ docs icons.
5. README.md: nguồn + SHA + ngày, bảng độ phủ `Trang | Khối | Số dòng token đã lấy | Số dòng thấy trên Figma | Đủ?`
   (cột Figma để `chưa đọc S1`), đếm số token mỗi nhóm trong theme.css để chứng minh không sót.
6. Kiểm tự động: viết script nhỏ (để ở design/_ref/untitled-ui/_task/)
   so số biến `--color-*` / `--shadow-*` / `--text-*` / `--radius-*` / `--spacing-*` … trong theme.css với số dòng
   trong tokens.untitled.json. Phải khớp; ghi kết quả vào README.

Khi xong in ra: danh sách file, số token mỗi nhóm, kết quả script kiểm, chỗ nào không chắc.
