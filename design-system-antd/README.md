---
type: design-system
status: draft
updated: 2026-11-06
links:
  - design-system-antd/token-mapping.md
---

# Design system thử nghiệm — shadcn → Figma variable → Ant Design (ng-zorro)

> Bộ **thử**, độc lập hoàn toàn với `design-system/` (DS v2) và `design/`. Không dùng chung file token,
> component hay file Figma. Chỉ dùng chung rule nghiệp vụ. Khi thử xong mới quyết có thay DS v2 hay không.

## Vì sao có bộ này

- DS v2 gom nhiều nguồn (Untitled, shadcn, Astryx, Spartan) nên số liệu lệch nhau, padding không đều.
- Dev web dùng **Angular + ng-zorro-antd** (Ant Design). Handoff từ thư viện khác hệ khiến dev phải dịch lại.

## Nguyên tắc

| # | Nguyên tắc |
|---|---|
| 1 | **Figma variable là nguồn chuẩn.** Tên đặt theo biến Less của ng-zorro (vd `@height-base` → `height/base`) để dev biết sửa biến nào |
| 2 | **Giá trị foundation lấy từ shadcn/Spartan** (theme neutral). Ant Design chỉ nhận giá trị đó vào biến của nó |
| 3 | Mỗi token rơi vào 1 trong 3 trường hợp: **1:1** · **Ghi đè** (dev đổi giá trị biến Less) · **Thêm mới** (Ant Design không có, dev thêm vào theme) |
| 4 | Clone component từ shadcn: **không chép số thô**, mọi con số gắn về biến. Số không gắn được → người duyệt quyết |
| 5 | **Biến thể và thuộc tính component bám API ng-zorro** (vd button `nzType`, `nzSize`). shadcn chỉ quyết giao diện |
| 6 | Mọi token mới phát sinh khi làm component đều thêm vào `token-mapping.md` — một bảng duy nhất từ đầu đến cuối |

## Nguồn

| Nguồn | Dùng để | Đường dẫn |
|---|---|---|
| Shadcn UI Kit for Figma (Embed) | Cách trình bày trên Figma: trang Style Guide (bảng Tên biến · Giá trị · Mẫu), mỗi component một trang (khung tài liệu + Playground sáng/tối + section Components) | figma.com/design/uSGI07mEcItaHEVre2RwFq (chỉ xem, đọc qua trình duyệt) |
| shadcn/ui v4 | Giá trị token + class component (nguyên văn) | ui.shadcn.com/docs/theming · github shadcn-ui/ui `apps/v4/registry/new-york-v4/ui/*` |
| Spartan UI | Đối chiếu bản Angular của shadcn — token giống shadcn, khác 2 màu sidebar nền tối | spartan.ng/documentation/theming |
| ng-zorro-antd 22.2.0 | Tên + mặc định biến Less | ng.ant.design/docs/customize-theme · `components/style/themes/default.less` |

## File Figma bộ thử

[Invlogis DS · AntD pilot](https://www.figma.com/design/ElvhTYV3unixPkXky2oKIY) — Drafts, team innvie. Collection `color` (Light/Dark) · `size` · `type`; code syntax WEB = tên biến Less ng-zorro (xem trong Dev Mode).

## Thứ tự làm

1. ✅ Bảng mapping token (`token-mapping.md`)
2. ✅ Foundations: duyệt 06/11 (`foundations/foundations.md`) · dựng Figma 06/11 (105 biến, 20 text style, 4 effect style, trang Style Guide)
3. ⬜ Base components hàng loạt — người duyệt chọn biến thể giữ/loại trước khi dựng
4. ⬜ Rà máy (số thô chưa gắn biến, padding không đều) → đánh giá hiệu quả
