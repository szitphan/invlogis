---
type: design-foundations
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/components/base/logo.md
  - design/brand/invlogis/README.md
  - design/brand/invlogis/logo/logo-spec.md
  - design/brand/invlogis/product/touchpoints.md
  - design/brand/delta/logo/logo-spec.md
  - docs/_product/tenant-parameters.md
  - design-system/tokens.json
---

# Foundations · Logo

> Một phần của [[design-system/foundations/README.md|Foundations]], mã trạng thái `logo`, mục 14. Chốt ở DEC-326 trên trang
> review Logo. File này là luật dùng logo trong sản phẩm. Cấu tạo nét, tương phản từng phần, luật in ấn nằm ở bộ nhận diện:
> `design/brand/invlogis/logo/logo-spec.md`, `design/brand/delta/logo/logo-spec.md`. Component: `design-system/components/base/logo.md`.

## 14. Logo

### 14.1 Ba khối của trang Logos

| Khối | Gồm | Ghi chú |
|---|---|---|
| Logo sản phẩm | Invlogis: logo ngang, ký hiệu | Mục 14.2 |
| Logo khách | Logo từng khách, cùng bộ biến thể với Invlogis | Mục 14.4 |
| Đối tác | Chỉ trỏ sang `Bank logo`, `App logo` ở khu Master | Không chép lại ở đây |

Không có khối logo báo chí (Press logos của Untitled): chỉ phục vụ website marketing, sản phẩm không dùng.

### 14.2 Sản phẩm chỉ dùng 2 biến thể

| Biến thể | Nền sáng | Nền tối | Dùng khi |
|---|---|---|---|
| Logo ngang | `invlogis-primary.svg` | `invlogis-reverse.svg` | Mọi chỗ có đủ bề rộng, kể cả splash |
| Ký hiệu | `invlogis-symbol-small.svg` | `invlogis-symbol-small-reverse.svg` | Thanh menu thu gọn, chỗ không đủ rộng |

- Tệp nằm ở `design/brand/invlogis/logo/`. Các tệp còn lại (xếp dọc, đơn sắc, khẩu hiệu, "by innvie") chỉ cho in ấn, deck,
  marketing; component Logo không có chúng.
- **Splash dùng logo ngang**, không dùng xếp dọc. `invlogis-stacked.svg` không có bản nền tối.
- **Ký hiệu dưới 48 dùng bản nhỏ**, tách từ `favicon.svg`: thân dày hơn, khớp lưới điểm ảnh. Trong sản phẩm mọi vị trí ký hiệu
  đều dưới 48, nên component chỉ dùng bản nhỏ. Hai tệp đổi theo chế độ của app, không theo hệ điều hành; `favicon.svg` giữ
  nguyên cho tab trình duyệt. `invlogis-symbol.svg` (từ 48 trở lên) chỉ dùng ngoài sản phẩm.
- Không đặt ký hiệu cạnh logo chữ (`logo-spec.md` Mục 5).

### 14.3 Cỡ và vùng trống

Không có token cỡ logo. Trục Size theo thang `size/*`, cùng số ở Web và Mobile:

| Chỗ dùng | Cao | Token | Trước đây |
|---|---|---|---|
| Đầu menu web | 24 | `size/3xl` | 28, gắn `control/height/sm` |
| Thanh trên mobile web, màn chủ app | 24 | `size/3xl` | chưa có luật |
| Ký hiệu ở menu thu gọn 64 | 24 | `size/3xl` | chưa có luật |
| Đăng nhập | 40 | `size/5xl` | 40 |
| Splash | 64 | `size/7xl` | 72 |

Áp cho cả Invlogis và logo khách:

- **Cao tối thiểu 20.** Vùng trống 1 x; **trong thanh điều hướng tối thiểu 0,5 x**. `x` ≈ 0,52 chiều cao logo: ở cao 24 thì
  1 x = 12,5, 0,5 x = 6,2. Khoảng 8 giữa logo và nút thu gọn của Sidebar đạt 0,5 x.
- **Logo rộng quá thì hạ cao, không dưới 20; không cắt logo.** Đầu menu 240: trừ lề 12 hai bên, nút thu gọn 32 và khoảng 8 còn
  176 cho logo. Delta cao 24 rộng 142, vừa.
- Lockup "by innvie" (≥ 48) và lockup khẩu hiệu (≥ 64) không dùng trong sản phẩm, số giữ ở `logo-spec.md`.

### 14.4 Logo khách (tenant)

Mọi khách cùng cấu trúc và cùng bộ biến thể, chỉ khác tệp: một component Logo, trục `Owner` = Invlogis · Khách. Tầng
`[Lõi] [Cấu hình]`: cơ chế và chỗ đặt là lõi, tệp theo từng khách.

| Tham số | Vai | Thiếu thì |
|---|---|---|
| `P-logo` | Logo ngang trên nền sáng + tên hiển thị | Chữ cái đầu tên khách trên ô `P-mau-logo` |
| `P-logo-nen-toi` | Logo ngang trên nền Tối | Tệp chính đặt trên ô trắng |
| `P-logo-vuong` | Logo vuông bản nền sáng và nền Tối, dùng ở menu thu gọn, thanh trên mobile web | Chữ cái đầu trên ô `P-mau-logo` |
| `P-mau-logo` | Màu ô chữ cái đầu | Mặc định #262626 |
| `P-favicon`, `P-icon-app` | Favicon, icon app | Mục 14.5 |

Giá trị từng khách ở `docs/_product/tenant-parameters.md`. Delta: `design/brand/delta/logo/`.

**Logo khách thay Invlogis ở:** góc menu, đăng nhập, splash app, splash web, màn chủ app, email giao dịch, chứng từ in.

**Đặt trên nền:**

- Logo thật đặt thẳng trên nền, **không tô ô**. `P-mau-logo` chỉ tô ô khi hiện chữ cái đầu, vì chữ đen trên ô xanh Delta chỉ
  3,29:1 và mảng xanh trong logo chìm vào ô; chữ cái trắng trên cùng ô đạt 5,29:1.
- Chế độ Tối dùng `P-logo-nen-toi`. Khách chưa nộp thì đặt tệp chính trên ô trắng cố định, lề `space/sm` (đạt 0,5 x ở cao 24), bo
  `radius/md`. Không tự đảo màu bằng code: mất mảng màu trong logo, đổi nhận diện của khách. Delta chữ đen trên nền Tối #191919
  chỉ 1,01:1 nên bắt buộc dùng `delta-reverse.svg`.

### 14.5 Điểm chạm

| Điểm chạm | Logo | Luật |
|---|---|---|
| Menu web mở rộng | Logo ngang 24 | Có tên đơn vị, chi nhánh theo `sidebar-navigation.md` |
| Menu web thu gọn 64 | Logo vuông 24 | Thiếu `P-logo-vuong` thì chữ cái đầu trên ô; không cắt logo chữ |
| Web trên điện thoại | Ký hiệu 24 | **Mọi màn có logo**, dùng ký hiệu để còn chỗ cho tiêu đề trang |
| App · màn chủ | Logo ngang 24 | Màn chủ, splash, đăng nhập có logo |
| App · màn con | Không logo | Giữ tiêu đề + quay lại |
| Đăng nhập | Logo ngang 40 | Chân màn như dòng dưới |
| Splash | Logo ngang 64 | Trên app rộng tối đa bằng màn trừ lề, logo rộng thì hạ cao, không dưới 20: Delta còn cao khoảng 61 trên khung 393. Theo chế độ Sáng, Tối; khách chưa có bản nền tối thì **giữ nền trắng**, kể cả khi người dùng ở chế độ Tối |
| Chân đăng nhập, splash | Dòng "Được phát triển bởi innvie", cao 20 | Tắt được theo khách (`P-hien-phat-trien-boi`). Không dùng "Vận hành trên" |
| Màn Giới thiệu, giấy tờ | innvie | Luôn có, không phụ thuộc tham số trên |
| Favicon, icon app | Theo khách ngay từ đầu | `P-favicon`, `P-icon-app`. Mỗi khách một bản app trên store (`docs/_product/saas-core-vs-tenant.md` Mục 7 việc 3) |
| Email giao dịch, chứng từ in | Logo khách | Delta: chứng từ in dùng `delta-original.svg` |

Tầng của chân màn: `[Lõi] [Cấu hình]`, khách lớn có thể đòi tắt.

### 14.6 Màu thương hiệu

Collection `9. Brand · Invlogis` (DEC-261): `invlogis/*`, `innvie/primary`. Chỉ dùng cho logo, trang giới thiệu, tài liệu;
**không dùng trong component sản phẩm**: màu sản phẩm theo khách đi qua collection `7. Brand` và vai `color/accent/*`
([color.md](color.md) mục 3.5).

- Có trong `tokens.css` dưới dạng `--invlogis-*`, `--innvie-primary` để trang giới thiệu dùng chung (DEC-326). Component gọi các biến
  này thì `python3 _scripts/ds-token-usage.py --check` báo WARN `brandleak`.
- `design/brand/invlogis/brand-tokens.css` giữ tiền tố `--brand-c-*`, cùng giá trị; `python3 _scripts/ds-v2-tokens.py --check` báo khi lệch.
- SVG logo mang sẵn mã màu. Gradient logo #A3B0FF khác `invlogis/peri` #97A6FF, nên không đổi màu logo bằng token.

### 14.7 Còn mở

- Delta bật hay tắt dòng "Được phát triển bởi innvie": `P-hien-phat-trien-boi` chưa chốt (OQ).
- Logo tỉ lệ rộng hơn 8,8:1: cao 20 vẫn quá 176 ở đầu menu. Chưa có luật.
- Ô trắng cố định chưa có token nền luôn trắng; `color/text/white` chỉ cho chữ.
- Email: ảnh phải là PNG; header chàm đêm của mẫu hiện tại là màu Invlogis, chưa quyết khi đặt logo khách.
