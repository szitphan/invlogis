# Định dạng deck.md

`deck.md` là nguồn sự thật của một bộ slide. AI viết file này. `engine/build-deck.py` là bên duy nhất
sinh HTML từ nó. Muốn đổi slide thì sửa `deck.md` rồi build lại, không sửa file `.html`.

## Khung file

```markdown
---
type: meeting-deck
meeting: open-questions        # loại buổi họp (kịch bản), xem recipe-*.md
delivery: meeting              # meeting = chiếu khi họp · async = gửi khách tự trả lời (xem mục Hình thức)
feature: refund                # tuỳ chọn — bỏ khi deck cấp dự án
title: Rà soát câu hỏi mở — Hoàn tiền
client: Tên khách              # hiện ở slide bìa
presenter: Tên người trình bày # tuỳ chọn, hiện ở slide bìa
date: 2026-10-08               # ngày họp (ISO); bìa tự hiện 08/10/2026
duration: 45                   # phút — presenter báo khi quá giờ (chỉ meeting)
reply_to: chị Lan (lan@…)      # chỉ async — người nhận câu trả lời, hiện nguyên văn trên slide hướng dẫn
reply_by: 2026-10-15           # chỉ async — hạn trả lời (ISO), hiện ở bìa + slide hướng dẫn
footer: Rà soát câu hỏi mở     # tuỳ chọn, mặc định = title
brand: innvie                  # tuỳ chọn — thư mục design/brand/{slug}/; `none` để tắt
status: draft
updated: 2026-10-06
links:                         # mọi file nguồn đã dùng (hook stale theo dõi)
  - docs/refund/srs/refund-spec.md
---

<!-- layout: title -->
# Tiêu đề
Dòng phụ

---

<!-- layout: oq; id: OQ-1; src: docs/...; recommend: C -->
## Câu hỏi?
...
```

- Các slide ngăn nhau bằng một dòng chỉ có `---`.
- Dòng đầu mỗi slide là directive `<!-- key: value; key: value -->` (dấu `;` ngăn các cặp). Không có
  directive thì: slide đầu có `# ` → `title`; slide có `### A.` → `oq`; còn lại → `bullets`.

## Directive

| Key | Áp cho | Ý nghĩa | Khách thấy? |
|---|---|---|---|
| `layout` | mọi slide | `title` · `goal` · `agenda` · `bullets` · `section` · `oq` · `recap` · `end` (`guide` chỉ do build sinh) | — |
| `id` | `oq` | Mã câu hỏi gốc (vd `OQ-3`). Khoá lưu quyết định và là cột Mã khi xuất kết quả | Không, chỉ presenter |
| `src` | `oq` | Đường dẫn file chứa câu hỏi gốc, để `/deck import` biết cập nhật về đâu | Không, chỉ presenter |
| `recommend` | `oq` | Chữ cái phương án BA đề xuất. Thẻ đó có viền xanh + nhãn "Đề xuất" | Có (nhãn) |
| `group` | `oq` | Nhóm chủ đề, hiện cạnh "Câu hỏi 3/8" | Có |
| `time` | mọi slide | Số phút dự kiến. Presenter báo đỏ khi quá | Không |
| `refs` | mọi slide | Mã liên quan, ngăn bằng `,` (FR/BR/UC…). Chỉ hiện ở presenter | Không |

## Nội dung trong slide

| Viết | Hiển thị |
|---|---|
| `# …` | Tiêu đề lớn (title / end) |
| `## …` | Tiêu đề slide. Với `oq`: **câu hỏi** |
| `> …` | Khối bối cảnh (nền xám, viền trái) |
| `**Nhãn:** nội dung` | Dòng có nhãn, vd `**Ảnh hưởng:** …` |
| `**Tài liệu:** …` | Dòng nguồn cho khách (chữ nhỏ, xám): tên tài liệu khách gửi + ngày bản + số mục, tên mục. Đặt ngay sau `>` bối cảnh |
| `- …` / `1. …` | Gạch đầu dòng |
| dòng thường | Đoạn văn |
| `### A. Tên phương án` | Mở một thẻ phương án (chỉ `oq`). Chữ cái A–D |
| ↳ dòng thường ngay dưới | Mô tả ngắn của phương án |
| ↳ `+ …` | Ưu điểm |
| ↳ `- …` | Nhược điểm |
| `::: notes` … `:::` | Ghi chú người trình bày. Chỉ hiện ở cửa sổ presenter (phím P) |

Inline: `**đậm**`, `*nghiêng*`, `` `mã` ``, `[chữ](https://…)`.

Thẻ phương án kết thúc khi gặp `### ` khác, `## `, `> ` hoặc `**Nhãn:**`. Vì vậy dòng
`**Ảnh hưởng:**` đặt sau thẻ cuối vẫn là dòng của slide, không bị nhét vào thẻ.

## Layout

| Layout | Dùng cho | Ghi chú |
|---|---|---|
| `title` | Bìa | Nền đậm. Tự thêm dòng `client · date · presenter` từ frontmatter |
| `goal` / `agenda` / `bullets` | Mục tiêu họp, agenda, bước tiếp theo | Cùng một khung, khác tên để đọc file dễ hơn |
| `section` | Ngăn nhóm chủ đề | Chữ lớn giữa slide |
| `oq` | Một câu hỏi mở | Có phương án → các thẻ bấm được để chốt. Không có phương án → ô trả lời lớn |
| `recap` | Tổng kết | Bảng tự điền từ quyết định ghi trong buổi họp (bấm vào câu hỏi để mở lại đúng slide câu đó) + nút Tải/Copy/Xoá |
| `end` | Kết | Căn giữa |

## Hình thức (`delivery`)

| | `meeting` (mặc định) | `async` |
|---|---|---|
| Ai cầm file | BA chiếu, share screen | Khách tự mở trên máy họ |
| Slide hướng dẫn | Không | **Build tự chèn** "Hướng dẫn trả lời" ngay sau bìa (câu chữ cố định trong `build-deck.py` → `guide_slide`, điền `reply_to` + `reply_by`). Không viết tay — lint chặn |
| Điều hướng | Phím tắt | Phím tắt + thanh nút **Hướng dẫn · ‹ · n/N · ›** góc dưới phải |
| Nhãn trên slide `oq` | Quyết định · Hoãn · "Đã chốt" | Trả lời · **Cần trao đổi thêm** · "Đã chọn" |
| Slide `recap` | Tải kết quả (.md) | Ô **Họ tên người trả lời** (bắt buộc trước khi tải/copy) + Tải câu trả lời |
| Nhúng vào HTML | Ghi chú, `src`, `refs`, `recommend`, `time` | **Chỉ `id`** — ghi chú/nguồn/refs/time KHÔNG nhúng (khách mở mã nguồn là đọc được). Phím P tắt |
| File xuất | `{…}-ket-qua.md` | `{…}-tra-loi.md`, frontmatter thêm `delivery`, `client`, `respondent`; cột Nguồn để trống |
| Nút Copy | Chép nguyên `.md` kết quả | Chép **thư trả lời** đọc được: "Chào anh/chị" · tóm tắt số câu · `Câu N. …` / `Trả lời:` / `Ý kiến thêm:` · ký tên. Có cả bản HTML (in đậm khi dán vào email) và bản chữ thường (Zalo) |

Lint riêng `async`: thiếu slide `recap` → **lỗi** (khách không có nút gửi lại); `reply_by` sai định dạng → lỗi;
thiếu `reply_to` → cảnh báo (slide hướng dẫn ghi "gửi lại cho người đã gửi file này").

## Brand (thương hiệu đơn vị trình bày)

Brand nằm ở **dự án**, không nằm trong skill: `design/brand/{slug}/brand.yml` + file logo cùng thư mục.

```yaml
name: Tên đơn vị
colors:
  primary: "#0036B5"     # nền slide bìa / ngăn mục / kết; nút chính
  on-primary: "#FFFFFF"  # chữ trên nền primary
  accent: "#00A2FF"      # thanh tiến độ, viền + nền thẻ đề xuất
logo:
  on-primary: logo-color.png   # PNG nền trong suốt hoặc SVG, đặt trên nền primary
  on-light: logo-black.png     # PNG nền trong suốt, đặt trên nền trắng
mark:                          # biểu tượng không chữ — trang trí bìa / ngăn mục; nên dùng SVG (cỡ lớn, PNG dễ mờ)
  on-primary: mark-color.png
  on-light: mark-black.png
```

| Frontmatter | Kết quả |
|---|---|
| `brand: <slug>` | Dùng `design/brand/<slug>/`. Không có thư mục → lỗi lint |
| không khai | Đúng 1 brand trong `design/brand/` → tự dùng. 0 hoặc nhiều → không brand |
| `brand: none` | Tắt brand (vd deck white-label) |

Có brand thì: bìa có logo góc trên + mark lớn bên phải; ngăn mục và slide kết dùng nền `primary` (slide kết: logo nhỏ góc trên phải, lời cảm ơn giữa slide); slide
nội dung có logo nhỏ ở chân trang. Logo được nhúng base64 vào HTML để vẫn chạy offline.

## Lint (gate trong build-deck.py — lỗi thì không ghi HTML)

| Luật | Lỗi khi |
|---|---|
| Mã nội bộ | Chữ hiển thị có `FR-x-001`, `BR-…`, `E-…`, `OQ-3`, `UC-…`, `US-001`, `CR-…`, `OBJ-…`, `CMP-…`… |
| Đường dẫn nội bộ | Chữ hiển thị có `docs/…` hoặc tên file `.md` |
| Mật độ | Vượt số ký tự hiển thị theo layout (`oq` 900, `bullets` 620, `title` 260); quá 7 gạch đầu dòng |
| Câu hỏi | `oq` thiếu `## câu hỏi`, câu hỏi > 170 ký tự, bối cảnh > 300 ký tự |
| Phương án | > 4 phương án, trùng chữ cái, > 3 ý +/− mỗi loại, > 260 ký tự/thẻ, `recommend` không khớp |
| id | Hai slide `oq` trùng `id` |
| Brand | `brand:` khai tên không có trong `design/brand/`, hoặc thiếu file logo ghi trong `brand.yml` |

Cảnh báo (vẫn build): thiếu `id` / `src` / dòng `**Tài liệu:**` trên `oq`, có `oq` mà không có `recap`, chỉ 1 phương án, thiếu
field frontmatter.

Mã nội bộ và đường dẫn chỉ được nằm trong directive hoặc `::: notes`. Đó là nơi BA cần thấy khi trả lời
khách, còn khách thì không thấy.
