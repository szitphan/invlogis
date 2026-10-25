# qa/db/queries — truy vấn kiểm dữ liệu (chỉ đọc)

Quy ước:
- DB là SQL Server, schema theo tenant. Mọi truy vấn phải nêu rõ schema (không giả định `dbo`).
- Chỉ `SELECT`. Cấm INSERT/UPDATE/DELETE/DDL; dữ liệu tiền đề dựng qua API (hook "dựng dữ liệu test") chứ không ghi thẳng DB.
- Chỉ chạy trên DEV/SIT, kết nối qua biến `QA_DB_CONNECTION` ở `qa/.env`. Không bao giờ trỏ prod.
- Tên file: `<feature>-<mục-đích>.sql`; đầu file ghi tham số (`-- @param`) và CHK/FR phục vụ.
- Không để dữ liệu cá nhân thật trong kết quả lưu lại.

Chưa có truy vấn nào; thêm khi test cần đối chiếu số liệu.
