# Spec: trích xuất design system Untitled UI (v8.0) làm tài liệu tham chiếu

> Người nhận: một AI agent có trình duyệt (Chrome điều khiển được) và shell (`gh`, `curl`).
> Mục đích cuối: đội Invlogis so sánh Foundations của Untitled UI với DS v2 của mình
> (`design/v2/foundations.md`, `design/v2/tokens.json`) rồi chọn phần nên học. **Bạn chỉ lo bước trích
> xuất.** Báo cáo so sánh do phiên khác làm sau, dựa trên output của bạn.

## 1. Nguồn

| # | Nguồn | Truy cập | Vai trò |
|---|---|---|---|
| S1 | Figma `❖ PREVIEW ❖ Untitled UI Figma – PRO VARIABLES (v8.0)`, fileKey `QERVV4a2Fpa1FmsZ5LGW3S`, https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/?node-id=1023-36350 | Chỉ xem trên trình duyệt (tài khoản user đang đăng nhập) | **Nguồn chính**: cấu trúc biến, mô tả cách dùng, style, ghi chú |
| S2 | Repo `untitleduico/react`: `styles/theme.css` (834 dòng), `styles/typography.css`, `styles/globals.css`, `.storybook/colors.css` | `gh api repos/untitleduico/react/contents/styles/theme.css -H 'Accept: application/vnd.github.raw'` | Giá trị token máy đọc được, cả Light và Dark (`.dark-mode`) |
| S3 | Tài liệu web: https://www.untitledui.com/react/docs/ gồm `introduction`, `theming`, `dark-mode`, `typography`, `icons`, `installation`, `cli`, `rtl`, `upgrade` | `curl` / WebFetch | Luật dùng ở dạng chữ (khá ít) |

S1 và S2 lệch nhau thì **ghi cả hai, đánh dấu lệch**, không tự chọn. Figma v8 là bản thiết kế, repo React có
thể chậm hoặc nhanh hơn một nhịp.

## 2. Giới hạn đã kiểm (đừng thử lại)

- **Figma MCP chính thức** (`create_session`, `get_metadata`, `get_variable_defs`…) báo *"you don't have edit access"*:
  cần quyền sửa, kể cả khi chỉ đọc.
- **Không duplicate được, không xin đổi quyền được** (user đã xác nhận). Export bị tắt ("Someone with edit access… disabled
  exporting, copying, and sharing"). **Không bấm "Ask to edit"**, không comment lên file.
- Plugin Reqwise / plugin Figma bất kỳ: không chạy được trên file chỉ xem.
- Trong trang Figma **không có biến global `figma`**. Canvas vẽ bằng WebGL nên chữ trên canvas không có trong DOM.
- Chạy JS trả về chuỗi có query string hoặc cookie sẽ bị chặn (`[BLOCKED: Cookie/query string data]`). Cắt chuỗi
  trước khi trả về, bỏ phần URL.

## 3. Cách đọc S1 đã chạy được

1. **Panel phải (DOM)**: bấm vào vùng trống của canvas → panel Properties liệt kê *Text styles, Color styles, Effect styles,
   Layout guide styles* của cả file. Đọc bằng JS: `document.body.innerText`, cắt từ `lastIndexOf('Text styles')`. Mở thư mục
   bằng nút "Toggle folder" (dùng `find` để lấy ref), rồi đọc lại. Đây là cách **rẻ và chính xác nhất**. Ưu tiên lấy tên
   style, cỡ chữ/dòng, giá trị bóng ở đây.
2. **Chọn layer → zoom vừa khối**: panel Layers → bấm tên frame hoặc section con → `shift+2`. Panel phải hiện kích thước
   và layout của node đang chọn (DOM, đọc được).
3. **Đọc chữ trên canvas**: dùng `computer.zoom` với vùng nhỏ. Ở mức zoom canvas khoảng 20%, vùng 500×390 px màn hình vẫn
   đọc rõ chữ 12px. Frame quá cao thì chọn section con (bước 2) thay vì cuộn.
4. **Tránh**: cuộn chuột (chỉ khoảng 10px mỗi nấc), kéo bằng tool tay (nhảy, khó kiểm soát). Ẩn/hiện UI bằng `cmd+\`.
   Đóng banner "You can only view" trước khi làm.

## 4. Phạm vi

### Đợt 1: Foundations (bắt buộc)

Các trang trong nhóm `❖ FOUNDATIONS`, cộng `❖ Getting started` và `❖ Variables`:

| Trang | Cần lấy |
|---|---|
| Getting started | Cấu trúc file, quy ước đặt tên, cách tổ chức trang, hướng dẫn đổi màu brand |
| Variables | Danh sách collection, số biến, chế độ (mode) của từng collection. Đã thấy: `_Primitives`, `1. Color modes`, `2. Radius`, `3. Spacing`, `4. Widths`, `5. Containers`, `6. Typography` |
| Colors | Frame `Colors` (bảng gốc), `Gradients`, `Color variables` (4 section: Text, Border, Foreground, Background), `Color utility variables` (Alpha + Utility), `Notes and documentation` (cao 19.216px) |
| Typography | Text style (Display 2xl…xs, Text xl…xs × Regular/Medium/Semibold/Bold), font, letter-spacing, ghi chú dùng |
| Logos, Icons, Misc icons | Bộ icon (tên thư viện, cỡ, nét, cách đặt tên, số lượng), luật dùng; logo chỉ cần ghi cấu trúc |
| Effect styles | Shadows, Focus rings, Backdrop blurs: tên, giá trị từng lớp bóng, dùng cho gì |
| Spacing, radius & grids | Thang spacing, radius, width, container; grid desktop/tablet/mobile (cột, rãnh, lề, breakpoint) |

### Đợt 2: Base components (chỉ khi user bảo làm tiếp)

Avatars, Badges, Button groups, Buttons, Checkboxes, Dropdowns, Inputs, Progress indicators, Radio groups, Select, Sliders,
Tags, Text editors, Toggles, Tooltips. Với mỗi component: thuộc tính và biến thể, cỡ, trạng thái, token đang gắn.
Không làm Shared assets và Application examples.

## 5. Output

Ghi vào `design/_ref/untitled-ui/` (tạo mới; **không đụng** `design/v2/`, `design/design.md`, `.claude/`):

```
design/_ref/untitled-ui/
├── README.md                 nguồn, ngày đọc, phạm vi đã phủ, bảng độ phủ (mục 6)
├── 00-structure.md           trang, collection, mode, quy ước đặt tên
├── 01-colors-primitives.md   các dải màu × bậc, hex, nhãn tương phản trên ô
├── 02-colors-semantic.md     text / border / fg / bg / alpha / utility / component colors
├── 03-typography.md
├── 04-spacing-radius-grid.md
├── 05-effects.md             shadow, focus ring, backdrop blur
├── 06-icons.md
├── tokens.untitled.json      máy đọc được, sơ đồ ở dưới
└── shots/                    ảnh chụp tham chiếu (*.png), đặt tên theo trang-khối
```

**Bảng token** (mọi file 01–05) có cột cố định:

| Token | Light | Dark | Cách dùng (tóm tắt) | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `text-secondary` | neutral-700 | neutral-300 | Chữ phụ: nhãn, tiêu đề mục | S1 · S2 | |

- **Light/Dark** ghi alias (`neutral-700`), không ghi hex. Hex chỉ có trong `01-colors-primitives.md`.
- **Cách dùng**: viết lại ngắn bằng lời của bạn (≤ 25 từ), giữ tên component được nhắc tới (vd "input field", "featured
  icons"). Không chép nguyên văn các đoạn dài.
- **Nguồn**: `S1` / `S2` / `S3`, có thể kèm node-id. Lệch giữa S1 và S2 → cột Ghi chú `⚠ lệch: S1=…, S2=…`.
- Không đọc được (mờ, bị che) → `?` + lý do. **Không đoán giá trị.**

`tokens.untitled.json`:

```json
{ "source": {"figma": "QERVV4a2Fpa1FmsZ5LGW3S", "repo": "untitleduico/react@<sha>", "read_at": "YYYY-MM-DD"},
  "collections": [{ "name": "1. Color modes", "modes": ["Light","Dark"],
    "variables": [{ "name": "Colors/Text/text-secondary (700)", "type": "color",
      "values": {"Light": "{neutral.700}", "Dark": "{neutral.300}"}, "usage": "…", "src": ["S1","S2"] }] }] }
```

Đầu mỗi file .md thêm frontmatter: `type: design-reference`, `status: draft`, `updated: <ngày>`, `links: [nguồn]`.

## 6. Kiểm trước khi bàn giao

1. **Độ phủ**: README có bảng `Trang | Khối | Số dòng token đã lấy | Số dòng thấy trên Figma | Đủ?`. Số trên Figma đếm từ
   panel (vd collection `_Primitives` ghi số biến) hoặc đếm hàng trong ảnh chụp.
2. **Đối chiếu S1↔S2**: so mọi token màu nghĩa ở cả hai chế độ, liệt kê chỗ lệch.
3. **Mẫu ngẫu nhiên**: chọn 10 token, mở lại Figma đọc lại, ghi kết quả vào README.
4. Bóng: đủ từng lớp (x, y, blur, spread, màu, độ mờ). Chữ: cỡ / dòng / độ đậm / letter-spacing.
5. Liệt kê **luật dùng** tìm thấy (vd "border-secondary là viền mặc định của phần lớn component"; "placeholder dùng
   neutral-500 vì tương phản tốt hơn 400") trong mục `## Luật dùng` của từng file. Đây là phần đội cần nhất.

## 7. Những gì đã có sẵn (để kiểm, khỏi đọc lại từ đầu)

- Bảng gốc v8 **lấy theo Tailwind CSS v4.1** (ghi trên frame Colors). Có *Base* (white, black, transparent), *Brand*
  (= primary, mặc định tím, 50–950), 17 sắc (red…rose), 8 dải xám (Slate, Gray, Zinc, Neutral, Stone, Taupe, Mauve, Mist,
  Olive; Neutral là xám mặc định). Mỗi ô ghi nhãn WCAG (vd `AAA 21.00`, `AA 4.83`).
- Màu nghĩa theo nhóm `text-*`, `border-*`, `fg-*`, `bg-*`, hậu tố `_hover`, `_alt`, `_on-brand`, `_subtle`, `-solid`.
  Đã đọc xong bảng Text và Border, phần lớn Foreground và Background (cần đọc lại cho đủ bằng cách ở mục 3).
- Text styles: Display 2xl 72/90, xl 60/72, lg 48/60, md 36/44, sm, xs; Text xl, lg, md, sm, xs; mỗi cỡ có 4 độ đậm.
  Theo repo: font Inter cho cả body và display; tracking âm từ display-md (−0,72px) tới 2xl (−1,44px).
- Effect styles có 3 nhóm: Shadows, Focus rings, Backdrop blurs. Repo: `shadow-xs…3xl`, `shadow-skeuomorphic`, `focus-ring`
  = brand-500, `focus-ring-error` = red-500.
- Layout guide: Grid desktop, tablet, mobile; 12 / 6 / 5 / 3 / 2 cột (auto). Repo: container 1280, breakpoint xxs 320, xs 600.

## 8. Không làm

- Không sửa file của Invlogis ngoài `design/_ref/untitled-ui/`. Không commit.
- Không thao tác lên file Figma (comment, ask to edit, đổi gì).
- Không viết so sánh hay đề xuất. Chỉ trích xuất trung thực, có nguồn.

Báo cáo khi xong: danh sách file, bảng độ phủ, số chỗ lệch S1↔S2, các khối không đọc được.
