# Dispatch Management — BA Workspace

Không gian làm việc phân tích nghiệp vụ (BA) cho hệ thống quản lý vận hành của **Delta**, doanh nghiệp vận tải có đội đầu kéo, xe tải và sơ mi-rơ mooc. Repo chứa tài liệu yêu cầu, không chứa mã nguồn sản phẩm.

## Dự án làm gì

Hệ thống mới (Delta 3.0 / Delta MIS giai đoạn 1) gồm hai mảng:

- **Điều phối vận tải**: nhận đơn, điều xe, theo dõi chuyến, giao nhận container, chứng từ hiện trường. Thiết kế đích (to-be) lấy từ các SOP Delta gửi.
- **Vận hành nội bộ** (kế thừa hệ thống cũ, SRS LG): xưởng sửa chữa, kho phụ tùng, mua hàng hoá dịch vụ, thanh toán và công nợ, quản lý phương tiện, nghiệp vụ cây dầu.

Người dùng gồm nhân viên nội bộ Delta (Website), lái xe, nhân viên hiện trường và nhân viên đối tác cây dầu (Delta Super App — app mobile dùng chung cho nhiều bên; Partner Portal cũ đã gộp vào). Quyền truy cập cấp theo chức năng, không theo vai trò cố định. Dữ liệu tổ chức theo Công ty → Chi nhánh → Cơ sở.

## Đang ở đâu

| Hạng mục | Trạng thái |
|---|---|
| Bối cảnh dự án, glossary, môi trường vận hành | Có trong `docs/_shared/` |
| Bản đồ đối tượng nghiệp vụ (ORCA) | Bản đầu tiên từ SRS LG: 30 đối tượng, 50 quan hệ — `docs/_shared/object-map.md` |
| Điều tra trước brainstorm | 4 báo cáo trong `docs/_research/` (cảnh báo hạn container, biên bản giao nhận điện tử, tích hợp ePort, đọc chứng từ hiện trường) |
| Brainstorm mảng điều phối | Đang phỏng vấn |
| Design system + quy tắc giao diện chung | Có trong `design/` |
| Feature có SRS riêng | Chưa có |

Việc đang mở và việc kế tiếp: `_workspace/backlog.md`. Lịch sử thay đổi: `_workspace/changelog.md`.

## Cấu trúc thư mục

| Thư mục | Chứa gì |
|---|---|
| `docs-input/` | Tài liệu khách gửi (SOP, SRS cũ, chứng từ mẫu, tài liệu tích hợp), đã chuyển sang `.md`. Sổ nguồn ở `docs-input/README.md` |
| `docs/_shared/` | Tài liệu dùng chung toàn dự án: project profile, glossary, bản đồ đối tượng, tổng quan hệ thống |
| `docs/_research/` | Báo cáo điều tra ý tưởng trước khi cam kết làm |
| `docs/{feature}/` | Mỗi feature một thư mục: URD/BRD/PRD, SRS, use case, user flow, wireframe, user story |
| `design/` | Design system (`design.md`, token CSS, component) và quy tắc giao diện chung (`ui-common/`) |
| `_workspace/` | Backlog, changelog, Knowledge Graph của repo |
| `_guides/` | Hướng dẫn quy trình làm tài liệu (`pipeline.md`) |
| `_templates/` | Khung tài liệu mà các lệnh dùng |
| `.claude/` | Lệnh, rule và agent review cho Claude Code |

## Cách làm việc

Tài liệu được sinh và cập nhật qua các lệnh `/…` trong Claude Code. Mọi lệnh đều trình kế hoạch và diff để duyệt trước khi ghi file. Thứ tự thường dùng:

```
/intake          tài liệu khách gửi → docs-input/
/object-map      bản đồ đối tượng nghiệp vụ
/discover        điều tra 1 ý tưởng còn phân vân
/brainstorm      đào sâu 1 feature
/srs             đặc tả yêu cầu, rồi use case, ERD, flow
/user-flow       luồng màn hình, trước khi vẽ wireframe
/wireframe-ascii, /wireframe-html, /figma-screen
/userstory, /ac  backlog giao dev
```

Danh sách lệnh đầy đủ và quy ước (đặt tên, frontmatter, trạng thái tài liệu) ở `CLAUDE.md`. Quy trình chi tiết ở `_guides/pipeline.md`.

## Quy ước chính

- Viết tiếng Việt, dùng từ nghiệp vụ thay cho thuật ngữ kỹ thuật.
- Tên file kebab-case không dấu. Mã yêu cầu có tiền tố feature (`FR-{feature}-001`), mã đối tượng dạng `OBJ-{slug}`.
- Trạng thái tài liệu: `draft → in-review → revisions → approved → shipped`.
- Ý tưởng ghi rõ nguồn gốc: `[SOP to-be]` (khách đã thiết kế), `[SOP+]` (đào sâu hơn SOP), `[Mới]`.
- Chỗ chưa có nguồn thì ghi thành câu hỏi mở (OQ), không tự suy rồi coi là đã chốt.
