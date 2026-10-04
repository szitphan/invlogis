# Crosswalk: Control type (BA) → component Astryx

Tra ngược từ cột **Control type** của bảng Screen description (`# | Items | Control type | Data type |
Description`) sang component ứng viên. Bảng này chỉ để **tìm ứng viên**: chọn cuối cùng theo mục của
component trong `design/components.md` (Nên/Không nên), tên set Figma theo `design/figma-library-keys.json`.
Lệch với `components.md` thì `components.md` thắng; lệch với `design.md` thì `design.md` thắng.

## Bảng tra

| Control type (BA) | Điều kiện phân biệt (Data type / Description) | Component ứng viên | Set Figma |
|---|---|---|---|
| Textbox | 1 dòng chữ, email, mã, số điện thoại | Text Input + Field | `TextInput`, `Field` |
| Textbox | Số, có bước tăng/giảm hoặc min/max | Number Input + Field | `NumberInput`, `Field` |
| Textbox | Mật khẩu | Text Input (kiểu password) + Field | `TextInput`, `Field` |
| Textbox | Gõ để gợi ý từ danh sách | Typeahead | `Typeahead` |
| Textbox | Nhập nhiều giá trị thành thẻ | Tokenizer | `Tokenizer` |
| Textarea | Nhiều dòng | Text Area + Field | `TextArea`, `Field` |
| Dropdown | Chọn 1 trong danh sách | Selector | `Selector` |
| Dropdown | Chọn nhiều | Multi Selector | `Selector / MultiSelector` |
| Dropdown | Mục có mô tả/ảnh, tìm trong danh sách lớn | Complex Selector | `ComplexSelector` |
| Dropdown | Danh sách **hành động** (không phải giá trị) | Dropdown Menu / More Menu | `DropdownMenu`, `MoreMenu` |
| Checkbox | 1 lựa chọn đồng ý / nhiều lựa chọn độc lập | Checkbox Input | `Checkbox / CheckboxInput`, `Checkbox / CheckboxList` |
| Radio | Chọn 1, 3–7 lựa chọn cần thấy hết | Radio List | `Radio / RadioList` |
| Radio | Chọn 1, 2–4 lựa chọn ngắn, đổi chế độ xem | Segmented Control | `SegmentedControl` |
| Toggle / Switch | Bật/tắt có hiệu lực ngay | Switch | `Switch` |
| Datepicker | Ngày / khoảng ngày / ngày giờ / giờ | Date Input / Date Range Input / Date Time Input / Time Input | `DateInput`, `DateRangeInput`, `DateTimeInput`, `TimeInput` |
| Upload | Chọn hoặc kéo thả file | File Input | `FileInput` |
| Slider | Chọn giá trị trong khoảng | Slider | `Slider` |
| Button | Hành động (chính / phụ / nguy hiểm) | Button (biến thể theo vai trò) | `Button` |
| Button | Chỉ có icon | Icon Button | `Button` (Type=Icon Only) |
| Button | Nhóm hành động liên quan | Button Group | `Action / ButtonGroup` |
| Link | Điều hướng bằng chữ | Link | `Link` |
| Label | Chữ tĩnh, tiêu đề | Text / Heading | `Text`, `Heading` |
| Label | Trạng thái nghiệp vụ | Badge / Status Dot (nhóm theo *Ánh xạ trạng thái nghiệp vụ* trong `design.md`) | `Badge`, `StatusDot` |
| Label | Cặp khoá–giá trị của đối tượng | Metadata List | `MetadataList` |
| Label | Ngày giờ hiển thị | Timestamp | `Timestamp` |
| Banner | Thông báo gắn với trang/khối | Banner | `Banner` |
| Toast | Xác nhận ngắn, không chặn | Toast | `Toast` |
| Modal | Chặn tương tác đến khi phản hồi | Dialog (mobile: Bottom Sheet) | `Dialog`, `BottomSheet` |
| Popover / Tooltip | Nội dung phụ neo vào phần tử | Popover / Tooltip / Hover Card | `Popover`, `Tooltip`, `HoverCard` |
| Table | Dữ liệu hàng–cột | Table (+ Pagination khi có phân trang) | `TableHeaderCell`, `TableCell`, `Pagination` |
| List | Danh sách mục dọc / cây phân cấp | List / Tree List | `List / .ListItem`, `TreeList` |
| Tab | Chia nội dung cùng màn | Tab List | `Tabs / TabList` |
| Stepper | Tiến trình nhiều bước | Stepper | `Stepper`, `Stepper / Step` |
| Search / Filter | Bộ lọc nhiều điều kiện trên danh sách/bảng | Power Search | `PowerSearch / Trigger`, `PowerSearch / Popover` |
| Search / Filter | Ô tìm kiếm đơn | Text Input (có icon tìm) | `TextInput` |
| Card | Khối nội dung / bấm được / chọn được | Card / Clickable Card / Selectable Card | `Card`, `ClickableCard`, `SelectableCard` |
| Avatar | Ảnh đại diện người | Avatar / Avatar Group | `Avatar`, `AvatarGroup` |
| Image | Ảnh/thumbnail | Thumbnail | `Thumbnail` |
| Icon | Icon trang trí/chỉ dẫn | Icon | `Icon` |
| Loading | Đang tải | Skeleton / Spinner / Progress Bar | `Skeleton`, `Spinner`, `ProgressBar` |
| Empty state | Không có dữ liệu | Empty State | `EmptyState` |
| Navigation | Menu cấp ứng dụng / breadcrumb | Side Nav / Top Nav / Breadcrumbs | `Navigation / SideNav`, `Navigation / TopNav`, `Breadcrumbs` |

**Keys (quét lại 01/10/2026):** `figma-library-keys.json` gồm cả component đơn (Popover, Tooltip,
HoverCard, `Navigation / TopNav`, Carousel…). Tên ở dòng Figma của `components.md` không có trong keys
→ ghi gap, chờ sinh lại keys.

Control type không có trong bảng → đọc *Bảng chọn nhanh* của `components.md`; vẫn không có → ghi
gap "chưa có chuẩn trong design.md", không tự dựng component thay thế.

## Component dùng chung, hành vi theo feature

Component cho **khung**: anatomy, biến thể, state, a11y, ràng buộc. Feature cho **nội dung và hành
vi**: field nào, giá trị mặc định, toán tử, phụ thuộc giữa các field, trạng thái rỗng/lỗi, áp dụng và
xoá. Nguồn hành vi là SRS (FR/BR/Error) + cột Description của bảng Screen description.

Ví dụ bộ lọc: `PowerSearch` quy định cách hiện điều kiện, sửa từng điều kiện, xoá. Feature quy định
lọc theo cột nào, toán tử nào cho từng cột, giá trị mặc định, và thông báo khi không có kết quả.
Thiếu phần hành vi → hỏi user hoặc ghi OQ, không chép hành vi của feature khác.
