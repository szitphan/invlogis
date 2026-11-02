---
type: design-foundations
feature: ds-v2
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/foundations/icon.md
  - design-system/tokens.json
---

# Foundations · Misc icons (DEC-331, DEC-332, DEC-335)

Mã trạng thái `misc-icon`, duyệt riêng với `icon`. Bộ icon phụ ngoài Lucide; luật dùng icon chung ở [icon.md](icon.md).
Trên Figma: trang `DS · Foundations`, hàng Misc icons.

## Featured icon

Khối nhấn mạnh quanh một icon Lucide (DEC-258, DEC-329 ic10, ic11). Luật khi nào dùng: [icon.md](icon.md) mục 3.1.

| Token | Khối | Icon | Dùng cho |
|---|---|---|---|
| `featured-icon/size-compact` | 36 | 20 | Upload Compact |
| `featured-icon/size-md` | 40 | 20 | Upload Full web |
| `featured-icon/size` | 48 | 24 | Màn trống, màn kết quả, đầu dialog, ô bấm tải lên app |
| `featured-icon/size-xl` | 56 | 28 | Cỡ lớn theo Untitled, cho màn trống cần nổi hơn |

Cỡ Featured giữ nguyên trên web và app, không theo `icon/size/*`, và không còn mượn `control/height/*`. Thang `size/*` không có 36 và 56 nên hai token này là số trần có ghi lý do.

| Kiểu | Hình | Nền | Icon | Dùng cho |
|---|---|---|---|---|
| `light` | Tròn `radius/full` | Xám `color/bg/secondary`; Brand `color/accent/bg`; `color/bg/{success,warning,error}/secondary` | `color/fg/secondary`; Brand và trạng thái theo sắc | Báo kết quả có màu: màn kết quả, đầu hộp thoại. Vùng dữ liệu rỗng không dùng kiểu này, xem mục Mẫu nền và minh hoạ |
| `modern` | Vuông `radius/inner` 8 | Không nền, viền `color/border/primary` | `color/fg/secondary` | Ô tải lên trung tính |
| `modern-subtle` | Vuông `radius/inner` 8 | `color/bg/secondary`, không viền | `color/fg/secondary` | Vùng dữ liệu rỗng (DEC-335 ms17); như `modern`, đặt trên nền trắng cần khối rõ hơn. Tên đề xuất |
| `dark` | Vuông `radius/inner` 8 | Xám `color/bg/secondary_solid`; Brand `color/brand/800`; `color/bg/{success,warning,error}/solid` | `color/fg/white` | Kết quả quan trọng; dùng ít, trên màn điều vận dày dữ liệu nền đặc dễ gây chú ý quá mức |

Tương phản đo từ `tokens.json` (Sáng · Tối, ngưỡng đồ hoạ 3:1):

| Kiểu, sắc | Sáng | Tối |
|---|---|---|
| `light` xám | 9,93:1 | 10,6:1 |
| `light` Brand (8 dải màu khách) | 6,12–8,70:1 | 7,47–9,75:1 |
| `light` thành công | 3,32:1 | 4,54:1 |
| `light` cảnh báo | 3,63:1 | 4,62:1 |
| `light` lỗi | 3,69:1 | 4,45:1 |
| `modern` trên nền trang | 10,37:1 | 11,86:1 |
| `modern-subtle` | 9,93:1 | 10,6:1 |
| `dark` xám | 7,81:1 | 7,81:1 |
| `dark` Brand (8 dải màu khách) | 9,77–15,13:1 | 9,77–15,13:1 |
| `dark` thành công | 5,72:1 | 5,72:1 |
| `dark` cảnh báo | 6,33:1 | 6,33:1 |
| `dark` lỗi | 6,57:1 | 6,57:1 |

`dark` có 5 sắc. Xám không dùng `color/bg/primary_solid` vì với `color/fg/white` ở Tối chỉ 1,26:1; Brand không dùng `color/accent/solid` vì ở Tối chỉ 1,78–1,90:1.

Figma: set `Featured icon` (`6657:163375`) trên trang Base, 48 biến thể, trục Type × Color × Size; Upload dùng instance của set này. Spec riêng trong `design-system/components/` chưa viết.

## File type icon

Tờ giấy gập góc + nhãn đuôi tệp (DEC-335 ms01). Dùng ở dòng tệp không có ảnh nhỏ: danh sách chứng từ, ô tải tệp ([Field Upload](../components/application/field-upload.md)). Ngoài trời đọc được chữ đuôi, không phải đoán hình như icon Lucide `file-text`.

Figma: `File type icon` `6657:165918`, 8 loại × 2 cỡ, gắn `color/file-type/*`.

| Loại | Dùng cho | Nền nhãn | Mã | Chữ trắng trên nền |
|---|---|---|---|---|
| PDF | Tệp PDF | `color/file-type/pdf` | #B42318 | 6,57:1 |
| DOC | Tệp Word | `color/file-type/doc` | #1F4FB8 | 7,32:1 |
| XLS | Tệp Excel | `color/file-type/xls` | #1B7542 | 5,72:1 |
| CSV | Tệp CSV | `color/file-type/csv` | #1B7542 | 5,72:1 |
| IMG | Ảnh JPG, PNG | `color/file-type/img` | #6A50E4 | 5,41:1 |
| ZIP | Tệp nén | `color/file-type/zip` | #525252 | 7,81:1 |
| VID | Video bằng chứng, vd video cắt chì trong SOP giao nhận | `color/file-type/vid` | #B54708 | 5,43:1 |
| Other | Định dạng ngoài 7 loại trên, vd XML. Không vẽ thêm loại | Không có nhãn | — | — |

- **Màu:** nhãn giữ màu nhận diện loại tệp, Sáng = Tối (DEC-335 ms02). Chữ nhãn `color/fg/white`. Tờ giấy nền `color/bg/primary`, nét `color/border/primary`, đổi theo chế độ. Màu nhãn không mang nghĩa trạng thái: nhãn PDF đỏ không phải lỗi.
- **Cỡ:** một bộ cho web và app: `size/4xl` 32, `size/5xl` 40 (DEC-335 ms04). Đồ hoạ, không phải vùng chạm, nên không theo `control/height/*`. Không thêm token.
- Icon không tự bấm được; vùng bấm thuộc dòng tệp chứa nó.

## Check icon

**Bỏ** (DEC-335 ms15). Danh sách điều kiện dùng icon Lucide: `circle-check` khi đã đạt, `circle` khi chưa đạt ([icon.md](icon.md)). Đã gỡ bộ cũ khỏi Figma.

## Payment method icon

**Bỏ tên bộ này, gộp còn một bộ** (DEC-335 ms12): 56 logo Untitled ở `design-system/icons/payment/` + NAPAS, VietQR, tổng 58 logo. `_Card brand` của Payment input dùng bộ này.

- **Loại:** thẻ, cổng thanh toán, ví. **Cỡ:** khung 34 × 24. **Màu:** nguyên màu thương hiệu, không gắn token.
- **Khi nào dùng:** nhận diện đúng dịch vụ thanh toán đó. Nghĩa thanh toán trong nghiệp vụ dùng icon Lucide ở [icon.md](icon.md) mục 7.
- **NAPAS, VietQR:** Figma làm nguồn, lấy từ bộ cũ `Payment method icon` (NAPAS ảnh PNG chính thức napas.com.vn; VietQR SVG Wikimedia Commons). Repo chưa có tệp, không tự vẽ lại.

## Flag

25 nước × 2 hình (tròn, chữ nhật) × 3 cỡ 16, 20, 24 = 150 biến thể (DEC-335 ms07). Figma: `Flag` `6706:1532`. Màu nguyên bản của cờ, không gắn token.

**Dùng ở** (DEC-335 ms06):

- **Ngôn ngữ:** hàng Ngôn ngữ của [Header navigation](../components/application/header-navigation.md), cờ đi cùng tên ngôn ngữ, không đứng một mình. `P-ngon-ngu-giao-dien` có Tiếng Việt (cờ VN), Tiếng Anh (cờ US, user chốt 02/11, DEC-335).
- **Quốc gia:** tuyến qua nước khác, Tag Flag.
- **Không có** bộ chọn mã vùng: số điện thoại theo đầu số 0 hoặc 84.

## Bank logo

Danh mục dùng chung, tầng `[Lõi]`, không theo khách (DEC-335 ms13). 69 ngân hàng theo danh sách VietQR, sắp theo mức phổ biến, × 3 cỡ 24, 32, 40. Figma: `Bank logo` `6704:101952`; BIN ghi trong mô tả biến thể. Logo nguyên màu thương hiệu, không gắn token; ô chứa logo dùng `color/logo/bg`, trắng ở cả Sáng và Tối để logo không chìm trên nền Tối (DEC-338).

**Khi nào dùng:** cỡ 24 trong danh sách chọn ngân hàng (lệnh chi trả hộ, ngân hàng của nhà cung cấp); luôn đi cùng tên ngân hàng. Spec component chưa dùng.

## App logo

Logo các app Invlogis có thể kết nối (nhắn tin, bản đồ, email, văn phòng, kế toán, thanh toán, vận chuyển), dùng trong màn Kết nối / Tích hợp; hiện chưa có tài liệu nghiệp vụ nào mô tả màn này. Figma: `App logo` `6709:1020`, 15 ô × 3 cỡ 24, 32, 40 (DEC-335 ms14). Nguyên màu thương hiệu; nguồn Simple Icons, Wikimedia theo ghi chú Figma.

10 ô đã có logo. **5 ô trống chờ logo từ đối tác:** MISA, VNPay, MoMo, ZaloPay, GHN; không tự vẽ. Zalo nằm ở bộ này vì bộ Social không có.

## Huy hiệu cửa hàng ứng dụng

App Store, Google Play, cao 40 (`size/5xl`) (DEC-335 ms05). Chỉ dùng ở email kích hoạt tài khoản và trang đăng nhập khi mở trên điện thoại; không đặt trong sản phẩm sau đăng nhập.

- **Hình lấy nguyên bản, không sửa màu, không gắn token:** tài sản của Apple và Google. Nguồn xem thử: `design/_ref/untitled-ui/react/components/base/buttons/app-store-buttons.tsx`, chưa xuất tệp vào `design-system/icons/`.
- **Đường dẫn theo khách:** `P-link-tai-app` trong `docs/_product/tenant-parameters.md`, tầng `[Cấu hình]`, mỗi khách một bản app (DEC-326).

## _Dot

Phần con ẩn cho chấm trạng thái (DEC-335 ms10), không thêm token. Cỡ chuẩn 6 (`size/sm`), màu truyền từ cha. Dùng trong Badge, Tag, `_Avatar status`; Figma `7171:1776`. Map Dot, Map Marker giữ chấm vẽ riêng cỡ 14 và 12, viền trắng 2, vì 8 instance đang ghi đè màu.

| Cha | Cỡ chấm | Phần cha giữ |
|---|---|---|
| Badge, Tag | 6 | Màu theo tông |
| `_Avatar status` | 6–16 theo cỡ Avatar | Viền trắng, chấm rỗng Offline |
| `Map Marker` `Status` | 12 | Chấm vẽ riêng, viền trắng 2, bóng |

Cha cần chấm lớn hơn 6 thì đặt lại cỡ instance theo số trong spec của cha.

## Nút Play trên ảnh nhỏ video

Lớp phủ tròn 32 `size/4xl`, `radius/full`, nền `color/bg/overlay_solid`, icon Lucide `play` nét, `color/fg/white` (DEC-335 ms11). Chỉ đặt trên ảnh nhỏ video trong thư viện ảnh của lệnh, để phân biệt với ảnh chụp. Không tô tam giác: không thuộc danh sách Fill=On của DEC-329.

## Mã QR

Hiện mã: component [QR code](../components/base/qr-code.md), cỡ 96, 128, chỉ cho biên bản giao nhận (DEC-335 ms08). Quét mã: vẫn dùng 3 icon Lucide, không có đồ hoạ riêng. Số container không đi bằng mã vạch.

## Mẫu nền và minh hoạ

- **Mẫu nền:** không dùng background pattern ở bất kỳ đâu, gồm trang lỗi (DEC-335 ms16). Trong thẻ, bảng dày dữ liệu hay ngoài trời, lưới mờ là nhiễu.
- **Vùng dữ liệu rỗng:** Featured icon `modern-subtle` (bản xám: nền `color/bg/secondary`, không viền) + chữ nói vì sao rỗng + hành động tiếp theo (DEC-335 ms17). Mọi icon dùng trong vùng này theo đúng bản đó.
- **Minh hoạ:** `design-system/components/_work/error-page/illos.py` không vào foundation; 4 hình của Untitled không lấy.

## Không lấy từ Untitled (DEC-335 ms18)

| Món | Lý do |
|---|---|
| Emoji, Cursor, Check item text, iPhone mockup, Credit card, Section divider | Phục vụ trang giới thiệu, bảng giá, ảnh mockup; không màn logistics nào cần |
| Folder icon | Lucide `folder` đủ dùng cho hồ sơ chứng từ |
| Rating (ms09) | Không có màn chấm điểm; sao đã mang nghĩa Yêu thích theo DEC-329. Khi có màn đánh giá thì mở lại ở component đó |
| Background pattern (ms16), Illustrations (ms17) | Xem mục Mẫu nền và minh hoạ |

## Bộ phụ: Payment và Social (DEC-329 ic16)

- `design-system/icons/payment/` 56 logo cổng thanh toán, thẻ, ví (khung 34 × 24, nhiều màu). `design-system/icons/social/` 22 logo mạng xã hội (khung 24, `currentColor`). Tên file kebab-case, bỏ đuôi `-icon`.
- Nguồn: Untitled UI React, `design/_ref/untitled-ui/react/components/foundations/payment-icons`, `social-icons`, xuất nguyên path sang SVG; viền ô thẻ `stroke-border-secondary` đổi thành `#E5E5E5` (`color/border/secondary` Sáng). Integration icons không lấy.
- **Giấy phép:** phần code Untitled UI React theo MIT (`design/_ref/untitled-ui/react/LICENSE`, bản chép ở `design-system/icons/LICENSE-untitled-ui.txt`). MIT không cấp quyền thương hiệu: logo vẫn thuộc chủ thương hiệu, chỉ dùng đúng nghĩa nhận diện dịch vụ đó.
- NAPAS, VietQR thuộc bộ thanh toán (mục Payment method icon, DEC-335 ms12). MoMo, VNPay, ZaloPay chờ logo từ đối tác, Zalo ở bộ App logo (mục App logo, DEC-335 ms14). Nghĩa thanh toán trong nghiệp vụ vẫn dùng icon Lucide ở `icon.md` mục 7.
- **Social trên Figma đơn sắc đen** (nguồn `currentColor`): khi đặt instance gắn `color/fg/primary` để không chìm ở Tối, không sửa master (DEC-335 ms14). Tài liệu nghiệp vụ chưa có màn dùng.
