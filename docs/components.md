# Components: Hướng dẫn chọn và dùng (Astryx)

> **Nguồn:** tài liệu component của Astryx (`github.com/facebook/astryx`, `@astryxdesign/core` 0.6.3:
> `usage.description` và `bestPractices` trong `packages/core/src/**/*.doc.mjs`, cùng example trong
> `packages/cli/assets/templates/blocks/components/**`). Chia section theo https://astryx.atmeta.com/components.
> **Chỉ dịch**, không thêm ý. Component nào Astryx không có Nên/Không nên thì ghi rõ là không có.
> Trích ngày 27/09/2026: 99 component, 452 example.

**Vai trò.** `docs/design.md` vẫn là nguồn chuẩn cho token, bố cục và luật vẽ. File này bổ sung phần
*chọn component nào* và *dùng thế nào cho đúng*. Nếu hai file lệch nhau thì `design.md` thắng, và
ghi chỗ lệch vào Known Gaps.

**Cách AI dùng file này**
1. Tra **Bảng chọn nhanh** để tìm component ứng viên theo nhu cầu.
2. Đọc mục của component đó. **Nên / Không nên** là tiêu chí loại: gặp một dòng *Không nên* khớp
   tình huống thì chuyển sang component được chỉ tới trong dòng đó.
3. Chọn **Example** gần nhất làm mẫu dựng. Tên example giữ nguyên tiếng Anh để tra ngược mã nguồn.
4. Dòng **Figma** cho biết component set để `instantiate` (tên trong `docs/figma-library-keys.json`).
   Các prop code (`presentation`, `xstyle`, `renderCell`…) chỉ áp khi viết code; khi vẽ Figma, bỏ
   qua phần kỹ thuật và giữ ý về hành vi.

**Trang Figma.** Mỗi section dưới đây là một trang cùng tên trong file thư viện, theo đúng thứ tự
11 section của Astryx: Action · Chat · Container · Content · Feedback & Status · Form Controls ·
Layout · Navigation · Overlay · Table & List · Utility (trang *Data Input* cũ đổi thành *Form Controls*).
Trang *Utility* chỉ có khung hướng dẫn của VisuallyHidden, không có component vì không có hình.
Trong file dự án (Cách B), 11 trang này nằm dưới dòng `——— 02 · COMPONENTS ———` (nhóm DESIGN SYSTEMS), xem *Cấu trúc trang
file dự án* trong `setup-figma.md`.

**Example trên Figma (cập nhật 28/09/2026).** Mỗi example trong bảng **Examples** là một frame
`Block — <tên example>` (Header / Description / Preview) nằm dưới khung `Hướng dẫn · <Component>`,
mô tả và chữ trong preview bằng tiếng Việt, dựng từ instance thật của thư viện. Tên Block giữ nguyên
tên example tiếng Anh để tra được hai chiều. Trang Chat gom mọi component vào một khung, nên Block
nằm trong nhóm `Examples · <Component>` ngay dưới hướng dẫn của component đó.
Thứ tự Block trong mỗi component giống thứ tự bảng **Examples** ở file này. Example nào Astryx không
có mô tả (thường là example mặc định trùng tên component, như `Grid`, `Selector`) thì không có trong
bảng và không có Block.

## Bảng chọn nhanh

**Action**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Button](#button) | Button kích hoạt một hành động khi được bấm. | `Button` |
| [Button Group](#button-group) | ButtonGroup gộp các hành động liên quan thành một control liền khối. | `Action / ButtonGroup` |
| [Dropdown Menu](#dropdown-menu) | Menu thả xuống hiển thị danh sách mục hành động trong một popup mở từ một nút. | `DropdownMenu` (+ `DropdownMenuItem`, `DropdownMenuCheckboxItem`, `DropdownMenuRadioItem`) |
| [Icon Button](#icon-button) | Nút chỉ hiện icon, không có chữ. | `Button` (Type=Icon Only) |
| [Link](#link) | Thẻ liên kết đã tạo kiểu cho điều hướng bằng chữ, nằm trong đoạn văn hoặc đứng riêng. | `Link` |
| [More Menu](#more-menu) | MoreMenu là nút ba chấm mở ra danh sách hành động. | `MoreMenu` |
| [Segmented Control](#segmented-control) | Nhóm nút phân đoạn cho phép chọn một trong một tập nhỏ các lựa chọn loại trừ nhau. | `SegmentedControl`, `SegmentedControl / SegmentedControlItem` |
| [Toggle Button](#toggle-button) | ToggleButton chuyển giữa trạng thái được chọn và không được chọn để biểu diễn một lựa chọn bật/tắt kéo dài. | `Button / ToggleButton` |
| [Toggle Button Group](#toggle-button-group) | Nhóm các toggle button cho hành vi chọn một (loại trừ) hoặc chọn nhiều. | chưa có set riêng — xếp các `Button / ToggleButton` cạnh nhau |
| [Toolbar](#toolbar) | Toolbar là thanh ngang có ba vùng trái, giữa, phải. | `Toolbar` |

**Chat**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Chat Composer](#chat-composer) | ChatComposer là khung nhập tin nhắn của một giao diện chat. | `Chat / ChatComposer` |
| [Chat Layout](#chat-layout) | ChatLayout là khung bố cục cho giao diện chat toàn trang. | `Chat / ChatLayout` (khung bố cục); nút cuộn: `Chat / ChatLayoutScrollButton` |
| [Chat Message](#chat-message) | Lớp bọc ngữ cảnh người gửi | `Chat / ChatMessage` |
| [Chat Message Metadata](#chat-message-metadata) | Đặt ChatMessageMetadata dưới tin nhắn hoặc trong slot metadata của ChatMessageBubble cuối để hiện thời gian, nội dung chân và trạng thái gửi (tùy chọn). | `Chat / ChatMessageMetadata` |
| [Chat System Message](#chat-system-message) | Dùng ChatSystemMessage cho nội dung ngắn, không thuộc người gửi nào, trong bản ghi chat. | `Chat / ChatSystemMessage` |
| [Chat Tool Calls](#chat-tool-calls) | ChatToolCalls hiển thị các lần gọi công cụ/hàm trong câu trả lời của LLM. | `Chat / ChatToolCalls` |

**Container**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Card](#card) | Card là vùng chứa có viền, có thể nâng, dành cho các mục rời rạc, tự đủ nghĩa | `Card` |
| [Carousel](#carousel) | Carousel cuộn ngang một hàng mục khi chúng tràn bề rộng sẵn có. | `Carousel` |
| [Clickable Card](#clickable-card) | Card tương tác làm đích điều hướng hoặc hành động. | `ClickableCard` |
| [Collapsible](#collapsible) | Collapsible ẩn và hiện nội dung sau một nút kích hoạt. | `Collapsible` |
| [Selectable Card](#selectable-card) | Card chuyển giữa trạng thái được chọn và không được chọn, có viền màu nhấn. | `SelectableCard` |

**Content**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Avatar](#avatar) | Avatar đại diện cho một người hoặc nhóm bằng ảnh đại diện, chữ viết tắt hoặc icon mặc định. | `Avatar` |
| [Avatar Group](#avatar-group) | AvatarGroup hiển thị nhiều avatar trong một hàng chồng lên nhau, có chỉ báo phần tràn (tùy chọn). | `AvatarGroup` |
| [Blockquote](#blockquote) | Khối trích dẫn có đường kẻ ở mép đầu dòng và chữ màu phụ. | `Blockquote` |
| [Citation](#citation) | Citation hiển thị tham chiếu trong dòng tới nguồn bên ngoài. | `Citation` |
| [Code](#code) | Phần tử code trong dòng. | `Code` |
| [Code Block](#code-block) | CodeBlock hiển thị code tô màu cú pháp với số dòng, nút sao chép và phần thu gọn tùy chọn. | `CodeBlock` |
| [Empty State](#empty-state) | EmptyState hiển thị nội dung giữ chỗ khi một vùng nội dung không có dữ liệu. | `EmptyState` |
| [Heading](#heading) | Component heading có ngữ nghĩa, hiển thị phần tử h1–h6 với kiểu theo theme, cỡ theo token thang chữ, và cắt dòng bằng line-clamp. | `Heading` |
| [Icon](#icon) | Icon là ký hiệu hình nhỏ đại diện cho hành động, đối tượng hoặc khái niệm. | `Icon` (trang Icons) |
| [Kbd](#kbd) | Hiển thị phím tắt dưới dạng badge phím. | `Kbd` |
| [Markdown](#markdown) | Hiển thị chuỗi markdown thành các component theo kiểu Astryx. | `Markdown` |
| [Text](#text) | Text hiển thị chữ thân và heading theo kiểu của theme. | `Text` |
| [Thumbnail](#thumbnail) | Thumbnail hiển thị bản xem trước vuông, gọn của một ảnh đính kèm. | `Thumbnail` |
| [Timestamp](#timestamp) | Timestamp định dạng giá trị ngày hoặc giờ thành chữ dễ đọc. | `Timestamp` |
| [Token](#token) | Token là phần tử nhỏ trong dòng biểu diễn các mẩu dữ liệu liên quan rời rạc, như thẻ, danh mục hoặc lựa chọn. | `Token` |

**Feedback & Status**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Badge](#badge) | Badge làm nổi một trạng thái hoặc danh mục trong nháy mắt. | `Badge` |
| [Banner](#banner) | Banner hiển thị thông điệp cố định ở đầu trang hoặc đầu một phần. | `Banner` |
| [Progress Bar](#progress-bar) | Thanh ngang thể hiện tiến độ hoàn thành của một tác vụ. | `ProgressBar` |
| [Skeleton](#skeleton) | Khối giữ chỗ có hiệu ứng shimmer, xem trước hình dạng nội dung khi đang tải. | `Skeleton` |
| [Spinner](#spinner) | Chỉ báo đang tải có hiệu ứng cho tiến trình không rõ thời lượng, như lấy dữ liệu hoặc gửi form. | `Spinner` |
| [Status Dot](#status-dot) | Chấm màu nhỏ truyền tải trạng thái như trực tuyến/ngoại tuyến hoặc mức độ nghiêm trọng. | `StatusDot` |

**Form Controls**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Calendar](#calendar) | Calendar cho người dùng chọn một ngày hoặc khoảng ngày trên lưới tháng. | `Calendar` |
| [Checkbox Input](#checkbox-input) | CheckboxInput bật/tắt một giá trị đơn. | `Checkbox / CheckboxInput` (nhóm: `Checkbox / CheckboxList`) |
| [Complex Selector](#complex-selector) | Dùng ComplexSelector khi một lựa chọn cần nội dung tùy biến phong phú hơn một dòng lựa chọn của Selector. | `ComplexSelector` |
| [Date Input](#date-input) | DateInput cho người dùng gõ hoặc chọn ngày từ popover lịch. | `DateInput` |
| [Date Range Input](#date-range-input) | DateRangeInput cho người dùng chọn ngày bắt đầu và kết thúc từ popover lịch hai tháng. | `DateRangeInput` |
| [Date Time Input](#date-time-input) | DateTimeInput gộp chọn ngày và giờ trong một trường. | `DateTimeInput` |
| [Field](#field) | Field là lớp bọc cấp thấp cho control tùy biến, gốc hoặc bên thứ ba chưa có sẵn nhãn, mô tả và giao diện trạng thái. | `Field` |
| [File Input](#file-input) | FileInput cho tải tệp lên, hỗ trợ kéo thả (tùy chọn). | `FileInput` |
| [Multi Selector](#multi-selector) | Dropdown có checkbox để chọn nhiều giá trị từ một danh sách. | `Selector / MultiSelector` |
| [Number Input](#number-input) | Input form cho giá trị số, có sẵn kiểm tra, ràng buộc min/max và nút bước. | `NumberInput` |
| [Power Search](#power-search) | PowerSearch là thanh lọc có cấu trúc, mỗi token biểu diễn một trường, toán tử và giá trị. | `PowerSearch / Popover`, `PowerSearch / Trigger` |
| [Radio List](#radio-list) | Nhóm lựa chọn chỉ chọn được một tại một thời điểm. | `Radio / RadioList` |
| [Selector](#selector) | Dropdown chọn một giá trị từ danh sách lựa chọn. | `Selector` |
| [Slider](#slider) | Control kéo được để chọn một giá trị số hoặc một khoảng trong biên xác định. | `Slider` |
| [Switch](#switch) | Control bật/tắt cho trạng thái có hiệu lực ngay. | `Switch` |
| [Text Area](#text-area) | TextArea là ô nhập chữ nhiều dòng để thu nội dung dài như bình luận, mô tả hay tin nhắn. | `TextArea` |
| [Text Input](#text-input) | TextInput thu chữ ngắn như tên, email hoặc truy vấn tìm kiếm. | `TextInput` |
| [Time Input](#time-input) | TimeInput mặc định dùng bộ chọn giờ của trình duyệt/hệ điều hành trên con trỏ thô và trường gõ của Astryx trên con trỏ mịn. | `TimeInput` |
| [Tokenizer](#tokenizer) | Tokenizer là input chọn nhiều cho phép tìm, chọn và quản lý nhiều mục hiển thị dưới dạng chip gỡ được. | `Tokenizer` |
| [Typeahead](#typeahead) | Ô nhập tìm kiếm được để chọn một mục từ tập dữ liệu lớn hoặc động. | `Typeahead` |
| [Typeahead Item](#typeahead-item) | Bộ hiển thị mục dropdown mặc định cho kết quả typeahead. | không có set riêng — là dòng kết quả trong `Typeahead` |

**Layout**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [App Shell](#app-shell) | AppShell là khung trang của một ứng dụng. | `AppShell` |
| [Aspect Ratio](#aspect-ratio) | Giữ tỉ lệ rộng/cao cố định cho phần tử con khi vùng chứa đổi cỡ. | `AspectRatio` |
| [Divider](#divider) | Đường phân cách trực quan chia nội dung thành các phần riêng. | `Divider` |
| [Form Layout](#form-layout) | Vùng chứa bố cục sắp xếp các trường form với khoảng cách và hướng nhất quán. | `Layout / FormLayout` |
| [Grid](#grid) | Vùng chứa bố cục CSS grid để xếp phần tử con theo hàng và cột. | không có set — dựng bằng auto layout (wrap) / layout grid |
| [Layout](#layout) | Layout là primitive năm slot tổng quát để sắp xếp các vùng header, start, content, end và footer trong một trang hoặc vùng chứa có biên. | không có set — dựng bằng auto layout |
| [Resize Handle](#resize-handle) | Thanh phân cách kéo được giữa các panel. | `ResizeHandle` |
| [Scrollable Area](#scrollable-area) | Cung cấp một viewport cuộn gốc và một hộp nội dung thật được theo dõi. | không có set — frame có clip content + cuộn |
| [Section](#section) | Section là cách đúng để tạo các vùng trang và nhóm nội dung liên quan trên trang. | `Layout / Section` |
| [Stack](#stack) | Stack xếp các mục theo hàng hoặc cột với khoảng cách nhất quán. | không có set — dựng bằng auto layout |

**Navigation**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Breadcrumbs](#breadcrumbs) | Breadcrumbs hiển thị chuỗi liên kết từ gốc tới trang hiện tại. | `Breadcrumbs`, `Breadcrumbs / BreadcrumbItem` |
| [Outline](#outline) | Sidebar mục lục cho trang tài liệu, trung tâm trợ giúp, wiki và trang cài đặt dài. | `Outline` (+ `.OutlineItem`) |
| [Pagination](#pagination) | Pagination cho người dùng đi qua các trang nội dung. | `Pagination` |
| [Side Nav](#side-nav) | Component điều hướng sidebar để tổ chức các trang ứng dụng với section, mục lồng và icon. | `Navigation / SideNav` (+ `.SideNavItem`, `.SideNavHeading`) |
| [Stepper](#stepper) | Stepper hiển thị tiến trình qua một chuỗi bước logic có đánh số. | `Stepper` (+ `Stepper / Step`) |
| [Tab List](#tab-list) | TabList cung cấp điều hướng dạng tab để tổ chức nội dung thành các phần phân loại. | `Tabs / TabList`, `Tabs / .Tab` |
| [Top Nav](#top-nav) | TopNav là thanh điều hướng ngang cho điều hướng cấp sản phẩm ở header ứng dụng. | `Navigation / TopNav` (+ `Navigation / TopNavHeading`, `Navigation / .TopNavItem`) |
| [Top Nav Mega Menu](#top-nav-mega-menu) | Mục điều hướng hiện panel mega menu tràn bề rộng khi hover. | `Navigation / TopNavMegaMenu`, `Navigation / .TopNavMegaMenuItem` |
| [Top Nav Mega Menu Featured Card](#top-nav-mega-menu-featured-card) | Card nổi bật chuẩn cho slot featured của TopNavMegaMenu. | `Navigation / .TopNavMegaMenuFeaturedCard` |
| [Top Nav Menu](#top-nav-menu) | Mục điều hướng hiện menu popover mở khi hover, gồm các mục phong phú có icon, tiêu đề và mô tả (tùy chọn). | `Navigation / TopNavMenu` |

**Overlay**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [Bottom Sheet](#bottom-sheet) | Bề mặt cảm ứng di động cho bộ lọc, hành động, form và màn chi tiết, trượt lên từ đáy viewport | `BottomSheet` |
| [Bottom Sheet Switcher](#bottom-sheet-switcher) | Điều phối luồng bottom sheet nhiều bước trong một hộp thoại dùng chung | không có set — nhiều khung `BottomSheet` nối bằng luồng |
| [Command Palette](#command-palette) | CommandPalette là hộp thoại tìm kiếm được để truy cập nhanh lệnh, điều hướng và hành động. | `CommandPalette` (+ `.CommandPaletteItem`) |
| [Dialog](#dialog) | Dialog hiển thị lớp phủ modal chặn tương tác với trang cho tới khi người dùng phản hồi. | `Dialog` |
| [Hover Card](#hover-card) | HoverCard hiện thông tin bổ sung khi người dùng hover hoặc focus vào phần tử kích hoạt. | `HoverCard` |
| [Lightbox](#lightbox) | Lớp phủ toàn màn để xem ảnh và video ở độ phân giải đầy đủ. | `Lightbox` |
| [Overlay](#overlay) | Overlay phủ nội dung hành động hoặc hỗ trợ lên media, card, video hoặc bề mặt có biên khác, có nền mờ và hành vi hiện ra (tùy chọn). | `Overlay` |
| [Popover](#popover) | Lớp phủ mở bằng cú bấm, neo vào một nút hoặc phần tử kích hoạt. | `Popover` |
| [Toast](#toast) | Toast hiện thông báo ngắn, không chặn, để xác nhận một hành động hoặc đưa thông tin tạm thời. | `Toast` |
| [Tooltip](#tooltip) | Gợi ý chữ ngắn hiện khi hover hoặc focus, neo vào phần tử kích hoạt. | `Tooltip` |

**Table & List**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [List](#list) | Tập mục theo chiều dọc với khoảng cách, divider nhất quán và dấu đầu dòng (tùy chọn). | `List / .ListItem`, `Item` |
| [Metadata List](#metadata-list) | MetadataList hiển thị cặp khóa–giá trị cho thuộc tính đối tượng như chất lượng, tình trạng, trạng thái, theo bố cục có cấu trúc. | `MetadataList` |
| [Overflow List](#overflow-list) | Danh sách ngang tự ẩn mục khi vượt bề rộng sẵn có. | `OverflowList` |
| [Table](#table) | Table hiển thị dữ liệu có cấu trúc theo hàng và cột với số chiều nhất quán. | `TableHeaderCell`, `TableCell` |
| [Tree List](#tree-list) | Cấu trúc cây mở rộng được để hiển thị dữ liệu phân cấp với đường nối nhánh. | `TreeList` |

**Utility**

| Component | Dùng khi (câu đầu của Usage) | Figma |
|---|---|---|
| [VisuallyHidden](#visuallyhidden) | Hiển thị nội dung trong cây trợ năng nhưng ẩn về hình. | không vẽ (không có hình) |

---

# Action

## Button

`Button` · Figma: `Button` · trang **Action**

**Usage.** Button kích hoạt một hành động khi được bấm. Dùng cho gửi form, xác nhận, điều hướng, hoặc bất kỳ tương tác nào cần một lời kêu gọi hành động rõ ràng.

**Nên**

- ✅ Dành Primary cho hành động quan trọng nhất duy nhất trên màn. Các hành động khác dùng Secondary hoặc Ghost tùy mức nhấn mạnh.
- ✅ Viết nhãn mô tả hành động ("Lưu thay đổi", "Xóa tài khoản", "Gửi lời mời"), không dùng nhãn mơ hồ như "OK" hay "Bấm vào đây".
- ✅ Hiện trạng thái đang tải cho hành động mất thời gian, như lưu hay gửi, để người dùng biết hệ thống đang xử lý.
- ✅ Luôn có nhãn cho nút chỉ có icon để trình đọc màn hình đọc được nút làm gì. Thêm tooltip cho người nhìn thấy.
- ✅ Nút chỉ có icon thì dùng IconButton ('@astryxdesign/core/IconButton'). Đây là component riêng, không export từ '@astryxdesign/core/Button'.

**Không nên**

- ❌ Đặt nhiều hơn một nút Primary trên cùng một màn; điều này làm loãng thứ bậc thị giác.
- ❌ Dùng biến thể Destructive mà không có bước xác nhận cho hành động không hoàn tác được, như xóa dữ liệu.
- ❌ Dùng nút để điều hướng. Nếu chỉ đưa người dùng sang trang khác thì dùng Link. Nút dành cho hành động như lưu, xóa, gửi.

**Examples**

| Example | Mô tả |
|---|---|
| Button — Floating | Nút hành động nổi được nâng bằng `elevation="med"`. Dùng elevation cho nút nằm nổi trên nội dung, như FAB. |
| Button — Variants | Cả bốn biến thể đặt cạnh nhau: primary, secondary, ghost và destructive. Bảng tham chiếu nhanh để chọn đúng biến thể. |
| Button — Sizes | Nút nhỏ, vừa, lớn đặt cạnh nhau. Nhỏ cho giao diện dày đặc như toolbar, vừa cho đa số trường hợp, lớn cho CTA nổi bật. |
| Button — Variants | Cả 4 biến thể ở trạng thái mặc định, vô hiệu và đang tải. Primary cho hành động chính, Secondary cho phần lớn hành động khác, Ghost cho mức nhấn thấp, Destructive cho hành động nguy hiểm. |
| Button — End Slot | Nút có badge ở cuối hiển thị số đếm hoặc trạng thái. Dùng cho số thông báo, tin chưa đọc, hoặc nút cần một chỉ báo trực quan. |
| Button — Icon | Nút có icon đầu củng cố cho nhãn. Dùng khi icon giúp người dùng nhận ra hành động nhanh hơn, như dấu cộng cho "Mới" hay thùng rác cho "Xóa". |

## Button Group

`ButtonGroup` · Figma: `Action / ButtonGroup` · trang **Action**

**Usage.** ButtonGroup gộp các hành động liên quan thành một control liền khối. Dùng khi nhiều nút là các lựa chọn hoặc thao tác liên quan, nên đi liền nhau về thị giác, như sao chép/cắt/dán hay hoàn tác/làm lại.

**Nên**

- ✅ Gộp các nút thực hiện hành động liên quan trên cùng một đối tượng, như sao chép, cắt, dán trên đoạn chữ đang chọn.
- ✅ Dùng cùng một biến thể cho mọi nút trong nhóm để chúng trông như một khối liền.
- ✅ Giữ nhóm nhỏ (2–4 nút). Nhiều hành động hơn thì dùng Toolbar hoặc DropdownMenu.
- ✅ Đặt tên nhóm theo đối tượng mà các nút tác động. Nhãn này là tên truy cập của nhóm và trình đọc màn hình đọc nó trước mỗi nút.
- ✅ Giữ cả nhóm là một điểm dừng Tab. Phím mũi tên di chuyển giữa các nút theo hướng của nhóm, Home/End nhảy về hai đầu, nút bị vô hiệu thì bỏ qua (kỹ thuật roving tabindex của WAI-ARIA APG).

**Không nên**

- ❌ Trộn các hành động rất khác nhau. Nút Lưu cạnh nút Xóa trong cùng nhóm gây khó hiểu.
- ❌ Dùng ButtonGroup để điều hướng. Chuyển giữa các view thì dùng SegmentedControl hoặc TabList.
- ❌ Lồng ButtonGroup vào nhau. Cần nhiều nhóm thì đặt cạnh nhau có khoảng cách.
- ❌ Vô hiệu cả nhóm để báo một hành động đang chạy. Nút bị vô hiệu làm mất focus, người dùng bàn phím bị lạc chỗ; hãy để nhóm bật và hiện tiến trình trên chính nút đã khởi động việc đó.

**Examples**

| Example | Mô tả |
|---|---|
| ButtonGroup — Basic | Ba hành động liên quan gộp thành một control liền khối. Có nhãn nhóm cho trợ năng và giữ mọi nút cùng biến thể để đọc như một khối. |
| ButtonGroup — Floating | Thanh hành động dạng nhóm được nâng bằng `elevation="med"`. Các nút liền nhau dùng chung một bề mặt nên bóng nâng cả khối. |

## Dropdown Menu

`DropdownMenu` · Figma: `DropdownMenu` (+ `DropdownMenu / DropdownMenuItem`, `DropdownMenu / DropdownMenuCheckboxItem`, `DropdownMenu / DropdownMenuRadioItem`, `DropdownMenu / DropdownMenuRadioGroup`) · trang **Action**

**Usage.** Menu thả xuống hiển thị danh sách mục hành động trong một popup mở từ một nút. Dùng để đưa ra các lựa chọn hành động như bước tiếp theo của một quy trình, hoặc cung cấp hành động theo ngữ cảnh mà không làm rối giao diện.

**Nên**

- ✅ Giữ mục menu ngắn gọn, hướng hành động để người dùng lướt nhanh.
- ✅ Dùng section và divider để nhóm hành động liên quan khi menu có nhiều mục.
- ✅ Với một tập hành động ngắn, phẳng, dùng presentation="bottom-sheet" khi chính sách sản phẩm yêu cầu bề mặt cảm ứng dạng modal.
- ✅ Dùng presentation="adaptive" khi cùng một tập hành động ngắn cần neo cạnh nút trên giao diện chuột và chuyển thành BottomSheet trên giao diện cảm ứng nhỏ.
- ✅ Với cấu trúc phân cấp không thể hiện bằng các flyout cạnh nhau trên màn cảm ứng nhỏ, sản phẩm có thể chủ động dùng kiểu "đi sâu" (drill-in) kèm hành động Quay lại.
- ✅ Chọn presentation rõ ràng trong code sản phẩm. Media query "màn nhỏ, con trỏ thô, không hover" là một chính sách hữu ích, nhưng DropdownMenu không áp đặt một breakpoint thiết bị chung.
- ✅ Khi nội dung không còn là một danh sách ngắn các hành động tức thì, hãy đánh giá lại tương tác và chọn component khớp với tác vụ thực tế; chỉ đặc điểm nội dung không quyết định component.

**Không nên**

- ❌ Dùng DropdownMenu để điều hướng; dùng component điều hướng.
- ❌ Đặt quá 10–12 mục trong một menu mà không chia section.

**Examples**

| Example | Mô tả |
|---|---|
| DropdownMenu — Actions | Menu hành động có divider tách thao tác an toàn và thao tác phá hủy. Dùng cho hành động theo dòng trên tài liệu, dự án, bản ghi. |
| DropdownMenu — Adaptive presentation | Chọn bottom sheet trên màn cảm ứng nhỏ và popover neo cạnh nút trong các trường hợp khác. Media query là chính sách sản phẩm, còn DropdownMenu lo cả hai cách hiển thị. |
| DropdownMenu — Icon Trigger | Menu tràn mở từ nút chỉ có icon, không chevron, không chữ. Dùng cho hành động theo dòng trong bảng, card, danh sách khi nút chữ tốn chỗ. |
| Dropdown Menu | Nút mở menu thả xuống với các mục hành động. Menu mở sẵn để xem trước. |
| DropdownMenu — Disabled | Menu có một số mục bị vô hiệu theo quyền. Dùng khi một số hành động cần quyền cao hơn, như thao tác chỉ dành cho admin. |
| DropdownMenu — Sections | Mục menu chia thành các section có tiêu đề để dễ lướt. Dùng khi có từ 6 hành động trở lên thuộc các nhóm rõ ràng, như Tạo mới và Quản lý. |
| DropdownMenu — Submenu | Menu hành động có submenu lồng. Hover hoặc mũi tên Phải mở flyout; mũi tên Trái / Escape đóng lại. Dùng để nhóm các đích đến hoặc hành động phụ liên quan mà không làm chật cấp trên cùng. |

## Icon Button

`IconButton` · Figma: `Button` (Type=Icon Only) · trang **Action**

**Usage.** Nút chỉ hiện icon, không có chữ. Dùng IconButton trong toolbar, dòng bảng và giao diện gọn khi chỗ hẹp và icon được hiểu phổ biến.

**Nên**

- ✅ Viết aria-label cụ thể: icon thùng rác có nhãn "Xóa cuộc trò chuyện" rõ hơn chỉ "Xóa" với trình đọc màn hình.
- ✅ Thêm tooltip: ngay cả icon bánh răng cũng có thể nghĩa là Cài đặt, Tùy chọn hay Cấu hình.
- ✅ Dùng Ghost trong toolbar và vùng dày đặc để giảm rối mắt.

**Không nên**

- ❌ Dùng IconButton khi chỉ nhìn icon không rõ hành động; hãy dùng Button có chữ.
- ❌ Bỏ tooltip; label chỉ đến được trình đọc màn hình, người nhìn thấy cần gợi ý khi hover.

**Examples**

| Example | Mô tả |
|---|---|
| IconButton — Action Bar | Hàng icon button Ghost làm thanh công cụ gọn. |
| IconButton — Floating | Nút hành động nổi (FAB). Dạng nút nổi phổ biến nhất là chỉ có icon. Nâng bằng `elevation="high"`. |
| IconButton — Loading State | Icon button hiện spinner khi bấm để phản hồi thao tác bất đồng bộ. |
| Icon Button | Icon button với icon cờ lê. |
| IconButton — With Tooltips | Icon button có tooltip giải thích từng hành động khi hover. |

## Link

`Link` · Figma: `Link` · trang **Action**

**Usage.** Thẻ liên kết đã tạo kiểu cho điều hướng bằng chữ, nằm trong đoạn văn hoặc đứng riêng. Hỗ trợ liên kết ngoài, biến thể gạch chân, tooltip và component liên kết tùy biến để tích hợp router. Dùng để điều hướng giữa các trang hoặc tới URL bên ngoài.

**Nên**

- ✅ Viết chữ liên kết ngắn gọn, mô tả rõ đích đến.
- ✅ Đặt `isStandalone` khi liên kết nằm ngoài đoạn văn để nhận cỡ chữ cơ sở phù hợp.
- ✅ Chỉ đặt `label` khi nội dung liên kết không phải chữ mô tả (ví dụ liên kết chỉ có icon). Với liên kết chữ, chữ hiển thị đã là tên truy cập; thêm `label` sẽ ghi đè với trình đọc màn hình, gây hại.

**Không nên**

- ❌ Dùng Link cho hành động không điều hướng; dùng Button.
- ❌ Dùng chữ chung chung như "bấm vào đây" hay "xem thêm"; hãy mô tả đích đến.
- ❌ Đặt `label` cho liên kết chữ; `aria-label` khiến công nghệ hỗ trợ không đọc được nội dung thật của liên kết.

**Examples**

| Example | Mô tả |
|---|---|
| Link — External Links | Danh sách dọc các liên kết ngoài mở tab mới, có icon chỉ báo. |
| Link — Inline Text | Liên kết nằm trong một đoạn văn bản thân. |
| Link | Một liên kết đứng riêng. |
| Link — With Tooltips | Hàng ngang các liên kết đứng riêng có tooltip mô tả khi hover. |

## More Menu

`MoreMenu` · Figma: `MoreMenu` · trang **Action**

**Usage.** MoreMenu là nút ba chấm mở ra danh sách hành động. Dùng cho hành động phụ không cần luôn hiển thị, như trong dòng bảng, đầu card hoặc toolbar.

**Nên**

- ✅ Dùng cho hành động tràn hoặc hành động phụ; giữ hành động chính hiển thị bên ngoài menu.
- ✅ Dùng divider hoặc section để nhóm hành động liên quan khi menu có nhiều mục.
- ✅ Dùng `presentation="adaptive"` khi nút tràn cần mở BottomSheet vừa tầm ngón cái trên thiết bị cảm ứng nhỏ.

**Không nên**

- ❌ Giấu hành động chính trong MoreMenu; chúng phải hiển thị trực tiếp.

**Examples**

| Example | Mô tả |
|---|---|
| MoreMenu — Bottom Sheet | Nút tràn mở các hành động trong BottomSheet. Dùng cách hiển thị này cho tập hành động ngắn trên màn cảm ứng nhỏ. |
| MoreMenu — Default | Menu ba chấm cơ bản với các mục hành động chỉ có chữ. |
| More Menu | Menu ba chấm cơ bản với các mục hành động đơn giản. |
| MoreMenu — With Dividers | Menu ba chấm có divider tách hành động phá hủy khỏi hành động an toàn. |
| MoreMenu — With Sections | Menu ba chấm với các hành động chia thành nhóm có nhãn. |

## Segmented Control

`SegmentedControl` · Figma: `SegmentedControl`, `SegmentedControl / SegmentedControlItem` · trang **Action**

**Usage.** Nhóm nút phân đoạn cho phép chọn một trong một tập nhỏ các lựa chọn loại trừ nhau. Dùng SegmentedControl khi mọi lựa chọn cần hiển thị cùng lúc và lựa chọn điều khiển một giá trị hoặc chế độ, không phải điều hướng trang.

**Nên**

- ✅ Dùng để chuyển giữa 2–5 view hoặc chế độ loại trừ nhau, khi mọi lựa chọn cần hiển thị.
- ✅ Có nhãn mô tả cho control để nhóm truy cập được với trình đọc màn hình.

**Không nên**

- ❌ Dùng để điều hướng cấp trang; dùng TabList. TabList là component điều hướng, còn SegmentedControl là input luôn có đúng một lựa chọn được chọn.
- ❌ Dùng cho trạng thái bật/tắt đơn giản; dùng ToggleButton. ToggleButton bật/tắt độc lập, còn SegmentedControl buộc chọn một trong nhóm.
- ❌ Bọc SegmentedControl bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| SegmentedControl — Disabled Item | SegmentedControl có một lựa chọn bị vô hiệu riêng cho lựa chọn không khả dụng. |
| SegmentedControl — Fill Layout | SegmentedControl giãn các phân đoạn đều nhau lấp đầy bề rộng, hữu ích trong vùng chứa có bề rộng cố định. |
| SegmentedControl — Icon Only | SegmentedControl gọn, ẩn nhãn, chỉ hiện icon cho bố cục hẹp. |
| SegmentedControl — With Icons | SegmentedControl có cặp icon và nhãn làm bộ chuyển chế độ xem. |

## Toggle Button

`ToggleButton` · Figma: `Button / ToggleButton` · trang **Action**

**Usage.** ToggleButton chuyển giữa trạng thái được chọn và không được chọn để biểu diễn một lựa chọn bật/tắt kéo dài. Dùng riêng lẻ cho hành động nhị phân như in đậm, tắt tiếng, yêu thích, hoặc trong ToggleButtonGroup cho control toolbar chọn một hoặc chọn nhiều.

**Nên**

- ✅ Dùng icon tô đặc hoặc có màu cho trạng thái đang nhấn để người dùng thấy ngay trạng thái hiện tại, ví dụ ngôi sao viền và ngôi sao đặc.
- ✅ Giữ nhãn giống hệt giữa trạng thái nhấn và không nhấn. Để phần thể hiện thị giác (icon, độ đậm, nền) truyền tải thay đổi.
- ✅ Bọc các toggle liên quan trong ToggleButtonGroup có nhãn truy cập để trình đọc màn hình đọc chúng như một tập liền.

**Không nên**

- ❌ Dùng ToggleButton cho hành động một lần như "Gửi" hay "Xóa"; đó là Button thường, không phải toggle.
- ❌ Trộn ToggleButton với Button thường trong cùng nhóm; ToggleButtonGroup chỉ chứa ToggleButton.
- ❌ Dùng ToggleButton cho cài đặt bật/tắt được lưu qua các phiên; dùng Switch, vốn truyền tải nghĩa "cài đặt" tốt hơn.

**Examples**

| Example | Mô tả |
|---|---|
| ToggleButton — Color | Toggle button có icon màu khi nhấn. Minh họa toolbar định dạng dùng màu nhấn và màu phản ứng theo ngữ nghĩa (sao vàng, tim đỏ, bookmark xanh). |
| ToggleButton — Icon Swap | Toggle button chỉ có icon, đổi giữa icon viền và icon đặc khi nhấn. Dùng cho yêu thích, bookmark, tắt tiếng, khi chính icon truyền tải trạng thái. |
| ToggleButton — Label | Toggle button có nhãn chữ, đổi độ đậm chữ khi nhấn. Dùng khi chỉ icon không đủ truyền tải hành động. |
| ToggleButton — States | Trạng thái mặc định, đang nhấn, vô hiệu và đang tải của toggle button đứng riêng. Cho thấy phần thể hiện thị giác thay đổi qua từng trạng thái. |

## Toggle Button Group

`ToggleButtonGroup` · Figma: chưa có set riêng — xếp các `Button / ToggleButton` cạnh nhau · trang **Action**

**Usage.** Nhóm các toggle button cho hành vi chọn một (loại trừ) hoặc chọn nhiều. Dùng discriminated union trên `type` để value/onChange an toàn kiểu.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| Toggle Button Group | ToggleButtonGroup quản lý một tập ToggleButton với hành vi chọn một hoặc chọn nhiều, cho các lựa chọn như chế độ xem hay bộ lọc. |
| ToggleButtonGroup — Vertical | ToggleButtonGroup xếp dọc theo hướng vertical, minh họa cả chọn một và chọn nhiều; hợp với danh sách lựa chọn kiểu sidebar và toolbar dọc. |
| ToggleButton — Group | Nhóm toggle button ở chế độ chọn một và chọn nhiều. Chọn một đóng vai bộ chuyển chế độ xem; chọn nhiều tạo thành toolbar định dạng. |

## Toolbar

`Toolbar` · Figma: `Toolbar` · trang **Action**

**Usage.** Toolbar là thanh ngang có ba vùng trái, giữa, phải. Dùng cho hành động theo ngữ cảnh trong một vùng nội dung (trên bảng, trong card, trong panel), không dùng làm header cấp trang. Đặt size một lần trên toolbar thì mọi nút, input và tab bên trong tự khớp theo.

**Nên**

- ✅ Đặt hành động phụ như "Quay lại" bên trái, hành động chính như "Lưu" bên phải.
- ✅ Làm toolbar tạm thời (như chọn hàng loạt) khác biệt về thị giác để người dùng biết nó theo ngữ cảnh, ví dụ bằng màu nền hoặc viền.
- ✅ Tách toolbar khỏi nội dung bên dưới bằng divider, biến thể nền, hoặc cả hai.
- ✅ Dùng Toolbar làm đầu card khi đầu card có hành động tương tác như lọc hay thêm; nó cho bố cục slot, điều hướng bàn phím và truyền size xuống con. Nếu đầu card chỉ có tiêu đề, không hành động, LayoutHeader hoặc Section là đủ.

**Không nên**

- ❌ Nhồi quá nhiều hành động vào một toolbar; chuyển mục ít dùng vào MoreMenu.
- ❌ Đặt size trên từng nút con; đặt một lần trên toolbar và nó tự truyền xuống.
- ❌ Dùng Toolbar cho điều hướng toàn ứng dụng như link menu chính hay đăng xuất; dùng TopNav hoặc LayoutHeader.

**Examples**

| Example | Mô tả |
|---|---|
| Toolbar — Bulk Actions | Toolbar gọn, biến thể muted, hiện hành động chọn hàng loạt. Dùng khi người dùng chọn nhiều mục trong danh sách hoặc bảng và cần truy cập nhanh thao tác theo lô. |
| Toolbar — Card Header | Toolbar làm đầu card với tiêu đề căn trái và icon hành động bên phải. Dùng Toolbar thay LayoutHeader khi đầu card có hành động tương tác; Toolbar thêm bố cục slot đầu/cuối, điều hướng bàn phím và tự truyền size. Nếu chỉ có tiêu đề, LayoutHeader hoặc Section là đủ. |
| Toolbar — Sizes | Toolbar nhỏ, vừa, lớn đặt cạnh nhau. Prop size tự truyền xuống nút và input con. Nhỏ cho giao diện dày như card, vừa cho đa số trường hợp, lớn cho bố cục thoáng. |
| Toolbar — Table Filter | Thanh lọc trên bảng: ô tìm kiếm đứng đầu hàng, mỗi trường bên cạnh là một trigger đóng đồng thời là chip lọc của chính nó (chưa đặt thì hiện tên trường, đã đặt thì hiện cả mệnh đề), các mệnh đề gấp dần từ cuối thành một con số khi hàng hẹp lại, tiếp theo là số kết quả trực tiếp, nút xóa hết và bộ chọn cột. Dùng để tìm, lọc, thu hẹp các dòng bản ghi phẳng như công việc, đơn hàng, ticket, người dùng. |
| Toolbar — Three Slot | Toolbar có nội dung đầu, giữa, cuối theo lưới ba cột. Dùng khi cần tiêu đề ở giữa, điều hướng và hành động ở hai bên. |
| Toolbar — Tab Navigation | Toolbar có tab ở slot đầu và nút hành động ở cuối. Dùng làm đầu card hoặc section khi nội dung chia tab và có một hành động chính đi kèm. |

---

# Chat

## Chat Composer

`ChatComposer` · Figma: `Chat / ChatComposer` · trang **Chat**

**Usage.** ChatComposer là khung nhập tin nhắn của một giao diện chat. Nó điều phối bản nháp (controlled hoặc uncontrolled), cung cấp sẵn một input hỗ trợ token và nút gửi/dừng, đồng thời sắp xếp các nội dung tùy chọn: drawer, header, footer và trạng thái. Input và nút gửi tùy biến có thể tham gia cùng hợp đồng về giá trị, gửi, vô hiệu, dừng và focus qua useChatComposerContext().

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| ChatComposer — Attachments | Chat composer có token tệp gỡ được trong một drawer thu gọn được. Dùng khi người dùng đính kèm tệp hoặc ngữ cảnh vào tin nhắn. |
| ChatComposer — Flat | Composer mặc định được nâng (`elevation="low"`). Đặt `elevation="none"` để làm phẳng; khi đó nó vẽ viền với cách xử lý nghỉ / hover / focus giống text input. |
| ChatComposer — Footer Actions | Chat composer có dropdown menu chọn model và cài đặt ở footer, nút micro ở slot hành động gửi. |
| ChatComposer — Full Featured | Chat composer đủ mọi slot: drawer đính kèm thu gọn được, hành động ở header, thanh tiến độ ngữ cảnh, dropdown ở footer và nút micro. Cấu hình composer tối đa. |
| ChatComposer — Simple | Chat composer tối giản với placeholder và xử lý gửi. Cách đơn giản nhất để thả ô nhập tin nhắn vào trang. |
| ChatComposer — Streaming | Chat composer ở trạng thái đang stream, có nút dừng. Dùng khi trợ lý đang sinh câu trả lời và người dùng có thể hủy. |
| ChatComposer — Validation | Chat composer có thông báo trạng thái lỗi và cảnh báo. Trạng thái có thể nằm trên hoặc dưới composer để hiện phản hồi kiểm tra hoặc hệ thống. |

## Chat Layout

`ChatLayout` · Figma: `Chat / ChatLayout` (khung bố cục); nút cuộn: `Chat / ChatLayoutScrollButton` · trang **Chat**

**Usage.** ChatLayout là khung bố cục cho giao diện chat toàn trang. Nó hiển thị tin nhắn theo luồng trang bình thường và ghim composer ở đáy với lớp làm mờ kiểu kính mờ. Đặt prop density để điều khiển khoảng cách, mặc định balanced. Dùng để bọc ChatMessageList và ChatComposer cho trải nghiệm chat hoàn chỉnh, có sẵn tự cuộn và nút cuộn xuống cuối.

**Nên**

- ✅ Truyền ChatMessageList làm children và ChatComposer qua prop composer để có giao diện chat hoàn chỉnh.
- ✅ Cung cấp emptyState để cuộc trò chuyện mới hiện lời gợi ý thay vì màn trống.
- ✅ Dùng scrollRef khi chat nhúng trong trang mà phần tử cha lo việc cuộn.

**Không nên**

- ❌ Đặt chiều cao cố định cho layout; để nó lấp đầy vùng chứa bằng flex: 1.
- ❌ Đặt nhiều ChatLayout trong cùng một vùng cuộn; mỗi cái đều giả định nó sở hữu ngữ cảnh cuộn của mình.

**Examples**

| Example | Mô tả |
|---|---|
| ChatLayout — Panel View | Chat dạng sidebar hẹp trong vùng chứa bị giới hạn, tự chuyển sang mật độ compact. Dùng cho panel bên, drawer hoặc widget chat nhúng khi bề ngang hạn chế. |

## Chat Message

`ChatMessage` · Figma: `Chat / ChatMessage` · trang **Chat**

**Usage.** Lớp bọc ngữ cảnh người gửi: lo avatar, tên, metadata và căn lề theo vai trò người gửi.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| ChatMessage — Avatar & Name | Tin nhắn có avatar và tên người gửi. Đặt tên trên bubble khi dùng bubble, hoặc trên lớp bọc tin nhắn khi nội dung thô. |
| ChatMessage — Ghost | Biến thể Ghost cho tin nhắn không có viền bubble. Giữ padding để căn lề nhưng nền trong suốt, hợp với câu trả lời kiểu AI. |
| ChatMessage — Multi-Bubble | Các bubble gộp nhóm dùng prop group để giảm bo góc. Dùng first, middle, last để nối trực quan các bubble liên quan của cùng người gửi. |
| Chat Message | Nhóm nhiều bubble của người dùng kèm trạng thái gửi, và câu trả lời Ghost của trợ lý có avatar, tên, thời gian và thông tin model. |

## Chat Message Metadata

`ChatMessageMetadata` · Figma: `Chat / ChatMessageMetadata` · trang **Chat**

**Usage.** Đặt ChatMessageMetadata dưới tin nhắn hoặc trong slot metadata của ChatMessageBubble cuối để hiện thời gian, nội dung chân và trạng thái gửi (tùy chọn). Slot giá trị đơn không hiển thị (boolean, chuỗi rỗng) không tạo dấu phân cách; số 0 vẫn hiển thị. Nội dung React phức hợp do nơi gọi tự quản.

**Nên**

- ✅ Đặt metadata trong slot metadata của bubble cuối khi tin nhắn dùng bubble, để nó đi sau nội dung bubble.
- ✅ Truyền thời gian và nội dung chân độc lập; dấu phân cách được bỏ với slot không hiển thị. Node React phức hợp được dùng nguyên như truyền vào.

**Không nên**

- ❌ Đưa hành động ở chân mà không có tên truy cập và hành vi tương tác riêng; hàng metadata không sở hữu các control đó.
- ❌ Đặt cùng một metadata trên cả bubble và tin nhắn bao nó.

**Examples**

| Example | Mô tả |
|---|---|
| ChatMessageMetadata — Footer Actions | Tin nhắn của trợ lý có hành động ở chân: sao chép, thử lại, thích/không thích và nhãn model. Dùng cho câu trả lời AI cần phản hồi hoặc control tiện ích. |
| Chat Message Metadata | Cuộc trò chuyện ba tin nhắn minh họa trạng thái lỗi có thử lại, trạng thái gửi, và đủ hành động ở chân kèm nhãn model. |
| ChatMessageMetadata — Status | Cả 5 trạng thái gửi (đang gửi, đã gửi, đã nhận, đã đọc, lỗi), mỗi cái kèm thời gian. Dùng để hiện tiến trình gửi tin hoặc báo lỗi. |
| ChatMessageMetadata — Timestamps | Metadata chỉ có thời gian trên tin nhắn người dùng và trợ lý. Hỗ trợ thời gian tuyệt đối và tương đối qua Timestamp. |

## Chat System Message

`ChatSystemMessage` · Figma: `Chat / ChatSystemMessage` · trang **Chat**

**Usage.** Dùng ChatSystemMessage cho nội dung ngắn, không thuộc người gửi nào, trong bản ghi chat. Chọn biến thể default cho thông báo trạng thái mang tính sự kiện và biến thể divider cho ngắt ngày hoặc ngắt phần. Nội dung default dài sẽ xuống dòng trong bề rộng sẵn có. Component mang ngữ nghĩa status và nhánh divider có separator gắn nhãn.

**Nên**

- ✅ Giữ thông điệp ngắn và tự đủ nghĩa để vẫn hiểu được khi không có icon.
- ✅ Dùng biến thể divider cho ranh giới thời gian hoặc phần, và default cho thông báo trạng thái mang tính sự kiện.

**Không nên**

- ❌ Dùng ChatSystemMessage cho nội dung do người gửi viết; dùng ChatMessage và ChatMessageBubble.
- ❌ Dùng hình icon do nơi gọi cung cấp làm nguồn nghĩa duy nhất; thông điệp hiển thị phải mang cùng thông tin.

**Examples**

| Example | Mô tả |
|---|---|
| Chat System Message | Tin nhắn hệ thống cho ngăn cách ngày, cập nhật trạng thái và thông báo thông tin. Minh họa cả default và divider trong một luồng hội thoại thực tế. |
| ChatSystemMessage — Status Updates | Tin nhắn trạng thái thực tế trong hội thoại: thay đổi thành viên, mốc thời gian và thông báo đã giải quyết. |
| ChatSystemMessage — Variants | Biến thể default và divider đặt cạnh nhau. Default cho cập nhật trạng thái trong dòng, divider cho ngăn cách ngày hoặc ngắt phần. |
| ChatSystemMessage — Icon | Tin nhắn hệ thống có icon đầu củng cố loại tin nhắn. Dùng icon để người dùng lướt và nhận ra loại tin nhanh. |

## Chat Tool Calls

`ChatToolCalls` · Figma: `Chat / ChatToolCalls` · trang **Chat**

**Usage.** ChatToolCalls hiển thị các lần gọi công cụ/hàm trong câu trả lời của LLM. Truyền một mảng lời gọi và component lo phần còn lại: một lời gọi hiển thị trong dòng, nhiều lời gọi gộp thành bản tóm tắt với lời gọi mới nhất hiện ở bề mặt. Dùng ở bất cứ đâu một agent AI cần cho thấy nó đã làm gì.

**Nên**

- ✅ Có chuỗi target trên mỗi lời gọi để người dùng thấy công cụ tác động lên cái gì: đường dẫn tệp, lệnh shell hay truy vấn tìm kiếm.
- ✅ Hiện thời lượng trên lời gọi đã xong để người dùng đánh giá công cụ nào chậm và hiểu vì sao câu trả lời mất thời gian.
- ✅ Cung cấp nhãn nhóm khi con số đếm tự động không giải thích được các lời gọi là gì.
- ✅ Cung cấp resultDetail với code block cho lời gọi có đầu ra (diff cho chỉnh sửa, output terminal cho lệnh shell) để người dùng xem kết quả ngay trong dòng.
- ✅ Đặt key duy nhất cho mỗi lời gọi khi stream để React tạo hiệu ứng thêm mới mà không mount lại dòng đã xong.

**Không nên**

- ❌ Bỏ trường status. Thiếu nó lời gọi mặc định là complete, gây hiểu sai với lời gọi còn đang chạy hoặc đã lỗi.
- ❌ Hiển thị tool call ngoài ngữ cảnh tin nhắn chat; chúng được thiết kế để nằm trong tin nhắn trợ lý, không đứng riêng.
- ❌ Tự bọc từng lời gọi; component tự chọn bố cục đơn hay nhóm theo độ dài mảng.

**Examples**

| Example | Mô tả |
|---|---|
| ChatToolCalls — Expandable | Tool call có chi tiết kết quả mở rộng được, hiện diff và output lệnh trong code block. Bấm vào một dòng để xem kết quả. |
| ChatToolCalls — Statuses | Cả bốn trạng thái (chờ, đang chạy, hoàn tất, lỗi) trong một nhóm. |
| ChatToolCalls — Simple | Một tool call trong dòng phía trên một nhóm nhiều lời gọi thu gọn được có thống kê diff. Minh họa cả hai bố cục. |

---

# Container

## Card

`Card` · Figma: `Card` · trang **Container**

**Usage.** Card là vùng chứa có viền, có thể nâng, dành cho các mục rời rạc, tự đủ nghĩa: những thứ có thể sắp xếp lại, gỡ bỏ hoặc tương tác độc lập. Card KHÔNG phải công cụ bố cục mặc định. Đa số nhóm nội dung không cần vùng chứa; khoảng cách và căn lề tự tạo nhóm thị giác. Chỉ dùng Card khi các mục cần ranh giới tương tác rõ ràng hoặc cần so sánh trực quan trong lưới.

**Nên**

- ✅ Tự hỏi "mục này có sắp xếp lại hay gỡ bỏ độc lập được không?" Có thì là card. Không thì chỉ là một phần của trang: dùng heading + Stack hoặc Section.
- ✅ Dùng card cho mục rời rạc: một hồ sơ người dùng, một thông báo, một chỉ số, một sản phẩm trong lưới. Mỗi card đại diện cho một "thứ" có ranh giới tương tác rõ.
- ✅ Chỉ khoảng cách và căn lề đã tạo nhóm thị giác. Không phải thứ gì cũng cần vùng chứa; thử bỏ card và xem nhóm có còn rõ nhờ khoảng trắng và kiểu chữ không.
- ✅ Giữ padding nhất quán giữa các card anh em để chúng thẳng hàng trong lưới hoặc danh sách.
- ✅ Ghép card với Layout khi cần header có cấu trúc, nội dung cuộn được và footer có hành động.

**Không nên**

- ❌ Mặc định dùng card để nhóm thị giác. Heading + Stack với khoảng cách đúng tạo thứ bậc mà không cần thêm viền khắp nơi. Card nên là ngoại lệ, không phải mặc định.
- ❌ Bọc các phần của trang trong card. "Cài đặt chung", "Tùy chọn thông báo", nhóm form: đây là vùng của trang, dùng Section hoặc heading + stack.
- ❌ Tạo lưới card giống hệt nhau (icon + heading + chữ, lặp lại). Thay đổi bố cục hoặc xét lại xem có cần card không.
- ❌ Lồng card trong card; làm phẳng thứ bậc hoặc dùng khoảng cách và divider.
- ❌ Dùng biến thể màu để báo trạng thái; dùng Banner hoặc Badge. Card màu dành cho phân loại.

**Examples**

| Example | Mô tả |
|---|---|
| Card — Callout | Card biến thể muted cho mẹo, ghi chú hoặc thông tin bổ sung. Dùng khi nội dung cần khác biệt nhưng không nổi bật. Biến thể muted dùng nền wash thay vì mặc định nổi, tạo cảm giác lõm vào thay vì nâng lên. Hợp với sidebar, panel trợ giúp hoặc callout trong dòng. |
| Card — Elevations | Bốn mức elevation đặt cạnh nhau. Card mặc định phẳng; chỉ nâng bằng `elevation` khi nó cần nổi trên nội dung xung quanh. |
| Card | Card có heading và chữ thân, kiểu vùng chứa mặc định. |
| Card — Variants | Biến thể default, muted và màu đặt cạnh nhau. Dùng biến thể màu để phân loại card trực quan, như màu nhóm, thẻ dự án hay loại nội dung. Mỗi màu dùng token nền tương ứng của theme nên tự thích ứng sáng/tối. |
| Card — Layout | Card có header có cấu trúc, vùng nội dung và footer với nút hành động. Dùng cho form, hộp thoại hoặc panel cài đặt cần phần rõ ràng. Ghép Card với Layout để tự có divider giữa header, nội dung và footer. Footer mặc định căn hành động sang phải. |
| Card — Simple | Card có heading và chữ thân. Dùng cho tóm tắt, mô tả hoặc nội dung nhóm cần tách khỏi trang. Card tự lo viền, nền và padding; chỉ cần truyền nội dung. Đặt bề rộng để giới hạn, hoặc để nó lấp đầy phần tử cha. |

## Carousel

`Carousel` · Figma: `Carousel` · trang **Container**

**Usage.** Carousel cuộn ngang một hàng mục khi chúng tràn bề rộng sẵn có. Dùng cho lưới card, thư viện ảnh, danh sách sản phẩm hoặc bất kỳ tập mục nào cần duyệt được mà không chiếm cả trang.

**Nên**

- ✅ Bật scroll-snap khi mỗi mục cần dừng chính xác ở mép đầu, như thư viện ảnh hay danh sách sản phẩm.
- ✅ Dùng hasLoop cho tập nhỏ, quay vòng được như thư viện ảnh, nơi đi qua mục cuối rồi về mục đầu là tự nhiên.
- ✅ Luôn có aria-label mô tả carousel chứa gì, như "Sản phẩm nổi bật" hay "Thành viên nhóm".
- ✅ Carousel theo mẫu carousel của WAI-ARIA APG nhưng không tự xoay: vùng có nhãn và mang aria-roledescription="carousel", mỗi mục là một group tên "Slide N of M", vùng cuộn là một điểm dừng tab để người dùng bàn phím cuộn bằng phím mũi tên.
- ✅ Dùng khoảng cách và bề rộng mục nhất quán để carousel trông có chủ đích, không như nội dung tràn do vô tình.
- ✅ Tin vào điều hướng có sẵn: người dùng trackpad vuốt ngang, người dùng chuột giữ Shift khi lăn bánh xe để đi qua các mục.

**Không nên**

- ❌ Dùng carousel cho nội dung mọi người dùng bắt buộc phải thấy. Không phải ai cũng cuộn ngang, hãy đặt nội dung quan trọng ở vùng nhìn thấy ngay.
- ❌ Tự chuyển mục. Để người dùng cuộn theo nhịp của họ.
- ❌ Lồng carousel. Carousel trong carousel gây rối và phá điều hướng bàn phím.

**Examples**

| Example | Mô tả |
|---|---|
| Carousel — Cards | Hàng card cuộn ngang có bật snap. Dùng cho lưới tính năng, danh sách sản phẩm hoặc tập card tràn bề rộng. Carousel tự thêm mép mờ và nút điều hướng. |
| Carousel | Carousel ngang các card có scroll-snap và nút điều hướng. Cuộn hoặc bấm mũi tên để duyệt. |
| Carousel — Snap | Carousel scroll-snap có nút điều hướng và card thành viên nhóm. Mỗi card dừng ở mép đầu khi cuộn. Dùng khi mục cần xem từng cái một thay vì như một dải liên tục. |

## Clickable Card

`ClickableCard` · Figma: `ClickableCard` · trang **Container**

**Usage.** Card tương tác làm đích điều hướng hoặc hành động. Phần tử tương tác lồng bên trong hoạt động độc lập.

**Nên**

- ✅ Dùng cho card điều hướng tới trang chi tiết hoặc kích hoạt một hành động duy nhất.
- ✅ Thoải mái lồng nút hoặc liên kết bên trong; chúng tự xử lý sự kiện của mình.

**Không nên**

- ❌ Dùng để bật/tắt chọn; dùng SelectableCard.

**Examples**

| Example | Mô tả |
|---|---|
| Clickable Card — Elevated | Clickable card nâng bằng `elevation="med"` để bóng báo hiệu cả bề mặt tương tác được. |
| Clickable Card | Clickable card điều hướng khi bấm. Phần tử tương tác lồng bên trong hoạt động độc lập. |
| Clickable Card — Nested Button | Card sản phẩm điều hướng khi bấm nhưng có nút "Thêm vào giỏ" độc lập bên trong. |

## Collapsible

`Collapsible` · Figma: `Collapsible` · trang **Container**

**Usage.** Collapsible ẩn và hiện nội dung sau một nút kích hoạt. Dùng trong panel cài đặt, trang FAQ hoặc màn chi tiết để giữ trang dễ lướt, đồng thời cho người dùng đi sâu vào phần họ quan tâm. Bọc nhiều collapsible trong CollapsibleGroup để có hành vi accordion. Component collapsible tùy biến thì dùng trực tiếp hook `useCollapsible`.

**Nên**

- ✅ Dùng hasDividers trên CollapsibleGroup cho danh sách kiểu FAQ: có sẵn đường kẻ giữa các dòng theo token viền, không tự vẽ viền.
- ✅ Bọc mỗi Collapsible trong một Card để tách thị giác trong bố cục accordion, hoặc dùng hasDividers của CollapsibleGroup cho danh sách phẳng; không kết hợp cả hai.
- ✅ Dùng CollapsibleGroup với type="single" cho trang cài đặt hoặc FAQ khi chỉ một phần được mở tại một thời điểm.
- ✅ Dùng type="multiple" khi người dùng cần so sánh nội dung giữa các phần, như danh sách tính năng hoặc bậc giá.
- ✅ Mở sẵn phần (defaultIsOpen) khi nội dung có khả năng cần ngay lần xem đầu; đừng bắt người dùng bấm mới thấy thông tin thiết yếu.

**Không nên**

- ❌ Giấu nội dung quan trọng hoặc bắt buộc sau collapsible; người dùng có thể không phát hiện ra.
- ❌ Lồng collapsible sâu quá hai cấp; khó tìm và khó điều hướng nội dung.
- ❌ Dùng collapsible cho một đoạn ngắn duy nhất; hiện thẳng chữ ra.

**Examples**

| Example | Mô tả |
|---|---|
| Collapsible — Controlled | Quản lý phần đang mở từ state của cha, để thứ khác ngoài cú bấm có thể đổi nó: tham số URL, form nhảy tới bước lỗi kiểm tra, hoặc nút Trước/Sau như trong ví dụ. onChange trả về toàn bộ giá trị đang mở. |
| Collapsible — FAQ | FAQ dựng bằng hasDividers: đường kẻ dòng và padding theo mật độ, không CSS tùy biến. Câu hỏi tự đặt kiểu chữ (body semibold, không phải cỡ large 17px mặc định của trigger) để danh sách câu hỏi đọc như các dòng chứ không như chồng heading; câu hỏi và câu trả lời phân biệt bằng độ đậm và màu thay vì cỡ chữ. |
| Collapsible — Multiple Mode | Nhiều phần mở cùng lúc để so sánh, như danh sách tính năng, bậc giá. Mỗi Collapsible một Card, nên mỗi trigger giữ cỡ chữ lớn: nó là heading của bề mặt, không phải một dòng trong danh sách. |
| Collapsible | Nhóm accordion ba phần ở chế độ single: mở một phần thì các phần khác đóng. |
| Collapsible — Single Mode | Chỉ một phần mở tại một thời điểm, nên chỉ một khối nội dung giành sự chú ý. Dùng defaultValue để mở sẵn phần người đọc lần đầu cần. Mỗi Collapsible sở hữu một Section, nên trigger là heading của section đó. |
| Collapsible — With Dividers | Danh sách phẳng trên nền trang với Divider đặt tay, cho panel chi tiết và sidebar nơi card quá nặng. Là các dòng, nên trigger hạ xuống body-semibold và có một dòng metadata phụ dưới mỗi câu trả lời. |

## Selectable Card

`SelectableCard` · Figma: `SelectableCard` · trang **Container**

**Usage.** Card chuyển giữa trạng thái được chọn và không được chọn, có viền màu nhấn. Để điều hướng thì dùng ClickableCard.

**Nên**

- ✅ Dùng cho chọn gói, chip lọc hoặc lưới lựa chọn.
- ✅ Chọn một thì lưu một ID; chọn nhiều thì dùng một Set.
- ✅ Khi đang focus, bật/tắt chọn bằng Space hoặc Enter.

**Không nên**

- ❌ Dùng để điều hướng; dùng ClickableCard.

**Examples**

| Example | Mô tả |
|---|---|
| Selectable Card — Elevated | Selectable card nâng bằng `elevation="low"`. Vòng chọn bên trong chồng lên bóng, nên card được chọn vẫn giữ elevation. |
| Selectable Card — Multi-select | Bộ chọn thẻ chọn nhiều dùng selectable card biến thể màu, viền chọn cùng màu. |
| Selectable Card | Bộ chọn gói với hành vi chọn một kiểu radio. Card hiện viền màu nhấn khi được chọn. |

---

# Content

## Avatar

`Avatar` · Figma: `Avatar` · trang **Content**

**Usage.** Avatar đại diện cho một người hoặc nhóm bằng ảnh đại diện, chữ viết tắt hoặc icon mặc định. Dùng trong đầu bình luận, danh bạ, tin nhắn chat, card người dùng và bất cứ đâu cần nhận diện ai đó bằng hình.

**Nên**

- ✅ Luôn truyền name để avatar hiện chữ viết tắt khi ảnh lỗi, và để trình đọc màn hình đọc được đó là ai.
- ✅ Chọn cỡ hợp ngữ cảnh: xsm hoặc sm cho nhắc tên trong dòng, md hoặc lg cho danh sách và card, xl cho đầu trang hồ sơ.
- ✅ Thêm chấm trạng thái khi việc biết ai đó có sẵn sàng hay không là quan trọng, như trong chat hay màn nhóm.
- ✅ Khi bọc Avatar trong Tooltip hoặc HoverCard của mình, đặt tooltip={false} để tooltip tên có sẵn không chồng lên.
- ✅ Cho mọi avatar tương tác (href hoặc onClick) một name hoặc alt. Đó là tên truy cập của control, và sẽ có cảnh báo khi phát triển nếu thiếu.

**Không nên**

- ❌ Dựa vào nhãn trạng thái để đặt tên cho avatar tương tác. "Đang trực tuyến" không nói gì về việc liên kết dẫn đi đâu.
- ❌ Dùng Avatar cho logo, ảnh sản phẩm hay bất cứ thứ gì không phải người hoặc nhóm. Dùng ảnh hoặc icon.
- ❌ Dùng xstyle hoặc className để ghi đè hình dạng. Dùng prop shape để theme điều khiển toàn cục.

**Examples**

| Example | Mô tả |
|---|---|
| Avatar — Fallback Chain | Minh họa chuỗi dự phòng: ảnh chính, ảnh dự phòng, chữ viết tắt, rồi icon mặc định. |
| Avatar — Initials | Hiện chữ viết tắt thay cho ảnh. Avatar tự lấy chữ đầu của tên và họ. Dùng khi chỉ có tên người dùng, như tài khoản ẩn danh hoặc người dùng mới. |
| Avatar — Interactive | Làm avatar tương tác được bằng `href` (hiển thị như liên kết) hoặc `onClick` (hiển thị như nút). Cả hai đều focus được và có vòng focus-visible cho người dùng bàn phím. Dùng cho liên kết hồ sơ, popup nhắc tên, hoặc avatar mà người dùng có thể thao tác. |
| Avatar | Avatar ở mọi cỡ với ảnh, chữ viết tắt dự phòng và chấm trạng thái. Tham chiếu nhanh để chọn đúng cỡ. |
| Avatar — Tooltip | Mặc định avatar hiện tên trong tooltip khi hover và khi focus bằng bàn phím. Truyền chuỗi để hiện chữ tùy biến, hoặc false để tắt tooltip. |
| Avatar — User Card | Đặt avatar cạnh tên và vai trò để tạo một dòng card người dùng. Dùng cho đầu bình luận, danh bạ, phần hồ sơ, hoặc nơi cần nhận diện một người trong nháy mắt. |
| Avatar — Photo | Hiện ảnh đại diện ở các cỡ khác nhau. Dùng khi có URL ảnh người dùng. Ảnh lỗi thì hiện chữ viết tắt. |
| Avatar — Status Dot | Thêm chấm trạng thái vào avatar để cho biết ai đó đang trực tuyến, vắng hay bận. Dùng trong chat, nhắn tin, hoặc giao diện cần biết độ sẵn sàng. |

## Avatar Group

`AvatarGroup` · Figma: `AvatarGroup` · trang **Content**

**Usage.** AvatarGroup hiển thị nhiều avatar trong một hàng chồng lên nhau, có chỉ báo phần tràn (tùy chọn). Dùng API ghép: truyền trực tiếp các Avatar con để mỗi avatar mang prop riêng (chấm trạng thái, xử lý bấm, v.v.).

**Nên**

- ✅ Tự cắt danh sách và chỉ truyền các avatar muốn hiển thị; thường 3–5. Nhóm hiển thị đúng các con được truyền và không bao giờ tự cắt.
- ✅ Dùng AvatarGroupOverflow cho nội dung tràn tùy biến như nút mở popover hoặc nút "thêm thành viên".
- ✅ Truyền chấm trạng thái, xử lý bấm hoặc tooltip trực tiếp trên từng Avatar con.
- ✅ Làm avatar tương tác bằng href hoặc onClick để dẫn tới hồ sơ. Các avatar tương tác chung một điểm dừng Tab; phím mũi tên di chuyển giữa chúng, và nhóm đọc gợi ý bàn phím cho công nghệ hỗ trợ (kỹ thuật roving tabindex của WAI-ARIA APG).

**Không nên**

- ❌ Lồng AvatarGroup; dùng một nhóm duy nhất chứa mọi avatar.
- ❌ Đặt size trên avatar con. Size của nhóm luôn thắng size riêng của con, kể cả khi nhóm để size mặc định, nên size của con bị bỏ qua mà không báo.

**Examples**

| Example | Mô tả |
|---|---|
| Avatar Group — Interactive | Hàng mặt người với avatar dẫn tới hồ sơ, chỉ báo tràn mở danh sách thành viên đầy đủ. Cả nhóm là một điểm dừng Tab; phím mũi tên di chuyển giữa các avatar và nút tràn. |
| Avatar Group | Hàng avatar chồng nhau với tập hiển thị đã cắt và số tràn tính từ server. Hiện thành viên nhóm theo bố cục hàng mặt người gọn. |
| Avatar — Group | Chồng nhiều avatar trong một hàng để đại diện cho một nhóm người. Dùng cho danh sách nhóm, người review PR, hoặc số người tham gia khi muốn hiện gương mặt mà không tốn chỗ. |

## Blockquote

`Blockquote` · Figma: `Blockquote` · trang **Content**

**Usage.** Khối trích dẫn có đường kẻ ở mép đầu dòng và chữ màu phụ. Dùng để làm nổi nội dung trích dẫn, lời chứng thực hoặc đoạn trích. Đường kẻ và padding theo hướng logic nên chuyển sang mép phải ở ngôn ngữ viết phải sang trái.

**Nên**

- ✅ Dùng cho chữ trích dẫn, lời chứng thực hoặc đoạn trích nổi bật từ nguồn bên ngoài.
- ✅ Cung cấp prop cite khi biết nguồn trích dẫn.
- ✅ Truyền nguồn qua cite thay vì gõ vào children, để nó hiển thị thành phần tử <cite> có ngữ nghĩa mà công nghệ hỗ trợ phân biệt được với lời trích.

**Không nên**

- ❌ Dùng cho hộp callout hoặc ghi chú thông tin; dùng Banner.
- ❌ Tự bọc phần ghi nguồn trong <footer>. <footer> trong <blockquote> thành landmark contentinfo, trang có nhiều trích dẫn sẽ báo nhiều footer trang.

**Examples**

| Example | Mô tả |
|---|---|
| Blockquote — Showcase | Blockquote có và không có ghi nguồn. Tham chiếu nhanh cho component. |
| Blockquote — Testimonials | Nhiều trích dẫn xếp trong lưới card cho phần lời chứng thực. Kết hợp với Card và Grid để tạo bố cục bằng chứng xã hội. |
| Blockquote — With Attribution | Một trích dẫn thường và một trích dẫn có ghi nguồn cite. Dùng cite để ghi công tác giả hoặc nguồn gốc. |

## Citation

`Citation` · Figma: `Citation` · trang **Content**

**Usage.** Citation hiển thị tham chiếu trong dòng tới nguồn bên ngoài. Dùng để ghi nguồn thông tin trong câu trả lời do AI sinh, bài viết, hoặc bất cứ đâu cần nguồn gốc và liên kết nguồn.

**Nên**

- ✅ Dùng biến thể label khi tiêu đề nguồn thêm ngữ cảnh có ý nghĩa cho người đọc.
- ✅ Dùng biến thể number cho tham chiếu gọn trong chữ thân, như chú thích cuối trang.

**Không nên**

- ❌ Trộn biến thể label và number trong cùng đoạn. Chọn một kiểu cho mỗi ngữ cảnh để nhất quán thị giác.

**Examples**

| Example | Mô tả |
|---|---|
| Citation — Inline Text | Citation nằm trong một đoạn văn, cho thấy cách chúng chảy cùng nội dung xung quanh. |
| Citation — Showcase | Mọi biến thể citation: chip nhãn và badge số, có và không có icon, liên kết. |
| Citation — Source List | Danh sách nguồn trích dẫn có icon, như ở cuối câu trả lời AI hoặc chân bài viết. |

## Code

`Code` · Figma: `Code` · trang **Content**

**Usage.** Phần tử code trong dòng. Hiển thị <code> có font đơn cách và nền nhạt. Khối code nhiều dòng thì dùng CodeBlock.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| Code — Text Sizes | Code trong dòng nằm trong chữ heading, body, supporting và label. Code tự khớp cỡ chữ của phần tử chữ cha. |
| Code — Inline | Tham chiếu code trong dòng trộn trong một đoạn chữ thân. Dùng Code để đánh dấu tên hàm, hook hoặc thuật ngữ API cho nổi khỏi văn xuôi. |
| Code | Đoạn code ngắn trong một câu, cho thấy Code hiển thị cạnh chữ thân. |
| Code — Content Types | Code trong dòng cho biến, lệnh terminal, thuộc tính CSS, đường dẫn tệp và phím tắt. Cho thấy Code thích ứng với nhiều loại nội dung kỹ thuật. |

## Code Block

`CodeBlock` · Figma: `CodeBlock` · trang **Content**

**Usage.** CodeBlock hiển thị code tô màu cú pháp với số dòng, nút sao chép và phần thu gọn tùy chọn. Dùng CodeBlock cho đoạn nhiều dòng như tệp nguồn, lệnh terminal, ví dụ cấu hình. Dùng Code cho tham chiếu trong dòng tới tên hàm, biến hoặc cờ CLI trong chữ thân.

**Nên**

- ✅ Đặt prop language khớp nội dung code để tô màu cú pháp chính xác. Không rõ ngôn ngữ thì dùng "plaintext".
- ✅ Thêm title khi code đại diện cho một tệp. Nó cho người đọc ngữ cảnh và nằm trên thanh header cạnh nút sao chép.
- ✅ Dùng Code cho tham chiếu ngắn trong dòng như tên hàm hoặc cờ CLI, và CodeBlock cho đoạn nhiều dòng đứng riêng.

**Không nên**

- ❌ Bật số dòng cho đoạn ngắn (dưới 5 dòng), nơi nó chỉ gây rối mà không giúp điều hướng.
- ❌ Lồng code block trong vùng chứa cuộn được. Dùng prop maxHeight, vốn xử lý tràn sẵn.

**Examples**

| Example | Mô tả |
|---|---|
| Code — Snippet | Lệnh terminal ngắn có nút sao chép, không số dòng. Dùng cho hướng dẫn cài đặt hoặc lệnh một dòng người đọc sẽ dán trực tiếp. |
| Code — Highlighted | Code TypeScript có một số dòng được tô nổi để hướng sự chú ý vào đoạn quan trọng. Dùng highlightLines để chỉ ra code mới hoặc quan trọng trong hướng dẫn và changelog. |
| Code — Config | Tệp cấu hình JSON có thanh tiêu đề và số dòng. Prop title thêm nhãn tên tệp ở header để người đọc biết code thuộc tệp nào. |
| Code — Scrollable | Code block dài có chiều cao tối đa để cuộn dọc. Dùng maxHeight để khối không chiếm hết trang khi hiển thị tệp lớn. |
| Code Block | Code block TypeScript tô màu cú pháp có số dòng, thanh tiêu đề và nút sao chép. |
| Code — Terminal | Khối lệnh kiểu terminal tối: CodeBlock bash bọc trong SyntaxTheme với preset GitHub Dark, bật nút sao chép, không số dòng. Dùng cho phiên shell hoặc output CLI cần đọc như terminal kể cả trên trang sáng. Dùng preset cú pháp tối thay vì tự vẽ hộp tối bằng CSS tùy biến. |

## Empty State

`EmptyState` · Figma: `EmptyState` · trang **Content**

**Usage.** EmptyState hiển thị nội dung giữ chỗ khi một vùng nội dung không có dữ liệu. Dùng cho danh sách rỗng, không có kết quả tìm kiếm, thiết lập lần đầu hoặc hộp thư đã dọn sạch. Luôn có tiêu đề và bước tiếp theo để người dùng không bị kẹt.

**Nên**

- ✅ Có tiêu đề rõ ràng và nút kêu gọi hành động để người dùng biết làm gì tiếp.
- ✅ Dùng hình minh họa hoặc icon củng cố ngữ cảnh của trạng thái rỗng.
- ✅ Dùng biến thể compact trong card hoặc sidebar khi chỗ hẹp.

**Không nên**

- ❌ Để trạng thái rỗng không có hướng dẫn; luôn giải thích chuyện gì đã xảy ra và người dùng có thể làm gì tiếp.
- ❌ Dùng thông điệp chung chung như "Không có dữ liệu"; nói cụ thể cái gì rỗng và vì sao.
- ❌ Dùng EmptyState cho thông báo lỗi cần hành động ngay; dùng Banner.

**Examples**

| Example | Mô tả |
|---|---|
| EmptyState — Actions | Trạng thái rỗng đầy đủ với icon, thông điệp và nút hành động. Dùng khi tìm kiếm không ra kết quả, bộ lọc loại hết mục, hoặc danh sách đã bị làm trống. Các nút cho người dùng lối đi tiếp: quay lại, xóa bộ lọc, hoặc thử truy vấn khác. |
| EmptyState — Compact | Trạng thái rỗng nhỏ hơn, khoảng cách hẹp cho vùng bị giới hạn. Dùng trong panel sidebar, widget card, hoặc drawer thông báo, nơi trạng thái rỗng cỡ đầy đủ sẽ lấn át bố cục. |
| EmptyState — Container | Trạng thái rỗng bọc trong Card cho thiết lập lần đầu hoặc onboarding. Dùng khi người dùng chưa tạo mục nào, như danh sách dự án, danh sách nhóm hoặc widget dashboard sẽ có dữ liệu khi họ hành động. |
| Empty State | Trạng thái không có kết quả với icon, thông điệp mô tả và nút kêu gọi hành động. |

## Heading

`Heading` · Figma: `Heading` · trang **Content**

**Usage.** Component heading có ngữ nghĩa, hiển thị phần tử h1–h6 với kiểu theo theme, cỡ theo token thang chữ, và cắt dòng bằng line-clamp.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| Heading — Card Grid | Lưới card responsive với heading và mô tả bị cắt dòng để bố cục đồng đều. |
| Heading — Page Hierarchy | Bố cục trang thực tế minh họa heading cấp h1 tới h3 kèm chữ phụ. |
| Heading — Truncation | Cắt heading một dòng và nhiều dòng có dấu ba chấm cho bố cục hẹp. |

## Icon

`Icon` · Figma: `Icon` (trang Icons)

**Usage.** Icon là ký hiệu hình nhỏ đại diện cho hành động, đối tượng hoặc khái niệm. Chúng giúp dễ lướt và củng cố nghĩa bên cạnh chữ. Hỗ trợ cả component SVG trực tiếp và tên icon ngữ nghĩa thích ứng theo theme đang dùng.

**Nên**

- ✅ Dùng tên icon ngữ nghĩa khi có; chúng tự thích ứng khi theme đổi.
- ✅ Ghi đè icon qua theme, không ghi đè toàn cục: defineTheme({icons: {close: <XMarkIcon />}}) giới hạn việc thay trong <Theme> đang dùng, và extends gộp nông vào theme dẫn xuất. registerIcons() sửa registry toàn tiến trình và cảnh báo khi phát triển, nên chỉ dùng lúc khởi động app, không dùng làm điểm tùy biến theme cho thư viện.
- ✅ Ghép icon với nhãn chữ cho trợ năng; phần tử chỉ có icon cần nhãn truy cập.
- ✅ Với icon đứng riêng có nghĩa (không có chữ bên cạnh), đặt tên truy cập qua prop `label`: nó đặt role="img" + aria-label và bỏ ẩn icon.
- ✅ Dùng token màu cho màu icon, không dùng mã hex cứng.
- ✅ Lưu ý ngữ cảnh; icon trang trí trong component gọn có thể gây phân tâm thay vì giúp ích.

**Không nên**

- ❌ Dùng icon làm cách duy nhất để truyền nghĩa; luôn có phương án chữ.
- ❌ Đổi cỡ icon bằng giá trị pixel tùy ý; dùng prop size có sẵn.
- ❌ Trộn kiểu icon (ví dụ viền và đặc) trong cùng ngữ cảnh.
- ❌ Hiển thị phần tử SVG thô; luôn bọc trong Icon để cỡ và màu nhất quán.
- ❌ Truyền prop `name`; Icon dùng `icon` (không phải `name`) để chỉ định icon.

**Examples**

| Example | Mô tả |
|---|---|
| Icon — Non-Semantic Colors | Bảng màu không ngữ nghĩa cho icon. |
| Icon — Semantic Colors | Mọi biến thể màu icon ngữ nghĩa kèm nhãn. |
| Icon — Size Variants | Mọi cỡ icon từ rất nhỏ tới lớn. |
| Icon — Status Indicators | Danh sách trạng thái dùng icon ngữ nghĩa cho thành công, cảnh báo, lỗi và thông tin. |

## Kbd

`Kbd` · Figma: `Kbd` · trang **Content**

**Usage.** Hiển thị phím tắt dưới dạng badge phím. Dùng Kbd trong tooltip, menu và chữ trợ giúp để chỉ tổ hợp phím.

**Nên**

- ✅ Đặt phím tắt gần hành động nó kích hoạt: trong tooltip, mục menu hoặc hướng dẫn trong dòng.
- ✅ Dùng mod thay cho ctrl hoặc cmd; nó tự thích ứng theo nền tảng của người dùng.

**Không nên**

- ❌ Dùng Kbd làm cách duy nhất để khám phá một hành động; phím tắt bổ sung cho control hiển thị, không thay thế chúng.

**Examples**

| Example | Mô tả |
|---|---|
| Kbd — Inline Instructions | Phím tắt hiển thị trong dòng chữ hướng dẫn. |
| Kbd — Menu Shortcuts | Danh sách kiểu menu ghép nhãn hành động với phím tắt. |
| Kbd — Modifier Combinations | Tổ hợp phím bổ trợ và phím đặc biệt hiển thị dưới dạng badge phím tắt. |

## Markdown

`Markdown` · Figma: `Markdown` · trang **Content**

**Usage.** Hiển thị chuỗi markdown thành các component theo kiểu Astryx. Dùng Markdown cho nội dung người dùng tạo, câu trả lời AI và tài liệu; nó xử lý heading, danh sách, bảng, code block và citation với kiểu nhất quán.

**Nên**

- ✅ Đặt headingLevelStart khớp thứ bậc trang, ví dụ bắt đầu từ 3 nếu markdown nằm trong một section h2.
- ✅ Dùng contentWidth để giữ văn xuôi ở độ dài dòng dễ đọc trong bố cục rộng.
- ✅ Dùng plugin tạo bởi createMarkdownPlugin cho cú pháp tái sử dụng, biến đổi AST bất biến và hiển thị phần mở rộng có kiểu. Giữ thứ tự danh sách ổn định khi cấu hình cú pháp không đổi.
- ✅ Thêm markdownSoftBreaksPlugin khi xuống dòng đơn có ý nghĩa. Nó khớp remark-breaks với Markdown được hỗ trợ, kể cả nhãn liên kết nhiều dòng; code và nội dung mờ khác giữ nguyên.
- ✅ Dùng createMarkdownTextTransform để khớp văn xuôi; nó bảo vệ code, liên kết, ảnh, citation, công thức toán và cú pháp mở rộng được chấp nhận. Chỉ cung cấp requiredSubstrings khi chúng bao phủ an toàn mọi trường hợp khớp.
- ✅ Dùng createMarkdownFenceTransform cho ngôn ngữ code-fence đã khai báo có dữ liệu ngữ nghĩa. createNode trả về một node mở rộng dạng khối; renderer plugin chuẩn và toText của nó lo phần hiển thị. components.code vẫn thắng, và đề xuất bị từ chối hoặc lỗi thì giữ CodeBlock dự phòng truy cập được, sao chép được.
- ✅ Dùng createMarkdownSourceDecoration để gắn metadata không hiển thị (kết quả tìm, chú thích review) vào các khối mà một khoảng nguồn chạm tới, và getMarkdownSourceDecorations để đọc lại ở plugin sau. Decoration xuất hiện trên tài liệu đã ổn định chứ không trên các mảnh đang stream, và không bao giờ đổi hiển thị, chữ sao chép, tên truy cập, id, thứ tự focus hay điều hướng.
- ✅ Import parseMarkdownAst hoặc parseInlineAst từ @astryxdesign/core/Markdown/parser khi code server hoặc React Server Component cần chạy plugin trên cây chỉ đọc chuẩn. Subpath parser và plugin không có ranh giới use-client. Component Markdown vẫn thuộc client, nên mục plugin chứa hàm không được truyền qua ranh giới tuần tự hóa RSC.
- ✅ Dùng createMarkdownFrontmatter cho metadata tài liệu có kiểu. Phương thức parse() đưa metadata trực tiếp cho host; plugin của nó bỏ khối đầu hoàn chỉnh trước khi hiển thị và giữ lại khối chưa xong khi stream.
- ✅ Import createMarkdownRemarkTransform từ '@astryxdesign/core/Markdown/remark' chỉ để tái sử dụng plugin Remark đồng bộ chỉ-biến-đổi có sẵn; nó nằm ngoài mọi bundle khác. Kiểm chứng từng plugin bằng fixture: mọi thứ ngoài tập MDAST được hỗ trợ (việc bất đồng bộ, plugin parser/compiler, state của processor, HTML thô, node không hỗ trợ, vị trí giả, metadata Astryx không biểu diễn được) sẽ giữ tài liệu hợp lệ gần nhất và báo một chẩn đoán.
- ✅ Dùng inlinePlugins cho định danh có tiền tố, nhắc tên và các cách viết tắt chỉ trong văn xuôi, thay vì tiền xử lý chuỗi markdown.
- ✅ Chỉ cung cấp components.math cho tài liệu dùng công thức toán giữa dấu đô la. Renderer lo dàn trang và đầu ra truy cập được; Astryx truyền biểu thức dạng chữ và không bao giờ chạy HTML thô.
- ✅ Khi parse trực tiếp, dùng MathParseOptions và xử lý InlineNodeWithMath hoặc BlockNodeWithMath. Parse toán tăng dần cũng dùng createIncrementalState<true>() và IncrementalParseState<true>; lời gọi mặc định và chú thích ParseOptions giữ các union cũ.
- ✅ Ghép với Outline và useOutlineFromMarkdown để điều hướng theo phần: heading được sinh thuộc tính id khớp id mục outline, nên liên kết hash cuộn tới đúng đích.

**Không nên**

- ❌ Dùng Markdown cho bố cục tự viết tay; dùng Text và Heading trực tiếp khi bạn kiểm soát nội dung.

**Examples**

| Example | Mô tả |
|---|---|
| Markdown — Cited Content | Markdown có chip citation liên kết tới nguồn bên ngoài. |
| Markdown — Compact AI Response | Markdown gọn cho câu trả lời AI với cấp heading dịch xuống. |
| Markdown — Data Table | Bảng so sánh hiển thị từ chuỗi markdown. |
| Markdown — Rich Content | Markdown có heading, danh sách, code block, bảng, trích dẫn và danh sách việc. |
| Markdown | Nội dung markdown phong phú với heading, danh sách và định dạng. |

## Text

`Text` · Figma: `Text` · trang **Content**

**Usage.** Text hiển thị chữ thân và heading theo kiểu của theme. Dùng Text với type ngữ nghĩa cho chữ thân, nhãn và chú thích, và Heading cho tiêu đề phần để xuất đúng phần tử h1–h6.

**Nên**

- ✅ Chọn type ngữ nghĩa (body, label, supporting, large, code) thay vì tự đặt cỡ và độ đậm; theme lo chi tiết.
- ✅ Đặt accessibilityLevel trên Heading khi cấp hiển thị khác dàn ý tài liệu để trình đọc màn hình đọc đúng thứ bậc.
- ✅ Dùng maxLines với một số để cắt nội dung dài; tooltip tự hiện khi hover nên không mất chữ.
- ✅ Bật hasTabularNumbers cho cột số liệu để chữ số thẳng hàng dọc giữa các dòng.

**Không nên**

- ❌ Ghi đè cỡ và độ đậm khi đã có type ngữ nghĩa khớp; ghi đè thêm chống lại theme và vỡ khi theme đổi.
- ❌ Nhảy cấp heading trong dàn ý tài liệu; đi h1 rồi h2 rồi h3, không bao giờ h1 rồi h3.
- ❌ Dùng thẻ HTML thô như <p>, <h1>–<h6> hay <span> cho chữ; Text và Heading tự áp đúng token theme.
- ❌ Truyền prop `variant`; Text không có prop `variant`. Dùng `type` cho kiểu ngữ nghĩa (body, label, large, supporting, code) hoặc dùng Heading cho heading.
- ❌ Dùng Text cho heading; dùng Heading với prop `level` (1–6) cho tiêu đề phần và heading.

**Examples**

| Example | Mô tả |
|---|---|
| Text — Colors | Mọi lựa chọn màu chữ (primary, secondary, disabled, placeholder, active) áp lên chữ thân để thấy mục đích dùng. |
| Text — Heading Levels | Cả 6 cấp heading (h1 tới h6) hiển thị bằng Heading để thấy trọn thang chữ. |
| Text — Inline | Trộn chữ body và code trong cùng một dòng bằng chế độ hiển thị inline mặc định. |
| Text — Truncation | Cắt chữ một dòng và nhiều dòng có dấu ba chấm bằng maxLines trong vùng chứa giới hạn bề rộng. |
| Text — Types | Cả 5 type chữ ngữ nghĩa (body, large, label, supporting, code) với kiểu mặc định từ theme. |
| Text — Weight | 4 độ đậm (normal, medium, semibold, bold) áp lên chữ thân. |
| Text — Word Break | So sánh chế độ ngắt từ break-word và break-all trên một chuỗi dài không ngắt được. |
| Text — Wrap | 4 chế độ xuống dòng (wrap, nowrap, balance, pretty) trong vùng chứa giới hạn bề rộng. |

## Thumbnail

`Thumbnail` · Figma: `Thumbnail` · trang **Content**

**Usage.** Thumbnail hiển thị bản xem trước vuông, gọn của một ảnh đính kèm. Nó hiện hiệu ứng shimmer khi đang tải lên, ảnh khi thành công, và icon giữ chỗ khi chưa có nguồn. Dùng trong chat composer, danh sách tải tệp lên, hoặc nơi cần xem trước ảnh nhỏ kèm hành động gỡ và bấm (tùy chọn).

**Nên**

- ✅ Luôn cung cấp prop label là tên tệp để thumbnail và nút gỡ truy cập được với trình đọc màn hình và hiện tooltip khi hover.
- ✅ Dùng isLoading không kèm src để hiện skeleton khi đang tải lên lần đầu, và isLoading kèm src để hiện lớp spinner khi đã có URL xem trước.
- ✅ Ghép onClick với lightbox hoặc màn chi tiết để người dùng xem ảnh đầy đủ; thumbnail tự thêm ngữ nghĩa nút và lớp phủ khi hover.

**Không nên**

- ❌ Dùng Thumbnail cho tệp không phải ảnh như PDF hay bảng tính; dùng component tệp đính kèm có icon phù hợp.
- ❌ Bỏ alt khi có src; trình đọc màn hình cần mô tả nội dung ảnh, không chỉ tên tệp từ label.

**Examples**

| Example | Mô tả |
|---|---|
| Thumbnail — Disabled | Thumbnail ở trạng thái vô hiệu, độ mờ giảm. Nút gỡ và xử lý bấm bị tắt khi vô hiệu. |
| Thumbnail — Gallery | Hàng thumbnail bấm được có nhãn, mở màn chi tiết. Dùng cho danh sách ảnh đính kèm khi người dùng cần xem trước và quản lý tệp tải lên. |
| Thumbnail — Removable | Thumbnail có lớp nút gỡ. Nút đóng dùng phát hiện độ sáng APCA để luôn nhìn thấy trên cả ảnh tối và sáng. |
| Thumbnail | Thumbnail có ảnh và nhãn. |
| Thumbnail — States | Mọi trạng thái hình ảnh cạnh nhau: đã tải ảnh, giữ chỗ, skeleton đang tải và lớp đang tải lên. Minh họa trọn vòng đời thumbnail từ rỗng tới đã tải. |

## Timestamp

`Timestamp` · Figma: `Timestamp` · trang **Content**

**Usage.** Timestamp định dạng giá trị ngày hoặc giờ thành chữ dễ đọc. Dùng để cho biết thứ gì được tạo, cập nhật hoặc lên lịch khi nào; chọn tương đối cho độ mới, tuyệt đối cho độ chính xác, hoặc auto để component tự quyết.

**Nên**

- ✅ Dùng định dạng auto trong feed và danh sách để mục mới hiện "2 giờ trước" và mục cũ tự hiện ngày đầy đủ.
- ✅ Giữ định dạng nhất quán trong cùng danh sách hoặc bảng; trộn thời gian tương đối và tuyệt đối trong một cột làm rối khi lướt.
- ✅ Bật isTimezoneShown khi người xem ở nhiều múi giờ, như lịch nhóm toàn cầu hoặc nhật ký kiểm toán.
- ✅ Dùng tooltipEntries khi người đọc phải so sánh múi giờ, như nhật ký sự cố nơi cả giờ của người đọc và múi giờ gốc của sự kiện đều quan trọng.
- ✅ Gắn nhãn mọi mục khi tooltip hiện hơn một múi giờ; chữ viết tắt trần không phải lúc nào cũng nhận ra được (Tokyo hiện "GMT+9", không phải "JST").
- ✅ Dùng isLive cho dashboard đang hoạt động hoặc feed thời gian thực để thời gian tương đối luôn đúng mà không tải lại trang.
- ✅ Dùng tooltipEntries khi người đọc cần lấy giá trị chính xác: nhật ký sự cố hoặc bản ghi deploy nơi ai đó dán giờ UTC hoặc giây Unix sang chỗ khác; cấu hình entries biến phần hover thành các dòng bấm-để-sao-chép.

**Không nên**

- ❌ Hiện timestamp Unix thô hoặc chuỗi ISO cho người dùng; luôn đưa qua Timestamp để có định dạng dễ đọc.
- ❌ Tránh định dạng system_date hoặc system_time trong giao diện người dùng; chúng dành cho công cụ lập trình viên, log và ngữ cảnh máy đọc.
- ❌ Tắt hover card trên thời gian tương đối; người dùng mong hover để thấy ngày đầy đủ khi thấy "3 giờ trước".
- ❌ Chồng nhiều múi giờ vào một card; card rộng tối đa 300px và dòng có nhãn dài sẽ xuống dòng. Hai hoặc ba mục là dễ đọc.
- ❌ Truyền chữ viết tắt độ lệch cố định như "EST" làm timezoneID; nó là định danh hợp lệ nhưng không theo giờ mùa hè, nên sai một giờ trong nửa năm. Dùng id vùng, "America/New_York".

**Examples**

| Example | Mô tả |
|---|---|
| Timestamp — Auto | Định dạng auto hiện thời gian tương đối cho ngày gần và chuyển sang ngày đầy đủ cho ngày cũ. Lựa chọn mặc định cho đa số trường hợp. |
| Timestamp — Colors | Timestamp ở từng biến thể màu: primary, secondary, disabled và active. |
| Timestamp — Formats | Mọi định dạng hiển thị cạnh nhau: date, date_time, time và bản system tương ứng. Dùng date và date_time cho giao diện người dùng, bản system cho log và công cụ lập trình. |
| Timestamp — Relative | Nhãn thời gian tương đối từ vài giây tới vài tháng trước, có tooltip hiện ngày đầy đủ khi hover. Dùng trong feed, luồng bình luận và nhật ký hoạt động. |
| Timestamp — Timezone | Timestamp có gắn chữ viết tắt múi giờ. Bật isTimezoneShown cho người xem ở nhiều múi giờ, như nhật ký kiểm toán hay lịch nhóm. |
| Timestamp — Tooltip time zones | Tooltip khi hover hiện một thời điểm theo nhiều múi giờ hoặc định dạng. Dùng tooltipEntries khi người đọc phải so sánh múi giờ, như nhật ký sự cố mang cả giờ của người đọc và múi giờ gốc của sự kiện. |

## Token

`Token` · Figma: `Token` · trang **Content**

**Usage.** Token là phần tử nhỏ trong dòng biểu diễn các mẩu dữ liệu liên quan rời rạc, như thẻ, danh mục hoặc lựa chọn. Dùng để gắn nhãn nội dung, hiện bộ lọc đang áp, hoặc biểu diễn mục gỡ được như người nhận đã chọn trong ô soạn thư.

**Nên**

- ✅ Dùng màu để phân biệt danh mục (ví dụ xanh lá cho "Đang hoạt động", đỏ cho "Bị chặn", xanh dương cho "Đang xét duyệt") để người dùng lướt trạng thái nhanh.
- ✅ Cung cấp callback onRemove khi token biểu diễn lựa chọn của người dùng có thể hoàn tác, như bộ lọc hoặc giá trị chọn nhiều.
- ✅ Thêm icon đầu khi nó giúp nhận ra loại token nhanh hơn, như icon người cho token người dùng hoặc icon thẻ cho nhãn.
- ✅ Giữ nhãn ngắn: một tới ba từ. Token cắt bằng dấu ba chấm khi chữ tràn.

**Không nên**

- ❌ Dùng token cho hành động chính hoặc điều hướng; dùng Button hoặc Link. Token để hiển thị metadata, không để kích hoạt quy trình.
- ❌ Ẩn nhãn trừ khi chỉ icon đã được hiểu phổ biến. Chấm màu không có chữ là mơ hồ.
- ❌ Trộn quá nhiều màu trong một nhóm token. Giữ hai hoặc ba màu có nghĩa để bảng màu dễ lướt.

**Examples**

| Example | Mô tả |
|---|---|
| Token — Clickable | Token tương tác phản hồi khi bấm. Dùng cho bộ lọc bật/tắt hoặc token mở màn chi tiết khi được chọn. |
| Token — Colors | Cả 11 biến thể màu ở trạng thái mặc định và vô hiệu. Dùng màu để phân loại thực thể hoặc truyền tải trạng thái nhanh. |
| Token — End Content | Token có nội dung cuối như badge số đếm hoặc chỉ báo trạng thái sau nhãn. Dùng cho số thông báo, số lượng mục hoặc thông tin trạng thái gọn. |
| Token — Icon | Token có icon đầu cho biết loại thực thể. Dùng khi icon giúp người dùng nhận ra loại token nhanh hơn, như icon người cho người hoặc icon thẻ cho nhãn. |
| Token — Removable | Token có nút bỏ cho lựa chọn người dùng có thể hoàn tác. Dùng trong trường chọn nhiều, bộ lọc đang áp, hoặc danh sách mục người dùng đã chọn. |

---

# Feedback & Status

## Badge

`Badge` · Figma: `Badge` · trang **Feedback & Status**

**Usage.** Badge làm nổi một trạng thái hoặc danh mục trong nháy mắt. Dùng tiết chế: chỉ khi giá trị là một trạng thái riêng biệt (Đang hoạt động, Thất bại) hoặc một thẻ nhóm (Kỹ thuật, Thiết kế). Phần lớn metadata (ngày, thời lượng, số đếm, mô tả) nên là chữ mô tả thường, không phải badge.

**Nên**

- ✅ Mỗi badge trạng thái đều giành sự chú ý. Chỉ gắn badge cho trạng thái người dùng cần để ý hoặc cần hành động: lỗi, cảnh báo, mục cần theo dõi tiếp. Không cần hành động thì chữ thường là đủ.
- ✅ Chỉ dùng biến thể success, warning, error cho trạng thái hệ thống cần chú ý: "Thất bại", "Suy giảm", "Cần xử lý". Chúng có nền đặc đậm được thiết kế để nổi bật.
- ✅ Dùng biến thể màu (blue, purple, teal, v.v.) cho thẻ danh mục để nhóm hoặc phân loại mục: tên nhóm, loại nội dung, mức ưu tiên.
- ✅ Giữ nhãn một hoặc hai từ. Cần chi tiết hơn thì đặt trong chữ xung quanh thay vì trong badge.
- ✅ Thêm icon khi nó giúp nhận ra loại badge nhanh, nhưng luôn kèm nhãn chữ.

**Không nên**

- ❌ Gắn badge "success" cho mọi mục khỏe/đang hoạt động/bình thường. Nếu mọi dòng đều có badge xanh "Đang hoạt động", không cái nào nổi bật; badge thêm nhiễu chứ không thêm thông tin. Chỉ hiện trạng thái cần người dùng chú ý (lỗi, cảnh báo, việc đang chờ).
- ❌ Dùng badge cho metadata. Thời lượng ("cửa sổ 6 giờ"), số đếm ("12 loại trigger"), ngày và mô tả không phải trạng thái hay danh mục; dùng chữ mô tả (Text với type="supporting").
- ❌ Dùng biến thể trạng thái ngữ nghĩa (success, warning, error, info) cho danh mục hoặc nội dung thông tin. Chúng rất nổi về thị giác và chỉ nên báo trạng thái hệ thống.
- ❌ Lặp cùng một badge ở mọi dòng của bảng hoặc danh sách. Nếu cùng giá trị xuất hiện ở hầu hết các dòng, nó không thêm thông tin; dùng chữ thường cho trạng thái phổ biến và để dành badge cho trường hợp ngoại lệ.
- ❌ Làm badge bấm được; chúng là chỉ báo chỉ đọc. Dùng nút hoặc liên kết nếu người dùng cần hành động.

**Examples**

| Example | Mô tả |
|---|---|
| Badge — Colors | Gắn thẻ mục theo danh mục mã màu như nhóm, mức ưu tiên, chủ đề. Dùng 9 biến thể màu không ngữ nghĩa khi cần phân biệt nhóm bằng mắt. |
| Badge — Counts | Hiện số trong badge cho số thông báo, tin chưa đọc hoặc tổng việc. Dùng cạnh icon, mục điều hướng hoặc nhãn danh sách. |
| Badge — Variants | Mọi biến thể badge ngữ nghĩa và màu trong một khung. Biến thể ngữ nghĩa cho trạng thái, biến thể màu cho danh mục. |
| Badge — Status | Hiện trạng thái của một mục như Đang hoạt động, Đang chờ, Thất bại. Dùng trong dòng bảng, mục danh sách hoặc trang chi tiết khi người dùng cần thấy trạng thái nhanh. |

## Banner

`Banner` · Figma: `Banner` · trang **Feedback & Status**

**Usage.** Banner hiển thị thông điệp cố định ở đầu trang hoặc đầu một phần. Dùng cho lỗi form, cập nhật hệ thống, thông báo bảo trì, hoặc xác nhận thành công mà người dùng cần thấy cho tới khi xử lý.

**Nên**

- ✅ Chọn status khớp thông điệp: info cho cập nhật, warning cho thận trọng, error cho sự cố, success cho xác nhận.
- ✅ Dùng container card bên trong nội dung trang và container section cho thông điệp tràn hết bề rộng trang.
- ✅ Cho phép đóng banner info và success. Giữ banner lỗi hiển thị cho tới khi người dùng sửa xong.
- ✅ Giữ tiêu đề ngắn, dễ lướt: "Thanh toán thất bại" thay vì "Đã có sự cố khi xử lý khoản thanh toán gần nhất của bạn."
- ✅ Đặt collapsible={false} khi người dùng cần nội dung để xử lý thông điệp, như danh sách trường bị lỗi kiểm tra. Giữ nút thu gọn mặc định khi chi tiết đủ dài để che lấp thông điệp chính của banner.
- ✅ Banner error và warning hiển thị với role="alert"; info và success với role="status". Gắn banner alert để phản hồi một sự kiện chứ không ngay lần vẽ đầu, để công nghệ hỗ trợ có thay đổi để báo.

**Không nên**

- ❌ Dùng Banner cho thông điệp ngắn hạn tự biến mất; dùng Toast.
- ❌ Chồng nhiều banner cùng status; gộp các thông điệp liên quan vào một banner.
- ❌ Chỉ dựa vào màu hoặc icon trạng thái để mang nghĩa; nói rõ đó là trạng thái gì trong chữ tiêu đề, vì icon chỉ là trang trí với trình đọc màn hình.

**Examples**

| Example | Mô tả |
|---|---|
| Banner — Collapsible | Kết hợp nút hành động, nút đóng và vùng chi tiết thu gọn được trong một banner. Children mặc định nằm sau nút thu gọn; `collapsible={{defaultIsOpen: true}}` mở sẵn, `collapsible={false}` bỏ hẳn nút thu gọn. Dùng cho thông báo phức tạp như thay đổi cấu hình hoặc tóm tắt deploy. |
| Banner — Dismiss | Cho người dùng đóng banner sau khi đọc. Dùng cho thông báo bảo trì, mẹo tính năng, hoặc thông điệp không quan trọng mà người dùng có thể xác nhận đã đọc. |
| Banner — Floating | Banner nổi nâng bằng `elevation="med"`. Banner mặc định nằm trong dòng; nâng lên khi cần đọc như một lớp phủ trên nội dung. |
| Banner — Full Width | Banner tràn bề rộng, không bo góc, cho thông báo cấp trang. Dùng ở đầu trang cho thông báo toàn site hoặc cảnh báo bảo trì. |
| Banner — Statuses | Cả bốn status xếp chồng: info, success, warning và error. Tham chiếu nhanh để chọn đúng status. |
| Banner — Statuses | Cả 4 status: info, success, warning, error. Dùng để hiện thông điệp cố định như cập nhật, xác nhận, thận trọng hay sự cố ở đầu trang hoặc phần. |
| Banner — Action | Thêm nút vào banner để người dùng xử lý thông điệp. Dùng cho hết hạn dùng thử, thanh toán thất bại, hoặc việc cần phản hồi. |

## Progress Bar

`ProgressBar` · Figma: `ProgressBar` · trang **Feedback & Status**

**Usage.** Thanh ngang thể hiện tiến độ hoàn thành của một tác vụ. Dùng cho thao tác biết trước thời lượng, hoặc làm chỉ báo động khi không tính được tiến độ. Hỗ trợ biến thể màu ngữ nghĩa, nhãn giá trị và định dạng tùy biến.

**Nên**

- ✅ Dùng thanh xác định khi biết tổng khối lượng việc, và không xác định khi không biết.
- ✅ Chọn biến thể màu khớp ngữ cảnh: accent cho tiến độ chung, success cho hoàn thành, warning hoặc error cho cảnh báo.
- ✅ Luôn có label, kể cả khi ẩn; trình đọc màn hình cần nó để báo cái gì đang tải.

**Không nên**

- ❌ Đặt icon hoặc nhãn bên trong thanh; ghép chúng bên cạnh bằng component bố cục.
- ❌ Dùng thanh tiến độ cho hành động tức thì; nó dành cho thao tác tốn thời gian đáng kể.
- ❌ Chồng nhiều thanh tiến độ cho cùng một thao tác; dùng một thanh có nhãn giá trị.

**Examples**

| Example | Mô tả |
|---|---|
| ProgressBar — Custom Format | Thanh tiến độ có nhãn giá trị tùy biến hiện dung lượng đĩa theo GB. |
| ProgressBar — Indeterminate | Thanh tiến độ không xác định cho thao tác không rõ thời lượng. |
| ProgressBar — Semantic Variants | Mọi biến thể màu ngữ nghĩa xếp dọc. |
| Progress Bar | Thanh tiến độ đầy 60%. |
| ProgressBar — With Value Label | Thanh tiến độ hiện phần trăm hiện tại. |

## Skeleton

`Skeleton` · Figma: `Skeleton` · trang **Feedback & Status**

**Usage.** Khối giữ chỗ có hiệu ứng shimmer, xem trước hình dạng nội dung khi đang tải. Dùng để dựng màn đang tải khớp bố cục nội dung thật. Nội dung chưa rõ kích thước thì dùng Spinner.

**Nên**

- ✅ Khớp cỡ và hình dạng nội dung đang tải để tạo giữ chỗ giống thật.
- ✅ So le nhiều skeleton bằng prop `index` để có hiệu ứng sóng tự nhiên.

**Không nên**

- ❌ Dùng khi chưa rõ kích thước nội dung; dùng Spinner.
- ❌ Kết hợp với Spinner trên cùng vùng nội dung; chọn một kiểu đang tải.
- ❌ Hiện skeleton vô thời hạn; nếu tải quá lâu, hiện trạng thái lỗi hoặc rỗng.

**Examples**

| Example | Mô tả |
|---|---|
| Skeleton — Card Loading | Skeleton card có avatar, tên và các dòng nội dung. |
| Skeleton | Khối giữ chỗ skeleton đang tải. |
| Skeleton — Staggered List | Các dòng skeleton so le với bề rộng khác nhau. |
| Skeleton — Table Rows | Skeleton bảng với bề rộng cột so le. |

## Spinner

`Spinner` · Figma: `Spinner` · trang **Feedback & Status**

**Usage.** Chỉ báo đang tải có hiệu ứng cho tiến trình không rõ thời lượng, như lấy dữ liệu hoặc gửi form. Hỗ trợ nhãn hiển thị, nhiều cỡ và biến thể nền tối. Nội dung đã biết kích thước thì dùng Skeleton.

**Nên**

- ✅ Cung cấp nhãn có nghĩa mô tả cái gì đang tải cho người dùng trình đọc màn hình.
- ✅ Dùng shade "onMedia" khi đặt trên nền tối hoặc nền màu nhấn.

**Không nên**

- ❌ Dùng cho vùng nội dung đã biết kích thước; dùng Skeleton để giữ bố cục.
- ❌ Chồng nhiều spinner trong cùng màn; dùng một cái đại diện cho trạng thái đang tải chung.

**Examples**

| Example | Mô tả |
|---|---|
| Spinner — On Media Shade | Spinner shade mặc định và onMedia cho nền sáng và tối. |
| Spinner | Chỉ báo spinner cỡ lớn. |
| Spinner — Sizes | Mọi cỡ spinner đặt cạnh nhau. |
| Spinner — With Label | Spinner có chữ và nhãn nhiều dòng phong phú. |

## Status Dot

`StatusDot` · Figma: `StatusDot` · trang **Feedback & Status**

**Usage.** Chấm màu nhỏ truyền tải trạng thái như trực tuyến/ngoại tuyến hoặc mức độ nghiêm trọng. Hỗ trợ năm biến thể ngữ nghĩa và hiệu ứng nhấp nháy (tùy chọn). Luôn ghép với nhãn chữ hiển thị, vì chỉ màu không được mang nghĩa.

**Nên**

- ✅ Dùng StatusDot như tín hiệu nhị phân có/không; tránh mã hóa nhiều trạng thái khác nhau trong một chấm, vì chỉ màu và cỡ không phân biệt được chúng một cách tin cậy.
- ✅ Luôn ghép với nhãn chữ hiển thị để trạng thái không chỉ truyền bằng màu.
- ✅ Cung cấp prop `label` mô tả cho trợ năng trình đọc màn hình.
- ✅ Ghép chấm với một icon mang trạng thái bằng hình dạng riêng khi chấm phải đứng một mình không có chữ bên cạnh, để nghĩa vẫn còn khi không có màu.
- ✅ Nếu không thêm được nhãn hay icon, bảo đảm trạng thái được truyền tải ở chỗ khác một cách truy cập được (ví dụ chữ bên cạnh, một cột bảng, hoặc vùng live).

**Không nên**

- ❌ Chỉ dựa vào màu để truyền tải trạng thái; StatusDot đứng riêng không hoàn toàn truy cập được, nên người dựng phải làm trạng thái phân biệt được trong ngữ cảnh bằng nhãn, icon hoặc phương án truy cập khác.
- ❌ Dùng hiệu ứng nhấp nháy cho mục đích trang trí thuần túy; để dành cho trạng thái cần chú ý ngay.

**Examples**

| Example | Mô tả |
|---|---|
| StatusDot — Pulsing | Chấm nhấp nháy cho trạng thái trực tiếp, đang xử lý và lỗi. |
| Status Dot | Chấm trạng thái tích cực. |
| StatusDot — Status Indicators | Danh sách chấm trạng thái có nhãn cho chỉ báo hiện diện như trực tuyến, vắng, ngoại tuyến. |
| StatusDot — Variants | Cả năm biến thể màu ngữ nghĩa xếp thành hàng. |

---

# Form Controls

## Calendar

`Calendar` · Figma: `Calendar` · trang **Form Controls**

**Usage.** Calendar cho người dùng chọn một ngày hoặc khoảng ngày trên lưới tháng. Dùng trong luồng đặt chỗ, giao diện lập lịch, bộ lọc ngày, hoặc nơi người dùng cần thấy các ngày xung quanh làm ngữ cảnh.

**Nên**

- ✅ Đặt ngày min và max để giới hạn lựa chọn trong khoảng hợp lệ, như chỉ ngày tương lai khi đặt chỗ hoặc quý hiện tại cho báo cáo.
- ✅ Dùng chế độ range khi người dùng cần chọn ngày bắt đầu và kết thúc, như chuyến đi hoặc đơn xin nghỉ.
- ✅ Dùng dateConstraints để vô hiệu ngày cụ thể như cuối tuần hoặc ngày lễ, và giải thích vì sao chúng không chọn được.
- ✅ Hiện hai tháng cạnh nhau khi người dùng thường chọn khoảng ngày vắt qua ranh giới tháng.

**Không nên**

- ❌ Dùng lịch cho ngày quá xa trong quá khứ hoặc tương lai như ngày sinh. Ô nhập chữ nhanh hơn cho nhập tự do.
- ❌ Vô hiệu cả khối ngày lớn mà không có ngữ cảnh. Người dùng phải hiểu vì sao ngày không chọn được.

**Examples**

| Example | Mô tả |
|---|---|
| Calendar — Constraints | Giới hạn ngày chọn được bằng biên min/max và quy tắc tùy biến như chỉ ngày trong tuần. Dùng cho giao diện lập lịch khi có ngày không khả dụng. |
| Calendar — Range | Chọn ngày bắt đầu và kết thúc, khoảng giữa được tô nổi. Dùng cho ngày đặt chỗ, đơn xin nghỉ hoặc bộ lọc báo cáo. |
| Calendar | Lịch chọn một ngày, tương tác được, có ngày đang chọn. Bấm ngày bất kỳ để đổi lựa chọn. |
| Calendar — Single | Chọn một ngày trên lưới tháng. Dùng cho ngày hẹn, hạn chót hoặc trường cần một ngày. |
| Calendar — Two Months | Hai tháng cạnh nhau để chọn khoảng vắt qua ranh giới tháng. Dùng trong giao diện đặt phòng hoặc du lịch khi ngày nhận và trả phòng thường rơi vào hai tháng khác nhau. |

## Checkbox Input

`CheckboxInput` · Figma: `Checkbox / CheckboxInput` (nhóm: `Checkbox / CheckboxList`) · trang **Form Controls**

**Usage.** CheckboxInput bật/tắt một giá trị đơn. Dùng cho cài đặt như "Bật thông báo", chấp nhận điều khoản, hoặc lựa chọn đồng ý tham gia. Nhiều checkbox trong một nhóm thì dùng CheckboxList.

**Nên**

- ✅ Luôn có nhãn hiển thị để người dùng biết mình đang bật/tắt cái gì. Chỉ dùng isLabelHidden khi ngữ cảnh xung quanh đã rõ ràng.
- ✅ Thêm mô tả cho lựa chọn cần thêm ngữ cảnh, như giải thích "Chia sẻ dữ liệu sử dụng" thực sự chia sẻ những gì.
- ✅ Dùng trạng thái indeterminate cho checkbox "chọn tất cả" khi chỉ một số mục trong nhóm được chọn.

**Không nên**

- ❌ Dùng checkbox cho lựa chọn loại trừ nhau; dùng RadioList khi chỉ chọn được một.
- ❌ Dùng checkbox cho hành động có hiệu lực ngay; dùng switch hoặc nút.
- ❌ Bọc checkbox bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| CheckboxInput — States | Checkbox có nhãn và mô tả ở trạng thái đã chọn, chưa chọn và vô hiệu. Mỗi checkbox điều khiển một cài đặt bật/tắt. Thêm mô tả để giải thích cài đặt làm gì. |
| CheckboxInput — Indeterminate | Checkbox "chọn tất cả" điều khiển một nhóm lựa chọn. Khi chỉ một số được chọn, nó hiện dấu gạch thay cho dấu tích. Bấm vào thì chọn hoặc bỏ chọn tất cả. |
| Checkbox Input | Checkbox tương tác ở trạng thái đã chọn, chưa chọn và indeterminate, có mô tả. |
| CheckboxInput — Status | Checkbox có thông điệp kiểm tra lỗi, cảnh báo và thành công. Dùng prop status để phản hồi sau khi kiểm tra form: lỗi chặn gửi, cảnh báo để thông tin, thành công để xác nhận. |

## Complex Selector

`ComplexSelector` · Figma: `ComplexSelector` · trang **Form Controls**

**Usage.** Dùng ComplexSelector khi một lựa chọn cần nội dung tùy biến phong phú hơn một dòng lựa chọn của Selector. Nó cố ý là một component duy nhất: ComplexSelector sở hữu field, trigger, popover, khôi phục focus và luồng changeAction, còn render prop content sở hữu cấu trúc truy cập riêng của bộ chọn.

**Nên**

- ✅ Dùng variant="ghost" kèm startIcon khi bộ chọn mở từ toolbar. Dùng alignment="end" khi bề mặt rộng cần căn mép cuối theo trigger.
- ✅ Với trình chỉnh sửa theo bước, giữ state nháp trong nội dung ghép và chỉ gọi helper onChange được cung cấp từ nút Áp dụng. Hủy hoặc đóng thì không ghi nhận.
- ✅ Ghép nội dung hộp thoại từ cấu trúc truy cập phù hợp với việc: RadioList cho lựa chọn đơn giản, Calendar/input ngày cho chọn ngày, TreeList hoặc danh sách tìm kiếm được cho phân cấp, hoặc lưới tùy biến khi điều hướng mũi tên hai chiều hữu ích.
- ✅ Dùng helper onChange được cung cấp từ children; nó đã gọi cả onChange và changeAction và cập nhật trạng thái bận lạc quan.
- ✅ Gọi close() từ nội dung tùy biến khi một lựa chọn cần đóng popup. Giữ mở cho nội dung nhiều bước hoặc luồng nhập tự do.
- ✅ Dùng hook focus của Astryx cho nội dung tùy biến: useGridFocus cho lưới hai chiều, useTreeFocus qua TreeList cho phân cấp, useListFocus cho tập tuyến tính tùy biến.
- ✅ Đánh giá nội dung tùy biến theo WCAG 2.2: thao tác bàn phím, focus nhìn thấy/không bị che, tên và vai trò, nhãn/hướng dẫn, cỡ vùng chạm, tương phản/tương phản phi chữ đặc biệt liên quan tới popover bộ chọn.

**Không nên**

- ❌ Tự dựng lại ARIA của trigger, quản lý focus popover hay xử lý changeAction trong code sản phẩm.
- ❌ Dùng ComplexSelector cho danh sách chữ một cột đơn thuần; dùng Selector.

**Examples**

| Example | Mô tả |
|---|---|
| Complex Selector — Deadline Picker | Trường hạn chót nhiều bước: chọn mốc có sẵn như Hôm nay hay Tuần sau, hoặc chuyển sang ngày giờ tùy chọn trước khi áp dụng. Popup mở cho tới khi người dùng ghi nhận, nên nội dung sở hữu hành động Áp dụng. |
| Complex Selector | Bộ chọn hai trục: chọn loại quả và độ chín trong một control. ComplexSelector sở hữu trigger, popover và khôi phục focus, còn lưới tùy biến sở hữu ngữ nghĩa bàn phím của nó. |
| Complex Selector — Tree Search | Bộ chọn đích đến kết hợp ô tìm kiếm với phân cấp TreeList. TreeList sở hữu điều hướng bàn phím dạng cây; ComplexSelector sở hữu trigger, popover và khôi phục focus. Chọn một thư mục thì popup đóng. |

## Date Input

`DateInput` · Figma: `DateInput` · trang **Form Controls**

**Usage.** DateInput cho người dùng gõ hoặc chọn ngày từ popover lịch. Dùng cho lập lịch, hạn chót, ngày đặt chỗ hoặc trường form cần một ngày cụ thể.

**Nên**

- ✅ Có nhãn và mô tả rõ để người dùng hiểu ngày nào được yêu cầu.
- ✅ Dùng min, max và dateConstraints để giới hạn ngày chọn được trong khoảng hợp lệ.
- ✅ Dùng hasClear khi ngày là tùy chọn để người dùng có thể đặt lại.
- ✅ Hiện trạng thái đang tải bằng changeAction khi ngày kích hoạt lưu phía server.
- ✅ Dùng DateInput trong InputGroup khi thêm tiền tố hoặc hậu tố tĩnh ngắn, như gợi ý hạn chót.

**Không nên**

- ❌ Dùng DateInput cho chữ tự do không biểu diễn ngày lịch.
- ❌ Ẩn nhãn khi không có ngữ cảnh xung quanh làm rõ mục đích trường.
- ❌ Chỉ dựa vào lịch; ô chữ cho người dùng gõ ngày trực tiếp, nhanh hơn với ngày đã biết.
- ❌ Bọc DateInput bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| DateInput — Clearable | Ô ngày có nút xóa để đặt lại giá trị. Dùng khi trường ngày là tùy chọn và người dùng có thể cần hoàn tác lựa chọn. |
| DateInput — Min/Max Constraints | Ô ngày bị giới hạn trong khoảng min/max. Dùng khi chỉ một số ngày hợp lệ, như lịch trống đặt chỗ hay một quý tài chính. |
| DateInput — Formats | Prop format dùng lại bộ từ vựng định dạng của Timestamp để điều khiển cách hiện giá trị đã ghi nhận: date, date_long (mặc định), date_weekday và system_date, hoặc một hàm cho chuỗi tùy biến hoàn toàn. Định dạng chỉ áp cho giá trị đã ghi nhận, không bao giờ áp cho chữ người dùng đang gõ. |
| Date Input | Ô nhập ngày có popover lịch. Gõ ngày hoặc bấm icon lịch để chọn. |
| DateInput — Description | Ô ngày có chữ trợ giúp dưới nhãn giải thích trường cần gì. Dùng khi chỉ nhãn chưa làm rõ mục đích của ngày. |
| DateInput — Validation | Ô ngày ở cả ba trạng thái: lỗi, cảnh báo và thành công. Dùng để báo lỗi kiểm tra, nhắc người dùng thận trọng, hoặc xác nhận lựa chọn hợp lệ. |

## Date Range Input

`DateRangeInput` · Figma: `DateRangeInput` · trang **Form Controls**

**Usage.** DateRangeInput cho người dùng chọn ngày bắt đầu và kết thúc từ popover lịch hai tháng. Dùng để lọc dữ liệu theo giai đoạn, tạo báo cáo, dashboard phân tích và luồng đặt chỗ.

**Nên**

- ✅ Dùng preset cho khoảng phổ biến như "7 ngày qua" để chọn nhanh hơn.
- ✅ Dùng min/max để giới hạn ngày chọn được trong khoảng hợp lệ.
- ✅ Giữ hasClear bật (mặc định) để người dùng có thể đặt lại bộ lọc.
- ✅ Có nhãn và mô tả rõ để người dùng hiểu khoảng ngày điều khiển cái gì.

**Không nên**

- ❌ Dùng DateRangeInput khi chỉ cần một ngày; dùng DateInput.
- ❌ Ẩn nhãn khi không có ngữ cảnh xung quanh làm rõ mục đích.
- ❌ Bọc DateRangeInput bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Date Range Input | Bộ chọn khoảng ngày có nút trigger và popover lịch hai tháng với các khoảng preset. |
| DateRangeInput — With Presets | Bộ chọn khoảng ngày có preset chọn nhanh cho giai đoạn phổ biến. Dùng cho dashboard phân tích, bộ lọc báo cáo, hoặc ngữ cảnh người dùng thường chọn khung thời gian chuẩn. |
| DateRangeInput — Validation | Ô khoảng ngày ở cả ba trạng thái: lỗi, cảnh báo, thành công. Dùng để báo trùng lịch đặt chỗ, đánh dấu giai đoạn cao điểm, hoặc xác nhận khoảng còn trống. |

## Date Time Input

`DateTimeInput` · Figma: `DateTimeInput` · trang **Form Controls**

**Usage.** DateTimeInput gộp chọn ngày và giờ trong một trường. Với nativePicker="touch" (mặc định), thiết bị chuột/trackpad dùng trường gõ và popover của Astryx, còn thiết bị con trỏ thô dùng control ngày giờ của trình duyệt/hệ điều hành trong cùng trường hai phần. nativePicker="always" dùng control gốc trên mọi loại con trỏ; nativePicker="never" giữ bề mặt riêng của Astryx: trường con trỏ trên con trỏ mịn và bottom sheet Ngày/Giờ phối hợp trên con trỏ thô. Hai phần khi đóng nằm cạnh nhau khi có ít nhất 400px và xuống thành các hàng tràn bề rộng khi dưới 400px, không phụ thuộc bề rộng viewport. Dùng cho lập lịch, tạo sự kiện, đặt hạn chót hoặc trường form cần một thời điểm cụ thể.

**Nên**

- ✅ Có nhãn và mô tả rõ để người dùng hiểu thời điểm nào được yêu cầu.
- ✅ Dùng min và max để giới hạn thời điểm chọn được trong khoảng hợp lệ.
- ✅ Dùng hasClear khi thời điểm là tùy chọn để người dùng có thể đặt lại.
- ✅ Chọn định dạng giờ (12h hoặc 24h) khớp locale của người dùng.

**Không nên**

- ❌ Dùng DateTimeInput khi chỉ cần ngày; dùng DateInput.
- ❌ Dùng DateTimeInput khi chỉ cần giờ; dùng TimeInput.
- ❌ Ẩn nhãn khi không có ngữ cảnh xung quanh làm rõ mục đích trường.
- ❌ Bọc DateTimeInput bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Date Time Input | Bộ chọn ngày và giờ kết hợp. Desktop mở popover lịch kèm ô giờ; thiết bị cảm ứng mở bottom sheet Ngày/Giờ. |
| DateTimeInput — Validation | DateTimeInput ở cả ba trạng thái: lỗi, cảnh báo, thành công. Dùng để báo trùng lịch, nhắc người dùng về trường hợp biên, hoặc xác nhận thời điểm hợp lệ. |

## Field

`Field` · Figma: `Field` · trang **Form Controls**

**Usage.** Field là lớp bọc cấp thấp cho control tùy biến, gốc hoặc bên thứ ba chưa có sẵn nhãn, mô tả và giao diện trạng thái. Dùng khi cần khung Field quanh một control bạn tự làm; dùng trực tiếp các input Astryx đã tạo kiểu như TextInput, Typeahead, Select khi chúng đã có prop nhãn, mô tả và kiểm tra.

**Nên**

- ✅ Bọc control tùy biến, input gốc hoặc widget bên thứ ba cần nhãn, chữ trợ giúp, chỉ báo tùy chọn/bắt buộc hoặc trạng thái kiểm tra.
- ✅ Luôn có nhãn cho trợ năng, kể cả khi ẩn về hình bằng isLabelHidden.
- ✅ Dùng inputID và descriptionID để nối nhãn và mô tả với control bên trong bằng htmlFor và aria-describedby.

**Không nên**

- ❌ Bọc Field quanh input đã tạo kiểu như TextInput, Typeahead, Select, DateInput, TextArea; các component đó đã tự vẽ khung Field.
- ❌ Dùng biến thể status attached trên control không viền như slider, switch, checkbox; dùng detached để thông điệp không chồng lên control.
- ❌ Đặt cả isOptional và isRequired trên cùng một trường.
- ❌ Ẩn nhãn mà không có cách khác để người dùng hiểu mục đích trường.

**Examples**

| Example | Mô tả |
|---|---|
| Field — Required & Optional | Chỉ báo bắt buộc và tùy chọn cạnh nhau. Dùng isRequired cho trường phải điền, isOptional để làm rõ trường có thể bỏ qua. |
| Field | Trường form bọc một text input kèm nhãn, mô tả và trạng thái kiểm tra. |
| Field — Validation States | Cả ba trạng thái kiểm tra: lỗi, cảnh báo, thành công. Lỗi cho nhập sai, cảnh báo cho vấn đề tiềm ẩn như tên đã được dành riêng, thành công để xác nhận nhập đúng như API key. |
| Field — Description | Trường có chữ trợ giúp dưới nhãn. Dùng mô tả để giải thích yêu cầu định dạng, ràng buộc, hoặc dữ liệu sẽ được xử lý thế nào, như "Ít nhất 8 ký tự" hay "Chúng tôi sẽ gửi liên kết xác nhận". |

## File Input

`FileInput` · Figma: `FileInput` · trang **Form Controls**

**Usage.** FileInput cho tải tệp lên, hỗ trợ kéo thả (tùy chọn). Dùng để chọn một hoặc nhiều tệp, có sẵn kiểm tra loại tệp, dung lượng và số lượng. Ghép với trạng thái kiểm tra để phản hồi việc tải lên.

**Nên**

- ✅ Luôn chỉ định prop accept để hướng người dùng tới loại tệp hợp lệ.
- ✅ Dùng maxSize và maxFiles để chặn tải lên quá cỡ; component tự kiểm tra và hiện lỗi.
- ✅ Thêm mô tả để nêu ràng buộc như giới hạn dung lượng hoặc định dạng được chấp nhận.
- ✅ Dùng changeAction cho luồng tải lên tức thì hưởng lợi từ giao diện lạc quan.

**Không nên**

- ❌ Dùng FileInput để tải lên thư mục; v1 không hỗ trợ.
- ❌ Tránh chế độ dropzone trừ khi chỗ hẹp; kéo thả là tương tác người dùng mong đợi khi tải tệp lên.
- ❌ Bọc FileInput bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| FileInput — Basic | Tải lên một tệp (controlled) có loại tệp chấp nhận, giới hạn dung lượng và chữ trợ giúp. Dùng cho trường tải tài liệu tiêu chuẩn trong form. |

## Multi Selector

`MultiSelector` · Figma: `Selector / MultiSelector` · trang **Form Controls**

**Usage.** Dropdown có checkbox để chọn nhiều giá trị từ một danh sách. Mục đã chọn có thể hiện dưới dạng số đếm, nhãn hoặc badge. Dùng để lọc, hoặc khi đưa ra một tập lựa chọn hữu hạn cần chọn nhiều.

**Nên**

- ✅ Dùng cho tập lựa chọn hữu hạn, vừa phải, cần chọn nhiều.
- ✅ Bật lọc tìm kiếm khi danh sách vượt ~15 lựa chọn.
- ✅ Dùng renderOption cho dòng lựa chọn tùy biến; phần checkbox vẫn do MultiSelector sở hữu.
- ✅ Bật chọn tất cả khi đa số người dùng sẽ muốn chọn tất cả hoặc gần hết.
- ✅ Chỉ dùng trong InputGroup khi control cần phần tiền tố hoặc hậu tố ngắn trên cùng một bề mặt input; ưu tiên hiển thị trigger dạng số đếm hoặc nhãn để nhóm giữ một dòng.
- ✅ Dùng variant="ghost" khi multi-selector nằm trong toolbar cùng nút Ghost. Nếu cần trạng thái kiểm tra ở đó, ưu tiên statusVariant="tooltip" để toolbar giữ chiều cao gọn.
- ✅ Dùng presentation="adaptive" khi multi-selector cần thành bottom sheet trên màn cảm ứng nhỏ.

**Không nên**

- ❌ Dùng để chọn một giá trị; dùng Selector.
- ❌ Hiện quá ~20 lựa chọn mà không bật tìm kiếm.
- ❌ Bọc MultiSelector bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| MultiSelector — Bottom Sheet | Giữ danh sách chọn nhiều mở trong bottom sheet trong khi bật/tắt các lựa chọn. |
| MultiSelector — Column Visibility | Bật/tắt hiển thị cột với nhãn ẩn, tìm kiếm, chọn tất cả và số đếm đã chọn. |
| MultiSelector — Form Composition | Hai multi-selector trong form với trạng thái bắt buộc/tùy chọn. |
| MultiSelector — Ghost Toolbar | Biến thể MultiSelector không viền ghép với nút Ghost trong toolbar. |
| MultiSelector — Searchable | Chọn nhiều có lọc tìm kiếm và chọn tất cả. |
| MultiSelector — Sectioned Permissions | Chọn nhiều với lựa chọn nhóm thành các section có nhãn. |

## Number Input

`NumberInput` · Figma: `NumberInput` · trang **Form Controls**

**Usage.** Input form cho giá trị số, có sẵn kiểm tra, ràng buộc min/max và nút bước. Dùng NumberInput cho số lượng, số đo, phần trăm và các input tương tự.

**Nên**

- ✅ Cho người dùng dán số đã định dạng: dán 1,234,234,234 sẽ được đọc theo locale của trường và ghi nhận thành 1234234234 khi rời ô. Không bao giờ chặn việc gõ.
- ✅ Đặt min, max và step để hướng người dùng tới giá trị hợp lệ.
- ✅ Hiện đơn vị (ví dụ "%" hay "GB") để người dùng biết con số biểu diễn gì.
- ✅ Đặt isWheelEnabled={false} khi input nằm trong bề mặt cuộn, nơi thao tác lăn chuột luôn phải cuộn trang.

**Không nên**

- ❌ Dùng NumberInput cho chữ tự do tình cờ chứa số; dùng TextInput.
- ❌ Đặt cả isOptional và isRequired trên cùng một trường.
- ❌ Bọc NumberInput bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| NumberInput — Clearable | Ô số có nút xóa, hậu tố đơn vị và ràng buộc min/max. |
| NumberInput — Range Constrained | Ô số có biên min/max và mô tả trợ giúp. |
| Number Input | Ô số để nhập số lượng. |
| NumberInput — Status Variants | Ô số ở trạng thái kiểm tra lỗi, cảnh báo và thành công. |
| NumberInput — With Units | Ô số có hậu tố đơn vị phần trăm và khoảng hợp lệ. |

## Power Search

`PowerSearch` · Figma: `PowerSearch / Popover`, `PowerSearch / Trigger` · trang **Form Controls**

**Usage.** PowerSearch là thanh lọc có cấu trúc, mỗi token biểu diễn một trường, toán tử và giá trị. Dùng cho lọc đa chiều phức tạp khi người dùng cần kết hợp nhiều tiêu chí tìm kiếm. Tìm kiếm đơn giản một trường thì dùng text input.

**Nên**

- ✅ Định nghĩa tên trường và bí danh rõ ràng, mô tả tốt để người dùng tìm nhanh bộ lọc cần.
- ✅ Cung cấp số kết quả để người dùng thấy bộ lọc ảnh hưởng tới tập dữ liệu thế nào.

**Không nên**

- ❌ Dùng PowerSearch cho tìm kiếm từ khóa đơn giản; text input chuẩn phù hợp hơn cho tra cứu một trường.
- ❌ Bọc PowerSearch bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| PowerSearch — Content Search | Power search có contentSearchFieldKey để chữ tự do tự ánh xạ vào trường tiêu đề. |
| PowerSearch — Full Featured | Power search với nhiều loại trường: enum, chọn nhiều, thực thể và lọc chữ. |
| PowerSearch — Preset Filters | Power search khởi tạo với token lọc đặt sẵn cho trạng thái và mức ưu tiên. |
| PowerSearch — Search with Table | Ghép PowerSearch với Table, dùng usePowerSearchConfig để tự sinh cấu hình và lọc dữ liệu. |
| Power Search | Thanh lọc dạng token với trường enum và chữ, điền sẵn bộ lọc mẫu. |

## Radio List

`RadioList` · Figma: `Radio / RadioList` · trang **Form Controls**

**Usage.** Nhóm lựa chọn chỉ chọn được một tại một thời điểm. Mọi lựa chọn hiển thị cùng lúc nên dễ so sánh. Dùng khi người dùng cần chọn một từ một tập nhỏ.

**Nên**

- ✅ Giữ số lựa chọn ít: thường 2 tới 7.
- ✅ Dùng nhãn rõ, ngắn gọn, phân biệt từng lựa chọn trong nháy mắt.
- ✅ Chọn sẵn một lựa chọn mặc định khi có mặc định hợp lý; đừng để nhóm trống trừ khi lựa chọn là tùy chọn.

**Không nên**

- ❌ Dùng khi cần chọn nhiều; dùng CheckboxList.
- ❌ Dùng cho danh sách dài; dùng Selector để dễ khám phá hơn.
- ❌ Dùng bố cục ngang với hơn 4 lựa chọn; nó xuống dòng lộn xộn.
- ❌ Bọc RadioList bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| RadioList — Horizontal Layout | Radio list hướng ngang cho lựa chọn gọn. |
| RadioList — Pricing Tier | Radio list có thông tin giá ở nội dung cuối để chọn gói. |
| RadioList — With Descriptions | Radio list có mô tả cho cả nhóm và từng mục. |
| RadioList — With Validation | Radio list bắt buộc có thông báo lỗi khi chưa chọn gì. |

## Selector

`Selector` · Figma: `Selector` · trang **Form Controls**

**Usage.** Dropdown chọn một giá trị từ danh sách lựa chọn. Hỗ trợ nhãn, kiểm tra, mô tả và trạng thái bắt buộc/tùy chọn. Dùng trong form và cài đặt khi có số lựa chọn vừa phải. Gõ phím để tìm giống select gốc: gõ khi trigger đang focus và đóng sẽ chọn thẳng lựa chọn khớp, nhấn lặp lại sẽ xoay vòng các lựa chọn cùng chữ cái đầu, dấu cách cũng tính là ký tự khớp ("new y" tới "New York"). Khi menu mở, gõ phím di chuyển mục tô sáng và Enter ghi nhận. Có hasSearch thì gõ trên trigger đóng sẽ mở popup và điền vào ô tìm kiếm.

**Nên**

- ✅ Có nhãn hiển thị để người dùng hiểu họ đang chọn gì.
- ✅ Dùng section và divider để sắp xếp lựa chọn khi danh sách vượt ~8 mục.
- ✅ Dùng renderOption cho dòng lựa chọn tùy biến. Không truyền SelectorOption trực tiếp làm JSX children.
- ✅ Đặt placeholder có nghĩa gợi ý lựa chọn mong đợi (ví dụ "Chọn quốc gia" chứ không phải "Chọn...").
- ✅ Chỉ dùng trong InputGroup khi selector cần phần tiền tố hoặc hậu tố ngắn trên cùng một bề mặt input.
- ✅ Dùng variant="ghost" khi selector nằm trong toolbar cùng nút Ghost. Nếu cần trạng thái kiểm tra ở đó, ưu tiên statusVariant="tooltip" để toolbar giữ chiều cao gọn.
- ✅ Dùng presentation="adaptive" khi selector cần thành bottom sheet trên màn cảm ứng nhỏ.

**Không nên**

- ❌ Dùng cho menu hành động; dùng Dropdown Menu để kích hoạt lệnh hoặc điều hướng.
- ❌ Dùng khi chỉ có hai lựa chọn; dùng SegmentedControl hoặc radio.
- ❌ Dùng Selector để điều hướng; liên kết phải là liên kết, không phải lựa chọn dropdown.
- ❌ Dùng cho lựa chọn có/không hoặc bật/tắt; dùng Switch hoặc CheckboxInput.
- ❌ Đặt quá ~20 lựa chọn mà không chia section; cân nhắc Typeahead cho danh sách lớn.
- ❌ Bọc Selector bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Selector — Bottom Sheet | Hiện danh sách chọn một trong bottom sheet cho giao diện cảm ứng nhỏ. |
| Selector — Clearable | Selector có nút xóa để đặt lại giá trị đã chọn. |
| Selector — Ghost Toolbar | Biến thể Selector không viền ghép với nút Ghost trong toolbar. |
| Selector — Option descriptions | Lựa chọn có mô tả nên dropdown vẽ dòng hai hàng. Trigger khi đóng có cỡ theo padding: bằng token size với giá trị một dòng, và cao hơn đúng một dòng với giá trị hai dòng; cả hai theo nhịp 4px. InputGroup ghim chiều cao dòng nên giá trị gập lại thành một dòng ở đó. |
| Selector — Grouped Sections | Selector với lựa chọn nhóm thành các section có nhãn. |
| Selector — Validation States | Selector ở trạng thái kiểm tra lỗi, cảnh báo và thành công. |

## Slider

`Slider` · Figma: `Slider` · trang **Form Controls**

**Usage.** Control kéo được để chọn một giá trị số hoặc một khoảng trong biên xác định. Hỗ trợ chọn một giá trị và khoảng, vạch chia, định dạng giá trị tùy biến và hướng dọc. Dùng khi người dùng cần khám phá một dải liên tục, như âm lượng, giá hay phần trăm.

**Nên**

- ✅ Luôn có nhãn, kể cả khi ẩn về hình, để slider truy cập được với trình đọc màn hình.
- ✅ Định dạng giá trị với đơn vị có nghĩa như "$50" hay "75%" thay vì số thô.

**Không nên**

- ❌ Dùng để nhập số chính xác; ghép với text input hoặc dùng NumberInput.
- ❌ Đặt bước lớn tới mức chỉ còn vài vị trí; dùng SegmentedControl hoặc radio.
- ❌ Bọc slider bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Slider — Formatted Value | Slider có định dạng tùy biến hiện nhiệt độ theo độ F. |
| Slider — Range | Slider khoảng để chọn dải giá trị như biên giá. |
| Slider | Slider đặt ở 50%. |
| Slider — With Marks | Slider có vạch chia gắn nhãn theo khoảng cố định. |
| Slider — Validation States | Slider ở trạng thái kiểm tra lỗi, cảnh báo và thành công. |

## Switch

`Switch` · Figma: `Switch` · trang **Form Controls**

**Usage.** Control bật/tắt cho trạng thái có hiệu lực ngay. Hỗ trợ nhãn, mô tả, trạng thái đang tải và kiểm tra. Dùng cho cài đặt hoặc tùy chọn áp dụng tức thì. Thay đổi cần gửi form thì dùng checkbox.

**Nên**

- ✅ Dùng cho cài đặt áp dụng ngay; bật/tắt có hiệu lực mà không cần nút lưu riêng.
- ✅ Ghép với nhãn rõ, ngắn gọn mô tả cài đặt đang được điều khiển.

**Không nên**

- ❌ Dùng cho lựa chọn cần gửi form mới có hiệu lực; dùng checkbox.
- ❌ Dùng switch cho giá trị nhiều trạng thái; nó chỉ bật/tắt.
- ❌ Bọc switch bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Switch — Disabled | Switch bị vô hiệu có nhãn và mô tả cho tính năng bị khóa. |
| Switch — Settings Panel | Panel cài đặt với các switch dàn đều trong một card. |
| Switch | Switch bật thông báo. |
| Switch — With Description | Switch có nhãn và chữ mô tả phụ. |
| Switch — With Status | Switch ở trạng thái kiểm tra lỗi, cảnh báo và thành công. |

## Text Area

`TextArea` · Figma: `TextArea` · trang **Form Controls**

**Usage.** TextArea là ô nhập chữ nhiều dòng để thu nội dung dài như bình luận, mô tả hay tin nhắn. Dùng khi nội dung nhập dự kiến trải nhiều dòng. Giá trị ngắn, một dòng thì dùng TextInput.

**Nên**

- ✅ Có nhãn hiển thị để người dùng biết cần nhập gì. Nếu phải ẩn nhãn, đặt isLabelHidden với nhãn mô tả cho trình đọc màn hình.
- ✅ Đặt maxLength kèm bộ đếm ký tự khi có giới hạn; nó giúp người dùng giữ trong giới hạn trước khi gửi.
- ✅ Dùng prop status để hiện phản hồi kiểm tra ngay tại chỗ: thành công khi nhập hợp lệ, cảnh báo cho giới hạn mềm, lỗi cho vi phạm cứng.
- ✅ Thêm mô tả hoặc placeholder để làm rõ nội dung mong đợi, như "Mô tả chi tiết vấn đề", nhưng không bao giờ dựa vào placeholder làm nhãn duy nhất.

**Không nên**

- ❌ Tránh dùng TextArea cho giá trị ngắn, một dòng như tên hay email; dùng TextInput.
- ❌ Chỉ dựa vào placeholder để truyền tải mục đích trường; placeholder biến mất khi focus và không phải nhãn truy cập được.
- ❌ Hiện thông điệp trạng thái mà không đặt loại status; viền màu và icon mới là thứ kéo sự chú ý của người dùng tới thông điệp.
- ❌ Bọc TextArea bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| TextArea — Character Count | TextArea có maxLength và bộ đếm ký tự trực tiếp. Bộ đếm chuyển đỏ khi vượt giới hạn. |
| Text Area | TextArea có chữ placeholder. |
| TextArea — States | TextArea bắt buộc, vô hiệu và đang tải đặt cạnh nhau. Cho thấy các trạng thái tương tác component hỗ trợ. |
| TextArea — Validation | Cả ba biến thể status (lỗi, cảnh báo, thành công) có thông điệp, cùng trường hợp lỗi không có thông điệp. Dùng để hiện phản hồi kiểm tra ngay khi người dùng gõ. |
| TextArea — Icon | TextArea có icon đầu gợi ý nội dung mong đợi, như bong bóng chat cho tin nhắn hoặc bút chì cho ghi chú. |

## Text Input

`TextInput` · Figma: `TextInput` · trang **Form Controls**

**Usage.** TextInput thu chữ ngắn như tên, email hoặc truy vấn tìm kiếm. Dùng cho giá trị một dòng khi nội dung nhập dự kiến ngắn. Ghép với trạng thái kiểm tra để hướng người dùng qua các trường bắt buộc hoặc có định dạng.

**Nên**

- ✅ Luôn có nhãn hiển thị để người dùng biết trường dùng để làm gì. Chỉ ẩn nhãn khi ngữ cảnh xung quanh đã rõ, như thanh tìm kiếm có icon kính lúp.
- ✅ Dùng trạng thái kiểm tra kèm thông điệp giải thích sai ở đâu: "Email phải có @" tốt hơn chỉ đổi viền sang đỏ.
- ✅ Đặt cỡ input khớp độ dài nội dung dự kiến để người dùng ước lượng cần gõ bao nhiêu: nhỏ cho mã bưu chính, vừa cho tên, lớn cho URL.
- ✅ Thêm nút xóa cho ô tìm kiếm và lọc để người dùng đặt lại nhanh mà không phải bôi đen hết chữ.

**Không nên**

- ❌ Dùng placeholder thay cho nhãn; placeholder biến mất khi focus và trình đọc màn hình không đọc tin cậy.
- ❌ Dùng TextInput cho nội dung nhiều dòng như bình luận hay mô tả; dùng TextArea.
- ❌ Đánh dấu mọi trường là bắt buộc; chỉ gắn cờ trường thật sự bắt buộc để người dùng không bị ngợp bởi lỗi kiểm tra.
- ❌ Bọc TextInput bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| TextInput — Icon | Input có icon đầu gợi ý nội dung mong đợi. Dùng khi icon giúp nhận ra trường nhanh hơn, như ổ khóa cho mật khẩu hay phong bì cho email. |
| TextInput — Search | Ô tìm kiếm có nhãn ẩn, icon đầu và nút xóa. Dùng cho thanh tìm kiếm trên toolbar và header, nơi icon đã đủ ngữ cảnh. |
| TextInput — Sizes | Input nhỏ, vừa, lớn đặt cạnh nhau. Nhỏ cho giao diện dày như bộ lọc bảng, vừa cho đa số form, lớn cho trang một trường nổi bật. |
| TextInput — States | Trạng thái kiểm tra lỗi, cảnh báo và thành công có thông điệp. Dùng để cho người dùng thấy sai ở đâu và cách sửa. |
| TextInput — Status variant | Prop statusVariant điều khiển thông điệp trạng thái gắn liền với input có viền (mặc định, chồng ngay bên dưới) hay tách rời (nằm bên dưới như phần tử riêng có khoảng cách). |
| TextInput — Types | Loại text, password, email cùng các tính năng cấp trường: tooltip, bắt buộc, tùy chọn, mô tả, vô hiệu và đang tải. |

## Time Input

`TimeInput` · Figma: `TimeInput` · trang **Form Controls**

**Usage.** TimeInput mặc định dùng bộ chọn giờ của trình duyệt/hệ điều hành trên con trỏ thô và trường gõ của Astryx trên con trỏ mịn. Nó chuyển giá trị về định dạng chuẩn và hỗ trợ chỉnh bằng phím mũi tên trên bề mặt gõ. Dùng trong form, luồng lập lịch, hoặc giao diện cần chọn một giờ cụ thể.

**Nên**

- ✅ Chọn định dạng giờ (12h hoặc 24h) khớp locale người dùng: 12 giờ có AM/PM cho giao diện hướng Mỹ, 24 giờ cho ngữ cảnh quốc tế hoặc kỹ thuật.
- ✅ Đặt ràng buộc min và max khi ngữ cảnh có khoảng hợp lệ, như giờ làm việc hay khung sự kiện, để người dùng không gửi được giờ ngoài biên.
- ✅ Cung cấp mô tả hoặc placeholder gợi ý định dạng hoặc mục đích mong đợi, như "Giờ làm việc: 9:00 – 17:00".
- ✅ Dùng prop status để hiện lỗi kiểm tra ngay tại chỗ: thông điệp như "Giờ phải nằm trong giờ làm việc" để người dùng biết chính xác cần sửa gì.
- ✅ Bật hasClear khi trường là tùy chọn để người dùng xóa được giờ đã chọn.
- ✅ Đặt TimeInput trong InputGroup khi giờ cần phần tiền tố hoặc hậu tố một dòng, như nhãn bắt đầu/kết thúc hoặc ký hiệu múi giờ.

**Không nên**

- ❌ Dùng TimeInput cho chọn ngày và giờ kết hợp; ghép với một DateInput riêng.
- ❌ Ẩn nhãn; kể cả khi chật chỗ, giữ nhãn hiển thị hoặc có mô tả để mục đích rõ ràng.
- ❌ Bọc TimeInput bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| TimeInput — Constrained | Ô giờ có ràng buộc min/max giới hạn lựa chọn trong khung cụ thể. Dùng để chặn chọn ngoài biên cho lịch hẹn, đặt chỗ hoặc xếp ca. |
| TimeInput — Formats | Định dạng 12 giờ, 24 giờ và có giây đặt cạnh nhau. 12h cho giao diện hướng Mỹ, 24h cho ngữ cảnh quốc tế hoặc kỹ thuật, có giây cho thời gian chính xác. |
| TimeInput — Increment | Ô giờ có bước tăng tùy biến. Phím mũi tên nhảy theo khoảng đã định (ví dụ 15 phút) để xếp lịch theo khung nhanh. |
| Time Input | Ô giờ mặc định dùng bộ chọn của trình duyệt/hệ điều hành trên cảm ứng và nhập gõ của Astryx trên con trỏ mịn. |
| TimeInput — States | Trạng thái mặc định, vô hiệu, lỗi, cảnh báo và thành công. Dùng thông điệp trạng thái để phản hồi rõ về lựa chọn giờ. |

## Tokenizer

`Tokenizer` · Figma: `Tokenizer` · trang **Form Controls**

**Usage.** Tokenizer là input chọn nhiều cho phép tìm, chọn và quản lý nhiều mục hiển thị dưới dạng chip gỡ được. Dùng khi người dùng cần dựng một tập lựa chọn từ nguồn dữ liệu tìm kiếm được, như thêm thành viên nhóm, gắn thẻ hoặc chọn bộ lọc.

**Nên**

- ✅ Viết placeholder cho biết người dùng có thể tìm gì, như "Tìm người..." hay "Thêm thẻ...", để ô nhập không phải một ô trống bí ẩn.
- ✅ Đặt maxEntries khi số lựa chọn cần giới hạn, như giới hạn một lượt review tối đa 5 người duyệt.
- ✅ Dùng hasCreate cho gắn thẻ tự do khi người dùng cần nhập giá trị chưa có trong nguồn tìm kiếm.
- ✅ Hiện trạng thái kiểm tra bằng prop status để người dùng biết ngay khi lựa chọn bị thiếu hoặc không hợp lệ.

**Không nên**

- ❌ Dùng Tokenizer để chọn một mục; dùng Typeahead. Tokenizer dành cho dựng tập từ hai mục trở lên.
- ❌ Tránh áp màu tùy biến cho từng token trong Tokenizer; dùng kiểu token mặc định để nhất quán cả tập.
- ❌ Ẩn nhãn; mọi Tokenizer cần nhãn hiển thị để người dùng hiểu họ đang chọn gì. Chỉ dùng isLabelHidden khi ngữ cảnh xung quanh đã rõ mục đích.
- ❌ Bọc Tokenizer bị vô hiệu trong Tooltip để giải thích lý do; control bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Tokenizer — Clear | Tokenizer có nút xóa tất cả để gỡ hàng loạt mọi token đã chọn. |
| Tokenizer — Creatable | Tokenizer chữ tự do để tạo thẻ tùy biến và mẫu kết hợp tạo-hoặc-tìm. Dùng khi người dùng cần nhập giá trị có thể chưa có trong danh sách định sẵn. |
| Tokenizer — End Content | Tokenizer có nút hành động ở slot cuối. Dùng cho hành động trong dòng như áp dụng lựa chọn cạnh ô nhập. |
| Tokenizer — Icon | Tokenizer có icon tìm kiếm ở đầu để củng cố hành vi tìm kiếm. |
| Tokenizer — Max Entries | Tokenizer có giới hạn số lựa chọn. Ô nhập tự ẩn khi đạt giới hạn, chặn thêm mới. |
| Tokenizer — Overflow | Tokenizer cắt phần tràn khi không focus. Chế độ inline đẩy nội dung xuống khi mở rộng; chế độ layer phủ lên mà không xê dịch bố cục. |
| Tokenizer | Tokenizer có thẻ đặt sẵn và nguồn tìm kiếm. |
| Tokenizer — States | Tokenizer ở trạng thái vô hiệu, lỗi, cảnh báo và thành công. Dùng để truyền tải phản hồi kiểm tra hoặc khóa lựa chọn không cho sửa. |

## Typeahead

`Typeahead` · Figma: `Typeahead` · trang **Form Controls**

**Usage.** Ô nhập tìm kiếm được để chọn một mục từ tập dữ liệu lớn hoặc động. Kết quả hiện khi người dùng gõ, hỗ trợ nguồn dữ liệu bất đồng bộ, tìm kiếm có debounce và hiển thị mục tùy biến. Dùng khi danh sách lựa chọn quá lớn cho dropdown Selector.

**Nên**

- ✅ Cung cấp placeholder mô tả gợi ý người dùng có thể tìm gì.
- ✅ Hiện gợi ý khi focus nếu người dùng có lợi khi thấy lựa chọn phổ biến hoặc gần đây trước khi gõ.
- ✅ Thêm độ trễ tìm kiếm cho nguồn dữ liệu từ xa để tránh quá nhiều request mạng.
- ✅ Dùng trong InputGroup khi typeahead cần phần tiền tố hoặc hậu tố một dòng.

**Không nên**

- ❌ Dùng cho danh sách lựa chọn ngắn, tĩnh; dùng Selector để dễ khám phá hơn.
- ❌ Dùng cho chọn nhiều; dùng Tokenizer.
- ❌ Đặt nhiều Typeahead sát nhau mà không có nhãn rõ phân biệt chúng.
- ❌ Bọc Typeahead bị vô hiệu trong Tooltip để giải thích lý do; trigger bị vô hiệu nuốt sự kiện hover mà Tooltip cần. Dùng prop disabledMessage.

**Examples**

| Example | Mô tả |
|---|---|
| Typeahead — Limited Results | Typeahead có dropdown giới hạn tối đa ba kết quả. |
| Typeahead — Search Field | Ô tìm kiếm có icon và gợi ý khi focus. |
| Typeahead — With Helper Text | Typeahead có mô tả dưới nhãn. |
| Typeahead — With Validation | Typeahead có thông báo lỗi kiểm tra. |

## Typeahead Item

`TypeaheadItem` · Figma: không có set riêng — là dòng kết quả trong `Typeahead` · trang **Form Controls**

**Usage.** Bộ hiển thị mục dropdown mặc định cho kết quả typeahead. Hiện nhãn kèm icon, mô tả và avatar (tùy chọn). Được export để dùng trong renderItem tùy biến.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| TypeaheadItem — Basic | Typeahead có kết quả hiển thị bằng TypeaheadItem, thêm mô tả phụ dưới mỗi nhãn. Dùng trong renderItem để giữ kết quả tùy biến nhất quán về hình. |
| Typeahead Item | Typeahead hiển thị mục tùy biến bằng TypeaheadItem cho avatar và mô tả. |

---

# Layout

## App Shell

`AppShell` · Figma: `AppShell` · trang **Layout**

**Usage.** AppShell là khung trang của một ứng dụng. Nó có slot cho điều hướng trên, điều hướng bên, banner và nội dung chính. Dùng làm lớp bọc gốc cho mọi trang. Nó tự xử lý điều hướng di động responsive và liên kết bỏ qua tới nội dung. Cấu hình thu gọn điều hướng bên bằng prop collapsible trên SideNav.

**Nên**

- ✅ Chọn đúng chiều cao: "fill" cho dashboard có cuộn bên trong, "auto" cho trang dài theo nội dung.
- ✅ Đặt `contentPadding` theo loại nội dung: 4 cho form và cài đặt, 0 cho bảng và dashboard.
- ✅ Đặt tên truy cập cho mọi slot điều hướng. AppShell hiển thị TopNav và SideNav thành các landmark điều hướng riêng, trình đọc màn hình liệt kê chúng theo tên, nên truyền `label` cho từng cái.
- ✅ Bắt đầu heading của trang bên trong `children`. AppShell sở hữu liên kết bỏ qua, landmark banner và landmark main, nhưng không vẽ heading nào, nên heading đầu tiên trong vùng nội dung là h1 của trang.

**Không nên**

- ❌ Lồng AppShell trong AppShell; nó là khung bố cục ngoài cùng.
- ❌ Dùng cho bố cục trang con; dùng Layout cho vùng nội dung bên trong AppShell.
- ❌ Tự thêm liên kết bỏ qua hoặc phần tử <main>. AppShell đã vẽ cả hai, và landmark main thứ hai làm cái đầu mơ hồ.

**Examples**

| Example | Mô tả |
|---|---|
| AppShell — Content Only | Khung tối giản không có điều hướng, hữu ích cho trang tràn viền, màn đăng nhập hoặc view nhúng. |
| App Shell | App shell cơ bản có padding nội dung. |
| AppShell — Side Nav Only | App shell với header của SideNav mang nhận diện ứng dụng, không cần TopNav. |
| AppShell — Top Nav Only | Bố cục đơn giản có TopNav, không điều hướng bên, hợp với landing page. |
| AppShell — Top Nav with Side Nav | Bố cục phổ biến nhất: TopNav cho nhận diện ứng dụng và SideNav cho điều hướng cấp trang. |
| AppShell — With Banner | Bố cục đầy đủ với TopNav, SideNav và banner thông tin đóng được nằm giữa điều hướng và nội dung. |

## Aspect Ratio

`AspectRatio` · Figma: `AspectRatio` · trang **Layout**

**Usage.** Giữ tỉ lệ rộng/cao cố định cho phần tử con khi vùng chứa đổi cỡ. Dùng cho vùng chứa media như video, ảnh, thumbnail, hoặc nội dung cần tỉ lệ nhất quán. Nó lấy bề rộng từ vùng chứa và suy ra chiều cao theo tỉ lệ, nên cần một phần tử tổ tiên có bề rộng xác định.

**Nên**

- ✅ Viết tỉ lệ dạng phân số cho dễ đọc: `ratio={16 / 9}` thay vì `ratio={1.78}`. Đây là số, nên dạng chuỗi `ratio="16/9"` là lỗi kiểu.
- ✅ Dùng cho media cần tỉ lệ nhất quán qua các cỡ màn.
- ✅ Dùng `fit="cover"` cho ảnh và video để component định cỡ phần tử con; phần tử con không lặp lại style `width`/`height`/`objectFit`.
- ✅ Truyền một phần tử con. Khi đặt `fit`, mọi con trực tiếp bị kéo giãn lấp đầy hộp, nên đặt lớp phủ hoặc chú thích trong một phần tử bọc duy nhất thay vì truyền như con thứ hai.
- ✅ Mô tả media con bằng `alt`, hoặc `alt=""` khi ảnh chỉ trang trí. AspectRatio không thêm vai trò hay tên truy cập riêng, nên phần tử con mang toàn bộ mô tả truy cập.
- ✅ Với tỉ lệ phụ thuộc breakpoint, ghi đè tỉ lệ theo responsive: truyền quy tắc `aspectRatio` qua `xstyle` (StyleX), hoặc ghi đè `aspect-ratio` từ CSS không layer của bạn trong quy tắc `@media`/`@container`; style component nằm trong cascade layer `astryx-base` nên CSS không layer của nơi dùng sẽ thắng. Cho quy tắc `xstyle` một nhánh `default` cạnh nhánh điều kiện (`{default: 3, '@container ...': '3 / 2'}`); chỉ có nhánh điều kiện thì ngoài query tỉ lệ không được đặt và hộp sụp.

**Không nên**

- ❌ Dùng làm vùng chứa bố cục chung; dùng component bố cục tiêu chuẩn.
- ❌ Lồng AspectRatio; một cấp là đủ.
- ❌ Giới hạn chiều cao riêng lẻ. Bề rộng lấy từ vùng chứa, nên chỉ đặt `height` hoặc `maxHeight` sẽ ép hộp lệch tỉ lệ; ghép với `width: "auto"` để định cỡ theo chiều cao.
- ❌ Đặt trong phần tử cha co theo nội dung như `inline-flex`, `width: fit-content` hoặc hộp float. Ở đó nó không đóng góp bề rộng nội tại và sụp về 0.

**Examples**

| Example | Mô tả |
|---|---|
| AspectRatio — Circle Image | Vùng chứa tròn qua shape="ellipse" với ratio={1}, hợp cho avatar và ảnh hồ sơ. |
| AspectRatio — Image Gallery | Lưới ảnh với tỉ lệ 4:3 nhất quán. |
| Aspect Ratio | Ba vùng chứa tỉ lệ cùng chiều cao (1:1, 4:3, 16:9), mỗi cái có ảnh và nhãn tỉ lệ bên dưới. |
| AspectRatio — Square Image | Tỉ lệ vuông 1:1, hợp cho avatar và ảnh kiểu Instagram. |
| AspectRatio — 16:9 Widescreen Image | Tỉ lệ màn rộng 16:9 bọc một ảnh. |
| AspectRatio — Loading Skeleton | Vùng chứa tỉ lệ có skeleton giữ chỗ đang tải. |

## Divider

`Divider` · Figma: `Divider` · trang **Layout**

**Usage.** Đường phân cách trực quan chia nội dung thành các phần riêng. Dùng để tạo ranh giới rõ giữa các nhóm nội dung liên quan, hoặc đánh dấu các vùng tương tác trong bố cục.

**Nên**

- ✅ Dùng divider nhạt giữa các phần nội dung liên quan và divider đậm cho ranh giới tương phản cao.
- ✅ Thêm nhãn cho divider khi các phần cần tiêu đề danh mục hiển thị.

**Không nên**

- ❌ Lạm dụng divider; ưu tiên khoảng cách và bố cục để tách nội dung khi có thể.

**Examples**

| Example | Mô tả |
|---|---|
| Divider — Full Bleed | Divider vượt qua padding vùng chứa để trải hết bề rộng. Dùng trong card hoặc panel khi muốn tách mép-tới-mép gọn gàng, như giữa tóm tắt đơn hàng và tổng tiền. |
| Divider — Variants | Divider ngang ở biến thể nhạt và đậm, cùng một divider có nhãn. Tham chiếu nhanh cho kiểu phân cách. |
| Divider — Variants | Divider nhạt, có nhãn và đậm trong một card. Nhạt giữa các phần liên quan, có nhãn cho phương án thay thế như "hoặc", đậm cho ranh giới tương phản cao. |
| Divider — Vertical | Divider dọc tách các chỉ số đặt cạnh nhau. Dùng giữa card số liệu, nhóm toolbar hoặc bố cục ngang cần ranh giới giữa các phần. |

## Form Layout

`FormLayout` · Figma: `Layout / FormLayout` · trang **Layout**

**Usage.** Vùng chứa bố cục sắp xếp các trường form với khoảng cách và hướng nhất quán. FormLayout lo vị trí trường, không lo state hay gửi form; bọc nó trong <form> cho việc đó. Hỗ trợ hướng vertical (mặc định), horizontal và horizontal-labels, và có thể lồng để kết hợp.

**Nên**

- ✅ Xếp trường theo chiều dọc cho đa số form. Dễ lướt nhất từ trên xuống.
- ✅ Lồng FormLayout ngang trong FormLayout dọc khi các trường tự nhiên đi thành cặp, như Tên + Họ hay Thành phố + Tỉnh + Mã bưu chính.
- ✅ Dùng horizontal-labels cho trang cài đặt, nơi nhãn nằm cạnh input.

**Không nên**

- ❌ Dùng FormLayout cho state hay gửi form. Nó chỉ là bố cục. Bọc nó trong <form> cho việc đó.
- ❌ Đặt các trường không liên quan cạnh nhau trong bố cục ngang. Để dành cho trường thuộc về nhau.
- ❌ Lồng horizontal-labels trong FormLayout khác. Nó dùng CSS Grid và phải là vùng chứa ngoài cùng.

**Examples**

| Example | Mô tả |
|---|---|
| FormLayout — Horizontal | Hai trường cạnh nhau cho input tự nhiên đi cặp như tên và họ. |
| FormLayout — Settings Form | Form cài đặt với nhãn đặt cạnh input. |
| FormLayout — Mixed Controls | Form với nhiều loại control: text input, selector và checkbox. |
| FormLayout — Nested Address Form | Form địa chỉ kết hợp bố cục dọc và ngang cho các trường nhóm. |
| Form Layout | Bố cục form dọc với các trường text input. |

## Grid

`Grid` · Figma: không có set — dựng bằng auto layout (wrap) / layout grid · trang **Layout**

**Usage.** Vùng chứa bố cục CSS grid để xếp phần tử con theo hàng và cột. Dùng Grid cho thư viện card, dashboard và bố cục nhiều cột. Hỗ trợ số cột cố định và cột responsive tự dàn lại theo bề rộng sẵn có.

**Nên**

- ✅ Dùng cột responsive cho bố cục cần thích ứng cỡ màn: `columns={{minWidth: 280}}`.
- ✅ Giới hạn số cột bằng `max` để hàng không quá rộng trên màn lớn.
- ✅ Dùng `repeat: 'fill'` (mặc định) cho bề rộng mục nhất quán. Dùng `'fit'` khi mục cần giãn lấp khoảng trống còn lại.
- ✅ Template track dùng gián tiếp qua biến CSS (không phải inline style thô), nên ghi đè `gridTemplateColumns` bằng `xstyle` (kể cả trong `@media`) có hiệu lực.

**Không nên**

- ❌ Tự viết CSS grid; Grid lo khoảng cách và hành vi responsive.
- ❌ Dùng `HStack` có xuống dòng để làm lưới; dùng Grid.

**Examples**

| Example | Mô tả |
|---|---|
| Grid — Dashboard Layout | Bố cục dashboard với widget nhiều cỡ và một hàng tóm tắt tràn bề rộng. |
| Grid — Card Gallery | Thư viện card với cột responsive giữ bề rộng nhất quán. |
| Grid — Responsive Auto-Fit | Lưới responsive, card giãn lấp khoảng trống còn lại. |
| Grid — Column Spanning | Lưới có mục nổi bật trải qua nhiều cột và hàng. |

## Layout

`Layout` · Figma: không có set — dựng bằng auto layout · trang **Layout**

**Usage.** Layout là primitive năm slot tổng quát để sắp xếp các vùng header, start, content, end và footer trong một trang hoặc vùng chứa có biên. AppShell sở hữu khung trang và hành vi điều hướng toàn ứng dụng; dùng HStack hoặc VStack cho xếp chồng theo một hướng đơn giản.

**Nên**

- ✅ Dùng Layout khi nội dung cần các vùng có tên header, start, content, end hoặc footer.
- ✅ Dùng HStack và VStack cho xếp chồng một hướng đơn giản trong vùng nội dung.

**Không nên**

- ❌ Dùng Layout cho bố cục xếp chồng đơn giản; dùng HStack hoặc VStack.
- ❌ Dùng Layout làm khung trang hoặc cho điều hướng toàn ứng dụng; đó là trách nhiệm của AppShell.

**Examples**

| Example | Mô tả |
|---|---|
| Layout — Basic Card | Bố cục card có header, vùng nội dung cuộn được và footer có nút hành động. |
| Layout — Content Only | Bố cục tối giản chỉ có vùng nội dung trong card, không header hay footer. |
| Layout — Content Width | Bố cục dùng contentWidth để giới hạn và căn giữa nội dung trong khi divider vẫn tràn viền. |
| Layout — Dual Panel | Bố cục kiểu trình duyệt tệp: panel start cho thư mục, nội dung chính cho tệp, panel end cho chi tiết. |
| Layout — Full Bleed Content | Bố cục có nội dung trải mép-tới-mép, padding 0, hợp cho bảng hoặc ảnh. |
| Layout — Sidebar Navigation | Bố cục trang cài đặt có panel sidebar điều hướng, vùng nội dung, header và footer. |

## Resize Handle

`ResizeHandle` · Figma: `ResizeHandle` · trang **Layout**

**Usage.** Thanh phân cách kéo được giữa các panel. Thiết kế tay nắm dạng viên thuốc: ẩn khi nghỉ, hiện khi hover (độ mờ 0.6), đậm hoàn toàn khi kéo (1.0). Truy cập được bằng bàn phím.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| Resizable — Collapsible with snap points | Sidebar thu gọn được có điểm bắt, điều khiển bằng useResizable. Kéo sẽ bắt vào bề rộng đặt sẵn, kéo quá mức tối thiểu thì panel thu gọn, và phương thức expand mở lại bằng code. |

## Scrollable Area

`ScrollableArea` · Figma: không có set — frame có clip content + cuộn · trang **Layout**

**Usage.** Cung cấp một viewport cuộn gốc và một hộp nội dung thật được theo dõi. Viewport chỉ vào thứ tự tab khi một trục logic được yêu cầu thực sự cuộn được, và việc chặn cuộn (containment) chỉ áp lên trục thực sự cuộn.

**Nên**

- ✅ Đặt cho mỗi vùng một nhãn ngắn gọn cho biết nội dung mà người dùng bàn phím sẽ cuộn.
- ✅ Chọn `inline`, `block` hoặc `both` theo ý đồ nội dung; component tự ánh xạ trục logic theo chế độ viết và hướng chữ.
- ✅ Giữ `overscroll="allow"` mặc định cho vùng lồng nhau trừ khi tương tác cố ý cần chặn.
- ✅ Dùng `useScrollableArea` khi component đã sở hữu cả viewport và hộp nội dung phù hợp, hoặc khi phần tử con phải là mục flex/grid trực tiếp hoặc giữ cơ sở block-size phần trăm xác định.
- ✅ ScrollableArea sở hữu một hộp nội dung block bình thường với cỡ tối thiểu 100%. Chế độ inline và cả hai trục dùng định cỡ inline max-content, nên bố cục inline nội tại cố ý rộng hơn viewport.
- ✅ Dùng prop padding logic trên hộp nội dung để component tràn viền lồng bên trong nhận cùng hình học thụt lề.
- ✅ Chỉ đặt `isFullBleed` khi chính viewport cần chạm mép vùng chứa tổ tiên; mặc định tắt.
- ✅ Chỉ đặt `stickyContainment="always"` khi một viewport vừa khít cần cố ý giữ vai trò biên Sticky.

**Không nên**

- ❌ Ẩn thanh cuộn gốc mà không có một chỉ báo tràn khác nhìn thấy và thao tác được.
- ❌ Thêm lớp bọc overflow khác quanh ScrollableArea; một viewport gốc nên sở hữu việc cuộn.

**Examples**

| Example | Mô tả |
|---|---|
| Scrollable Area — Inline Rail | axis="inline" cuộn ngang cùng các card; isFullBleed cho dải chạy tới mép panel trong khi padding nội dung giữ card đầu thẳng hàng với heading. |
| Scrollable Area — Overscroll | Cùng một section, hai chính sách mép: overscroll="allow" mặc định chuyển thao tác chạm tới cuối sang panel phía sau, còn overscroll="contain" dừng nó ở mép section. |
| Scrollable Area | Panel tệp chiều cao cố định cuộn theo trục block; heading nằm trong viewport nên cuộn đi cùng nội dung. |
| Scrollable Area — Sticky Section Labels | Viewport cuộn là khối chứa cho position: sticky, nên nhãn section ghim vào mép trên danh sách thay vì của trang. |
| Scrollable Area — Sticky Passthrough | Section có nội dung vừa khít thì cắt thay vì cuộn, nên nhãn sticky của nó đi ra ngoài và ghim vào mép panel. Section kế tiếp đặt stickyContainment="always" và giữ nhãn trong hộp của chính nó. |
| Scrollable Area — Two-Axis Board | axis="both" cho hộp nội dung định cỡ inline max-content, nên một bảng rộng và cao hơn panel cuộn được cả hai trục từ một viewport. |

## Section

`Section` · Figma: `Layout / Section` · trang **Layout**

**Usage.** Section là cách đúng để tạo các vùng trang và nhóm nội dung liên quan trên trang. Dùng cho nhóm cài đặt, phần form, vùng sidebar, hoặc bất cứ khi nào cần tách thị giác giữa các phần của trang. Nếu định dùng Card cho một phần của trang, hãy dùng Section.

**Nên**

- ✅ Dùng Section cho nhóm cấp trang: panel cài đặt, nhóm form, vùng sidebar. Đây là các phần của trang, không phải mục rời rạc.
- ✅ Bắt đầu với biến thể mặc định. Chỉ dùng muted để hướng sự chú ý tới một vùng cụ thể.
- ✅ Thêm divider giữa các section cùng nền cần tách.
- ✅ Kết hợp với heading + Stack cho mẫu section trang điển hình.

**Không nên**

- ❌ Dùng Card khi ý bạn là Section. Card cho mục rời rạc (một thông báo, một hồ sơ). Section cho vùng trang.

**Examples**

| Example | Mô tả |
|---|---|
| Section — Variants | Cả ba biến thể nền xếp chồng: section (bề mặt mặc định), muted và transparent. Tham chiếu nhanh để chọn đúng biến thể. |
| Section — Default with Wash | Một section mặc định xếp trên một section muted tràn bề rộng. Cho thấy muted hướng sự chú ý tới một vùng cụ thể như lời mời nâng cấp hay banner. |
| Section — With Dividers | Các section kề nhau tách bằng divider dưới, như trang cài đặt. Dùng divider khi xếp các section cùng biến thể cần tách thị giác mà không đổi nền. |

## Stack

`Stack` · Figma: không có set — dựng bằng auto layout · trang **Layout**

**Usage.** Stack xếp các mục theo hàng hoặc cột với khoảng cách nhất quán. Dùng prop gap để điều khiển khoảng cách giữa các mục.

**Nên**

- ✅ Dùng prop gap cho khoảng cách giữa các mục; không tự thêm margin.
- ✅ Dùng StackItem với size="fill" để một mục giãn lấp khoảng trống còn lại.

**Không nên**

- ❌ Lồng stack trong stack; thử wrap="wrap" trước để mục chảy xuống dòng tiếp.

**Examples**

| Example | Mô tả |
|---|---|
| Stack — Alignment | Nút đặt ở đầu, giữa và cuối một hàng. |
| Stack — Directions | Badge xếp ngang và dọc trong hai card cạnh nhau. |
| Stack — Fill Item | Avatar, chữ và nút trong một hàng; chữ giãn lấp khoảng trống sẵn có. |

---

# Navigation

## Breadcrumbs

`Breadcrumbs` · Figma: `Breadcrumbs`, `Breadcrumbs / BreadcrumbItem` · trang **Navigation**

**Usage.** Breadcrumbs hiển thị chuỗi liên kết từ gốc tới trang hiện tại. Dùng ở đầu trang chi tiết, panel cài đặt, hoặc nơi người dùng cần thấy mình đang ở đâu và quay ngược lên.

**Nên**

- ✅ Đặt breadcrumbs phía trên heading trang để người dùng thấy vị trí trước khi đọc nội dung.
- ✅ Giữ nhãn ngắn và khớp tiêu đề trang mà chúng dẫn tới: "Cài đặt" chứ không phải "Trang cài đặt ứng dụng".
- ✅ Dùng biến thể supporting trong giao diện dày như trang quản trị hoặc sidebar, nơi breadcrumb cần kín đáo.
- ✅ Để mục cuối là chữ thường, không phải liên kết; nó là trang hiện tại. Component tự làm điều này khi đặt isCurrent.
- ✅ Component theo mẫu Breadcrumb của WAI-ARIA APG: landmark nav có nhãn bọc một danh sách có thứ tự, aria-current="page" trên mục hiện tại. Mục có menu còn theo mẫu Menu Button của APG, mở bằng Enter, Space hoặc ArrowDown và đóng bằng Escape.
- ✅ Đặt nhãn riêng cho từng chuỗi khi một trang có nhiều hơn một, để các landmark nav phân biệt được trong danh sách landmark của trình đọc màn hình.
- ✅ Dấu phân cách gạch chéo có sẵn tự lật trong RTL. Với dấu phân cách tùy biến, để nguyên các dấu ngoặc góc tự lật theo Unicode như ›; mũi tên và dấu phân cách Icon thì lật một lần bằng rtlStyles.mirror.

**Không nên**

- ❌ Dùng breadcrumbs làm điều hướng chính. Chúng bổ sung cho sidebar hoặc top nav, không thay thế.
- ❌ Hiện breadcrumbs ở trang cấp cao nhất không có cha; chúng chỉ thêm rối mà không giúp gì.
- ❌ Để chuỗi dài quá 5 cấp. Cần nhiều hơn thì cân nhắc đơn giản hóa phân cấp trang.
- ❌ Lật dấu phân cách mà thuật toán bidi đã lật. Ký tự ngoặc góc như › là Bidi_Mirrored nên tự lật trong RTL, rtlStyles.mirror sẽ lật ngược lại. Ký tự mũi tên như → và mọi dấu phân cách Icon thì không, nên cần rtlStyles.mirror qua xstyle.

**Examples**

| Example | Mô tả |
|---|---|
| Breadcrumbs — Separators | Thay "/" mặc định bằng ký tự khác như chevron, mũi tên hay chấm. Dùng khi phong cách trang cần dấu phân cách khác. |
| Breadcrumbs — Deep Path | Chuỗi breadcrumb 5 cấp cho nội dung lồng sâu. Dùng trong thương mại điện tử, trình duyệt tệp, hoặc giao diện có nhiều cấp phân cấp. |
| Breadcrumbs — Menu item | Cho một mục giữa chuỗi prop `menu` để biến nó thành trigger menu, chuyển giữa các đích anh em. Nó dùng lại API mục của DropdownMenu nên mảng lựa chọn có sẵn (hoặc children ghép) đưa vào nguyên văn. |
| Breadcrumbs | Chuỗi breadcrumb thể hiện phân cấp trang với tổ tiên có liên kết và trang hiện tại. |
| Breadcrumbs — Variants | So sánh biến thể default và supporting cạnh nhau. Dùng supporting trong giao diện dày như trang quản trị, nơi breadcrumb cần kín đáo. |
| Breadcrumbs — Icons | Thêm icon trước nhãn breadcrumb để nhận ra nhanh. Dùng icon nhà cho mục gốc và icon ngữ cảnh cho các phần chính. |

## Outline

`Outline` · Figma: `Outline` (+ `.OutlineItem`) · trang **Navigation**

**Usage.** Sidebar mục lục cho trang tài liệu, trung tâm trợ giúp, wiki và trang cài đặt dài. Dùng để điều hướng trong một trang, không dùng cho route ứng dụng. Có thanh chỉ báo trượt tới heading đang hoạt động. Danh sách là một điểm dừng tab: phím mũi tên di chuyển giữa các heading, Home/End nhảy về hai đầu, Enter/Space kích hoạt.

**Nên**

- ✅ Truyền danh sách heading phẳng có thứ tự và để level điều khiển thụt lề.
- ✅ Dùng activeId khi logic cuộn tùy biến quyết định phần đang hoạt động.
- ✅ Dùng density="compact" trong sidebar dày khi chiều dọc chật.
- ✅ Dùng useOutlineFromMarkdown hoặc useOutlineFromDOM khi heading sinh ra từ nội dung.
- ✅ Truyền scrollContainerRef khi nội dung cuộn trong khung chia, modal hoặc panel thay vì viewport.
- ✅ Đặt offset bằng chiều cao header cố định phủ lên nội dung, để heading dừng bên dưới header chứ không bị che.

**Không nên**

- ❌ Dùng Outline cho điều hướng ứng dụng; dùng SideNav hoặc TopNav cho route.
- ❌ Dùng Outline cho phân cấp mở rộng được; dùng TreeList khi node cần mở và thu gọn.
- ❌ Hiểu onNavigateEnd là "đã tới nơi"; nó cũng chạy khi người dùng ngắt việc cuộn.

**Examples**

| Example | Mô tả |
|---|---|
| Outline — Controlled | Tự điều khiển phần đang hoạt động bằng activeId và onActiveIdChange. Truyền activeId sẽ tắt scroll-spy có sẵn để logic của bạn sở hữu phần tô sáng. |
| Outline — Deep Nesting | Heading cấp 1 tới 4 ánh xạ vào thụt lề sâu dần, nên tài liệu dài có mục con vẫn dễ lướt. |
| Outline — Density | Hai biến thể mật độ điều khiển padding mục. Compact cho sidebar dày, default cho bố cục tài liệu tiêu chuẩn. Chỉ báo trượt tự khớp chiều cao từng mục. |
| Outline | Dàn ý tài liệu với phần đang hoạt động được tô bằng thanh chỉ báo trượt. |

## Pagination

`Pagination` · Figma: `Pagination` · trang **Navigation**

**Usage.** Pagination cho người dùng đi qua các trang nội dung. Đặt dưới bảng, danh sách hoặc lưới card để người dùng đi tới lui qua kết quả. Chọn biến thể theo ngữ cảnh: số trang cho bảng dữ liệu, số đếm cho danh sách lớn, compact cho chỗ hẹp, dots cho carousel.

**Nên**

- ✅ Đặt pagination dưới nội dung nó điều khiển để người dùng thấy kết quả trước khi chuyển trang.
- ✅ Dùng biến thể pages cho bảng dữ liệu khi người dùng cần nhảy tới một trang cụ thể.
- ✅ Dùng biến thể count kèm bộ chọn cỡ trang khi người dùng cần điều khiển số mục thấy cùng lúc.
- ✅ Dùng biến thể dots cho carousel và hướng dẫn từng bước khi tổng nhỏ và vị trí quan trọng hơn con số.
- ✅ Truyền totalItems khi biết tổng để người dùng thấy còn bao nhiêu nội dung.

**Không nên**

- ❌ Hiện pagination khi mọi mục vừa một trang; không có gì để phân trang.
- ❌ Dùng biến thể dots cho hơn khoảng 10 trang; chấm trở nên quá nhỏ để hữu ích.
- ❌ Đặt pagination phía trên nội dung; người dùng mong nó ở dưới.

**Examples**

| Example | Mô tả |
|---|---|
| Pagination — Dots Carousel | Carousel đánh giá dùng phân trang dạng chấm để đi qua các card lời chứng thực. Dùng dots cho carousel, thư viện ảnh và nội dung phân trang có tổng nhỏ, nơi vị trí nhìn thấy quan trọng hơn số trang. |
| Pagination — Page Size Selector | Bảng giao dịch có pagination và dropdown cỡ trang ở dưới. Cho thấy pagination làm chân trang dưới nội dung thật, số dòng mỗi trang chỉnh được. |
| Pagination — Variants | Cả bốn biến thể hiển thị xếp chồng: dots, compact, count và pages. Tham chiếu nhanh để chọn đúng biến thể. |
| Pagination — With Table | Pagination dưới bảng dữ liệu, cắt trang phía client. Dùng biến thể count cỡ nhỏ cho màn dữ liệu dày khi người dùng cần thấy khoảng mục. |

## Side Nav

`SideNav` · Figma: `Navigation / SideNav` (+ `Navigation / .SideNavItem`, `Navigation / .SideNavSection`, `Navigation / .SideNavHeading`, `Navigation / .SideNavCollapseButton`) · trang **Navigation**

**Usage.** Component điều hướng sidebar để tổ chức các trang ứng dụng với section, mục lồng và icon. Dùng SideNav làm điều hướng chính khi ứng dụng có từ 5 đích đến trở lên hoặc cần nhóm theo phân cấp.

**Nên**

- ✅ Dùng section để nhóm mục điều hướng liên quan và giúp người dùng lướt tìm đích đến.
- ✅ Ghép biến thể icon viền và đặc để trạng thái được chọn khác biệt rõ.
- ✅ Đánh dấu trang hiện tại bằng isSelected: nó đặt aria-current="page", nên đích hiện tại được đọc ra chứ không chỉ dựa vào màu.
- ✅ SideNav vẽ một landmark điều hướng, và mục thu gọn được theo mẫu Disclosure của WAI-ARIA APG: nút bật/tắt mang aria-expanded và aria-controls, nhóm nó sở hữu bị vô hiệu tương tác khi thu gọn. Giữ nhãn mục ngắn; chúng đặt tên cho mục chỉ có icon trừ khi có aria-label có nghĩa bổ sung ngữ cảnh.
- ✅ Khi nav thu gọn, mục có con hiện chúng trong flyout submenu. Trên thiết bị hover được, trỏ vào mục sẽ mở sau một khoảng trễ ngắn và rời đi thì đóng; flyout mở bằng cú bấm giữ mở tới khi bị đóng. Trên cảm ứng, nó mở khi chạm. Không đặt vào đó hành động không có đường nào khác để tới.

**Không nên**

- ❌ Thêm SideNavHeading khi TopNav đã mang nhận diện ứng dụng; điều này lặp thương hiệu.
- ❌ Dùng để lọc nội dung; dùng tab hoặc nút lọc.

**Examples**

| Example | Mô tả |
|---|---|
| SideNav — End Content | Mục điều hướng bên có badge, số đếm và menu ngữ cảnh ở nội dung cuối. |
| SideNav — Nested Items | Điều hướng bên có mục lồng thu gọn được cho cài đặt hoặc menu phân cấp. |
| SideNav — Header with Menu | Điều hướng bên có dropdown chuyển tài khoản ở header cho ứng dụng nhiều tài khoản. |

## Stepper

`Stepper` · Figma: `Stepper` (+ `Stepper / Step`) · trang **Navigation**

**Usage.** Stepper hiển thị tiến trình qua một chuỗi bước logic có đánh số. Dùng cho quy trình nhiều bước như form, onboarding hay thanh toán, khi người dùng cần thấy vị trí hiện tại và các bước phía trước. Hiển thị dưới dạng danh sách có thứ tự (không phải landmark điều hướng).

**Nên**

- ✅ Giữ nhãn bước ngắn và mô tả: "Thanh toán" chứ không phải "Nhập thông tin thanh toán của bạn".
- ✅ Dùng hướng dọc khi bước có mô tả dài. Stepper ngang tự xử lý vùng chứa hẹp: khi khung cho mỗi bước ít hơn horizontalOptions.minimumStepWidth (mặc định 112px) nó bỏ nhãn, dùng thanh phân đoạn và hiện collapsedVariant đã cấu hình bên dưới.
- ✅ Đặt horizontalOptions.collapsedVariant là 'withLabel' khi trang đã có sẵn Quay lại/Tiếp tục, hoặc 'hiddenLabel' khi giao diện xung quanh sở hữu cả heading bước hiện tại lẫn điều hướng và chỉ cần một thanh tiến độ trần.
- ✅ Cung cấp onStepClick cho quy trình không tuyến tính khi người dùng có thể cần quay lại bước trước.
- ✅ Chỉ dùng status để áp màu ngữ nghĩa (accent/success/warning/error); truyền icon tùy biến cho chỉ báo phong phú hơn.

**Không nên**

- ❌ Dùng stepper cho ít hơn 3 bước; heading đơn giản hoặc thanh tiến độ tốt hơn.
- ❌ Dùng quá 7 bước; cân nhắc gộp bước liên quan hoặc dùng mẫu khác.

**Examples**

| Example | Mô tả |
|---|---|
| Stepper — Custom Content | Stepper dọc, mỗi bước sở hữu một phần của trang. Slot content nhận node bất kỳ (trường form, panel tóm tắt, banner), nên stepper không chỉ dành cho form nhiều bước. Chỉ hiển thị slot cho bước đang hoạt động là điều khiến luồng mở rộng từng bước một. |
| Stepper — Indicator Modes | Các giá trị prop indicator cạnh nhau: none (thanh và nhãn tự mang tiến độ), auto (dấu tích khi xong, vòng khi hiện tại, số cho bước phía trước), always-number, và icon tùy biến cho từng bước. |
| Stepper — On-Track Horizontal | Bố cục on-track hướng ngang: thay vì nằm cạnh nhãn, mỗi chỉ báo được gắn vào chính đường nối, nên các node đánh số đọc như hạt trên một đường liền. Nhãn căn giữa dưới node. |
| Stepper — On-Track Vertical | Bố cục on-track hướng dọc: chỉ báo nằm trong dòng trên một ray nối liền, nhãn và mô tả cạnh node. So với bố cục separated, nơi chỉ báo nằm cạnh đoạn thanh riêng của nó thay vì trên ray chung. |
| Stepper — Checkout Progress | Stepper mặc định: thanh ngang, mỗi bước sở hữu một đoạn bằng nhau của thanh tiến độ phía trên nhãn. Chỉ báo auto mặc định tự quyết theo từng bước: dấu tích khi xong, vòng ở bước hiện tại, số cho các bước còn phía trước. Bấm bước bất kỳ để nhảy tới. |
| Stepper — Validation Status | Status ngữ nghĩa theo bước trong luồng xác minh: success hiện dấu tích xanh, error ký hiệu đỏ, accent cho bước đang làm. Status chỉ đặt màu và ký hiệu chỉ báo, không bao giờ đổi đường nối, và được đọc thành chữ cho công nghệ hỗ trợ. |
| Stepper — Horizontal Narrow Collapsed | Stepper ngang hẹp dùng horizontalOptions. Ở bề rộng 320px, bốn bước xuống dưới minimumStepWidth 112px và thu gọn thành tóm tắt bước hiện tại kèm nút Trước và Sau. |

## Tab List

`TabList` · Figma: `Tabs / TabList`, `Tabs / .Tab` · trang **Navigation**

**Usage.** TabList cung cấp điều hướng dạng tab để tổ chức nội dung thành các phần phân loại. Dùng để người dùng chuyển giữa các view liên quan mà không rời trang, mục tràn được xử lý bằng menu "thêm" có sẵn.

**Nên**

- ✅ Giữ nhãn tab ngắn và mô tả để người dùng lướt nhanh các phần có sẵn.
- ✅ Để bật xử lý tràn: dải hẹp hơn các tab sẽ cuộn, và tab đang chọn luôn nằm trong tầm nhìn. Dùng TabMenu khi muốn một nhóm lựa chọn bổ sung được chọn lọc thay vì dải cuộn.
- ✅ Khi dùng hasDivider với nút hành động cạnh tab, khớp cỡ Button với cỡ TabList (cùng md, cùng sm); dải tab có divider chừa chỗ để tab và nút cùng cỡ thẳng một đường cơ sở phía trên đường kẻ.
- ✅ Dùng role="tablist" khi dải chuyển panel tại chỗ, và cho mỗi tab một panelId trỏ tới panel nó mở: đó là cách trình đọc màn hình đi từ tab tới nội dung. Bỏ khi điều hướng giữa các view.
- ✅ Đặt isFullBleed để giãn thanh tab trong LayoutHeader, Card hoặc Section có padding tới mép nội dung của vùng chứa, thay vì dùng CSS margin âm.

**Không nên**

- ❌ Dùng tab cho bước tuần tự hoặc quy trình; dùng stepper hoặc mẫu wizard.
- ❌ Đặt quá 6–8 tab hiển thị trước menu tràn; ưu tiên danh mục quan trọng nhất.
- ❌ Nhầm TabList với SegmentedControl hoặc ToggleButton. TabList để điều hướng giữa các view. SegmentedControl và ToggleButton là control nhập: SegmentedControl luôn có đúng một lựa chọn được chọn, còn ToggleButton bật hoặc tắt được.

**Examples**

| Example | Mô tả |
|---|---|
| TabList — Fill Layout | Tab giãn lấp bề rộng sẵn có, có divider dưới. |
| TabList — With Actions | Mẫu header trang với tab bên trái và nút hành động đẩy sang phải. Khi hasDivider là true, khớp cỡ Button với cỡ TabList để tab và hành động thẳng một đường cơ sở phía trên divider. |
| TabList — With Badge | Tab có badge số thông báo qua endContent. Dùng biến thể error cho số cấp bách và neutral cho số mang tính thông tin. |
| TabList — With Icons | Tab có icon đầu cạnh nhãn chữ. |
| TabList — With Overflow Menu | Tab list có dropdown menu cho mục bổ sung không vừa trong dòng. |
| TabList — With Status Dot | Tab có chấm trạng thái qua endContent để thấy nhanh sức khỏe môi trường trực tiếp. |

## Top Nav

`TopNav` · Figma: `Navigation / TopNav` (+ `Navigation / TopNavHeading`, `Navigation / .TopNavItem`) · trang **Navigation**

**Usage.** TopNav là thanh điều hướng ngang cho điều hướng cấp sản phẩm ở header ứng dụng. Dùng TopNav cho tối đa 5 mục điều hướng luôn hiển thị, hoặc điều hướng tối giản đi kèm tìm kiếm và control. Phân cấp điều hướng phức tạp thì dùng sidebar; để lọc nội dung thì dùng tab hoặc nút lọc.

**Nên**

- ✅ Có logo và tên sản phẩm ở slot heading để nhận diện rõ ứng dụng.
- ✅ Giới hạn mục điều hướng chính tối đa 5 để lướt nhanh và giảm tải nhận thức.

**Không nên**

- ❌ Tránh dùng TopNav để lọc nội dung trang; dùng Tabs hoặc control lọc.
- ❌ Tránh phân cấp điều hướng lồng sâu; giữ menu một cấp.

**Examples**

| Example | Mô tả |
|---|---|
| TopNav — Centered Navigation | Bố cục điều hướng có mục căn giữa, hai bên là heading logo và hành động cuối. |
| TopNav — Enterprise Dashboard | Thanh điều hướng đầy đủ với mục có icon và nhãn, tìm kiếm, thông báo và CTA chính. |
| TopNav — Hover Menu | Thanh điều hướng có dropdown mở khi hover, hiện mục sản phẩm có icon và mô tả. |
| TopNav — Mega Menu | Điều hướng kiểu marketing với mega menu tràn bề rộng gồm mục sản phẩm và card nổi bật quảng bá. |
| TopNav — Multiple Dropdowns | Thanh điều hướng có nhiều dropdown mở khi hover, tự đóng khi chuyển giữa chúng. |
| TopNav — With Logo | Thanh điều hướng có icon logo thương hiệu, liên kết heading, mục điều hướng và hành động hồ sơ. |

## Top Nav Mega Menu

`TopNavMegaMenu` · Figma: `Navigation / TopNavMegaMenu`, `Navigation / .TopNavMegaMenuItem` · trang **Navigation**

**Usage.** Mục điều hướng hiện panel mega menu tràn bề rộng khi hover. Dùng API slot với prop items và featured. TopNavMegaMenuItem tự hiển thị ở cả chế độ desktop và drawer di động. Hỗ trợ drawer thu gọn trong dòng qua context chế độ hiển thị.

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| TopNavMegaMenu — Basic | Trigger mega menu trong TopNav mở panel các mục liên kết phong phú. Dùng khi một phần điều hướng có nhiều đích đáng mô tả. |
| Top Nav Mega Menu | Minh họa TopNavMegaMenu với các mục và card nổi bật trong panel mega menu. |

## Top Nav Mega Menu Featured Card

`TopNavMegaMenuFeaturedCard` · Figma: `Navigation / .TopNavMegaMenuFeaturedCard` · trang **Navigation**

**Usage.** Card nổi bật chuẩn cho slot featured của TopNavMegaMenu. Cung cấp card nhất quán với ảnh, tiêu đề, mô tả và liên kết CTA (tùy chọn).

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| TopNavMegaMenuFeaturedCard — Basic | Card quảng bá có tiêu đề, mô tả và liên kết kêu gọi hành động. Truyền vào slot featured của TopNavMegaMenu để làm nổi thông báo. |
| Top Nav Mega Menu Featured Card | Minh họa TopNavMegaMenuFeaturedCard có tiêu đề, mô tả và liên kết CTA trong mega menu. |

## Top Nav Menu

`TopNavMenu` · Figma: `Navigation / TopNavMenu` · trang **Navigation**

**Usage.** Mục điều hướng hiện menu popover mở khi hover, gồm các mục phong phú có icon, tiêu đề và mô tả (tùy chọn).

**Nên / Không nên.** Astryx không có hướng dẫn cho component này. Dựa vào Usage và các example.

**Examples**

| Example | Mô tả |
|---|---|
| TopNavMenu — Basic | Dropdown menu trong TopNav dựng từ mảng items có icon và mô tả. Dùng để nhóm các đích liên quan dưới một trigger. |
| Top Nav Menu | Minh họa TopNavMenu với dropdown mở khi hover chứa các mục có icon và mô tả. |

---

# Overlay

## Bottom Sheet

`BottomSheet` · Figma: `BottomSheet` · trang **Overlay**

**Usage.** Bề mặt cảm ứng di động cho bộ lọc, hành động, form và màn chi tiết, trượt lên từ đáy viewport; dùng BottomSheetSwitcher cho luồng nhiều bước.

**Nên**

- ✅ Dùng cho bề mặt ưu tiên di động (bộ lọc, bảng chia sẻ, hành động nhanh) khi nội dung cần trượt lên từ mép dưới.
- ✅ Chọn chiều cao khởi đầu vừa nội dung: 'hug' cho nội dung ngắn có giới hạn, 'capped' cho danh sách, 'tall' cho form hoặc nội dung đang stream/đổi cỡ.
- ✅ Dùng purpose='form' để bảo vệ dữ liệu đã nhập khỏi cú bấm vào nền mờ và cú vuốt, nhưng vẫn cho Escape; để dành purpose='required' cho luồng phải kết thúc bằng một hành động rõ ràng.

**Không nên**

- ❌ Làm nội dung sheet quá dài. Cân nhắc chia thành bước và dùng Bottom Sheet Switcher.

**Examples**

| Example | Mô tả |
|---|---|
| Bottom Sheet — Height variants | So sánh chiều cao khởi đầu hug, capped và tall cho lượng nội dung khác nhau. |
| Bottom Sheet — Mobile keyboard | Form cao, cuộn được, giữ control đang focus hiển thị phía trên bàn phím di động. |
| Bottom Sheet — No scrim | Giữ trang phía sau nhìn thấy và tương tác được với bottom sheet không modal. |
| Bottom Sheet | Bề mặt lọc di động trượt lên từ mép dưới. |
| Bottom Sheet — Snap points | Điểm dừng khi kéo đổi cỡ: bề mặt làm việc nửa chiều cao, và mức hé nhìn trượt đi và làm mỏng nền mờ. |
| Dialog — Adaptive presentation | Công thức tùy chọn cho lớp bọc AdaptiveDialog: Dialog vẫn là mặc định ở mọi nơi, còn touchPresentation="bottom-sheet" chỉ chuyển ở cỡ lg trở xuống khi con trỏ thô và không hover được. Có ghi đè presentation xác định cho test/môi trường bất thường, và lưu ý purpose của BottomSheet điều khiển việc đóng bằng vuốt và nền mờ. Ví dụ dùng: touchPresentation="dialog" giữ Dialog, "fullscreen" chọn Dialog toàn màn, "bottom-sheet" chọn BottomSheet chỉ cho dải hướng cảm ứng. Giữ presentation làm ghi đè xác định. Không dùng mặc định cho AlertDialog hoặc xác nhận phá hủy. |
| DropdownMenu — Adaptive presentation | Chọn bottom sheet cho màn cảm ứng nhỏ và popover neo cạnh nút trong các trường hợp khác. Media query là chính sách sản phẩm, còn DropdownMenu lo cả hai cách hiển thị. |
| MultiSelector — Bottom Sheet | Giữ danh sách chọn nhiều mở trong bottom sheet trong khi bật/tắt các lựa chọn. |
| Selector — Bottom Sheet | Hiện danh sách chọn một trong bottom sheet cho giao diện cảm ứng nhỏ. |

## Bottom Sheet Switcher

`BottomSheetSwitcher` · Figma: không có set — nhiều khung `BottomSheet` nối bằng luồng · trang **Overlay**

**Usage.** Điều phối luồng bottom sheet nhiều bước trong một hộp thoại dùng chung; đặt activeSheet bằng sheetId của BottomSheet lồng bên trong để mở hoặc chuyển bước, và null để đóng.

**Nên**

- ✅ Dùng khi mỗi bước phụ thuộc bước trước và chỉ một bước cần chú ý tại một thời điểm.
- ✅ Cho mỗi con một sheetId duy nhất và label không rỗng, chọn purpose khớp yêu cầu đóng, và theo mẫu Dialog (Modal) của WAI-ARIA cho luồng có nền mờ.

**Không nên**

- ❌ Chia thông tin qua nhiều sheet khi người dùng cần so sánh chúng; dùng bố cục toàn trang giữ nội dung liên quan hiển thị cùng nhau.
- ❌ Dùng switcher khi nhiều panel phải cùng tương tác được hoặc cùng hiển thị; activeSheet cố ý chỉ chọn một bước tương tác.

**Examples**

| Example | Mô tả |
|---|---|
| Bottom Sheet Switcher — Review flow | Luồng form hai bước cho người dùng xem lại cài đặt, xác nhận, hoặc quay lại mà không thay hộp thoại dùng chung. |
| Bottom Sheet Switcher | Luồng ba bước chuyển giữa các sheet ôm nội dung có chiều cao khác nhau trong một hộp thoại dùng chung. |

## Command Palette

`CommandPalette` · Figma: `CommandPalette` (+ `.CommandPaletteItem`, `.CommandPaletteEmpty`) · trang **Overlay**

**Usage.** CommandPalette là hộp thoại tìm kiếm được để truy cập nhanh lệnh, điều hướng và hành động. Dùng làm trình khởi chạy điều khiển bằng bàn phím, lọc và chọn nhờ SearchSource.

**Nên**

- ✅ Cung cấp searchSource có kết quả khởi tạo để người dùng thấy lựa chọn hữu ích trước khi gõ.
- ✅ Dùng auxiliaryData.group trên mục để tự sắp xếp kết quả thành các section có nhãn.

**Không nên**

- ❌ Dùng CommandPalette cho dropdown hoặc menu đơn giản; dùng Menu hoặc Selector cho lựa chọn trong dòng.
- ❌ Thêm quá nhiều nhóm hoặc mục; chọn lọc kết quả để palette nhanh và dễ lướt.

**Examples**

| Example | Mô tả |
|---|---|
| CommandPalette — Async Search | Tìm kiếm phía server có spinner đang tải và trạng thái rỗng tùy biến. |
| CommandPalette — Grouped | Command palette có mục nhóm qua auxiliaryData.group. |
| CommandPalette — Custom Footer | Command palette có footer với thông điệp mẹo tùy biến. |
| CommandPalette — Picker Mode | Bộ chọn một giá trị, lựa chọn được giữ và có dấu tích chỉ báo. |
| CommandPalette — Rich Items | Hiển thị mục tùy biến có icon, phím tắt và tìm theo từ khóa. |
| Command Palette | Command palette cơ bản có mục tĩnh và điều hướng bàn phím. |

## Dialog

`Dialog` · Figma: `Dialog` · trang **Overlay**

**Usage.** Dialog hiển thị lớp phủ modal chặn tương tác với trang cho tới khi người dùng phản hồi. Dùng cho xác nhận xóa, form chỉnh sửa, chấp nhận điều khoản, hoặc quyết định không được bỏ qua. Khi muốn hiện dialog mà không quản lý state mở, dùng hook `useImperativeDialog`: gọi `dialog.show(content)` và đặt `dialog.element` trong cây.

**Nên**

- ✅ Chọn đúng purpose: info cho nội dung đóng được, form để tránh vô tình đóng khi bấm nền, required khi người dùng bắt buộc phản hồi.
- ✅ Có tiêu đề rõ ở header để người dùng hiểu ngay dialog đang hỏi gì.
- ✅ Dùng purpose="form" cho dialog có input để người dùng không vô tình mất dữ liệu khi bấm nền.
- ✅ Giữ dialog tập trung vào một tác vụ; nếu nội dung vượt quá sức chứa, cân nhắc dùng trang đầy đủ.

**Không nên**

- ❌ Dùng dialog cho thông điệp đơn giản có thể hiện trong dòng hoặc dạng toast.
- ❌ Lồng dialog trong dialog; tổ chức lại luồng thành các bước trong một dialog.
- ❌ Dùng biến thể fullscreen cho xác nhận đơn giản; nó dành cho nội dung phức tạp như trình soạn thảo hoặc form dài.

**Examples**

| Example | Mô tả |
|---|---|
| Dialog — Adaptive presentation | Công thức tùy chọn cho lớp bọc AdaptiveDialog: Dialog vẫn là mặc định ở mọi nơi, còn touchPresentation="bottom-sheet" chỉ chuyển ở cỡ lg trở xuống khi con trỏ thô và không hover được. Có ghi đè presentation xác định cho test/môi trường bất thường, và lưu ý purpose của BottomSheet điều khiển việc đóng bằng vuốt và nền mờ. Ví dụ dùng: touchPresentation="dialog" giữ Dialog, "fullscreen" chọn Dialog toàn màn, "bottom-sheet" chọn BottomSheet chỉ cho dải hướng cảm ứng. Giữ presentation làm ghi đè xác định. Không dùng mặc định cho AlertDialog hoặc xác nhận phá hủy. |
| Dialog — Confirmation | Yêu cầu người dùng xác nhận hành động phá hủy trước khi thực hiện. Dùng trước khi xóa dự án, gỡ thành viên, thu hồi API key, hoặc thao tác không hoàn tác được. |
| Dialog — Form | Thu nhập liệu mà không rời trang. Dùng purpose="form" nên bấm nền không đóng. Dùng cho sửa hồ sơ, tạo mục mới hoặc cập nhật cài đặt tại chỗ. |
| Dialog — Fullscreen | Chiếm toàn bộ viewport cho nội dung cần tối đa không gian. Dùng cho trình xem tài liệu, trình soạn thảo văn bản, wizard nhiều bước hoặc xem trước media khi bề rộng dialog chuẩn quá hẹp. |
| Dialog — Scrollable | Giới hạn chiều cao dialog và cuộn phần thân khi nội dung tràn. Dùng cho điều khoản, thỏa thuận giấy phép, changelog, hoặc nội dung dài người dùng cần xem trước khi chấp nhận. |
| Dialog | Dialog modal có header, nội dung thân và nút đóng. |
| Dialog — Required | Không đóng được bằng Escape hay bấm nền; người dùng phải chủ động chọn một hành động. Dùng purpose="required". Dùng cho chuyển quyền sở hữu, xác nhận pháp lý, hoặc quyết định quan trọng không được bỏ qua. |

## Hover Card

`HoverCard` · Figma: `HoverCard` · trang **Overlay**

**Usage.** HoverCard hiện thông tin bổ sung khi người dùng hover hoặc focus vào phần tử kích hoạt. Dùng cho card hồ sơ, tóm tắt liên kết, hoặc định nghĩa trong dòng khi người dùng cần thêm ngữ cảnh mà không rời trang.

**Nên**

- ✅ Giữ nội dung ở mức bổ sung; hover card nâng cao hiểu biết mà không chặn luồng công việc chính.
- ✅ Có gạch chân nét đứt trên trigger dạng chữ để người dùng biết phần tử hover được.
- ✅ Dùng API hook (useHoverCard) khi cần kiểm soát thời điểm hoặc vị trí nhiều hơn.
- ✅ Để touchTrigger ở auto để chạm mở card trên trigger không làm gì khác, và không cản trở trên trigger thực hiện hành động.
- ✅ Ưu tiên đặt HoverCard trong ngữ cảnh khối thay vì trực tiếp trong <p>, heading hoặc liên kết. Các vị trí đó vẫn được hỗ trợ khi cần qua portal sửa lỗi, nhưng DOM và thứ tự tab có thể khác.

**Không nên**

- ❌ Đặt hành động quan trọng hoặc thông tin bắt buộc trong hover card; người dùng có thể bỏ lỡ nội dung chỉ hiện khi hover.
- ❌ Dùng hover card khi Tooltip hoặc Popover đơn giản là đủ.
- ❌ Dùng HoverCard cho nội dung người dùng phải tương tác; nó biến mất khi con trỏ rời đi.

**Examples**

| Example | Mô tả |
|---|---|
| HoverCard — Definition | Hiện định nghĩa thuật ngữ khi hover trong đoạn văn. Dùng cho thuật ngữ kỹ thuật, biệt ngữ hoặc khái niệm một số người đọc chưa biết, như bảng thuật ngữ gắn trong chữ. |
| HoverCard — Link Preview | Hiện tóm tắt trang khi hover liên kết: tiêu đề, mô tả và URL. Dùng cho liên kết tài liệu, tham chiếu bài viết, hoặc URL mà xem trước giúp người dùng quyết định có bấm không. |
| HoverCard — Profile Preview | Hiện tóm tắt hồ sơ người dùng khi hover với tên, vai trò và tiểu sử. Dùng trên tên người dùng, avatar hoặc nhắc tên để xem trước hồ sơ mà không rời trang. |
| Hover Card | Hover card hiện xem trước hồ sơ người dùng khi hover nút kích hoạt. Mở sẵn để xem trước. |

## Lightbox

`Lightbox` · Figma: `Lightbox` · trang **Overlay**

**Usage.** Lớp phủ toàn màn để xem ảnh và video ở độ phân giải đầy đủ. Hỗ trợ chế độ một mục và thư viện có điều hướng trước/sau, phóng to và kéo ảnh (tùy chọn), và control video gốc.

**Nên**

- ✅ Luôn có alt cho mọi ảnh để trợ năng trình đọc màn hình.
- ✅ Dùng chế độ thư viện với onIndexChange cho tập nhiều ảnh.
- ✅ Chỉ bật hasZoom khi xem ảnh độ phân giải cao cần soi kỹ.

**Không nên**

- ❌ Dùng lightbox cho nội dung không phải ảnh; nó chuyên cho ảnh.
- ❌ Lồng nội dung tương tác trong chú thích; giữ chúng là chữ thường.

**Examples**

| Example | Mô tả |
|---|---|
| Lightbox — Gallery | Lưới thumbnail mở thư viện toàn màn. Bấm thumbnail bất kỳ mở lightbox ở vị trí đó. Điều hướng trước/sau cho người dùng duyệt mọi ảnh mà không đóng. |
| Lightbox | Trình xem ảnh toàn màn có chú thích. |
| Lightbox — Video | Mở video trong lightbox. Có control gốc của trình duyệt. Phóng to và kéo bị tắt với mục video. |
| Lightbox — Zoom | Lightbox bật phóng to và kéo. Bấm đúp ảnh để phóng to; kéo để di chuyển. Bấm đúp lần nữa hoặc dùng nút đóng để thoát. |

## Overlay

`Overlay` · Figma: `Overlay` · trang **Overlay**

**Usage.** Overlay phủ nội dung hành động hoặc hỗ trợ lên media, card, video hoặc bề mặt có biên khác, có nền mờ và hành vi hiện ra (tùy chọn).

**Nên**

- ✅ Dùng overlay cho hành động hoặc nhãn ngắn, theo ngữ cảnh, thuộc trực tiếp về media hoặc bề mặt bên dưới.
- ✅ Giữ nội dung overlay gọn để vẫn đọc được trên nền mờ và không che thông tin hình ảnh quan trọng.

**Không nên**

- ❌ Dùng Overlay cho nội dung nổi neo bên ngoài bề mặt. Dùng Popover, Tooltip hoặc Dialog cho các mẫu đó.

**Examples**

| Example | Mô tả |
|---|---|
| Overlay — Bottom Strip | Đặt nội dung hỗ trợ gọn trong dải nền mờ ở đáy mà không che hết ảnh. |
| Overlay — Hover Reveal | Hiện hành động overlay khi hover hoặc focus bàn phím. Dùng khi hành động nên im lặng về thị giác cho tới khi media được chú ý. |
| Overlay | Card media có nền mờ luôn hiện và nội dung hành động căn giữa. |

## Popover

`Popover` · Figma: `Popover` · trang **Overlay**

**Usage.** Lớp phủ mở bằng cú bấm, neo vào một nút hoặc phần tử kích hoạt. Dùng cho hành động phụ, xác nhận trong dòng, hoặc thông tin bổ sung không đáng dùng cả một dialog. Xem trước khi hover thì dùng HoverCard, chữ trợ giúp ngắn thì dùng Tooltip.

**Nên**

- ✅ Giữ nội dung popover tập trung vào một tác vụ hoặc một mẩu thông tin.
- ✅ Có cách đóng rõ ràng: bấm ra ngoài hoặc nút đóng tường minh.
- ✅ Tạo theme cho bề mặt vẽ qua target popover. Ghi đè popover-surface cũ vẫn được hỗ trợ để tương thích, còn theme mới dùng target chuẩn.

**Không nên**

- ❌ Lồng popover trong popover; gây rối focus và điều hướng.
- ❌ Cho rằng chỉ độ phức tạp của input quyết định cách hiển thị; hãy đánh giá yêu cầu về focus, không gian và tương tác của tác vụ.
- ❌ Cho rằng chỉ việc cuộn nghĩa là Popover là component sai; một Popover có biên có thể cuộn trong khi tương tác neo tập trung vẫn phù hợp.

**Examples**

| Example | Mô tả |
|---|---|
| Popover — Bottom Sheet Alternative | Phương án BottomSheet tùy chọn cho màn cảm ứng nhỏ, khi hành động nên hiển thị dạng modal neo vào mép dưới. |
| Popover — Confirm Action | Popover xác nhận trong dòng cho hành động phá hủy, có nút xóa và hủy. |
| Popover — Filter Panel | Popover có bộ lọc checkbox và hành động áp dụng/đặt lại. |
| Popover — Keyboard Shortcuts | Popover hiện danh sách phím tắt theo cặp phím và mô tả. |
| Popover — Settings Panel | Popover có switch để quản lý tùy chọn người dùng như thông báo, chế độ tối và âm thanh. |

## Toast

`Toast` · Figma: `Toast` · trang **Overlay**

**Usage.** Toast hiện thông báo ngắn, không chặn, để xác nhận một hành động hoặc đưa thông tin tạm thời. Dùng khi người dùng cần phản hồi nhưng không cần quyết định, như lưu, xóa hay đổi trạng thái. Khi dùng thật, ưu tiên hook `useToast()`; nó lo vị trí, xếp chồng, tự đóng và khử trùng lặp qua `ToastViewport`. Toast nằm trong lề viewport và vùng an toàn, xuống dòng với nội dung dài, và vào, ra hoặc vuốt để đóng về phía mép trên hoặc dưới đã cấu hình. Vuốt dọc dùng cùng mô hình không gian như chuyển động vị trí: toast ở trên rời đi lên trên, toast ở dưới rời đi xuống dưới. Vuốt chờ ý định rõ ràng hướng về mép trước khi hủy chuyển động chạm gốc, và báo lý do đóng thủ công sẵn có. Bút được hỗ trợ như nhập chạm trực tiếp; kéo chuột bị loại để không xung đột với bôi chọn chữ trên desktop, nơi nút đóng hiển thị vẫn có sẵn. Đặt `isAutoHide: false` tường minh khi hành động hoặc thông điệp phải còn đó. Component `Toast` vẽ phần tử toast trong dòng, hữu ích cho xem trước, tài liệu và trình diễn tĩnh không cần vòng đời viewport.

**Nên**

- ✅ Giữ thông điệp ngắn: vài từ cho người dùng biết chuyện gì đã xảy ra, như "Đã lưu thay đổi" hay "Đã gửi tin nhắn".
- ✅ Thêm hành động hoàn tác ngắn ở slot endContent cho thao tác đảo ngược được. Đặt isAutoHide là false khi hành động phải còn đó.
- ✅ Dùng uniqueID để khử trùng lặp toast bắn ra từ hành động lặp lại, như bấm nút lưu nhiều lần.
- ✅ Dùng loại error cho thất bại cần chú ý nhưng không cần hành động ngay; nó giữ tới khi bị đóng để người dùng không bỏ lỡ.

**Không nên**

- ❌ Dùng toast cho lỗi nghiêm trọng chặn người dùng. Dùng Banner cho thông điệp cố định, đúng ngữ cảnh, cần xác nhận.
- ❌ Đặt nội dung dài hoặc nhiều dòng trong toast; nó biến mất sau 5 giây và người dùng có thể chưa đọc xong.
- ❌ Hiện lỗi kiểm tra form dưới dạng toast. Dùng kiểm tra tại trường để người dùng thấy chính xác trường nào cần sửa.

**Examples**

| Example | Mô tả |
|---|---|
| Toast — Action | Toast cố định có nút hoặc liên kết ở cuối để người dùng hành động theo thông báo, như hoàn tác xóa hoặc xem báo cáo. |
| Toast — Deduplication | Chặn toast trùng lặp bằng uniqueID. Dùng ignore để giữ toast đầu, hoặc overwrite để thay bằng nội dung cập nhật như phần trăm tiến độ. |
| Toast — Dismiss | Hiện toast cố định và đóng bằng code qua hàm useToast trả về. Dùng cho thao tác chạy lâu cần dọn thủ công. |
| Toast | Thông báo toast gọi bằng code qua useToast và hiển thị trong toast viewport. |
| Toast — Stacking | Nhiều toast xếp chồng dọc với hiệu ứng vào/ra mượt. Bấm liên tục để xem toast xếp hàng và đóng thế nào. |
| Toast — Types | Biến thể toast info và error cạnh nhau. Toast info tự đóng sau 5 giây, toast error giữ tới khi người dùng đóng. |

## Tooltip

`Tooltip` · Figma: `Tooltip` · trang **Overlay**

**Usage.** Gợi ý chữ ngắn hiện khi hover hoặc focus, neo vào phần tử kích hoạt. Dùng để mô tả nút chỉ có icon, hiện đầy đủ chữ của nhãn bị cắt, hoặc cung cấp ngữ cảnh bổ sung mà không làm rối giao diện.

**Nên**

- ✅ Giữ nội dung tooltip ngắn gọn: nhắm dưới 140 ký tự chữ thường.
- ✅ Thêm tooltip cho nút chỉ có icon và control thiếu nhãn hiển thị.
- ✅ Đặt touchTrigger là tap khi trigger là nút chỉ để hiện tooltip, như icon thông tin: cảm ứng không có hover, còn auto giữ cú chạm cho trigger thực hiện hành động.

**Không nên**

- ❌ Đặt phần tử tương tác như liên kết hay nút trong tooltip; dùng HoverCard hoặc Popover.
- ❌ Dùng tooltip cho thông tin thiết yếu người dùng bắt buộc phải thấy để hoàn thành tác vụ.

**Examples**

| Example | Mô tả |
|---|---|
| Tooltip — Action Bar | Tooltip trên thanh nút hành động với mô tả theo ngữ cảnh. |
| Tooltip — Hook Usage | Tooltip dùng hook useTooltip để điều khiển bằng code. |
| Tooltip — Inline Text | Tooltip trên thuật ngữ trong dòng để định nghĩa. |

---

# Table & List

## List

`List` · Figma: `List` (+ `List / .ListItem`), `Item` · trang **Table & List**

**Usage.** Tập mục theo chiều dọc với khoảng cách, divider nhất quán và dấu đầu dòng (tùy chọn). Hỗ trợ header, icon, avatar, badge và mục tương tác có hành vi bấm hoặc liên kết. Dùng để hiển thị nhóm nội dung liên quan có thứ tự hoặc không thứ tự.

**Nên**

- ✅ Có header để gắn nhãn danh sách và cho trình đọc màn hình ngữ cảnh.
- ✅ Dùng slot nội dung đầu và cuối để thêm icon, avatar hoặc badge cho từng mục.

**Không nên**

- ❌ Đặt phần tử tương tác trong mục danh sách tương tác; tạo vùng bấm lồng nhau và hành vi focus khó hiểu.
- ❌ Dùng danh sách cho một mục duy nhất hoặc để dàn nội dung không liên quan; danh sách ngụ ý một tập có nghĩa.
- ❌ Trộn mục bấm được và không bấm được trong cùng danh sách mà không có khác biệt thị giác rõ.

**Examples**

| Example | Mô tả |
|---|---|
| List — Basic | Danh sách đơn giản có nhãn và mô tả cho bố cục kiểu cài đặt. |
| List — Bulleted Features | Danh sách gạch đầu dòng các điểm nổi bật dùng dấu chấm tròn. |
| List — Message List | Danh sách tin nhắn kiểu chat có avatar, chữ xem trước và badge chưa đọc. |
| List — Ordered Steps | Hướng dẫn từng bước đánh số dùng dấu thập phân. |

## Metadata List

`MetadataList` · Figma: `MetadataList` · trang **Table & List**

**Usage.** MetadataList hiển thị cặp khóa–giá trị cho thuộc tính đối tượng như chất lượng, tình trạng, trạng thái, theo bố cục có cấu trúc. Dùng cho panel chi tiết, tóm tắt cài đặt và thông tin bản ghi.

**Nên**

- ✅ Chọn vị trí nhãn theo nội dung: "start" cho giá trị ngắn, "top" cho giá trị dài hoặc phức tạp.
- ✅ Thu gọn danh sách dài bằng `maxNumOfItems` để trang dễ lướt.

**Không nên**

- ❌ Dùng cho nhập liệu form nhiều; dùng bố cục form.
- ❌ Dùng cho dữ liệu không có cấu trúc khóa–giá trị rõ ràng.

**Examples**

| Example | Mô tả |
|---|---|
| MetadataList — Basic | Danh sách metadata khóa–giá trị một cột. |
| MetadataList — Collapsible | Danh sách metadata có nút xem thêm sau một số mục nhất định. |
| MetadataList — Horizontal | Mục metadata xếp ngang để hiển thị gọn trong dòng. |
| MetadataList — Multi-Column | Lưới metadata nhiều cột có thẻ token. |

## Overflow List

`OverflowList` · Figma: `OverflowList` · trang **Table & List**

**Usage.** Danh sách ngang tự ẩn mục khi vượt bề rộng sẵn có. Dùng OverflowList cho breadcrumbs, toolbar, danh sách thẻ, hoặc hàng cần thu gọn mượt ở cỡ nhỏ.

**Nên**

- ✅ Cung cấp overflowRenderer có nghĩa: badge "+N nữa", dropdown hoặc chỉ báo số đếm.
- ✅ Khi hàng đã có menu riêng, dùng onOverflowChange để đưa các mục bị thu vào menu đó thay vì thêm điểm neo thứ hai bằng overflowRenderer.
- ✅ Đặt minVisibleItems để giữ mục chính luôn hiển thị, và maxVisibleItems để giới hạn hàng ở số lượng cố định bất kể bề rộng.
- ✅ Dùng maxRows để mục xuống dòng tới một số hàng giới hạn (ví dụ đám thẻ hai hàng) trước khi thu phần còn lại vào chỉ báo.

**Không nên**

- ❌ Dùng OverflowList cho chồng dọc; xuống dòng nhiều hàng theo chiều ngang được hỗ trợ qua maxRows, nhưng mục vẫn chảy trái sang phải, không trên xuống dưới.

**Examples**

| Example | Mô tả |
|---|---|
| OverflowList — Capped Toolbar | maxVisibleItems giới hạn hàng ở ba hành động kể cả khi vừa được nhiều hơn; phần còn lại chuyển vào dropdown. |
| OverflowList — Collapse From Start | Danh sách tràn ẩn mục từ đầu, giữ mục mới nhất hiển thị. |
| OverflowList — Multi-row Tags | Thẻ xuống dòng tối đa hai hàng bằng maxRows, rồi thu phần còn lại vào badge số đếm. |
| OverflowList — Badge Tags | Hàng badge đổi cỡ được, thu thành badge số đếm khi tràn. |
| OverflowList — Dropdown Actions | Toolbar hành động thu nút tràn vào dropdown menu. |
| Overflow List | Danh sách nút thu mục tràn vào chỉ báo +N. |
| Toolbar — Table Filter | Thanh lọc trên bảng: ô tìm kiếm đứng đầu hàng, mỗi trường bên cạnh là một trigger đóng đồng thời là chip lọc của chính nó (chưa đặt thì hiện tên trường, đã đặt thì hiện cả mệnh đề), các mệnh đề gấp dần từ cuối thành một con số khi hàng hẹp lại, tiếp theo là số kết quả trực tiếp, nút xóa hết và bộ chọn cột. Dùng để tìm, lọc, thu hẹp các dòng bản ghi phẳng như công việc, đơn hàng, ticket, người dùng. |

## Table

`Table` · Figma: `TableHeaderCell`, `TableCell` · trang **Table & List**

**Usage.** Table hiển thị dữ liệu có cấu trúc theo hàng và cột với số chiều nhất quán. Hỗ trợ nội dung ô phong phú, sắp xếp, chọn, phân trang và quản lý cột qua hệ plugin ghép được. Dùng Table cho tập dữ liệu có cấu trúc đồng nhất; dữ liệu đơn giản hơn hoặc không nhất quán thì cân nhắc bố cục danh sách hoặc card.

**Nên**

- ✅ Dùng biến thể mật độ và divider khớp mật độ thông tin và nhu cầu lướt của dữ liệu.
- ✅ Ghép nội dung ô phong phú bằng component Astryx như Badge, StatusDot, Avatar qua renderCell.
- ✅ Ở chế độ children, đặt mọi hàng trong TableHeader, TableBody hoặc TableFooter. <table> không chứa <tr> trực tiếp được: parser HTML chèn <tbody> ngầm cho markup render phía server còn React thì không ở client, nên hàng không bọc sẽ lệch khi hydrate.
- ✅ Đặt bề rộng tường minh cho mọi cột bằng proportional() hoặc pixel(). proportional(1) chia flex đều với tối thiểu 120px, ngăn cột sụp trên viewport hẹp. Bỏ width thì mất mức tối thiểu.
- ✅ Dùng API hướng dữ liệu từ React Server Components: proportional(), pixel() và định nghĩa cột không có prop hàm là an toàn phía server. Cột dùng renderCell (hoặc prop hàm bất kỳ) cần bọc bảng trong component "use client", vì hàm không qua được ranh giới server-client.

**Không nên**

- ❌ Dùng bảng cho dữ liệu không có cột nhất quán. Dùng bố cục danh sách hoặc card cho nội dung không đồng nhất.
- ❌ Bật mọi plugin cùng lúc. Chỉ thêm tính năng tình huống cần để giao diện tập trung.
- ❌ Bỏ width ở cột nhiều chữ; không có proportional() tường minh thì chúng không có tối thiểu và có thể bị ép gần bằng 0 trên di động.

**Quy tắc dự án** (ở `docs/design.md`, thắng file này nếu lệch): § Quy tắc bảng danh sách · § Sửa trong bảng
(sửa trong ô, báo lỗi ô) · § Phân trang danh sách · § Bộ lọc nâng cao · § Tuỳ chỉnh cột.

**Examples**

| Example | Mô tả |
|---|---|
| Table — Column Settings | Bảng có bộ chọn hiển thị cột trên toolbar. Bật/tắt cột. |
| Table — Popover Filters | Bảng có control lọc dạng popover mở từ icon ở header cột. |
| Table — Grid Dividers | Bảng gọn có divider dạng lưới hiện cả viền hàng và cột, hợp cho dữ liệu số dày đặc. |
| Table — In Card | Bảng đặt trong card có heading, minh họa căn lề tràn vùng chứa. |
| Table — Inline Filters | Bảng có control lọc trong dòng hiển thị ngay dưới mỗi header cột. |
| Table — Paginated Data | Bảng dữ liệu phân trang, đi qua tập dữ liệu lớn từng trang. |
| Table — Resizable Columns | Bảng có tay nắm đổi cỡ cột kéo được. Kéo mép phải của header bất kỳ để đổi cỡ. |
| Table — Rich Cell Content | Bảng có nội dung ô phong phú, dùng Link cho email và Badge cho nhãn vai trò. |
| Table — Row Selection | Bảng có checkbox chọn hàng và checkbox chọn tất cả ở header. |
| Table | Bảng hướng dữ liệu có bề rộng cột theo tỉ lệ và pixel, tô sáng khi hover. |
| Table — Sortable Columns | Bảng có cột sắp xếp được, bấm header để sắp tăng hoặc giảm. |
| Table — Striped Rows | Bảng có màu hàng xen kẽ và tô sáng khi hover để dễ lướt. |

## Tree List

`TreeList` · Figma: `TreeList` (+ `TreeList / .TreeListItem`, `.TreeRail`) · trang **Table & List**

**Usage.** Cấu trúc cây mở rộng được để hiển thị dữ liệu phân cấp với đường nối nhánh. Dùng cho trình duyệt tệp, duyệt danh mục lồng nhau, hoặc giao diện trực quan hóa quan hệ cha–con.

**Nên**

- ✅ Cung cấp nhãn và icon có nghĩa cho mỗi node để phân cấp dễ lướt.
- ✅ Mở sẵn các nhánh quan trọng để người dùng thấy ngay nội dung chính.
- ✅ Hàng lá chừa chỗ cho cột chevron bất cứ khi nào cây có mục mở rộng được để thẳng hàng; chỉ cây phẳng hoàn toàn (không có mục mở rộng nào) mới vẽ hàng sát lề. Dựa vào điều này thay vì chỉnh thụt lề bằng CSS tùy biến.

**Không nên**

- ❌ Lồng sâu quá 4–5 cấp; làm phẳng cấu trúc hoặc dùng mẫu khác.
- ❌ Dùng cây cho dữ liệu phẳng, không phân cấp; dùng List.

**Examples**

| Example | Mô tả |
|---|---|
| TreeList — File Tree With Icons | Cây trình duyệt tệp có icon thư mục và tài liệu phân biệt thư mục với tệp. |
| TreeList — Interactive Settings | Cây cài đặt có mục bấm được và liên kết tài liệu. |
| TreeList — Mailbox Tree | Cây thư mục email có badge số chưa đọc. |
| TreeList — Navigation Tree | Cây điều hướng có mục được chọn cho trang hiện tại. |
| Tree List — Variants | Prop `variant` điều khiển có hiện đường dẫn phân cấp không: `lineGuides` (mặc định) vẽ đường nối giữa hàng cha và con, `noGuides` chỉ dựa vào thụt lề. Nó độc lập với `density`, vốn điều khiển khoảng cách. |

---

# Utility

## VisuallyHidden

`VisuallyHidden` · Figma: không vẽ (không có hình) · trang **Utility** (chỉ có hướng dẫn)

**Usage.** Hiển thị nội dung trong cây trợ năng nhưng ẩn về hình. Dùng cho tên truy cập của control chỉ có icon, vùng thông báo aria-live, và ngữ cảnh bổ sung cho trình đọc màn hình. Cố ý không có prop tạo kiểu; mục đích là luôn vô hình.

**Nên**

- ✅ Dùng để đặt tên truy cập cho nút và control chỉ có icon để trình đọc màn hình đọc được.
- ✅ Hiển thị dạng khối (as="div") với aria-live để thông báo cập nhật động như kéo thả hoặc số kết quả.

**Không nên**

- ❌ Dùng để ẩn nội dung với mọi người; nó vẫn nằm trong cây trợ năng; dùng render có điều kiện hoặc `hidden` để gỡ hẳn nội dung.
- ❌ Đặt control tương tác bên trong; nội dung không nhìn thấy và không nhận được thao tác con trỏ.

**Examples**

| Example | Mô tả |
|---|---|
| VisuallyHidden — Live Region | Vùng aria-live mức polite thông báo các thay đổi trạng thái chỉ có trên hình cho công nghệ hỗ trợ. |
| VisuallyHidden — Structural Heading | Đặt tên truy cập cho một phần ngầm định về hình để người dùng trình đọc màn hình điều hướng tới. |
| VisuallyHidden — Supplementary Context | Thêm ngữ cảnh chỉ cho trình đọc màn hình vào dữ liệu hình ảnh ngắn gọn, như nói rõ mũi tên xu hướng nghĩa là gì. |
