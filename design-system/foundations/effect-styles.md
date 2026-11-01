---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Lớp nổi, làm mờ nền

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (8.x) để các DEC và spec trích "foundations mục 8…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 8. Lớp nổi (DEC-125, DEC-137, DEC-234)

| Bậc | Viền | Bóng | Dùng cho |
|---|---|---|---|
| `elev/0` | — | không | Ô nhập, khối phụ trong thẻ (phẳng) |
| `elev/1` | `color/border/secondary` | 0 1 2 · `shadow/sm` | Thẻ (DEC-125) |
| `elev/2` | `color/border/secondary` | 0 4 12 · `shadow/md` + 0 1 3 · `shadow/md-soft` | Menu thả, popover, gợi ý ô tìm |
| `elev/3` | — | 0 16 40 · `shadow/lg` + 0 4 12 · `shadow/md` | Dialog, sheet, toast |

Màu bóng là biến Semantic (DEC-258), đổi theo sáng/tối như Untitled UI:

| Biến | Light | Dark |
|---|---|---|
| `color/shadow/sm` | #101828 6% | #000 40% |
| `color/shadow/md` | #101828 10% | #000 50% |
| `color/shadow/md-soft` | #101828 6% | #000 40% |
| `color/shadow/lg` | #101828 16% | #000 60% |

`elev/3` lớp 2 đổi 8% → 10% khi gom về biến `shadow/md`.

- Thẻ mặc định có viền mảnh và bóng rất nhẹ (`elev/1`). Bóng đậm chỉ cho lớp nổi tạm (`elev/2`, `elev/3`).
- `Base / Card` chọn Elevation None · Low · Med · High = không bóng · `elev/1` · `elev/2` · `elev/3`, mặc định Low; thẻ đang
  nhấn (Pressed) và Disabled bỏ bóng (DEC-234).
- Effect style Figma tên `elev/1 · 2 · 3`; viền gắn riêng bằng `color/border/secondary`; màu từng lớp gắn biến `color/shadow/*`.

### 8.1 Làm mờ nền (DEC-258)

| Token | Giá trị | Áp vào |
|---|---|---|
| `blur/sm` | 8 | Đầu màn, thanh công cụ dính trên cùng khi cuộn (nền trắng 70%) |
| `blur/md` | 16 | Thanh điều hướng nổi app (DEC-160), thanh hành động nổi đáy màn (nền trắng 60%) |
| `blur/lg` | 24 | Nền sau dialog, sheet: scrim 35% + blur thay scrim 50% |
| `blur/xl` | 40 | Không dùng trong app nghiệp vụ |

Web: `backdrop-filter: blur(var(--blur-md))`. Flutter: `BackdropFilter(ImageFilter.blur(sigmaX: InvBlur.blurMd, …))`.

