---
paths:
  - "docs-input/**"
  - "docs/*/brainstorms/**"
  - "docs/*/srs/**"
---

# Source Coverage — đối chiếu tài liệu khách theo từng mục

> Rule chung cho skill đọc tài liệu khách vào giải pháp (`/brainstorm`, `/srs`, `/intake`, tách/gộp
> feature) và mọi lượt làm việc hứa "sẽ đưa X vào". Máy: `_scripts/source-coverage.py` (gate) +
> `_scripts/intake-sync.py` (cột Feed của sổ nguồn).

## 1. Vì sao

Sổ nguồn cũ tính "đã feed" theo cả file: có 1 doc feature trỏ tới nguồn là ✅. Hậu quả đã gặp: nguồn ✅
nhưng nhiều mục chưa ai đọc (mục "feature riêng" không có chủ, tách feature chép bản gộp không đối chiếu
lại, bản mới của khách tự ✅ vì doc có `updated:` mới). Chỉ đếm theo từng mục mới bắt được phần rơi.

## 2. Sổ đối chiếu

Mỗi nguồn có 1 file `docs-input/_coverage/{slug}.md` (slug = tên file nguồn không đuôi). Thư mục `_*`
không bị coi là nguồn.

```markdown
# Sổ đối chiếu: {tên tài liệu như khách gọi} (SRC-xx)

> Nguồn: `{đường dẫn trong docs-input}`
> Bản: {ngày tài liệu} (nhận YYYY-MM-DD)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 2.2 Tạo JobID nghiệp vụ (AI01) | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7, OQ-12 | |
| 2.2.1 Kiến trúc tích hợp Google Document AI | | | |
| 3.1 Trích xuất mã QR để thanh toán | ➡ payables | | QR ≥3 lần/15 phút |
| 5.2 Chi phí kết nối API Banking | ➖ | | báo giá ngân hàng, không phải yêu cầu |
```

- **Dòng = mục** lấy từ tiêu đề `#` của nguồn. Nguồn ít tiêu đề (bản chuyển từ docx) → lấy theo mục lục
  (`[**4.2.** **Tên**`). Ảnh/chứng từ mẫu không có mục → 1 dòng cho cả tài liệu.
- **Ô Kết quả trống = theo mục cha** (mục có số là tiền tố; mục không số theo dòng có kết quả gần nhất
  phía trên). Thêm dòng con khi mục con có kết quả khác cha.
- **Dòng `> Bản:`** = bản nguồn sổ đã đối chiếu. Máy so với dòng `> Phiên bản:` của nguồn.

| Kết quả | Nghĩa | Bắt buộc |
|---|---|---|
| ✅ | Đã đưa vào tài liệu | Ở đâu = đường dẫn có thật trong `docs/` (+ mã B/FR/OQ) |
| ➡ {feature} | Thuộc feature khác | Slug feature. Feature chưa có thư mục → máy tạo task "Lập feature" |
| ➖ | Ngoài phạm vi / không phải yêu cầu | Ghi chú = lý do |
| ⏳ | Chờ khách trả lời | Ghi chú = mã OQ ở doc feature |
| ⬜ | Chưa xử lý | — |
| 🔄 | Đổi ở bản mới, cần rà lại | Máy ghi; rà xong đổi sang kết quả khác |

## 3. Máy làm gì

| Việc | Script | Khi nào |
|---|---|---|
| Cột Feed sổ nguồn: ⬜ chưa feed · 🟡 đối chiếu n/m · ✅ đối chiếu m/m · ➖ giữ nguyên | `intake-sync.py` | hook mỗi lượt |
| ✅ chỉ khi hết ⬜/🔄, mọi ➡ trỏ feature đã có thư mục, không dòng ghi sai | `intake-sync.py` | như trên |
| Nguồn ✅ cũ chưa có sổ → 🟡 + task "Lập sổ đối chiếu" | `intake-sync.py` | như trên |
| Bản mới (Phiên bản mới hơn `> Bản:`) → đọc bảng *Tổng quan thay đổi* trong `_changes/`: Thêm mới/Sửa → 🔄, Bỏ → ➖; task "Rà lại SRC theo bản" (Xong khi hết 🔄). Không có bảng → mọi mục đã xử lý thành 🔄 | `intake-sync.py` | như trên |
| Mục còn mở của nguồn feature trỏ tới + mục ➡ giao cho feature; exit 1 nếu còn | `source-coverage.py <feature>` | skill gọi |
| Dòng ghi sai: ✅ không có đường dẫn/đường dẫn không tồn tại, ➖ thiếu lý do | `source-coverage.py` | như trên |

```bash
python3 _scripts/source-coverage.py <feature>        # gate theo feature
python3 _scripts/source-coverage.py --source SRC-07  # 1 nguồn
python3 _scripts/source-coverage.py --all            # tổng quan
```

## 4. Claude phải làm

1. **Đọc nguồn → ghi sổ cùng lượt.** Mỗi lần đưa nội dung nguồn vào doc feature, sửa sổ trong cùng L1
   (dòng `docs-input/_coverage/{slug}.md | update | …`). Không có sổ thì lập sổ trước.
2. **Đọc hết mục, không chỉ mục đang cần.** Mục không thuộc feature đang làm vẫn phải có kết quả (➡ / ➖)
   — mục "để sau" mà không ghi là chỗ rơi.
3. **Hứa "sẽ đưa vào" chưa phải ✅.** Để ⬜ (hoặc ⏳ nếu chờ khách); thêm task backlog theo `backlog.md`.
4. **Tách/gộp feature** → chạy gate cho từng feature mới; đổi ➡ theo slug mới; mục chép từ bản gộp
   phải mở nguồn đối chiếu lại, không chép kết quả cũ.
5. **Gate trước khi đổi status.** `/brainstorm` không chuyển `in-review`/`approved` khi gate exit 1.
   `/srs` cảnh báo + hỏi (soft gate).
6. **Bản mới của khách** → `/intake` phải ghi bảng *Tổng quan thay đổi* (máy dựa vào bảng này để mở lại
   mục). Rà từng mục 🔄 rồi đổi kết quả.

## 5. Anti-patterns

- ❌ Đánh ✅ cả nguồn vì "đã đọc" mà sổ còn ⬜.
- ❌ ✅ không có Ở đâu — không kiểm lại được.
- ❌ Xoá dòng mục khỏi sổ vì "không liên quan" → ghi ➖ + lý do.
- ❌ Sửa tay cột Feed của sổ nguồn — máy ghi đè theo sổ đối chiếu.

## Tóm tắt 1 dòng

> **Tài liệu khách tính theo từng mục trong `docs-input/_coverage/` · mỗi mục có kết quả + Ở đâu/lý do ·
> bản mới tự mở lại mục đổi · gate `source-coverage.py <feature>` trước khi chốt brainstorm/SRS.**
