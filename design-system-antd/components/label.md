---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/input.md
  - design-system-antd/components/select.md
---

# Label — `nz-form-label` (trong `nz-form-item`)

> Bộ thử AntD. **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
> Nguồn: `shadcnuikit.com/components/label` trả 404 (kit không có trang Label, không có registry `label1…`);
> dùng `ui.shadcn.com/docs/components/label` + `/docs/components/field` (FieldLabel · FieldDescription · FieldError).
> Thuộc tính theo **API ng-zorro 22.x** (`nz-form-label`, `nz-form-control`). Con số là token trong `token-mapping.md` Mục 7.12 (đề xuất).
> Kiểu khớp mẫu ghép Input/Select: chữ `text/base/medium`, nhãn cách ô 6.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nz-form-label` | Set `Label` | Kiểu (3) × Gợi ý (2) × Trạng thái (2) = 12 | |
| `nzRequired` | `Kiểu` = Bắt buộc | dấu `*` **sau** chữ, `color/error` | ng-zorro đặt `*` trước chữ → ghi đè đặt sau để chữ nhãn thẳng với ô |
| (không có) | `Kiểu` = Tuỳ chọn + `Chữ phụ` (text) | "(không bắt buộc)" `text/sm` `color/text-secondary` | span riêng; mặc định mọi ô là bắt buộc |
| `nzTooltipTitle` · `nzTooltipIcon` | `Gợi ý` = Có + `Icon` (instance swap) | icon info 16 `color/text-secondary` | Rê/chạm mở Tooltip (trang Tooltip) |
| `nzNoColon` | — | luôn `true` | Không dấu `:` sau nhãn |
| `nzFor` | — | dev gắn id ô | Chạm nhãn = focus ô |
| disabled | `Trạng thái` = Đã tắt | `opacity/disabled` 50% | Theo ô đang tắt |
| `nzText` | `Nhãn` (text) | | |

**Trường form** (`nz-form-item`) — set phụ ghép Label + instance Input `47:77`/`47:108`:

| ng-zorro | Figma property | Giá trị | Ghi chú |
|---|---|---|---|
| `nzLayout` vertical / horizontal · `nzLabelAlign` | `Bố cục` | Nhãn trên · Nhãn trái | Nhãn trái: cột nhãn 120, gap 16, nhãn canh giữa ô cao 36; mobile luôn Nhãn trên |
| `nz-form-control nzExtra` | `Dòng dưới` = Gợi ý + `Gợi ý` (text) | `text/sm` `color/text-secondary`, cách ô 6 | "Theo đăng ký xe" |
| `nzErrorTip` · `nzValidateStatus` | `Dòng dưới` = Lỗi + `Báo lỗi` (text) | `text/sm` `color/error`; ô Input = trạng thái Lỗi | Thay dòng gợi ý, không hiện cả hai |

Set `Trường form` = Bố cục (2) × Dòng dưới (3) = 6. Chữ nhãn trong Trường form sửa bằng override instance `Label`.

## 2. Dựng tạm — đề xuất Dùng / Không dùng

Vì kit không có ví dụ đánh số, mã `lb-NN` là mã tự đặt từ các mẫu docs shadcn (label, field) và từ mẫu Input web-02/03/14/25 đã duyệt.

| Mã | Ví dụ | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| lb-01 | Nhãn trên ô nhập | `nz-form-label` + `nz-input` | **Dùng** | Mọi form: Biển số xe, Mã lệnh |
| lb-02 | Nhãn bắt buộc `*` | `nzRequired` | **Dùng** | Mã lệnh vận tải, Biển số, Tài xế |
| lb-03 | Nhãn tuỳ chọn "(không bắt buộc)" | chữ phụ riêng | **Dùng** | Ghi chú cho tài xế — rõ hơn bỏ trống không giải thích |
| lb-04 | Nhãn + icon ⓘ | `nzTooltipTitle` | **Dùng** | Tải trọng tối đa, Phí phát sinh — giải thích quy tắc ngắn |
| lb-05 | Nhãn + dòng gợi ý dưới ô | `nz-form-control nzExtra` | **Dùng** | "Theo đăng ký xe" (khớp Input web-03) |
| lb-06 | Nhãn + báo lỗi dưới ô | `nzErrorTip` | **Dùng** | Biển số sai định dạng |
| lb-07 | Nhãn trái (form ngang) | `nzLayout="horizontal"` | **Dùng** | Màn chi tiết/sửa rộng trên web; mobile không dùng |
| lb-08 | Nhãn cho Select | `nz-form-label` + `nz-select` | **Dùng** | Tài xế phụ trách, Loại xe |
| lb-09 | Nhãn nhóm Checkbox/Radio | `nz-form-label` + `nz-checkbox-group` | **Dùng** | Loại hàng — nhãn nhóm khác nhãn từng ô |
| lb-10 | Form ngắn lệnh vận tải | 3 `nz-form-item` | **Dùng** | Mẫu dev kiểm khoảng cách giữa các trường (16) |
| lb-11 | Nhãn gắn Checkbox ("Accept terms", demo shadcn) | `nz-checkbox` có chữ | Không dùng | Trùng: Checkbox đã có chữ bên cạnh ô (Checkbox mẫu ghép/web-01) |
| lb-12 | Nhãn nổi / nằm trong ô | — | Không dùng | Input web-14 đã bỏ; web-25 (nhãn trong ô) chỉ cho form mobile và nằm ở trang Input |
| lb-13 | Nhãn hàng chữ hoa nhỏ (caption) | — | Không dùng | Trang trí, không có trong ng-zorro, lệch quy ước nhãn Medium 14 |
| lb-14 | Nhãn + liên kết phụ cùng hàng ("Quên mật khẩu?") | `nzTooltip` ngoài | Không dùng | Đăng nhập tài xế dùng OTP; chưa có form cần link cạnh nhãn |

## 3. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Label** (`71:5864`) — khuôn như Select/Input:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Label` (tài liệu) | `71:7908` | Rộng 1536: đầu trang · Playground Light `71:7916` / Dark `71:7935` · `Ví dụ đã chốt` `71:7954` (10 thẻ lb-01…10) · `Mapping` `71:8023` (10 hàng thuộc tính, 6 hàng token) |
| Section Components | `71:6000` | Set `Label` `71:5999` = 12 biến thể (ma trận cột Mặc định/Đã tắt, hàng Kiểu → có/không ⓘ) · Set `Trường form` `71:6171` = 6 biến thể |
| Section Mẫu ghép | `71:7199` | 10 component `Label mẫu ghép/lb-NN …` (`71:6896` lb-01 · `71:6919` · `71:6946` · `71:6973` · `71:6997` · `71:7018` · `71:7034` · `71:7057` · `71:7087` · `71:7125` lb-10) |
| Biến mới | `VariableID:71:11449…11452` | `label/gap` · `label/field-gap` · `label/column-gap` · `label/column-width` |

Thuộc tính Label: `Nhãn` (text) · `Chữ phụ` (text) · `Icon` (instance swap, mặc định `icon/info` `55:3764`). Thuộc tính Trường form: `Gợi ý` · `Báo lỗi` (text).
Chữ nhãn: text style `text/base/medium` (không dùng style `text/sm/medium`, vì mẫu ghép Input/Select hiện dùng base 14).
Dùng lại icon `icon/info` (trang Button) — không tạo icon mới.
