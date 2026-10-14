# Sổ đối chiếu: SRS cũ LG (lg-export) (SRC-22)

> Nguồn: `srs-cu/lg-srs-export.md`
> Bản: không ghi ngày bản (nhận 2026-10-01)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| [v2.0] Quy tắc chung xử lý giao diện trên website (Website common rules & shared components) | ➖ |  | tr. 10 · trùng tài liệu Quy tắc giao diện chung web (SRC-20), đối chiếu ở sổ của tài liệu đó |
| UC00.00.01 - Lưu nháp bản ghi tạo mới | ➡ common-workspace |  | tr. 41 |
| UC00.00.02 - Xem thanh tiến trình và chuyển tiếp nghiệp vụ | ✅ | `docs/cross-process-flow/brainstorms/cross-process-flow.md` Mục 2, 5.2 | tr. 46 |
| UC00.00.03 - Tạo mới nghiệp vụ tiếp theo từ thông tin nghiệp vụ trước | ✅ | `docs/cross-process-flow/brainstorms/cross-process-flow.md` Mục 4, 5.3 | tr. 57 |
| UC00.00.04 - Export chi tiết tất cả các feature | ➡ common-workspace |  | tr. 71 |
| Export detail feature - Module Cây dầu | ➡ common-workspace |  | tr. 74 |
| Export detail feature - Module Xưởng | ➡ common-workspace |  | tr. 88 |
| UC00.00.05 - Import | ➡ common-workspace |  | tr. 128 |
| UC00.00.06 - Xem màn hình Home | ➡ common-workspace |  | tr. 139 |
| UC00.00.09 - Export danh sách | ✅ | `docs/cross-process-flow/srs/cross-process-flow-spec.md` FR-cross-process-flow-022 | tr. 144 |
| [not done] UC00.00.10 - Export báo cáo | ➡ common-workspace |  | tr. 146 |
| UC00.00.11 - Bulk actions cho màn danh sách | ➡ common-workspace |  | tr. 150 |
| UC02.03.01 - Thay đổi ngôn ngữ | ➡ account-access |  | tr. 160 |
| Cập nhật danh mục | ➡ common-workspace |  | tr. 163 |
| [not done] Seed dữ liệu khởi đầu | ➡ common-workspace |  | tr. 164 |
| [not done] Cơ cấu tổ chức, phân vùng dữ liệu và quản lý feature theo Chi nhánh/Cơ sở | ➡ organization |  | tr. 197 |
| Format mã quản lý feature và yêu cầu | ➡ common-workspace |  | tr. 202 |
| [not done] Danh mục dùng chung & riêng và quy tắc chia sẻ dữ liệu danh mục | ➡ common-workspace |  | tr. 210 |
| Workflow và validation rules chung của 1 common feature | ➡ common-workspace |  | tr. 212 |
| Phân quyền chức năng và dữ liệu | ➡ access-control |  | tr. 217 |
| Yêu cầu chức năng - Functional Requirements | ➖ |  | tr. 236 · mục lục lặp lại bên trong SRS, không phải yêu cầu |
| Epic 01 - Quản lý tài khoản cá nhân | ➡ account-access |  | tr. 247 |
| UC01.01 - Đăng nhập | ➡ account-access |  | tr. 248 |
| UC01.02 - Quên mật khẩu | ➡ account-access |  | tr. 258 |
| UC01.03 - Đăng xuất | ➡ account-access |  | tr. 267 |
| UC01.04 - Đổi mật khẩu | ➡ account-access |  | tr. 269 |
| UC01.05 - Tạo mật khẩu mới | ➡ account-access |  | tr. 273 |
| UC01.06 - Xem thông tin cá nhân | ➡ account-access |  | tr. 278 |
| Module 1 - Xưởng | ➡ product-catalog |  | tr. 282 |
| Epic 03 - Danh mục | ➡ organization |  | tr. 283 |
| 03 - Lưu đồ trạng thái chung cho danh mục | ➡ organization |  | tr. 284 |
| Feature 03.01 - Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 285 |
| 03.01 - Thông báo & Lịch sử hoạt động | ➡ product-catalog |  | tr. 286 |
| UC03.01.01 - Xem danh mục Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 288 |
| UC03.01.02 - Xem thông tin Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 293 |
| UC03.01.03 - Tạo đề xuất tạo mới Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 298 |
| UC03.01.04 - Huỷ đề xuất cấp mới Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 308 |
| UC03.01.05 - Phê duyệt/Từ chối đề xuất cấp mới Dịch vụ kỹ thuật | ➡ product-catalog |  | tr. 313 |
| Feature 03.03 - Phụ tùng vật tư | ➡ product-catalog |  | tr. 322 |
| 03.03 - Thông báo & Lịch sử hoạt động | ➡ product-catalog |  | tr. 323 |
| UC03.03.01 - Xem danh mục phụ tùng vật tư | ➡ product-catalog |  | tr. 325 |
| UC03.03.02 - Xem thông tin phụ tùng vật tư | ➡ product-catalog |  | tr. 329 |
| UC03.03.03 - Tạo đề xuất tạo mới phụ tùng vật tư | ➡ product-catalog |  | tr. 334 |
| UC03.03.04 - Huỷ đề xuất cấp mới phụ tùng vật tư | ➡ product-catalog |  | tr. 344 |
| UC03.03.05 - Phê duyệt/Từ chối đề xuất cấp mới phụ tùng vật tư | ➡ product-catalog |  | tr. 349 |
| Feature 03.04 - Công cụ dụng cụ | ➡ product-catalog |  | tr. 358 |
| 03.04 - Thông báo & Lịch sử hoạt động | ➡ product-catalog |  | tr. 359 |
| UC03.04.01 - Xem danh mục công cụ dụng cụ | ➡ product-catalog |  | tr. 361 |
| UC03.04.02 - Xem thông tin công cụ dụng cụ | ➡ product-catalog |  | tr. 365 |
| UC03.04.03 - Tạo đề xuất tạo mới công cụ dụng cụ | ➡ product-catalog |  | tr. 370 |
| UC03.04.04 - Huỷ đề xuất cấp mới công cụ dụng cụ | ➡ product-catalog |  | tr. 377 |
| UC03.04.05 - Phê duyệt/Từ chối đề xuất cấp mới công cụ dụng cụ | ➡ product-catalog |  | tr. 382 |
| Feature 03.05 - Lốp | ➡ product-catalog |  | tr. 391 |
| 03.05 - Thông báo & Lịch sử hoạt động | ➡ product-catalog |  | tr. 392 |
| UC03.05.01 - Xem danh mục lốp | ➡ product-catalog |  | tr. 394 |
| UC03.05.02 - Xem thông tin lốp | ➡ product-catalog |  | tr. 399 |
| UC03.05.03 - Tạo đề xuất tạo mới lốp | ➡ product-catalog |  | tr. 404 |
| UC03.05.04 - Huỷ đề xuất cấp mới lốp | ➡ product-catalog |  | tr. 412 |
| UC03.05.05 - Phê duyệt/Từ chối đề xuất cấp mới lốp | ➡ product-catalog |  | tr. 417 |
| Feature 03.06 - Ắc quy | ➡ product-catalog |  | tr. 424 |
| 03.06 - Thông báo & Lịch sử hoạt động | ➡ product-catalog |  | tr. 425 |
| UC03.06.01 - Xem danh mục ắc quy | ➡ product-catalog |  | tr. 427 |
| UC03.06.02 - Xem thông tin ắc quy | ➡ product-catalog |  | tr. 432 |
| UC03.06.03 - Tạo đề xuất tạo mới ắc quy | ➡ product-catalog |  | tr. 437 |
| UC03.06.04 - Huỷ đề xuất cấp mới ắc quy | ➡ product-catalog |  | tr. 444 |
| UC03.06.05 - Phê duyệt/Từ chối đề xuất cấp mới ắc quy | ➡ product-catalog |  | tr. 449 |
| Feature 03.07 - Nhà cung cấp HHDV | ➡ partners |  | tr. 458 |
| 03.07 - Thông báo & Lịch sử hoạt động | ➡ partners |  | tr. 459 |
| UC03.07.01 - Xem danh mục nhà cung cấp HHDV | ➡ partners |  | tr. 461 |
| UC03.07.02 - Xem thông tin nhà cung cấp HHDV | ➡ partners |  | tr. 467 |
| UC03.07.03 - Tạo đề xuất tạo mới nhà cung cấp HHDV | ➡ partners |  | tr. 474 |
| UC03.07.04 - Huỷ đề xuất cấp mới nhà cung cấp HHDV | ➡ partners |  | tr. 488 |
| UC03.07.05 - Phê duyệt/Từ chối đề xuất cấp mới nhà cung cấp HHDV | ➡ partners |  | tr. 493 |
| Feature 03.08 - Khách hàng DK05 | ➡ partners |  | tr. 502 |
| 03.08 - Thông báo & Lịch sử hoạt động | ➡ partners |  | tr. 503 |
| UC03.08.01 - Xem danh mục khách hàng DK05 | ➡ partners |  | tr. 505 |
| UC03.08.02 - Xem thông tin khách hàng DK05 | ➡ partners |  | tr. 510 |
| UC03.08.03 - Tạo đề xuất tạo mới khách hàng DK05 | ➡ partners |  | tr. 517 |
| UC03.08.04 - Huỷ đề xuất cấp mới khách hàng DK05 | ➡ partners |  | tr. 528 |
| UC03.08.05 - Phê duyệt/Từ chối đề xuất cấp mới khách hàng DK05 | ➡ partners |  | tr. 533 |
| Feature 03.09 - Xe của khách hàng | ➡ partners |  | tr. 542 |
| 03.09 - Thông báo & Lịch sử hoạt động | ➡ partners |  | tr. 543 |
| UC03.09.01 - Xem danh mục xe của khách hàng | ➡ partners |  | tr. 545 |
| UC03.09.02 - Xem thông tin xe của khách hàng | ➡ partners |  | tr. 549 |
| UC03.09.03 - Tạo đề xuất tạo mới xe của khách hàng | ➡ partners |  | tr. 554 |
| UC03.09.04 - Huỷ đề xuất cấp mới xe của khách hàng | ➡ partners |  | tr. 565 |
| UC03.09.05 - Phê duyệt/Từ chối đề xuất cấp mới xe của khách hàng | ➡ partners |  | tr. 570 |
| Feature 03.10 - Chi phí cấp 1 | ➡ cost-catalog |  | tr. 578 |
| 03.10 - Thông báo & Lịch sử hoạt động | ➡ cost-catalog |  | tr. 579 |
| UC03.10.01 - Xem danh mục chi phí cấp 1 | ➡ cost-catalog |  | tr. 581 |
| UC03.10.02 - Xem thông tin chi phí cấp 1 | ➡ cost-catalog |  | tr. 585 |
| UC03.10.03 - Tạo đề xuất tạo mới chi phí cấp 1 | ➡ cost-catalog |  | tr. 591 |
| UC03.10.04 - Huỷ đề xuất cấp mới chi phí cấp 1 | ➡ cost-catalog |  | tr. 598 |
| UC03.10.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1 | ➡ cost-catalog |  | tr. 603 |
| Feature 03.11 - Chi phí cấp 2 | ➡ cost-catalog |  | tr. 611 |
| 03.11 - Thông báo & Lịch sử hoạt động | ➡ cost-catalog |  | tr. 612 |
| UC03.11.01 - Xem danh mục chi phí cấp 2 | ➡ cost-catalog |  | tr. 614 |
| UC03.11.02 - Xem thông tin chi phí cấp 2 | ➡ cost-catalog |  | tr. 618 |
| UC03.11.03 - Tạo đề xuất tạo mới chi phí cấp 2 | ➡ cost-catalog |  | tr. 625 |
| UC03.11.04 - Huỷ đề xuất cấp mới chi phí cấp 2 | ➡ cost-catalog |  | tr. 632 |
| UC03.11.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 2 | ➡ cost-catalog |  | tr. 637 |
| Feature 03.12 - Chi phí cấp 3 | ➡ cost-catalog |  | tr. 645 |
| 03.12 - Thông báo & Lịch sử hoạt động | ➡ cost-catalog |  | tr. 646 |
| UC03.12.01 - Xem danh mục chi phí cấp 3 | ➡ cost-catalog |  | tr. 648 |
| UC03.12.02 - Xem thông tin chi phí cấp 3 | ➡ cost-catalog |  | tr. 652 |
| UC03.12.03 - Tạo đề xuất tạo mới chi phí cấp 3 | ➡ cost-catalog |  | tr. 657 |
| UC03.12.04 - Huỷ đề xuất cấp mới chi phí cấp 3 | ➡ cost-catalog |  | tr. 666 |
| UC03.12.05 - Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 3 | ➡ cost-catalog |  | tr. 671 |
| Epic 04 - Quản lý tài sản | ➡ inventory-count |  | tr. 680 |
| Quản lý vòng đời và trạng thái các hàng hoá trong xưởng | ➡ inventory-count |  | tr. 681 |
| Feature 04.02 - Hàng tồn kho | ➡ inventory-count |  | tr. 698 |
| UC04.02.01 - Xem danh sách hàng tồn kho của xưởng | ➡ inventory-count |  | tr. 699 |
| Sub-feature 01 - Kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 706 |
| 04.02 - Thông báo & Lịch sử hoạt động | ➡ inventory-count |  | tr. 707 |
| 04.02 - Lưu đồ trạng thái cho kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 711 |
| UC04.02.01 - Xem lịch sử kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 713 |
| UC04.02.02 - Xem thông tin kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 717 |
| UC04.02.03 - Tạo mới yêu cầu kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 729 |
| UC04.02.04 - Thu hồi yêu cầu kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 741 |
| UC04.02.05 - Phê duyệt/Từ chối yêu cầu kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 745 |
| UC04.02.06 - Ghi nhận kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 752 |
| UC04.02.07 - Thu hồi yêu cầu kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 765 |
| UC04.02.08 - Phê duyệt/Từ chối ghi nhận kiểm kê hàng tồn kho | ➡ inventory-count |  | tr. 770 |
| Feature 04.03 - Hàng tồn xưởng | ➡ inventory-count |  | tr. 778 |
| UC04.03.01 - Xem danh sách hàng tồn xưởng của xưởng | ➡ inventory-count |  | tr. 779 |
| Sub-feature 01 - Kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 787 |
| 04.03 - Thông báo & Lịch sử hoạt động | ➡ inventory-count |  | tr. 788 |
| 04.03 - Lưu đồ trạng thái cho kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 792 |
| UC04.03.01 - Xem lịch sử kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 794 |
| UC04.03.02 - Xem thông tin kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 798 |
| UC04.03.03 - Tạo mới yêu cầu kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 809 |
| UC04.03.04 - Thu hồi yêu cầu kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 822 |
| UC04.03.05 - Phê duyệt/Từ chối yêu cầu kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 825 |
| UC04.03.06 - Ghi nhận kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 832 |
| UC04.03.07 - Thu hồi yêu cầu kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 843 |
| UC04.03.08 - Phê duyệt/Từ chối ghi nhận kiểm kê hàng tồn xưởng | ➡ inventory-count |  | tr. 847 |
| Feature 04.04 - Danh mục rác thải | ➡ inventory-count |  | tr. 853 |
| Sub-feature 01 - Thanh lý rác thải | ➡ inventory-count |  | tr. 854 |
| 04.04 - Thông báo & Lịch sử hoạt động | ➡ inventory-count |  | tr. 855 |
| 04.04 - Lưu đồ trạng thái cho thanh lý rác thải | ➡ inventory-count |  | tr. 857 |
| UC04.04.01 - Xem lịch sử thanh lý rác thải | ➡ inventory-count |  | tr. 858 |
| UC04.04.02 - Xem thông tin thanh lý rác thải | ➡ inventory-count |  | tr. 863 |
| UC04.04.03 - Tạo mới yêu cầu thanh lý rác thải | ➡ inventory-count |  | tr. 869 |
| UC04.04.04 - Thu hồi yêu cầu thanh lý rác thải | ➡ inventory-count |  | tr. 879 |
| UC04.04.05 - Phê duyệt/Từ chối yêu cầu thanh lý rác thải | ➡ inventory-count |  | tr. 883 |
| UC04.04.06 - Ghi nhận thanh toán cho thanh lý rác thải | ➡ inventory-count |  | tr. 890 |
| UC04.04.07 - Xem danh mục rác thải của xưởng | ➡ inventory-count |  | tr. 893 |
| Epic 05 - Nghiệp vụ xưởng | ➡ purchasing |  | tr. 897 |
| Quản lý kinh doanh | ➡ purchasing |  | tr. 898 |
| Feature 05.01 - Mua hàng hoá dịch vụ | ➡ purchasing |  | tr. 899 |
| 05.01 - Thông báo & Lịch sử hoạt động | ➡ purchasing |  | tr. 900 |
| 05.01 - Lưu đồ trạng thái cho đơn mua HHDV | ➡ purchasing |  | tr. 905 |
| UC05.01.01 - Xem lịch sử mua hàng hoá dịch vụ | ➡ purchasing |  | tr. 907 |
| UC05.01.02 - Xem thông tin đơn mua hàng hoá dịch vụ | ➡ purchasing |  | tr. 913 |
| UC05.01.03 - Tạo mới đơn mua HHDV | ➡ purchasing |  | tr. 926 |
| UC05.01.04 - Huỷ tạo mới đơn mua HHDV | ➡ purchasing |  | tr. 961 |
| UC05.01.05 - Phê duyệt/Từ chối tạo mới đơn mua HHDV lần 1 | ➡ purchasing |  | tr. 966 |
| UC05.01.06 - Phê duyệt/Từ chối tạo mới đơn mua HHDV lần 2 | ➡ purchasing |  | tr. 975 |
| Feature 05.02 - Báo giá hàng hoá dịch vụ | ➡ repair-quotation |  | tr. 984 |
| 05.02 - Thông báo & Lịch sử hoạt động | ➡ repair-quotation |  | tr. 985 |
| 05.02 - Lưu đồ trạng thái cho báo giá | ➡ repair-quotation |  | tr. 990 |
| UC05.02.01 - Xem danh sách báo giá | ➡ repair-quotation |  | tr. 992 |
| UC05.02.02 - Xem thông tin báo giá | ➡ repair-quotation |  | tr. 998 |
| UC05.02.03 - Tạo mới báo giá | ➡ repair-quotation |  | tr. 1016 |
| UC05.02.04 - Huỷ tạo mới báo giá | ➡ repair-quotation |  | tr. 1065 |
| UC05.02.05 - Phê duyệt/Từ chối tạo mới báo giá | ➡ repair-quotation |  | tr. 1069 |
| UC05.02.06 - Xác nhận/Từ chối báo giá | ➡ repair-quotation |  | tr. 1078 |
| Quản lý xuất nhập | ➡ repair-quotation |  | tr. 1087 |
| Feature 05.03 - Nhập kho | ➡ stock-movement |  | tr. 1088 |
| 05.03 - Thông báo & Lịch sử hoạt động | ➡ stock-movement |  | tr. 1089 |
| 05.03 - Lưu đồ trạng thái cho nhập kho | ➡ stock-movement |  | tr. 1091 |
| UC05.03.01 - Xem lịch sử nhập kho | ➡ stock-movement |  | tr. 1092 |
| UC05.03.02 - Xem thông tin nhập kho | ➡ stock-movement |  | tr. 1095 |
| UC05.03.03 - Tạo yêu cầu nhập kho | ➡ stock-movement |  | tr. 1101 |
| UC05.03.04 - Huỷ yêu cầu nhập kho | ➡ stock-movement |  | tr. 1125 |
| UC05.03.05 - Phê duyệt/Từ chối yêu cầu nhập kho | ➡ stock-movement |  | tr. 1129 |
| Feature 05.04 - Xuất kho | ➡ stock-movement |  | tr. 1139 |
| 05.04 - Thông báo & Lịch sử hoạt động | ➡ stock-movement |  | tr. 1140 |
| 05.04 - Lưu đồ trạng thái cho phiếu xuất kho | ➡ stock-movement |  | tr. 1143 |
| UC05.04.01 - Xem lịch sử xuất kho | ➡ stock-movement |  | tr. 1144 |
| UC05.04.02 - Xem thông tin phiếu xuất kho | ➡ stock-movement |  | tr. 1149 |
| UC05.04.03 - Tạo mới phiếu xuất kho | ➡ stock-movement |  | tr. 1164 |
| UC05.04.04 - Thu hồi phiếu xuất kho | ➡ stock-movement |  | tr. 1179 |
| UC05.04.05 - Phê duyệt/Từ chối tạo mới phiếu xuất kho lần 1 | ➡ stock-movement |  | tr. 1183 |
| UC05.04.06 - Phê duyệt/Từ chối tạo mới phiếu xuất kho lần 2 | ➡ stock-movement |  | tr. 1191 |
| Quản lý sửa chữa | ➡ stock-movement |  | tr. 1200 |
| Feature 05.06 - Sửa chữa | ➡ repair-order |  | tr. 1201 |
| 05.06 - Thông báo & Lịch sử hoạt động | ➡ repair-order |  | tr. 1202 |
| 05.06 - Lưu đồ trạng thái cho lệnh sửa chữa | ➡ repair-order |  | tr. 1205 |
| UC05.06.01 - Xem lịch sử sửa chữa | ➡ repair-order |  | tr. 1207 |
| UC05.06.02 - Xem thông tin lệnh sửa chữa | ➡ repair-order |  | tr. 1213 |
| UC05.06.03 - Tạo mới lệnh sửa chữa | ➡ repair-order |  | tr. 1264 |
| UC05.06.04 - Chốt/cập nhật chốt lệnh sửa chữa | ➡ repair-order |  | tr. 1294 |
| UC05.06.05 - Chốt/cập nhật chốt lệnh sửa chữa (trường hợp Thay lốp xe Delta) | ➡ repair-order |  | tr. 1321 |
| Feature 05.07 - Báo cáo sự cố | ➡ incident-report |  | tr. 1337 |
| 05.07 - Lưu đồ trạng thái cho báo cáo sự cố | ➡ incident-report |  | tr. 1338 |
| 05.07 - Thông báo & Lịch sử hoạt động | ➡ incident-report |  | tr. 1340 |
| UC05.07.01 - Xem danh sách báo cáo sự cố | ➡ incident-report |  | tr. 1343 |
| UC05.07.02 - Xem thông tin chi tiết báo cáo sự cố | ➡ incident-report |  | tr. 1348 |
| UC05.07.03 - Xác nhận/từ chối báo cáo sự cố của lái xe | ➡ incident-report |  | tr. 1356 |
| Epic 06 - Thanh toán | ➡ workshop-payment |  | tr. 1362 |
| Chi phí | ➡ workshop-payment |  | tr. 1363 |
| Feature 06.01 - Thanh toán trả trước | ➡ workshop-payment |  | tr. 1364 |
| 06.01 - Thông báo & Lịch sử hoạt động | ➡ workshop-payment |  | tr. 1365 |
| 06.01 - Lưu đồ trạng thái cho thanh toán trả trước | ➡ workshop-payment |  | tr. 1369 |
| UC06.01.01 - Xem lịch sử thanh toán trả trước | ➡ workshop-payment |  | tr. 1371 |
| UC06.01.02 - Xem thông tin thanh toán trả trước | ➡ workshop-payment |  | tr. 1376 |
| UC06.01.03 - Tạo mới đề nghị thanh toán trả trước | ➡ workshop-payment |  | tr. 1389 |
| UC06.01.04 - Huỷ tạo mới đề nghị thanh toán trả trước | ➡ workshop-payment |  | tr. 1405 |
| UC06.01.05 - Phê duyệt/Từ chối đề nghị thanh toán trả trước | ➡ workshop-payment |  | tr. 1411 |
| UC06.01.06 - Phê duyệt/Từ chối chi thanh toán trả trước | ➡ workshop-payment |  | tr. 1420 |
| UC06.01.07 - Ghi nhận thanh toán cho thanh toán trả trước | ➡ workshop-payment |  | tr. 1428 |
| Feature 06.02 - Thanh toán trả sau | ➡ workshop-payment |  | tr. 1432 |
| 06.02 - Thông báo & Lịch sử hoạt động | ➡ workshop-payment |  | tr. 1433 |
| 06.02 - Lưu đồ trạng thái cho bảng công nợ | ➡ workshop-payment |  | tr. 1437 |
| UC06.02.01 - Xem danh sách công nợ | ➡ workshop-payment |  | tr. 1440 |
| UC06.02.02 - Xem chi tiết bảng công nợ theo tháng | ➡ workshop-payment |  | tr. 1446 |
| UC06.02.03 - Chốt/cập nhật chốt/chốt tiếp (mới) công nợ theo tháng | ➡ workshop-payment |  | tr. 1447 |
| UC06.02.04 - Ghi nhận thanh toán/Cập nhật ghi nhận thanh toán công nợ theo tháng | ➡ workshop-payment |  | tr. 1465 |
| Bồi thường | ➡ workshop-payment |  | tr. 1474 |
| Feature 06.03 - Bồi thường thiệt hại | ➡ workshop-payment |  | tr. 1475 |
| 06.03 - Thông báo & Lịch sử hoạt động | ➡ workshop-payment |  | tr. 1476 |
| 06.03 - Lưu đồ trạng thái cho đề nghị bồi thường | ➡ workshop-payment |  | tr. 1480 |
| UC06.03.01 - Xem danh sách đề nghị bồi thường | ➡ workshop-payment |  | tr. 1481 |
| UC06.03.02 - Xem thông tin đề nghị bồi thường | ➡ workshop-payment |  | tr. 1486 |
| UC06.03.03 - Tạo mới/Hoàn thiện thông tin đề nghị bồi thường | ➡ workshop-payment |  | tr. 1503 |
| UC06.03.04 - Thu hồi tạo mới/hoàn thiện đề nghị bồi thường | ➡ workshop-payment |  | tr. 1543 |
| UC06.03.05 - Phê duyệt/Từ chối tạo mới/hoàn thiện đề nghị bồi thường | ➡ workshop-payment |  | tr. 1548 |
| Doanh thu | ➡ workshop-payment |  | tr. 1557 |
| Feature 06.04 - Thanh toán bán HHDV | ➡ service-sales-payment |  | tr. 1558 |
| Sub-feature 01 - Thanh toán bán HHDV trả trước | ➡ service-sales-payment |  | tr. 1559 |
| 06.04 - Thông báo & Lịch sử hoạt động | ➡ service-sales-payment |  | tr. 1560 |
| 06.04 - Lưu đồ trạng thái cho thanh toán bán HHDV trả trước | ➡ service-sales-payment |  | tr. 1562 |
| UC06.04.01 - Xem lịch sử thanh toán bán HHDV trả trước | ➡ service-sales-payment |  | tr. 1563 |
| UC06.04.02 - Xem thông tin thanh toán bán HHDV trả trước | ➡ service-sales-payment |  | tr. 1568 |
| UC06.04.03 - Tạo mới/cập nhật đề nghị thanh toán bán HHDV trả trước | ➡ service-sales-payment |  | tr. 1581 |
| Sub-feature 02 - Thanh toán bán HHDV trả sau | ➡ service-sales-payment |  | tr. 1608 |
| 06.04 - Thông báo & Lịch sử hoạt động - Thanh toán trả sau | ➡ service-sales-payment |  | tr. 1609 |
| 06.04 - Lưu đồ trạng thái cho thanh toán trả sau | ➡ service-sales-payment |  | tr. 1610 |
| UC06.04.04 - Xem danh sách công nợ | ➡ service-sales-payment |  | tr. 1611 |
| UC06.04.03 - Cập nhật đề nghị thanh toán bán HHDV trả sau | ➡ service-sales-payment |  | tr. 1617 |
| UC06.04.05 - Xem thông tin thanh toán bán HHDV trả sau | ➡ service-sales-payment |  | tr. 1641 |
| Epic 11 - Dashboards | ➡ workshop-reports |  | tr. 1654 |
| Epic 10 - Báo cáo | ➡ workshop-reports |  | tr. 1655 |
| 10.01 - Lịch sử hoạt động | ➡ workshop-reports |  | tr. 1656 |
| UC10.01.01 - Xem danh sách báo cáo | ➡ workshop-reports |  | tr. 1657 |
| UC10.01.01 - Tạo báo cáo | ➡ workshop-reports |  | tr. 1663 |
| UC10.01.02 - Xem chi tiết báo cáo | ➡ workshop-reports |  | tr. 1678 |
| Module 2 - Cây dầu | ➡ fuel-purchase |  | tr. 1683 |
| Epic 14 - Dashboards | ➡ fuel-stations |  | tr. 1684 |
| UC12.00.01 - Xem dashboards tổng hợp của tất cả cây dầu | ➡ fuel-stations |  | tr. 1685 |
| UC12.00.02 - Xem dashboards riêng từng cây dầu | ➡ fuel-stations |  | tr. 1691 |
| UC12.00.03 - Xem tổng hợp giao dịch dầu | ➡ fuel-stations |  | tr. 1708 |
| Epic 12 - Nghiệp vụ cây dầu | ➡ fuel-purchase |  | tr. 1713 |
| Feature 12.1 - Mua dầu | ➡ fuel-purchase |  | tr. 1714 |
| 12.01 - Lưu đồ trạng thái kế hoạch mua dầu | ➡ fuel-purchase |  | tr. 1715 |
| UC12.01.01 - Xem danh sách kế hoạch mua dầu | ➡ fuel-purchase |  | tr. 1717 |
| UC12.01.02 - Tạo mới kế hoạch mua dầu | ➡ fuel-purchase |  | tr. 1728 |
| UC12.01.03 - Xem chi tiết kế hoạch mua dầu | ➡ fuel-purchase |  | tr. 1739 |
| UC12.01.04 - Phê duyệt kế hoạch mua dầu | ➡ fuel-purchase |  | tr. 1746 |
| 12.01 - Lưu đồ trạng thái đơn mua dầu | ➡ fuel-purchase |  | tr. 1753 |
| UC12.01.07 - Xem danh sách đơn mua dầu (PO) | ➡ fuel-purchase |  | tr. 1754 |
| UC12.01.08 - Xem đơn mua dầu (PO) | ➡ fuel-purchase |  | tr. 1762 |
| Feature 12.2 - Nhập dầu | ➡ fuel-purchase |  | tr. 1770 |
| UC12.02.01 - Xem danh sách phiếu nhập dầu | ➡ fuel-purchase |  | tr. 1771 |
| UC12.02.02 - Xem chi tiết phiếu nhập dầu | ➡ fuel-purchase |  | tr. 1777 |
| UC12.02.03 - Tạo phiếu nhập dầu từ nhà cung cấp | ➡ fuel-purchase |  | tr. 1788 |
| UC12.02.04 - Tạo phiếu nhập dầu từ phương tiện | ➡ fuel-purchase |  | tr. 1802 |
| UC12.02.05 - Phê duyệt phiếu nhập dầu | ➡ fuel-purchase |  | tr. 1808 |
| Feature 12.3 - Cấp dầu | ➡ fuel-issuing |  | tr. 1811 |
| UC12.03.01 - Xem danh sách phiếu cấp dầu | ➡ fuel-issuing |  | tr. 1812 |
| UC12.03.02 - Xem chi tiết & phê duyệt/từ chối phiếu cấp dầu | ➡ fuel-issuing |  | tr. 1820 |
| Epic 15 - Thanh toán | ➡ fuel-payment |  | tr. 1826 |
| Feature 12.05 - Thanh toán trả sau | ➡ fuel-payment |  | tr. 1827 |
| 12.05 - Lưu đồ trạng thái | ➡ fuel-payment |  | tr. 1828 |
| UC12.05.01 - Xem tổng quan thanh toán trả sau | ➡ fuel-payment |  | tr. 1831 |
| UC12.05.02 - Xem chi tiết kỳ chốt công nợ | ➡ fuel-payment |  | tr. 1839 |
| UC12.05.03 - Chốt công nợ | ➡ fuel-payment |  | tr. 1848 |
| UC12.05.04 - Ghi nhận thanh toán | ➡ fuel-payment |  | tr. 1858 |
| Epic 16 - Danh mục | ➡ fuel-stations |  | tr. 1863 |
| Feature 12.4 - Danh mục bổ sung | ➡ fuel-stations |  | tr. 1864 |
| Sub-feature 12.4.2 - Cây dầu mua ngoài | ➡ fuel-stations |  | tr. 1865 |
| 12.04 - Lưu đồ vòng đời trạng thái của cây dầu mua ngoài | ➡ fuel-stations |  | tr. 1866 |
| UC12.04.04 - Xem danh sách cây dầu mua ngoài | ➡ fuel-stations |  | tr. 1868 |
| UC12.04.05 - Xem chi tiết cây dầu mua ngoài | ➡ fuel-stations |  | tr. 1875 |
| UC12.04.06 - Tạo mới cây dầu mua ngoài | ➡ fuel-stations |  | tr. 1884 |
| Module 3 - Administration | ➡ access-control |  | tr. 1892 |
| Feature 13.01 - Quản lý tài khoản | ➡ access-control |  | tr. 1893 |
| 13.01 - Lịch sử hoạt động | ➡ access-control |  | tr. 1894 |
| 13.01 - Lưu đồ trạng thái của tài khoản | ➡ access-control |  | tr. 1895 |
| UC13.01.01 - Xem danh sách tài khoản | ➡ access-control |  | tr. 1896 |
| UC13.01.02 - Tạo tài khoản | ➡ access-control |  | tr. 1900 |
| UC13.01.03 - Xem chi tiết & chỉnh sửa tài khoản | ➡ access-control |  | tr. 1916 |
| Feature 13.02 - Quản lý nhóm quyền | ➡ access-control |  | tr. 1927 |
| UC13.02.01 - Xem danh sách nhóm quyền | ➡ access-control |  | tr. 1928 |
| UC13.02.02 - Tạo mới & chỉnh sửa nhóm quyền | ➡ access-control |  | tr. 1931 |
| Feature 02.02 - Phân quyền tài khoản | ➡ access-control |  | tr. 1942 |
| UC02.02.01 - Thay đổi phân quyền chức năng | ➡ access-control |  | tr. 1944 |
| Module 4 - Nhân sự | ➡ employee-records |  | tr. 1953 |
| Feature 02.01 - Quản trị nhân viên | ➡ employee-records |  | tr. 1954 |
| 02.01 - Lưu đồ trạng thái | ➡ employee-records |  | tr. 1955 |
| 02.01 - Thông báo & Lịch sử hoạt động | ➡ employee-records |  | tr. 1957 |
| UC02.01.01 - Xem danh sách nhân viên | ➡ employee-records |  | tr. 1960 |
| UC02.01.02 - Xem thông tin chi tiết nhân viên | ➡ employee-records |  | tr. 1964 |
| Sub-feature 01 - Cấp mới nhân viên | ➡ employee-records |  | tr. 1970 |
| UC02.01.03 - Tạo đề xuất cấp mới nhân viên | ➡ employee-records |  | tr. 1971 |
| UC02.01.04 - Huỷ đề xuất cấp mới nhân viên | ➡ employee-records |  | tr. 1985 |
| UC02.01.05 - Phê duyệt/từ chối yêu cầu tạo mới nhân viên | ➡ employee-records |  | tr. 1990 |
| Sub-feature 02 - Xin nghỉ nhân viên | ➡ employee-records |  | tr. 1998 |
| UC02.01.06 - Tạo yêu cầu xin nghỉ nhân viên | ➡ employee-records |  | tr. 1999 |
| UC02.01.07 - Huỷ yêu cầu xin nghỉ nhân viên | ➡ employee-records |  | tr. 2003 |
| UC02.01.08 - Phê duyệt/từ chối yêu cầu xin nghỉ nhân viên | ➡ employee-records |  | tr. 2007 |
| Module 5 - Danh mục | ➡ vehicle-management |  | tr. 2013 |
| Feature 04.01 - Phương tiện | ➡ vehicle-management |  | tr. 2014 |
| 04 - Lưu đồ trạng thái cho phương tiện | ➡ vehicle-management |  | tr. 2015 |
| [WIP] 04.01 - Thông báo & Lịch sử hoạt động | ➡ vehicle-management |  | tr. 2016 |
| [v.1.0] UC04.00.01 - Xem danh sách phương tiện Delta | ➡ vehicle-management |  | tr. 2025 |
| [v2.0] UC04.00.01 - Xem danh sách phương tiện | ➡ vehicle-management |  | tr. 2032 |
| [v1.0] UC04.00.02 - Xem thông tin chi tiết phương tiện Delta | ➡ vehicle-management |  | tr. 2039 |
| [v2.0] UC04.00.02 - Xem chi tiết phương tiện | ➡ vehicle-management |  | tr. 2060 |
| UC04.00.03 - Cập nhật thông tin chung phương tiện | ➡ vehicle-management |  | tr. 2097 |
| UC04.00.04 - Cập nhật hàng hóa & thiết bị phương tiện | ➡ vehicle-management |  | tr. 2113 |
| UC04.00.05 - Cập nhật định mức nhiên liệu phương tiện | ➡ vehicle-management |  | tr. 2125 |
| UC04.00.06 - Xem & Phê duyệt yêu cầu cập nhật phương tiện | ➡ vehicle-management |  | tr. 2130 |
| UC04.00.07 - Xem lịch sử thay đổi của phương tiện | ➡ vehicle-management |  | tr. 2139 |
| UC04.01.01 - Xem lịch sử bàn giao/thu hồi phương tiện | ➡ vehicle-management |  | tr. 2146 |
| Sub-feature 01 - Bàn giao phương tiện | ➡ vehicle-management |  | tr. 2153 |
| 04.01 - Lưu đồ trạng thái cho bàn giao phương tiện | ➡ vehicle-management |  | tr. 2154 |
| [v1.0] UC04.01.01 - Xem thông tin bàn giao phương tiện | ➡ vehicle-management |  | tr. 2155 |
| [v2.0] UC04.01.01 - Xem thông tin bàn giao phương tiện | ➡ vehicle-management |  | tr. 2169 |
| [v1.0] UC04.01.02 - Tạo yêu cầu bàn giao phương tiện | ➡ vehicle-management |  | tr. 2183 |
| [v2.0] UC04.01.02 - Tạo yêu cầu bàn giao phương tiện | ➡ vehicle-management |  | tr. 2205 |
| UC04.01.03 - Huỷ đề xuất bàn giao phương tiện | ➡ vehicle-management |  | tr. 2222 |
| UC04.01.04 - Phê duyệt/Từ chối đề xuất bàn giao phương tiện | ➡ vehicle-management |  | tr. 2227 |
| UC04.01.05 - Ký biên bản bàn giao phương tiện | ➡ vehicle-management |  | tr. 2237 |
| Sub-feature 02 - Thu hồi phương tiện | ➡ vehicle-management |  | tr. 2246 |
| 04.01 - Lưu đồ trạng thái cho thu hồi phương tiện | ➡ vehicle-management |  | tr. 2247 |
| [v1.0] UC04.01.06 - Xem thông tin thu hồi phương tiện | ➡ vehicle-management |  | tr. 2248 |
| [v2.0] UC04.01.06 - Xem thông tin thu hồi phương tiện | ➡ vehicle-management |  | tr. 2261 |
| [v1.0] UC04.01.07 - Tạo yêu cầu thu hồi phương tiện | ➡ vehicle-management |  | tr. 2271 |
| [v2.0] UC04.01.07 - Tạo yêu cầu thu hồi phương tiện | ➡ vehicle-management |  | tr. 2291 |
| UC04.01.08 - Huỷ đề xuất thu hồi phương tiện | ➡ vehicle-management |  | tr. 2306 |
| UC04.01.09 - Phê duyệt/Từ chối đề xuất thu hồi phương tiện | ➡ vehicle-management |  | tr. 2311 |
| UC04.01.10 - Ký biên bản thu hồi phương tiện | ➡ vehicle-management |  | tr. 2321 |
| Sub-feature 03 - Định mức nhiên liệu cho PT | ➡ fuel-allowance |  | tr. 2330 |
| 04.01 - Lưu đồ trạng thái cho định mức nhiên liệu PT | ➡ fuel-allowance |  | tr. 2331 |
| UC04.01.11 - Xem lịch sử định mức NL cho phương tiện | ➡ fuel-allowance |  | tr. 2333 |
| UC04.01.12 - Xem thông tin định mức nhiên liệu PT | ➡ fuel-allowance |  | tr. 2338 |
| UC04.01.13 - Tạo yêu cầu định mức nhiên liệu PT | ➡ fuel-allowance |  | tr. 2353 |
| UC04.01.14 - Huỷ đề xuất định mức nhiên liệu PT | ➡ fuel-allowance |  | tr. 2364 |
| UC04.01.15 - Phê duyệt/Từ chối đề xuất định mức nhiên liệu PT | ➡ fuel-allowance |  | tr. 2369 |
| UC04.01.16 - Cập nhật mức tiêu hao nhiên liệu thực tế PT | ➡ fuel-allowance |  | tr. 2378 |
| UC04.01.17 - Huỷ cập nhật mức tiêu hao nhiên liệu PT | ➡ fuel-allowance |  | tr. 2391 |
| UC04.01.18 - Phê duyệt/Từ chối cập nhật mức tiêu hao nhiên liệu PT | ➡ fuel-allowance |  | tr. 2396 |
| UC04.01.19 - Định mức khoán nhiên liệu thực tế PT | ➡ fuel-allowance |  | tr. 2405 |
| UC04.01.20 - Huỷ định mức khoán nhiên liệu PT | ➡ fuel-allowance |  | tr. 2416 |
| UC04.01.21 - Phê duyệt/Từ chối định mức khoán nhiên liệu PT | ➡ fuel-allowance |  | tr. 2421 |
| Feature 03.02 - Xưởng | ➡ organization |  | tr. 2430 |
| 03.02 - Thông báo & Lịch sử hoạt động | ➡ organization |  | tr. 2431 |
| UC03.02.01 - Xem danh mục Xưởng | ➡ organization |  | tr. 2433 |
| UC03.02.02 - Xem thông tin xưởng | ➡ organization |  | tr. 2437 |
| UC03.02.03 - Tạo đề xuất tạo mới xưởng | ➡ organization |  | tr. 2441 |
| UC03.02.04 - Huỷ đề xuất cấp mới xưởng | ➡ organization |  | tr. 2447 |
| UC03.02.05 - Phê duyệt/Từ chối đề xuất cấp mới xưởng | ➡ organization |  | tr. 2451 |
| Sub-feature 12.4.1 - Cây dầu nội bộ | ➡ fuel-stations |  | tr. 2458 |
| 12.04 - Lưu đồ vòng đời trạng thái của cây dầu nội bộ | ➡ fuel-stations |  | tr. 2459 |
| UC12.04.01 - Xem danh sách cây dầu nội bộ | ➡ fuel-stations |  | tr. 2461 |
| UC12.04.02 - Xem chi tiết cây dầu nội bộ | ➡ fuel-stations |  | tr. 2480 |
| UC12.04.03 - Tạo mới cây dầu nội bộ | ➡ fuel-stations |  | tr. 2491 |
| Barem Và Sensor iGAS — Error Code Contract Cho FE | ➡ fuel-issuing |  | tr. 2505 |
| Module 6 - Quản trị hệ thống | ➡ reminders |  | tr. 2516 |
| Epic 08 - Lịch nhắc | ➡ reminders |  | tr. 2517 |
| 08.04 - Thông báo & Lịch sử hoạt động | ➡ reminders |  | tr. 2518 |
| 08.04 - Lưu đồ trạng thái cho lịch nhắc | ➡ reminders |  | tr. 2520 |
| UC08.04.01 - Xem danh sách lịch nhắc | ➡ reminders |  | tr. 2521 |
| UC08.04.02 - Xem thông tin lịch nhắc | ➡ reminders |  | tr. 2545 |
| UC08.04.03 - Tạo mới/cập nhật lịch nhắc | ➡ reminders |  | tr. 2552 |
| UC08.04.04 - Thu hồi yêu cầu lịch nhắc | ➡ reminders |  | tr. 2567 |
| UC08.04.05 - Phê duyệt/Từ chối yêu cầu lịch nhắc | ➡ reminders |  | tr. 2571 |
| UC08.04.06 - Xem lịch nhắc của từng phương tiện (old version) | ➡ reminders |  | tr. 2578 |
| UC08.04.07 - Xem email nhắc lịch cho tất cả phương tiện | ➡ reminders |  | tr. 2583 |
| Epic 09 - Trợ giúp | ➡ help-center |  | tr. 2586 |
| Feature 09.01 - Câu hỏi thường gặp (FAQs) | ➡ help-center |  | tr. 2587 |
| UC09.01.01 - Xem danh sách và chi tiết câu hỏi thường gặp | ➡ help-center |  | tr. 2588 |
| UC09.01.02 - Tạo/cập nhật câu hỏi thường gặp | ➡ help-center |  | tr. 2591 |
| UC09.01.03 - Xóa câu hỏi thường gặp | ➡ help-center |  | tr. 2595 |
| Feature 09.02 - Hướng dẫn sử dụng | ➡ help-center |  | tr. 2597 |
| UC09.02.01 - Xem danh sách hướng dẫn sử dụng | ➡ help-center |  | tr. 2598 |
| UC09.02.02 - Tạo/cập nhật hướng dẫn sử dụng | ➡ help-center |  | tr. 2601 |
| UC09.02.03 - Xóa hướng dẫn sử dụng | ➡ help-center |  | tr. 2605 |
| UC09.02.04 - Xem chi tiết hướng dẫn sử dụng | ➡ help-center |  | tr. 2607 |
| Yêu cầu phi chức năng - Non-Functional Requirements | ➡ common-workspace |  | tr. 2609 |
