---
type: design-crosswalk
status: draft
updated: 2026-10-30
links:
  - design/ba-crosswalk.md
  - design-system/components/README.md
  - design-system/README.md
  - _workspace/decisions.md
---

# Crosswalk DS v2: Control type (BA) → mã component

> Bản DS v2 của [ba-crosswalk.md](../ba-crosswalk.md) (bản đó trỏ thư viện Astryx cũ, giữ tới vòng 6). Cột **Mã component**
> là `id` trong `handoff/components/registry.json` — cùng một mã dùng ở bảng mô tả màn của BA, trên Figma và trong code
> Angular / Flutter (DEC-255). Máy đọc bảng này sinh `handoff/crosswalk.json`; mã không có spec → script báo lỗi.
> Dòng có Mã `—` là **gap**: DS v2 chưa có mã handoff, cột Ghi chú nêu component mới đang dựng hoặc Astryx tạm dùng.
> 14 mã `l1.*` bỏ cùng tài liệu L0/L1/L2 (DEC-312); mã `base.*` / `application.*` thêm khi `ds-v2-handoff.py` đọc được hai thư mục đó.

| Control type (BA) | Khi nào | Mã component | Ghi chú |
|---|---|---|---|
| Textbox | 1 dòng chữ, email, mã, số điện thoại, số | — | đang dựng Base Inputs (`_work/input`) |
| Textbox | Mã OTP, mã xác nhận nhiều ô (app) | — | bỏ cùng L1 cũ (DEC-312), chưa có thay; chỉ app |
| Textbox | Gõ để gợi ý từ danh sách | — | chưa dựng; Astryx `Typeahead` |
| Textarea | Nhiều dòng | — | chưa dựng; Astryx `TextArea` |
| Dropdown | Chọn 1 / chọn nhiều trong danh sách | — | chưa dựng; Astryx `Selector` |
| Checkbox / Radio | Chọn trong vài lựa chọn hiện dạng thẻ | — | Radio groups kiểu Icon card (DEC-278), chưa có md; lựa chọn có mô tả, ảnh |
| Checkbox | 1 lựa chọn đồng ý / nhiều lựa chọn độc lập | — | chưa dựng; Astryx `Checkbox` |
| Radio | Chọn 1, 3–7 lựa chọn ngắn | — | chưa dựng; Astryx `Radio / RadioList` |
| Toggle / Switch | Bật/tắt có hiệu lực ngay | — | chưa dựng; Astryx `Switch` |
| Datepicker | Ngày / khoảng ngày / giờ | — | chưa dựng; Astryx `DateInput` |
| Upload | Chọn hoặc kéo thả file | — | chưa dựng; Astryx `FileInput` |
| Button | Hành động chính / phụ / nguy hiểm, nút chỉ icon | — | đang dựng Base Buttons (`_work/buttons`) |
| Label | Trạng thái nghiệp vụ | — | Base Badge (`components/base/badge.md`); nhóm màu theo bảng ánh xạ trạng thái |
| Label | Dòng trạng thái kèm thời điểm, người làm | — | bỏ cùng L1 cũ (DEC-312), chưa có thay |
| Popover / Tooltip | Chữ giải thích neo vào phần tử | — | Base Tooltip (`components/base/tooltip.md`) |
| List | Danh sách mục dọc | — | bỏ cùng L1 cũ (DEC-312), chưa có thay |
| Card | Khối nội dung chung | — | bỏ cùng L1 cũ (DEC-312), chưa có thay |
| Card | Thẻ một bản ghi (mã, trạng thái, dòng thông tin, nút) | — | bỏ cùng L1 cũ (DEC-312); Record card dựng lại ở Application (DEC-260) |
| Card | Thẻ số liệu tổng hợp | — | bỏ cùng L1 cũ (DEC-312), chưa có thay |
| Avatar | Ảnh đại diện người | — | Base Avatar (`components/base/avatar.md`) |
| Avatar | Nhóm người | — | Base Avatar (`components/base/avatar.md`) |
| Loading | Tiến độ theo bước, phần trăm | — | bỏ cùng L1 cũ (DEC-312); Progress để sau (DEC-260) |
| Table | Dữ liệu hàng–cột | — | chưa dựng; Astryx `TableCell`, `Pagination` |
| Tab | Chia nội dung cùng màn | — | chưa dựng; Astryx `Tabs / TabList` |
| Stepper | Tiến trình nhiều bước | — | chưa dựng (BL-241) |
| Modal | Chặn tương tác đến khi phản hồi | — | chưa dựng; Astryx `Dialog`, `BottomSheet` |
| Toast / Banner | Thông báo | — | chưa dựng; Astryx `Toast`, `Banner` |
| Empty state | Không có dữ liệu | — | chưa dựng; Astryx `EmptyState` |
| Navigation | Menu ứng dụng, thanh tab app | — | chưa dựng; Astryx `Navigation / SideNav` |
