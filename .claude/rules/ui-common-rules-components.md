---
paths:
  - "design/ui-common/**"
  - "docs/**/srs/**"
  - "docs/**/usecases/**"
  - "docs/**/ascii-wireframe/**"
  - "docs/**/html-wireframe/**"
  - "docs/**/html-design/**"
  - ".claude/skills/srs/**"
  - ".claude/skills/usecase/**"
  - ".claude/skills/user-flow/**"
  - ".claude/skills/sequence/**"
  - ".claude/skills/wireframe-*/**"
  - ".claude/skills/prototype-*/**"
  - ".claude/skills/figma-screen/**"
  - ".claude/agents/uxui-reviewer.md"
---

# UI Common Rules & Components — gọi theo mã, UC chỉ mô tả phần riêng

> Rule chung cho MỌI skill viết hoặc review đặc tả màn hình / use case / lỗi. Mỗi skill đã nối MUST
> reference file này trong Constraints + References. Nội dung cụ thể sống ở `design/ui-common/`, KHÔNG
> chép vào `.claude/`.

## 1. Phạm vi

| Skill / agent | Dùng phần nào |
|---|---|
| `/srs` | Mục 10 "Cấu hình UI Common Rules & Components" + Error Matrix dùng lại E-common |
| `/usecase` | Bước/Extension gọi CMP/GR; cột Errors dùng E-common |
| `/user-flow` | Nhận diện màn/nhánh do CMP sinh ra (confirm, lỗi Loại 2, rỗng) |
| `/wireframe-ascii`, `/wireframe-html`, `/prototype-html` | Cột Description: `Xem CMP-xx` / `Theo GR-xx` + phần UC phải khai báo |
| `/figma-screen` | Dùng đúng component ghi ở dòng **Figma** của CMP; cập nhật node + ảnh cache |
| `/sequence` | Nhánh lỗi dùng mã E-common thay vì tự đặt mã |
| `uxui-reviewer` | Tiêu chí review Mục 9 |

## 2. Hai file nguồn

| File | Chứa | Mã |
|---|---|---|
| `design/ui-common/screen-patterns.md` | Component dùng chung (bảng 5 cột, Figma, UC phải khai báo) | `CMP-01…` |
| `design/ui-common/conventions.md` | Quy tắc giao diện chung + bảng lỗi dùng chung | `GR-01…`, `E-common-NNN` |

Chưa có 2 file → báo 1 dòng "Chưa có UI Common Rules & Components — mô tả đầy đủ trong UC" và chạy
như cũ. KHÔNG tự sinh nội dung CMP/GR.

## 3. Đọc gì, khi nào

1. Đầu skill: đọc **bảng mục lục** đầu mỗi file (mã · tên · dùng khi).
2. Màn/UC chạm tới CMP/GR nào → đọc mục đó (Grep `^## CMP-xx` / `^### GR-xx` rồi Read theo dòng).
3. Mục trỏ sang design.md → đọc đúng mục design.md theo `design-system.md`.
4. Đọc lại từ file mỗi lần chạy, không trích từ trí nhớ.

## 4. Nhận diện CMP/GR

Element/bước khớp cột "Dùng khi" của bảng mục lục → gọi mã đó. Dấu hiệu thường gặp: toast sau hành
động (CMP-01), thông báo cho người khác (CMP-02), xác nhận Xoá/Thu hồi/Phê duyệt/Từ chối/Huỷ form
(CMP-03), cuối danh sách (CMP-04), bộ lọc/badge lọc (CMP-05, GR-20), tuỳ chỉnh cột (CMP-06), cột hành
động (CMP-07), icon lịch sử (CMP-08), luồng nhiều bước (CMP-09), đính kèm (CMP-10), menu trái
(CMP-11); trường nhập, ngày, tiền, số, email, SĐT, tìm, rỗng, chưa lưu, sắp/nhóm/freeze/export (GR).

## 5. Cách ghi trong UC / màn

- Cột Description (hoặc bước UC): `• Xem CMP-03 — Confirm Dialog` rồi **chỉ** liệt kê phần "UC phải
  khai báo" của CMP đó, điền bằng dữ liệu feature. Không chép lại phần chung.
- Quy tắc: `• Theo GR-01` + chỉ phần riêng (trường bắt buộc, giới hạn khác mặc định).
- Thiếu phần "UC phải khai báo" → hỏi user hoặc ghi OQ. KHÔNG lấy hành vi của feature khác
  (đúng `design-system.md` Luật 7).

## 6. Override phải có lý do

Khác quy tắc chung → ghi `Override GR-xx: {giá trị mới} — lý do: {…}`. Không có lý do → không override.
Override lặp ở ≥ 2 feature → đề xuất đưa lên CMP/GR (Mục 8).

## 7. Lỗi dùng chung E-common

- Lỗi trùng nghĩa với bảng E-common → dùng lại `E-common-NNN`, KHÔNG tạo `E-{feature}-NNN` mới.
- `E-{feature}-NNN` chỉ cho lỗi nghiệp vụ riêng của feature; ghi rõ loại GR-15 (Inline / Popup / Toast).
- Error Matrix SRS: liệt kê E-common feature dùng ở dòng riêng, không chép wording (wording ở conventions.md).
- KG parse bảng E-common như feature `common` (`kg-build.mjs`) — `E-common-NNN` không phải broken ref.

## 8. Thiếu CMP/GR

Gặp mẫu lặp mà chưa có mã → ghi tạm phần mô tả đầy đủ trong UC + gợi ý `/update-overview patterns`
(CMP) hoặc `/update-overview conventions` (GR) để thêm vào nguồn chung qua approval gate. Skill KHÔNG
tự sửa 2 file nguồn.

## 9. Tiêu chí review (uxui-reviewer, tự kiểm trước L1)

(a) Element khớp CMP/GR nào thì đã gọi mã chưa · (b) phần "UC phải khai báo" đủ chưa · (c) override
có lý do · (d) lỗi trùng nghĩa đã dùng E-common · (e) không chép lại phần chung hoặc wording cố định.

## 10. Ảnh và Figma

Dòng **Figma** mỗi CMP: component Astryx / component dự án · node mẫu trong file dự án · ảnh cache
`design/ui-common/images/cmp-NN.png`. `/figma-screen` khi vẽ CMP: dùng đúng component đó; có node mới thì đề xuất
cập nhật dòng Figma + chụp ảnh (Figma MCP `get_screenshot`) qua L2.

## 11. Thứ tự ưu tiên

`design/design.md` (token, component, câu chữ) **>** CMP/GR **>** override trong UC (phải có lý do).
CMP/GR lệch design.md → design.md thắng, đề xuất sửa CMP/GR.

## 12. Phụ lục A trong SRS cuối (chép nguyên văn bằng máy)

CMP/GR chỉ trỏ sang design.md để tránh 2 nơi lệch nhau — nhưng SRS gửi stakeholder phải ĐỦ nội dung.
Vì vậy spec có **Phụ lục A — UI Common Rules & Components áp dụng**, nằm giữa 2 marker
`<!-- ui-common:begin -->` / `<!-- ui-common:end -->`, sinh bởi `_scripts/ui-common-expand.py`:

- Lấy mã CMP/GR/E-common xuất hiện trong spec (ngoài phụ lục), chép nguyên văn mục CMP/GR + mục design.md
  ghi ở dòng `- **design.md:**` (tách `;`) + ảnh `cmp-NN.png` + dòng E-common, kèm `Nguồn: file:dòng`.
- **Máy sinh, KHÔNG sửa tay, AI KHÔNG viết lại.** Muốn đổi nội dung → sửa nguồn (design.md / CMP / GR)
  rồi chạy lại `--write`.
- `/srs` sinh sau khi có Mục 10 (qua L2); update mode chạy `--check`. `/export`, `/preview` chạy `--check`
  trước khi xuất — cũ/thiếu thì cảnh báo + đề nghị sinh lại.
- Bảng E-common trong phụ lục dùng header **"Mã lỗi"** (không phải "ID") để KG không coi spec là nơi
  định nghĩa thứ hai.
- Thêm CMP/GR mới → nhớ ghi dòng `design.md:` (hoặc `—` nếu không có mục tương ứng).

## Tóm tắt 1 dòng

> **Gọi `Xem CMP-xx` / `Theo GR-xx`, UC chỉ điền phần "UC phải khai báo" · SRS cuối có Phụ lục A máy chép nguyên văn · override có lý do · lỗi trùng
> nghĩa dùng E-common · thiếu mã thì đề xuất `/update-overview` · design.md > CMP/GR > UC.**
