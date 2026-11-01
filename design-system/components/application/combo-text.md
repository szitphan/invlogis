---
type: design-component
status: stale
status_prev: draft
updated: 2026-10-27
links:
  - design-system/foundations/misc-icon.md
  - design-system/components/application/container-slot.md
  - _workspace/decisions.md
---

# Combo Text

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Combo Text` (6801:15783), trang
> DS · Application components, Section `Combo text` 6802:15841, Demo 6802:15849 · DEC-267, DEC-272

Tổ hợp đầu kéo – mooc – container trong **một dòng chữ** (cách C, `design-system/foundations/misc-icon.md` mục 5.4). Một component cho
web và app.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: cột Tổ hợp của danh sách Lệnh web (mặc định; mở rộng dòng thì hiện Combo Slots), nhãn marker bản đồ, dòng
  phụ thẻ Lệnh app.
- Dạng: **`15C-456.78` 2 cầu sau › `15R-203.77` 40ft 3 giàn › `2×20` MSKU 704512 3 (có hàng) + CAIU 558120 9 (có hàng)**.
- Nhãn cấu hình (`Load`: 1×20, 2×20, 1×40, 1×45) **luôn hiện**; chỉ danh sách container (`Boxes`) co và cắt "…".

### Cấu tạo

| Phần | Nội dung | Token |
|---|---|---|
| Dòng | auto-layout ngang, khoảng 4, rộng FILL, cắt nội dung | — |
| `Tractor`, `Trailer` | biển số | `type/label` · `color/text/primary` |
| `Tractor type`, `Trailer type` | loại xe / mooc; tắt bằng Has Types | `type/body` · `color/text/tertiary` |
| Dấu `›` | ngăn đầu kéo · mooc · tải | `type/body` · `color/text/disabled` |
| `Load` | 2×20 · 1×40… | `type/label` · `color/text/primary` |
| `Boxes` | số container + trạng thái vị trí trong ngoặc, nối bằng " + "; FILL, 1 dòng, cắt "…" | `type/code` · `color/text/tertiary` |
| `Note` | "· không kéo mooc" / "không container" | `type/body` · `color/text/disabled` |

### Biến thể

| Config | Khi nào |
|---|---|
| No Trailer | đầu kéo chạy một mình (trường hợp 1) |
| No Container | kéo mooc rỗng (trường hợp 2) |
| One Box | 1×20 / 1×40 / 1×45 |
| Two Boxes | 2×20 (cùng Lệnh hoặc ghép 2 Lệnh — ghi "· LVT-…" trong ngoặc) |

Container chưa có số: `Boxes` = "— (chưa có số)".

### Chữ dài

Chỉ `Boxes` co. Dưới 360 tắt **Has Types** để nhãn `Load` không bị đẩy ra ngoài. Kiểm ở 560, 420, 320.

### Nên và không nên

- Nên: dùng trong ô bảng hẹp; mở chi tiết / mở rộng dòng để xem đủ container.
- Không nên: xuống nhiều dòng (khi cần nhiều dòng dùng Combo Slots); bỏ nhãn cấu hình.

### Trợ năng — chấm theo WCAG 2.2

- Chữ bị cắt "…" phải có bản đủ: tooltip (web) hoặc mở chi tiết. Tên truy cập = toàn văn dòng.

### Thuộc tính

TEXT `Tractor` · `Tractor type` · `Trailer` · `Trailer type` · `Load` · `Boxes` · BOOLEAN `Has Types` · VARIANT `Config`.

### Được dùng trong

Demo `Danh sách lệnh vận tải / Web` (cột Tổ hợp, dòng mở rộng hiện Container Slot Compact), `Lệnh của tôi / Mobile`.

### Kiểm máy

27/10: kiểm tên fail 0. Đã sửa: cắt từng phần làm mất container thứ hai → gộp `Boxes`, thêm `Load` luôn hiện, thêm
Has Types. Dark: chưa điền giá trị Dark.

## Mobile

> Mode Platform = Mobile, cùng component. Rộng thẻ app 343 → tắt Has Types.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
