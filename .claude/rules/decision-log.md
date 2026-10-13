---
paths:
  - "_workspace/decisions.md"
  - "docs/**"
  - "design/**"
---

# Decision Log — mỗi quyết định có lý do và phương án đã bỏ

> Nguồn: `_workspace/decisions.md`. Rule chung cho mọi skill và mọi lượt làm việc có user chốt một
> lựa chọn (phạm vi, quy tắc, giao diện, cách làm).

## 1. Khi nào ghi DEC

| Tình huống | Ghi ở đâu |
|---|---|
| User (hoặc đội) chốt giữa ≥2 phương án: phạm vi, quy tắc nghiệp vụ dùng chung, design system, mẫu màn, quy ước làm việc | **`_workspace/decisions.md`** — 1 dòng DEC |
| Khách trả lời OQ | Biên bản `docs/meetings/*.md` mục "Quyết định" (không chép sang DEC) |
| Chốt từng ý khi phỏng vấn brainstorm | `_workspace/interviews/{feature}-interview.md` (không chép sang DEC) |
| Đổi thứ đã `approved` / baseline | `/cr` → `docs/cr/CR-{id}.md` (rule `change-request.md`) |
| Sửa câu chữ, sửa lỗi, không có lựa chọn | Không ghi — changelog đủ |

## 2. Cột bắt buộc

`Mã | Ngày | Quyết định | Lý do | Phương án đã bỏ | Ai chốt | Nguồn / ghi ở | Trạng thái`

- **Lý do**: câu user nói hoặc dữ kiện dẫn tới lựa chọn (tương phản, trùng nghĩa, chi phí…). Không có thì
  **hỏi user 1 câu** trước khi ghi; user không trả lời → `⚠ chưa ghi lý do`. KHÔNG tự bịa lý do.
- **Phương án đã bỏ**: các phương án đã đưa ra mà không chọn. Không có phương án thay thế → `—`.
- **Trạng thái**: `hiệu lực` · `thay bởi DEC-xxx` (không xoá dòng cũ; dòng mới ghi DEC cũ ở cột Phương án đã bỏ).
- Mã tăng dần toàn file, không tái dùng; dòng mới thêm cuối nhóm phù hợp.

## 3. Trích trong doc

- Doc ghi mã thay cho ngày: `(DEC-034)` thay `(chốt 12/10/2026)`. Lý do dài không chép vào doc.
- Doc chỉ cần 1 câu ngắn nếu dev cần hiểu ngay; nguồn sự thật của lý do là sổ.

## 4. Cách ghi

Thêm dòng DEC là Edit file đã tồn tại → báo 1 dòng "Đã ghi DEC-NNN: … (lý do: …)", không cần L2 riêng
(như backlog). Sửa/đổi Trạng thái dòng cũ → L2 bảng Trước → Sau.

## Anti-patterns

- ❌ Ghi "(chốt dd/mm)" trong doc mà không có dòng DEC.
- ❌ Lý do kiểu "theo lab", "theo design.md" — đó là nơi ghi, không phải lý do.
- ❌ Xoá DEC cũ khi đổi ý — phải `thay bởi`.

## Tóm tắt 1 dòng

> **User chốt giữa các phương án → 1 dòng DEC có lý do + phương án đã bỏ; doc trích `(DEC-NNN)`; đổi ý thì
> `thay bởi`, không xoá.**
