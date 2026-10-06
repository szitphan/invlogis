# Kịch bản: họp chốt câu hỏi mở (`meeting: open-questions`)

Mục đích buổi họp: khách **trả lời / chọn** để đội đi tiếp. Không phải buổi trình bày tính năng.
Mỗi câu hỏi một slide, và slide phải giúp khách quyết định trong vài phút.

## Trình tự slide

### Họp trực tiếp (`delivery: meeting`)

| # | Layout | Nội dung | Thời lượng gợi ý |
|---|---|---|---|
| 1 | `title` | Tên buổi họp + 1 dòng "hôm nay cần chốt gì" | — |
| 2 | `goal` | Mục tiêu: chốt N câu · câu chưa chốt được thì thống nhất ai trả lời + hạn · tổng thời lượng | 2 phút |
| 3 | `agenda` | Các nhóm câu hỏi (theo `group`) + số câu mỗi nhóm. Bỏ slide này khi ≤ 4 câu | 1 phút |
| … | `section` | Ngăn nhóm. Chỉ dùng khi ≥ 3 nhóm **và** ≥ 8 câu | — |
| … | `oq` × N | Mỗi câu hỏi 1 slide (khung bên dưới) | 5–10 phút/câu |
| N+1 | `recap` | Tổng kết quyết định (tự điền lúc họp) + tải kết quả | 3 phút |
| N+2 | `bullets` | Bước tiếp theo: cập nhật tài liệu nào, câu hoãn ai trả lời, hạn nào | 2 phút |
| N+3 | `end` | Cảm ơn | — |

### Gửi khách tự trả lời (`delivery: async`)

Không có buổi họp, không có người trình bày, nên trình tự gọn hơn và mỗi slide phải tự đủ nghĩa.

| # | Layout | Nội dung |
|---|---|---|
| 1 | `title` | Tên bộ câu hỏi + 1 dòng "nhờ anh/chị trả lời giúp N câu để đội đi tiếp". Bìa tự hiện hạn trả lời |
| 2 | *(tự chèn)* | **Hướng dẫn trả lời** — build sinh, KHÔNG viết |
| 3 | `goal` | Vì sao cần trả lời + mất khoảng bao lâu (≈ 2–3 phút/câu). Không ghi "thời lượng họp" |
| … | `section` / `oq` × N | Như trên. Bỏ `agenda` khi ≤ 6 câu |
| N+1 | `recap` | `## Tổng kết câu trả lời` (khung tự điền + ô tên + nút tải) |
| N+2 | `end` | Cảm ơn + "đội sẽ phản hồi trong {N} ngày sau khi nhận" nếu user đã nói |

Khác cách viết so với họp:

- **Lý do đề xuất lên slide.** Có `recommend` thì thêm 1 dòng `**Vì sao đề xuất C:** …` (lời khách, không
  mã) — ghi chú không được gửi đi nên khách không thấy lý do nếu chỉ để trong notes.
- **Câu hỏi mở thật** (không phương án) → bối cảnh nói rõ khách cần trả lời gì, ví dụ mức chi tiết mong
  muốn, vì không có ai hỏi lại tại chỗ.
- Không viết "trong buổi họp hôm nay", "thống nhất tại chỗ". Không cần `time:`.
- Vẫn giữ `::: notes` cho BA (nguồn, câu hỏi phụ) — chỉ nằm trong `deck.md`, không vào file gửi khách.

## Khung một slide `oq`

```markdown
<!-- layout: oq; id: {mã gốc}; src: {file gốc}; recommend: {chữ}; group: {nhóm}; time: {phút} -->
## {Câu hỏi viết lại bằng lời của khách, kết thúc bằng dấu ?}

> {Bối cảnh 1–2 câu: hiện trạng / vì sao đang treo. Có số liệu thì nêu số}

### A. {Tên phương án ngắn}
{1 dòng mô tả nếu tên chưa đủ rõ}
+ {ưu điểm nhìn từ phía khách}
- {nhược điểm / đánh đổi}

### B. …

**Ảnh hưởng:** {phần nào của sản phẩm phụ thuộc vào câu trả lời — nói bằng màn / quy trình / vai trò, không nói mã}

::: notes
- Nguồn: {mã FR/BR/OQ + file:mục}
- Vì sao đề xuất {chữ}: {lý do + bằng chứng}
- Nếu khách chọn {X} thì cần hỏi thêm: {câu phụ}
:::
```

## Viết câu hỏi

- **Viết lại câu hỏi gốc theo lời khách.** Câu gốc trong tài liệu thường viết cho đội nội bộ (có mã,
  tên mục, giả định kỹ thuật). Lên slide thì dùng thuật ngữ nghiệp vụ của khách, đọc trong
  `docs/_shared/project-profile.md` mục "Người dùng & thuật ngữ".
- Một slide chỉ hỏi **một quyết định**. Câu gốc gộp nhiều ý (vd "có sinh phiếu không, **và** 1 lệnh có
  nhiều phiếu không?") thì tách thành 2 slide, hoặc giữ 1 câu chính và đưa ý phụ xuống notes làm câu
  hỏi tiếp theo.
- Câu hỏi đóng (chọn A/B) thì cho phương án. Câu hỏi mở thật sự ("quy trình hiện nay ra sao?") thì
  **không bịa phương án**: bỏ trống `###`, slide sẽ hiện ô trả lời lớn.

## Phương án — chống bịa

- Mỗi phương án phải có gốc: tài liệu nguồn, SOP, hiện trạng khách đã mô tả, hoặc cách làm phổ biến mà
  BA nêu rõ là đề xuất. Ghi gốc đó trong notes.
- 2–3 phương án là tốt nhất, tối đa 4. Luôn có sẵn nút **Khác** và **Hoãn** trên slide, nên không cần
  viết phương án "Khác".
- Ưu/nhược viết từ góc nhìn khách: tốc độ, kiểm soát, chi phí vận hành, trải nghiệm người dùng của họ.
  Không viết "dễ code", "đỡ sửa DB".
- `recommend` chỉ đặt khi BA có lý do. Lý do ghi trong notes để BA nói được khi khách hỏi "vì sao?".
  Không có cơ sở thì để trống, đừng đề xuất cho có.

## Sắp thứ tự

1. Câu **chặn** nhiều phần nhất lên trước (đếm số FR/màn/quy trình phụ thuộc — `kg impact` giúp đếm).
2. Gom câu cùng nhóm cạnh nhau (`group`).
3. Thời lượng không đủ cho hết (tổng `time` > `duration` − 10 phút mở/đóng) → đề xuất bỏ bớt câu ít
   chặn, hoặc tách 2 buổi. Hỏi user, không tự cắt.

## Slide "Bước tiếp theo"

Liệt kê việc sau họp bằng lời nghiệp vụ: "Cập nhật đặc tả phần {X} theo quyết định", "Câu hoãn:
{ai} trả lời trước {ngày}", "Gửi biên bản trong {N} ngày". Không ghi tên skill hay đường dẫn.
