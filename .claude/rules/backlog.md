# Backlog — task tự thêm, tự đóng

> Rule chung cho MỌI skill và mọi lượt làm việc. Nguồn: `docs/_shared/backlog.md` (task) +
> `docs-input/README.md` (sổ nguồn). Máy làm phần tất định (`_scripts/intake-sync.py`, hook); rule này
> phủ phần máy không tự biết: task phát sinh từ hội thoại.

## Máy tự làm (không cần nhắc)

| Sự kiện | Kết quả | Khi nào chạy |
|---|---|---|
| File mới trong `docs-input/` | Thêm dòng sổ `⬜ chưa feed` + task `BL-NNN` "Đọc và feed" | Đầu phiên, mỗi lượt user gửi tin, sau mỗi Write/Edit |
| File trong `docs-input/` đổi tên/chuyển chỗ (cùng nội dung) | Đổi đường dẫn trong sổ + task | như trên |
| Doc trong `docs/{feature}/` trỏ tới nguồn `⬜` | Nguồn → `✅ đã feed`, task feed tự đóng | như trên |
| Điều kiện cột **Xong khi** thoả | Task → `✅`, ghi ngày + bằng chứng, chuyển sang mục Đã xong | như trên |

Hook in `[intake-sync] + nguồn mới …` vào đầu lượt → đọc nguồn đó theo memory "ingest-new-client-docs",
xếp nhóm + đặt tên theo quy ước trong `docs-input/README.md` (sổ tự nhận đổi chỗ).

## Claude phải làm

1. **Thêm task** khi user nói "cần làm / để sau / nhớ xử lý X", hoặc skill kết thúc còn việc dở cấp dự án
   (bước tiếp theo đã hứa, câu hỏi mở chặn tiến độ, nguồn cần xử lý). KHÔNG thêm task cho OQ nghiệp vụ
   nằm sẵn trong doc feature — OQ sống ở doc đó.
2. **Mỗi task phải có cột Xong khi máy kiểm được** (`exists:` / `grep:` / `fed:`, `!` phủ định, `&&` nối),
   trỏ vào **output thật** của việc (file sinh ra, mã xuất hiện). Chỉ dùng `manual` khi việc là quyết định
   không để lại dấu vết file (vd chốt bản nào thay thế bản nào).
3. **Đóng task `manual`** khi việc đã xong trong hội thoại: đổi Trạng thái `✅` + Xong + Bằng chứng
   (1 câu: user chốt gì, ngày nào). Script tự chuyển dòng sang mục Đã xong.
4. **Đổi tên/di chuyển file trong `docs-input/`**: cập nhật link trong `docs/` cùng lượt (L2); sổ + backlog
   script tự theo.
5. Thêm/sửa backlog là Edit file đã tồn tại → báo 1 dòng "Đã thêm BL-NNN: … (Xong khi: …)". Không cần
   L2 diff riêng cho dòng backlog — đây là sổ theo dõi, không phải tài liệu nghiệp vụ.

## Anti-patterns

- ❌ Task không có điều kiện Xong khi (hoặc `manual` cho việc có output file) → không bao giờ tự đóng.
- ❌ Sửa tay cột *tự động* của sổ nguồn (Dùng ở / Việc mở) — lần chạy sau ghi đè.
- ❌ Tự hạ `✅ đã feed` của sổ — trạng thái do người ghi là quyết định của user.

## Tóm tắt 1 dòng

> **Máy lo nguồn mới / đổi chỗ / feed / đóng task theo điều kiện · Claude thêm task từ hội thoại, luôn kèm
> điều kiện Xong khi máy kiểm được, đóng tay chỉ task `manual`.**
