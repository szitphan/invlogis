// GENERATED — không sửa tay. Nguồn: design/v2/ · sinh bởi _scripts/ds-v2-handoff.py
// ignore_for_file: constant_identifier_names, lines_longer_than_80_chars

import 'dart:ui' show lerpDouble;

import 'package:flutter/material.dart';

/// Primitives — giá trị gốc. Màn hình KHÔNG dùng trực tiếp; đi qua [InvColors], [InvSpacing]...
abstract final class InvPrimitives {
  static const Color neutral50 = Color(0xFFFAFAFA);
  static const Color neutral100 = Color(0xFFF5F5F5);
  static const Color neutral200 = Color(0xFFE5E5E5);
  static const Color neutral300 = Color(0xFFD4D4D4);
  static const Color neutral400 = Color(0xFFA3A3A3);
  static const Color neutral500 = Color(0xFF737373);
  static const Color neutral600 = Color(0xFF525252);
  static const Color neutral700 = Color(0xFF404040);
  static const Color neutral800 = Color(0xFF262626);
  static const Color neutral900 = Color(0xFF171717);
  static const Color neutral950 = Color(0xFF0A0A0A);
  static const Color blue50 = Color(0xFFE7EFFD);
  static const Color blue100 = Color(0xFFD3E2FE);
  static const Color blue200 = Color(0xFFB5CFFF);
  static const Color blue300 = Color(0xFF93B9FF);
  static const Color blue400 = Color(0xFF6C9EFE);
  static const Color blue500 = Color(0xFF4982F7);
  static const Color blue600 = Color(0xFF3468D7);
  static const Color blue700 = Color(0xFF1F4FB8);
  static const Color blue800 = Color(0xFF163F98);
  static const Color blue900 = Color(0xFF0D2F7A);
  static const Color blue950 = Color(0xFF051F5C);
  static const Color teal50 = Color(0xFFE2F5F4);
  static const Color teal100 = Color(0xFFC6EDEB);
  static const Color teal200 = Color(0xFFA9DDD9);
  static const Color teal300 = Color(0xFF8AC9C5);
  static const Color teal400 = Color(0xFF67B3AD);
  static const Color teal500 = Color(0xFF449D95);
  static const Color teal600 = Color(0xFF2B847C);
  static const Color teal700 = Color(0xFF0B6B64);
  static const Color teal800 = Color(0xFF015751);
  static const Color teal900 = Color(0xFF01433E);
  static const Color teal950 = Color(0xFF002F2C);
  static const Color purple50 = Color(0xFFEFEAFE);
  static const Color purple100 = Color(0xFFE3DBFE);
  static const Color purple200 = Color(0xFFD0C4FF);
  static const Color purple300 = Color(0xFFB9AAFE);
  static const Color purple400 = Color(0xFF9E8CFE);
  static const Color purple500 = Color(0xFF836BFF);
  static const Color purple600 = Color(0xFF6A50E4);
  static const Color purple700 = Color(0xFF5536C4);
  static const Color purple800 = Color(0xFF4429A3);
  static const Color purple900 = Color(0xFF341C82);
  static const Color purple950 = Color(0xFF250F63);
  static const Color yellow50 = Color(0xFFFFF3DC);
  static const Color yellow100 = Color(0xFFFEE4B6);
  static const Color yellow200 = Color(0xFFF2D099);
  static const Color yellow300 = Color(0xFFE3B87A);
  static const Color yellow400 = Color(0xFFD19D59);
  static const Color yellow500 = Color(0xFFBF8239);
  static const Color yellow600 = Color(0xFFA56A21);
  static const Color yellow700 = Color(0xFF8A5300);
  static const Color yellow800 = Color(0xFF704303);
  static const Color yellow900 = Color(0xFF573301);
  static const Color yellow950 = Color(0xFF3F2300);
  static const Color green50 = Color(0xFFE8F5EC);
  static const Color green100 = Color(0xFFD3EDDB);
  static const Color green200 = Color(0xFFB3E0C1);
  static const Color green300 = Color(0xFF93CFA6);
  static const Color green400 = Color(0xFF6FBB89);
  static const Color green500 = Color(0xFF4CA66D);
  static const Color green600 = Color(0xFF348D57);
  static const Color green700 = Color(0xFF1B7542);
  static const Color green800 = Color(0xFF105F34);
  static const Color green900 = Color(0xFF054A26);
  static const Color green950 = Color(0xFF013519);
  static const Color red50 = Color(0xFFFDECEC);
  static const Color red100 = Color(0xFFFDDBDB);
  static const Color red200 = Color(0xFFFFC1BF);
  static const Color red300 = Color(0xFFFFA19C);
  static const Color red400 = Color(0xFFFC7970);
  static const Color red500 = Color(0xFFF05547);
  static const Color red600 = Color(0xFFD23C2E);
  static const Color red700 = Color(0xFFB42318);
  static const Color red800 = Color(0xFF94170E);
  static const Color red900 = Color(0xFF760B05);
  static const Color red950 = Color(0xFF580100);
  static const Color orange50 = Color(0xFFFFF7ED);
  static const Color orange100 = Color(0xFFFBEAD7);
  static const Color orange200 = Color(0xFFFFD3AB);
  static const Color orange300 = Color(0xFFFFB782);
  static const Color orange400 = Color(0xFFFE9356);
  static const Color orange500 = Color(0xFFF96E34);
  static const Color orange600 = Color(0xFFDE5626);
  static const Color orange700 = Color(0xFFC2410C);
  static const Color orange800 = Color(0xFFA03201);
  static const Color orange900 = Color(0xFF7E2500);
  static const Color orange950 = Color(0xFF5C1901);
  static const Color charcoal800 = Color(0xFF3B3B3B);
  static const Color charcoal900 = Color(0xFF262626);
  static const Color charcoal950 = Color(0xFF171717);
  static const Color white = Color(0xFFFFFFFF);
  static const Color alphaNeutral95050 = Color(0x800A0A0A);
  static const Color alphaShadow6 = Color(0x0F101828);
  static const Color alphaShadow10 = Color(0x1A101828);
  static const Color alphaShadow16 = Color(0x29101828);
  static const Color alphaBlack40 = Color(0x66000000);
  static const Color alphaBlack50 = Color(0x80000000);
  static const Color alphaBlack60 = Color(0x99000000);
  static const double space0 = 0.0;
  static const double space2 = 2.0;
  static const double space4 = 4.0;
  static const double space6 = 6.0;
  static const double space8 = 8.0;
  static const double space12 = 12.0;
  static const double space16 = 16.0;
  static const double space20 = 20.0;
  static const double space24 = 24.0;
  static const double space32 = 32.0;
  static const double space40 = 40.0;
  static const double space48 = 48.0;
  static const double space64 = 64.0;
  static const double space80 = 80.0;
  static const double space96 = 96.0;
  static const double radiusNone = 0.0;
  static const double radiusXxs = 2.0;
  static const double radiusXs = 4.0;
  static const double radiusSm = 6.0;
  static const double radiusMd = 8.0;
  static const double radiusLg = 10.0;
  static const double radiusXl = 12.0;
  static const double radius2xl = 16.0;
  static const double radius3xl = 20.0;
  static const double radius4xl = 24.0;
  static const double radiusFull = 9999.0;
}

/// Semantic — màu theo vai trò, mode Light | Dark. Bản nháp theo quy tắc đảo bậc của Untitled UI (50↔950 … 500 giữ), đã đo và chỉnh: chữ phụ, icon phụ, viền ô nhập → neutral/400; nút chính sáng neutral/50; nền surface 950, canvas 900 (DEC-257). Brand, Context Dark chưa điền.
@immutable
class InvColors extends ThemeExtension<InvColors> {
  const InvColors({
    required this.bgCanvas,
    required this.bgSurface,
    required this.bgMuted,
    required this.bgHover,
    required this.bgSelected,
    required this.bgInverse,
    required this.textPrimary,
    required this.textSecondary,
    required this.textTertiary,
    required this.textInverse,
    required this.iconPrimary,
    required this.iconSecondary,
    required this.borderDefault,
    required this.borderStrong,
    required this.borderInput,
    required this.borderFocus,
    required this.borderDanger,
    required this.actionPrimary,
    required this.actionPrimaryHover,
    required this.actionPrimaryPressed,
    required this.actionSecondary,
    required this.actionSecondaryHover,
    required this.actionDanger,
    required this.actionDangerSubtle,
    required this.statusSuccessText,
    required this.statusSuccessIcon,
    required this.statusSuccessBg,
    required this.statusSuccessBgStrong,
    required this.statusSuccessSolid,
    required this.statusSuccessSolidHover,
    required this.statusSuccessBorder,
    required this.statusSuccessBorderSubtle,
    required this.statusWarningText,
    required this.statusWarningIcon,
    required this.statusWarningBg,
    required this.statusWarningBgStrong,
    required this.statusWarningSolid,
    required this.statusWarningSolidHover,
    required this.statusWarningBorder,
    required this.statusWarningBorderSubtle,
    required this.statusDangerText,
    required this.statusDangerIcon,
    required this.statusDangerBg,
    required this.statusDangerBgStrong,
    required this.statusDangerSolid,
    required this.statusDangerSolidHover,
    required this.statusDangerBorder,
    required this.statusDangerBorderSubtle,
    required this.statusInfoText,
    required this.statusInfoIcon,
    required this.statusInfoBg,
    required this.statusInfoBgStrong,
    required this.statusInfoSolid,
    required this.statusInfoSolidHover,
    required this.statusInfoBorder,
    required this.statusInfoBorderSubtle,
    required this.chipGrayBg,
    required this.chipGrayFg,
    required this.chipBlueBg,
    required this.chipBlueFg,
    required this.chipTealBg,
    required this.chipTealFg,
    required this.chipPurpleBg,
    required this.chipPurpleFg,
    required this.chipYellowBg,
    required this.chipYellowFg,
    required this.chipGreenBg,
    required this.chipGreenFg,
    required this.chipRedBg,
    required this.chipRedFg,
    required this.chipOrangeBg,
    required this.chipOrangeFg,
    required this.overlayScrim,
    required this.shadowSm,
    required this.shadowMd,
    required this.shadowMdSoft,
    required this.shadowLg,
    required this.focusGap,
  });

  /// Không dùng nữa (DEC-258): nền trang trắng như bg/surface; giữ token để không gãy tham chiếu cũ.
  final Color bgCanvas;
  /// Nền trang và nền mọi thẻ, bảng, sheet. Dùng ở: Card, Record Card, Summary Card, List Item.
  final Color bgSurface;
  /// Nền khối phụ trong thẻ, ô nhập app. Dùng ở: khối tóm tắt trong Card, Text Field (app), OTP Field.
  final Color bgMuted;
  /// Nền khi rê chuột lên thứ nền trắng. Dùng ở: dòng bảng, mục menu, List Item (web).
  final Color bgHover;
  /// Nền mục đang chọn khi khách không có màu riêng. Dùng ở: List Item đang chọn, mục menu đang chọn.
  final Color bgSelected;
  /// Nền tối tương phản cao. Dùng ở: Tooltip, toast trung tính.
  final Color bgInverse;
  /// Tiêu đề, giá trị chính. Dùng ở: tiêu đề Card, giá trị trong Record Card, chữ Text Field đã nhập.
  final Color textPrimary;
  /// Chữ phụ: nhãn trường (web = app), mô tả, thời gian. Dùng ở: nhãn Text Field, nhãn dòng Record Card, Status Row.
  final Color textSecondary;
  /// Chữ gợi ý trong ô và chữ tắt; không dùng cho nội dung (2,58:1). Dùng ở: placeholder Text Field, nút Disabled.
  final Color textTertiary;
  /// Chữ trên nền đậm. Dùng ở: chữ nút Primary, chữ Tooltip.
  final Color textInverse;
  /// Icon đi cùng chữ chính. Dùng ở: icon dòng Record Card, icon List Item.
  final Color iconPrimary;
  /// Icon phụ: chevron, icon trong ô. Dùng ở: icon Text Field, chevron List Item.
  final Color iconSecondary;
  /// Viền dùng nhiều nhất: viền thẻ, kẻ bảng, vạch chia. Dùng ở: Card, Record Card, List Item (vạch chia).
  final Color borderDefault;
  /// Viền tách khối đậm hơn mặc định. Dùng ở: viền nút Secondary, chip viền.
  final Color borderStrong;
  /// Viền tương phản cao (≥ 3:1) cho thứ người dùng nhập hoặc chọn. Dùng ở: Text Field, OTP Field, radio Selectable Card.
  final Color borderInput;
  /// Vòng focus 2px và viền ô đang gõ; than chì cho mọi khách (DEC-170). Dùng ở: .focus / Ring, Text Field đang gõ.
  final Color borderFocus;
  /// Viền lỗi. Dùng ở: Text Field lỗi, OTP Field lỗi.
  final Color borderDanger;
  /// Nền hành động chính. Dùng ở: nút Primary, tab chip đang chọn.
  final Color actionPrimary;
  /// Nền nút Primary khi rê chuột.
  final Color actionPrimaryHover;
  /// Nền nút Primary khi bấm.
  final Color actionPrimaryPressed;
  /// Nền hành động phụ và nền xám của trạng thái tắt. Dùng ở: nút Secondary, nút Disabled.
  final Color actionSecondary;
  /// Nền nút Secondary khi rê chuột.
  final Color actionSecondaryHover;
  /// Chữ, icon hành động phá huỷ. Dùng ở: nút Danger (xoá, huỷ lệnh).
  final Color actionDanger;
  /// Nền nhạt của nút Danger.
  final Color actionDangerSubtle;
  /// Thành công · Chữ trạng thái: chữ dưới ô, chữ trong banner.
  final Color statusSuccessText;
  /// Thành công · Icon trạng thái.
  final Color statusSuccessIcon;
  /// Thành công · Nền nhạt: banner, thanh thông báo.
  final Color statusSuccessBg;
  /// Thành công · Nền vòng Featured icon.
  final Color statusSuccessBgStrong;
  /// Thành công · Nền đặc chữ trắng: toast, huy hiệu đếm.
  final Color statusSuccessSolid;
  /// Thành công · Nền đặc khi rê chuột.
  final Color statusSuccessSolidHover;
  /// Thành công · Viền trạng thái.
  final Color statusSuccessBorder;
  /// Thành công · Viền nhạt quanh banner.
  final Color statusSuccessBorderSubtle;
  /// Cảnh báo · Chữ trạng thái: chữ dưới ô, chữ trong banner.
  final Color statusWarningText;
  /// Cảnh báo · Icon trạng thái.
  final Color statusWarningIcon;
  /// Cảnh báo · Nền nhạt: banner, thanh thông báo.
  final Color statusWarningBg;
  /// Cảnh báo · Nền vòng Featured icon.
  final Color statusWarningBgStrong;
  /// Cảnh báo · Nền đặc chữ trắng: toast, huy hiệu đếm.
  final Color statusWarningSolid;
  /// Cảnh báo · Nền đặc khi rê chuột.
  final Color statusWarningSolidHover;
  /// Cảnh báo · Viền trạng thái.
  final Color statusWarningBorder;
  /// Cảnh báo · Viền nhạt quanh banner.
  final Color statusWarningBorderSubtle;
  /// Lỗi · Chữ trạng thái: chữ dưới ô, chữ trong banner.
  final Color statusDangerText;
  /// Lỗi · Icon trạng thái.
  final Color statusDangerIcon;
  /// Lỗi · Nền nhạt: banner, thanh thông báo.
  final Color statusDangerBg;
  /// Lỗi · Nền vòng Featured icon.
  final Color statusDangerBgStrong;
  /// Lỗi · Nền đặc chữ trắng: toast, huy hiệu đếm.
  final Color statusDangerSolid;
  /// Lỗi · Nền đặc khi rê chuột.
  final Color statusDangerSolidHover;
  /// Lỗi · Viền trạng thái.
  final Color statusDangerBorder;
  /// Lỗi · Viền nhạt quanh banner.
  final Color statusDangerBorderSubtle;
  /// Thông tin · Chữ trạng thái: chữ dưới ô, chữ trong banner.
  final Color statusInfoText;
  /// Thông tin · Icon trạng thái.
  final Color statusInfoIcon;
  /// Thông tin · Nền nhạt: banner, thanh thông báo.
  final Color statusInfoBg;
  /// Thông tin · Nền vòng Featured icon.
  final Color statusInfoBgStrong;
  /// Thông tin · Nền đặc chữ trắng: toast, huy hiệu đếm.
  final Color statusInfoSolid;
  /// Thông tin · Nền đặc khi rê chuột.
  final Color statusInfoSolidHover;
  /// Thông tin · Viền trạng thái.
  final Color statusInfoBorder;
  /// Thông tin · Viền nhạt quanh banner.
  final Color statusInfoBorderSubtle;
  /// Chip trạng thái gray: nền. Dùng ở: Status Chip, Status Row.
  final Color chipGrayBg;
  /// Chip trạng thái gray: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipGrayFg;
  /// Chip trạng thái blue: nền. Dùng ở: Status Chip, Status Row.
  final Color chipBlueBg;
  /// Chip trạng thái blue: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipBlueFg;
  /// Chip trạng thái teal: nền. Dùng ở: Status Chip, Status Row.
  final Color chipTealBg;
  /// Chip trạng thái teal: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipTealFg;
  /// Chip trạng thái purple: nền. Dùng ở: Status Chip, Status Row.
  final Color chipPurpleBg;
  /// Chip trạng thái purple: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipPurpleFg;
  /// Chip trạng thái yellow: nền. Dùng ở: Status Chip, Status Row.
  final Color chipYellowBg;
  /// Chip trạng thái yellow: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipYellowFg;
  /// Chip trạng thái green: nền. Dùng ở: Status Chip, Status Row.
  final Color chipGreenBg;
  /// Chip trạng thái green: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipGreenFg;
  /// Chip trạng thái red: nền. Dùng ở: Status Chip, Status Row.
  final Color chipRedBg;
  /// Chip trạng thái red: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipRedFg;
  /// Chip trạng thái orange: nền. Dùng ở: Status Chip, Status Row.
  final Color chipOrangeBg;
  /// Chip trạng thái orange: chữ, icon. Dùng ở: Status Chip, Status Row.
  final Color chipOrangeFg;
  /// Lớp phủ sau dialog, sheet.
  final Color overlayScrim;
  /// Màu bóng, đổi theo sáng/tối. Dùng trong: elev/1.
  final Color shadowSm;
  /// Màu bóng, đổi theo sáng/tối. Dùng trong: elev/2 lớp 1, elev/3 lớp 2.
  final Color shadowMd;
  /// Màu bóng, đổi theo sáng/tối. Dùng trong: elev/2 lớp 2.
  final Color shadowMdSoft;
  /// Màu bóng, đổi theo sáng/tối. Dùng trong: elev/3 lớp 1.
  final Color shadowLg;
  /// Khe 2px giữa control và vòng focus, trùng nền trang (DEC-258, thay collection Context). Dùng ở: .focus / Ring, ruột nút Ghost, Outline.
  final Color focusGap;

  static const light = InvColors(
    bgCanvas: InvPrimitives.white,
    bgSurface: InvPrimitives.white,
    bgMuted: InvPrimitives.neutral100,
    bgHover: InvPrimitives.neutral50,
    bgSelected: InvPrimitives.neutral100,
    bgInverse: InvPrimitives.neutral900,
    textPrimary: InvPrimitives.neutral900,
    textSecondary: InvPrimitives.neutral500,
    textTertiary: InvPrimitives.neutral400,
    textInverse: InvPrimitives.white,
    iconPrimary: InvPrimitives.neutral700,
    iconSecondary: InvPrimitives.neutral500,
    borderDefault: InvPrimitives.neutral200,
    borderStrong: InvPrimitives.neutral300,
    borderInput: InvPrimitives.neutral500,
    borderFocus: InvPrimitives.charcoal900,
    borderDanger: InvPrimitives.red700,
    actionPrimary: InvPrimitives.charcoal900,
    actionPrimaryHover: InvPrimitives.charcoal800,
    actionPrimaryPressed: InvPrimitives.charcoal950,
    actionSecondary: InvPrimitives.neutral100,
    actionSecondaryHover: InvPrimitives.neutral200,
    actionDanger: InvPrimitives.red700,
    actionDangerSubtle: InvPrimitives.red50,
    statusSuccessText: InvPrimitives.green700,
    statusSuccessIcon: InvPrimitives.green600,
    statusSuccessBg: InvPrimitives.green50,
    statusSuccessBgStrong: InvPrimitives.green100,
    statusSuccessSolid: InvPrimitives.green700,
    statusSuccessSolidHover: InvPrimitives.green800,
    statusSuccessBorder: InvPrimitives.green700,
    statusSuccessBorderSubtle: InvPrimitives.green300,
    statusWarningText: InvPrimitives.yellow700,
    statusWarningIcon: InvPrimitives.yellow600,
    statusWarningBg: InvPrimitives.yellow50,
    statusWarningBgStrong: InvPrimitives.yellow100,
    statusWarningSolid: InvPrimitives.yellow700,
    statusWarningSolidHover: InvPrimitives.yellow800,
    statusWarningBorder: InvPrimitives.yellow700,
    statusWarningBorderSubtle: InvPrimitives.yellow300,
    statusDangerText: InvPrimitives.red700,
    statusDangerIcon: InvPrimitives.red600,
    statusDangerBg: InvPrimitives.red50,
    statusDangerBgStrong: InvPrimitives.red100,
    statusDangerSolid: InvPrimitives.red700,
    statusDangerSolidHover: InvPrimitives.red800,
    statusDangerBorder: InvPrimitives.red700,
    statusDangerBorderSubtle: InvPrimitives.red300,
    statusInfoText: InvPrimitives.blue700,
    statusInfoIcon: InvPrimitives.blue600,
    statusInfoBg: InvPrimitives.blue50,
    statusInfoBgStrong: InvPrimitives.blue100,
    statusInfoSolid: InvPrimitives.blue700,
    statusInfoSolidHover: InvPrimitives.blue800,
    statusInfoBorder: InvPrimitives.blue700,
    statusInfoBorderSubtle: InvPrimitives.blue300,
    chipGrayBg: InvPrimitives.neutral100,
    chipGrayFg: InvPrimitives.neutral600,
    chipBlueBg: InvPrimitives.blue50,
    chipBlueFg: InvPrimitives.blue700,
    chipTealBg: InvPrimitives.teal50,
    chipTealFg: InvPrimitives.teal700,
    chipPurpleBg: InvPrimitives.purple50,
    chipPurpleFg: InvPrimitives.purple700,
    chipYellowBg: InvPrimitives.yellow50,
    chipYellowFg: InvPrimitives.yellow700,
    chipGreenBg: InvPrimitives.green50,
    chipGreenFg: InvPrimitives.green700,
    chipRedBg: InvPrimitives.red50,
    chipRedFg: InvPrimitives.red700,
    chipOrangeBg: InvPrimitives.orange50,
    chipOrangeFg: InvPrimitives.orange700,
    overlayScrim: InvPrimitives.alphaNeutral95050,
    shadowSm: InvPrimitives.alphaShadow6,
    shadowMd: InvPrimitives.alphaShadow10,
    shadowMdSoft: InvPrimitives.alphaShadow6,
    shadowLg: InvPrimitives.alphaShadow16,
    focusGap: InvPrimitives.white,
  );

  static const dark = InvColors(
    bgCanvas: InvPrimitives.neutral950,
    bgSurface: InvPrimitives.neutral950,
    bgMuted: InvPrimitives.neutral900,
    bgHover: InvPrimitives.neutral900,
    bgSelected: InvPrimitives.neutral800,
    bgInverse: InvPrimitives.neutral100,
    textPrimary: InvPrimitives.neutral100,
    textSecondary: InvPrimitives.neutral400,
    textTertiary: InvPrimitives.neutral600,
    textInverse: InvPrimitives.neutral950,
    iconPrimary: InvPrimitives.neutral300,
    iconSecondary: InvPrimitives.neutral400,
    borderDefault: InvPrimitives.neutral800,
    borderStrong: InvPrimitives.neutral700,
    borderInput: InvPrimitives.neutral400,
    borderFocus: InvPrimitives.neutral50,
    borderDanger: InvPrimitives.red300,
    actionPrimary: InvPrimitives.neutral50,
    actionPrimaryHover: InvPrimitives.neutral200,
    actionPrimaryPressed: InvPrimitives.neutral300,
    actionSecondary: InvPrimitives.neutral800,
    actionSecondaryHover: InvPrimitives.neutral700,
    actionDanger: InvPrimitives.red300,
    actionDangerSubtle: InvPrimitives.red950,
    statusSuccessText: InvPrimitives.green300,
    statusSuccessIcon: InvPrimitives.green400,
    statusSuccessBg: InvPrimitives.green950,
    statusSuccessBgStrong: InvPrimitives.green900,
    statusSuccessSolid: InvPrimitives.green700,
    statusSuccessSolidHover: InvPrimitives.green600,
    statusSuccessBorder: InvPrimitives.green300,
    statusSuccessBorderSubtle: InvPrimitives.green700,
    statusWarningText: InvPrimitives.yellow300,
    statusWarningIcon: InvPrimitives.yellow400,
    statusWarningBg: InvPrimitives.yellow950,
    statusWarningBgStrong: InvPrimitives.yellow900,
    statusWarningSolid: InvPrimitives.yellow700,
    statusWarningSolidHover: InvPrimitives.yellow600,
    statusWarningBorder: InvPrimitives.yellow300,
    statusWarningBorderSubtle: InvPrimitives.yellow700,
    statusDangerText: InvPrimitives.red300,
    statusDangerIcon: InvPrimitives.red400,
    statusDangerBg: InvPrimitives.red950,
    statusDangerBgStrong: InvPrimitives.red900,
    statusDangerSolid: InvPrimitives.red700,
    statusDangerSolidHover: InvPrimitives.red600,
    statusDangerBorder: InvPrimitives.red300,
    statusDangerBorderSubtle: InvPrimitives.red700,
    statusInfoText: InvPrimitives.blue300,
    statusInfoIcon: InvPrimitives.blue400,
    statusInfoBg: InvPrimitives.blue950,
    statusInfoBgStrong: InvPrimitives.blue900,
    statusInfoSolid: InvPrimitives.blue700,
    statusInfoSolidHover: InvPrimitives.blue600,
    statusInfoBorder: InvPrimitives.blue300,
    statusInfoBorderSubtle: InvPrimitives.blue700,
    chipGrayBg: InvPrimitives.neutral900,
    chipGrayFg: InvPrimitives.neutral400,
    chipBlueBg: InvPrimitives.blue950,
    chipBlueFg: InvPrimitives.blue300,
    chipTealBg: InvPrimitives.teal950,
    chipTealFg: InvPrimitives.teal300,
    chipPurpleBg: InvPrimitives.purple950,
    chipPurpleFg: InvPrimitives.purple300,
    chipYellowBg: InvPrimitives.yellow950,
    chipYellowFg: InvPrimitives.yellow300,
    chipGreenBg: InvPrimitives.green950,
    chipGreenFg: InvPrimitives.green300,
    chipRedBg: InvPrimitives.red950,
    chipRedFg: InvPrimitives.red300,
    chipOrangeBg: InvPrimitives.orange950,
    chipOrangeFg: InvPrimitives.orange300,
    overlayScrim: InvPrimitives.alphaNeutral95050,
    shadowSm: InvPrimitives.alphaBlack40,
    shadowMd: InvPrimitives.alphaBlack50,
    shadowMdSoft: InvPrimitives.alphaBlack40,
    shadowLg: InvPrimitives.alphaBlack60,
    focusGap: InvPrimitives.neutral950,
  );

  @override
  InvColors copyWith({Color? bgCanvas, Color? bgSurface, Color? bgMuted, Color? bgHover, Color? bgSelected, Color? bgInverse, Color? textPrimary, Color? textSecondary, Color? textTertiary, Color? textInverse, Color? iconPrimary, Color? iconSecondary, Color? borderDefault, Color? borderStrong, Color? borderInput, Color? borderFocus, Color? borderDanger, Color? actionPrimary, Color? actionPrimaryHover, Color? actionPrimaryPressed, Color? actionSecondary, Color? actionSecondaryHover, Color? actionDanger, Color? actionDangerSubtle, Color? statusSuccessText, Color? statusSuccessIcon, Color? statusSuccessBg, Color? statusSuccessBgStrong, Color? statusSuccessSolid, Color? statusSuccessSolidHover, Color? statusSuccessBorder, Color? statusSuccessBorderSubtle, Color? statusWarningText, Color? statusWarningIcon, Color? statusWarningBg, Color? statusWarningBgStrong, Color? statusWarningSolid, Color? statusWarningSolidHover, Color? statusWarningBorder, Color? statusWarningBorderSubtle, Color? statusDangerText, Color? statusDangerIcon, Color? statusDangerBg, Color? statusDangerBgStrong, Color? statusDangerSolid, Color? statusDangerSolidHover, Color? statusDangerBorder, Color? statusDangerBorderSubtle, Color? statusInfoText, Color? statusInfoIcon, Color? statusInfoBg, Color? statusInfoBgStrong, Color? statusInfoSolid, Color? statusInfoSolidHover, Color? statusInfoBorder, Color? statusInfoBorderSubtle, Color? chipGrayBg, Color? chipGrayFg, Color? chipBlueBg, Color? chipBlueFg, Color? chipTealBg, Color? chipTealFg, Color? chipPurpleBg, Color? chipPurpleFg, Color? chipYellowBg, Color? chipYellowFg, Color? chipGreenBg, Color? chipGreenFg, Color? chipRedBg, Color? chipRedFg, Color? chipOrangeBg, Color? chipOrangeFg, Color? overlayScrim, Color? shadowSm, Color? shadowMd, Color? shadowMdSoft, Color? shadowLg, Color? focusGap}) =>
      InvColors(bgCanvas: bgCanvas ?? this.bgCanvas, bgSurface: bgSurface ?? this.bgSurface, bgMuted: bgMuted ?? this.bgMuted, bgHover: bgHover ?? this.bgHover, bgSelected: bgSelected ?? this.bgSelected, bgInverse: bgInverse ?? this.bgInverse, textPrimary: textPrimary ?? this.textPrimary, textSecondary: textSecondary ?? this.textSecondary, textTertiary: textTertiary ?? this.textTertiary, textInverse: textInverse ?? this.textInverse, iconPrimary: iconPrimary ?? this.iconPrimary, iconSecondary: iconSecondary ?? this.iconSecondary, borderDefault: borderDefault ?? this.borderDefault, borderStrong: borderStrong ?? this.borderStrong, borderInput: borderInput ?? this.borderInput, borderFocus: borderFocus ?? this.borderFocus, borderDanger: borderDanger ?? this.borderDanger, actionPrimary: actionPrimary ?? this.actionPrimary, actionPrimaryHover: actionPrimaryHover ?? this.actionPrimaryHover, actionPrimaryPressed: actionPrimaryPressed ?? this.actionPrimaryPressed, actionSecondary: actionSecondary ?? this.actionSecondary, actionSecondaryHover: actionSecondaryHover ?? this.actionSecondaryHover, actionDanger: actionDanger ?? this.actionDanger, actionDangerSubtle: actionDangerSubtle ?? this.actionDangerSubtle, statusSuccessText: statusSuccessText ?? this.statusSuccessText, statusSuccessIcon: statusSuccessIcon ?? this.statusSuccessIcon, statusSuccessBg: statusSuccessBg ?? this.statusSuccessBg, statusSuccessBgStrong: statusSuccessBgStrong ?? this.statusSuccessBgStrong, statusSuccessSolid: statusSuccessSolid ?? this.statusSuccessSolid, statusSuccessSolidHover: statusSuccessSolidHover ?? this.statusSuccessSolidHover, statusSuccessBorder: statusSuccessBorder ?? this.statusSuccessBorder, statusSuccessBorderSubtle: statusSuccessBorderSubtle ?? this.statusSuccessBorderSubtle, statusWarningText: statusWarningText ?? this.statusWarningText, statusWarningIcon: statusWarningIcon ?? this.statusWarningIcon, statusWarningBg: statusWarningBg ?? this.statusWarningBg, statusWarningBgStrong: statusWarningBgStrong ?? this.statusWarningBgStrong, statusWarningSolid: statusWarningSolid ?? this.statusWarningSolid, statusWarningSolidHover: statusWarningSolidHover ?? this.statusWarningSolidHover, statusWarningBorder: statusWarningBorder ?? this.statusWarningBorder, statusWarningBorderSubtle: statusWarningBorderSubtle ?? this.statusWarningBorderSubtle, statusDangerText: statusDangerText ?? this.statusDangerText, statusDangerIcon: statusDangerIcon ?? this.statusDangerIcon, statusDangerBg: statusDangerBg ?? this.statusDangerBg, statusDangerBgStrong: statusDangerBgStrong ?? this.statusDangerBgStrong, statusDangerSolid: statusDangerSolid ?? this.statusDangerSolid, statusDangerSolidHover: statusDangerSolidHover ?? this.statusDangerSolidHover, statusDangerBorder: statusDangerBorder ?? this.statusDangerBorder, statusDangerBorderSubtle: statusDangerBorderSubtle ?? this.statusDangerBorderSubtle, statusInfoText: statusInfoText ?? this.statusInfoText, statusInfoIcon: statusInfoIcon ?? this.statusInfoIcon, statusInfoBg: statusInfoBg ?? this.statusInfoBg, statusInfoBgStrong: statusInfoBgStrong ?? this.statusInfoBgStrong, statusInfoSolid: statusInfoSolid ?? this.statusInfoSolid, statusInfoSolidHover: statusInfoSolidHover ?? this.statusInfoSolidHover, statusInfoBorder: statusInfoBorder ?? this.statusInfoBorder, statusInfoBorderSubtle: statusInfoBorderSubtle ?? this.statusInfoBorderSubtle, chipGrayBg: chipGrayBg ?? this.chipGrayBg, chipGrayFg: chipGrayFg ?? this.chipGrayFg, chipBlueBg: chipBlueBg ?? this.chipBlueBg, chipBlueFg: chipBlueFg ?? this.chipBlueFg, chipTealBg: chipTealBg ?? this.chipTealBg, chipTealFg: chipTealFg ?? this.chipTealFg, chipPurpleBg: chipPurpleBg ?? this.chipPurpleBg, chipPurpleFg: chipPurpleFg ?? this.chipPurpleFg, chipYellowBg: chipYellowBg ?? this.chipYellowBg, chipYellowFg: chipYellowFg ?? this.chipYellowFg, chipGreenBg: chipGreenBg ?? this.chipGreenBg, chipGreenFg: chipGreenFg ?? this.chipGreenFg, chipRedBg: chipRedBg ?? this.chipRedBg, chipRedFg: chipRedFg ?? this.chipRedFg, chipOrangeBg: chipOrangeBg ?? this.chipOrangeBg, chipOrangeFg: chipOrangeFg ?? this.chipOrangeFg, overlayScrim: overlayScrim ?? this.overlayScrim, shadowSm: shadowSm ?? this.shadowSm, shadowMd: shadowMd ?? this.shadowMd, shadowMdSoft: shadowMdSoft ?? this.shadowMdSoft, shadowLg: shadowLg ?? this.shadowLg, focusGap: focusGap ?? this.focusGap);

  @override
  InvColors lerp(covariant ThemeExtension<InvColors>? other, double t) {
    if (other is! InvColors) return this;
    return InvColors(bgCanvas: Color.lerp(bgCanvas, other.bgCanvas, t)!, bgSurface: Color.lerp(bgSurface, other.bgSurface, t)!, bgMuted: Color.lerp(bgMuted, other.bgMuted, t)!, bgHover: Color.lerp(bgHover, other.bgHover, t)!, bgSelected: Color.lerp(bgSelected, other.bgSelected, t)!, bgInverse: Color.lerp(bgInverse, other.bgInverse, t)!, textPrimary: Color.lerp(textPrimary, other.textPrimary, t)!, textSecondary: Color.lerp(textSecondary, other.textSecondary, t)!, textTertiary: Color.lerp(textTertiary, other.textTertiary, t)!, textInverse: Color.lerp(textInverse, other.textInverse, t)!, iconPrimary: Color.lerp(iconPrimary, other.iconPrimary, t)!, iconSecondary: Color.lerp(iconSecondary, other.iconSecondary, t)!, borderDefault: Color.lerp(borderDefault, other.borderDefault, t)!, borderStrong: Color.lerp(borderStrong, other.borderStrong, t)!, borderInput: Color.lerp(borderInput, other.borderInput, t)!, borderFocus: Color.lerp(borderFocus, other.borderFocus, t)!, borderDanger: Color.lerp(borderDanger, other.borderDanger, t)!, actionPrimary: Color.lerp(actionPrimary, other.actionPrimary, t)!, actionPrimaryHover: Color.lerp(actionPrimaryHover, other.actionPrimaryHover, t)!, actionPrimaryPressed: Color.lerp(actionPrimaryPressed, other.actionPrimaryPressed, t)!, actionSecondary: Color.lerp(actionSecondary, other.actionSecondary, t)!, actionSecondaryHover: Color.lerp(actionSecondaryHover, other.actionSecondaryHover, t)!, actionDanger: Color.lerp(actionDanger, other.actionDanger, t)!, actionDangerSubtle: Color.lerp(actionDangerSubtle, other.actionDangerSubtle, t)!, statusSuccessText: Color.lerp(statusSuccessText, other.statusSuccessText, t)!, statusSuccessIcon: Color.lerp(statusSuccessIcon, other.statusSuccessIcon, t)!, statusSuccessBg: Color.lerp(statusSuccessBg, other.statusSuccessBg, t)!, statusSuccessBgStrong: Color.lerp(statusSuccessBgStrong, other.statusSuccessBgStrong, t)!, statusSuccessSolid: Color.lerp(statusSuccessSolid, other.statusSuccessSolid, t)!, statusSuccessSolidHover: Color.lerp(statusSuccessSolidHover, other.statusSuccessSolidHover, t)!, statusSuccessBorder: Color.lerp(statusSuccessBorder, other.statusSuccessBorder, t)!, statusSuccessBorderSubtle: Color.lerp(statusSuccessBorderSubtle, other.statusSuccessBorderSubtle, t)!, statusWarningText: Color.lerp(statusWarningText, other.statusWarningText, t)!, statusWarningIcon: Color.lerp(statusWarningIcon, other.statusWarningIcon, t)!, statusWarningBg: Color.lerp(statusWarningBg, other.statusWarningBg, t)!, statusWarningBgStrong: Color.lerp(statusWarningBgStrong, other.statusWarningBgStrong, t)!, statusWarningSolid: Color.lerp(statusWarningSolid, other.statusWarningSolid, t)!, statusWarningSolidHover: Color.lerp(statusWarningSolidHover, other.statusWarningSolidHover, t)!, statusWarningBorder: Color.lerp(statusWarningBorder, other.statusWarningBorder, t)!, statusWarningBorderSubtle: Color.lerp(statusWarningBorderSubtle, other.statusWarningBorderSubtle, t)!, statusDangerText: Color.lerp(statusDangerText, other.statusDangerText, t)!, statusDangerIcon: Color.lerp(statusDangerIcon, other.statusDangerIcon, t)!, statusDangerBg: Color.lerp(statusDangerBg, other.statusDangerBg, t)!, statusDangerBgStrong: Color.lerp(statusDangerBgStrong, other.statusDangerBgStrong, t)!, statusDangerSolid: Color.lerp(statusDangerSolid, other.statusDangerSolid, t)!, statusDangerSolidHover: Color.lerp(statusDangerSolidHover, other.statusDangerSolidHover, t)!, statusDangerBorder: Color.lerp(statusDangerBorder, other.statusDangerBorder, t)!, statusDangerBorderSubtle: Color.lerp(statusDangerBorderSubtle, other.statusDangerBorderSubtle, t)!, statusInfoText: Color.lerp(statusInfoText, other.statusInfoText, t)!, statusInfoIcon: Color.lerp(statusInfoIcon, other.statusInfoIcon, t)!, statusInfoBg: Color.lerp(statusInfoBg, other.statusInfoBg, t)!, statusInfoBgStrong: Color.lerp(statusInfoBgStrong, other.statusInfoBgStrong, t)!, statusInfoSolid: Color.lerp(statusInfoSolid, other.statusInfoSolid, t)!, statusInfoSolidHover: Color.lerp(statusInfoSolidHover, other.statusInfoSolidHover, t)!, statusInfoBorder: Color.lerp(statusInfoBorder, other.statusInfoBorder, t)!, statusInfoBorderSubtle: Color.lerp(statusInfoBorderSubtle, other.statusInfoBorderSubtle, t)!, chipGrayBg: Color.lerp(chipGrayBg, other.chipGrayBg, t)!, chipGrayFg: Color.lerp(chipGrayFg, other.chipGrayFg, t)!, chipBlueBg: Color.lerp(chipBlueBg, other.chipBlueBg, t)!, chipBlueFg: Color.lerp(chipBlueFg, other.chipBlueFg, t)!, chipTealBg: Color.lerp(chipTealBg, other.chipTealBg, t)!, chipTealFg: Color.lerp(chipTealFg, other.chipTealFg, t)!, chipPurpleBg: Color.lerp(chipPurpleBg, other.chipPurpleBg, t)!, chipPurpleFg: Color.lerp(chipPurpleFg, other.chipPurpleFg, t)!, chipYellowBg: Color.lerp(chipYellowBg, other.chipYellowBg, t)!, chipYellowFg: Color.lerp(chipYellowFg, other.chipYellowFg, t)!, chipGreenBg: Color.lerp(chipGreenBg, other.chipGreenBg, t)!, chipGreenFg: Color.lerp(chipGreenFg, other.chipGreenFg, t)!, chipRedBg: Color.lerp(chipRedBg, other.chipRedBg, t)!, chipRedFg: Color.lerp(chipRedFg, other.chipRedFg, t)!, chipOrangeBg: Color.lerp(chipOrangeBg, other.chipOrangeBg, t)!, chipOrangeFg: Color.lerp(chipOrangeFg, other.chipOrangeFg, t)!, overlayScrim: Color.lerp(overlayScrim, other.overlayScrim, t)!, shadowSm: Color.lerp(shadowSm, other.shadowSm, t)!, shadowMd: Color.lerp(shadowMd, other.shadowMd, t)!, shadowMdSoft: Color.lerp(shadowMdSoft, other.shadowMdSoft, t)!, shadowLg: Color.lerp(shadowLg, other.shadowLg, t)!, focusGap: Color.lerp(focusGap, other.focusGap, t)!);
  }
}

/// Brand — dải màu theo khách (tenant). Chọn theo slug khách: InvBrandColors.all[slug].
@immutable
class InvBrandColors extends ThemeExtension<InvBrandColors> {
  const InvBrandColors({
    required this.brand50,
    required this.brand100,
    required this.brand200,
    required this.brand300,
    required this.brand400,
    required this.brand500,
    required this.brand600,
    required this.brand700,
    required this.brand800,
    required this.brand900,
    required this.brand950,
  });

  /// Nền dòng bảng đang chọn
  final Color brand50;
  /// Nền mục menu đang chọn, nền avatar
  final Color brand100;
  /// Chưa có vai; ẩn khỏi bảng chọn biến
  final Color brand200;
  /// Chưa có vai; ẩn khỏi bảng chọn biến
  final Color brand300;
  /// Chưa có vai; ẩn khỏi bảng chọn biến
  final Color brand400;
  /// Chưa có vai; ẩn khỏi bảng chọn biến
  final Color brand500;
  /// Chưa có vai; ẩn khỏi bảng chọn biến
  final Color brand600;
  /// Chữ liên kết, mã chứng từ
  final Color brand700;
  /// Công tắc bật, ô chọn, radio và viền chỗ đang chọn, gạch tab đang chọn, thanh tiến độ
  final Color brand800;
  /// Rê chuột trên phần mang màu khách
  final Color brand900;
  /// Đang bấm phần mang màu khách
  final Color brand950;

  /// Than chì (mặc định)
  static const thanChi = InvBrandColors(
    brand50: Color(0xFFF5F5F5),
    brand100: Color(0xFFEBEBEB),
    brand200: Color(0xFFD9D9D9),
    brand300: Color(0xFFBFBFBF),
    brand400: Color(0xFF999999),
    brand500: Color(0xFF737373),
    brand600: Color(0xFF575757),
    brand700: Color(0xFF404040),
    brand800: Color(0xFF262626),
    brand900: Color(0xFF171717),
    brand950: Color(0xFF0A0A0A),
  );

  /// Xanh lá (154° (Delta #1B7B46))
  static const xanhLa = InvBrandColors(
    brand50: Color(0xFFF0F8F2),
    brand100: Color(0xFFDFF1E3),
    brand200: Color(0xFFC2E3CB),
    brand300: Color(0xFF98CFA8),
    brand400: Color(0xFF64B47F),
    brand500: Color(0xFF239857),
    brand600: Color(0xFF027C42),
    brand700: Color(0xFF026535),
    brand800: Color(0xFF004F28),
    brand900: Color(0xFF00381B),
    brand950: Color(0xFF00220E),
  );

  /// Xanh ngọc (190°)
  static const xanhNgoc = InvBrandColors(
    brand50: Color(0xFFEDF9F7),
    brand100: Color(0xFFD9F1EF),
    brand200: Color(0xFFB6E4E0),
    brand300: Color(0xFF81D0CA),
    brand400: Color(0xFF2DB6AF),
    brand500: Color(0xFF0A938E),
    brand600: Color(0xFF047773),
    brand700: Color(0xFF03615D),
    brand800: Color(0xFF024C49),
    brand900: Color(0xFF003634),
    brand950: Color(0xFF00201F),
  );

  /// Xanh dương (255°)
  static const xanhDuong = InvBrandColors(
    brand50: Color(0xFFF0F6FE),
    brand100: Color(0xFFE0ECFD),
    brand200: Color(0xFFC4DBF9),
    brand300: Color(0xFF9EC2F1),
    brand400: Color(0xFF6FA3E5),
    brand500: Color(0xFF4081D2),
    brand600: Color(0xFF1D67BB),
    brand700: Color(0xFF0A529F),
    brand800: Color(0xFF003F80),
    brand900: Color(0xFF002C5E),
    brand950: Color(0xFF001A3D),
  );

  /// Chàm (272°)
  static const cham = InvBrandColors(
    brand50: Color(0xFFF3F5FE),
    brand100: Color(0xFFE5EBFD),
    brand200: Color(0xFFCED8FA),
    brand300: Color(0xFFADBDF2),
    brand400: Color(0xFF889BE6),
    brand500: Color(0xFF6478D3),
    brand600: Color(0xFF4B5DBC),
    brand700: Color(0xFF3B4AA0),
    brand800: Color(0xFF2C3882),
    brand900: Color(0xFF1D2661),
    brand950: Color(0xFF0E1442),
  );

  /// Tím (300°)
  static const tim = InvBrandColors(
    brand50: Color(0xFFF7F4FD),
    brand100: Color(0xFFEDE8FB),
    brand200: Color(0xFFDED3F5),
    brand300: Color(0xFFC7B4EB),
    brand400: Color(0xFFAB90DB),
    brand500: Color(0xFF8E6AC7),
    brand600: Color(0xFF764EAF),
    brand700: Color(0xFF613C94),
    brand800: Color(0xFF4C2C78),
    brand900: Color(0xFF371D59),
    brand950: Color(0xFF220C3C),
  );

  /// Đỏ đô (18°)
  static const doDo = InvBrandColors(
    brand50: Color(0xFFFEF3F3),
    brand100: Color(0xFFFCE5E5),
    brand200: Color(0xFFF7CDCD),
    brand300: Color(0xFFEEABAC),
    brand400: Color(0xFFDD8285),
    brand500: Color(0xFFC65860),
    brand600: Color(0xFFAD3946),
    brand700: Color(0xFF912835),
    brand800: Color(0xFF751A27),
    brand900: Color(0xFF560D19),
    brand950: Color(0xFF3A010A),
  );

  /// Cam đất (45°)
  static const camDat = InvBrandColors(
    brand50: Color(0xFFFDF3EF),
    brand100: Color(0xFFFBE6DD),
    brand200: Color(0xFFF5D0C0),
    brand300: Color(0xFFEBB096),
    brand400: Color(0xFFDA8964),
    brand500: Color(0xFFC26030),
    brand600: Color(0xFFA94400),
    brand700: Color(0xFF8A3600),
    brand800: Color(0xFF6D2900),
    brand900: Color(0xFF501B00),
    brand950: Color(0xFF330D00),
  );

  static const all = <String, InvBrandColors>{
    'than-chi': thanChi,
    'xanh-la': xanhLa,
    'xanh-ngoc': xanhNgoc,
    'xanh-duong': xanhDuong,
    'cham': cham,
    'tim': tim,
    'do-do': doDo,
    'cam-dat': camDat,
  };

  @override
  InvBrandColors copyWith({Color? brand50, Color? brand100, Color? brand200, Color? brand300, Color? brand400, Color? brand500, Color? brand600, Color? brand700, Color? brand800, Color? brand900, Color? brand950}) =>
      InvBrandColors(brand50: brand50 ?? this.brand50, brand100: brand100 ?? this.brand100, brand200: brand200 ?? this.brand200, brand300: brand300 ?? this.brand300, brand400: brand400 ?? this.brand400, brand500: brand500 ?? this.brand500, brand600: brand600 ?? this.brand600, brand700: brand700 ?? this.brand700, brand800: brand800 ?? this.brand800, brand900: brand900 ?? this.brand900, brand950: brand950 ?? this.brand950);

  @override
  InvBrandColors lerp(covariant ThemeExtension<InvBrandColors>? other, double t) {
    if (other is! InvBrandColors) return this;
    return InvBrandColors(brand50: Color.lerp(brand50, other.brand50, t)!, brand100: Color.lerp(brand100, other.brand100, t)!, brand200: Color.lerp(brand200, other.brand200, t)!, brand300: Color.lerp(brand300, other.brand300, t)!, brand400: Color.lerp(brand400, other.brand400, t)!, brand500: Color.lerp(brand500, other.brand500, t)!, brand600: Color.lerp(brand600, other.brand600, t)!, brand700: Color.lerp(brand700, other.brand700, t)!, brand800: Color.lerp(brand800, other.brand800, t)!, brand900: Color.lerp(brand900, other.brand900, t)!, brand950: Color.lerp(brand950, other.brand950, t)!);
  }
}

/// Component — màu theo phần của component (DEC-174).
@immutable
class InvComponentColors extends ThemeExtension<InvComponentColors> {
  const InvComponentColors({
    required this.buttonBgPrimary,
    required this.buttonBgPrimaryHover,
    required this.buttonBgPrimaryPressed,
    required this.buttonFgPrimary,
    required this.buttonBgSecondary,
    required this.buttonBgSecondaryHover,
    required this.buttonBgSecondaryPressed,
    required this.buttonFgSecondary,
    required this.buttonBgGhostHover,
    required this.buttonBgGhostPressed,
    required this.buttonFgGhost,
    required this.buttonBgDanger,
    required this.buttonBgDangerHover,
    required this.buttonBgDangerPressed,
    required this.buttonFgDanger,
    required this.buttonBgOutlineHover,
    required this.buttonBgOutlinePressed,
    required this.buttonFgOutline,
    required this.buttonBorderOutline,
    required this.buttonBorderOutlineDisabled,
    required this.buttonBgDisabled,
    required this.buttonFgDisabled,
    required this.buttonFocusDanger,
    required this.avatarBg,
    required this.avatarFg,
    required this.avatarStatusOnline,
    required this.avatarStatusBusy,
    required this.avatarStatusAway,
    required this.avatarStatusOffline,
    required this.avatarUploadBorder,
    required this.avatarUploadFg,
    required this.avatarScrim,
    required this.avatarEditBg,
    required this.avatarEditFg,
    required this.avatarOverflowBg,
    required this.avatarOverflowFg,
    required this.tooltipBg,
    required this.tooltipFg,
    required this.listRowBgHover,
    required this.listRowBgPressed,
    required this.listRowBgSelected,
    required this.listRowFgDisabled,
    required this.listRowFgSecondaryPressed,
    required this.listRowDivider,
    required this.listRowCheckFg,
    required this.cardBgDefault,
    required this.cardBgHover,
    required this.cardBgPressed,
    required this.cardBorderDefault,
    required this.cardBorderPressed,
    required this.cardBorderSelected,
    required this.cardBorderDashed,
    required this.cardRelatedBg,
    required this.cardLeadBg,
    required this.cardFgSecondaryPressed,
    required this.cardFgSecondaryHover,
    required this.cardDisabledBg,
    required this.cardDisabledFg,
    required this.cardDisabledLeadBg,
    required this.cardCheckBg,
    required this.cardCheckFg,
    required this.cardCheckBorder,
    required this.cardRadioBorder,
    required this.cardRadioOn,
    required this.cardChoiceBg,
    required this.cardChoiceBgHover,
    required this.cardChoiceBgPressed,
    required this.fieldBgWeb,
    required this.fieldBgApp,
    required this.fieldBgHover,
    required this.fieldBgDisabled,
    required this.fieldBgReadonly,
    required this.fieldBorderDefault,
    required this.fieldBorderActive,
    required this.fieldBorderError,
    required this.fieldBorderDisabled,
    required this.fieldFgValue,
    required this.fieldFgPlaceholder,
    required this.fieldFgLabelWeb,
    required this.fieldFgLabelApp,
    required this.fieldFgHelper,
    required this.fieldFgError,
    required this.fieldFgDisabled,
    required this.fieldFgIcon,
    required this.progressBgTrack,
    required this.progressFillBrand,
    required this.progressFillSuccess,
    required this.progressFillInfo,
    required this.progressFillWarning,
    required this.progressFillDanger,
    required this.progressFillNeutral,
  });

  /// Nền nút primary (DEC-174, DEC-176)
  final Color buttonBgPrimary;
  /// Nền nút primary khi rê chuột (web)
  final Color buttonBgPrimaryHover;
  /// Nền nút primary khi bấm
  final Color buttonBgPrimaryPressed;
  /// Chữ, icon, vòng quay của nút primary
  final Color buttonFgPrimary;
  /// Nền nút secondary (DEC-174, DEC-176)
  final Color buttonBgSecondary;
  /// Nền nút secondary khi rê chuột (web)
  final Color buttonBgSecondaryHover;
  /// Nền nút secondary khi bấm
  final Color buttonBgSecondaryPressed;
  /// Chữ, icon, vòng quay của nút secondary
  final Color buttonFgSecondary;
  /// Nền nút ghost khi rê chuột (web)
  final Color buttonBgGhostHover;
  /// Nền nút ghost khi bấm
  final Color buttonBgGhostPressed;
  /// Chữ, icon, vòng quay của nút ghost
  final Color buttonFgGhost;
  /// Nền nút danger (DEC-174, DEC-176)
  final Color buttonBgDanger;
  /// Nền nút danger khi rê chuột (web)
  final Color buttonBgDangerHover;
  /// Nền nút danger khi bấm
  final Color buttonBgDangerPressed;
  /// Chữ, icon, vòng quay của nút danger
  final Color buttonFgDanger;
  /// Nền nút outline khi rê chuột (web): neutral/300, 1,34:1 so với Default trên nền xám (DEC-240, thay phần Hover của DEC-210 cho Outline)
  final Color buttonBgOutlineHover;
  /// Nền nút outline khi bấm: neutral/400 (DEC-240)
  final Color buttonBgOutlinePressed;
  /// Chữ, icon, vòng quay của nút outline
  final Color buttonFgOutline;
  /// Viền nút outline
  final Color buttonBorderOutline;
  /// Viền nút outline lúc Disabled: giữ viền, nền button/bg/disabled; ≥ 1,1:1 trên nền trắng và xám (DEC-240)
  final Color buttonBorderOutlineDisabled;
  /// Nền nút tắt, mọi kiểu (DEC-174)
  final Color buttonBgDisabled;
  /// Chữ, icon nút tắt, mọi kiểu (DEC-174)
  final Color buttonFgDisabled;
  /// Vòng focus nút Danger; kiểu khác dùng color/border/focus (DEC-198)
  final Color buttonFocusDanger;
  /// Nền avatar chữ viết tắt, icon (DEC-201)
  final Color avatarBg;
  /// Chữ viết tắt, icon avatar (DEC-201)
  final Color avatarFg;
  /// Chấm Trực tuyến (DEC-201, DEC-204)
  final Color avatarStatusOnline;
  /// Chấm Đang bận (DEC-204)
  final Color avatarStatusBusy;
  /// Chấm Vắng mặt (DEC-204)
  final Color avatarStatusAway;
  /// Viền chấm rỗng Ngoại tuyến (DEC-204)
  final Color avatarStatusOffline;
  /// Viền đứt ô trống tải ảnh avatar (DEC-201)
  final Color avatarUploadBorder;
  /// Icon ô trống tải ảnh avatar (DEC-201)
  final Color avatarUploadFg;
  /// Lớp phủ khi đang tải ảnh avatar (DEC-203)
  final Color avatarScrim;
  /// Nền nút đổi ảnh (DEC-203)
  final Color avatarEditBg;
  /// Icon nút đổi ảnh (DEC-203)
  final Color avatarEditFg;
  /// Nền ô "+n" của Avatar Group (DEC-205)
  final Color avatarOverflowBg;
  /// Chữ ô "+n" của Avatar Group (DEC-205)
  final Color avatarOverflowFg;
  /// Nền tooltip và mũi tên (DEC-206)
  final Color tooltipBg;
  /// Chữ tooltip (DEC-206)
  final Color tooltipFg;
  /// Nền dòng khi rê chuột, chỉ web: neutral/100 (1,10:1 so với trắng), đậm hơn color/bg/hover neutral/50 (1,04:1) để thấy được; lệch DEC-210 cho dòng danh sách (DEC-232)
  final Color listRowBgHover;
  /// Nền dòng khi bấm giữ: neutral/200 (DEC-174) (DEC-232)
  final Color listRowBgPressed;
  /// Nền dòng đang chọn, kèm dấu tick cuối dòng (DEC-172) (DEC-232)
  final Color listRowBgSelected;
  /// Chữ, icon dòng tắt: xám, không làm mờ (DEC-174) (DEC-232)
  final Color listRowFgDisabled;
  /// Chữ phụ, giá trị khi dòng đang bấm: neutral/600, 6,22:1 trên nền bấm neutral/200; như card/fg/secondary-pressed (DEC-232)
  final Color listRowFgSecondaryPressed;
  /// Đường kẻ dưới dòng (DEC-182) (DEC-232)
  final Color listRowDivider;
  /// Dấu tick cuối dòng đang chọn (DEC-172) (DEC-232)
  final Color listRowCheckFg;
  /// Nền thẻ (DEC-125, DEC-181) (DEC-209)
  final Color cardBgDefault;
  /// Nền thẻ rê chuột, chỉ web: neutral/100, 1,10:1 so với nền trắng (DEC-247, thay phần Hover của DEC-210) (DEC-209)
  final Color cardBgHover;
  /// Nền thẻ đang bấm: neutral/300 (1,47:1 so với nền trắng, 1,34:1 so với khối phụ) (DEC-238, thay DEC-209)
  final Color cardBgPressed;
  /// Viền thẻ, 1,25:1 — thẻ là khối chứa có bóng, không phải control (DEC-125) (DEC-209)
  final Color cardBorderDefault;
  /// Viền thẻ đang bấm: neutral/400; Hover giữ viền thường (DEC-238, DEC-210)
  final Color cardBorderPressed;
  /// Viền thẻ đang chọn, theo dải màu khách (foundations 3.5) (DEC-209)
  final Color cardBorderSelected;
  /// Viền đứt 1px (nét 4/4) của Base / Card Tone=Dashed: thẻ của đối tượng chưa tồn tại hoặc đã huỷ; Hover chỉ đổi nền (DEC-237)
  final Color cardBorderDashed;
  /// Nền khối phụ .card / Related (DEC-194) (DEC-209)
  final Color cardRelatedBg;
  /// Nền vòng icon đầu thẻ, nền ảnh chờ (DEC-164) (DEC-209)
  final Color cardLeadBg;
  /// Chữ phụ và icon phụ khi thẻ đang bấm: neutral/600, 5,27:1 trên nền card/bg/pressed (neutral/500 chỉ 3,68:1) (DEC-238)
  final Color cardFgSecondaryPressed;
  /// Chữ phụ và icon phụ khi thẻ đang rê chuột: neutral/600, đủ 4,5:1 trên card/bg/hover và card/choice/bg-hover (DEC-238)
  final Color cardFgSecondaryHover;
  /// Nền thẻ tắt, một kiểu tắt chung (DEC-174) (DEC-238)
  final Color cardDisabledBg;
  /// Chữ, icon thẻ tắt (DEC-174) (DEC-238)
  final Color cardDisabledFg;
  /// Nền vòng icon và ruột radio của Selectable Card chưa chọn + Disabled: trắng, 1,10:1 so với nền thẻ tắt (DEC-238)
  final Color cardDisabledLeadBg;
  /// Nền tick thẻ đang chọn (brand/800); tick trắng ≥ 9,77:1 ở 8 dải (DEC-209)
  final Color cardCheckBg;
  /// Dấu tick trắng (DEC-209)
  final Color cardCheckFg;
  /// Viền quanh tick (DEC-209) (đổi tên từ card/check/ring, BL-243)
  final Color cardCheckBorder;
  /// Viền radio chưa chọn của Selectable Card (DEC-184, DEC-236)
  final Color cardRadioBorder;
  /// Radio đang chọn: brand/800 (DEC-184, DEC-236)
  final Color cardRadioOn;
  /// Nền thẻ Tone=Muted (Selectable Card chưa chọn), không viền (DEC-184, DEC-234, DEC-236)
  final Color cardChoiceBg;
  /// Nền Muted khi rê chuột (web): nền nghỉ đã xám nên rê chuột đậm hơn một bậc (DEC-236)
  final Color cardChoiceBgHover;
  /// Nền Muted khi bấm: neutral/300, đậm hơn hover một bậc (DEC-174, DEC-236); chữ phụ dùng card/fg/secondary-pressed
  final Color cardChoiceBgPressed;
  /// Ô nhập web: nền ô (DEC-184) (DEC-207)
  final Color fieldBgWeb;
  /// Ô nhập app: nền ô, nhãn nằm trong ô (DEC-184) (DEC-207)
  final Color fieldBgApp;
  /// Ô nhập: nền rê chuột, chỉ web (DEC-210) (DEC-207)
  final Color fieldBgHover;
  /// Ô nhập: nền khi tắt, cùng màu nút tắt — một kiểu xám nhạt (DEC-174) (DEC-207)
  final Color fieldBgDisabled;
  /// Ô nhập: nền chỉ đọc, không viền (DEC-207)
  final Color fieldBgReadonly;
  /// Ô nhập: viền nghỉ 1px (DEC-184) (DEC-207)
  final Color fieldBorderDefault;
  /// Ô nhập: viền đang gõ 2px, than chì mọi khách; cũng là dấu focus (DEC-184, DEC-170) (DEC-207)
  final Color fieldBorderActive;
  /// Ô nhập: viền lỗi 2px (DEC-184) (DEC-207)
  final Color fieldBorderError;
  /// Ô nhập: viền khi tắt (DEC-174) (DEC-207)
  final Color fieldBorderDisabled;
  /// Ô nhập: chữ giá trị (DEC-207)
  final Color fieldFgValue;
  /// Ô nhập: chữ gợi ý trong ô trống; text/secondary để đạt 4,5:1 (DEC-207)
  final Color fieldFgPlaceholder;
  /// Ô nhập web: nhãn trên ô (DEC-207)
  final Color fieldFgLabelWeb;
  /// Ô nhập app: nhãn caption trong ô (DEC-184) (DEC-207)
  final Color fieldFgLabelApp;
  /// Ô nhập: dòng gợi ý dưới ô (DEC-192) (DEC-207)
  final Color fieldFgHelper;
  /// Ô nhập: chữ lỗi dưới ô, dấu * bắt buộc sau nhãn (DEC-177) (DEC-207)
  final Color fieldFgError;
  /// Ô nhập: chữ, nhãn, icon khi tắt (DEC-174) (DEC-207)
  final Color fieldFgDisabled;
  /// Ô nhập: icon đầu, icon cuối (nét lớp Vector, DEC-202) (DEC-207)
  final Color fieldFgIcon;
  /// Rãnh của Bar, phần chưa tô (DEC-243)
  final Color progressBgTrack;
  /// Phần tô Tone Brand, theo dải màu khách (DEC-167, DEC-243)
  final Color progressFillBrand;
  /// Phần tô, đoạn Tone success (DEC-243)
  final Color progressFillSuccess;
  /// Phần tô, đoạn Tone info (DEC-243)
  final Color progressFillInfo;
  /// Phần tô, đoạn Tone warning (DEC-243)
  final Color progressFillWarning;
  /// Phần tô, đoạn Tone danger (DEC-243)
  final Color progressFillDanger;
  /// Phần tô, đoạn Tone neutral (DEC-243)
  final Color progressFillNeutral;

  /// Tính từ Semantic (sáng/tối) + Brand (khách) đang dùng.
  factory InvComponentColors.from(InvColors s, InvBrandColors b) {
    final buttonBgPrimary = s.actionPrimary;
    final buttonBgPrimaryHover = s.actionPrimaryHover;
    final buttonBgPrimaryPressed = s.actionPrimaryPressed;
    final buttonFgPrimary = s.textInverse;
    final buttonBgSecondary = s.actionSecondary;
    final buttonBgSecondaryHover = s.actionSecondaryHover;
    final buttonBgSecondaryPressed = InvPrimitives.neutral300;
    final buttonFgSecondary = s.textPrimary;
    final buttonBgGhostHover = s.bgSelected;
    final buttonBgGhostPressed = s.actionSecondaryHover;
    final buttonFgGhost = s.textPrimary;
    final buttonBgDanger = s.actionDangerSubtle;
    final buttonBgDangerHover = InvPrimitives.red100;
    final buttonBgDangerPressed = InvPrimitives.red200;
    final buttonFgDanger = s.actionDanger;
    final buttonBgOutlineHover = InvPrimitives.neutral300;
    final buttonBgOutlinePressed = InvPrimitives.neutral400;
    final buttonFgOutline = s.textPrimary;
    final buttonBorderOutline = s.borderStrong;
    final buttonBorderOutlineDisabled = s.borderDefault;
    final buttonBgDisabled = s.actionSecondary;
    final buttonFgDisabled = s.textTertiary;
    final buttonFocusDanger = s.actionDanger;
    final avatarBg = b.brand100;
    final avatarFg = b.brand800;
    final avatarStatusOnline = s.chipGreenFg;
    final avatarStatusBusy = s.chipOrangeFg;
    final avatarStatusAway = s.chipYellowFg;
    final avatarStatusOffline = s.chipGrayFg;
    final avatarUploadBorder = s.borderInput;
    final avatarUploadFg = s.textSecondary;
    final avatarScrim = s.overlayScrim;
    final avatarEditBg = buttonBgPrimary;
    final avatarEditFg = buttonFgPrimary;
    final avatarOverflowBg = s.bgMuted;
    final avatarOverflowFg = s.textSecondary;
    final tooltipBg = s.bgInverse;
    final tooltipFg = s.textInverse;
    final listRowBgHover = InvPrimitives.neutral100;
    final listRowBgPressed = InvPrimitives.neutral200;
    final listRowBgSelected = s.bgSelected;
    final listRowFgDisabled = s.textTertiary;
    final listRowFgSecondaryPressed = InvPrimitives.neutral600;
    final listRowDivider = s.borderDefault;
    final listRowCheckFg = s.iconPrimary;
    final cardBgDefault = s.bgSurface;
    final cardBgHover = InvPrimitives.neutral100;
    final cardBgPressed = InvPrimitives.neutral300;
    final cardBorderDefault = s.borderDefault;
    final cardBorderPressed = InvPrimitives.neutral400;
    final cardBorderSelected = b.brand800;
    final cardBorderDashed = s.borderStrong;
    final cardRelatedBg = s.bgMuted;
    final cardLeadBg = s.bgMuted;
    final cardFgSecondaryPressed = InvPrimitives.neutral600;
    final cardFgSecondaryHover = InvPrimitives.neutral600;
    final cardDisabledBg = s.actionSecondary;
    final cardDisabledFg = s.textTertiary;
    final cardDisabledLeadBg = s.bgSurface;
    final cardCheckBg = cardBorderSelected;
    final cardCheckFg = s.textInverse;
    final cardCheckBorder = cardBgDefault;
    final cardRadioBorder = s.borderInput;
    final cardRadioOn = cardBorderSelected;
    final cardChoiceBg = s.bgMuted;
    final cardChoiceBgHover = s.actionSecondaryHover;
    final cardChoiceBgPressed = buttonBgSecondaryPressed;
    final fieldBgWeb = s.bgSurface;
    final fieldBgApp = s.bgMuted;
    final fieldBgHover = s.bgHover;
    final fieldBgDisabled = buttonBgDisabled;
    final fieldBgReadonly = s.bgMuted;
    final fieldBorderDefault = s.borderInput;
    final fieldBorderActive = s.borderFocus;
    final fieldBorderError = s.borderDanger;
    final fieldBorderDisabled = s.borderDefault;
    final fieldFgValue = s.textPrimary;
    final fieldFgPlaceholder = s.textTertiary;
    final fieldFgLabelWeb = s.textSecondary;
    final fieldFgLabelApp = s.textSecondary;
    final fieldFgHelper = s.textSecondary;
    final fieldFgError = s.statusDangerText;
    final fieldFgDisabled = s.textTertiary;
    final fieldFgIcon = s.iconSecondary;
    final progressBgTrack = s.borderDefault;
    final progressFillBrand = b.brand800;
    final progressFillSuccess = s.statusSuccessText;
    final progressFillInfo = s.statusInfoText;
    final progressFillWarning = s.statusWarningText;
    final progressFillDanger = s.statusDangerText;
    final progressFillNeutral = s.chipGrayFg;
    return InvComponentColors(buttonBgPrimary: buttonBgPrimary, buttonBgPrimaryHover: buttonBgPrimaryHover, buttonBgPrimaryPressed: buttonBgPrimaryPressed, buttonFgPrimary: buttonFgPrimary, buttonBgSecondary: buttonBgSecondary, buttonBgSecondaryHover: buttonBgSecondaryHover, buttonBgSecondaryPressed: buttonBgSecondaryPressed, buttonFgSecondary: buttonFgSecondary, buttonBgGhostHover: buttonBgGhostHover, buttonBgGhostPressed: buttonBgGhostPressed, buttonFgGhost: buttonFgGhost, buttonBgDanger: buttonBgDanger, buttonBgDangerHover: buttonBgDangerHover, buttonBgDangerPressed: buttonBgDangerPressed, buttonFgDanger: buttonFgDanger, buttonBgOutlineHover: buttonBgOutlineHover, buttonBgOutlinePressed: buttonBgOutlinePressed, buttonFgOutline: buttonFgOutline, buttonBorderOutline: buttonBorderOutline, buttonBorderOutlineDisabled: buttonBorderOutlineDisabled, buttonBgDisabled: buttonBgDisabled, buttonFgDisabled: buttonFgDisabled, buttonFocusDanger: buttonFocusDanger, avatarBg: avatarBg, avatarFg: avatarFg, avatarStatusOnline: avatarStatusOnline, avatarStatusBusy: avatarStatusBusy, avatarStatusAway: avatarStatusAway, avatarStatusOffline: avatarStatusOffline, avatarUploadBorder: avatarUploadBorder, avatarUploadFg: avatarUploadFg, avatarScrim: avatarScrim, avatarEditBg: avatarEditBg, avatarEditFg: avatarEditFg, avatarOverflowBg: avatarOverflowBg, avatarOverflowFg: avatarOverflowFg, tooltipBg: tooltipBg, tooltipFg: tooltipFg, listRowBgHover: listRowBgHover, listRowBgPressed: listRowBgPressed, listRowBgSelected: listRowBgSelected, listRowFgDisabled: listRowFgDisabled, listRowFgSecondaryPressed: listRowFgSecondaryPressed, listRowDivider: listRowDivider, listRowCheckFg: listRowCheckFg, cardBgDefault: cardBgDefault, cardBgHover: cardBgHover, cardBgPressed: cardBgPressed, cardBorderDefault: cardBorderDefault, cardBorderPressed: cardBorderPressed, cardBorderSelected: cardBorderSelected, cardBorderDashed: cardBorderDashed, cardRelatedBg: cardRelatedBg, cardLeadBg: cardLeadBg, cardFgSecondaryPressed: cardFgSecondaryPressed, cardFgSecondaryHover: cardFgSecondaryHover, cardDisabledBg: cardDisabledBg, cardDisabledFg: cardDisabledFg, cardDisabledLeadBg: cardDisabledLeadBg, cardCheckBg: cardCheckBg, cardCheckFg: cardCheckFg, cardCheckBorder: cardCheckBorder, cardRadioBorder: cardRadioBorder, cardRadioOn: cardRadioOn, cardChoiceBg: cardChoiceBg, cardChoiceBgHover: cardChoiceBgHover, cardChoiceBgPressed: cardChoiceBgPressed, fieldBgWeb: fieldBgWeb, fieldBgApp: fieldBgApp, fieldBgHover: fieldBgHover, fieldBgDisabled: fieldBgDisabled, fieldBgReadonly: fieldBgReadonly, fieldBorderDefault: fieldBorderDefault, fieldBorderActive: fieldBorderActive, fieldBorderError: fieldBorderError, fieldBorderDisabled: fieldBorderDisabled, fieldFgValue: fieldFgValue, fieldFgPlaceholder: fieldFgPlaceholder, fieldFgLabelWeb: fieldFgLabelWeb, fieldFgLabelApp: fieldFgLabelApp, fieldFgHelper: fieldFgHelper, fieldFgError: fieldFgError, fieldFgDisabled: fieldFgDisabled, fieldFgIcon: fieldFgIcon, progressBgTrack: progressBgTrack, progressFillBrand: progressFillBrand, progressFillSuccess: progressFillSuccess, progressFillInfo: progressFillInfo, progressFillWarning: progressFillWarning, progressFillDanger: progressFillDanger, progressFillNeutral: progressFillNeutral);
  }

  @override
  InvComponentColors copyWith({Color? buttonBgPrimary, Color? buttonBgPrimaryHover, Color? buttonBgPrimaryPressed, Color? buttonFgPrimary, Color? buttonBgSecondary, Color? buttonBgSecondaryHover, Color? buttonBgSecondaryPressed, Color? buttonFgSecondary, Color? buttonBgGhostHover, Color? buttonBgGhostPressed, Color? buttonFgGhost, Color? buttonBgDanger, Color? buttonBgDangerHover, Color? buttonBgDangerPressed, Color? buttonFgDanger, Color? buttonBgOutlineHover, Color? buttonBgOutlinePressed, Color? buttonFgOutline, Color? buttonBorderOutline, Color? buttonBorderOutlineDisabled, Color? buttonBgDisabled, Color? buttonFgDisabled, Color? buttonFocusDanger, Color? avatarBg, Color? avatarFg, Color? avatarStatusOnline, Color? avatarStatusBusy, Color? avatarStatusAway, Color? avatarStatusOffline, Color? avatarUploadBorder, Color? avatarUploadFg, Color? avatarScrim, Color? avatarEditBg, Color? avatarEditFg, Color? avatarOverflowBg, Color? avatarOverflowFg, Color? tooltipBg, Color? tooltipFg, Color? listRowBgHover, Color? listRowBgPressed, Color? listRowBgSelected, Color? listRowFgDisabled, Color? listRowFgSecondaryPressed, Color? listRowDivider, Color? listRowCheckFg, Color? cardBgDefault, Color? cardBgHover, Color? cardBgPressed, Color? cardBorderDefault, Color? cardBorderPressed, Color? cardBorderSelected, Color? cardBorderDashed, Color? cardRelatedBg, Color? cardLeadBg, Color? cardFgSecondaryPressed, Color? cardFgSecondaryHover, Color? cardDisabledBg, Color? cardDisabledFg, Color? cardDisabledLeadBg, Color? cardCheckBg, Color? cardCheckFg, Color? cardCheckBorder, Color? cardRadioBorder, Color? cardRadioOn, Color? cardChoiceBg, Color? cardChoiceBgHover, Color? cardChoiceBgPressed, Color? fieldBgWeb, Color? fieldBgApp, Color? fieldBgHover, Color? fieldBgDisabled, Color? fieldBgReadonly, Color? fieldBorderDefault, Color? fieldBorderActive, Color? fieldBorderError, Color? fieldBorderDisabled, Color? fieldFgValue, Color? fieldFgPlaceholder, Color? fieldFgLabelWeb, Color? fieldFgLabelApp, Color? fieldFgHelper, Color? fieldFgError, Color? fieldFgDisabled, Color? fieldFgIcon, Color? progressBgTrack, Color? progressFillBrand, Color? progressFillSuccess, Color? progressFillInfo, Color? progressFillWarning, Color? progressFillDanger, Color? progressFillNeutral}) =>
      InvComponentColors(buttonBgPrimary: buttonBgPrimary ?? this.buttonBgPrimary, buttonBgPrimaryHover: buttonBgPrimaryHover ?? this.buttonBgPrimaryHover, buttonBgPrimaryPressed: buttonBgPrimaryPressed ?? this.buttonBgPrimaryPressed, buttonFgPrimary: buttonFgPrimary ?? this.buttonFgPrimary, buttonBgSecondary: buttonBgSecondary ?? this.buttonBgSecondary, buttonBgSecondaryHover: buttonBgSecondaryHover ?? this.buttonBgSecondaryHover, buttonBgSecondaryPressed: buttonBgSecondaryPressed ?? this.buttonBgSecondaryPressed, buttonFgSecondary: buttonFgSecondary ?? this.buttonFgSecondary, buttonBgGhostHover: buttonBgGhostHover ?? this.buttonBgGhostHover, buttonBgGhostPressed: buttonBgGhostPressed ?? this.buttonBgGhostPressed, buttonFgGhost: buttonFgGhost ?? this.buttonFgGhost, buttonBgDanger: buttonBgDanger ?? this.buttonBgDanger, buttonBgDangerHover: buttonBgDangerHover ?? this.buttonBgDangerHover, buttonBgDangerPressed: buttonBgDangerPressed ?? this.buttonBgDangerPressed, buttonFgDanger: buttonFgDanger ?? this.buttonFgDanger, buttonBgOutlineHover: buttonBgOutlineHover ?? this.buttonBgOutlineHover, buttonBgOutlinePressed: buttonBgOutlinePressed ?? this.buttonBgOutlinePressed, buttonFgOutline: buttonFgOutline ?? this.buttonFgOutline, buttonBorderOutline: buttonBorderOutline ?? this.buttonBorderOutline, buttonBorderOutlineDisabled: buttonBorderOutlineDisabled ?? this.buttonBorderOutlineDisabled, buttonBgDisabled: buttonBgDisabled ?? this.buttonBgDisabled, buttonFgDisabled: buttonFgDisabled ?? this.buttonFgDisabled, buttonFocusDanger: buttonFocusDanger ?? this.buttonFocusDanger, avatarBg: avatarBg ?? this.avatarBg, avatarFg: avatarFg ?? this.avatarFg, avatarStatusOnline: avatarStatusOnline ?? this.avatarStatusOnline, avatarStatusBusy: avatarStatusBusy ?? this.avatarStatusBusy, avatarStatusAway: avatarStatusAway ?? this.avatarStatusAway, avatarStatusOffline: avatarStatusOffline ?? this.avatarStatusOffline, avatarUploadBorder: avatarUploadBorder ?? this.avatarUploadBorder, avatarUploadFg: avatarUploadFg ?? this.avatarUploadFg, avatarScrim: avatarScrim ?? this.avatarScrim, avatarEditBg: avatarEditBg ?? this.avatarEditBg, avatarEditFg: avatarEditFg ?? this.avatarEditFg, avatarOverflowBg: avatarOverflowBg ?? this.avatarOverflowBg, avatarOverflowFg: avatarOverflowFg ?? this.avatarOverflowFg, tooltipBg: tooltipBg ?? this.tooltipBg, tooltipFg: tooltipFg ?? this.tooltipFg, listRowBgHover: listRowBgHover ?? this.listRowBgHover, listRowBgPressed: listRowBgPressed ?? this.listRowBgPressed, listRowBgSelected: listRowBgSelected ?? this.listRowBgSelected, listRowFgDisabled: listRowFgDisabled ?? this.listRowFgDisabled, listRowFgSecondaryPressed: listRowFgSecondaryPressed ?? this.listRowFgSecondaryPressed, listRowDivider: listRowDivider ?? this.listRowDivider, listRowCheckFg: listRowCheckFg ?? this.listRowCheckFg, cardBgDefault: cardBgDefault ?? this.cardBgDefault, cardBgHover: cardBgHover ?? this.cardBgHover, cardBgPressed: cardBgPressed ?? this.cardBgPressed, cardBorderDefault: cardBorderDefault ?? this.cardBorderDefault, cardBorderPressed: cardBorderPressed ?? this.cardBorderPressed, cardBorderSelected: cardBorderSelected ?? this.cardBorderSelected, cardBorderDashed: cardBorderDashed ?? this.cardBorderDashed, cardRelatedBg: cardRelatedBg ?? this.cardRelatedBg, cardLeadBg: cardLeadBg ?? this.cardLeadBg, cardFgSecondaryPressed: cardFgSecondaryPressed ?? this.cardFgSecondaryPressed, cardFgSecondaryHover: cardFgSecondaryHover ?? this.cardFgSecondaryHover, cardDisabledBg: cardDisabledBg ?? this.cardDisabledBg, cardDisabledFg: cardDisabledFg ?? this.cardDisabledFg, cardDisabledLeadBg: cardDisabledLeadBg ?? this.cardDisabledLeadBg, cardCheckBg: cardCheckBg ?? this.cardCheckBg, cardCheckFg: cardCheckFg ?? this.cardCheckFg, cardCheckBorder: cardCheckBorder ?? this.cardCheckBorder, cardRadioBorder: cardRadioBorder ?? this.cardRadioBorder, cardRadioOn: cardRadioOn ?? this.cardRadioOn, cardChoiceBg: cardChoiceBg ?? this.cardChoiceBg, cardChoiceBgHover: cardChoiceBgHover ?? this.cardChoiceBgHover, cardChoiceBgPressed: cardChoiceBgPressed ?? this.cardChoiceBgPressed, fieldBgWeb: fieldBgWeb ?? this.fieldBgWeb, fieldBgApp: fieldBgApp ?? this.fieldBgApp, fieldBgHover: fieldBgHover ?? this.fieldBgHover, fieldBgDisabled: fieldBgDisabled ?? this.fieldBgDisabled, fieldBgReadonly: fieldBgReadonly ?? this.fieldBgReadonly, fieldBorderDefault: fieldBorderDefault ?? this.fieldBorderDefault, fieldBorderActive: fieldBorderActive ?? this.fieldBorderActive, fieldBorderError: fieldBorderError ?? this.fieldBorderError, fieldBorderDisabled: fieldBorderDisabled ?? this.fieldBorderDisabled, fieldFgValue: fieldFgValue ?? this.fieldFgValue, fieldFgPlaceholder: fieldFgPlaceholder ?? this.fieldFgPlaceholder, fieldFgLabelWeb: fieldFgLabelWeb ?? this.fieldFgLabelWeb, fieldFgLabelApp: fieldFgLabelApp ?? this.fieldFgLabelApp, fieldFgHelper: fieldFgHelper ?? this.fieldFgHelper, fieldFgError: fieldFgError ?? this.fieldFgError, fieldFgDisabled: fieldFgDisabled ?? this.fieldFgDisabled, fieldFgIcon: fieldFgIcon ?? this.fieldFgIcon, progressBgTrack: progressBgTrack ?? this.progressBgTrack, progressFillBrand: progressFillBrand ?? this.progressFillBrand, progressFillSuccess: progressFillSuccess ?? this.progressFillSuccess, progressFillInfo: progressFillInfo ?? this.progressFillInfo, progressFillWarning: progressFillWarning ?? this.progressFillWarning, progressFillDanger: progressFillDanger ?? this.progressFillDanger, progressFillNeutral: progressFillNeutral ?? this.progressFillNeutral);

  @override
  InvComponentColors lerp(covariant ThemeExtension<InvComponentColors>? other, double t) {
    if (other is! InvComponentColors) return this;
    return InvComponentColors(buttonBgPrimary: Color.lerp(buttonBgPrimary, other.buttonBgPrimary, t)!, buttonBgPrimaryHover: Color.lerp(buttonBgPrimaryHover, other.buttonBgPrimaryHover, t)!, buttonBgPrimaryPressed: Color.lerp(buttonBgPrimaryPressed, other.buttonBgPrimaryPressed, t)!, buttonFgPrimary: Color.lerp(buttonFgPrimary, other.buttonFgPrimary, t)!, buttonBgSecondary: Color.lerp(buttonBgSecondary, other.buttonBgSecondary, t)!, buttonBgSecondaryHover: Color.lerp(buttonBgSecondaryHover, other.buttonBgSecondaryHover, t)!, buttonBgSecondaryPressed: Color.lerp(buttonBgSecondaryPressed, other.buttonBgSecondaryPressed, t)!, buttonFgSecondary: Color.lerp(buttonFgSecondary, other.buttonFgSecondary, t)!, buttonBgGhostHover: Color.lerp(buttonBgGhostHover, other.buttonBgGhostHover, t)!, buttonBgGhostPressed: Color.lerp(buttonBgGhostPressed, other.buttonBgGhostPressed, t)!, buttonFgGhost: Color.lerp(buttonFgGhost, other.buttonFgGhost, t)!, buttonBgDanger: Color.lerp(buttonBgDanger, other.buttonBgDanger, t)!, buttonBgDangerHover: Color.lerp(buttonBgDangerHover, other.buttonBgDangerHover, t)!, buttonBgDangerPressed: Color.lerp(buttonBgDangerPressed, other.buttonBgDangerPressed, t)!, buttonFgDanger: Color.lerp(buttonFgDanger, other.buttonFgDanger, t)!, buttonBgOutlineHover: Color.lerp(buttonBgOutlineHover, other.buttonBgOutlineHover, t)!, buttonBgOutlinePressed: Color.lerp(buttonBgOutlinePressed, other.buttonBgOutlinePressed, t)!, buttonFgOutline: Color.lerp(buttonFgOutline, other.buttonFgOutline, t)!, buttonBorderOutline: Color.lerp(buttonBorderOutline, other.buttonBorderOutline, t)!, buttonBorderOutlineDisabled: Color.lerp(buttonBorderOutlineDisabled, other.buttonBorderOutlineDisabled, t)!, buttonBgDisabled: Color.lerp(buttonBgDisabled, other.buttonBgDisabled, t)!, buttonFgDisabled: Color.lerp(buttonFgDisabled, other.buttonFgDisabled, t)!, buttonFocusDanger: Color.lerp(buttonFocusDanger, other.buttonFocusDanger, t)!, avatarBg: Color.lerp(avatarBg, other.avatarBg, t)!, avatarFg: Color.lerp(avatarFg, other.avatarFg, t)!, avatarStatusOnline: Color.lerp(avatarStatusOnline, other.avatarStatusOnline, t)!, avatarStatusBusy: Color.lerp(avatarStatusBusy, other.avatarStatusBusy, t)!, avatarStatusAway: Color.lerp(avatarStatusAway, other.avatarStatusAway, t)!, avatarStatusOffline: Color.lerp(avatarStatusOffline, other.avatarStatusOffline, t)!, avatarUploadBorder: Color.lerp(avatarUploadBorder, other.avatarUploadBorder, t)!, avatarUploadFg: Color.lerp(avatarUploadFg, other.avatarUploadFg, t)!, avatarScrim: Color.lerp(avatarScrim, other.avatarScrim, t)!, avatarEditBg: Color.lerp(avatarEditBg, other.avatarEditBg, t)!, avatarEditFg: Color.lerp(avatarEditFg, other.avatarEditFg, t)!, avatarOverflowBg: Color.lerp(avatarOverflowBg, other.avatarOverflowBg, t)!, avatarOverflowFg: Color.lerp(avatarOverflowFg, other.avatarOverflowFg, t)!, tooltipBg: Color.lerp(tooltipBg, other.tooltipBg, t)!, tooltipFg: Color.lerp(tooltipFg, other.tooltipFg, t)!, listRowBgHover: Color.lerp(listRowBgHover, other.listRowBgHover, t)!, listRowBgPressed: Color.lerp(listRowBgPressed, other.listRowBgPressed, t)!, listRowBgSelected: Color.lerp(listRowBgSelected, other.listRowBgSelected, t)!, listRowFgDisabled: Color.lerp(listRowFgDisabled, other.listRowFgDisabled, t)!, listRowFgSecondaryPressed: Color.lerp(listRowFgSecondaryPressed, other.listRowFgSecondaryPressed, t)!, listRowDivider: Color.lerp(listRowDivider, other.listRowDivider, t)!, listRowCheckFg: Color.lerp(listRowCheckFg, other.listRowCheckFg, t)!, cardBgDefault: Color.lerp(cardBgDefault, other.cardBgDefault, t)!, cardBgHover: Color.lerp(cardBgHover, other.cardBgHover, t)!, cardBgPressed: Color.lerp(cardBgPressed, other.cardBgPressed, t)!, cardBorderDefault: Color.lerp(cardBorderDefault, other.cardBorderDefault, t)!, cardBorderPressed: Color.lerp(cardBorderPressed, other.cardBorderPressed, t)!, cardBorderSelected: Color.lerp(cardBorderSelected, other.cardBorderSelected, t)!, cardBorderDashed: Color.lerp(cardBorderDashed, other.cardBorderDashed, t)!, cardRelatedBg: Color.lerp(cardRelatedBg, other.cardRelatedBg, t)!, cardLeadBg: Color.lerp(cardLeadBg, other.cardLeadBg, t)!, cardFgSecondaryPressed: Color.lerp(cardFgSecondaryPressed, other.cardFgSecondaryPressed, t)!, cardFgSecondaryHover: Color.lerp(cardFgSecondaryHover, other.cardFgSecondaryHover, t)!, cardDisabledBg: Color.lerp(cardDisabledBg, other.cardDisabledBg, t)!, cardDisabledFg: Color.lerp(cardDisabledFg, other.cardDisabledFg, t)!, cardDisabledLeadBg: Color.lerp(cardDisabledLeadBg, other.cardDisabledLeadBg, t)!, cardCheckBg: Color.lerp(cardCheckBg, other.cardCheckBg, t)!, cardCheckFg: Color.lerp(cardCheckFg, other.cardCheckFg, t)!, cardCheckBorder: Color.lerp(cardCheckBorder, other.cardCheckBorder, t)!, cardRadioBorder: Color.lerp(cardRadioBorder, other.cardRadioBorder, t)!, cardRadioOn: Color.lerp(cardRadioOn, other.cardRadioOn, t)!, cardChoiceBg: Color.lerp(cardChoiceBg, other.cardChoiceBg, t)!, cardChoiceBgHover: Color.lerp(cardChoiceBgHover, other.cardChoiceBgHover, t)!, cardChoiceBgPressed: Color.lerp(cardChoiceBgPressed, other.cardChoiceBgPressed, t)!, fieldBgWeb: Color.lerp(fieldBgWeb, other.fieldBgWeb, t)!, fieldBgApp: Color.lerp(fieldBgApp, other.fieldBgApp, t)!, fieldBgHover: Color.lerp(fieldBgHover, other.fieldBgHover, t)!, fieldBgDisabled: Color.lerp(fieldBgDisabled, other.fieldBgDisabled, t)!, fieldBgReadonly: Color.lerp(fieldBgReadonly, other.fieldBgReadonly, t)!, fieldBorderDefault: Color.lerp(fieldBorderDefault, other.fieldBorderDefault, t)!, fieldBorderActive: Color.lerp(fieldBorderActive, other.fieldBorderActive, t)!, fieldBorderError: Color.lerp(fieldBorderError, other.fieldBorderError, t)!, fieldBorderDisabled: Color.lerp(fieldBorderDisabled, other.fieldBorderDisabled, t)!, fieldFgValue: Color.lerp(fieldFgValue, other.fieldFgValue, t)!, fieldFgPlaceholder: Color.lerp(fieldFgPlaceholder, other.fieldFgPlaceholder, t)!, fieldFgLabelWeb: Color.lerp(fieldFgLabelWeb, other.fieldFgLabelWeb, t)!, fieldFgLabelApp: Color.lerp(fieldFgLabelApp, other.fieldFgLabelApp, t)!, fieldFgHelper: Color.lerp(fieldFgHelper, other.fieldFgHelper, t)!, fieldFgError: Color.lerp(fieldFgError, other.fieldFgError, t)!, fieldFgDisabled: Color.lerp(fieldFgDisabled, other.fieldFgDisabled, t)!, fieldFgIcon: Color.lerp(fieldFgIcon, other.fieldFgIcon, t)!, progressBgTrack: Color.lerp(progressBgTrack, other.progressBgTrack, t)!, progressFillBrand: Color.lerp(progressFillBrand, other.progressFillBrand, t)!, progressFillSuccess: Color.lerp(progressFillSuccess, other.progressFillSuccess, t)!, progressFillInfo: Color.lerp(progressFillInfo, other.progressFillInfo, t)!, progressFillWarning: Color.lerp(progressFillWarning, other.progressFillWarning, t)!, progressFillDanger: Color.lerp(progressFillDanger, other.progressFillDanger, t)!, progressFillNeutral: Color.lerp(progressFillNeutral, other.progressFillNeutral, t)!);
  }
}

/// Platform — số đo theo nền tảng. App dùng InvPlatform.mobile.
@immutable
class InvPlatform extends ThemeExtension<InvPlatform> {
  const InvPlatform({
    required this.radiusControl,
    required this.radiusField,
    required this.radiusCard,
    required this.radiusInner,
    required this.radiusOverlay,
    required this.radiusChip,
    required this.radiusMenu,
    required this.radiusMenuItem,
    required this.radiusBadge,
    required this.radiusTab,
    required this.spaceInsetXs,
    required this.spaceInsetSm,
    required this.spaceInsetMd,
    required this.spaceInsetLg,
    required this.spaceInsetXl,
    required this.spaceGapXs,
    required this.spaceGapSm,
    required this.spaceGapMd,
    required this.spaceGapLg,
    required this.spaceGapXl,
    required this.spaceGap2xl,
    required this.layoutScreenInset,
    required this.layoutCardPadding,
    required this.layoutListGap,
    required this.layoutSectionGap,
    required this.layoutTitleGap,
    required this.layoutEmptyPadding,
    required this.layoutContentMaxWidth,
    required this.formFieldGap,
    required this.touchMin,
    required this.controlHeightSm,
    required this.controlHeightMd,
    required this.controlHeightLg,
    required this.controlPaddingXSm,
    required this.controlPaddingXMd,
    required this.controlPaddingXLg,
    required this.controlPaddingXIconSm,
    required this.controlPaddingXIconMd,
    required this.controlPaddingXIconLg,
    required this.controlIconGap,
    required this.tabPaddingX,
    required this.tabPaddingXIcon,
    required this.tabGap,
    required this.navHeight,
    required this.navOffsetBottom,
    required this.navPaddingX,
    required this.navItemPaddingY,
    required this.navScanSize,
    required this.chipHeight,
    required this.chipHeightSm,
    required this.chipHeightLg,
    required this.chipFontSizeSm,
    required this.chipLineHeightSm,
    required this.chipLabelMaxWidth,
    required this.chipPaddingX,
    required this.chipPaddingXSm,
    required this.chipPaddingXLg,
    required this.chipPaddingXIcon,
    required this.chipIconGap,
    required this.chipDotGap,
    required this.chipDotSize,
    required this.avatarSizeSm,
    required this.avatarSizeMd,
    required this.avatarSizeLg,
    required this.avatarStatusSizeSm,
    required this.avatarStatusSizeMd,
    required this.avatarStatusSizeLg,
    required this.avatarEditSizeMd,
    required this.avatarEditSizeLg,
    required this.avatarSizeXl,
    required this.avatarSizeXxl,
    required this.avatarStatusSizeXl,
    required this.avatarStatusSizeXxl,
    required this.avatarEditSizeXl,
    required this.avatarEditSizeXxl,
    required this.avatarIconSizeSm,
    required this.avatarIconSizeMd,
    required this.avatarIconSizeLg,
    required this.avatarIconSizeXl,
    required this.avatarIconSizeXxl,
    required this.avatarEditIconSizeMd,
    required this.avatarEditIconSizeLg,
    required this.avatarEditIconSizeXl,
    required this.avatarEditIconSizeXxl,
    required this.avatarSpinnerSizeSm,
    required this.avatarSpinnerSizeMd,
    required this.avatarSpinnerSizeLg,
    required this.avatarSpinnerSizeXl,
    required this.avatarSpinnerSizeXxl,
    required this.avatarGroupOverlapSm,
    required this.avatarGroupOverlapMd,
    required this.avatarGroupOverlapLg,
    required this.avatarRing,
    required this.tooltipPaddingX,
    required this.tooltipPaddingY,
    required this.tooltipRadius,
    required this.tooltipMaxWidth,
    required this.tooltipOffset,
    required this.tooltipArrowW,
    required this.tooltipArrowH,
    required this.focusWidth,
    required this.focusOffset,
    required this.typeDisplaySize,
    required this.typeDisplayLineHeight,
    required this.typeTitle1Size,
    required this.typeTitle1LineHeight,
    required this.typeTitle2Size,
    required this.typeTitle2LineHeight,
    required this.typeTitle3Size,
    required this.typeTitle3LineHeight,
    required this.typeHeadingSize,
    required this.typeHeadingLineHeight,
    required this.typeBodySize,
    required this.typeBodyLineHeight,
    required this.typeLabelSize,
    required this.typeLabelLineHeight,
    required this.typeCaptionSize,
    required this.typeCaptionLineHeight,
    required this.typeCodeSize,
    required this.typeCodeLineHeight,
    required this.typeLabelWeight,
    required this.iconSizeSm,
    required this.iconSizeMd,
    required this.iconSizeLg,
    required this.iconSizeChip,
    required this.listRowMinHeight,
    required this.listRowPaddingX,
    required this.listRowPaddingY,
    required this.listRowGap,
    required this.listRowTextGap,
    required this.listRowRadius,
    required this.listRowDividerHeight,
    required this.listRowValueMaxWidth,
    required this.cardPaddingNone,
    required this.cardPaddingCompact,
    required this.cardPaddingSpacious,
    required this.cardRowIconCell,
    required this.cardLeadSize,
    required this.cardMediaSize,
    required this.cardMediaSizeSm,
    required this.cardActionGap,
    required this.cardBorderWidth,
    required this.cardBorderWidthSelected,
    required this.cardRowLabelMax,
    required this.cardRowMinHeight,
    required this.cardCheckSize,
    required this.cardCheckRing,
    required this.cardRadioSize,
    required this.cardRadioRing,
    required this.cardRadioOnRing,
    required this.cardChoiceTextGap,
    required this.fieldBorderWidth,
    required this.fieldBorderWidthActive,
    required this.fieldWidthDefault,
    required this.fieldEdgeInset,
    required this.fieldTextInset,
    required this.fieldContentGap,
    required this.fieldHintInset,
    required this.fieldLabelMaxWidth,
    required this.progressHeightSm,
    required this.progressHeightMd,
    required this.progressGap,
    required this.progressWidthDefault,
    required this.progressSegmentWidth,
    required this.otpCellWidth,
    required this.widthXs,
    required this.widthSm,
    required this.widthMd,
    required this.widthLg,
    required this.widthXl,
    required this.width2xl,
    required this.tableRowMinHeight,
    required this.tableCellPaddingY,
    required this.tableCellPaddingX,
  });

  /// Nút, tab chip, ô tìm
  final double radiusControl;
  /// Ô nhập, ô chọn
  final double radiusField;
  /// Thẻ, nhóm có viền, khối trong trang, bảng; bo không quá lề thẻ (DEC-165)
  final double radiusCard;
  /// Khối phụ trong thẻ, ảnh nhỏ
  final double radiusInner;
  /// Dialog, popover; đầu sheet trên app (DEC-259: web 16, app 24)
  final double radiusOverlay;
  /// Chip trạng thái, avatar
  final double radiusChip;
  /// Menu thả, popover danh sách (DEC-259, như Untitled)
  final double radiusMenu;
  /// Mục trong menu thả (DEC-259)
  final double radiusMenuItem;
  /// Badge vuông cho nhãn phân loại, không phải trạng thái (DEC-259)
  final double radiusBadge;
  /// Tab kiểu nút (web 8, app tab chip tròn); tab gạch không bo (DEC-259)
  final double radiusTab;
  /// Lề trong component
  final double spaceInsetXs;
  /// Lề trong component
  final double spaceInsetSm;
  /// Lề trong component
  final double spaceInsetMd;
  /// Lề trong component
  final double spaceInsetLg;
  /// Lề trong component
  final double spaceInsetXl;
  /// Khoảng giữa các phần tử
  final double spaceGapXs;
  /// Khoảng giữa các phần tử
  final double spaceGapSm;
  /// Khoảng giữa các phần tử
  final double spaceGapMd;
  /// Khoảng giữa các phần tử
  final double spaceGapLg;
  /// Khoảng giữa các phần tử
  final double spaceGapXl;
  /// Khoảng giữa các phần tử
  final double spaceGap2xl;
  /// Lề màn (DEC-259: web 32 như Untitled, app 16)
  final double layoutScreenInset;
  /// Lề chứa: lề trong thẻ, nhóm có viền, dòng trong nhóm (DEC-164, DEC-165)
  final double layoutCardPadding;
  /// Giữa các thẻ, dòng trong danh sách
  final double layoutListGap;
  /// Giữa các khối lớn
  final double layoutSectionGap;
  /// Tiêu đề màn → nội dung (DEC-192)
  final double layoutTitleGap;
  /// Lề trên dưới màn trống, màn kết quả, đăng nhập (DEC-259)
  final double layoutEmptyPadding;
  /// Rộng nội dung tối đa màn chi tiết, form web; màn bảng trải hết (DEC-259)
  final double layoutContentMaxWidth;
  /// Giữa 2 ô nhập trong một nhóm (DEC-192)
  final double formFieldGap;
  /// Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138)
  final double touchMin;
  /// Cao control cỡ SM: nút trong hàng bảng (web), tab chip, nút nhỏ (app) (DEC-173)
  final double controlHeightSm;
  /// Cao control cỡ MD (mặc định): nút, ô nhập web; nút trong thẻ, sheet, nút icon (app) (DEC-173)
  final double controlHeightMd;
  /// Cao control cỡ LG: màn đăng nhập, nút cần nổi (web); nút chân màn, ô nhập (app) (DEC-173)
  final double controlHeightLg;
  /// Lề trái phải trong nút cỡ SM (DEC-192)
  final double controlPaddingXSm;
  /// Lề trái phải trong nút cỡ MD (DEC-192)
  final double controlPaddingXMd;
  /// Lề trái phải trong nút cỡ LG; nút app 52 lề 24 (DEC-163, DEC-192)
  final double controlPaddingXLg;
  /// Lề phía có icon trong nút cỡ SM: lùi một bậc thang (DEC-192)
  final double controlPaddingXIconSm;
  /// Lề phía có icon trong nút cỡ MD: lùi một bậc thang (DEC-192)
  final double controlPaddingXIconMd;
  /// Lề phía có icon trong nút cỡ LG: lùi một bậc thang (DEC-163, DEC-192)
  final double controlPaddingXIconLg;
  /// Icon → chữ trong nút, tab chip (DEC-161, DEC-192)
  final double controlIconGap;
  /// Lề trái phải trong tab: web tab gạch, app tab chip (DEC-164, DEC-192)
  final double tabPaddingX;
  /// Lề phía có icon trong tab: lùi một bậc thang (DEC-192)
  final double tabPaddingXIcon;
  /// Giữa 2 tab (DEC-192)
  final double tabGap;
  /// Cao thanh điều hướng nổi app (DEC-160); chỉ app, giá trị Web cho đủ mode
  final double navHeight;
  /// Thanh điều hướng → vùng an toàn đáy màn (DEC-160); chỉ app
  final double navOffsetBottom;
  /// Lề trong thanh điều hướng (DEC-160); chỉ app
  final double navPaddingX;
  /// Lề trên dưới mục, nên nền mục đang chọn cao 56 (DEC-160); chỉ app
  final double navItemPaddingY;
  /// Nút Quét mã giữa thanh điều hướng (DEC-160); chỉ app
  final double navScanSize;
  /// Cao chip MD (DEC-259 theo Untitled: sm 22 · md 24 · lg 28)
  final double chipHeight;
  /// Cao chip Size SM: 16 = một dòng chữ 12/16, dùng ở đầu thẻ bản ghi; web và app cùng 16 (DEC-239); MD là chip/height
  final double chipHeightSm;
  /// Cao chip LG (DEC-259)
  final double chipHeightLg;
  /// Chip SM: cỡ chữ cố định 12 cả web lẫn app, không theo type/caption/size (DEC-239)
  final double chipFontSizeSm;
  /// Chip SM: cao dòng cố định 16 cả web lẫn app (DEC-239)
  final double chipLineHeightSm;
  /// Chip: rộng tối đa lớp nhãn 160, dài hơn cắt "…" một dòng (DEC-239)
  final double chipLabelMaxWidth;
  /// Lề chip MD (DEC-259: 10 như Untitled)
  final double chipPaddingX;
  /// Lề chip SM (DEC-259)
  final double chipPaddingXSm;
  /// Lề chip LG (DEC-259)
  final double chipPaddingXLg;
  /// Lề phía icon chip Soft: lùi một bậc (DEC-200)
  final double chipPaddingXIcon;
  /// Icon → chữ chip Soft (DEC-200)
  final double chipIconGap;
  /// Chấm → chữ chip Dot (DEC-200)
  final double chipDotGap;
  /// Cỡ chấm chip Dot (DEC-200)
  final double chipDotSize;
  /// Cỡ avatar SM (DEC-201)
  final double avatarSizeSm;
  /// Cỡ avatar MD (DEC-201)
  final double avatarSizeMd;
  /// Cỡ avatar LG (DEC-201)
  final double avatarSizeLg;
  /// Chấm trạng thái avatar SM, chưa tính viền trắng 2 (DEC-201)
  final double avatarStatusSizeSm;
  /// Chấm trạng thái avatar MD, chưa tính viền trắng 2 (DEC-201)
  final double avatarStatusSizeMd;
  /// Chấm trạng thái avatar LG, chưa tính viền trắng 2 (DEC-201)
  final double avatarStatusSizeLg;
  /// Nút đổi ảnh trên avatar MD (DEC-201)
  final double avatarEditSizeMd;
  /// Nút đổi ảnh trên avatar LG (DEC-201)
  final double avatarEditSizeLg;
  /// Cỡ avatar XL, ảnh đại diện đổi được (DEC-203)
  final double avatarSizeXl;
  /// Cỡ avatar XXL, đầu trang hồ sơ (DEC-203)
  final double avatarSizeXxl;
  /// Chấm trạng thái avatar XL (DEC-203)
  final double avatarStatusSizeXl;
  /// Chấm trạng thái avatar XXL (DEC-203)
  final double avatarStatusSizeXxl;
  /// Nút đổi ảnh trên avatar XL (DEC-203)
  final double avatarEditSizeXl;
  /// Nút đổi ảnh trên avatar XXL (DEC-203)
  final double avatarEditSizeXxl;
  /// Icon trong Avatar SM (Content=Icon, Upload): 14 (DEC-242)
  final double avatarIconSizeSm;
  /// Icon trong Avatar MD (Content=Icon, Upload): 20 (DEC-242)
  final double avatarIconSizeMd;
  /// Icon trong Avatar LG (Content=Icon, Upload): 24 (thư viện icon có tới cỡ 24) (DEC-242)
  final double avatarIconSizeLg;
  /// Icon trong Avatar XL (Content=Icon, Upload): 24 (DEC-242)
  final double avatarIconSizeXl;
  /// Icon trong Avatar XXL (Content=Icon, Upload): 24 (DEC-242)
  final double avatarIconSizeXxl;
  /// Icon camera nút đổi ảnh MD (nút 20): 12 (DEC-242)
  final double avatarEditIconSizeMd;
  /// Icon camera nút đổi ảnh LG (nút 24): 14 (DEC-242)
  final double avatarEditIconSizeLg;
  /// Icon camera nút đổi ảnh XL (nút 28): 16 (DEC-242)
  final double avatarEditIconSizeXl;
  /// Icon camera nút đổi ảnh XXL (nút 32): 16 (DEC-242)
  final double avatarEditIconSizeXxl;
  /// Vòng quay Uploading, Avatar SM: 12 (DEC-242)
  final double avatarSpinnerSizeSm;
  /// Vòng quay Uploading, Avatar MD: 16 (DEC-242)
  final double avatarSpinnerSizeMd;
  /// Vòng quay Uploading, Avatar LG: 20 (DEC-242)
  final double avatarSpinnerSizeLg;
  /// Vòng quay Uploading, Avatar XL: 24 (DEC-242)
  final double avatarSpinnerSizeXl;
  /// Vòng quay Uploading, Avatar XXL: 28 (DEC-242)
  final double avatarSpinnerSizeXxl;
  /// Avatar Group SM: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (6), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242)
  final double avatarGroupOverlapSm;
  /// Avatar Group MD: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (8), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242)
  final double avatarGroupOverlapMd;
  /// Avatar Group LG: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (12), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242)
  final double avatarGroupOverlapLg;
  /// Viền trắng quanh avatar trong Group, chấm trạng thái, nút đổi ảnh (DEC-205)
  final double avatarRing;
  /// Lề trái phải tooltip (DEC-206)
  final double tooltipPaddingX;
  /// Lề trên dưới tooltip (DEC-206)
  final double tooltipPaddingY;
  /// Bo tooltip (DEC-206)
  final double tooltipRadius;
  /// Rộng tối đa tooltip, quá thì xuống dòng (DEC-206)
  final double tooltipMaxWidth;
  /// Tooltip cách đối tượng (DEC-206)
  final double tooltipOffset;
  /// Rộng mũi tên tooltip (DEC-206)
  final double tooltipArrowW;
  /// Cao mũi tên tooltip (DEC-206)
  final double tooltipArrowH;
  /// Độ dày vòng focus
  final double focusWidth;
  /// Khoảng cách vòng focus tới mép control
  final double focusOffset;
  /// Số lớn, màn giới thiệu
  final double typeDisplaySize;
  /// Số lớn, màn giới thiệu
  final double typeDisplayLineHeight;
  /// Tiêu đề màn
  final double typeTitle1Size;
  /// Tiêu đề màn
  final double typeTitle1LineHeight;
  /// Tiêu đề dialog, sheet, khối lớn
  final double typeTitle2Size;
  /// Tiêu đề dialog, sheet, khối lớn
  final double typeTitle2LineHeight;
  /// Tiêu đề khối, thẻ
  final double typeTitle3Size;
  /// Tiêu đề khối, thẻ
  final double typeTitle3LineHeight;
  /// Tiêu đề nhóm nhỏ
  final double typeHeadingSize;
  /// Tiêu đề nhóm nhỏ
  final double typeHeadingLineHeight;
  /// Chữ đọc, giá trị
  final double typeBodySize;
  /// Chữ đọc, giá trị
  final double typeBodyLineHeight;
  /// Nút, nhãn, tab
  final double typeLabelSize;
  /// Nút, nhãn, tab
  final double typeLabelLineHeight;
  /// Thông tin phụ, thời gian
  final double typeCaptionSize;
  /// Thông tin phụ, thời gian
  final double typeCaptionLineHeight;
  /// Mã lệnh, mã chứng từ
  final double typeCodeSize;
  /// Mã lệnh, mã chứng từ
  final double typeCodeLineHeight;
  /// Độ đậm nhãn, nút: web 500, app 600 (DEC-133)
  final FontWeight typeLabelWeight;
  /// Icon trong nút có chữ, ô nhập, ô tìm, mũi tên tuyến, chevron (DEC-143)
  final double iconSizeSm;
  /// Icon menu, hàng bảng, hàng danh sách, nút icon (DEC-143)
  final double iconSizeMd;
  /// Icon thanh tab app, icon đứng riêng (DEC-143)
  final double iconSizeLg;
  /// Icon trong chip trạng thái (DEC-143)
  final double iconSizeChip;
  /// Cao tối thiểu của Base / List Item: web 36, app 52. Cao thật theo nội dung (DEC-182) (DEC-232)
  final double listRowMinHeight;
  /// Lề trái phải của dòng: web 8, app 12, bằng lề dọc để lề 4 phía đều (DEC-165) (DEC-232)
  final double listRowPaddingX;
  /// Lề trên dưới của thân dòng: web 8, app 12. Chữ 1 dòng web 20 + 2×8 = 36 (DEC-182, DEC-165) (DEC-232)
  final double listRowPaddingY;
  /// Khoảng giữa đầu dòng, chữ, giá trị, cuối dòng, dấu chọn: web 8, app 12 (DEC-232)
  final double listRowGap;
  /// Khoảng giữa Label và Description: 2 (DEC-182) (DEC-232)
  final double listRowTextGap;
  /// Bo nền dòng khi hover, pressed, selected: 8, không quá lề dọc (DEC-165) (DEC-232)
  final double listRowRadius;
  /// Dày đường kẻ dưới dòng, kẻ đầy ngang (DEC-182) (DEC-232)
  final double listRowDividerHeight;
  /// Rộng tối đa chữ giá trị (Value) cuối dòng, dài hơn cắt "…" (DEC-182, DEC-193) (DEC-232)
  final double listRowValueMaxWidth;
  /// Lề trong Base / Card, Padding = None: 0, nội dung tự lo lề (DEC-234)
  final double cardPaddingNone;
  /// Lề trong Base / Card, Padding = Compact: 12 (DEC-234)
  final double cardPaddingCompact;
  /// Lề trong Base / Card, Padding = Spacious: 24 (DEC-234); Default là layout/card-padding 16
  final double cardPaddingSpacious;
  /// Ô 24 đặt icon đầu dòng trong thẻ (.card / Row): icon 16 giữa ô, chữ cách ô 8 → K3 64 (DEC-164) (DEC-209)
  final double cardRowIconCell;
  /// Ô 36 đầu thẻ: vòng icon `.card / Header`, vòng icon Selectable Card; chữ cách 12 → K4 80 (DEC-164) (DEC-209)
  final double cardLeadSize;
  /// Ảnh nhỏ cỡ MD của `.card / Media`: 64, đầu thẻ bản ghi (Base / Record Card), bo radius/inner; chữ ở 108 là ngoại lệ đường K (DEC-209, DEC-237)
  final double cardMediaSize;
  /// Ảnh nhỏ cỡ SM của `.card / Media`: 48, đầu thẻ chọn (Base / Selectable Card), bo radius/inner (DEC-237)
  final double cardMediaSizeSm;
  /// Giữa 2 nút ở chân thẻ (Slot Footer của Record Card): web 8, app 12 (DEC-192) (DEC-209, DEC-235)
  final double cardActionGap;
  /// Viền mảnh của thẻ, đặt trong (DEC-125) (DEC-209)
  final double cardBorderWidth;
  /// Viền thẻ đang chọn, đặt trong (DEC-209)
  final double cardBorderWidthSelected;
  /// Rộng tối đa nhãn .card / Row Label Value, dài hơn cắt "…" để giá trị còn chỗ (DEC-209)
  final double cardRowLabelMax;
  /// Cao tối thiểu dòng trong thẻ = ô icon 24, dòng có và không icon cao bằng nhau (DEC-164) (DEC-209)
  final double cardRowMinHeight;
  /// Tick tròn thẻ đang chọn (.card / Check), đè góc trên phải lệch ra ngoài 6 (DEC-209)
  final double cardCheckSize;
  /// Viền trắng quanh tick, tách tick khỏi viền 2px của thẻ (DEC-209)
  final double cardCheckRing;
  /// Radio thẻ chọn: web 16 (Astryx 6234:14440), app 20 (DEC-184, DEC-196, DEC-236)
  final double cardRadioSize;
  /// Nét radio chưa chọn (DEC-184 bản chốt, DEC-236)
  final double cardRadioRing;
  /// Nét radio đang chọn, chừa chấm trắng 6 (web) · 8 (app) (DEC-184 bản chốt, DEC-236)
  final double cardRadioOnRing;
  /// Tên → mô tả ở Selectable Card: web 2, app 4 (DEC-184, DEC-236)
  final double cardChoiceTextGap;
  /// Ô nhập: viền nghỉ 1px (DEC-184) (DEC-207)
  final double fieldBorderWidth;
  /// Ô nhập: viền đang gõ và viền lỗi 2px (DEC-184) (DEC-207)
  final double fieldBorderWidthActive;
  /// Ô nhập: rộng mặc định. Web 320; app 361 = 393 − 2 × 16 (DEC-192). Dùng thật thì Fill theo khung (DEC-207)
  final double fieldWidthDefault;
  /// Ô nhập: lề từ mép ô tới khối đầu. Mép chữ = edge-inset + text-inset = 12 web, 16 app; icon đầu, cuối cách mép đúng số này (DEC-184, DEC-192, DEC-196) (DEC-207)
  final double fieldEdgeInset;
  /// Ô nhập: lề trái phải vùng chữ. Web 4 = 12 − 8, app 0 (DEC-184) (DEC-207)
  final double fieldTextInset;
  /// Ô nhập: khoảng icon → vùng chữ; cộng text-inset ra 8 web (DEC-192), 16 app (DEC-196) (DEC-207)
  final double fieldContentGap;
  /// Ô nhập: lề trái dòng gợi ý, dòng lỗi. Web 0 canh mép ô, app 16 thẳng chữ trong ô (DEC-192) (DEC-207)
  final double fieldHintInset;
  /// Ô nhập: rộng tối đa nhãn, để nhãn dài cắt "…" mà dấu * vẫn ngay sau nhãn. 300 ≈ rộng mặc định trừ lề và chỗ cho *; ô hẹp hơn thì chỉnh (DEC-207)
  final double fieldLabelMaxWidth;
  /// Cao thanh tiến độ cỡ SM: thẻ gọn trên app (DEC-243)
  final double progressHeightSm;
  /// Cao thanh tiến độ cỡ MD, mặc định: dòng quy trình web, thẻ tóm tắt (DEC-243)
  final double progressHeightMd;
  /// Khe giữa hai nhóm đoạn của thanh chia đoạn (DEC-243)
  final double progressGap;
  /// Thanh tiến độ: bề rộng mặc định của component. Web 320; app 361 = 393 − 2 × 16 lề màn. Dùng instance thì kéo rộng theo khung (Fill) (DEC-243)
  final double progressWidthDefault;
  /// Rộng mặc định của một đoạn (`.progress / Segment`) khi đặt tự do, chưa nằm trong khung chứa. Trong Base / Progress đoạn luôn Fill hoặc có % rộng nên số này không đổi hình thanh (DEC-243)
  final double progressSegmentWidth;
  /// Ô mã OTP: rộng một ô. App 48 theo bản vẽ account-access 3.4; web 40 là giá trị đề xuất, chưa dựng khối Web (DEC-244)
  final double otpCellWidth;
  /// Popover, menu thả rộng (DEC-259)
  final double widthXs;
  /// Dialog xác nhận, drawer thường (Untitled slideout 400) (DEC-259)
  final double widthSm;
  /// Dialog form, form 1 cột (DEC-259)
  final double widthMd;
  /// Đoạn văn tối đa, dialog lớn (DEC-259)
  final double widthLg;
  /// Drawer rộng (DEC-259)
  final double widthXl;
  /// Khung nội dung tối đa web (DEC-259)
  final double width2xl;
  /// Cao tối thiểu dòng bảng (DEC-259, như Untitled)
  final double tableRowMinHeight;
  /// Lề trên dưới ô bảng
  final double tableCellPaddingY;
  /// Lề trái phải ô bảng
  final double tableCellPaddingX;

  static const web = InvPlatform(
    radiusControl: InvPrimitives.radiusMd,
    radiusField: InvPrimitives.radiusMd,
    radiusCard: InvPrimitives.radiusXl,
    radiusInner: InvPrimitives.radiusMd,
    radiusOverlay: InvPrimitives.radius2xl,
    radiusChip: InvPrimitives.radiusFull,
    radiusMenu: InvPrimitives.radiusMd,
    radiusMenuItem: InvPrimitives.radiusSm,
    radiusBadge: InvPrimitives.radiusSm,
    radiusTab: InvPrimitives.radiusMd,
    spaceInsetXs: InvPrimitives.space4,
    spaceInsetSm: InvPrimitives.space8,
    spaceInsetMd: InvPrimitives.space12,
    spaceInsetLg: InvPrimitives.space16,
    spaceInsetXl: InvPrimitives.space24,
    spaceGapXs: InvPrimitives.space4,
    spaceGapSm: InvPrimitives.space8,
    spaceGapMd: InvPrimitives.space12,
    spaceGapLg: InvPrimitives.space16,
    spaceGapXl: InvPrimitives.space24,
    spaceGap2xl: InvPrimitives.space32,
    layoutScreenInset: InvPrimitives.space32,
    layoutCardPadding: InvPrimitives.space16,
    layoutListGap: InvPrimitives.space8,
    layoutSectionGap: InvPrimitives.space32,
    layoutTitleGap: InvPrimitives.space16,
    layoutEmptyPadding: InvPrimitives.space80,
    layoutContentMaxWidth: 1280.0,
    formFieldGap: InvPrimitives.space16,
    touchMin: 24.0,
    controlHeightSm: 28.0,
    controlHeightMd: 32.0,
    controlHeightLg: 40.0,
    controlPaddingXSm: InvPrimitives.space8,
    controlPaddingXMd: InvPrimitives.space12,
    controlPaddingXLg: InvPrimitives.space16,
    controlPaddingXIconSm: InvPrimitives.space6,
    controlPaddingXIconMd: InvPrimitives.space8,
    controlPaddingXIconLg: InvPrimitives.space12,
    controlIconGap: InvPrimitives.space6,
    tabPaddingX: InvPrimitives.space8,
    tabPaddingXIcon: InvPrimitives.space6,
    tabGap: InvPrimitives.space8,
    navHeight: 64.0,
    navOffsetBottom: InvPrimitives.space8,
    navPaddingX: InvPrimitives.space4,
    navItemPaddingY: InvPrimitives.space4,
    navScanSize: 56.0,
    chipHeight: 24.0,
    chipHeightSm: 22.0,
    chipHeightLg: 28.0,
    chipFontSizeSm: 12.0,
    chipLineHeightSm: 18.0,
    chipLabelMaxWidth: 160.0,
    chipPaddingX: 10.0,
    chipPaddingXSm: InvPrimitives.space8,
    chipPaddingXLg: InvPrimitives.space12,
    chipPaddingXIcon: InvPrimitives.space8,
    chipIconGap: InvPrimitives.space4,
    chipDotGap: InvPrimitives.space6,
    chipDotSize: 8.0,
    avatarSizeSm: 24.0,
    avatarSizeMd: 36.0,
    avatarSizeLg: 48.0,
    avatarStatusSizeSm: 6.0,
    avatarStatusSizeMd: 10.0,
    avatarStatusSizeLg: 12.0,
    avatarEditSizeMd: 20.0,
    avatarEditSizeLg: 24.0,
    avatarSizeXl: 64.0,
    avatarSizeXxl: 88.0,
    avatarStatusSizeXl: 14.0,
    avatarStatusSizeXxl: 16.0,
    avatarEditSizeXl: 28.0,
    avatarEditSizeXxl: 32.0,
    avatarIconSizeSm: 14.0,
    avatarIconSizeMd: 20.0,
    avatarIconSizeLg: 24.0,
    avatarIconSizeXl: 24.0,
    avatarIconSizeXxl: 24.0,
    avatarEditIconSizeMd: 12.0,
    avatarEditIconSizeLg: 14.0,
    avatarEditIconSizeXl: 16.0,
    avatarEditIconSizeXxl: 16.0,
    avatarSpinnerSizeSm: 12.0,
    avatarSpinnerSizeMd: 16.0,
    avatarSpinnerSizeLg: 20.0,
    avatarSpinnerSizeXl: 24.0,
    avatarSpinnerSizeXxl: 28.0,
    avatarGroupOverlapSm: -6.0,
    avatarGroupOverlapMd: -8.0,
    avatarGroupOverlapLg: -12.0,
    avatarRing: 2.0,
    tooltipPaddingX: InvPrimitives.space8,
    tooltipPaddingY: InvPrimitives.space4,
    tooltipRadius: InvPrimitives.radiusMd,
    tooltipMaxWidth: 240.0,
    tooltipOffset: 4.0,
    tooltipArrowW: 8.0,
    tooltipArrowH: 4.0,
    focusWidth: 2.0,
    focusOffset: 2.0,
    typeDisplaySize: 32.0,
    typeDisplayLineHeight: 40.0,
    typeTitle1Size: 24.0,
    typeTitle1LineHeight: 32.0,
    typeTitle2Size: 20.0,
    typeTitle2LineHeight: 28.0,
    typeTitle3Size: 17.0,
    typeTitle3LineHeight: 24.0,
    typeHeadingSize: 14.0,
    typeHeadingLineHeight: 20.0,
    typeBodySize: 14.0,
    typeBodyLineHeight: 20.0,
    typeLabelSize: 14.0,
    typeLabelLineHeight: 20.0,
    typeCaptionSize: 12.0,
    typeCaptionLineHeight: 16.0,
    typeCodeSize: 12.0,
    typeCodeLineHeight: 16.0,
    typeLabelWeight: FontWeight.w500,
    iconSizeSm: 14.0,
    iconSizeMd: 16.0,
    iconSizeLg: 20.0,
    iconSizeChip: 14.0,
    listRowMinHeight: 36.0,
    listRowPaddingX: InvPrimitives.space8,
    listRowPaddingY: InvPrimitives.space8,
    listRowGap: InvPrimitives.space8,
    listRowTextGap: InvPrimitives.space2,
    listRowRadius: InvPrimitives.radiusMd,
    listRowDividerHeight: 1.0,
    listRowValueMaxWidth: 120.0,
    cardPaddingNone: InvPrimitives.space0,
    cardPaddingCompact: InvPrimitives.space12,
    cardPaddingSpacious: InvPrimitives.space24,
    cardRowIconCell: InvPrimitives.space24,
    cardLeadSize: 36.0,
    cardMediaSize: InvPrimitives.space64,
    cardMediaSizeSm: InvPrimitives.space48,
    cardActionGap: InvPrimitives.space8,
    cardBorderWidth: 1.0,
    cardBorderWidthSelected: 2.0,
    cardRowLabelMax: 120.0,
    cardRowMinHeight: InvPrimitives.space24,
    cardCheckSize: InvPrimitives.space20,
    cardCheckRing: 2.0,
    cardRadioSize: 16.0,
    cardRadioRing: 1.5,
    cardRadioOnRing: 5.0,
    cardChoiceTextGap: InvPrimitives.space2,
    fieldBorderWidth: 1.0,
    fieldBorderWidthActive: 2.0,
    fieldWidthDefault: 320.0,
    fieldEdgeInset: InvPrimitives.space8,
    fieldTextInset: InvPrimitives.space4,
    fieldContentGap: InvPrimitives.space4,
    fieldHintInset: InvPrimitives.space0,
    fieldLabelMaxWidth: 300.0,
    progressHeightSm: 4.0,
    progressHeightMd: 6.0,
    progressGap: InvPrimitives.space2,
    progressWidthDefault: 320.0,
    progressSegmentWidth: 24.0,
    otpCellWidth: 40.0,
    widthXs: 320.0,
    widthSm: 400.0,
    widthMd: 560.0,
    widthLg: 720.0,
    widthXl: 960.0,
    width2xl: 1280.0,
    tableRowMinHeight: 52.0,
    tableCellPaddingY: InvPrimitives.space16,
    tableCellPaddingX: InvPrimitives.space24,
  );

  static const mobile = InvPlatform(
    radiusControl: InvPrimitives.radiusFull,
    radiusField: InvPrimitives.radiusXl,
    radiusCard: InvPrimitives.radius2xl,
    radiusInner: InvPrimitives.radiusXl,
    radiusOverlay: InvPrimitives.radius4xl,
    radiusChip: InvPrimitives.radiusFull,
    radiusMenu: InvPrimitives.radiusMd,
    radiusMenuItem: InvPrimitives.radiusSm,
    radiusBadge: InvPrimitives.radiusSm,
    radiusTab: InvPrimitives.radiusFull,
    spaceInsetXs: InvPrimitives.space4,
    spaceInsetSm: InvPrimitives.space8,
    spaceInsetMd: InvPrimitives.space12,
    spaceInsetLg: InvPrimitives.space16,
    spaceInsetXl: InvPrimitives.space24,
    spaceGapXs: InvPrimitives.space4,
    spaceGapSm: InvPrimitives.space8,
    spaceGapMd: InvPrimitives.space12,
    spaceGapLg: InvPrimitives.space16,
    spaceGapXl: InvPrimitives.space24,
    spaceGap2xl: InvPrimitives.space32,
    layoutScreenInset: InvPrimitives.space16,
    layoutCardPadding: InvPrimitives.space16,
    layoutListGap: InvPrimitives.space12,
    layoutSectionGap: InvPrimitives.space24,
    layoutTitleGap: InvPrimitives.space16,
    layoutEmptyPadding: InvPrimitives.space64,
    layoutContentMaxWidth: 393.0,
    formFieldGap: InvPrimitives.space12,
    touchMin: 44.0,
    controlHeightSm: 36.0,
    controlHeightMd: 42.0,
    controlHeightLg: 52.0,
    controlPaddingXSm: InvPrimitives.space12,
    controlPaddingXMd: InvPrimitives.space16,
    controlPaddingXLg: InvPrimitives.space24,
    controlPaddingXIconSm: InvPrimitives.space8,
    controlPaddingXIconMd: InvPrimitives.space12,
    controlPaddingXIconLg: InvPrimitives.space20,
    controlIconGap: InvPrimitives.space8,
    tabPaddingX: InvPrimitives.space16,
    tabPaddingXIcon: InvPrimitives.space12,
    tabGap: InvPrimitives.space8,
    navHeight: 64.0,
    navOffsetBottom: InvPrimitives.space8,
    navPaddingX: InvPrimitives.space4,
    navItemPaddingY: InvPrimitives.space4,
    navScanSize: 56.0,
    chipHeight: 24.0,
    chipHeightSm: 22.0,
    chipHeightLg: 28.0,
    chipFontSizeSm: 12.0,
    chipLineHeightSm: 18.0,
    chipLabelMaxWidth: 160.0,
    chipPaddingX: 10.0,
    chipPaddingXSm: InvPrimitives.space8,
    chipPaddingXLg: InvPrimitives.space12,
    chipPaddingXIcon: InvPrimitives.space8,
    chipIconGap: InvPrimitives.space4,
    chipDotGap: InvPrimitives.space6,
    chipDotSize: 8.0,
    avatarSizeSm: 24.0,
    avatarSizeMd: 36.0,
    avatarSizeLg: 48.0,
    avatarStatusSizeSm: 6.0,
    avatarStatusSizeMd: 10.0,
    avatarStatusSizeLg: 12.0,
    avatarEditSizeMd: 20.0,
    avatarEditSizeLg: 24.0,
    avatarSizeXl: 64.0,
    avatarSizeXxl: 88.0,
    avatarStatusSizeXl: 14.0,
    avatarStatusSizeXxl: 16.0,
    avatarEditSizeXl: 28.0,
    avatarEditSizeXxl: 32.0,
    avatarIconSizeSm: 14.0,
    avatarIconSizeMd: 20.0,
    avatarIconSizeLg: 24.0,
    avatarIconSizeXl: 24.0,
    avatarIconSizeXxl: 24.0,
    avatarEditIconSizeMd: 12.0,
    avatarEditIconSizeLg: 14.0,
    avatarEditIconSizeXl: 16.0,
    avatarEditIconSizeXxl: 16.0,
    avatarSpinnerSizeSm: 12.0,
    avatarSpinnerSizeMd: 16.0,
    avatarSpinnerSizeLg: 20.0,
    avatarSpinnerSizeXl: 24.0,
    avatarSpinnerSizeXxl: 28.0,
    avatarGroupOverlapSm: -6.0,
    avatarGroupOverlapMd: -8.0,
    avatarGroupOverlapLg: -12.0,
    avatarRing: 2.0,
    tooltipPaddingX: InvPrimitives.space8,
    tooltipPaddingY: InvPrimitives.space4,
    tooltipRadius: InvPrimitives.radiusMd,
    tooltipMaxWidth: 240.0,
    tooltipOffset: 4.0,
    tooltipArrowW: 8.0,
    tooltipArrowH: 4.0,
    focusWidth: 2.0,
    focusOffset: 2.0,
    typeDisplaySize: 34.0,
    typeDisplayLineHeight: 40.0,
    typeTitle1Size: 28.0,
    typeTitle1LineHeight: 34.0,
    typeTitle2Size: 22.0,
    typeTitle2LineHeight: 28.0,
    typeTitle3Size: 17.0,
    typeTitle3LineHeight: 22.0,
    typeHeadingSize: 15.0,
    typeHeadingLineHeight: 20.0,
    typeBodySize: 15.0,
    typeBodyLineHeight: 22.0,
    typeLabelSize: 15.0,
    typeLabelLineHeight: 20.0,
    typeCaptionSize: 13.0,
    typeCaptionLineHeight: 18.0,
    typeCodeSize: 13.0,
    typeCodeLineHeight: 18.0,
    typeLabelWeight: FontWeight.w600,
    iconSizeSm: 16.0,
    iconSizeMd: 20.0,
    iconSizeLg: 24.0,
    iconSizeChip: 14.0,
    listRowMinHeight: 52.0,
    listRowPaddingX: InvPrimitives.space12,
    listRowPaddingY: InvPrimitives.space12,
    listRowGap: InvPrimitives.space12,
    listRowTextGap: InvPrimitives.space2,
    listRowRadius: InvPrimitives.radiusMd,
    listRowDividerHeight: 1.0,
    listRowValueMaxWidth: 120.0,
    cardPaddingNone: InvPrimitives.space0,
    cardPaddingCompact: InvPrimitives.space12,
    cardPaddingSpacious: InvPrimitives.space24,
    cardRowIconCell: InvPrimitives.space24,
    cardLeadSize: 36.0,
    cardMediaSize: InvPrimitives.space64,
    cardMediaSizeSm: InvPrimitives.space48,
    cardActionGap: InvPrimitives.space12,
    cardBorderWidth: 1.0,
    cardBorderWidthSelected: 2.0,
    cardRowLabelMax: 120.0,
    cardRowMinHeight: InvPrimitives.space24,
    cardCheckSize: InvPrimitives.space20,
    cardCheckRing: 2.0,
    cardRadioSize: InvPrimitives.space20,
    cardRadioRing: 1.5,
    cardRadioOnRing: 6.0,
    cardChoiceTextGap: InvPrimitives.space4,
    fieldBorderWidth: 1.0,
    fieldBorderWidthActive: 2.0,
    fieldWidthDefault: 361.0,
    fieldEdgeInset: InvPrimitives.space16,
    fieldTextInset: InvPrimitives.space0,
    fieldContentGap: InvPrimitives.space16,
    fieldHintInset: InvPrimitives.space16,
    fieldLabelMaxWidth: 300.0,
    progressHeightSm: 4.0,
    progressHeightMd: 6.0,
    progressGap: InvPrimitives.space2,
    progressWidthDefault: 361.0,
    progressSegmentWidth: 24.0,
    otpCellWidth: 48.0,
    widthXs: 320.0,
    widthSm: 400.0,
    widthMd: 560.0,
    widthLg: 720.0,
    widthXl: 960.0,
    width2xl: 1280.0,
    tableRowMinHeight: 52.0,
    tableCellPaddingY: InvPrimitives.space12,
    tableCellPaddingX: InvPrimitives.space16,
  );

  @override
  InvPlatform copyWith({double? radiusControl, double? radiusField, double? radiusCard, double? radiusInner, double? radiusOverlay, double? radiusChip, double? radiusMenu, double? radiusMenuItem, double? radiusBadge, double? radiusTab, double? spaceInsetXs, double? spaceInsetSm, double? spaceInsetMd, double? spaceInsetLg, double? spaceInsetXl, double? spaceGapXs, double? spaceGapSm, double? spaceGapMd, double? spaceGapLg, double? spaceGapXl, double? spaceGap2xl, double? layoutScreenInset, double? layoutCardPadding, double? layoutListGap, double? layoutSectionGap, double? layoutTitleGap, double? layoutEmptyPadding, double? layoutContentMaxWidth, double? formFieldGap, double? touchMin, double? controlHeightSm, double? controlHeightMd, double? controlHeightLg, double? controlPaddingXSm, double? controlPaddingXMd, double? controlPaddingXLg, double? controlPaddingXIconSm, double? controlPaddingXIconMd, double? controlPaddingXIconLg, double? controlIconGap, double? tabPaddingX, double? tabPaddingXIcon, double? tabGap, double? navHeight, double? navOffsetBottom, double? navPaddingX, double? navItemPaddingY, double? navScanSize, double? chipHeight, double? chipHeightSm, double? chipHeightLg, double? chipFontSizeSm, double? chipLineHeightSm, double? chipLabelMaxWidth, double? chipPaddingX, double? chipPaddingXSm, double? chipPaddingXLg, double? chipPaddingXIcon, double? chipIconGap, double? chipDotGap, double? chipDotSize, double? avatarSizeSm, double? avatarSizeMd, double? avatarSizeLg, double? avatarStatusSizeSm, double? avatarStatusSizeMd, double? avatarStatusSizeLg, double? avatarEditSizeMd, double? avatarEditSizeLg, double? avatarSizeXl, double? avatarSizeXxl, double? avatarStatusSizeXl, double? avatarStatusSizeXxl, double? avatarEditSizeXl, double? avatarEditSizeXxl, double? avatarIconSizeSm, double? avatarIconSizeMd, double? avatarIconSizeLg, double? avatarIconSizeXl, double? avatarIconSizeXxl, double? avatarEditIconSizeMd, double? avatarEditIconSizeLg, double? avatarEditIconSizeXl, double? avatarEditIconSizeXxl, double? avatarSpinnerSizeSm, double? avatarSpinnerSizeMd, double? avatarSpinnerSizeLg, double? avatarSpinnerSizeXl, double? avatarSpinnerSizeXxl, double? avatarGroupOverlapSm, double? avatarGroupOverlapMd, double? avatarGroupOverlapLg, double? avatarRing, double? tooltipPaddingX, double? tooltipPaddingY, double? tooltipRadius, double? tooltipMaxWidth, double? tooltipOffset, double? tooltipArrowW, double? tooltipArrowH, double? focusWidth, double? focusOffset, double? typeDisplaySize, double? typeDisplayLineHeight, double? typeTitle1Size, double? typeTitle1LineHeight, double? typeTitle2Size, double? typeTitle2LineHeight, double? typeTitle3Size, double? typeTitle3LineHeight, double? typeHeadingSize, double? typeHeadingLineHeight, double? typeBodySize, double? typeBodyLineHeight, double? typeLabelSize, double? typeLabelLineHeight, double? typeCaptionSize, double? typeCaptionLineHeight, double? typeCodeSize, double? typeCodeLineHeight, FontWeight? typeLabelWeight, double? iconSizeSm, double? iconSizeMd, double? iconSizeLg, double? iconSizeChip, double? listRowMinHeight, double? listRowPaddingX, double? listRowPaddingY, double? listRowGap, double? listRowTextGap, double? listRowRadius, double? listRowDividerHeight, double? listRowValueMaxWidth, double? cardPaddingNone, double? cardPaddingCompact, double? cardPaddingSpacious, double? cardRowIconCell, double? cardLeadSize, double? cardMediaSize, double? cardMediaSizeSm, double? cardActionGap, double? cardBorderWidth, double? cardBorderWidthSelected, double? cardRowLabelMax, double? cardRowMinHeight, double? cardCheckSize, double? cardCheckRing, double? cardRadioSize, double? cardRadioRing, double? cardRadioOnRing, double? cardChoiceTextGap, double? fieldBorderWidth, double? fieldBorderWidthActive, double? fieldWidthDefault, double? fieldEdgeInset, double? fieldTextInset, double? fieldContentGap, double? fieldHintInset, double? fieldLabelMaxWidth, double? progressHeightSm, double? progressHeightMd, double? progressGap, double? progressWidthDefault, double? progressSegmentWidth, double? otpCellWidth, double? widthXs, double? widthSm, double? widthMd, double? widthLg, double? widthXl, double? width2xl, double? tableRowMinHeight, double? tableCellPaddingY, double? tableCellPaddingX}) =>
      InvPlatform(radiusControl: radiusControl ?? this.radiusControl, radiusField: radiusField ?? this.radiusField, radiusCard: radiusCard ?? this.radiusCard, radiusInner: radiusInner ?? this.radiusInner, radiusOverlay: radiusOverlay ?? this.radiusOverlay, radiusChip: radiusChip ?? this.radiusChip, radiusMenu: radiusMenu ?? this.radiusMenu, radiusMenuItem: radiusMenuItem ?? this.radiusMenuItem, radiusBadge: radiusBadge ?? this.radiusBadge, radiusTab: radiusTab ?? this.radiusTab, spaceInsetXs: spaceInsetXs ?? this.spaceInsetXs, spaceInsetSm: spaceInsetSm ?? this.spaceInsetSm, spaceInsetMd: spaceInsetMd ?? this.spaceInsetMd, spaceInsetLg: spaceInsetLg ?? this.spaceInsetLg, spaceInsetXl: spaceInsetXl ?? this.spaceInsetXl, spaceGapXs: spaceGapXs ?? this.spaceGapXs, spaceGapSm: spaceGapSm ?? this.spaceGapSm, spaceGapMd: spaceGapMd ?? this.spaceGapMd, spaceGapLg: spaceGapLg ?? this.spaceGapLg, spaceGapXl: spaceGapXl ?? this.spaceGapXl, spaceGap2xl: spaceGap2xl ?? this.spaceGap2xl, layoutScreenInset: layoutScreenInset ?? this.layoutScreenInset, layoutCardPadding: layoutCardPadding ?? this.layoutCardPadding, layoutListGap: layoutListGap ?? this.layoutListGap, layoutSectionGap: layoutSectionGap ?? this.layoutSectionGap, layoutTitleGap: layoutTitleGap ?? this.layoutTitleGap, layoutEmptyPadding: layoutEmptyPadding ?? this.layoutEmptyPadding, layoutContentMaxWidth: layoutContentMaxWidth ?? this.layoutContentMaxWidth, formFieldGap: formFieldGap ?? this.formFieldGap, touchMin: touchMin ?? this.touchMin, controlHeightSm: controlHeightSm ?? this.controlHeightSm, controlHeightMd: controlHeightMd ?? this.controlHeightMd, controlHeightLg: controlHeightLg ?? this.controlHeightLg, controlPaddingXSm: controlPaddingXSm ?? this.controlPaddingXSm, controlPaddingXMd: controlPaddingXMd ?? this.controlPaddingXMd, controlPaddingXLg: controlPaddingXLg ?? this.controlPaddingXLg, controlPaddingXIconSm: controlPaddingXIconSm ?? this.controlPaddingXIconSm, controlPaddingXIconMd: controlPaddingXIconMd ?? this.controlPaddingXIconMd, controlPaddingXIconLg: controlPaddingXIconLg ?? this.controlPaddingXIconLg, controlIconGap: controlIconGap ?? this.controlIconGap, tabPaddingX: tabPaddingX ?? this.tabPaddingX, tabPaddingXIcon: tabPaddingXIcon ?? this.tabPaddingXIcon, tabGap: tabGap ?? this.tabGap, navHeight: navHeight ?? this.navHeight, navOffsetBottom: navOffsetBottom ?? this.navOffsetBottom, navPaddingX: navPaddingX ?? this.navPaddingX, navItemPaddingY: navItemPaddingY ?? this.navItemPaddingY, navScanSize: navScanSize ?? this.navScanSize, chipHeight: chipHeight ?? this.chipHeight, chipHeightSm: chipHeightSm ?? this.chipHeightSm, chipHeightLg: chipHeightLg ?? this.chipHeightLg, chipFontSizeSm: chipFontSizeSm ?? this.chipFontSizeSm, chipLineHeightSm: chipLineHeightSm ?? this.chipLineHeightSm, chipLabelMaxWidth: chipLabelMaxWidth ?? this.chipLabelMaxWidth, chipPaddingX: chipPaddingX ?? this.chipPaddingX, chipPaddingXSm: chipPaddingXSm ?? this.chipPaddingXSm, chipPaddingXLg: chipPaddingXLg ?? this.chipPaddingXLg, chipPaddingXIcon: chipPaddingXIcon ?? this.chipPaddingXIcon, chipIconGap: chipIconGap ?? this.chipIconGap, chipDotGap: chipDotGap ?? this.chipDotGap, chipDotSize: chipDotSize ?? this.chipDotSize, avatarSizeSm: avatarSizeSm ?? this.avatarSizeSm, avatarSizeMd: avatarSizeMd ?? this.avatarSizeMd, avatarSizeLg: avatarSizeLg ?? this.avatarSizeLg, avatarStatusSizeSm: avatarStatusSizeSm ?? this.avatarStatusSizeSm, avatarStatusSizeMd: avatarStatusSizeMd ?? this.avatarStatusSizeMd, avatarStatusSizeLg: avatarStatusSizeLg ?? this.avatarStatusSizeLg, avatarEditSizeMd: avatarEditSizeMd ?? this.avatarEditSizeMd, avatarEditSizeLg: avatarEditSizeLg ?? this.avatarEditSizeLg, avatarSizeXl: avatarSizeXl ?? this.avatarSizeXl, avatarSizeXxl: avatarSizeXxl ?? this.avatarSizeXxl, avatarStatusSizeXl: avatarStatusSizeXl ?? this.avatarStatusSizeXl, avatarStatusSizeXxl: avatarStatusSizeXxl ?? this.avatarStatusSizeXxl, avatarEditSizeXl: avatarEditSizeXl ?? this.avatarEditSizeXl, avatarEditSizeXxl: avatarEditSizeXxl ?? this.avatarEditSizeXxl, avatarIconSizeSm: avatarIconSizeSm ?? this.avatarIconSizeSm, avatarIconSizeMd: avatarIconSizeMd ?? this.avatarIconSizeMd, avatarIconSizeLg: avatarIconSizeLg ?? this.avatarIconSizeLg, avatarIconSizeXl: avatarIconSizeXl ?? this.avatarIconSizeXl, avatarIconSizeXxl: avatarIconSizeXxl ?? this.avatarIconSizeXxl, avatarEditIconSizeMd: avatarEditIconSizeMd ?? this.avatarEditIconSizeMd, avatarEditIconSizeLg: avatarEditIconSizeLg ?? this.avatarEditIconSizeLg, avatarEditIconSizeXl: avatarEditIconSizeXl ?? this.avatarEditIconSizeXl, avatarEditIconSizeXxl: avatarEditIconSizeXxl ?? this.avatarEditIconSizeXxl, avatarSpinnerSizeSm: avatarSpinnerSizeSm ?? this.avatarSpinnerSizeSm, avatarSpinnerSizeMd: avatarSpinnerSizeMd ?? this.avatarSpinnerSizeMd, avatarSpinnerSizeLg: avatarSpinnerSizeLg ?? this.avatarSpinnerSizeLg, avatarSpinnerSizeXl: avatarSpinnerSizeXl ?? this.avatarSpinnerSizeXl, avatarSpinnerSizeXxl: avatarSpinnerSizeXxl ?? this.avatarSpinnerSizeXxl, avatarGroupOverlapSm: avatarGroupOverlapSm ?? this.avatarGroupOverlapSm, avatarGroupOverlapMd: avatarGroupOverlapMd ?? this.avatarGroupOverlapMd, avatarGroupOverlapLg: avatarGroupOverlapLg ?? this.avatarGroupOverlapLg, avatarRing: avatarRing ?? this.avatarRing, tooltipPaddingX: tooltipPaddingX ?? this.tooltipPaddingX, tooltipPaddingY: tooltipPaddingY ?? this.tooltipPaddingY, tooltipRadius: tooltipRadius ?? this.tooltipRadius, tooltipMaxWidth: tooltipMaxWidth ?? this.tooltipMaxWidth, tooltipOffset: tooltipOffset ?? this.tooltipOffset, tooltipArrowW: tooltipArrowW ?? this.tooltipArrowW, tooltipArrowH: tooltipArrowH ?? this.tooltipArrowH, focusWidth: focusWidth ?? this.focusWidth, focusOffset: focusOffset ?? this.focusOffset, typeDisplaySize: typeDisplaySize ?? this.typeDisplaySize, typeDisplayLineHeight: typeDisplayLineHeight ?? this.typeDisplayLineHeight, typeTitle1Size: typeTitle1Size ?? this.typeTitle1Size, typeTitle1LineHeight: typeTitle1LineHeight ?? this.typeTitle1LineHeight, typeTitle2Size: typeTitle2Size ?? this.typeTitle2Size, typeTitle2LineHeight: typeTitle2LineHeight ?? this.typeTitle2LineHeight, typeTitle3Size: typeTitle3Size ?? this.typeTitle3Size, typeTitle3LineHeight: typeTitle3LineHeight ?? this.typeTitle3LineHeight, typeHeadingSize: typeHeadingSize ?? this.typeHeadingSize, typeHeadingLineHeight: typeHeadingLineHeight ?? this.typeHeadingLineHeight, typeBodySize: typeBodySize ?? this.typeBodySize, typeBodyLineHeight: typeBodyLineHeight ?? this.typeBodyLineHeight, typeLabelSize: typeLabelSize ?? this.typeLabelSize, typeLabelLineHeight: typeLabelLineHeight ?? this.typeLabelLineHeight, typeCaptionSize: typeCaptionSize ?? this.typeCaptionSize, typeCaptionLineHeight: typeCaptionLineHeight ?? this.typeCaptionLineHeight, typeCodeSize: typeCodeSize ?? this.typeCodeSize, typeCodeLineHeight: typeCodeLineHeight ?? this.typeCodeLineHeight, typeLabelWeight: typeLabelWeight ?? this.typeLabelWeight, iconSizeSm: iconSizeSm ?? this.iconSizeSm, iconSizeMd: iconSizeMd ?? this.iconSizeMd, iconSizeLg: iconSizeLg ?? this.iconSizeLg, iconSizeChip: iconSizeChip ?? this.iconSizeChip, listRowMinHeight: listRowMinHeight ?? this.listRowMinHeight, listRowPaddingX: listRowPaddingX ?? this.listRowPaddingX, listRowPaddingY: listRowPaddingY ?? this.listRowPaddingY, listRowGap: listRowGap ?? this.listRowGap, listRowTextGap: listRowTextGap ?? this.listRowTextGap, listRowRadius: listRowRadius ?? this.listRowRadius, listRowDividerHeight: listRowDividerHeight ?? this.listRowDividerHeight, listRowValueMaxWidth: listRowValueMaxWidth ?? this.listRowValueMaxWidth, cardPaddingNone: cardPaddingNone ?? this.cardPaddingNone, cardPaddingCompact: cardPaddingCompact ?? this.cardPaddingCompact, cardPaddingSpacious: cardPaddingSpacious ?? this.cardPaddingSpacious, cardRowIconCell: cardRowIconCell ?? this.cardRowIconCell, cardLeadSize: cardLeadSize ?? this.cardLeadSize, cardMediaSize: cardMediaSize ?? this.cardMediaSize, cardMediaSizeSm: cardMediaSizeSm ?? this.cardMediaSizeSm, cardActionGap: cardActionGap ?? this.cardActionGap, cardBorderWidth: cardBorderWidth ?? this.cardBorderWidth, cardBorderWidthSelected: cardBorderWidthSelected ?? this.cardBorderWidthSelected, cardRowLabelMax: cardRowLabelMax ?? this.cardRowLabelMax, cardRowMinHeight: cardRowMinHeight ?? this.cardRowMinHeight, cardCheckSize: cardCheckSize ?? this.cardCheckSize, cardCheckRing: cardCheckRing ?? this.cardCheckRing, cardRadioSize: cardRadioSize ?? this.cardRadioSize, cardRadioRing: cardRadioRing ?? this.cardRadioRing, cardRadioOnRing: cardRadioOnRing ?? this.cardRadioOnRing, cardChoiceTextGap: cardChoiceTextGap ?? this.cardChoiceTextGap, fieldBorderWidth: fieldBorderWidth ?? this.fieldBorderWidth, fieldBorderWidthActive: fieldBorderWidthActive ?? this.fieldBorderWidthActive, fieldWidthDefault: fieldWidthDefault ?? this.fieldWidthDefault, fieldEdgeInset: fieldEdgeInset ?? this.fieldEdgeInset, fieldTextInset: fieldTextInset ?? this.fieldTextInset, fieldContentGap: fieldContentGap ?? this.fieldContentGap, fieldHintInset: fieldHintInset ?? this.fieldHintInset, fieldLabelMaxWidth: fieldLabelMaxWidth ?? this.fieldLabelMaxWidth, progressHeightSm: progressHeightSm ?? this.progressHeightSm, progressHeightMd: progressHeightMd ?? this.progressHeightMd, progressGap: progressGap ?? this.progressGap, progressWidthDefault: progressWidthDefault ?? this.progressWidthDefault, progressSegmentWidth: progressSegmentWidth ?? this.progressSegmentWidth, otpCellWidth: otpCellWidth ?? this.otpCellWidth, widthXs: widthXs ?? this.widthXs, widthSm: widthSm ?? this.widthSm, widthMd: widthMd ?? this.widthMd, widthLg: widthLg ?? this.widthLg, widthXl: widthXl ?? this.widthXl, width2xl: width2xl ?? this.width2xl, tableRowMinHeight: tableRowMinHeight ?? this.tableRowMinHeight, tableCellPaddingY: tableCellPaddingY ?? this.tableCellPaddingY, tableCellPaddingX: tableCellPaddingX ?? this.tableCellPaddingX);

  @override
  InvPlatform lerp(covariant ThemeExtension<InvPlatform>? other, double t) {
    if (other is! InvPlatform) return this;
    return InvPlatform(radiusControl: lerpDouble(radiusControl, other.radiusControl, t), radiusField: lerpDouble(radiusField, other.radiusField, t), radiusCard: lerpDouble(radiusCard, other.radiusCard, t), radiusInner: lerpDouble(radiusInner, other.radiusInner, t), radiusOverlay: lerpDouble(radiusOverlay, other.radiusOverlay, t), radiusChip: lerpDouble(radiusChip, other.radiusChip, t), radiusMenu: lerpDouble(radiusMenu, other.radiusMenu, t), radiusMenuItem: lerpDouble(radiusMenuItem, other.radiusMenuItem, t), radiusBadge: lerpDouble(radiusBadge, other.radiusBadge, t), radiusTab: lerpDouble(radiusTab, other.radiusTab, t), spaceInsetXs: lerpDouble(spaceInsetXs, other.spaceInsetXs, t), spaceInsetSm: lerpDouble(spaceInsetSm, other.spaceInsetSm, t), spaceInsetMd: lerpDouble(spaceInsetMd, other.spaceInsetMd, t), spaceInsetLg: lerpDouble(spaceInsetLg, other.spaceInsetLg, t), spaceInsetXl: lerpDouble(spaceInsetXl, other.spaceInsetXl, t), spaceGapXs: lerpDouble(spaceGapXs, other.spaceGapXs, t), spaceGapSm: lerpDouble(spaceGapSm, other.spaceGapSm, t), spaceGapMd: lerpDouble(spaceGapMd, other.spaceGapMd, t), spaceGapLg: lerpDouble(spaceGapLg, other.spaceGapLg, t), spaceGapXl: lerpDouble(spaceGapXl, other.spaceGapXl, t), spaceGap2xl: lerpDouble(spaceGap2xl, other.spaceGap2xl, t), layoutScreenInset: lerpDouble(layoutScreenInset, other.layoutScreenInset, t), layoutCardPadding: lerpDouble(layoutCardPadding, other.layoutCardPadding, t), layoutListGap: lerpDouble(layoutListGap, other.layoutListGap, t), layoutSectionGap: lerpDouble(layoutSectionGap, other.layoutSectionGap, t), layoutTitleGap: lerpDouble(layoutTitleGap, other.layoutTitleGap, t), layoutEmptyPadding: lerpDouble(layoutEmptyPadding, other.layoutEmptyPadding, t), layoutContentMaxWidth: lerpDouble(layoutContentMaxWidth, other.layoutContentMaxWidth, t), formFieldGap: lerpDouble(formFieldGap, other.formFieldGap, t), touchMin: lerpDouble(touchMin, other.touchMin, t), controlHeightSm: lerpDouble(controlHeightSm, other.controlHeightSm, t), controlHeightMd: lerpDouble(controlHeightMd, other.controlHeightMd, t), controlHeightLg: lerpDouble(controlHeightLg, other.controlHeightLg, t), controlPaddingXSm: lerpDouble(controlPaddingXSm, other.controlPaddingXSm, t), controlPaddingXMd: lerpDouble(controlPaddingXMd, other.controlPaddingXMd, t), controlPaddingXLg: lerpDouble(controlPaddingXLg, other.controlPaddingXLg, t), controlPaddingXIconSm: lerpDouble(controlPaddingXIconSm, other.controlPaddingXIconSm, t), controlPaddingXIconMd: lerpDouble(controlPaddingXIconMd, other.controlPaddingXIconMd, t), controlPaddingXIconLg: lerpDouble(controlPaddingXIconLg, other.controlPaddingXIconLg, t), controlIconGap: lerpDouble(controlIconGap, other.controlIconGap, t), tabPaddingX: lerpDouble(tabPaddingX, other.tabPaddingX, t), tabPaddingXIcon: lerpDouble(tabPaddingXIcon, other.tabPaddingXIcon, t), tabGap: lerpDouble(tabGap, other.tabGap, t), navHeight: lerpDouble(navHeight, other.navHeight, t), navOffsetBottom: lerpDouble(navOffsetBottom, other.navOffsetBottom, t), navPaddingX: lerpDouble(navPaddingX, other.navPaddingX, t), navItemPaddingY: lerpDouble(navItemPaddingY, other.navItemPaddingY, t), navScanSize: lerpDouble(navScanSize, other.navScanSize, t), chipHeight: lerpDouble(chipHeight, other.chipHeight, t), chipHeightSm: lerpDouble(chipHeightSm, other.chipHeightSm, t), chipHeightLg: lerpDouble(chipHeightLg, other.chipHeightLg, t), chipFontSizeSm: lerpDouble(chipFontSizeSm, other.chipFontSizeSm, t), chipLineHeightSm: lerpDouble(chipLineHeightSm, other.chipLineHeightSm, t), chipLabelMaxWidth: lerpDouble(chipLabelMaxWidth, other.chipLabelMaxWidth, t), chipPaddingX: lerpDouble(chipPaddingX, other.chipPaddingX, t), chipPaddingXSm: lerpDouble(chipPaddingXSm, other.chipPaddingXSm, t), chipPaddingXLg: lerpDouble(chipPaddingXLg, other.chipPaddingXLg, t), chipPaddingXIcon: lerpDouble(chipPaddingXIcon, other.chipPaddingXIcon, t), chipIconGap: lerpDouble(chipIconGap, other.chipIconGap, t), chipDotGap: lerpDouble(chipDotGap, other.chipDotGap, t), chipDotSize: lerpDouble(chipDotSize, other.chipDotSize, t), avatarSizeSm: lerpDouble(avatarSizeSm, other.avatarSizeSm, t), avatarSizeMd: lerpDouble(avatarSizeMd, other.avatarSizeMd, t), avatarSizeLg: lerpDouble(avatarSizeLg, other.avatarSizeLg, t), avatarStatusSizeSm: lerpDouble(avatarStatusSizeSm, other.avatarStatusSizeSm, t), avatarStatusSizeMd: lerpDouble(avatarStatusSizeMd, other.avatarStatusSizeMd, t), avatarStatusSizeLg: lerpDouble(avatarStatusSizeLg, other.avatarStatusSizeLg, t), avatarEditSizeMd: lerpDouble(avatarEditSizeMd, other.avatarEditSizeMd, t), avatarEditSizeLg: lerpDouble(avatarEditSizeLg, other.avatarEditSizeLg, t), avatarSizeXl: lerpDouble(avatarSizeXl, other.avatarSizeXl, t), avatarSizeXxl: lerpDouble(avatarSizeXxl, other.avatarSizeXxl, t), avatarStatusSizeXl: lerpDouble(avatarStatusSizeXl, other.avatarStatusSizeXl, t), avatarStatusSizeXxl: lerpDouble(avatarStatusSizeXxl, other.avatarStatusSizeXxl, t), avatarEditSizeXl: lerpDouble(avatarEditSizeXl, other.avatarEditSizeXl, t), avatarEditSizeXxl: lerpDouble(avatarEditSizeXxl, other.avatarEditSizeXxl, t), avatarIconSizeSm: lerpDouble(avatarIconSizeSm, other.avatarIconSizeSm, t), avatarIconSizeMd: lerpDouble(avatarIconSizeMd, other.avatarIconSizeMd, t), avatarIconSizeLg: lerpDouble(avatarIconSizeLg, other.avatarIconSizeLg, t), avatarIconSizeXl: lerpDouble(avatarIconSizeXl, other.avatarIconSizeXl, t), avatarIconSizeXxl: lerpDouble(avatarIconSizeXxl, other.avatarIconSizeXxl, t), avatarEditIconSizeMd: lerpDouble(avatarEditIconSizeMd, other.avatarEditIconSizeMd, t), avatarEditIconSizeLg: lerpDouble(avatarEditIconSizeLg, other.avatarEditIconSizeLg, t), avatarEditIconSizeXl: lerpDouble(avatarEditIconSizeXl, other.avatarEditIconSizeXl, t), avatarEditIconSizeXxl: lerpDouble(avatarEditIconSizeXxl, other.avatarEditIconSizeXxl, t), avatarSpinnerSizeSm: lerpDouble(avatarSpinnerSizeSm, other.avatarSpinnerSizeSm, t), avatarSpinnerSizeMd: lerpDouble(avatarSpinnerSizeMd, other.avatarSpinnerSizeMd, t), avatarSpinnerSizeLg: lerpDouble(avatarSpinnerSizeLg, other.avatarSpinnerSizeLg, t), avatarSpinnerSizeXl: lerpDouble(avatarSpinnerSizeXl, other.avatarSpinnerSizeXl, t), avatarSpinnerSizeXxl: lerpDouble(avatarSpinnerSizeXxl, other.avatarSpinnerSizeXxl, t), avatarGroupOverlapSm: lerpDouble(avatarGroupOverlapSm, other.avatarGroupOverlapSm, t), avatarGroupOverlapMd: lerpDouble(avatarGroupOverlapMd, other.avatarGroupOverlapMd, t), avatarGroupOverlapLg: lerpDouble(avatarGroupOverlapLg, other.avatarGroupOverlapLg, t), avatarRing: lerpDouble(avatarRing, other.avatarRing, t), tooltipPaddingX: lerpDouble(tooltipPaddingX, other.tooltipPaddingX, t), tooltipPaddingY: lerpDouble(tooltipPaddingY, other.tooltipPaddingY, t), tooltipRadius: lerpDouble(tooltipRadius, other.tooltipRadius, t), tooltipMaxWidth: lerpDouble(tooltipMaxWidth, other.tooltipMaxWidth, t), tooltipOffset: lerpDouble(tooltipOffset, other.tooltipOffset, t), tooltipArrowW: lerpDouble(tooltipArrowW, other.tooltipArrowW, t), tooltipArrowH: lerpDouble(tooltipArrowH, other.tooltipArrowH, t), focusWidth: lerpDouble(focusWidth, other.focusWidth, t), focusOffset: lerpDouble(focusOffset, other.focusOffset, t), typeDisplaySize: lerpDouble(typeDisplaySize, other.typeDisplaySize, t), typeDisplayLineHeight: lerpDouble(typeDisplayLineHeight, other.typeDisplayLineHeight, t), typeTitle1Size: lerpDouble(typeTitle1Size, other.typeTitle1Size, t), typeTitle1LineHeight: lerpDouble(typeTitle1LineHeight, other.typeTitle1LineHeight, t), typeTitle2Size: lerpDouble(typeTitle2Size, other.typeTitle2Size, t), typeTitle2LineHeight: lerpDouble(typeTitle2LineHeight, other.typeTitle2LineHeight, t), typeTitle3Size: lerpDouble(typeTitle3Size, other.typeTitle3Size, t), typeTitle3LineHeight: lerpDouble(typeTitle3LineHeight, other.typeTitle3LineHeight, t), typeHeadingSize: lerpDouble(typeHeadingSize, other.typeHeadingSize, t), typeHeadingLineHeight: lerpDouble(typeHeadingLineHeight, other.typeHeadingLineHeight, t), typeBodySize: lerpDouble(typeBodySize, other.typeBodySize, t), typeBodyLineHeight: lerpDouble(typeBodyLineHeight, other.typeBodyLineHeight, t), typeLabelSize: lerpDouble(typeLabelSize, other.typeLabelSize, t), typeLabelLineHeight: lerpDouble(typeLabelLineHeight, other.typeLabelLineHeight, t), typeCaptionSize: lerpDouble(typeCaptionSize, other.typeCaptionSize, t), typeCaptionLineHeight: lerpDouble(typeCaptionLineHeight, other.typeCaptionLineHeight, t), typeCodeSize: lerpDouble(typeCodeSize, other.typeCodeSize, t), typeCodeLineHeight: lerpDouble(typeCodeLineHeight, other.typeCodeLineHeight, t), typeLabelWeight: t < 0.5 ? typeLabelWeight : other.typeLabelWeight, iconSizeSm: lerpDouble(iconSizeSm, other.iconSizeSm, t), iconSizeMd: lerpDouble(iconSizeMd, other.iconSizeMd, t), iconSizeLg: lerpDouble(iconSizeLg, other.iconSizeLg, t), iconSizeChip: lerpDouble(iconSizeChip, other.iconSizeChip, t), listRowMinHeight: lerpDouble(listRowMinHeight, other.listRowMinHeight, t), listRowPaddingX: lerpDouble(listRowPaddingX, other.listRowPaddingX, t), listRowPaddingY: lerpDouble(listRowPaddingY, other.listRowPaddingY, t), listRowGap: lerpDouble(listRowGap, other.listRowGap, t), listRowTextGap: lerpDouble(listRowTextGap, other.listRowTextGap, t), listRowRadius: lerpDouble(listRowRadius, other.listRowRadius, t), listRowDividerHeight: lerpDouble(listRowDividerHeight, other.listRowDividerHeight, t), listRowValueMaxWidth: lerpDouble(listRowValueMaxWidth, other.listRowValueMaxWidth, t), cardPaddingNone: lerpDouble(cardPaddingNone, other.cardPaddingNone, t), cardPaddingCompact: lerpDouble(cardPaddingCompact, other.cardPaddingCompact, t), cardPaddingSpacious: lerpDouble(cardPaddingSpacious, other.cardPaddingSpacious, t), cardRowIconCell: lerpDouble(cardRowIconCell, other.cardRowIconCell, t), cardLeadSize: lerpDouble(cardLeadSize, other.cardLeadSize, t), cardMediaSize: lerpDouble(cardMediaSize, other.cardMediaSize, t), cardMediaSizeSm: lerpDouble(cardMediaSizeSm, other.cardMediaSizeSm, t), cardActionGap: lerpDouble(cardActionGap, other.cardActionGap, t), cardBorderWidth: lerpDouble(cardBorderWidth, other.cardBorderWidth, t), cardBorderWidthSelected: lerpDouble(cardBorderWidthSelected, other.cardBorderWidthSelected, t), cardRowLabelMax: lerpDouble(cardRowLabelMax, other.cardRowLabelMax, t), cardRowMinHeight: lerpDouble(cardRowMinHeight, other.cardRowMinHeight, t), cardCheckSize: lerpDouble(cardCheckSize, other.cardCheckSize, t), cardCheckRing: lerpDouble(cardCheckRing, other.cardCheckRing, t), cardRadioSize: lerpDouble(cardRadioSize, other.cardRadioSize, t), cardRadioRing: lerpDouble(cardRadioRing, other.cardRadioRing, t), cardRadioOnRing: lerpDouble(cardRadioOnRing, other.cardRadioOnRing, t), cardChoiceTextGap: lerpDouble(cardChoiceTextGap, other.cardChoiceTextGap, t), fieldBorderWidth: lerpDouble(fieldBorderWidth, other.fieldBorderWidth, t), fieldBorderWidthActive: lerpDouble(fieldBorderWidthActive, other.fieldBorderWidthActive, t), fieldWidthDefault: lerpDouble(fieldWidthDefault, other.fieldWidthDefault, t), fieldEdgeInset: lerpDouble(fieldEdgeInset, other.fieldEdgeInset, t), fieldTextInset: lerpDouble(fieldTextInset, other.fieldTextInset, t), fieldContentGap: lerpDouble(fieldContentGap, other.fieldContentGap, t), fieldHintInset: lerpDouble(fieldHintInset, other.fieldHintInset, t), fieldLabelMaxWidth: lerpDouble(fieldLabelMaxWidth, other.fieldLabelMaxWidth, t), progressHeightSm: lerpDouble(progressHeightSm, other.progressHeightSm, t), progressHeightMd: lerpDouble(progressHeightMd, other.progressHeightMd, t), progressGap: lerpDouble(progressGap, other.progressGap, t), progressWidthDefault: lerpDouble(progressWidthDefault, other.progressWidthDefault, t), progressSegmentWidth: lerpDouble(progressSegmentWidth, other.progressSegmentWidth, t), otpCellWidth: lerpDouble(otpCellWidth, other.otpCellWidth, t), widthXs: lerpDouble(widthXs, other.widthXs, t), widthSm: lerpDouble(widthSm, other.widthSm, t), widthMd: lerpDouble(widthMd, other.widthMd, t), widthLg: lerpDouble(widthLg, other.widthLg, t), widthXl: lerpDouble(widthXl, other.widthXl, t), width2xl: lerpDouble(width2xl, other.width2xl, t), tableRowMinHeight: lerpDouble(tableRowMinHeight, other.tableRowMinHeight, t), tableCellPaddingY: lerpDouble(tableCellPaddingY, other.tableCellPaddingY, t), tableCellPaddingX: lerpDouble(tableCellPaddingX, other.tableCellPaddingX, t));
  }
}

/// Kiểu chữ — dựng từ [InvPlatform] để cỡ chữ đúng nền tảng.
abstract final class InvTypography {
  /// Số lớn, màn giới thiệu
  static TextStyle display(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplaySize, height: p.typeDisplayLineHeight / p.typeDisplaySize);
  /// Tiêu đề màn
  static TextStyle title1(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle1Size, height: p.typeTitle1LineHeight / p.typeTitle1Size);
  /// Tiêu đề dialog, sheet, khối lớn
  static TextStyle title2(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle2Size, height: p.typeTitle2LineHeight / p.typeTitle2Size);
  /// Tiêu đề khối, thẻ
  static TextStyle title3(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle3Size, height: p.typeTitle3LineHeight / p.typeTitle3Size);
  /// Tiêu đề nhóm nhỏ
  static TextStyle heading(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeHeadingSize, height: p.typeHeadingLineHeight / p.typeHeadingSize);
  /// Chữ đọc, giá trị
  static TextStyle body(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeBodySize, height: p.typeBodyLineHeight / p.typeBodySize);
  /// Nút, nhãn, tab
  static TextStyle label(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: p.typeLabelWeight, fontSize: p.typeLabelSize, height: p.typeLabelLineHeight / p.typeLabelSize);
  /// Thông tin phụ, thời gian
  static TextStyle caption(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize);
  /// Mã lệnh, mã chứng từ
  static TextStyle code(InvPlatform p) => TextStyle(fontFamily: 'JetBrainsMono', fontWeight: FontWeight.w400, fontSize: p.typeCodeSize, height: p.typeCodeLineHeight / p.typeCodeSize);
  /// Tên cột bảng, nhãn nhóm menu (ngoại lệ viết hoa DEC-027, DEC-133) · viết hoa: dùng .toUpperCase() ở chữ
  static TextStyle captionCaps(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w500, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize, letterSpacing: p.typeCaptionSize * 0.04);
  /// Chữ chip trạng thái Soft (DEC-200)
  static TextStyle captionStrong(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize);
  /// Chữ chip, badge, tag cỡ SM (DEC-261)
  static TextStyle chipSm(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.chipFontSizeSm, height: p.chipLineHeightSm / p.chipFontSizeSm);
  /// Chữ chip đã chọn cỡ SM (Tag Checked) (DEC-261)
  static TextStyle chipSmStrong(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.chipFontSizeSm, height: p.chipLineHeightSm / p.chipFontSizeSm);
}

/// Đổ bóng (effect style Figma).
abstract final class InvElevation {
  /// Thẻ (DEC-125)
  static const List<BoxShadow> elev1 = [BoxShadow(color: Color(0x0F101828), offset: Offset(0.0, 1.0), blurRadius: 2.0, spreadRadius: 0.0)];
  /// Menu thả, popover, gợi ý ô tìm
  static const List<BoxShadow> elev2 = [BoxShadow(color: Color(0x1A101828), offset: Offset(0.0, 4.0), blurRadius: 12.0, spreadRadius: 0.0), BoxShadow(color: Color(0x0F101828), offset: Offset(0.0, 1.0), blurRadius: 3.0, spreadRadius: 0.0)];
  /// Dialog, sheet, toast
  static const List<BoxShadow> elev3 = [BoxShadow(color: Color(0x29101828), offset: Offset(0.0, 16.0), blurRadius: 40.0, spreadRadius: 0.0), BoxShadow(color: Color(0x1A101828), offset: Offset(0.0, 4.0), blurRadius: 12.0, spreadRadius: 0.0)];
}

/// Làm mờ nền (DEC-258): dùng với BackdropFilter(filter: ImageFilter.blur(sigmaX: v, sigmaY: v)).
abstract final class InvBlur {
  /// Đầu màn, thanh công cụ dính trên cùng khi cuộn (nền trắng 70%).
  static const double blurSm = 8.0;
  /// Thanh điều hướng nổi app (DEC-160), thanh hành động nổi đáy màn.
  static const double blurMd = 16.0;
  /// Nền sau dialog, sheet: scrim 35% + blur.
  static const double blurLg = 24.0;
  /// Không dùng trong app nghiệp vụ.
  static const double blurXl = 40.0;
}

abstract final class InvMotion {
  static const Duration durationFast = Duration(milliseconds: 125);
  static const Duration durationMedium = Duration(milliseconds: 300);
  static const Duration durationSlow = Duration(milliseconds: 700);
  static const Curve easingStandard = Cubic(0.24, 1, 0.4, 1);
}

/// Gắn DS v2 vào ThemeData. Đổi khách: truyền brand khác.
ThemeData invTheme({Brightness brightness = Brightness.light, InvBrandColors brand = InvBrandColors.thanChi}) {
  final s = brightness == Brightness.dark ? InvColors.dark : InvColors.light;
  return ThemeData(
    brightness: brightness,
    fontFamily: 'Inter',
    scaffoldBackgroundColor: s.bgCanvas,
    extensions: [s, brand, InvComponentColors.from(s, brand), InvPlatform.mobile],
  );
}

extension InvThemeX on BuildContext {
  InvColors get invColors => Theme.of(this).extension<InvColors>()!;
  InvBrandColors get invBrand => Theme.of(this).extension<InvBrandColors>()!;
  InvComponentColors get invComponent => Theme.of(this).extension<InvComponentColors>()!;
  InvPlatform get invPlatform => Theme.of(this).extension<InvPlatform>()!;
}
