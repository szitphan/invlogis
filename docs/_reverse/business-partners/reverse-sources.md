# Đối tác: nhà cung cấp, khách hàng, xe của khách (`business-partners`) — Danh mục nguồn (provenance)

| Nguồn | Tài liệu | Loại | Ngày | Confidence | Encoding | Phần suy ra từ đây |
|---|---|---|---|---|---|---|
| SRS Web | Tài liệu SRS - ERP Delta 3.0 (Web) — `docs-input/srs-cu/lg-srs-export.md` (ảnh: `docs-input/srs-cu/images/`; bản gốc: ~/Downloads/lg-export.pdf (ngoài git)) | pdf → md | bản 30/9/2026 | high | OK — bảng chuyển từ PDF hay bị cắt ô | Nhà cung cấp HHDV, khách hàng DK05, xe của khách hàng: tr.283–284, tr.458–577 |
| Ghi chép thay đổi | Thay đổi so với SRS v2.0 (LG) — tài liệu nội bộ của đội — `docs/_product/srs-v2-change-log.md` | md | 2026-10-12 | medium | OK | Mục 0.3: CHG-21 (bên xuất hoá đơn có thể khác khách đặt dịch vụ) |

## Ghi chú nguồn

- SRS Web chuyển từ PDF theo bố cục trang: bảng hay bị cắt ô (chữ dồn dòng), `Cột n` là nhãn kỹ thuật. Ảnh trích lại từ PDF gốc ngày 2026-10-14 (lưu đồ hoạt động, lưu đồ trạng thái, mockup màn hình).
- Hai nguồn nói khác nhau cùng 1 điểm → ghi cả hai, nhãn 🟡, Conflict ở `reverse-gaps.md`. Không tự chọn bên.
- Ghi chép thay đổi là tài liệu của đội (không phải tài liệu khách), chỉ dùng để đối chiếu ở Mục 0.3.
