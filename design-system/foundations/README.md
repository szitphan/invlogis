---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/architecture.md
  - design-system/tokens.json
  - design-system/tokens.css
  - _workspace/decisions.md

---

# Design System — nền tảng (Foundations)

> Kết quả vòng 2/6, chốt 16–17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (DEC-119…139); bổ sung 19/10 từ phần khoảng cách, màu theo khách và vòng 4 (DEC-164…170, DEC-173, DEC-176,
> DEC-179, DEC-192…194, DEC-196); 20/10 nền đặt, thẻ, chip, avatar, dòng danh sách, thanh tiến độ, ô mã (DEC-231…246). File này là **luật dùng**. Giá trị máy đọc nằm ở `design-system/tokens.json`; `tokens.css` sinh ra từ
> json bằng `python3 _scripts/ds-v2-tokens.py`. Bảng trong file này lệch json thì **json thắng**.
> Thư mục này thay file `foundations.md` cũ (DEC-317): mỗi phần một file, giữ số mục cũ. Trên Figma: trang `🎨 DS · Foundations` (collection 0–8 theo mục 2; text style `type/*`; effect style `elev/*`).

## 0. Trạng thái từng mục

Component chỉ coi một mục là chuẩn khi mục đó `approved`; mục chưa duyệt vẫn dùng được nhưng trang review ghi "chưa duyệt".
Đổi bằng `python3 _scripts/ds-foundation-status.py set <mã> <trạng thái>` (dashboard và trang duyệt foundations gọi lệnh này).

<!-- foundation-status -->
| Mã | Mục | Ở đâu | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|---|
| color | Màu | [color.md](color.md) (mục 3) | approved | 2026-11-01 | DEC-316, DEC-320 · tên theo Untitled · DEC-316 · Dark #191919 · 52 token mới · web = mobile |
| type | Chữ | [typography.md](typography.md) (mục 4) | draft | 2026-11-01 |  |
| radius | Bo góc | [radius.md](radius.md) (mục 5) | draft | 2026-10-28 |  |
| space | Khoảng cách | [spacing.md](spacing.md) (mục 6) | draft | 2026-10-28 |  |
| grid | Lưới, độ rộng, breakpoint | [grids.md](grids.md) (mục 7) | draft | 2026-10-28 |  |
| elevation | Lớp nổi, làm mờ nền | [effect-styles.md](effect-styles.md) (mục 8) | draft | 2026-10-28 |  |
| touch-focus | Vùng chạm và focus | [touch-focus.md](touch-focus.md) (mục 9) | draft | 2026-10-28 |  |
| motion | Chuyển động | [motion.md](motion.md) (mục 10) | draft | 2026-10-28 |  |
| icon | Icon | [icon.md](icon.md) (mục 11) | draft | 2026-10-28 |  |
<!-- /foundation-status -->

## Các file

| Mục cũ | File | Mã trạng thái |
|---|---|---|
| 3 | [color.md](color.md) | color |
| 4 | [typography.md](typography.md) | type |
| 5 | [radius.md](radius.md) | radius |
| 6 | [spacing.md](spacing.md) | space |
| 7 | [grids.md](grids.md) | grid |
| 8 | [effect-styles.md](effect-styles.md) | elevation |
| 9 | [touch-focus.md](touch-focus.md) | touch-focus |
| 10 | [motion.md](motion.md) | motion |
| 11 | [icon.md](icon.md) | icon |
| — | [misc-icon.md](misc-icon.md) | — (phương tiện: ảnh, icon, tổ hợp) |
| — | [logo.md](logo.md) | — |

## 1. Nguồn tham chiếu (DEC-128, DEC-129)

| Nền tảng | Nguồn chính | Dùng để |
|---|---|---|
| App iOS, Android | Apple Human Interface Guidelines, Material Design 3 | Thang chữ app, vùng chạm, bo góc, lớp nổi |
| Web | Atlassian Design System (hệ dựng ra Jira, DEC-127) | Thang chữ web, khoảng cách, cao control, bảng |
| Web thích ứng | Material 3 (window size classes) | Cách đổi bố cục theo bề rộng (xét khi làm bản tablet) |
| Trợ năng | WCAG 2.2 | Tương phản, vùng chạm, vòng focus |
| Đối chiếu | Tailwind CSS, Ant Design | Chỉ để so; dev quen thang của Tailwind |

Số của các hệ lấy từ trang gốc ngày 16/10/2026 (bảng nguồn trên trang phỏng vấn).

## 2. Cấu trúc token (DEC-114, DEC-115, DEC-116)

| Tầng | Collection Figma | Chế độ | Ví dụ | Ai được gắn |
|---|---|---|---|---|
| Primitive | `0. Primitives` | Value | `neutral/900`, `space/16`, `radius/md`, `font-size/sm` | Chỉ tầng Semantic trỏ tới; ẩn khỏi bảng chọn |
| Semantic · màu | `1. Semantic` | Light, Dark | `color/text/tertiary`, `color/action/secondary-pressed` | Component, màn |
| Semantic · số đo | `2. Platform · Radius` · `3. Platform · Spacing & Layout` · `5. Platform · Sizes` | Web, Mobile | `radius/card`, `space/xxs`, `layout/screen-inset`, `control/height/md` | Component, màn |
| Semantic · chữ | `4. Platform · Typography` | Value (một bộ, DEC-322) | `type/body/size`, `type/label/line-height` | Text style `type/*` |
| Theo khách | `7. Brand` | 8 dải | `color/brand/800` | Component, màn, theo vai mục 3.5 |
| Component · số đo | `6. Platform · Component sizes` | Web, Mobile | Đang gộp về token chung (DEC-319): còn 59 token chờ đợt 2, sổ `components/_token-ledger.json` | Chính component đó |
| Thương hiệu | `9. Brand · Invlogis` | Value | `invlogis/*`, `innvie/*` (DEC-261) | Logo, trang giới thiệu; không dùng trong component sản phẩm |

- **Primitive màu, khoảng cách (`space/<px>`), bo góc (`radius/<px>`) chỉ để tầng Semantic trỏ tới** (DEC-315). Lớp nổi: style
  `elev/*` là tầng nghĩa, màu bóng qua `color/shadow/*`.
- **Token tầng Component (`6.`, `8.`) chỉ trỏ Semantic (`1.`–`5.`) hoặc Brand theo vai, kể cả số đo** (DEC-313). `8. Component`
  chỉ có một chế độ; trỏ thẳng Primitive thì sang Dark vẫn giữ màu sáng. Chưa có Semantic đúng vai thì thêm Semantic, không
  trỏ tắt. Máy kiểm: `python3 _scripts/ds-token-usage.py --check`. Chi tiết tầng: `architecture.md` mục 7.

- Platform tách 5 collection theo loại số đo, cùng mode Web/Mobile (DEC-257). Figma không lồng collection trong
  collection nên "Platform" chỉ là tiền tố tên; khung màn đặt mode Web hoặc Mobile cho **cả 5** collection. Trong
  `tokens.json` Platform vẫn là một nhóm, bảng chia sang 5 collection ở khoá `figma.collections`.

- Component và màn **không gắn Primitives, không ghi mã màu trần**. Cần màu mới thì thêm token nghĩa.
- Màn đặt chế độ `Platform` một lần ở khung màn (Web hoặc Mobile); chữ, bo góc, khoảng cách bên trong tự đổi.
  Trong code: `data-platform="mobile"` trên khung trang (mặc định là web), `data-theme="dark"` cho chế độ tối.
- **Không dùng nền trang xám nữa (DEC-258)**, cả web và app: nền trang trắng, thẻ trắng có viền `color/border/secondary`.
  Collection Context (DEC-241) đã bỏ; khe focus là token Semantic `color/focus/gap`. `color/bg/secondary` giữ cho khối phụ trong
  thẻ và ô nhập app. `color/bg/primary` trỏ về trắng, chỉ giữ để không gãy tham chiếu cũ.
- Dark: bản nháp theo quy tắc đảo bậc, đã đo và chỉnh, xem mục 3.6 (DEC-257). Brand chưa có giá trị Dark.
- Tên CSS = `--` + tên token thay `/` bằng `-`: `color/bg/primary` → `var(--color-bg-primary)`. Biến Figma có code syntax WEB đúng tên này.

## 12. Luật gắn token khi vẽ và code

1. Fill, viền, chữ gắn biến `Semantic`; bo góc, khoảng cách, lề gắn biến `Platform`. Không mã màu, không số trần.
2. Chữ dùng text style `type/*`; không chỉnh cỡ tay. Cần cỡ không có trong thang thì hỏi, không tự thêm.
3. Khung màn đặt chế độ `Platform` (Web hoặc Mobile) một lần.
4. Thẻ dùng `elev/1` + viền `color/border/secondary`; menu nổi `elev/2`; dialog, sheet, toast `elev/3`.
5. Sửa token: sửa `tokens.json` → chạy script sinh `tokens.css` → cập nhật biến Figma cùng lượt.
6. Khối có hình đặt gần góc khung: chạy máy đo lồng góc (mục 5, DEC-165) trước khi trình màn.
7. Nền trang luôn trắng (`color/bg/primary`), không dùng nền xám (DEC-258).

## 13. Còn mở

- Dark của Brand (quy ước `_alt`); biến Figma chưa điền Dark, chưa bỏ Context (BL-249, BL-252).
- Có bật Corner smoothing (góc liền mạch kiểu iOS) cho thẻ, sheet trên app không.
- Quyền publish thư viện của gói Figma (DEC-110).
- Việc còn mở của icon: `design-system/foundations/icon.md` mục 10.
