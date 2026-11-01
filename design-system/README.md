---
type: design-readme
status: draft
updated: 2026-10-30
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/tokens.json
  - design-system/crosswalk.md
  - design-system/components/platform-names.json
  - _scripts/ds-v2-handoff.py
  - _workspace/decisions.md
---

# Design System v2 — cửa vào cho dev

> Dành cho dev web (Angular) và app (Flutter). Cấu trúc theo DEC-255, học từ Zeta (Zebra), Spectrum (Adobe),
> Equinor, Backpack (Skyscanner). DS v2 đang dựng (vòng 4/6): tên component Angular/Flutter còn là **đề xuất**.

## 1. Một mã nối bốn bên

Mỗi component có **một mã** (tiền tố = nhóm `base` / `application`; `ds-v2-handoff.py` chưa đọc hai thư mục này — registry tạm rỗng sau khi bỏ `l1/`, DEC-312) (vd `base.button`) dùng chung ở tài liệu BA, Figma, Angular và Flutter:

```
BA: bảng mô tả màn (cột Control type)      docs/{feature}/screens/{flow}.md
        │  crosswalk.md
        ▼
Mã component  base.button                    handoff/components/registry.json
        ├── Figma   Base / Button (6373:491)
        ├── Spec    components/base/button.md (khối Web + khối Mobile)
        ├── Angular <inv-button>  InvButtonComponent
        └── Flutter InvButton
```

## 2. Đọc gì

| Bạn là | Lấy | Ở đâu |
|---|---|---|
| Dev Angular | Biến CSS (đổi theo `data-theme`, `data-platform`, `data-brand`, `data-context`) | `handoff/web/tokens.css` |
| | Biến SCSS trỏ biến CSS | `handoff/web/_tokens.scss` |
| Dev Flutter | Hằng + `ThemeExtension` (`InvColors`, `InvBrandColors`, `InvComponentColors`, `InvContextColors`, `InvPlatform`, `InvTypography`), hàm `invTheme()` | `handoff/flutter/invlogis_tokens.g.dart` |
| Cả hai | Danh sách component: mã, Figma node, spec, tên code | `handoff/components/registry.json` |
| | Thuộc tính từng component theo nền tảng (biến thể, mặc định, giá trị), token dùng, DEC | `handoff/components/{mã}.json` |
| | Spec đầy đủ cho người đọc (cấu tạo, trạng thái, trợ năng, nên/không nên) | `components/{base\|application}/{tên}.md` |
| | Icon: Lucide + icon nghiệp vụ tự vẽ + bảng nghĩa | `handoff/icons.json`, `icons/*.svg` |
| | Control type BA → mã component | `handoff/crosswalk.json` |
| Dùng Style Dictionary / Tokens Studio | Token chuẩn DTCG, 1 file mỗi collection mỗi mode | `handoff/tokens/*.tokens.json` + `index.json` |

## 3. Thư mục

```
design-system/
├── README.md                  ← file này
├── architecture.md · foundations.md · icons.md        luật (người đọc)
├── tokens.json                NGUỒN token (tên = tên biến Figma)
├── tokens.css                 sinh từ tokens.json (_scripts/ds-v2-tokens.py)
├── crosswalk.md               NGUỒN: Control type BA → mã component
├── icons/                     NGUỒN: svg icon nghiệp vụ tự vẽ
├── components/
│   ├── README.md              cấu trúc thư mục, cách ghi md
│   ├── platform-names.json    NGUỒN: tên Angular / Flutter của từng mã
│   ├── base/*.md · application/*.md   NGUỒN: spec component (DEC-260)
│   └── _work/{slug}/          trang brainstorm, chốt xong mới ghi md
└── handoff/                   SINH RA — không sửa tay
    ├── tokens/   DTCG
    ├── web/      tokens.css · _tokens.scss
    ├── flutter/  invlogis_tokens.g.dart
    ├── components/ registry.json · {mã}.json
    └── crosswalk.json · icons.json
```

## 4. Giữ ba bên khớp nhau

| Đổi gì | Sửa ở | Rồi chạy |
|---|---|---|
| Token | Biến Figma **và** `tokens.json` (cùng tên) | `python3 _scripts/ds-v2-tokens.py` → `python3 _scripts/ds-v2-handoff.py` |
| Component | Figma qua `/figma-component` **và** `components/{base\|application}/{tên}.md` | `python3 _scripts/ds-v2-handoff.py` |
| Tên code | `components/platform-names.json` (đổi `status` thành `dev đã chốt`) | `python3 _scripts/ds-v2-handoff.py` |
| Control type mới | `crosswalk.md` | `python3 _scripts/ds-v2-handoff.py` |

`python3 _scripts/ds-v2-handoff.py --check` không ghi gì. Lệnh này báo `handoff/` lệch nguồn, mã trỏ sai và tên biến CSS
bị trùng. Dùng trước khi gửi dev hoặc commit.

## 5. Ghi chú cho dev

- **Flutter:** `invlogis_tokens.g.dart` chưa được biên dịch thử (máy dựng chưa có Dart SDK). Gặp lỗi thì báo lại để sửa
  script, đừng sửa tay file sinh ra. Font cần khai trong `pubspec.yaml`: `CalSans`, `Inter`, `JetBrainsMono`.
- **Angular:** bắt đầu bằng cách import `tokens.css` toàn cục. `_tokens.scss` chỉ là tên SCSS cho cùng biến CSS,
  không chứa giá trị cứng.
- **Code Connect (Figma Dev Mode):** khi dev có code component, thêm file template `*.figma.template.js` (đường
  template là cách Code Connect còn hỗ trợ, áp cho cả Angular và Flutter). Chưa làm ở đợt này.
- **Màu theo khách:** đặt `data-brand="{slug}"` (web) hoặc `InvBrandColors.all[slug]` (Flutter); slug ở
  `handoff/tokens/index.json` → `modes.Brand`.
