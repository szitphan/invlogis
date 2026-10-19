---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Button

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Button` (6373:491, trang L1 · Base), khung
> tài liệu 6379:525 (hình nên / không nên, cấu tạo phóng 2×) · DEC-172…177, DEC-192, DEC-197…199

## Khi dùng

- **Primary:** hành động chính của một vùng (Lưu, Gửi duyệt, Xác nhận). Mỗi vùng chỉ một nút Primary.
- **Secondary:** hành động phụ đi cùng nút chính (Huỷ, Quay lại), nút trong thẻ, sheet.
- **Ghost:** hành động ít nhấn mạnh: thanh công cụ, đầu màn, hàng bảng; nút icon ở đầu màn.
- **Danger:** hành động phá huỷ (Xoá, Huỷ lệnh). Không bao giờ là nút chính của vùng; thường mở hộp xác nhận.
- **Outline:** nút phụ đặt trên nền xám, nơi Secondary chìm vào nền.
- **Content:** Label là mặc định. Leading Icon khi icon giúp nhận ra nhanh (Thêm, Tải xuống). Icon Only khi chỗ chật và icon
  quen thuộc; luôn có tên cho trình đọc màn hình và tooltip trên web.
- **Size:** app LG 52 cho nút chân màn, MD 42 cho nút trong thẻ, sheet và nút icon, SM 36 cho nút nhỏ. Web MD 32 mặc định,
  SM 28 trong hàng bảng, LG 40 ở màn đăng nhập và nút cần nổi (DEC-173).
- **Thứ tự** (DEC-088): chân dialog `[Phụ][Chính]` canh phải; hàng nút form trong trang `[Chính][Phụ]` canh trái.

## Nên và không nên

Hình minh hoạ ở khung tài liệu cạnh component trên Figma.

1. **Nên:** một Primary kèm một Secondary trong vùng. **Không nên:** hai Primary cạnh nhau.
2. **Nên:** Danger nền đỏ nhạt cho Xoá, đặt tách khỏi nút chính, bấm thì mở xác nhận. **Không nên:** Danger đứng ở chỗ nút
   chính hoặc nền đỏ đặc.

## Trạng thái

Default · Hover (chỉ web) · Pressed · Focus (vòng 2 cách 2; Danger màu đỏ, DEC-198) · Disabled (một kiểu xám, không làm mờ,
DEC-174) · Loading (vòng quay + "Đang lưu…", giữ nguyên cỡ nút, bấm thêm không làm gì). Không khoá nút gửi form: bấm khi
thiếu dữ liệu thì báo lỗi ngay tại ô (DEC-177).

## Chữ trên nút

Động từ ngắn 1–3 từ, viết hoa chữ đầu ("Lưu", "Gửi duyệt", "Xoá lệnh"). Tránh "OK", "Đồng ý" khi nói rõ được hành động.
Không viết hoa toàn bộ. Khi đang tải: "Đang lưu…", "Đang gửi…".

## Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | Kết quả |
|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | Primary 15,13 · Secondary 16,09 · Ghost 17,73 · Outline 17,73 · Danger 5,76 (rê 5,11) — **Danger lúc bấm 4,27 ✗** |
| 1.4.3 ngoại lệ | Disabled 2,34: được miễn (control không hoạt động) |
| 1.4.11 Tương phản ngoài chữ (AA) | Viền Outline 1,47, nền Secondary trên trắng 1,10: đạt vì chữ đủ để nhận ra nút. Vòng focus 15,13 (Danger 6,57) ✓ |
| 2.4.7 Focus thấy được (AA) · 2.4.13 Hình dạng focus (AAA) | ✓ vòng 2px, tương phản ≥ 3:1 |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ web SM 28, app ≥ 36 |
| 2.5.5 Kích thước đích (AAA, ≥ 44) | App SM 36, MD 42: code thêm vùng chạm vô hình 44 (foundations mục 9) |
| 4.1.2 Tên, vai trò | Icon Only bắt buộc `aria-label`; Loading đặt `aria-busy`, nhãn "Đang lưu…" để trình đọc báo |
| 2.1.1 Bàn phím | Enter, Space kích hoạt; theo thứ tự Tab |
| 2.3.3 Chuyển động (AAA) | Vòng quay đứng yên khi người dùng bật giảm chuyển động |
| **Điểm** | **8/9 đạt** · cần cải thiện: Danger lúc bấm 4,27 (giữ màu đã duyệt vì trạng thái chỉ thoáng qua, DEC-199) |

## Dùng ở đâu

Màn mẫu Câu 8d (nút chân sheet, nút trong thẻ, nút icon đầu màn); sau này là mọi component L2 có nút.

## Tên trong code

`<Button variant="primary|secondary|ghost|danger|outline" size="sm|md|lg" icon={…} iconOnly loading>`; biến CSS
`--button-*` (màu, `tokens.css` khối Component), `--control-*` (cao, lề), `--radius-control`, `--icon-size-sm`.

## Cấu tạo, thuộc tính, token

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Button` (6373:491) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Lưu | — |
| Loading Label | Chữ | Đang lưu… | — |
| Icon | Đổi component | icon/plus · Size=16 | — |
| Type | Biến thể | Primary | Primary · Secondary · Ghost · Danger · Outline |
| Content | Biến thể | Label | Label · Leading Icon · Icon Only |
| Size | Biến thể | SM | SM · MD · LG |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled · Loading |

225 biến thể · trục Type × Content × Size × State.

### Màu theo phần (token)

| Type | State | Nền | Viền | Chữ | Icon | Vòng focus |
|---|---|---|---|---|---|---|
| Primary | Default | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Hover | `button/bg/primary-hover` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Pressed | `button/bg/primary-pressed` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Focus | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | `color/border/focus · lan 4 + color/bg/surface · lan 2` |
| Primary | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Primary | Loading | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | — |
| Secondary | Default | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Hover | `button/bg/secondary-hover` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Pressed | `button/bg/secondary-pressed` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Focus | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | `color/border/focus · lan 4 + color/bg/surface · lan 2` |
| Secondary | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Secondary | Loading | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Ghost | Default | trong suốt | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Hover | `button/bg/ghost-hover` | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Pressed | `button/bg/ghost-pressed` | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Focus | `color/bg/surface` | — | `button/fg/ghost` | `button/fg/ghost` | `color/border/focus · lan 4 + color/bg/surface · lan 2` |
| Ghost | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Ghost | Loading | trong suốt | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Danger | Default | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Hover | `button/bg/danger-hover` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Pressed | `button/bg/danger-pressed` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Focus | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | `button/focus/danger · lan 4 + color/bg/surface · lan 2` |
| Danger | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Danger | Loading | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | — |
| Outline | Default | trong suốt | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Hover | `button/bg/outline-hover` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Pressed | `button/bg/outline-pressed` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Focus | `color/bg/surface` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | `color/border/focus · lan 4 + color/bg/surface · lan 2` |
| Outline | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Outline | Loading | trong suốt | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |

### Số đo theo phần (token)

| Content | Size | Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo | Cỡ icon |
|---|---|---|---|---|---|---|---|---|
| Label | SM | `control/height/sm` | ôm nội dung | `control/padding-x/sm` | `control/padding-x/sm` | `control/icon-gap` | `radius/control` | — |
| Label | MD | `control/height/md` | ôm nội dung | `control/padding-x/md` | `control/padding-x/md` | `control/icon-gap` | `radius/control` | — |
| Label | LG | `control/height/lg` | ôm nội dung | `control/padding-x/lg` | `control/padding-x/lg` | `control/icon-gap` | `radius/control` | — |
| Leading Icon | SM | `control/height/sm` | ôm nội dung | `control/padding-x-icon/sm` | `control/padding-x/sm` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Leading Icon | MD | `control/height/md` | ôm nội dung | `control/padding-x-icon/md` | `control/padding-x/md` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Leading Icon | LG | `control/height/lg` | ôm nội dung | `control/padding-x-icon/lg` | `control/padding-x/lg` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | SM | `control/height/sm` | `control/height/sm` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | MD | `control/height/md` | `control/height/md` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | LG | `control/height/lg` | `control/height/lg` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label | `type/label` |

<!-- auto:end -->
