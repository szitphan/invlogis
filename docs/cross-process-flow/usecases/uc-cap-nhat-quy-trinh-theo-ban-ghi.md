# Use Case: Cập nhật quy trình theo bản ghi

> Scope: Liên quy trình (dùng chung mọi module) · Level: sea

## Primary Actor

Hệ thống — hành động theo sự kiện của bản ghi nghiệp vụ (gửi, phê duyệt, từ chối, thu hồi, xoá, chốt công nợ, thanh toán).

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Người tạo bản ghi | Không thu hồi/xoá nhầm bản ghi đã có bước con |
| Người theo dõi quy trình | Trạng thái bước và quy trình luôn đúng, không phải sửa tay |

## Trigger

Một bản ghi thuộc bảng liên quy trình đổi trạng thái (gửi thành công, phê duyệt, từ chối, thu hồi, xoá), hoặc bảng công nợ được chốt lần đầu / phần công nợ của luồng được thanh toán.

## Preconditions

- Nghiệp vụ của bản ghi đã khai bảng liên quy trình (BR-cross-process-flow-007).

## Guarantees

- **Minimal Guarantee:** Không có bước nào gắn vào 2 cây; không có bản ghi đã sinh bước con bị thu hồi/xoá khi bảng liên quy trình không cho phép; trạng thái quy trình không bị sửa tay.
- **Success Guarantee:** Bước của bản ghi mang trạng thái mới; Quy trình mang trạng thái tính lại theo BR-cross-process-flow-002/003; màn đang mở nhận được báo cập nhật.

## Main Success Scenario

1. Bản ghi gốc của một luồng gửi thành công.
2. Hệ thống tạo Quy trình ở trạng thái Đang triển khai, sinh mã `QT-[Mã chi nhánh]-[YY]-[XXXX]` (FR-cross-process-flow-001, BR-cross-process-flow-004) và tạo Bước gốc.
3. Một bản ghi tiếp theo (bước chính hoặc nhánh phát sinh) gửi thành công.
4. Hệ thống thêm Bước vào cây của bản ghi nguồn, nối về đúng bản ghi tạo ra nó, lưu trường hợp phát sinh theo giá trị lúc xảy ra (FR-cross-process-flow-003, BR-cross-process-flow-005); bước ở Đang triển khai, thẻ bước hiện mã yêu cầu (BR-cross-process-flow-012). Ghi nhận gửi và thêm bước cùng thành công hoặc cùng không.
5. Bản ghi của bước được phê duyệt ở hành động cuối (hoặc hoàn tất theo UC riêng của nghiệp vụ).
6. Hệ thống chuyển Bước sang Đã hoàn thành (FR-cross-process-flow-004); thẻ bước đổi sang mã bản ghi khi bản ghi được duyệt (BR-cross-process-flow-012).
7. Hệ thống tính lại trạng thái Quy trình; khi mọi bước chính và nhánh phát sinh đã xong (không tính nhánh Đã huỷ) → Đã hoàn thành (BR-cross-process-flow-003).

## Extensions

**1a. Luồng độc lập (bản ghi gốc tự nó không tạo quy trình):**
- 1a1. Hệ thống chưa tạo quy trình. Khi nhánh phát sinh đầu tiên gửi thành công → tạo Quy trình với bản ghi gốc là nút đầu cây, tiếp bước 2.

**1b. Bản ghi chỉ được lưu nháp:**
- 1b1. Hệ thống không làm gì. Use case kết thúc.

**3a. Cây không nhận bước (lỗi khi thêm bước):**
- 3a1. Bản ghi không được ghi nhận gửi, giữ nguyên bản nháp (FR-cross-process-flow-003). Use case kết thúc với Minimal Guarantee.

**3b. Bản ghi nguồn vừa bị thu hồi trong lúc gửi:**
- 3b1. Thu hồi thắng: hệ thống chặn bằng popup E-cross-process-flow-003, bản nháp giữ lại (FR-cross-process-flow-003). Use case kết thúc với Minimal Guarantee.

**3c. Bước khai "1 bản ghi" đang có bản ghi Đã thu hồi/từ chối:**
- 3c1. Bản ghi mới thành bản ghi hiện hành; bản cũ mang nhãn Đã thay thế, không tính vào tiến độ (BR-cross-process-flow-011).
- 3c2. Bước về Đang triển khai; nếu là bước của luồng chính → Quy trình về Đang triển khai (BR-cross-process-flow-002). Tiếp bước 5.

**5a. Bản ghi bị từ chối hoặc thu hồi:**
- 5a1. Hệ thống chuyển Bước sang Đã thu hồi/từ chối; nhánh con đã có giữ nguyên.
- 5a2. Nếu là bước của luồng chính → Quy trình chuyển Đã dừng. Nếu là nhánh phát sinh → Quy trình giữ nguyên, Bước đang chờ = nhánh đó (BR-cross-process-flow-002).
- 5a3. Khi bản ghi được sửa và gửi lại (giữ nguyên mã yêu cầu), hoặc bước nhận bản ghi thay thế (3c) → Bước về Đang triển khai; nếu là bước của luồng chính → Quy trình về Đang triển khai. Tiếp bước 5.
- 5a4. Bản ghi đã bị thay thế mà được sửa rồi gửi lại → hệ thống chặn bằng E-cross-process-flow-001 (BR-cross-process-flow-011).

**5b. Người tạo thu hồi hoặc xoá bản ghi đã sinh bước con:**
- 5b1. Hệ thống chặn bằng popup E-cross-process-flow-002 (GR-15 Loại 2), nêu tối đa 2 bước con kèm mã + "và n bước khác"; bản ghi giữ nguyên trạng thái (FR-cross-process-flow-014). Hiện chưa nghiệp vụ nào cho thu hồi/xoá khi đã có bước con (Giả định spec Mục 11). Use case kết thúc với Minimal Guarantee.

**5c. Bản ghi đang Đã thu hồi/từ chối bị xoá (chỉ nghiệp vụ cho xoá):**
- 5c1. Bước của luồng chính: về Chưa triển khai, mã về `N/A`, hiện "Chưa tạo"; Quy trình tính lại như thể bản ghi đó chưa từng có (BR-cross-process-flow-002, BR-cross-process-flow-009).
- 5c2. Nhánh phát sinh: chuyển Đã huỷ (viền đứt, chữ gạch), không tính vào tiến độ, không chặn Quy trình Đã hoàn thành (BR-cross-process-flow-009, BR-cross-process-flow-003).
- 5c3. Bản ghi Đã thay thế: bỏ khỏi khối "Bản ghi trước đó", không đổi trạng thái gì (BR-cross-process-flow-009).

**5d. Bước là thanh toán trả sau:**
- 5d1. Chốt công nợ lần đầu → Bước Đang triển khai; phần công nợ thuộc nghiệp vụ của luồng đã thanh toán → Bước Đã hoàn thành (FR-cross-process-flow-004, BR-cross-process-flow-006). Tiếp bước 7.

**7a. Có màn sơ đồ / danh sách đang mở chứa quy trình này:**
- 7a1. Nếu thông tin đang hiện trên màn đó đổi, hệ thống báo cập nhật để màn đó hiện banner Theo GR-27 (FR-cross-process-flow-020).

## Related Requirements

FR-cross-process-flow-001 → 004, FR-cross-process-flow-014, FR-cross-process-flow-020 · BR-cross-process-flow-001 → 006, BR-cross-process-flow-007, BR-cross-process-flow-008, BR-cross-process-flow-009 → 012 · E-cross-process-flow-001, -002, -003 · NFR-cross-process-flow-010 — [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]]
