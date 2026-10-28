---
type: design-crosswalk
status: draft
updated: 2026-10-26
links:
  - design/ba-crosswalk.md
  - design/v2/components/README.md
  - design/v2/README.md
  - _workspace/decisions.md
---

# Crosswalk DS v2: Control type (BA) → mã component

> Bản DS v2 của [ba-crosswalk.md](../ba-crosswalk.md) (bản đó trỏ thư viện Astryx cũ, giữ tới vòng 6). Cột **Mã component**
> là `id` trong `handoff/components/registry.json` — cùng một mã dùng ở bảng mô tả màn của BA, trên Figma và trong code
> Angular / Flutter (DEC-255). Máy đọc bảng này sinh `handoff/crosswalk.json`; mã không có spec → script báo lỗi.
> Dòng có Mã `—` là **gap**: DS v2 chưa dựng, cột Ghi chú nêu component Astryx tạm dùng.

| Control type (BA) | Khi nào | Mã component | Ghi chú |
|---|---|---|---|
| Textbox | 1 dòng chữ, email, mã, số điện thoại, số | `l1.text-field` | |
| Textbox | Mã OTP, mã xác nhận nhiều ô (app) | `l1.otp-field` | chỉ app |
| Textbox | Gõ để gợi ý từ danh sách | — | chưa dựng; Astryx `Typeahead` |
| Textarea | Nhiều dòng | — | chưa dựng; Astryx `TextArea` |
| Dropdown | Chọn 1 / chọn nhiều trong danh sách | — | chưa dựng; Astryx `Selector` |
| Checkbox / Radio | Chọn trong vài lựa chọn hiện dạng thẻ | `l1.selectable-card` | lựa chọn có mô tả, ảnh |
| Checkbox | 1 lựa chọn đồng ý / nhiều lựa chọn độc lập | — | chưa dựng; Astryx `Checkbox` |
| Radio | Chọn 1, 3–7 lựa chọn ngắn | — | chưa dựng; Astryx `Radio / RadioList` |
| Toggle / Switch | Bật/tắt có hiệu lực ngay | — | chưa dựng; Astryx `Switch` |
| Datepicker | Ngày / khoảng ngày / giờ | — | chưa dựng; Astryx `DateInput` |
| Upload | Chọn hoặc kéo thả file | — | chưa dựng; Astryx `FileInput` |
| Button | Hành động chính / phụ / nguy hiểm, nút chỉ icon | `l1.button` | |
| Label | Trạng thái nghiệp vụ | `l1.status-chip` | nhóm màu theo bảng ánh xạ trạng thái |
| Label | Dòng trạng thái kèm thời điểm, người làm | `l1.status-row` | |
| Popover / Tooltip | Chữ giải thích neo vào phần tử | `l1.tooltip` | |
| List | Danh sách mục dọc | `l1.list-item` | |
| Card | Khối nội dung chung | `l1.card` | |
| Card | Thẻ một bản ghi (mã, trạng thái, dòng thông tin, nút) | `l1.record-card` | |
| Card | Thẻ số liệu tổng hợp | `l1.summary-card` | |
| Avatar | Ảnh đại diện người | `l1.avatar` | |
| Avatar | Nhóm người | `l1.avatar-group` | |
| Loading | Tiến độ theo bước, phần trăm | `l1.progress` | đang tách L0 `.progress / Bar` + L1 Progress Card (DEC-254) |
| Table | Dữ liệu hàng–cột | — | chưa dựng; Astryx `TableCell`, `Pagination` |
| Tab | Chia nội dung cùng màn | — | chưa dựng; Astryx `Tabs / TabList` |
| Stepper | Tiến trình nhiều bước | — | chưa dựng (BL-241) |
| Modal | Chặn tương tác đến khi phản hồi | — | chưa dựng; Astryx `Dialog`, `BottomSheet` |
| Toast / Banner | Thông báo | — | chưa dựng; Astryx `Toast`, `Banner` |
| Empty state | Không có dữ liệu | — | chưa dựng; Astryx `EmptyState` |
| Navigation | Menu ứng dụng, thanh tab app | — | chưa dựng; Astryx `Navigation / SideNav` |
