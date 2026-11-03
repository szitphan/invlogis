// GENERATED — không sửa tay. Nguồn: design-system/ · sinh bởi _scripts/ds-v2-handoff.py
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
  static const Color alphaNeutral95035 = Color(0x590A0A0A);
  static const Color alphaNeutral95050 = Color(0x800A0A0A);
  static const Color alphaDark070 = Color(0xB3191919);
  static const Color alphaBlack3 = Color(0x08000000);
  static const Color alphaBlack4 = Color(0x0A000000);
  static const Color alphaBlack5 = Color(0x0D000000);
  static const Color alphaBlack6 = Color(0x0F000000);
  static const Color alphaBlack8 = Color(0x14000000);
  static const Color alphaBlack14 = Color(0x24000000);
  static const Color alphaBlack18 = Color(0x2E000000);
  static const Color dark0 = Color(0xFF191919);
  static const Color dark1 = Color(0xFF202020);
  static const Color dark2 = Color(0xFF232323);
  static const Color dark3 = Color(0xFF2B2B2B);
  static const Color dark4 = Color(0xFF2E2E2E);
  static const Color black = Color(0xFF000000);
  static const Color alphaWhite10 = Color(0x1AFFFFFF);
  static const Color alphaBlack10 = Color(0x1A000000);
  static const Color alphaWhite20 = Color(0x33FFFFFF);
  static const Color alphaBlack20 = Color(0x33000000);
  static const Color alphaWhite30 = Color(0x4DFFFFFF);
  static const Color alphaBlack30 = Color(0x4D000000);
  static const Color alphaWhite40 = Color(0x66FFFFFF);
  static const Color alphaBlack40 = Color(0x66000000);
  static const Color alphaWhite50 = Color(0x80FFFFFF);
  static const Color alphaBlack50 = Color(0x80000000);
  static const Color alphaWhite60 = Color(0x99FFFFFF);
  static const Color alphaBlack60 = Color(0x99000000);
  static const Color alphaWhite70 = Color(0xB3FFFFFF);
  static const Color alphaBlack70 = Color(0xB3000000);
  static const Color alphaWhite80 = Color(0xCCFFFFFF);
  static const Color alphaBlack80 = Color(0xCC000000);
  static const Color alphaWhite90 = Color(0xE6FFFFFF);
  static const Color alphaBlack90 = Color(0xE6000000);
  static const Color alphaWhite100 = Color(0xFFFFFFFF);
  static const Color alphaBlack100 = Color(0xFF000000);
  static const Color alphaRed70055 = Color(0x8CB42318);
  static const Color fileTypePdf = Color(0xFFB42318);
  static const Color fileTypeDoc = Color(0xFF1F4FB8);
  static const Color fileTypeXls = Color(0xFF1B7542);
  static const Color fileTypeCsv = Color(0xFF1B7542);
  static const Color fileTypeImg = Color(0xFF6A50E4);
  static const Color fileTypeZip = Color(0xFF525252);
  static const Color fileTypeVid = Color(0xFFB54708);
  static const double space0 = 0.0;
  static const double space2 = 2.0;
  static const double space4 = 4.0;
  static const double space6 = 6.0;
  static const double space8 = 8.0;
  static const double space10 = 10.0;
  static const double space12 = 12.0;
  static const double space14 = 14.0;
  static const double space16 = 16.0;
  static const double space20 = 20.0;
  static const double space24 = 24.0;
  static const double space28 = 28.0;
  static const double space32 = 32.0;
  static const double space36 = 36.0;
  static const double space40 = 40.0;
  static const double space48 = 48.0;
  static const double space64 = 64.0;
  static const double space80 = 80.0;
  static const double space96 = 96.0;
  static const double space128 = 128.0;
  static const double space160 = 160.0;
  static const double space192 = 192.0;
  static const double space224 = 224.0;
  static const double space256 = 256.0;
  static const double space320 = 320.0;
  static const double space384 = 384.0;
  static const double space480 = 480.0;
  static const double space560 = 560.0;
  static const double space640 = 640.0;
  static const double space720 = 720.0;
  static const double space768 = 768.0;
  static const double space1024 = 1024.0;
  static const double space1280 = 1280.0;
  static const double space1440 = 1440.0;
  static const double space1600 = 1600.0;
  static const double space1920 = 1920.0;
  static const double radius0 = 0.0;
  static const double radius2 = 2.0;
  static const double radius4 = 4.0;
  static const double radius6 = 6.0;
  static const double radius8 = 8.0;
  static const double radius10 = 10.0;
  static const double radius12 = 12.0;
  static const double radius16 = 16.0;
  static const double radius20 = 20.0;
  static const double radius24 = 24.0;
  static const double radius9999 = 9999.0;
  static const double fontSizeXs = 12.0;
  static const double fontSizeSm = 14.0;
  static const double fontSizeMd = 16.0;
  static const double fontSizeLg = 18.0;
  static const double fontSizeXl = 20.0;
  static const double fontSizeDisplayXs = 24.0;
  static const double fontSizeDisplaySm = 30.0;
  static const double fontSizeDisplayMd = 36.0;
  static const double fontSizeDisplayLg = 48.0;
  static const double fontSizeDisplayXl = 60.0;
  static const double fontSizeDisplay2xl = 72.0;
  static const double lineHeightXs = 18.0;
  static const double lineHeightSm = 20.0;
  static const double lineHeightMd = 24.0;
  static const double lineHeightLg = 28.0;
  static const double lineHeightXl = 30.0;
  static const double lineHeightXsTight = 16.0;
  static const double lineHeightDisplayXs = 32.0;
  static const double lineHeightDisplaySm = 38.0;
  static const double lineHeightDisplayMd = 44.0;
  static const double lineHeightDisplayLg = 60.0;
  static const double lineHeightDisplayXl = 72.0;
  static const double lineHeightDisplay2xl = 90.0;
  static const double widthXxs = 320.0;
  static const double widthXs = 384.0;
  static const double widthSm = 480.0;
  static const double widthMd = 560.0;
  static const double widthLg = 640.0;
  static const double widthXl = 768.0;
  static const double width2xl = 1024.0;
  static const double width3xl = 1280.0;
  static const double width4xl = 1440.0;
  static const double width5xl = 1600.0;
  static const double width6xl = 1920.0;
}

/// Semantic — màu theo vai trò, mode Light | Dark. Dark nền #191919 (dark/0, DEC-316): nền nổi sáng dần dark/1…4, chữ chính neutral/200 #E5E5E5 (14:1), nút chính + vòng focus neutral/200, viền ô nhập neutral/500 (3,7:1). Chip, trạng thái đảo bậc (DEC-257). Màu khách ở Dark đi qua color/accent/* (bậc sáng của dải).
@immutable
class InvColors extends ThemeExtension<InvColors> {
  const InvColors({
    required this.actionPrimary,
    required this.actionPrimaryHover,
    required this.actionPrimaryPressed,
    required this.actionSecondary,
    required this.actionSecondaryHover,
    required this.actionSecondaryPressed,
    required this.bgDisabled,
    required this.bgErrorPrimary,
    required this.bgErrorPrimaryHover,
    required this.bgErrorPrimaryPressed,
    required this.bgErrorSecondary,
    required this.bgErrorSolid,
    required this.bgErrorSolidHover,
    required this.bgInfoPrimary,
    required this.bgInfoSecondary,
    required this.bgInfoSolid,
    required this.bgInfoSolidHover,
    required this.bgOverlay,
    required this.bgOverlaySolid,
    required this.bgPrimaryBlur,
    required this.bgPressed,
    required this.bgPrimary,
    required this.bgPrimaryAlt,
    required this.bgPrimaryHover,
    required this.bgPrimarySolid,
    required this.bgQuaternary,
    required this.bgQuaternaryHover,
    required this.bgSecondary,
    required this.bgSecondaryAlt,
    required this.bgSecondaryHover,
    required this.bgSecondarySolid,
    required this.bgSelected,
    required this.bgSkeleton,
    required this.bgSuccessPrimary,
    required this.bgSuccessSecondary,
    required this.bgSuccessSolid,
    required this.bgSuccessSolidHover,
    required this.bgTertiary,
    required this.bgWarningPrimary,
    required this.bgWarningSecondary,
    required this.bgWarningSolid,
    required this.bgWarningSolidHover,
    required this.borderDisabled,
    required this.borderError,
    required this.borderErrorSubtle,
    required this.borderInfo,
    required this.borderInfoSubtle,
    required this.borderInput,
    required this.borderPrimary,
    required this.borderSecondary,
    required this.borderSecondaryAlt,
    required this.borderSuccess,
    required this.borderSuccessSubtle,
    required this.borderTertiary,
    required this.borderWarning,
    required this.borderWarningSubtle,
    required this.fgDisabled,
    required this.fgErrorPrimary,
    required this.fgErrorSecondary,
    required this.fgInfoPrimary,
    required this.fgInverse,
    required this.fgPrimary,
    required this.fgQuaternary,
    required this.fgQuaternaryHover,
    required this.fgSecondary,
    required this.fgSecondaryHover,
    required this.fgSuccessPrimary,
    required this.fgSuccessSecondary,
    required this.fgTertiary,
    required this.fgTertiaryHover,
    required this.fgWarningPrimary,
    required this.fgWarningSecondary,
    required this.fgWhite,
    required this.focusRing,
    required this.focusRingError,
    required this.shadowXs,
    required this.shadowSm01,
    required this.shadowSm02,
    required this.shadowMd01,
    required this.shadowMd02,
    required this.shadowLg01,
    required this.shadowLg02,
    required this.shadowLg03,
    required this.shadowXl01,
    required this.shadowXl02,
    required this.shadowXl03,
    required this.shadow2xl01,
    required this.shadow2xl02,
    required this.shadow3xl01,
    required this.shadow3xl02,
    required this.textDisabled,
    required this.textErrorPrimary,
    required this.textErrorPrimaryHover,
    required this.textInfoPrimary,
    required this.textInverse,
    required this.textPlaceholder,
    required this.textPrimary,
    required this.textQuaternary,
    required this.textSecondary,
    required this.textSecondaryHover,
    required this.textSuccessPrimary,
    required this.textTertiary,
    required this.textTertiaryHover,
    required this.textTertiaryStrong,
    required this.textWarningPrimary,
    required this.textWhite,
    required this.utilityBlue100,
    required this.utilityBlue200,
    required this.utilityBlue300,
    required this.utilityBlue400,
    required this.utilityBlue50,
    required this.utilityBlue500,
    required this.utilityBlue600,
    required this.utilityBlue700,
    required this.utilityGreen100,
    required this.utilityGreen200,
    required this.utilityGreen300,
    required this.utilityGreen400,
    required this.utilityGreen50,
    required this.utilityGreen500,
    required this.utilityGreen600,
    required this.utilityGreen700,
    required this.utilityNeutral100,
    required this.utilityNeutral200,
    required this.utilityNeutral300,
    required this.utilityNeutral400,
    required this.utilityNeutral50,
    required this.utilityNeutral500,
    required this.utilityNeutral600,
    required this.utilityNeutral700,
    required this.utilityOrange100,
    required this.utilityOrange200,
    required this.utilityOrange300,
    required this.utilityOrange400,
    required this.utilityOrange50,
    required this.utilityOrange500,
    required this.utilityOrange600,
    required this.utilityOrange700,
    required this.utilityOrange800,
    required this.utilityPurple100,
    required this.utilityPurple200,
    required this.utilityPurple300,
    required this.utilityPurple400,
    required this.utilityPurple50,
    required this.utilityPurple500,
    required this.utilityPurple600,
    required this.utilityPurple700,
    required this.utilityRed100,
    required this.utilityRed200,
    required this.utilityRed300,
    required this.utilityRed400,
    required this.utilityRed50,
    required this.utilityRed500,
    required this.utilityRed600,
    required this.utilityRed700,
    required this.utilityTeal100,
    required this.utilityTeal200,
    required this.utilityTeal300,
    required this.utilityTeal400,
    required this.utilityTeal50,
    required this.utilityTeal500,
    required this.utilityTeal600,
    required this.utilityTeal700,
    required this.utilityYellow100,
    required this.utilityYellow200,
    required this.utilityYellow300,
    required this.utilityYellow400,
    required this.utilityYellow50,
    required this.utilityYellow500,
    required this.utilityYellow600,
    required this.utilityYellow700,
    required this.borderInputHover,
    required this.bgErrorOverlay,
    required this.vehicleMediaBg,
    required this.vehicleOutline,
    required this.logoBg,
    required this.fileTypePdf,
    required this.fileTypeDoc,
    required this.fileTypeXls,
    required this.fileTypeCsv,
    required this.fileTypeImg,
    required this.fileTypeZip,
    required this.fileTypeVid,
  });

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
  /// Nền nút Secondary khi bấm; nút Outline dùng chung thang secondary khi rê, bấm.
  final Color actionSecondaryPressed;
  /// Nền control tắt: nút, ô nhập, ô chọn (DEC-316)
  final Color bgDisabled;
  /// Nền lỗi chính (DEC-320)
  final Color bgErrorPrimary;
  /// Nền nhạt nút Danger khi rê chuột. (DEC-320)
  final Color bgErrorPrimaryHover;
  /// Nền nhạt nút Danger khi bấm. (DEC-320)
  final Color bgErrorPrimaryPressed;
  /// Nền lỗi phụ: featured icon (DEC-320)
  final Color bgErrorSecondary;
  /// Nền lỗi đặc: nút, featured icon, số liệu (DEC-320)
  final Color bgErrorSolid;
  /// Nền lỗi đặc khi rê chuột (DEC-320)
  final Color bgErrorSolidHover;
  /// Nền thông tin chính (DEC-320)
  final Color bgInfoPrimary;
  /// Nền thông tin phụ: featured icon (DEC-320)
  final Color bgInfoSecondary;
  /// Nền thông tin đặc: nút, featured icon, số liệu (DEC-320)
  final Color bgInfoSolid;
  /// Nền thông tin đặc khi rê chuột (DEC-320)
  final Color bgInfoSolidHover;
  /// Nền lớp phủ sau dialog, sheet: 35% + backdrop-blur/lg (DEC-258, DEC-327)
  final Color bgOverlay;
  /// Đường lùi của lớp phủ khi máy không chạy được làm mờ: 50%, không blur (DEC-327); lớp tối và rãnh vòng tiến độ đè lên ảnh (DEC-321)
  final Color bgOverlaySolid;
  /// Nền đầu màn dính và thanh nổi app, đi cùng backdrop-blur (DEC-327)
  final Color bgPrimaryBlur;
  /// Nền đang bấm của thứ nền trắng: dòng danh sách, thẻ bấm được (app không có hover); chữ phụ trên nền này dùng text/tertiary_strong (DEC-316)
  final Color bgPressed;
  /// Nền chính cho mọi bố cục và component (DEC-320)
  final Color bgPrimary;
  /// Nền trắng ở Light, sáng hơn nền trang ở Dark: menu, dialog, sheet (DEC-320)
  final Color bgPrimaryAlt;
  /// Rê chuột trên component nền trắng: menu chọn, dòng bảng (DEC-320)
  final Color bgPrimaryHover;
  /// Nền tối chính: tooltip, toast trung tính (DEC-320)
  final Color bgPrimarySolid;
  /// Nền cấp 4 trên nền sáng: thanh trượt, thanh tiến độ, công tắc tắt (DEC-320)
  final Color bgQuaternary;
  /// Rãnh công tắc tắt khi rê chuột (DEC-316, DEC-320)
  final Color bgQuaternaryHover;
  /// Nền phụ tạo tương phản với nền trắng (DEC-320)
  final Color bgSecondary;
  /// Nền phụ thành nền trang ở Dark (tab kiểu viền) (DEC-320)
  final Color bgSecondaryAlt;
  /// Rê chuột trên component nền phụ (DEC-320)
  final Color bgSecondaryHover;
  /// Nền tối phụ: featured icon (DEC-320)
  final Color bgSecondarySolid;
  /// Nền mục đang chọn khi khách không có màu riêng. Dùng ở: List Item đang chọn, mục menu đang chọn.
  final Color bgSelected;
  /// Khối chờ tải (skeleton) (DEC-316)
  final Color bgSkeleton;
  /// Nền thành công chính (DEC-320)
  final Color bgSuccessPrimary;
  /// Nền thành công phụ: featured icon (DEC-320)
  final Color bgSuccessSecondary;
  /// Nền thành công đặc: nút, featured icon, số liệu (DEC-320)
  final Color bgSuccessSolid;
  /// Nền thành công đặc khi rê chuột (DEC-320)
  final Color bgSuccessSolidHover;
  /// Nền cấp 3: công tắc tắt (DEC-320)
  final Color bgTertiary;
  /// Nền cảnh báo chính (DEC-320)
  final Color bgWarningPrimary;
  /// Nền cảnh báo phụ: featured icon (DEC-320)
  final Color bgWarningSecondary;
  /// Nền cảnh báo đặc: nút, featured icon, số liệu (DEC-320)
  final Color bgWarningSolid;
  /// Nền cảnh báo đặc khi rê chuột (DEC-320)
  final Color bgWarningSolidHover;
  /// Viền control tắt (DEC-316)
  final Color borderDisabled;
  /// Viền lỗi mặc định: ô nhập, tải tệp (DEC-320)
  final Color borderError;
  /// Viền lỗi nhạt hơn (DEC-320)
  final Color borderErrorSubtle;
  /// Viền thông tin (DEC-320)
  final Color borderInfo;
  /// Viền thông tin nhạt (DEC-320)
  final Color borderInfoSubtle;
  /// Viền tương phản cao (≥ 3:1) cho thứ người dùng nhập hoặc chọn. Dùng ở: Text Field, OTP Field, radio Selectable Card.
  final Color borderInput;
  /// Viền tương phản cao hơn mặc định: nhóm nút, nút Secondary (DEC-320)
  final Color borderPrimary;
  /// Viền dùng nhiều nhất, mặc định cho phần lớn component (DEC-320)
  final Color borderSecondary;
  /// Biến thể alpha của viền phụ, chỉ dùng cho menu nổi (DEC-320)
  final Color borderSecondaryAlt;
  /// Viền thành công (DEC-320)
  final Color borderSuccess;
  /// Viền thành công nhạt (DEC-320)
  final Color borderSuccessSubtle;
  /// Viền tương phản thấp: vạch chia rất nhạt, trục biểu đồ (DEC-320)
  final Color borderTertiary;
  /// Viền cảnh báo (DEC-320)
  final Color borderWarning;
  /// Viền cảnh báo nhạt (DEC-320)
  final Color borderWarningSubtle;
  /// Icon control tắt (DEC-316, DEC-320)
  final Color fgDisabled;
  /// Icon lỗi chính: featured icon (DEC-320)
  final Color fgErrorPrimary;
  /// Icon trong ô lỗi, chỉ số âm (DEC-320)
  final Color fgErrorSecondary;
  /// Icon thông tin chính: featured icon (DEC-320)
  final Color fgInfoPrimary;
  /// Icon trên nền đậm đổi theo chế độ: Tooltip, nút Primary (DEC-316, DEC-320)
  final Color fgInverse;
  /// Icon tương phản cao nhất (DEC-320)
  final Color fgPrimary;
  /// Tương phản thấp, chỉ cho icon trang trí và disabled (DEC-320, DEC-329 ic12)
  final Color fgQuaternary;
  /// Icon tương phản thấp khi rê chuột (DEC-320)
  final Color fgQuaternaryHover;
  /// Phần tử không phải chữ tương phản cao: icon đi cùng chữ chính (DEC-320)
  final Color fgSecondary;
  /// Icon khi rê chuột (DEC-320)
  final Color fgSecondaryHover;
  /// Icon thành công chính: featured icon (DEC-320)
  final Color fgSuccessPrimary;
  /// Chấm online avatar, chấm nút (DEC-320)
  final Color fgSuccessSecondary;
  /// Icon tương phản vừa (DEC-320) · Icon phụ mang nghĩa: chevron ô chọn, icon ô tìm, Help (DEC-329 ic12)
  final Color fgTertiary;
  /// Icon tương phản vừa khi rê chuột (DEC-320)
  final Color fgTertiaryHover;
  /// Icon cảnh báo chính: featured icon (DEC-320)
  final Color fgWarningPrimary;
  /// Cảnh báo phụ (DEC-320)
  final Color fgWarningSecondary;
  /// Icon luôn trắng, mọi chế độ (DEC-320)
  final Color fgWhite;
  /// Vòng focus mặc định; than chì cho mọi khách (DEC-170) (DEC-320)
  final Color focusRing;
  /// Vòng focus lỗi (DEC-320)
  final Color focusRingError;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xs lớp 1 (DEC-327).
  final Color shadowXs;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/sm lớp 1 (DEC-327).
  final Color shadowSm01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/sm lớp 2 (DEC-327).
  final Color shadowSm02;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/md lớp 1 (DEC-327).
  final Color shadowMd01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/md lớp 2 (DEC-327).
  final Color shadowMd02;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 1 (DEC-327).
  final Color shadowLg01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 2 (DEC-327).
  final Color shadowLg02;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 3 (DEC-327).
  final Color shadowLg03;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 1 (DEC-327).
  final Color shadowXl01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 2 (DEC-327).
  final Color shadowXl02;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 3 (DEC-327).
  final Color shadowXl03;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/2xl lớp 1 (DEC-327).
  final Color shadow2xl01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/2xl lớp 2 (DEC-327).
  final Color shadow2xl02;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/3xl lớp 1 (DEC-327).
  final Color shadow3xl01;
  /// Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/3xl lớp 2 (DEC-327).
  final Color shadow3xl02;
  /// Chữ control tắt; không dùng cho nội dung (DEC-316, DEC-320)
  final Color textDisabled;
  /// Chữ lỗi mặc định (DEC-320)
  final Color textErrorPrimary;
  /// Chữ lỗi khi rê chuột (DEC-320)
  final Color textErrorPrimaryHover;
  /// Chữ thông tin mặc định (DEC-320)
  final Color textInfoPrimary;
  /// Chữ trên nền đậm. Dùng ở: chữ nút Primary, chữ Tooltip.
  final Color textInverse;
  /// Chữ gợi ý trong ô nhập
  final Color textPlaceholder;
  /// Chữ chính: tiêu đề trang, giá trị chính
  final Color textPrimary;
  /// Chữ nhạt, tương phản thấp (DEC-320)
  final Color textQuaternary;
  /// Chữ phụ: nhãn, tiêu đề mục (DEC-320)
  final Color textSecondary;
  /// Chữ phụ khi rê chuột (DEC-320)
  final Color textSecondaryHover;
  /// Chữ thành công mặc định (DEC-320)
  final Color textSuccessPrimary;
  /// Chữ hỗ trợ, đoạn văn, nhãn trường, thời gian (DEC-320)
  final Color textTertiary;
  /// Chữ hỗ trợ khi rê chuột (DEC-320)
  final Color textTertiaryHover;
  /// Chữ phụ trên nền nhấn (hover, đang chọn) để giữ ≥ 4,5:1 (DEC-289). Dùng ở: dòng phụ thẻ phạm vi khi Hover/Open, dòng chọn Hover/Selected của Scope dialog. (DEC-320)
  final Color textTertiaryStrong;
  /// Chữ cảnh báo mặc định (DEC-320)
  final Color textWarningPrimary;
  /// Luôn trắng, mọi chế độ: chữ trên nền đặc (DEC-320)
  final Color textWhite;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityBlue100;
  /// Chip blue: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityBlue200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityBlue300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityBlue400;
  /// Chip trạng thái blue: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityBlue50;
  /// Chuỗi dữ liệu biểu đồ thứ 1 (DEC-316, DEC-320)
  final Color utilityBlue500;
  /// Chip blue: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityBlue600;
  /// Chip trạng thái blue: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityBlue700;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityGreen100;
  /// Chip green: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityGreen200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityGreen300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityGreen400;
  /// Chip trạng thái green: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityGreen50;
  /// Chuỗi dữ liệu biểu đồ thứ 5 (DEC-316, DEC-320)
  final Color utilityGreen500;
  /// Chip green: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityGreen600;
  /// Chip trạng thái green: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityGreen700;
  /// Chip trạng thái gray: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityNeutral100;
  /// Chip gray: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityNeutral200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityNeutral300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityNeutral400;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityNeutral50;
  /// Chip gray: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityNeutral500;
  /// Chip trạng thái gray: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityNeutral600;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityNeutral700;
  /// Chip trạng thái orange: nền. Dùng ở: Status Chip, Status Row. Light orange/100 (review R1, DEC-311: tách khỏi chip vàng). (DEC-320)
  final Color utilityOrange100;
  /// Chip orange: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityOrange200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityOrange300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityOrange400;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityOrange50;
  /// Chuỗi dữ liệu biểu đồ thứ 7 (DEC-316, DEC-320)
  final Color utilityOrange500;
  /// Chip orange: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityOrange600;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityOrange700;
  /// Chip trạng thái orange: chữ, icon. Dùng ở: Status Chip, Status Row. Light orange/800 (review R1, DEC-311). (DEC-320)
  final Color utilityOrange800;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityPurple100;
  /// Chip purple: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityPurple200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityPurple300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityPurple400;
  /// Chip trạng thái purple: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityPurple50;
  /// Chuỗi dữ liệu biểu đồ thứ 3 (DEC-316, DEC-320)
  final Color utilityPurple500;
  /// Chip purple: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityPurple600;
  /// Chip trạng thái purple: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityPurple700;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityRed100;
  /// Chip red: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityRed200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityRed300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityRed400;
  /// Chip trạng thái red: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityRed50;
  /// Chuỗi dữ liệu biểu đồ thứ 6 (DEC-316, DEC-320)
  final Color utilityRed500;
  /// Chip red: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityRed600;
  /// Chip trạng thái red: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityRed700;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityTeal100;
  /// Chip teal: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityTeal200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityTeal300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityTeal400;
  /// Chip trạng thái teal: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityTeal50;
  /// Chuỗi dữ liệu biểu đồ thứ 2 (DEC-316, DEC-320)
  final Color utilityTeal500;
  /// Chip teal: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityTeal600;
  /// Chip trạng thái teal: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityTeal700;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityYellow100;
  /// Chip yellow: viền Badge Outline (DEC-308) (DEC-316, DEC-320)
  final Color utilityYellow200;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityYellow300;
  /// Thang utility, đảo bậc ở Dark (DEC-320)
  final Color utilityYellow400;
  /// Chip trạng thái yellow: nền. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityYellow50;
  /// Chuỗi dữ liệu biểu đồ thứ 4 (DEC-316, DEC-320)
  final Color utilityYellow500;
  /// Chip yellow: chấm Badge Dot (DEC-310) (DEC-316, DEC-320)
  final Color utilityYellow600;
  /// Chip trạng thái yellow: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320)
  final Color utilityYellow700;
  /// Viền ô nhập khi rê chuột, đậm hơn border/input (DEC-321)
  final Color borderInputHover;
  /// Lớp phủ đỏ trên ảnh tải lỗi, không đổi theo Light/Dark vì ảnh không đổi (DEC-321)
  final Color bgErrorOverlay;
  /// Nền ô ảnh phương tiện (DEC-334 vh08)
  final Color vehicleMediaBg;
  /// Nét bao 0,6 theo hình ảnh phương tiện (DEC-334 vh08)
  final Color vehicleOutline;
  /// Ô nền logo đối tác (Bank logo): trắng ở cả Sáng và Tối để logo màu không chìm trên nền Tối (DEC-338)
  final Color logoBg;
  /// Nền nhãn PDF của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypePdf;
  /// Nền nhãn DOC của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeDoc;
  /// Nền nhãn XLS của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeXls;
  /// Nền nhãn CSV của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeCsv;
  /// Nền nhãn IMG của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeImg;
  /// Nền nhãn ZIP của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeZip;
  /// Nền nhãn VID của File type icon, màu nhận diện loại tệp, không đảo theo chế độ; chữ nhãn color/fg/white (DEC-335 ms02)
  final Color fileTypeVid;

  static const light = InvColors(
    actionPrimary: InvPrimitives.charcoal900,
    actionPrimaryHover: InvPrimitives.charcoal800,
    actionPrimaryPressed: InvPrimitives.charcoal950,
    actionSecondary: InvPrimitives.neutral100,
    actionSecondaryHover: InvPrimitives.neutral200,
    actionSecondaryPressed: InvPrimitives.neutral300,
    bgDisabled: InvPrimitives.neutral100,
    bgErrorPrimary: InvPrimitives.red50,
    bgErrorPrimaryHover: InvPrimitives.red100,
    bgErrorPrimaryPressed: InvPrimitives.red200,
    bgErrorSecondary: InvPrimitives.red100,
    bgErrorSolid: InvPrimitives.red700,
    bgErrorSolidHover: InvPrimitives.red800,
    bgInfoPrimary: InvPrimitives.blue50,
    bgInfoSecondary: InvPrimitives.blue100,
    bgInfoSolid: InvPrimitives.blue700,
    bgInfoSolidHover: InvPrimitives.blue800,
    bgOverlay: InvPrimitives.alphaNeutral95035,
    bgOverlaySolid: InvPrimitives.alphaNeutral95050,
    bgPrimaryBlur: InvPrimitives.alphaWhite70,
    bgPressed: InvPrimitives.neutral200,
    bgPrimary: InvPrimitives.white,
    bgPrimaryAlt: InvPrimitives.white,
    bgPrimaryHover: InvPrimitives.neutral50,
    bgPrimarySolid: InvPrimitives.neutral900,
    bgQuaternary: InvPrimitives.neutral200,
    bgQuaternaryHover: InvPrimitives.neutral300,
    bgSecondary: InvPrimitives.neutral50,
    bgSecondaryAlt: InvPrimitives.neutral50,
    bgSecondaryHover: InvPrimitives.neutral100,
    bgSecondarySolid: InvPrimitives.neutral600,
    bgSelected: InvPrimitives.neutral100,
    bgSkeleton: InvPrimitives.neutral100,
    bgSuccessPrimary: InvPrimitives.green50,
    bgSuccessSecondary: InvPrimitives.green100,
    bgSuccessSolid: InvPrimitives.green700,
    bgSuccessSolidHover: InvPrimitives.green800,
    bgTertiary: InvPrimitives.neutral100,
    bgWarningPrimary: InvPrimitives.yellow50,
    bgWarningSecondary: InvPrimitives.yellow100,
    bgWarningSolid: InvPrimitives.yellow700,
    bgWarningSolidHover: InvPrimitives.yellow800,
    borderDisabled: InvPrimitives.neutral200,
    borderError: InvPrimitives.red700,
    borderErrorSubtle: InvPrimitives.red300,
    borderInfo: InvPrimitives.blue700,
    borderInfoSubtle: InvPrimitives.blue300,
    borderInput: InvPrimitives.neutral500,
    borderPrimary: InvPrimitives.neutral300,
    borderSecondary: InvPrimitives.neutral200,
    borderSecondaryAlt: InvPrimitives.alphaBlack10,
    borderSuccess: InvPrimitives.green700,
    borderSuccessSubtle: InvPrimitives.green300,
    borderTertiary: InvPrimitives.neutral100,
    borderWarning: InvPrimitives.yellow700,
    borderWarningSubtle: InvPrimitives.yellow300,
    fgDisabled: InvPrimitives.neutral400,
    fgErrorPrimary: InvPrimitives.red600,
    fgErrorSecondary: InvPrimitives.red500,
    fgInfoPrimary: InvPrimitives.blue600,
    fgInverse: InvPrimitives.white,
    fgPrimary: InvPrimitives.neutral900,
    fgQuaternary: InvPrimitives.neutral400,
    fgQuaternaryHover: InvPrimitives.neutral500,
    fgSecondary: InvPrimitives.neutral700,
    fgSecondaryHover: InvPrimitives.neutral800,
    fgSuccessPrimary: InvPrimitives.green600,
    fgSuccessSecondary: InvPrimitives.green500,
    fgTertiary: InvPrimitives.neutral600,
    fgTertiaryHover: InvPrimitives.neutral700,
    fgWarningPrimary: InvPrimitives.yellow600,
    fgWarningSecondary: InvPrimitives.yellow500,
    fgWhite: InvPrimitives.white,
    focusRing: InvPrimitives.charcoal900,
    focusRingError: InvPrimitives.red700,
    shadowXs: InvPrimitives.alphaBlack5,
    shadowSm01: InvPrimitives.alphaBlack10,
    shadowSm02: InvPrimitives.alphaBlack10,
    shadowMd01: InvPrimitives.alphaBlack10,
    shadowMd02: InvPrimitives.alphaBlack6,
    shadowLg01: InvPrimitives.alphaBlack8,
    shadowLg02: InvPrimitives.alphaBlack3,
    shadowLg03: InvPrimitives.alphaBlack4,
    shadowXl01: InvPrimitives.alphaBlack8,
    shadowXl02: InvPrimitives.alphaBlack3,
    shadowXl03: InvPrimitives.alphaBlack4,
    shadow2xl01: InvPrimitives.alphaBlack18,
    shadow2xl02: InvPrimitives.alphaBlack4,
    shadow3xl01: InvPrimitives.alphaBlack14,
    shadow3xl02: InvPrimitives.alphaBlack4,
    textDisabled: InvPrimitives.neutral400,
    textErrorPrimary: InvPrimitives.red700,
    textErrorPrimaryHover: InvPrimitives.red700,
    textInfoPrimary: InvPrimitives.blue700,
    textInverse: InvPrimitives.white,
    textPlaceholder: InvPrimitives.neutral500,
    textPrimary: InvPrimitives.neutral900,
    textQuaternary: InvPrimitives.neutral500,
    textSecondary: InvPrimitives.neutral700,
    textSecondaryHover: InvPrimitives.neutral800,
    textSuccessPrimary: InvPrimitives.green700,
    textTertiary: InvPrimitives.neutral500,
    textTertiaryHover: InvPrimitives.neutral700,
    textTertiaryStrong: InvPrimitives.neutral600,
    textWarningPrimary: InvPrimitives.yellow700,
    textWhite: InvPrimitives.white,
    utilityBlue100: InvPrimitives.blue100,
    utilityBlue200: InvPrimitives.blue200,
    utilityBlue300: InvPrimitives.blue300,
    utilityBlue400: InvPrimitives.blue400,
    utilityBlue50: InvPrimitives.blue50,
    utilityBlue500: InvPrimitives.blue500,
    utilityBlue600: InvPrimitives.blue600,
    utilityBlue700: InvPrimitives.blue700,
    utilityGreen100: InvPrimitives.green100,
    utilityGreen200: InvPrimitives.green200,
    utilityGreen300: InvPrimitives.green300,
    utilityGreen400: InvPrimitives.green400,
    utilityGreen50: InvPrimitives.green50,
    utilityGreen500: InvPrimitives.green500,
    utilityGreen600: InvPrimitives.green600,
    utilityGreen700: InvPrimitives.green700,
    utilityNeutral100: InvPrimitives.neutral100,
    utilityNeutral200: InvPrimitives.neutral200,
    utilityNeutral300: InvPrimitives.neutral300,
    utilityNeutral400: InvPrimitives.neutral400,
    utilityNeutral50: InvPrimitives.neutral50,
    utilityNeutral500: InvPrimitives.neutral500,
    utilityNeutral600: InvPrimitives.neutral600,
    utilityNeutral700: InvPrimitives.neutral700,
    utilityOrange100: InvPrimitives.orange100,
    utilityOrange200: InvPrimitives.orange200,
    utilityOrange300: InvPrimitives.orange300,
    utilityOrange400: InvPrimitives.orange400,
    utilityOrange50: InvPrimitives.orange50,
    utilityOrange500: InvPrimitives.orange500,
    utilityOrange600: InvPrimitives.orange600,
    utilityOrange700: InvPrimitives.orange700,
    utilityOrange800: InvPrimitives.orange800,
    utilityPurple100: InvPrimitives.purple100,
    utilityPurple200: InvPrimitives.purple200,
    utilityPurple300: InvPrimitives.purple300,
    utilityPurple400: InvPrimitives.purple400,
    utilityPurple50: InvPrimitives.purple50,
    utilityPurple500: InvPrimitives.purple500,
    utilityPurple600: InvPrimitives.purple600,
    utilityPurple700: InvPrimitives.purple700,
    utilityRed100: InvPrimitives.red100,
    utilityRed200: InvPrimitives.red200,
    utilityRed300: InvPrimitives.red300,
    utilityRed400: InvPrimitives.red400,
    utilityRed50: InvPrimitives.red50,
    utilityRed500: InvPrimitives.red500,
    utilityRed600: InvPrimitives.red600,
    utilityRed700: InvPrimitives.red700,
    utilityTeal100: InvPrimitives.teal100,
    utilityTeal200: InvPrimitives.teal200,
    utilityTeal300: InvPrimitives.teal300,
    utilityTeal400: InvPrimitives.teal400,
    utilityTeal50: InvPrimitives.teal50,
    utilityTeal500: InvPrimitives.teal500,
    utilityTeal600: InvPrimitives.teal600,
    utilityTeal700: InvPrimitives.teal700,
    utilityYellow100: InvPrimitives.yellow100,
    utilityYellow200: InvPrimitives.yellow200,
    utilityYellow300: InvPrimitives.yellow300,
    utilityYellow400: InvPrimitives.yellow400,
    utilityYellow50: InvPrimitives.yellow50,
    utilityYellow500: InvPrimitives.yellow500,
    utilityYellow600: InvPrimitives.yellow600,
    utilityYellow700: InvPrimitives.yellow700,
    borderInputHover: InvPrimitives.neutral700,
    bgErrorOverlay: InvPrimitives.alphaRed70055,
    vehicleMediaBg: InvPrimitives.neutral50,
    vehicleOutline: InvPrimitives.neutral400,
    logoBg: InvPrimitives.white,
    fileTypePdf: InvPrimitives.fileTypePdf,
    fileTypeDoc: InvPrimitives.fileTypeDoc,
    fileTypeXls: InvPrimitives.fileTypeXls,
    fileTypeCsv: InvPrimitives.fileTypeCsv,
    fileTypeImg: InvPrimitives.fileTypeImg,
    fileTypeZip: InvPrimitives.fileTypeZip,
    fileTypeVid: InvPrimitives.fileTypeVid,
  );

  static const dark = InvColors(
    actionPrimary: InvPrimitives.neutral200,
    actionPrimaryHover: InvPrimitives.neutral300,
    actionPrimaryPressed: InvPrimitives.neutral400,
    actionSecondary: InvPrimitives.dark3,
    actionSecondaryHover: InvPrimitives.neutral700,
    actionSecondaryPressed: InvPrimitives.neutral600,
    bgDisabled: InvPrimitives.dark3,
    bgErrorPrimary: InvPrimitives.red950,
    bgErrorPrimaryHover: InvPrimitives.red900,
    bgErrorPrimaryPressed: InvPrimitives.red800,
    bgErrorSecondary: InvPrimitives.red900,
    bgErrorSolid: InvPrimitives.red700,
    bgErrorSolidHover: InvPrimitives.red600,
    bgInfoPrimary: InvPrimitives.blue950,
    bgInfoSecondary: InvPrimitives.blue900,
    bgInfoSolid: InvPrimitives.blue700,
    bgInfoSolidHover: InvPrimitives.blue600,
    bgOverlay: InvPrimitives.alphaNeutral95035,
    bgOverlaySolid: InvPrimitives.alphaNeutral95050,
    bgPrimaryBlur: InvPrimitives.alphaDark070,
    bgPressed: InvPrimitives.neutral700,
    bgPrimary: InvPrimitives.dark0,
    bgPrimaryAlt: InvPrimitives.dark1,
    bgPrimaryHover: InvPrimitives.dark2,
    bgPrimarySolid: InvPrimitives.neutral200,
    bgQuaternary: InvPrimitives.neutral700,
    bgQuaternaryHover: InvPrimitives.neutral600,
    bgSecondary: InvPrimitives.dark2,
    bgSecondaryAlt: InvPrimitives.dark0,
    bgSecondaryHover: InvPrimitives.dark3,
    bgSecondarySolid: InvPrimitives.neutral600,
    bgSelected: InvPrimitives.dark3,
    bgSkeleton: InvPrimitives.dark3,
    bgSuccessPrimary: InvPrimitives.green950,
    bgSuccessSecondary: InvPrimitives.green900,
    bgSuccessSolid: InvPrimitives.green700,
    bgSuccessSolidHover: InvPrimitives.green600,
    bgTertiary: InvPrimitives.dark3,
    bgWarningPrimary: InvPrimitives.yellow950,
    bgWarningSecondary: InvPrimitives.yellow900,
    bgWarningSolid: InvPrimitives.yellow700,
    bgWarningSolidHover: InvPrimitives.yellow600,
    borderDisabled: InvPrimitives.dark4,
    borderError: InvPrimitives.red300,
    borderErrorSubtle: InvPrimitives.red700,
    borderInfo: InvPrimitives.blue300,
    borderInfoSubtle: InvPrimitives.blue700,
    borderInput: InvPrimitives.neutral500,
    borderPrimary: InvPrimitives.neutral700,
    borderSecondary: InvPrimitives.dark4,
    borderSecondaryAlt: InvPrimitives.dark4,
    borderSuccess: InvPrimitives.green300,
    borderSuccessSubtle: InvPrimitives.green700,
    borderTertiary: InvPrimitives.dark2,
    borderWarning: InvPrimitives.yellow300,
    borderWarningSubtle: InvPrimitives.yellow700,
    fgDisabled: InvPrimitives.neutral600,
    fgErrorPrimary: InvPrimitives.red400,
    fgErrorSecondary: InvPrimitives.red400,
    fgInfoPrimary: InvPrimitives.blue400,
    fgInverse: InvPrimitives.neutral950,
    fgPrimary: InvPrimitives.white,
    fgQuaternary: InvPrimitives.neutral600,
    fgQuaternaryHover: InvPrimitives.neutral500,
    fgSecondary: InvPrimitives.neutral300,
    fgSecondaryHover: InvPrimitives.neutral200,
    fgSuccessPrimary: InvPrimitives.green400,
    fgSuccessSecondary: InvPrimitives.green400,
    fgTertiary: InvPrimitives.neutral400,
    fgTertiaryHover: InvPrimitives.neutral300,
    fgWarningPrimary: InvPrimitives.yellow400,
    fgWarningSecondary: InvPrimitives.yellow400,
    fgWhite: InvPrimitives.white,
    focusRing: InvPrimitives.neutral200,
    focusRingError: InvPrimitives.red300,
    shadowXs: InvPrimitives.alphaBlack40,
    shadowSm01: InvPrimitives.alphaBlack60,
    shadowSm02: InvPrimitives.alphaBlack40,
    shadowMd01: InvPrimitives.alphaBlack60,
    shadowMd02: InvPrimitives.alphaBlack40,
    shadowLg01: InvPrimitives.alphaBlack60,
    shadowLg02: InvPrimitives.alphaBlack40,
    shadowLg03: InvPrimitives.alphaBlack40,
    shadowXl01: InvPrimitives.alphaBlack60,
    shadowXl02: InvPrimitives.alphaBlack40,
    shadowXl03: InvPrimitives.alphaBlack40,
    shadow2xl01: InvPrimitives.alphaBlack60,
    shadow2xl02: InvPrimitives.alphaBlack40,
    shadow3xl01: InvPrimitives.alphaBlack60,
    shadow3xl02: InvPrimitives.alphaBlack40,
    textDisabled: InvPrimitives.neutral600,
    textErrorPrimary: InvPrimitives.red300,
    textErrorPrimaryHover: InvPrimitives.red300,
    textInfoPrimary: InvPrimitives.blue300,
    textInverse: InvPrimitives.neutral950,
    textPlaceholder: InvPrimitives.neutral400,
    textPrimary: InvPrimitives.neutral200,
    textQuaternary: InvPrimitives.neutral400,
    textSecondary: InvPrimitives.neutral300,
    textSecondaryHover: InvPrimitives.neutral200,
    textSuccessPrimary: InvPrimitives.green300,
    textTertiary: InvPrimitives.neutral400,
    textTertiaryHover: InvPrimitives.neutral300,
    textTertiaryStrong: InvPrimitives.neutral300,
    textWarningPrimary: InvPrimitives.yellow300,
    textWhite: InvPrimitives.white,
    utilityBlue100: InvPrimitives.blue900,
    utilityBlue200: InvPrimitives.blue800,
    utilityBlue300: InvPrimitives.blue700,
    utilityBlue400: InvPrimitives.blue600,
    utilityBlue50: InvPrimitives.blue950,
    utilityBlue500: InvPrimitives.blue400,
    utilityBlue600: InvPrimitives.blue400,
    utilityBlue700: InvPrimitives.blue300,
    utilityGreen100: InvPrimitives.green900,
    utilityGreen200: InvPrimitives.green800,
    utilityGreen300: InvPrimitives.green700,
    utilityGreen400: InvPrimitives.green600,
    utilityGreen50: InvPrimitives.green950,
    utilityGreen500: InvPrimitives.green400,
    utilityGreen600: InvPrimitives.green400,
    utilityGreen700: InvPrimitives.green300,
    utilityNeutral100: InvPrimitives.dark3,
    utilityNeutral200: InvPrimitives.neutral800,
    utilityNeutral300: InvPrimitives.neutral700,
    utilityNeutral400: InvPrimitives.neutral600,
    utilityNeutral50: InvPrimitives.neutral950,
    utilityNeutral500: InvPrimitives.neutral400,
    utilityNeutral600: InvPrimitives.neutral400,
    utilityNeutral700: InvPrimitives.neutral300,
    utilityOrange100: InvPrimitives.orange950,
    utilityOrange200: InvPrimitives.orange800,
    utilityOrange300: InvPrimitives.orange700,
    utilityOrange400: InvPrimitives.orange600,
    utilityOrange50: InvPrimitives.orange950,
    utilityOrange500: InvPrimitives.orange400,
    utilityOrange600: InvPrimitives.orange400,
    utilityOrange700: InvPrimitives.orange300,
    utilityOrange800: InvPrimitives.orange300,
    utilityPurple100: InvPrimitives.purple900,
    utilityPurple200: InvPrimitives.purple800,
    utilityPurple300: InvPrimitives.purple700,
    utilityPurple400: InvPrimitives.purple600,
    utilityPurple50: InvPrimitives.purple950,
    utilityPurple500: InvPrimitives.purple400,
    utilityPurple600: InvPrimitives.purple400,
    utilityPurple700: InvPrimitives.purple300,
    utilityRed100: InvPrimitives.red900,
    utilityRed200: InvPrimitives.red800,
    utilityRed300: InvPrimitives.red700,
    utilityRed400: InvPrimitives.red600,
    utilityRed50: InvPrimitives.red950,
    utilityRed500: InvPrimitives.red400,
    utilityRed600: InvPrimitives.red400,
    utilityRed700: InvPrimitives.red300,
    utilityTeal100: InvPrimitives.teal900,
    utilityTeal200: InvPrimitives.teal800,
    utilityTeal300: InvPrimitives.teal700,
    utilityTeal400: InvPrimitives.teal600,
    utilityTeal50: InvPrimitives.teal950,
    utilityTeal500: InvPrimitives.teal400,
    utilityTeal600: InvPrimitives.teal400,
    utilityTeal700: InvPrimitives.teal300,
    utilityYellow100: InvPrimitives.yellow900,
    utilityYellow200: InvPrimitives.yellow800,
    utilityYellow300: InvPrimitives.yellow700,
    utilityYellow400: InvPrimitives.yellow600,
    utilityYellow50: InvPrimitives.yellow950,
    utilityYellow500: InvPrimitives.yellow400,
    utilityYellow600: InvPrimitives.yellow400,
    utilityYellow700: InvPrimitives.yellow300,
    borderInputHover: InvPrimitives.neutral300,
    bgErrorOverlay: InvPrimitives.alphaRed70055,
    vehicleMediaBg: InvPrimitives.neutral700,
    vehicleOutline: InvPrimitives.neutral400,
    logoBg: InvPrimitives.white,
    fileTypePdf: InvPrimitives.fileTypePdf,
    fileTypeDoc: InvPrimitives.fileTypeDoc,
    fileTypeXls: InvPrimitives.fileTypeXls,
    fileTypeCsv: InvPrimitives.fileTypeCsv,
    fileTypeImg: InvPrimitives.fileTypeImg,
    fileTypeZip: InvPrimitives.fileTypeZip,
    fileTypeVid: InvPrimitives.fileTypeVid,
  );

  @override
  InvColors copyWith({Color? actionPrimary, Color? actionPrimaryHover, Color? actionPrimaryPressed, Color? actionSecondary, Color? actionSecondaryHover, Color? actionSecondaryPressed, Color? bgDisabled, Color? bgErrorPrimary, Color? bgErrorPrimaryHover, Color? bgErrorPrimaryPressed, Color? bgErrorSecondary, Color? bgErrorSolid, Color? bgErrorSolidHover, Color? bgInfoPrimary, Color? bgInfoSecondary, Color? bgInfoSolid, Color? bgInfoSolidHover, Color? bgOverlay, Color? bgOverlaySolid, Color? bgPrimaryBlur, Color? bgPressed, Color? bgPrimary, Color? bgPrimaryAlt, Color? bgPrimaryHover, Color? bgPrimarySolid, Color? bgQuaternary, Color? bgQuaternaryHover, Color? bgSecondary, Color? bgSecondaryAlt, Color? bgSecondaryHover, Color? bgSecondarySolid, Color? bgSelected, Color? bgSkeleton, Color? bgSuccessPrimary, Color? bgSuccessSecondary, Color? bgSuccessSolid, Color? bgSuccessSolidHover, Color? bgTertiary, Color? bgWarningPrimary, Color? bgWarningSecondary, Color? bgWarningSolid, Color? bgWarningSolidHover, Color? borderDisabled, Color? borderError, Color? borderErrorSubtle, Color? borderInfo, Color? borderInfoSubtle, Color? borderInput, Color? borderPrimary, Color? borderSecondary, Color? borderSecondaryAlt, Color? borderSuccess, Color? borderSuccessSubtle, Color? borderTertiary, Color? borderWarning, Color? borderWarningSubtle, Color? fgDisabled, Color? fgErrorPrimary, Color? fgErrorSecondary, Color? fgInfoPrimary, Color? fgInverse, Color? fgPrimary, Color? fgQuaternary, Color? fgQuaternaryHover, Color? fgSecondary, Color? fgSecondaryHover, Color? fgSuccessPrimary, Color? fgSuccessSecondary, Color? fgTertiary, Color? fgTertiaryHover, Color? fgWarningPrimary, Color? fgWarningSecondary, Color? fgWhite, Color? focusRing, Color? focusRingError, Color? shadowXs, Color? shadowSm01, Color? shadowSm02, Color? shadowMd01, Color? shadowMd02, Color? shadowLg01, Color? shadowLg02, Color? shadowLg03, Color? shadowXl01, Color? shadowXl02, Color? shadowXl03, Color? shadow2xl01, Color? shadow2xl02, Color? shadow3xl01, Color? shadow3xl02, Color? textDisabled, Color? textErrorPrimary, Color? textErrorPrimaryHover, Color? textInfoPrimary, Color? textInverse, Color? textPlaceholder, Color? textPrimary, Color? textQuaternary, Color? textSecondary, Color? textSecondaryHover, Color? textSuccessPrimary, Color? textTertiary, Color? textTertiaryHover, Color? textTertiaryStrong, Color? textWarningPrimary, Color? textWhite, Color? utilityBlue100, Color? utilityBlue200, Color? utilityBlue300, Color? utilityBlue400, Color? utilityBlue50, Color? utilityBlue500, Color? utilityBlue600, Color? utilityBlue700, Color? utilityGreen100, Color? utilityGreen200, Color? utilityGreen300, Color? utilityGreen400, Color? utilityGreen50, Color? utilityGreen500, Color? utilityGreen600, Color? utilityGreen700, Color? utilityNeutral100, Color? utilityNeutral200, Color? utilityNeutral300, Color? utilityNeutral400, Color? utilityNeutral50, Color? utilityNeutral500, Color? utilityNeutral600, Color? utilityNeutral700, Color? utilityOrange100, Color? utilityOrange200, Color? utilityOrange300, Color? utilityOrange400, Color? utilityOrange50, Color? utilityOrange500, Color? utilityOrange600, Color? utilityOrange700, Color? utilityOrange800, Color? utilityPurple100, Color? utilityPurple200, Color? utilityPurple300, Color? utilityPurple400, Color? utilityPurple50, Color? utilityPurple500, Color? utilityPurple600, Color? utilityPurple700, Color? utilityRed100, Color? utilityRed200, Color? utilityRed300, Color? utilityRed400, Color? utilityRed50, Color? utilityRed500, Color? utilityRed600, Color? utilityRed700, Color? utilityTeal100, Color? utilityTeal200, Color? utilityTeal300, Color? utilityTeal400, Color? utilityTeal50, Color? utilityTeal500, Color? utilityTeal600, Color? utilityTeal700, Color? utilityYellow100, Color? utilityYellow200, Color? utilityYellow300, Color? utilityYellow400, Color? utilityYellow50, Color? utilityYellow500, Color? utilityYellow600, Color? utilityYellow700, Color? borderInputHover, Color? bgErrorOverlay, Color? vehicleMediaBg, Color? vehicleOutline, Color? logoBg, Color? fileTypePdf, Color? fileTypeDoc, Color? fileTypeXls, Color? fileTypeCsv, Color? fileTypeImg, Color? fileTypeZip, Color? fileTypeVid}) =>
      InvColors(actionPrimary: actionPrimary ?? this.actionPrimary, actionPrimaryHover: actionPrimaryHover ?? this.actionPrimaryHover, actionPrimaryPressed: actionPrimaryPressed ?? this.actionPrimaryPressed, actionSecondary: actionSecondary ?? this.actionSecondary, actionSecondaryHover: actionSecondaryHover ?? this.actionSecondaryHover, actionSecondaryPressed: actionSecondaryPressed ?? this.actionSecondaryPressed, bgDisabled: bgDisabled ?? this.bgDisabled, bgErrorPrimary: bgErrorPrimary ?? this.bgErrorPrimary, bgErrorPrimaryHover: bgErrorPrimaryHover ?? this.bgErrorPrimaryHover, bgErrorPrimaryPressed: bgErrorPrimaryPressed ?? this.bgErrorPrimaryPressed, bgErrorSecondary: bgErrorSecondary ?? this.bgErrorSecondary, bgErrorSolid: bgErrorSolid ?? this.bgErrorSolid, bgErrorSolidHover: bgErrorSolidHover ?? this.bgErrorSolidHover, bgInfoPrimary: bgInfoPrimary ?? this.bgInfoPrimary, bgInfoSecondary: bgInfoSecondary ?? this.bgInfoSecondary, bgInfoSolid: bgInfoSolid ?? this.bgInfoSolid, bgInfoSolidHover: bgInfoSolidHover ?? this.bgInfoSolidHover, bgOverlay: bgOverlay ?? this.bgOverlay, bgOverlaySolid: bgOverlaySolid ?? this.bgOverlaySolid, bgPrimaryBlur: bgPrimaryBlur ?? this.bgPrimaryBlur, bgPressed: bgPressed ?? this.bgPressed, bgPrimary: bgPrimary ?? this.bgPrimary, bgPrimaryAlt: bgPrimaryAlt ?? this.bgPrimaryAlt, bgPrimaryHover: bgPrimaryHover ?? this.bgPrimaryHover, bgPrimarySolid: bgPrimarySolid ?? this.bgPrimarySolid, bgQuaternary: bgQuaternary ?? this.bgQuaternary, bgQuaternaryHover: bgQuaternaryHover ?? this.bgQuaternaryHover, bgSecondary: bgSecondary ?? this.bgSecondary, bgSecondaryAlt: bgSecondaryAlt ?? this.bgSecondaryAlt, bgSecondaryHover: bgSecondaryHover ?? this.bgSecondaryHover, bgSecondarySolid: bgSecondarySolid ?? this.bgSecondarySolid, bgSelected: bgSelected ?? this.bgSelected, bgSkeleton: bgSkeleton ?? this.bgSkeleton, bgSuccessPrimary: bgSuccessPrimary ?? this.bgSuccessPrimary, bgSuccessSecondary: bgSuccessSecondary ?? this.bgSuccessSecondary, bgSuccessSolid: bgSuccessSolid ?? this.bgSuccessSolid, bgSuccessSolidHover: bgSuccessSolidHover ?? this.bgSuccessSolidHover, bgTertiary: bgTertiary ?? this.bgTertiary, bgWarningPrimary: bgWarningPrimary ?? this.bgWarningPrimary, bgWarningSecondary: bgWarningSecondary ?? this.bgWarningSecondary, bgWarningSolid: bgWarningSolid ?? this.bgWarningSolid, bgWarningSolidHover: bgWarningSolidHover ?? this.bgWarningSolidHover, borderDisabled: borderDisabled ?? this.borderDisabled, borderError: borderError ?? this.borderError, borderErrorSubtle: borderErrorSubtle ?? this.borderErrorSubtle, borderInfo: borderInfo ?? this.borderInfo, borderInfoSubtle: borderInfoSubtle ?? this.borderInfoSubtle, borderInput: borderInput ?? this.borderInput, borderPrimary: borderPrimary ?? this.borderPrimary, borderSecondary: borderSecondary ?? this.borderSecondary, borderSecondaryAlt: borderSecondaryAlt ?? this.borderSecondaryAlt, borderSuccess: borderSuccess ?? this.borderSuccess, borderSuccessSubtle: borderSuccessSubtle ?? this.borderSuccessSubtle, borderTertiary: borderTertiary ?? this.borderTertiary, borderWarning: borderWarning ?? this.borderWarning, borderWarningSubtle: borderWarningSubtle ?? this.borderWarningSubtle, fgDisabled: fgDisabled ?? this.fgDisabled, fgErrorPrimary: fgErrorPrimary ?? this.fgErrorPrimary, fgErrorSecondary: fgErrorSecondary ?? this.fgErrorSecondary, fgInfoPrimary: fgInfoPrimary ?? this.fgInfoPrimary, fgInverse: fgInverse ?? this.fgInverse, fgPrimary: fgPrimary ?? this.fgPrimary, fgQuaternary: fgQuaternary ?? this.fgQuaternary, fgQuaternaryHover: fgQuaternaryHover ?? this.fgQuaternaryHover, fgSecondary: fgSecondary ?? this.fgSecondary, fgSecondaryHover: fgSecondaryHover ?? this.fgSecondaryHover, fgSuccessPrimary: fgSuccessPrimary ?? this.fgSuccessPrimary, fgSuccessSecondary: fgSuccessSecondary ?? this.fgSuccessSecondary, fgTertiary: fgTertiary ?? this.fgTertiary, fgTertiaryHover: fgTertiaryHover ?? this.fgTertiaryHover, fgWarningPrimary: fgWarningPrimary ?? this.fgWarningPrimary, fgWarningSecondary: fgWarningSecondary ?? this.fgWarningSecondary, fgWhite: fgWhite ?? this.fgWhite, focusRing: focusRing ?? this.focusRing, focusRingError: focusRingError ?? this.focusRingError, shadowXs: shadowXs ?? this.shadowXs, shadowSm01: shadowSm01 ?? this.shadowSm01, shadowSm02: shadowSm02 ?? this.shadowSm02, shadowMd01: shadowMd01 ?? this.shadowMd01, shadowMd02: shadowMd02 ?? this.shadowMd02, shadowLg01: shadowLg01 ?? this.shadowLg01, shadowLg02: shadowLg02 ?? this.shadowLg02, shadowLg03: shadowLg03 ?? this.shadowLg03, shadowXl01: shadowXl01 ?? this.shadowXl01, shadowXl02: shadowXl02 ?? this.shadowXl02, shadowXl03: shadowXl03 ?? this.shadowXl03, shadow2xl01: shadow2xl01 ?? this.shadow2xl01, shadow2xl02: shadow2xl02 ?? this.shadow2xl02, shadow3xl01: shadow3xl01 ?? this.shadow3xl01, shadow3xl02: shadow3xl02 ?? this.shadow3xl02, textDisabled: textDisabled ?? this.textDisabled, textErrorPrimary: textErrorPrimary ?? this.textErrorPrimary, textErrorPrimaryHover: textErrorPrimaryHover ?? this.textErrorPrimaryHover, textInfoPrimary: textInfoPrimary ?? this.textInfoPrimary, textInverse: textInverse ?? this.textInverse, textPlaceholder: textPlaceholder ?? this.textPlaceholder, textPrimary: textPrimary ?? this.textPrimary, textQuaternary: textQuaternary ?? this.textQuaternary, textSecondary: textSecondary ?? this.textSecondary, textSecondaryHover: textSecondaryHover ?? this.textSecondaryHover, textSuccessPrimary: textSuccessPrimary ?? this.textSuccessPrimary, textTertiary: textTertiary ?? this.textTertiary, textTertiaryHover: textTertiaryHover ?? this.textTertiaryHover, textTertiaryStrong: textTertiaryStrong ?? this.textTertiaryStrong, textWarningPrimary: textWarningPrimary ?? this.textWarningPrimary, textWhite: textWhite ?? this.textWhite, utilityBlue100: utilityBlue100 ?? this.utilityBlue100, utilityBlue200: utilityBlue200 ?? this.utilityBlue200, utilityBlue300: utilityBlue300 ?? this.utilityBlue300, utilityBlue400: utilityBlue400 ?? this.utilityBlue400, utilityBlue50: utilityBlue50 ?? this.utilityBlue50, utilityBlue500: utilityBlue500 ?? this.utilityBlue500, utilityBlue600: utilityBlue600 ?? this.utilityBlue600, utilityBlue700: utilityBlue700 ?? this.utilityBlue700, utilityGreen100: utilityGreen100 ?? this.utilityGreen100, utilityGreen200: utilityGreen200 ?? this.utilityGreen200, utilityGreen300: utilityGreen300 ?? this.utilityGreen300, utilityGreen400: utilityGreen400 ?? this.utilityGreen400, utilityGreen50: utilityGreen50 ?? this.utilityGreen50, utilityGreen500: utilityGreen500 ?? this.utilityGreen500, utilityGreen600: utilityGreen600 ?? this.utilityGreen600, utilityGreen700: utilityGreen700 ?? this.utilityGreen700, utilityNeutral100: utilityNeutral100 ?? this.utilityNeutral100, utilityNeutral200: utilityNeutral200 ?? this.utilityNeutral200, utilityNeutral300: utilityNeutral300 ?? this.utilityNeutral300, utilityNeutral400: utilityNeutral400 ?? this.utilityNeutral400, utilityNeutral50: utilityNeutral50 ?? this.utilityNeutral50, utilityNeutral500: utilityNeutral500 ?? this.utilityNeutral500, utilityNeutral600: utilityNeutral600 ?? this.utilityNeutral600, utilityNeutral700: utilityNeutral700 ?? this.utilityNeutral700, utilityOrange100: utilityOrange100 ?? this.utilityOrange100, utilityOrange200: utilityOrange200 ?? this.utilityOrange200, utilityOrange300: utilityOrange300 ?? this.utilityOrange300, utilityOrange400: utilityOrange400 ?? this.utilityOrange400, utilityOrange50: utilityOrange50 ?? this.utilityOrange50, utilityOrange500: utilityOrange500 ?? this.utilityOrange500, utilityOrange600: utilityOrange600 ?? this.utilityOrange600, utilityOrange700: utilityOrange700 ?? this.utilityOrange700, utilityOrange800: utilityOrange800 ?? this.utilityOrange800, utilityPurple100: utilityPurple100 ?? this.utilityPurple100, utilityPurple200: utilityPurple200 ?? this.utilityPurple200, utilityPurple300: utilityPurple300 ?? this.utilityPurple300, utilityPurple400: utilityPurple400 ?? this.utilityPurple400, utilityPurple50: utilityPurple50 ?? this.utilityPurple50, utilityPurple500: utilityPurple500 ?? this.utilityPurple500, utilityPurple600: utilityPurple600 ?? this.utilityPurple600, utilityPurple700: utilityPurple700 ?? this.utilityPurple700, utilityRed100: utilityRed100 ?? this.utilityRed100, utilityRed200: utilityRed200 ?? this.utilityRed200, utilityRed300: utilityRed300 ?? this.utilityRed300, utilityRed400: utilityRed400 ?? this.utilityRed400, utilityRed50: utilityRed50 ?? this.utilityRed50, utilityRed500: utilityRed500 ?? this.utilityRed500, utilityRed600: utilityRed600 ?? this.utilityRed600, utilityRed700: utilityRed700 ?? this.utilityRed700, utilityTeal100: utilityTeal100 ?? this.utilityTeal100, utilityTeal200: utilityTeal200 ?? this.utilityTeal200, utilityTeal300: utilityTeal300 ?? this.utilityTeal300, utilityTeal400: utilityTeal400 ?? this.utilityTeal400, utilityTeal50: utilityTeal50 ?? this.utilityTeal50, utilityTeal500: utilityTeal500 ?? this.utilityTeal500, utilityTeal600: utilityTeal600 ?? this.utilityTeal600, utilityTeal700: utilityTeal700 ?? this.utilityTeal700, utilityYellow100: utilityYellow100 ?? this.utilityYellow100, utilityYellow200: utilityYellow200 ?? this.utilityYellow200, utilityYellow300: utilityYellow300 ?? this.utilityYellow300, utilityYellow400: utilityYellow400 ?? this.utilityYellow400, utilityYellow50: utilityYellow50 ?? this.utilityYellow50, utilityYellow500: utilityYellow500 ?? this.utilityYellow500, utilityYellow600: utilityYellow600 ?? this.utilityYellow600, utilityYellow700: utilityYellow700 ?? this.utilityYellow700, borderInputHover: borderInputHover ?? this.borderInputHover, bgErrorOverlay: bgErrorOverlay ?? this.bgErrorOverlay, vehicleMediaBg: vehicleMediaBg ?? this.vehicleMediaBg, vehicleOutline: vehicleOutline ?? this.vehicleOutline, logoBg: logoBg ?? this.logoBg, fileTypePdf: fileTypePdf ?? this.fileTypePdf, fileTypeDoc: fileTypeDoc ?? this.fileTypeDoc, fileTypeXls: fileTypeXls ?? this.fileTypeXls, fileTypeCsv: fileTypeCsv ?? this.fileTypeCsv, fileTypeImg: fileTypeImg ?? this.fileTypeImg, fileTypeZip: fileTypeZip ?? this.fileTypeZip, fileTypeVid: fileTypeVid ?? this.fileTypeVid);

  @override
  InvColors lerp(covariant ThemeExtension<InvColors>? other, double t) {
    if (other is! InvColors) return this;
    return InvColors(actionPrimary: Color.lerp(actionPrimary, other.actionPrimary, t)!, actionPrimaryHover: Color.lerp(actionPrimaryHover, other.actionPrimaryHover, t)!, actionPrimaryPressed: Color.lerp(actionPrimaryPressed, other.actionPrimaryPressed, t)!, actionSecondary: Color.lerp(actionSecondary, other.actionSecondary, t)!, actionSecondaryHover: Color.lerp(actionSecondaryHover, other.actionSecondaryHover, t)!, actionSecondaryPressed: Color.lerp(actionSecondaryPressed, other.actionSecondaryPressed, t)!, bgDisabled: Color.lerp(bgDisabled, other.bgDisabled, t)!, bgErrorPrimary: Color.lerp(bgErrorPrimary, other.bgErrorPrimary, t)!, bgErrorPrimaryHover: Color.lerp(bgErrorPrimaryHover, other.bgErrorPrimaryHover, t)!, bgErrorPrimaryPressed: Color.lerp(bgErrorPrimaryPressed, other.bgErrorPrimaryPressed, t)!, bgErrorSecondary: Color.lerp(bgErrorSecondary, other.bgErrorSecondary, t)!, bgErrorSolid: Color.lerp(bgErrorSolid, other.bgErrorSolid, t)!, bgErrorSolidHover: Color.lerp(bgErrorSolidHover, other.bgErrorSolidHover, t)!, bgInfoPrimary: Color.lerp(bgInfoPrimary, other.bgInfoPrimary, t)!, bgInfoSecondary: Color.lerp(bgInfoSecondary, other.bgInfoSecondary, t)!, bgInfoSolid: Color.lerp(bgInfoSolid, other.bgInfoSolid, t)!, bgInfoSolidHover: Color.lerp(bgInfoSolidHover, other.bgInfoSolidHover, t)!, bgOverlay: Color.lerp(bgOverlay, other.bgOverlay, t)!, bgOverlaySolid: Color.lerp(bgOverlaySolid, other.bgOverlaySolid, t)!, bgPrimaryBlur: Color.lerp(bgPrimaryBlur, other.bgPrimaryBlur, t)!, bgPressed: Color.lerp(bgPressed, other.bgPressed, t)!, bgPrimary: Color.lerp(bgPrimary, other.bgPrimary, t)!, bgPrimaryAlt: Color.lerp(bgPrimaryAlt, other.bgPrimaryAlt, t)!, bgPrimaryHover: Color.lerp(bgPrimaryHover, other.bgPrimaryHover, t)!, bgPrimarySolid: Color.lerp(bgPrimarySolid, other.bgPrimarySolid, t)!, bgQuaternary: Color.lerp(bgQuaternary, other.bgQuaternary, t)!, bgQuaternaryHover: Color.lerp(bgQuaternaryHover, other.bgQuaternaryHover, t)!, bgSecondary: Color.lerp(bgSecondary, other.bgSecondary, t)!, bgSecondaryAlt: Color.lerp(bgSecondaryAlt, other.bgSecondaryAlt, t)!, bgSecondaryHover: Color.lerp(bgSecondaryHover, other.bgSecondaryHover, t)!, bgSecondarySolid: Color.lerp(bgSecondarySolid, other.bgSecondarySolid, t)!, bgSelected: Color.lerp(bgSelected, other.bgSelected, t)!, bgSkeleton: Color.lerp(bgSkeleton, other.bgSkeleton, t)!, bgSuccessPrimary: Color.lerp(bgSuccessPrimary, other.bgSuccessPrimary, t)!, bgSuccessSecondary: Color.lerp(bgSuccessSecondary, other.bgSuccessSecondary, t)!, bgSuccessSolid: Color.lerp(bgSuccessSolid, other.bgSuccessSolid, t)!, bgSuccessSolidHover: Color.lerp(bgSuccessSolidHover, other.bgSuccessSolidHover, t)!, bgTertiary: Color.lerp(bgTertiary, other.bgTertiary, t)!, bgWarningPrimary: Color.lerp(bgWarningPrimary, other.bgWarningPrimary, t)!, bgWarningSecondary: Color.lerp(bgWarningSecondary, other.bgWarningSecondary, t)!, bgWarningSolid: Color.lerp(bgWarningSolid, other.bgWarningSolid, t)!, bgWarningSolidHover: Color.lerp(bgWarningSolidHover, other.bgWarningSolidHover, t)!, borderDisabled: Color.lerp(borderDisabled, other.borderDisabled, t)!, borderError: Color.lerp(borderError, other.borderError, t)!, borderErrorSubtle: Color.lerp(borderErrorSubtle, other.borderErrorSubtle, t)!, borderInfo: Color.lerp(borderInfo, other.borderInfo, t)!, borderInfoSubtle: Color.lerp(borderInfoSubtle, other.borderInfoSubtle, t)!, borderInput: Color.lerp(borderInput, other.borderInput, t)!, borderPrimary: Color.lerp(borderPrimary, other.borderPrimary, t)!, borderSecondary: Color.lerp(borderSecondary, other.borderSecondary, t)!, borderSecondaryAlt: Color.lerp(borderSecondaryAlt, other.borderSecondaryAlt, t)!, borderSuccess: Color.lerp(borderSuccess, other.borderSuccess, t)!, borderSuccessSubtle: Color.lerp(borderSuccessSubtle, other.borderSuccessSubtle, t)!, borderTertiary: Color.lerp(borderTertiary, other.borderTertiary, t)!, borderWarning: Color.lerp(borderWarning, other.borderWarning, t)!, borderWarningSubtle: Color.lerp(borderWarningSubtle, other.borderWarningSubtle, t)!, fgDisabled: Color.lerp(fgDisabled, other.fgDisabled, t)!, fgErrorPrimary: Color.lerp(fgErrorPrimary, other.fgErrorPrimary, t)!, fgErrorSecondary: Color.lerp(fgErrorSecondary, other.fgErrorSecondary, t)!, fgInfoPrimary: Color.lerp(fgInfoPrimary, other.fgInfoPrimary, t)!, fgInverse: Color.lerp(fgInverse, other.fgInverse, t)!, fgPrimary: Color.lerp(fgPrimary, other.fgPrimary, t)!, fgQuaternary: Color.lerp(fgQuaternary, other.fgQuaternary, t)!, fgQuaternaryHover: Color.lerp(fgQuaternaryHover, other.fgQuaternaryHover, t)!, fgSecondary: Color.lerp(fgSecondary, other.fgSecondary, t)!, fgSecondaryHover: Color.lerp(fgSecondaryHover, other.fgSecondaryHover, t)!, fgSuccessPrimary: Color.lerp(fgSuccessPrimary, other.fgSuccessPrimary, t)!, fgSuccessSecondary: Color.lerp(fgSuccessSecondary, other.fgSuccessSecondary, t)!, fgTertiary: Color.lerp(fgTertiary, other.fgTertiary, t)!, fgTertiaryHover: Color.lerp(fgTertiaryHover, other.fgTertiaryHover, t)!, fgWarningPrimary: Color.lerp(fgWarningPrimary, other.fgWarningPrimary, t)!, fgWarningSecondary: Color.lerp(fgWarningSecondary, other.fgWarningSecondary, t)!, fgWhite: Color.lerp(fgWhite, other.fgWhite, t)!, focusRing: Color.lerp(focusRing, other.focusRing, t)!, focusRingError: Color.lerp(focusRingError, other.focusRingError, t)!, shadowXs: Color.lerp(shadowXs, other.shadowXs, t)!, shadowSm01: Color.lerp(shadowSm01, other.shadowSm01, t)!, shadowSm02: Color.lerp(shadowSm02, other.shadowSm02, t)!, shadowMd01: Color.lerp(shadowMd01, other.shadowMd01, t)!, shadowMd02: Color.lerp(shadowMd02, other.shadowMd02, t)!, shadowLg01: Color.lerp(shadowLg01, other.shadowLg01, t)!, shadowLg02: Color.lerp(shadowLg02, other.shadowLg02, t)!, shadowLg03: Color.lerp(shadowLg03, other.shadowLg03, t)!, shadowXl01: Color.lerp(shadowXl01, other.shadowXl01, t)!, shadowXl02: Color.lerp(shadowXl02, other.shadowXl02, t)!, shadowXl03: Color.lerp(shadowXl03, other.shadowXl03, t)!, shadow2xl01: Color.lerp(shadow2xl01, other.shadow2xl01, t)!, shadow2xl02: Color.lerp(shadow2xl02, other.shadow2xl02, t)!, shadow3xl01: Color.lerp(shadow3xl01, other.shadow3xl01, t)!, shadow3xl02: Color.lerp(shadow3xl02, other.shadow3xl02, t)!, textDisabled: Color.lerp(textDisabled, other.textDisabled, t)!, textErrorPrimary: Color.lerp(textErrorPrimary, other.textErrorPrimary, t)!, textErrorPrimaryHover: Color.lerp(textErrorPrimaryHover, other.textErrorPrimaryHover, t)!, textInfoPrimary: Color.lerp(textInfoPrimary, other.textInfoPrimary, t)!, textInverse: Color.lerp(textInverse, other.textInverse, t)!, textPlaceholder: Color.lerp(textPlaceholder, other.textPlaceholder, t)!, textPrimary: Color.lerp(textPrimary, other.textPrimary, t)!, textQuaternary: Color.lerp(textQuaternary, other.textQuaternary, t)!, textSecondary: Color.lerp(textSecondary, other.textSecondary, t)!, textSecondaryHover: Color.lerp(textSecondaryHover, other.textSecondaryHover, t)!, textSuccessPrimary: Color.lerp(textSuccessPrimary, other.textSuccessPrimary, t)!, textTertiary: Color.lerp(textTertiary, other.textTertiary, t)!, textTertiaryHover: Color.lerp(textTertiaryHover, other.textTertiaryHover, t)!, textTertiaryStrong: Color.lerp(textTertiaryStrong, other.textTertiaryStrong, t)!, textWarningPrimary: Color.lerp(textWarningPrimary, other.textWarningPrimary, t)!, textWhite: Color.lerp(textWhite, other.textWhite, t)!, utilityBlue100: Color.lerp(utilityBlue100, other.utilityBlue100, t)!, utilityBlue200: Color.lerp(utilityBlue200, other.utilityBlue200, t)!, utilityBlue300: Color.lerp(utilityBlue300, other.utilityBlue300, t)!, utilityBlue400: Color.lerp(utilityBlue400, other.utilityBlue400, t)!, utilityBlue50: Color.lerp(utilityBlue50, other.utilityBlue50, t)!, utilityBlue500: Color.lerp(utilityBlue500, other.utilityBlue500, t)!, utilityBlue600: Color.lerp(utilityBlue600, other.utilityBlue600, t)!, utilityBlue700: Color.lerp(utilityBlue700, other.utilityBlue700, t)!, utilityGreen100: Color.lerp(utilityGreen100, other.utilityGreen100, t)!, utilityGreen200: Color.lerp(utilityGreen200, other.utilityGreen200, t)!, utilityGreen300: Color.lerp(utilityGreen300, other.utilityGreen300, t)!, utilityGreen400: Color.lerp(utilityGreen400, other.utilityGreen400, t)!, utilityGreen50: Color.lerp(utilityGreen50, other.utilityGreen50, t)!, utilityGreen500: Color.lerp(utilityGreen500, other.utilityGreen500, t)!, utilityGreen600: Color.lerp(utilityGreen600, other.utilityGreen600, t)!, utilityGreen700: Color.lerp(utilityGreen700, other.utilityGreen700, t)!, utilityNeutral100: Color.lerp(utilityNeutral100, other.utilityNeutral100, t)!, utilityNeutral200: Color.lerp(utilityNeutral200, other.utilityNeutral200, t)!, utilityNeutral300: Color.lerp(utilityNeutral300, other.utilityNeutral300, t)!, utilityNeutral400: Color.lerp(utilityNeutral400, other.utilityNeutral400, t)!, utilityNeutral50: Color.lerp(utilityNeutral50, other.utilityNeutral50, t)!, utilityNeutral500: Color.lerp(utilityNeutral500, other.utilityNeutral500, t)!, utilityNeutral600: Color.lerp(utilityNeutral600, other.utilityNeutral600, t)!, utilityNeutral700: Color.lerp(utilityNeutral700, other.utilityNeutral700, t)!, utilityOrange100: Color.lerp(utilityOrange100, other.utilityOrange100, t)!, utilityOrange200: Color.lerp(utilityOrange200, other.utilityOrange200, t)!, utilityOrange300: Color.lerp(utilityOrange300, other.utilityOrange300, t)!, utilityOrange400: Color.lerp(utilityOrange400, other.utilityOrange400, t)!, utilityOrange50: Color.lerp(utilityOrange50, other.utilityOrange50, t)!, utilityOrange500: Color.lerp(utilityOrange500, other.utilityOrange500, t)!, utilityOrange600: Color.lerp(utilityOrange600, other.utilityOrange600, t)!, utilityOrange700: Color.lerp(utilityOrange700, other.utilityOrange700, t)!, utilityOrange800: Color.lerp(utilityOrange800, other.utilityOrange800, t)!, utilityPurple100: Color.lerp(utilityPurple100, other.utilityPurple100, t)!, utilityPurple200: Color.lerp(utilityPurple200, other.utilityPurple200, t)!, utilityPurple300: Color.lerp(utilityPurple300, other.utilityPurple300, t)!, utilityPurple400: Color.lerp(utilityPurple400, other.utilityPurple400, t)!, utilityPurple50: Color.lerp(utilityPurple50, other.utilityPurple50, t)!, utilityPurple500: Color.lerp(utilityPurple500, other.utilityPurple500, t)!, utilityPurple600: Color.lerp(utilityPurple600, other.utilityPurple600, t)!, utilityPurple700: Color.lerp(utilityPurple700, other.utilityPurple700, t)!, utilityRed100: Color.lerp(utilityRed100, other.utilityRed100, t)!, utilityRed200: Color.lerp(utilityRed200, other.utilityRed200, t)!, utilityRed300: Color.lerp(utilityRed300, other.utilityRed300, t)!, utilityRed400: Color.lerp(utilityRed400, other.utilityRed400, t)!, utilityRed50: Color.lerp(utilityRed50, other.utilityRed50, t)!, utilityRed500: Color.lerp(utilityRed500, other.utilityRed500, t)!, utilityRed600: Color.lerp(utilityRed600, other.utilityRed600, t)!, utilityRed700: Color.lerp(utilityRed700, other.utilityRed700, t)!, utilityTeal100: Color.lerp(utilityTeal100, other.utilityTeal100, t)!, utilityTeal200: Color.lerp(utilityTeal200, other.utilityTeal200, t)!, utilityTeal300: Color.lerp(utilityTeal300, other.utilityTeal300, t)!, utilityTeal400: Color.lerp(utilityTeal400, other.utilityTeal400, t)!, utilityTeal50: Color.lerp(utilityTeal50, other.utilityTeal50, t)!, utilityTeal500: Color.lerp(utilityTeal500, other.utilityTeal500, t)!, utilityTeal600: Color.lerp(utilityTeal600, other.utilityTeal600, t)!, utilityTeal700: Color.lerp(utilityTeal700, other.utilityTeal700, t)!, utilityYellow100: Color.lerp(utilityYellow100, other.utilityYellow100, t)!, utilityYellow200: Color.lerp(utilityYellow200, other.utilityYellow200, t)!, utilityYellow300: Color.lerp(utilityYellow300, other.utilityYellow300, t)!, utilityYellow400: Color.lerp(utilityYellow400, other.utilityYellow400, t)!, utilityYellow50: Color.lerp(utilityYellow50, other.utilityYellow50, t)!, utilityYellow500: Color.lerp(utilityYellow500, other.utilityYellow500, t)!, utilityYellow600: Color.lerp(utilityYellow600, other.utilityYellow600, t)!, utilityYellow700: Color.lerp(utilityYellow700, other.utilityYellow700, t)!, borderInputHover: Color.lerp(borderInputHover, other.borderInputHover, t)!, bgErrorOverlay: Color.lerp(bgErrorOverlay, other.bgErrorOverlay, t)!, vehicleMediaBg: Color.lerp(vehicleMediaBg, other.vehicleMediaBg, t)!, vehicleOutline: Color.lerp(vehicleOutline, other.vehicleOutline, t)!, logoBg: Color.lerp(logoBg, other.logoBg, t)!, fileTypePdf: Color.lerp(fileTypePdf, other.fileTypePdf, t)!, fileTypeDoc: Color.lerp(fileTypeDoc, other.fileTypeDoc, t)!, fileTypeXls: Color.lerp(fileTypeXls, other.fileTypeXls, t)!, fileTypeCsv: Color.lerp(fileTypeCsv, other.fileTypeCsv, t)!, fileTypeImg: Color.lerp(fileTypeImg, other.fileTypeImg, t)!, fileTypeZip: Color.lerp(fileTypeZip, other.fileTypeZip, t)!, fileTypeVid: Color.lerp(fileTypeVid, other.fileTypeVid, t)!);
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

/// Accent — màu khách theo vai (color/accent/*), đổi theo sáng/tối và theo khách.
@immutable
class InvAccentColors extends ThemeExtension<InvAccentColors> {
  const InvAccentColors({
    required this.accentBg,
    required this.accentBgSubtle,
    required this.accentBorder,
    required this.accentFg,
    required this.accentSolid,
    required this.accentSolidHover,
    required this.accentSolidPressed,
    required this.accentText,
    required this.accentTextHover,
  });

  /// Màu khách · Nền mục menu đang chọn, nền avatar (DEC-316)
  final Color accentBg;
  /// Màu khách · Nền dòng bảng đang chọn (DEC-316)
  final Color accentBgSubtle;
  /// Màu khách · Viền chỗ đang chọn: thẻ chọn, ô chọn (DEC-316)
  final Color accentBorder;
  /// Màu khách · Chữ viết tắt, icon avatar trên nền accent/bg (DEC-316)
  final Color accentFg;
  /// Màu khách · Công tắc bật, ô chọn, radio, gạch tab đang chọn, thanh tiến độ (DEC-316)
  final Color accentSolid;
  /// Màu khách · Rê chuột trên phần mang màu khách (DEC-316)
  final Color accentSolidHover;
  /// Màu khách · Đang bấm phần mang màu khách (DEC-316)
  final Color accentSolidPressed;
  /// Màu khách · Chữ liên kết, mã chứng từ (DEC-316)
  final Color accentText;
  /// Màu khách · Chữ liên kết khi rê chuột (DEC-316)
  final Color accentTextHover;

  /// Tính từ chế độ sáng/tối + dải màu khách đang dùng (DEC-316).
  factory InvAccentColors.from(bool dark, InvBrandColors b) => dark
      ? InvAccentColors(accentBg: b.brand900, accentBgSubtle: b.brand950, accentBorder: b.brand300, accentFg: b.brand200, accentSolid: b.brand300, accentSolidHover: b.brand200, accentSolidPressed: b.brand100, accentText: b.brand300, accentTextHover: b.brand200)
      : InvAccentColors(accentBg: b.brand100, accentBgSubtle: b.brand50, accentBorder: b.brand800, accentFg: b.brand800, accentSolid: b.brand800, accentSolidHover: b.brand900, accentSolidPressed: b.brand950, accentText: b.brand700, accentTextHover: b.brand800);

  @override
  InvAccentColors copyWith({Color? accentBg, Color? accentBgSubtle, Color? accentBorder, Color? accentFg, Color? accentSolid, Color? accentSolidHover, Color? accentSolidPressed, Color? accentText, Color? accentTextHover}) =>
      InvAccentColors(accentBg: accentBg ?? this.accentBg, accentBgSubtle: accentBgSubtle ?? this.accentBgSubtle, accentBorder: accentBorder ?? this.accentBorder, accentFg: accentFg ?? this.accentFg, accentSolid: accentSolid ?? this.accentSolid, accentSolidHover: accentSolidHover ?? this.accentSolidHover, accentSolidPressed: accentSolidPressed ?? this.accentSolidPressed, accentText: accentText ?? this.accentText, accentTextHover: accentTextHover ?? this.accentTextHover);

  @override
  InvAccentColors lerp(covariant ThemeExtension<InvAccentColors>? other, double t) {
    if (other is! InvAccentColors) return this;
    return InvAccentColors(accentBg: Color.lerp(accentBg, other.accentBg, t)!, accentBgSubtle: Color.lerp(accentBgSubtle, other.accentBgSubtle, t)!, accentBorder: Color.lerp(accentBorder, other.accentBorder, t)!, accentFg: Color.lerp(accentFg, other.accentFg, t)!, accentSolid: Color.lerp(accentSolid, other.accentSolid, t)!, accentSolidHover: Color.lerp(accentSolidHover, other.accentSolidHover, t)!, accentSolidPressed: Color.lerp(accentSolidPressed, other.accentSolidPressed, t)!, accentText: Color.lerp(accentText, other.accentText, t)!, accentTextHover: Color.lerp(accentTextHover, other.accentTextHover, t)!);
  }
}

/// Platform — số đo theo nền tảng. App dùng InvPlatform.mobile.
@immutable
class InvPlatform extends ThemeExtension<InvPlatform> {
  const InvPlatform({
    required this.radiusNone,
    required this.radiusXxs,
    required this.radiusXs,
    required this.radiusSm,
    required this.radiusMd,
    required this.radiusLg,
    required this.radiusXl,
    required this.radius2xl,
    required this.radius3xl,
    required this.radius4xl,
    required this.radiusFull,
    required this.radiusControl,
    required this.radiusField,
    required this.radiusCard,
    required this.radiusInner,
    required this.radiusOverlay,
    required this.radiusMenu,
    required this.radiusMenuItem,
    required this.radiusBadge,
    required this.spaceNone,
    required this.spaceXxs,
    required this.spaceXs,
    required this.spaceSm,
    required this.spaceMd,
    required this.spaceMdLg,
    required this.spaceLgXl,
    required this.spaceLg,
    required this.spaceXl,
    required this.space2xl,
    required this.space3xl,
    required this.space4xl,
    required this.space5xl,
    required this.space6xl,
    required this.space7xl,
    required this.space8xl,
    required this.space9xl,
    required this.space10xl,
    required this.space11xl,
    required this.containerPaddingMobile,
    required this.containerPaddingDesktop,
    required this.containerMaxWidthDesktop,
    required this.gridColumns,
    required this.gridGutter,
    required this.gridMargin,
    required this.layoutCardPadding,
    required this.layoutListGap,
    required this.layoutSectionGap,
    required this.layoutTitleGap,
    required this.layoutEmptyPadding,
    required this.formFieldGap,
    required this.touchMin,
    required this.controlHeightSm,
    required this.controlHeightMd,
    required this.controlHeightMl,
    required this.controlHeightLg,
    required this.controlPaddingXSm,
    required this.controlPaddingXMd,
    required this.controlPaddingXLg,
    required this.controlPaddingXIconSm,
    required this.controlPaddingXIconMd,
    required this.controlPaddingXIconLg,
    required this.controlIconGap,
    required this.controlLabelInset,
    required this.tabPaddingX,
    required this.tabPaddingXIcon,
    required this.tabGap,
    required this.navHeight,
    required this.navOffsetBottom,
    required this.navPaddingX,
    required this.navItemPaddingY,
    required this.navScanSize,
    required this.navChildIndent,
    required this.chipHeightSm,
    required this.chipHeightLg,
    required this.chipFontSizeSm,
    required this.chipLineHeightSm,
    required this.chipCountInset,
    required this.chipCountFontSize,
    required this.chipCountLineHeight,
    required this.avatarLabelWidth,
    required this.avatarLabelSubtitleSize,
    required this.avatarLabelSubtitleLineHeight,
    required this.chipPaddingXSm,
    required this.chipPaddingXMd,
    required this.chipPaddingXLg,
    required this.chipPaddingXIconLg,
    required this.avatarSizeMd,
    required this.avatarStatusSizeMd,
    required this.avatarSizeXxl,
    required this.avatarStatusSizeXl,
    required this.avatarEditSizeXl,
    required this.avatarIconSizeSm,
    required this.avatarEditIconSizeLg,
    required this.avatarSpinnerSizeXxl,
    required this.avatarGroupOverlapSm,
    required this.avatarGroupOverlapMd,
    required this.avatarGroupOverlapLg,
    required this.tooltipMaxWidth,
    required this.helpSheetTitleLineHeight,
    required this.uploadActionFontSize,
    required this.uploadDisabledOpacity,
    required this.uploadDividerWidth,
    required this.uploadAppTapMinHeight,
    required this.uploadRequiredGap,
    required this.uploadCompactTextMinWidth,
    required this.uploadMetaOffset,
    required this.listRowPaddingX,
    required this.listRowPaddingY,
    required this.listRowGap,
    required this.cardActionGap,
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
    required this.typeHintSize,
    required this.typeHintLineHeight,
    required this.typeCodeSize,
    required this.typeCodeLineHeight,
    required this.iconSizeXs,
    required this.iconSizeSm,
    required this.iconSizeMd,
    required this.iconSizeLg,
    required this.iconSizeChip,
    required this.featuredIconSize,
    required this.featuredIconSizeMd,
    required this.featuredIconSizeCompact,
    required this.featuredIconSizeXl,
    required this.fieldBorderWidth,
    required this.fieldWidthDefault,
    required this.fieldLabelMaxWidth,
    required this.progressWidthDefault,
    required this.widthParagraphMax,
    required this.sizeNone,
    required this.sizeXxs,
    required this.sizeXs,
    required this.sizeSm,
    required this.sizeMd,
    required this.sizeLg,
    required this.size14,
    required this.sizeXl,
    required this.size2xl,
    required this.size3xl,
    required this.size28,
    required this.size4xl,
    required this.size36,
    required this.size5xl,
    required this.size6xl,
    required this.size7xl,
    required this.size8xl,
    required this.size9xl,
    required this.size10xl,
    required this.size11xl,
    required this.tableRowMinHeight,
    required this.vehicleQSmH,
    required this.vehicleCardMediaAppW,
    required this.vehicleCardMediaAppH,
    required this.vehicleQLgW,
    required this.headerNavHeight,
    required this.headerNavAccountMenuWidth,
    required this.breadcrumbsCurrentMaxWidth,
    required this.breadcrumbsMenuMinWidth,
    required this.commandSearchWidth,
    required this.commandSearchHighlightPaddingX,
    required this.typeDisplay2xlSize,
    required this.typeDisplay2xlLineHeight,
    required this.typeDisplayXlSize,
    required this.typeDisplayXlLineHeight,
    required this.typeDisplayLgSize,
    required this.typeDisplayLgLineHeight,
    required this.typeDisplayMdSize,
    required this.typeDisplayMdLineHeight,
    required this.typeBodyLgSize,
    required this.typeBodyLgLineHeight,
    required this.otpCellWidth,
  });

  /// Thang bo góc Untitled `radius-none` = 0 (DEC-315)
  final double radiusNone;
  /// Thang bo góc Untitled `radius-xxs` = 2 (DEC-315)
  final double radiusXxs;
  /// Thang bo góc Untitled `radius-xs` = 4 (DEC-315)
  final double radiusXs;
  /// Thang bo góc Untitled `radius-sm` = 6 (DEC-315)
  final double radiusSm;
  /// Thang bo góc Untitled `radius-md` = 8 (DEC-315)
  final double radiusMd;
  /// Thang bo góc Untitled `radius-lg` = 10 (DEC-315)
  final double radiusLg;
  /// Thang bo góc Untitled `radius-xl` = 12 (DEC-315)
  final double radiusXl;
  /// Thang bo góc Untitled `radius-2xl` = 16 (DEC-315)
  final double radius2xl;
  /// Thang bo góc Untitled `radius-3xl` = 20 (DEC-315)
  final double radius3xl;
  /// Thang bo góc Untitled `radius-4xl` = 24 (DEC-315)
  final double radius4xl;
  /// Thang bo góc Untitled `radius-full` = tròn hẳn (DEC-315)
  final double radiusFull;
  /// Nút, tab chip, ô tìm; Web = App 8, bỏ viên thuốc (DEC-328)
  final double radiusControl;
  /// Ô nhập, ô chọn; Web = App 8 (DEC-328)
  final double radiusField;
  /// Thẻ, nhóm có viền, khối trong trang, bảng; Web = App 12, bo không quá lề thẻ (DEC-165, DEC-328)
  final double radiusCard;
  /// Khối phụ trong thẻ, ảnh nhỏ, ô icon vuông, Featured icon vuông; Web = App 8 (DEC-328)
  final double radiusInner;
  /// Hộp thoại, hộp thoại tìm, mọi sheet; Web = App 20 (DEC-328)
  final double radiusOverlay;
  /// Menu thả, popover danh sách: 10 = mục 6 + lề 4, đồng tâm (DEC-328)
  final double radiusMenu;
  /// Mục trong menu thả (DEC-259)
  final double radiusMenuItem;
  /// Badge vuông cho nhãn phân loại, không phải trạng thái (DEC-259)
  final double radiusBadge;
  /// Thang khoảng cách Untitled `spacing-none` = 0: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceNone;
  /// Thang khoảng cách Untitled `spacing-xxs` = 2: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceXxs;
  /// Thang khoảng cách Untitled `spacing-xs` = 4: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceXs;
  /// Thang khoảng cách Untitled `spacing-sm` = 6: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceSm;
  /// Thang khoảng cách Untitled `spacing-md` = 8: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceMd;
  /// Bậc Semantic 10: lề Badge MD (DEC-341), lề nút Web MD phía icon, khoảng Notification (DEC-346); thang Untitled không có bậc này
  final double spaceMdLg;
  /// Bậc Semantic 14: lề phía icon nút Web LG (DEC-346 pd01); thang Untitled không có bậc này
  final double spaceLgXl;
  /// Thang khoảng cách Untitled `spacing-lg` = 12: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceLg;
  /// Thang khoảng cách Untitled `spacing-xl` = 16: lề trong, khoảng giữa phần tử (DEC-314)
  final double spaceXl;
  /// Thang khoảng cách Untitled `spacing-2xl` = 20: lề trong, khoảng giữa phần tử (DEC-314)
  final double space2xl;
  /// Thang khoảng cách Untitled `spacing-3xl` = 24: lề trong, khoảng giữa phần tử (DEC-314)
  final double space3xl;
  /// Thang khoảng cách Untitled `spacing-4xl` = 32: lề trong, khoảng giữa phần tử (DEC-314)
  final double space4xl;
  /// Thang khoảng cách Untitled `spacing-5xl` = 40: lề trong, khoảng giữa phần tử (DEC-314)
  final double space5xl;
  /// Thang khoảng cách Untitled `spacing-6xl` = 48: lề trong, khoảng giữa phần tử (DEC-314)
  final double space6xl;
  /// Thang khoảng cách Untitled `spacing-7xl` = 64: lề trong, khoảng giữa phần tử (DEC-314)
  final double space7xl;
  /// Thang khoảng cách Untitled `spacing-8xl` = 80: lề trong, khoảng giữa phần tử (DEC-314)
  final double space8xl;
  /// Thang khoảng cách Untitled `spacing-9xl` = 96: lề trong, khoảng giữa phần tử (DEC-314)
  final double space9xl;
  /// Thang khoảng cách Untitled `spacing-10xl` = 128: lề trong, khoảng giữa phần tử (DEC-314)
  final double space10xl;
  /// Thang khoảng cách Untitled `spacing-11xl` = 160: lề trong, khoảng giữa phần tử (DEC-314)
  final double space11xl;
  /// Lề container trên điện thoại (DEC-324, tên Untitled)
  final double containerPaddingMobile;
  /// Lề container từ 768 trở lên (DEC-324, tên Untitled)
  final double containerPaddingDesktop;
  /// Rộng tối đa màn chi tiết, form web, đã gồm lề; nội dung còn 1216. Màn bảng trải hết, app không đọc token này (DEC-324)
  final double containerMaxWidthDesktop;
  /// Số cột màn (DEC-324). Tablet 6 cột ghi ở grid.tablet
  final double gridColumns;
  /// Rãnh cột cấp màn (DEC-324)
  final double gridGutter;
  /// Lề lưới và lề màn: đọc token này để đổi theo nền tảng (DEC-324)
  final double gridMargin;
  /// Lề chứa: lề trong thẻ, nhóm có viền, dòng trong nhóm (DEC-164, DEC-165)
  final double layoutCardPadding;
  /// Giữa các thẻ, dòng trong danh sách; Web = App 12 (DEC-341 sp04)
  final double layoutListGap;
  /// Giữa các khối lớn; Web = App 24 (DEC-341 sp04)
  final double layoutSectionGap;
  /// Tiêu đề màn → nội dung (DEC-192)
  final double layoutTitleGap;
  /// Lề trên dưới màn trống, màn kết quả, đăng nhập; Web = App 64 (DEC-259, DEC-341 sp04)
  final double layoutEmptyPadding;
  /// Giữa 2 ô nhập trong một nhóm; Web = App 16 (DEC-192, DEC-341 sp04)
  final double formFieldGap;
  /// Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138). Con trỏ thô trên web đọc số của app (DEC-339)
  final double touchMin;
  /// Cao control cỡ SM: nút trong hàng bảng (web), tab chip, nút nhỏ (app) (DEC-173)
  final double controlHeightSm;
  /// Cao control cỡ MD (mặc định): nút, ô nhập web; nút trong thẻ, sheet, nút icon (app). App 44 bằng touch/min, mở lại DEC-173 (DEC-341 sp10)
  final double controlHeightMd;
  /// Nút icon / avatar thanh trên (DEC-304); Featured icon không còn mượn (DEC-329 ic11) App còn 42, lệch control/height/md 44 (DEC-341 sp10 giữ, chờ quyết). App không dùng, Mobile bằng MD (user 02/11)
  final double controlHeightMl;
  /// Cao control cỡ LG: màn đăng nhập, nút cần nổi (web); nút chân màn, ô nhập (app) (DEC-173)
  final double controlHeightLg;
  /// Lề trái phải trong nút cỡ SM; Web 10 khớp nút thật (DEC-192, DEC-346 pd00)
  final double controlPaddingXSm;
  /// Lề trái phải trong nút cỡ MD (DEC-192)
  final double controlPaddingXMd;
  /// Lề trái phải trong nút cỡ LG; nút app 52 lề 24 (DEC-163, DEC-192)
  final double controlPaddingXLg;
  /// Lề phía có icon trong nút SM: Web lùi 2 như Untitled, App lùi 4 (DEC-192, DEC-346 pd01, pd02)
  final double controlPaddingXIconSm;
  /// Lề phía có icon trong nút MD: Web lùi 2 như Untitled, App lùi 4 (DEC-192, DEC-346 pd01, pd02)
  final double controlPaddingXIconMd;
  /// Lề phía có icon trong nút LG: Web lùi 2 như Untitled, App lùi 4 (DEC-163, DEC-192, DEC-346 pd01, pd02)
  final double controlPaddingXIconLg;
  /// Icon → chữ trong nút, tab chip (DEC-161, DEC-192)
  final double controlIconGap;
  /// Bọc chữ của nút: Web 2, App 4; itemSpacing 4 + bọc = icon → chữ Web 6, App 8 (DEC-346 pd01)
  final double controlLabelInset;
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
  /// Lề trái dòng con _Nav item 36 = 8 + 20 + 8, thay khung rỗng Indent (DEC-346 al00)
  final double navChildIndent;
  /// Cao chip Size SM 22 cả web lẫn app (DEC-259). Ngoại lệ: chữ 18 + 2 × 2 như Untitled Badge SM (DEC-341).
  final double chipHeightSm;
  /// Cao chip LG 28 = chữ 20 + 2 × 4 như Untitled (DEC-259, DEC-341)
  final double chipHeightLg;
  /// Chip SM: cỡ chữ 12 cả web lẫn app, bằng type/hint (DEC-239, DEC-322)
  final double chipFontSizeSm;
  /// Chip SM: cao dòng 18 cả web lẫn app, bằng type/hint (DEC-310, DEC-322)
  final double chipLineHeightSm;
  /// Badge SM có ô đếm: lề phải 3 = (22 − 16) / 2 (DEC-303, DEC-310) Ngoại lệ: (chip/height-sm 22 − ô đếm 16) / 2 (DEC-341).
  final double chipCountInset;
  /// Badge: chữ số đếm và Count Only 12 cố định web + app (review R11, DEC-304)
  final double chipCountFontSize;
  /// Badge: dòng chữ số đếm 16 cố định web + app (DEC-304)
  final double chipCountLineHeight;
  /// Avatar label: rộng mặc định 240, tên và dòng phụ cắt "…" một dòng (DEC-303) Ngoại lệ: 240, thang không có bậc (DEC-341).
  final double avatarLabelWidth;
  /// Avatar label: chữ dòng phụ 12 cố định web + app (DEC-304)
  final double avatarLabelSubtitleSize;
  /// Avatar label: dòng phụ cao 16 cố định web + app (DEC-304)
  final double avatarLabelSubtitleLineHeight;
  /// Badge SM: lề phía chữ 8 theo Untitled, mở lại DEC-310 (DEC-341 sp01)
  final double chipPaddingXSm;
  /// Badge MD: lề phía chữ 10 (DEC-341); trỏ primitive vì thang Semantic không có bậc 10
  final double chipPaddingXMd;
  /// Badge LG: lề phía chữ 12 theo Untitled, mở lại DEC-310 (DEC-341 sp01)
  final double chipPaddingXLg;
  /// Badge LG: lề phía chấm/icon 10; Badge MD: lề phía chữ 10 theo Untitled, mở lại DEC-310 (DEC-341 sp01)
  final double chipPaddingXIconLg;
  /// Cỡ avatar MD (DEC-201)
  final double avatarSizeMd;
  /// Chấm trạng thái avatar MD, chưa tính viền trắng 2 (DEC-201) Ngoại lệ: Untitled cũng dùng size-2.5 (DEC-341).
  final double avatarStatusSizeMd;
  /// Cỡ avatar XXL, đầu trang hồ sơ (DEC-203) Ngoại lệ: đầu trang hồ sơ (DEC-203), Untitled dừng ở 64 (DEC-341).
  final double avatarSizeXxl;
  /// Chấm trạng thái avatar XL (DEC-203)
  final double avatarStatusSizeXl;
  /// Nút đổi ảnh trên avatar XL (DEC-203)
  final double avatarEditSizeXl;
  /// Icon trong Avatar SM (Content=Icon, Upload): 14 (DEC-242)
  final double avatarIconSizeSm;
  /// Icon camera nút đổi ảnh LG (nút 24): 14 (DEC-242)
  final double avatarEditIconSizeLg;
  /// Vòng quay Uploading, Avatar XXL: 28 (DEC-242)
  final double avatarSpinnerSizeXxl;
  /// Avatar Group SM: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (6), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242) Ngoại lệ: −¼ đường kính, biến Figma không tính được (DEC-205) (DEC-341).
  final double avatarGroupOverlapSm;
  /// Avatar Group MD: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (8), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242) Ngoại lệ: −¼ đường kính, biến Figma không tính được (DEC-205) (DEC-341).
  final double avatarGroupOverlapMd;
  /// Avatar Group LG: khoảng giữa các avatar là số ÂM = lùi đè ¼ đường kính (12), gắn vào itemSpacing của Base / Avatar Group (DEC-205, DEC-242) Ngoại lệ: −¼ đường kính, biến Figma không tính được (DEC-205) (DEC-341).
  final double avatarGroupOverlapLg;
  /// Rộng tối đa tooltip, quá thì xuống dòng (DEC-206) Ngoại lệ: 240, thang không có bậc (DEC-341).
  final double tooltipMaxWidth;
  /// Dòng tiêu đề Help sheet, theo type/title-3 18/28 (DEC-322)
  final double helpSheetTitleLineHeight;
  /// Chữ nút Chọn tệp, link Thử lại, theo type/label 14 (DEC-322)
  final double uploadActionFontSize;
  /// Vùng kéo thả bị khoá (DEC-307)
  final double uploadDisabledOpacity;
  /// Rộng vạch chia dòng phụ file (DEC-307)
  final double uploadDividerWidth;
  /// Cao tối thiểu vùng bấm tải lên trên app (DEC-307) Ngoại lệ: vùng bấm tải lên app (DEC-307) (DEC-341).
  final double uploadAppTapMinHeight;
  /// Khoảng trước dấu * bắt buộc 2, như Untitled label.tsx (DEC-307, DEC-341 sp07)
  final double uploadRequiredGap;
  /// Rộng tối thiểu chữ vùng kéo thả gọn 160 (DEC-307, DEC-341 sp09)
  final double uploadCompactTextMinWidth;
  /// Khoảng trên dòng phụ file 2 như Untitled mt-0.5 (DEC-307, DEC-346 al08)
  final double uploadMetaOffset;
  /// Dòng menu, dòng chọn: lề ngang Web 8, App 12 (DEC-346 pd04)
  final double listRowPaddingX;
  /// Dòng menu, dòng chọn: lề dọc Web 8, App 12 (DEC-346 pd04)
  final double listRowPaddingY;
  /// Giữa các dòng tệp trong Field Upload: Web 8, App 12 (DEC-346 pd04)
  final double listRowGap;
  /// Giữa các nút trong đầu thẻ: Web 8, App 12 (DEC-162, DEC-346 pd04)
  final double cardActionGap;
  /// Độ dày vòng focus (DEC-339)
  final double focusWidth;
  /// Khoảng cách vòng focus tới mép control; vòng vào trong dùng số âm (DEC-339)
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
  /// Gợi ý dưới ô, chữ lỗi, dòng phụ file (DEC-306)
  final double typeHintSize;
  /// Gợi ý dưới ô, chữ lỗi, dòng phụ file (DEC-306)
  final double typeHintLineHeight;
  /// Mã lệnh, mã chứng từ
  final double typeCodeSize;
  /// Mã lệnh, mã chứng từ
  final double typeCodeLineHeight;
  /// Icon rất nhỏ: xoá trong tag, dấu tick, dấu ngăn, mũi tên bước số; web = app 12 (DEC-329 ic03)
  final double iconSizeXs;
  /// Icon trong nút có chữ, ô nhập, ô tìm, mũi tên tuyến, chevron; web = app 14 (DEC-329 ic02)
  final double iconSizeSm;
  /// Icon menu, hàng bảng, hàng danh sách, nút icon; web = app 16 (DEC-329 ic02)
  final double iconSizeMd;
  /// Icon thanh tab app, icon đứng riêng, nút lớn app, Featured 36 và 40; web = app 20 (DEC-329 ic02, ic04)
  final double iconSizeLg;
  /// Icon trong Badge 14, màu chip/{tone}/fg, nét 2.25 trên khung 24 (DEC-310, DEC-329 ic01)
  final double iconSizeChip;
  /// Featured icon 48, icon 24: màn trống, màn kết quả, đầu dialog, ô bấm tải lên app (icon.md mục 3.1, DEC-258, DEC-307, DEC-329 ic11)
  final double featuredIconSize;
  /// Featured icon 40, icon 20: Upload Full web (DEC-329 ic11)
  final double featuredIconSizeMd;
  /// Featured icon 36, icon 20: Upload Compact, trỏ bậc size/36 (DEC-329 ic11, DEC-341 sp08)
  final double featuredIconSizeCompact;
  /// Featured icon 56, icon 28 theo Untitled; ngoại lệ số trần vì thang không có 56 (DEC-329 ic11)
  final double featuredIconSizeXl;
  /// Ô nhập: viền nghỉ 1px (DEC-184) (DEC-207)
  final double fieldBorderWidth;
  /// Ô nhập: Web 320; app trải theo màn trừ lề, 361 chỉ là kết quả trên khung 393 (DEC-324). Figma: app dùng Fill
  final double fieldWidthDefault;
  /// Không còn gắn trên Figma: hàng nhãn rộng theo ô (DEC-346 al03). Xoá khi dọn biến. Chữ nhãn Figma tối đa 264 là số trần vì Figma không gắn biến vào max width của chữ
  final double fieldLabelMaxWidth;
  /// Thanh tiến độ: Web 320; app trải theo màn trừ lề (DEC-324). Figma: app dùng Fill
  final double progressWidthDefault;
  /// Đoạn văn tối đa với chữ 14; lớp .prose đọc biến này (DEC-324)
  final double widthParagraphMax;
  /// Thang kích thước theo bậc Untitled = 0: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeNone;
  /// Thang kích thước theo bậc Untitled = 2: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeXxs;
  /// Thang kích thước theo bậc Untitled = 4: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeXs;
  /// Thang kích thước theo bậc Untitled = 6: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeSm;
  /// Thang kích thước theo bậc Untitled = 8: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeMd;
  /// Thang kích thước theo bậc Untitled = 12: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeLg;
  /// Bậc 14 cho icon, lệch thang Untitled do user chọn, không dùng cho khoảng cách (DEC-329 ic05)
  final double size14;
  /// Thang kích thước theo bậc Untitled = 16: cao, rộng, cỡ khối của component (DEC-314)
  final double sizeXl;
  /// Thang kích thước theo bậc Untitled = 20: cao, rộng, cỡ khối của component (DEC-314)
  final double size2xl;
  /// Thang kích thước theo bậc Untitled = 24: cao, rộng, cỡ khối của component (DEC-314)
  final double size3xl;
  /// Bậc 28 cho cao, cỡ khối, lệch thang Untitled do user chọn, mở lại DEC-314 (DEC-341 sp08)
  final double size28;
  /// Thang kích thước theo bậc Untitled = 32: cao, rộng, cỡ khối của component (DEC-314)
  final double size4xl;
  /// Bậc 36 cho cao, cỡ khối, lệch thang Untitled do user chọn, mở lại DEC-314 (DEC-341 sp08)
  final double size36;
  /// Thang kích thước theo bậc Untitled = 40: cao, rộng, cỡ khối của component (DEC-314)
  final double size5xl;
  /// Thang kích thước theo bậc Untitled = 48: cao, rộng, cỡ khối của component (DEC-314)
  final double size6xl;
  /// Thang kích thước theo bậc Untitled = 64: cao, rộng, cỡ khối của component (DEC-314)
  final double size7xl;
  /// Thang kích thước theo bậc Untitled = 80: cao, rộng, cỡ khối của component (DEC-314)
  final double size8xl;
  /// Thang kích thước theo bậc Untitled = 96: cao, rộng, cỡ khối của component (DEC-314)
  final double size9xl;
  /// Thang kích thước theo bậc Untitled = 128: cao, rộng, cỡ khối của component (DEC-314)
  final double size10xl;
  /// Thang kích thước theo bậc Untitled = 160: cao, rộng, cỡ khối của component (DEC-314)
  final double size11xl;
  /// Cao tối thiểu dòng bảng (DEC-259, như Untitled) Ngoại lệ: chữ 20 + 2 × 16 (space/xl, lề ô bảng web) (DEC-341).
  final double tableRowMinHeight;
  /// Cao ảnh Vehicle Card web 160 × 100, rộng size/11xl (DEC-269, DEC-334)
  final double vehicleQSmH;
  /// Rộng ảnh Vehicle Card app 140 × 88 (DEC-269, DEC-334)
  final double vehicleCardMediaAppW;
  /// Cao ảnh Vehicle Card app 140 × 88 (DEC-269, DEC-334)
  final double vehicleCardMediaAppH;
  /// Rộng tối đa ảnh đầu trang chi tiết phương tiện, tỉ lệ 16:10; app trải theo màn (DEC-334)
  final double vehicleQLgW;
  /// Cao thanh trên Header navigation (DEC-305) Ngoại lệ: thanh trên theo DEC-305 (DEC-341).
  final double headerNavHeight;
  /// Rộng menu tài khoản mở từ avatar (DEC-305) Ngoại lệ: 256 giữ riêng (DEC-324) (DEC-341).
  final double headerNavAccountMenuWidth;
  /// Breadcrumbs: trang hiện tại rộng tối đa, quá thì cắt + tooltip (DEC-305) Ngoại lệ: 240, thang không có bậc (DEC-341).
  final double breadcrumbsCurrentMaxWidth;
  /// Breadcrumbs: rộng tối thiểu menu tầng ẩn “…” (DEC-305) Ngoại lệ: 240, thang không có bậc (DEC-341).
  final double breadcrumbsMenuMinWidth;
  /// Rộng hộp thoại tìm ⌘K giữa màn (DEC-305) Ngoại lệ: 600 giữ riêng (DEC-324) (DEC-341).
  final double commandSearchWidth;
  /// Lề trái phải nền chữ khớp (DEC-305) Ngoại lệ: nền chữ khớp, lớn hơn làm giãn chữ (DEC-341).
  final double commandSearchHighlightPaddingX;
  /// Số rất lớn, màn giới thiệu, Cal Sans (DEC-322)
  final double typeDisplay2xlSize;
  /// Số rất lớn, màn giới thiệu, Cal Sans (DEC-322)
  final double typeDisplay2xlLineHeight;
  /// Số rất lớn, màn giới thiệu (DEC-322)
  final double typeDisplayXlSize;
  /// Số rất lớn, màn giới thiệu (DEC-322)
  final double typeDisplayXlLineHeight;
  /// Số lớn, màn giới thiệu (DEC-322)
  final double typeDisplayLgSize;
  /// Số lớn, màn giới thiệu (DEC-322)
  final double typeDisplayLgLineHeight;
  /// Số lớn trên màn rộng (DEC-322)
  final double typeDisplayMdSize;
  /// Số lớn trên màn rộng (DEC-322)
  final double typeDisplayMdLineHeight;
  /// Chữ 16/24, bậc Text md của Untitled (DEC-322)
  final double typeBodyLgSize;
  /// Chữ 16/24, bậc Text md của Untitled (DEC-322)
  final double typeBodyLgLineHeight;
  /// Ô mã OTP: rộng một ô. Giữ theo chế độ vì component chỉ có một khối gốc (DEC-341 sp06)
  final double otpCellWidth;

  static const web = InvPlatform(
    radiusNone: InvPrimitives.radius0,
    radiusXxs: InvPrimitives.radius2,
    radiusXs: InvPrimitives.radius4,
    radiusSm: InvPrimitives.radius6,
    radiusMd: InvPrimitives.radius8,
    radiusLg: InvPrimitives.radius10,
    radiusXl: InvPrimitives.radius12,
    radius2xl: InvPrimitives.radius16,
    radius3xl: InvPrimitives.radius20,
    radius4xl: InvPrimitives.radius24,
    radiusFull: InvPrimitives.radius9999,
    radiusControl: InvPrimitives.radiusMd,
    radiusField: InvPrimitives.radiusMd,
    radiusCard: InvPrimitives.radiusXl,
    radiusInner: InvPrimitives.radiusMd,
    radiusOverlay: InvPrimitives.radius3xl,
    radiusMenu: InvPrimitives.radiusLg,
    radiusMenuItem: InvPrimitives.radiusSm,
    radiusBadge: InvPrimitives.radiusSm,
    spaceNone: InvPrimitives.space0,
    spaceXxs: InvPrimitives.space2,
    spaceXs: InvPrimitives.space4,
    spaceSm: InvPrimitives.space6,
    spaceMd: InvPrimitives.space8,
    spaceMdLg: InvPrimitives.space10,
    spaceLgXl: InvPrimitives.space14,
    spaceLg: InvPrimitives.space12,
    spaceXl: InvPrimitives.space16,
    space2xl: InvPrimitives.space20,
    space3xl: InvPrimitives.space24,
    space4xl: InvPrimitives.space32,
    space5xl: InvPrimitives.space40,
    space6xl: InvPrimitives.space48,
    space7xl: InvPrimitives.space64,
    space8xl: InvPrimitives.space80,
    space9xl: InvPrimitives.space96,
    space10xl: InvPrimitives.space128,
    space11xl: InvPrimitives.space160,
    containerPaddingMobile: InvPrimitives.spaceXl,
    containerPaddingDesktop: InvPrimitives.space4xl,
    containerMaxWidthDesktop: InvPrimitives.width3xl,
    gridColumns: 12.0,
    gridGutter: InvPrimitives.space4xl,
    gridMargin: InvPrimitives.containerPaddingDesktop,
    layoutCardPadding: InvPrimitives.spaceXl,
    layoutListGap: InvPrimitives.spaceLg,
    layoutSectionGap: InvPrimitives.space3xl,
    layoutTitleGap: InvPrimitives.spaceXl,
    layoutEmptyPadding: InvPrimitives.space7xl,
    formFieldGap: InvPrimitives.spaceXl,
    touchMin: 24.0,
    controlHeightSm: InvPrimitives.size28,
    controlHeightMd: 32.0,
    controlHeightMl: InvPrimitives.size36,
    controlHeightLg: 40.0,
    controlPaddingXSm: InvPrimitives.spaceMdLg,
    controlPaddingXMd: InvPrimitives.spaceLg,
    controlPaddingXLg: InvPrimitives.spaceXl,
    controlPaddingXIconSm: InvPrimitives.spaceMd,
    controlPaddingXIconMd: InvPrimitives.spaceMdLg,
    controlPaddingXIconLg: InvPrimitives.spaceLgXl,
    controlIconGap: InvPrimitives.spaceSm,
    controlLabelInset: InvPrimitives.spaceXxs,
    tabPaddingX: InvPrimitives.spaceMd,
    tabPaddingXIcon: InvPrimitives.spaceSm,
    tabGap: InvPrimitives.spaceMd,
    navHeight: 64.0,
    navOffsetBottom: InvPrimitives.spaceMd,
    navPaddingX: InvPrimitives.spaceXs,
    navItemPaddingY: InvPrimitives.spaceXs,
    navScanSize: 56.0,
    navChildIndent: InvPrimitives.space36,
    chipHeightSm: 22.0,
    chipHeightLg: InvPrimitives.size28,
    chipFontSizeSm: InvPrimitives.fontSizeXs,
    chipLineHeightSm: InvPrimitives.lineHeightXs,
    chipCountInset: 3.0,
    chipCountFontSize: InvPrimitives.fontSizeXs,
    chipCountLineHeight: InvPrimitives.lineHeightXsTight,
    avatarLabelWidth: 240.0,
    avatarLabelSubtitleSize: InvPrimitives.fontSizeXs,
    avatarLabelSubtitleLineHeight: InvPrimitives.lineHeightXsTight,
    chipPaddingXSm: InvPrimitives.spaceMd,
    chipPaddingXMd: InvPrimitives.spaceMdLg,
    chipPaddingXLg: InvPrimitives.spaceLg,
    chipPaddingXIconLg: InvPrimitives.spaceMdLg,
    avatarSizeMd: InvPrimitives.size36,
    avatarStatusSizeMd: 10.0,
    avatarSizeXxl: 88.0,
    avatarStatusSizeXl: InvPrimitives.size14,
    avatarEditSizeXl: InvPrimitives.size28,
    avatarIconSizeSm: InvPrimitives.size14,
    avatarEditIconSizeLg: InvPrimitives.size14,
    avatarSpinnerSizeXxl: InvPrimitives.size28,
    avatarGroupOverlapSm: -6.0,
    avatarGroupOverlapMd: -8.0,
    avatarGroupOverlapLg: -12.0,
    tooltipMaxWidth: 240.0,
    helpSheetTitleLineHeight: InvPrimitives.lineHeightLg,
    uploadActionFontSize: InvPrimitives.fontSizeSm,
    uploadDisabledOpacity: 0.6,
    uploadDividerWidth: 1.0,
    uploadAppTapMinHeight: 72.0,
    uploadRequiredGap: InvPrimitives.spaceXxs,
    uploadCompactTextMinWidth: InvPrimitives.size11xl,
    uploadMetaOffset: InvPrimitives.spaceXxs,
    listRowPaddingX: InvPrimitives.spaceMd,
    listRowPaddingY: InvPrimitives.spaceMd,
    listRowGap: InvPrimitives.spaceMd,
    cardActionGap: InvPrimitives.spaceMd,
    focusWidth: 2.0,
    focusOffset: 2.0,
    typeDisplaySize: InvPrimitives.fontSizeDisplaySm,
    typeDisplayLineHeight: InvPrimitives.lineHeightDisplaySm,
    typeTitle1Size: InvPrimitives.fontSizeDisplayXs,
    typeTitle1LineHeight: InvPrimitives.lineHeightDisplayXs,
    typeTitle2Size: InvPrimitives.fontSizeXl,
    typeTitle2LineHeight: InvPrimitives.lineHeightXl,
    typeTitle3Size: InvPrimitives.fontSizeLg,
    typeTitle3LineHeight: InvPrimitives.lineHeightLg,
    typeHeadingSize: InvPrimitives.fontSizeSm,
    typeHeadingLineHeight: InvPrimitives.lineHeightSm,
    typeBodySize: InvPrimitives.fontSizeSm,
    typeBodyLineHeight: InvPrimitives.lineHeightSm,
    typeLabelSize: InvPrimitives.fontSizeSm,
    typeLabelLineHeight: InvPrimitives.lineHeightSm,
    typeCaptionSize: InvPrimitives.fontSizeXs,
    typeCaptionLineHeight: InvPrimitives.lineHeightXsTight,
    typeHintSize: InvPrimitives.fontSizeXs,
    typeHintLineHeight: InvPrimitives.lineHeightXs,
    typeCodeSize: InvPrimitives.fontSizeXs,
    typeCodeLineHeight: InvPrimitives.lineHeightXsTight,
    iconSizeXs: InvPrimitives.sizeLg,
    iconSizeSm: InvPrimitives.size14,
    iconSizeMd: InvPrimitives.sizeXl,
    iconSizeLg: InvPrimitives.size2xl,
    iconSizeChip: InvPrimitives.size14,
    featuredIconSize: InvPrimitives.size6xl,
    featuredIconSizeMd: InvPrimitives.size5xl,
    featuredIconSizeCompact: InvPrimitives.size36,
    featuredIconSizeXl: 56.0,
    fieldBorderWidth: 1.0,
    fieldWidthDefault: InvPrimitives.widthXxs,
    fieldLabelMaxWidth: 320.0,
    progressWidthDefault: InvPrimitives.widthXxs,
    widthParagraphMax: InvPrimitives.widthMd,
    sizeNone: InvPrimitives.space0,
    sizeXxs: InvPrimitives.space2,
    sizeXs: InvPrimitives.space4,
    sizeSm: InvPrimitives.space6,
    sizeMd: InvPrimitives.space8,
    sizeLg: InvPrimitives.space12,
    size14: InvPrimitives.space14,
    sizeXl: InvPrimitives.space16,
    size2xl: InvPrimitives.space20,
    size3xl: InvPrimitives.space24,
    size28: InvPrimitives.space28,
    size4xl: InvPrimitives.space32,
    size36: InvPrimitives.space36,
    size5xl: InvPrimitives.space40,
    size6xl: InvPrimitives.space48,
    size7xl: InvPrimitives.space64,
    size8xl: InvPrimitives.space80,
    size9xl: InvPrimitives.space96,
    size10xl: InvPrimitives.space128,
    size11xl: InvPrimitives.space160,
    tableRowMinHeight: 52.0,
    vehicleQSmH: 100.0,
    vehicleCardMediaAppW: 140.0,
    vehicleCardMediaAppH: 88.0,
    vehicleQLgW: 480.0,
    headerNavHeight: 44.0,
    headerNavAccountMenuWidth: 256.0,
    breadcrumbsCurrentMaxWidth: 240.0,
    breadcrumbsMenuMinWidth: 240.0,
    commandSearchWidth: 600.0,
    commandSearchHighlightPaddingX: 1.0,
    typeDisplay2xlSize: InvPrimitives.fontSizeDisplay2xl,
    typeDisplay2xlLineHeight: InvPrimitives.lineHeightDisplay2xl,
    typeDisplayXlSize: InvPrimitives.fontSizeDisplayXl,
    typeDisplayXlLineHeight: InvPrimitives.lineHeightDisplayXl,
    typeDisplayLgSize: InvPrimitives.fontSizeDisplayLg,
    typeDisplayLgLineHeight: InvPrimitives.lineHeightDisplayLg,
    typeDisplayMdSize: InvPrimitives.fontSizeDisplayMd,
    typeDisplayMdLineHeight: InvPrimitives.lineHeightDisplayMd,
    typeBodyLgSize: InvPrimitives.fontSizeMd,
    typeBodyLgLineHeight: InvPrimitives.lineHeightMd,
    otpCellWidth: InvPrimitives.size5xl,
  );

  static const mobile = InvPlatform(
    radiusNone: InvPrimitives.radius0,
    radiusXxs: InvPrimitives.radius2,
    radiusXs: InvPrimitives.radius4,
    radiusSm: InvPrimitives.radius6,
    radiusMd: InvPrimitives.radius8,
    radiusLg: InvPrimitives.radius10,
    radiusXl: InvPrimitives.radius12,
    radius2xl: InvPrimitives.radius16,
    radius3xl: InvPrimitives.radius20,
    radius4xl: InvPrimitives.radius24,
    radiusFull: InvPrimitives.radius9999,
    radiusControl: InvPrimitives.radiusMd,
    radiusField: InvPrimitives.radiusMd,
    radiusCard: InvPrimitives.radiusXl,
    radiusInner: InvPrimitives.radiusMd,
    radiusOverlay: InvPrimitives.radius3xl,
    radiusMenu: InvPrimitives.radiusLg,
    radiusMenuItem: InvPrimitives.radiusSm,
    radiusBadge: InvPrimitives.radiusSm,
    spaceNone: InvPrimitives.space0,
    spaceXxs: InvPrimitives.space2,
    spaceXs: InvPrimitives.space4,
    spaceSm: InvPrimitives.space6,
    spaceMd: InvPrimitives.space8,
    spaceMdLg: InvPrimitives.space10,
    spaceLgXl: InvPrimitives.space14,
    spaceLg: InvPrimitives.space12,
    spaceXl: InvPrimitives.space16,
    space2xl: InvPrimitives.space20,
    space3xl: InvPrimitives.space24,
    space4xl: InvPrimitives.space32,
    space5xl: InvPrimitives.space40,
    space6xl: InvPrimitives.space48,
    space7xl: InvPrimitives.space64,
    space8xl: InvPrimitives.space80,
    space9xl: InvPrimitives.space96,
    space10xl: InvPrimitives.space128,
    space11xl: InvPrimitives.space160,
    containerPaddingMobile: InvPrimitives.spaceXl,
    containerPaddingDesktop: InvPrimitives.space4xl,
    containerMaxWidthDesktop: InvPrimitives.width3xl,
    gridColumns: 4.0,
    gridGutter: InvPrimitives.spaceXl,
    gridMargin: InvPrimitives.containerPaddingMobile,
    layoutCardPadding: InvPrimitives.spaceXl,
    layoutListGap: InvPrimitives.spaceLg,
    layoutSectionGap: InvPrimitives.space3xl,
    layoutTitleGap: InvPrimitives.spaceXl,
    layoutEmptyPadding: InvPrimitives.space7xl,
    formFieldGap: InvPrimitives.spaceXl,
    touchMin: 44.0,
    controlHeightSm: InvPrimitives.size36,
    controlHeightMd: 44.0,
    controlHeightMl: 44.0,
    controlHeightLg: 52.0,
    controlPaddingXSm: InvPrimitives.spaceLg,
    controlPaddingXMd: InvPrimitives.spaceXl,
    controlPaddingXLg: InvPrimitives.space3xl,
    controlPaddingXIconSm: InvPrimitives.spaceMd,
    controlPaddingXIconMd: InvPrimitives.spaceLg,
    controlPaddingXIconLg: InvPrimitives.space2xl,
    controlIconGap: InvPrimitives.spaceMd,
    controlLabelInset: InvPrimitives.spaceXs,
    tabPaddingX: InvPrimitives.spaceXl,
    tabPaddingXIcon: InvPrimitives.spaceLg,
    tabGap: InvPrimitives.spaceMd,
    navHeight: 64.0,
    navOffsetBottom: InvPrimitives.spaceMd,
    navPaddingX: InvPrimitives.spaceXs,
    navItemPaddingY: InvPrimitives.spaceXs,
    navScanSize: 56.0,
    navChildIndent: InvPrimitives.space36,
    chipHeightSm: 22.0,
    chipHeightLg: InvPrimitives.size28,
    chipFontSizeSm: InvPrimitives.fontSizeXs,
    chipLineHeightSm: InvPrimitives.lineHeightXs,
    chipCountInset: 3.0,
    chipCountFontSize: InvPrimitives.fontSizeXs,
    chipCountLineHeight: InvPrimitives.lineHeightXsTight,
    avatarLabelWidth: 240.0,
    avatarLabelSubtitleSize: InvPrimitives.fontSizeXs,
    avatarLabelSubtitleLineHeight: InvPrimitives.lineHeightXsTight,
    chipPaddingXSm: InvPrimitives.spaceMd,
    chipPaddingXMd: InvPrimitives.spaceMdLg,
    chipPaddingXLg: InvPrimitives.spaceLg,
    chipPaddingXIconLg: InvPrimitives.spaceMdLg,
    avatarSizeMd: InvPrimitives.size36,
    avatarStatusSizeMd: 10.0,
    avatarSizeXxl: 88.0,
    avatarStatusSizeXl: InvPrimitives.size14,
    avatarEditSizeXl: InvPrimitives.size28,
    avatarIconSizeSm: InvPrimitives.size14,
    avatarEditIconSizeLg: InvPrimitives.size14,
    avatarSpinnerSizeXxl: InvPrimitives.size28,
    avatarGroupOverlapSm: -6.0,
    avatarGroupOverlapMd: -8.0,
    avatarGroupOverlapLg: -12.0,
    tooltipMaxWidth: 240.0,
    helpSheetTitleLineHeight: InvPrimitives.lineHeightLg,
    uploadActionFontSize: InvPrimitives.fontSizeSm,
    uploadDisabledOpacity: 0.6,
    uploadDividerWidth: 1.0,
    uploadAppTapMinHeight: 72.0,
    uploadRequiredGap: InvPrimitives.spaceXxs,
    uploadCompactTextMinWidth: InvPrimitives.size11xl,
    uploadMetaOffset: InvPrimitives.spaceXxs,
    listRowPaddingX: InvPrimitives.spaceLg,
    listRowPaddingY: InvPrimitives.spaceLg,
    listRowGap: InvPrimitives.spaceLg,
    cardActionGap: InvPrimitives.spaceLg,
    focusWidth: 2.0,
    focusOffset: 2.0,
    typeDisplaySize: InvPrimitives.fontSizeDisplaySm,
    typeDisplayLineHeight: InvPrimitives.lineHeightDisplaySm,
    typeTitle1Size: InvPrimitives.fontSizeDisplayXs,
    typeTitle1LineHeight: InvPrimitives.lineHeightDisplayXs,
    typeTitle2Size: InvPrimitives.fontSizeXl,
    typeTitle2LineHeight: InvPrimitives.lineHeightXl,
    typeTitle3Size: InvPrimitives.fontSizeLg,
    typeTitle3LineHeight: InvPrimitives.lineHeightLg,
    typeHeadingSize: InvPrimitives.fontSizeSm,
    typeHeadingLineHeight: InvPrimitives.lineHeightSm,
    typeBodySize: InvPrimitives.fontSizeSm,
    typeBodyLineHeight: InvPrimitives.lineHeightSm,
    typeLabelSize: InvPrimitives.fontSizeSm,
    typeLabelLineHeight: InvPrimitives.lineHeightSm,
    typeCaptionSize: InvPrimitives.fontSizeXs,
    typeCaptionLineHeight: InvPrimitives.lineHeightXsTight,
    typeHintSize: InvPrimitives.fontSizeXs,
    typeHintLineHeight: InvPrimitives.lineHeightXs,
    typeCodeSize: InvPrimitives.fontSizeXs,
    typeCodeLineHeight: InvPrimitives.lineHeightXsTight,
    iconSizeXs: InvPrimitives.sizeLg,
    iconSizeSm: InvPrimitives.size14,
    iconSizeMd: InvPrimitives.sizeXl,
    iconSizeLg: InvPrimitives.size2xl,
    iconSizeChip: InvPrimitives.size14,
    featuredIconSize: InvPrimitives.size6xl,
    featuredIconSizeMd: InvPrimitives.size5xl,
    featuredIconSizeCompact: InvPrimitives.size36,
    featuredIconSizeXl: 56.0,
    fieldBorderWidth: 1.0,
    fieldWidthDefault: InvPrimitives.v100%,
    fieldLabelMaxWidth: 320.0,
    progressWidthDefault: InvPrimitives.v100%,
    widthParagraphMax: InvPrimitives.widthMd,
    sizeNone: InvPrimitives.space0,
    sizeXxs: InvPrimitives.space2,
    sizeXs: InvPrimitives.space4,
    sizeSm: InvPrimitives.space6,
    sizeMd: InvPrimitives.space8,
    sizeLg: InvPrimitives.space12,
    size14: InvPrimitives.space14,
    sizeXl: InvPrimitives.space16,
    size2xl: InvPrimitives.space20,
    size3xl: InvPrimitives.space24,
    size28: InvPrimitives.space28,
    size4xl: InvPrimitives.space32,
    size36: InvPrimitives.space36,
    size5xl: InvPrimitives.space40,
    size6xl: InvPrimitives.space48,
    size7xl: InvPrimitives.space64,
    size8xl: InvPrimitives.space80,
    size9xl: InvPrimitives.space96,
    size10xl: InvPrimitives.space128,
    size11xl: InvPrimitives.space160,
    tableRowMinHeight: 52.0,
    vehicleQSmH: 100.0,
    vehicleCardMediaAppW: 140.0,
    vehicleCardMediaAppH: 88.0,
    vehicleQLgW: 480.0,
    headerNavHeight: 56.0,
    headerNavAccountMenuWidth: 256.0,
    breadcrumbsCurrentMaxWidth: 240.0,
    breadcrumbsMenuMinWidth: 240.0,
    commandSearchWidth: 600.0,
    commandSearchHighlightPaddingX: 1.0,
    typeDisplay2xlSize: InvPrimitives.fontSizeDisplay2xl,
    typeDisplay2xlLineHeight: InvPrimitives.lineHeightDisplay2xl,
    typeDisplayXlSize: InvPrimitives.fontSizeDisplayXl,
    typeDisplayXlLineHeight: InvPrimitives.lineHeightDisplayXl,
    typeDisplayLgSize: InvPrimitives.fontSizeDisplayLg,
    typeDisplayLgLineHeight: InvPrimitives.lineHeightDisplayLg,
    typeDisplayMdSize: InvPrimitives.fontSizeDisplayMd,
    typeDisplayMdLineHeight: InvPrimitives.lineHeightDisplayMd,
    typeBodyLgSize: InvPrimitives.fontSizeMd,
    typeBodyLgLineHeight: InvPrimitives.lineHeightMd,
    otpCellWidth: InvPrimitives.size6xl,
  );

  @override
  InvPlatform copyWith({double? radiusNone, double? radiusXxs, double? radiusXs, double? radiusSm, double? radiusMd, double? radiusLg, double? radiusXl, double? radius2xl, double? radius3xl, double? radius4xl, double? radiusFull, double? radiusControl, double? radiusField, double? radiusCard, double? radiusInner, double? radiusOverlay, double? radiusMenu, double? radiusMenuItem, double? radiusBadge, double? spaceNone, double? spaceXxs, double? spaceXs, double? spaceSm, double? spaceMd, double? spaceMdLg, double? spaceLgXl, double? spaceLg, double? spaceXl, double? space2xl, double? space3xl, double? space4xl, double? space5xl, double? space6xl, double? space7xl, double? space8xl, double? space9xl, double? space10xl, double? space11xl, double? containerPaddingMobile, double? containerPaddingDesktop, double? containerMaxWidthDesktop, double? gridColumns, double? gridGutter, double? gridMargin, double? layoutCardPadding, double? layoutListGap, double? layoutSectionGap, double? layoutTitleGap, double? layoutEmptyPadding, double? formFieldGap, double? touchMin, double? controlHeightSm, double? controlHeightMd, double? controlHeightMl, double? controlHeightLg, double? controlPaddingXSm, double? controlPaddingXMd, double? controlPaddingXLg, double? controlPaddingXIconSm, double? controlPaddingXIconMd, double? controlPaddingXIconLg, double? controlIconGap, double? controlLabelInset, double? tabPaddingX, double? tabPaddingXIcon, double? tabGap, double? navHeight, double? navOffsetBottom, double? navPaddingX, double? navItemPaddingY, double? navScanSize, double? navChildIndent, double? chipHeightSm, double? chipHeightLg, double? chipFontSizeSm, double? chipLineHeightSm, double? chipCountInset, double? chipCountFontSize, double? chipCountLineHeight, double? avatarLabelWidth, double? avatarLabelSubtitleSize, double? avatarLabelSubtitleLineHeight, double? chipPaddingXSm, double? chipPaddingXMd, double? chipPaddingXLg, double? chipPaddingXIconLg, double? avatarSizeMd, double? avatarStatusSizeMd, double? avatarSizeXxl, double? avatarStatusSizeXl, double? avatarEditSizeXl, double? avatarIconSizeSm, double? avatarEditIconSizeLg, double? avatarSpinnerSizeXxl, double? avatarGroupOverlapSm, double? avatarGroupOverlapMd, double? avatarGroupOverlapLg, double? tooltipMaxWidth, double? helpSheetTitleLineHeight, double? uploadActionFontSize, double? uploadDisabledOpacity, double? uploadDividerWidth, double? uploadAppTapMinHeight, double? uploadRequiredGap, double? uploadCompactTextMinWidth, double? uploadMetaOffset, double? listRowPaddingX, double? listRowPaddingY, double? listRowGap, double? cardActionGap, double? focusWidth, double? focusOffset, double? typeDisplaySize, double? typeDisplayLineHeight, double? typeTitle1Size, double? typeTitle1LineHeight, double? typeTitle2Size, double? typeTitle2LineHeight, double? typeTitle3Size, double? typeTitle3LineHeight, double? typeHeadingSize, double? typeHeadingLineHeight, double? typeBodySize, double? typeBodyLineHeight, double? typeLabelSize, double? typeLabelLineHeight, double? typeCaptionSize, double? typeCaptionLineHeight, double? typeHintSize, double? typeHintLineHeight, double? typeCodeSize, double? typeCodeLineHeight, double? iconSizeXs, double? iconSizeSm, double? iconSizeMd, double? iconSizeLg, double? iconSizeChip, double? featuredIconSize, double? featuredIconSizeMd, double? featuredIconSizeCompact, double? featuredIconSizeXl, double? fieldBorderWidth, double? fieldWidthDefault, double? fieldLabelMaxWidth, double? progressWidthDefault, double? widthParagraphMax, double? sizeNone, double? sizeXxs, double? sizeXs, double? sizeSm, double? sizeMd, double? sizeLg, double? size14, double? sizeXl, double? size2xl, double? size3xl, double? size28, double? size4xl, double? size36, double? size5xl, double? size6xl, double? size7xl, double? size8xl, double? size9xl, double? size10xl, double? size11xl, double? tableRowMinHeight, double? vehicleQSmH, double? vehicleCardMediaAppW, double? vehicleCardMediaAppH, double? vehicleQLgW, double? headerNavHeight, double? headerNavAccountMenuWidth, double? breadcrumbsCurrentMaxWidth, double? breadcrumbsMenuMinWidth, double? commandSearchWidth, double? commandSearchHighlightPaddingX, double? typeDisplay2xlSize, double? typeDisplay2xlLineHeight, double? typeDisplayXlSize, double? typeDisplayXlLineHeight, double? typeDisplayLgSize, double? typeDisplayLgLineHeight, double? typeDisplayMdSize, double? typeDisplayMdLineHeight, double? typeBodyLgSize, double? typeBodyLgLineHeight, double? otpCellWidth}) =>
      InvPlatform(radiusNone: radiusNone ?? this.radiusNone, radiusXxs: radiusXxs ?? this.radiusXxs, radiusXs: radiusXs ?? this.radiusXs, radiusSm: radiusSm ?? this.radiusSm, radiusMd: radiusMd ?? this.radiusMd, radiusLg: radiusLg ?? this.radiusLg, radiusXl: radiusXl ?? this.radiusXl, radius2xl: radius2xl ?? this.radius2xl, radius3xl: radius3xl ?? this.radius3xl, radius4xl: radius4xl ?? this.radius4xl, radiusFull: radiusFull ?? this.radiusFull, radiusControl: radiusControl ?? this.radiusControl, radiusField: radiusField ?? this.radiusField, radiusCard: radiusCard ?? this.radiusCard, radiusInner: radiusInner ?? this.radiusInner, radiusOverlay: radiusOverlay ?? this.radiusOverlay, radiusMenu: radiusMenu ?? this.radiusMenu, radiusMenuItem: radiusMenuItem ?? this.radiusMenuItem, radiusBadge: radiusBadge ?? this.radiusBadge, spaceNone: spaceNone ?? this.spaceNone, spaceXxs: spaceXxs ?? this.spaceXxs, spaceXs: spaceXs ?? this.spaceXs, spaceSm: spaceSm ?? this.spaceSm, spaceMd: spaceMd ?? this.spaceMd, spaceMdLg: spaceMdLg ?? this.spaceMdLg, spaceLgXl: spaceLgXl ?? this.spaceLgXl, spaceLg: spaceLg ?? this.spaceLg, spaceXl: spaceXl ?? this.spaceXl, space2xl: space2xl ?? this.space2xl, space3xl: space3xl ?? this.space3xl, space4xl: space4xl ?? this.space4xl, space5xl: space5xl ?? this.space5xl, space6xl: space6xl ?? this.space6xl, space7xl: space7xl ?? this.space7xl, space8xl: space8xl ?? this.space8xl, space9xl: space9xl ?? this.space9xl, space10xl: space10xl ?? this.space10xl, space11xl: space11xl ?? this.space11xl, containerPaddingMobile: containerPaddingMobile ?? this.containerPaddingMobile, containerPaddingDesktop: containerPaddingDesktop ?? this.containerPaddingDesktop, containerMaxWidthDesktop: containerMaxWidthDesktop ?? this.containerMaxWidthDesktop, gridColumns: gridColumns ?? this.gridColumns, gridGutter: gridGutter ?? this.gridGutter, gridMargin: gridMargin ?? this.gridMargin, layoutCardPadding: layoutCardPadding ?? this.layoutCardPadding, layoutListGap: layoutListGap ?? this.layoutListGap, layoutSectionGap: layoutSectionGap ?? this.layoutSectionGap, layoutTitleGap: layoutTitleGap ?? this.layoutTitleGap, layoutEmptyPadding: layoutEmptyPadding ?? this.layoutEmptyPadding, formFieldGap: formFieldGap ?? this.formFieldGap, touchMin: touchMin ?? this.touchMin, controlHeightSm: controlHeightSm ?? this.controlHeightSm, controlHeightMd: controlHeightMd ?? this.controlHeightMd, controlHeightMl: controlHeightMl ?? this.controlHeightMl, controlHeightLg: controlHeightLg ?? this.controlHeightLg, controlPaddingXSm: controlPaddingXSm ?? this.controlPaddingXSm, controlPaddingXMd: controlPaddingXMd ?? this.controlPaddingXMd, controlPaddingXLg: controlPaddingXLg ?? this.controlPaddingXLg, controlPaddingXIconSm: controlPaddingXIconSm ?? this.controlPaddingXIconSm, controlPaddingXIconMd: controlPaddingXIconMd ?? this.controlPaddingXIconMd, controlPaddingXIconLg: controlPaddingXIconLg ?? this.controlPaddingXIconLg, controlIconGap: controlIconGap ?? this.controlIconGap, controlLabelInset: controlLabelInset ?? this.controlLabelInset, tabPaddingX: tabPaddingX ?? this.tabPaddingX, tabPaddingXIcon: tabPaddingXIcon ?? this.tabPaddingXIcon, tabGap: tabGap ?? this.tabGap, navHeight: navHeight ?? this.navHeight, navOffsetBottom: navOffsetBottom ?? this.navOffsetBottom, navPaddingX: navPaddingX ?? this.navPaddingX, navItemPaddingY: navItemPaddingY ?? this.navItemPaddingY, navScanSize: navScanSize ?? this.navScanSize, navChildIndent: navChildIndent ?? this.navChildIndent, chipHeightSm: chipHeightSm ?? this.chipHeightSm, chipHeightLg: chipHeightLg ?? this.chipHeightLg, chipFontSizeSm: chipFontSizeSm ?? this.chipFontSizeSm, chipLineHeightSm: chipLineHeightSm ?? this.chipLineHeightSm, chipCountInset: chipCountInset ?? this.chipCountInset, chipCountFontSize: chipCountFontSize ?? this.chipCountFontSize, chipCountLineHeight: chipCountLineHeight ?? this.chipCountLineHeight, avatarLabelWidth: avatarLabelWidth ?? this.avatarLabelWidth, avatarLabelSubtitleSize: avatarLabelSubtitleSize ?? this.avatarLabelSubtitleSize, avatarLabelSubtitleLineHeight: avatarLabelSubtitleLineHeight ?? this.avatarLabelSubtitleLineHeight, chipPaddingXSm: chipPaddingXSm ?? this.chipPaddingXSm, chipPaddingXMd: chipPaddingXMd ?? this.chipPaddingXMd, chipPaddingXLg: chipPaddingXLg ?? this.chipPaddingXLg, chipPaddingXIconLg: chipPaddingXIconLg ?? this.chipPaddingXIconLg, avatarSizeMd: avatarSizeMd ?? this.avatarSizeMd, avatarStatusSizeMd: avatarStatusSizeMd ?? this.avatarStatusSizeMd, avatarSizeXxl: avatarSizeXxl ?? this.avatarSizeXxl, avatarStatusSizeXl: avatarStatusSizeXl ?? this.avatarStatusSizeXl, avatarEditSizeXl: avatarEditSizeXl ?? this.avatarEditSizeXl, avatarIconSizeSm: avatarIconSizeSm ?? this.avatarIconSizeSm, avatarEditIconSizeLg: avatarEditIconSizeLg ?? this.avatarEditIconSizeLg, avatarSpinnerSizeXxl: avatarSpinnerSizeXxl ?? this.avatarSpinnerSizeXxl, avatarGroupOverlapSm: avatarGroupOverlapSm ?? this.avatarGroupOverlapSm, avatarGroupOverlapMd: avatarGroupOverlapMd ?? this.avatarGroupOverlapMd, avatarGroupOverlapLg: avatarGroupOverlapLg ?? this.avatarGroupOverlapLg, tooltipMaxWidth: tooltipMaxWidth ?? this.tooltipMaxWidth, helpSheetTitleLineHeight: helpSheetTitleLineHeight ?? this.helpSheetTitleLineHeight, uploadActionFontSize: uploadActionFontSize ?? this.uploadActionFontSize, uploadDisabledOpacity: uploadDisabledOpacity ?? this.uploadDisabledOpacity, uploadDividerWidth: uploadDividerWidth ?? this.uploadDividerWidth, uploadAppTapMinHeight: uploadAppTapMinHeight ?? this.uploadAppTapMinHeight, uploadRequiredGap: uploadRequiredGap ?? this.uploadRequiredGap, uploadCompactTextMinWidth: uploadCompactTextMinWidth ?? this.uploadCompactTextMinWidth, uploadMetaOffset: uploadMetaOffset ?? this.uploadMetaOffset, listRowPaddingX: listRowPaddingX ?? this.listRowPaddingX, listRowPaddingY: listRowPaddingY ?? this.listRowPaddingY, listRowGap: listRowGap ?? this.listRowGap, cardActionGap: cardActionGap ?? this.cardActionGap, focusWidth: focusWidth ?? this.focusWidth, focusOffset: focusOffset ?? this.focusOffset, typeDisplaySize: typeDisplaySize ?? this.typeDisplaySize, typeDisplayLineHeight: typeDisplayLineHeight ?? this.typeDisplayLineHeight, typeTitle1Size: typeTitle1Size ?? this.typeTitle1Size, typeTitle1LineHeight: typeTitle1LineHeight ?? this.typeTitle1LineHeight, typeTitle2Size: typeTitle2Size ?? this.typeTitle2Size, typeTitle2LineHeight: typeTitle2LineHeight ?? this.typeTitle2LineHeight, typeTitle3Size: typeTitle3Size ?? this.typeTitle3Size, typeTitle3LineHeight: typeTitle3LineHeight ?? this.typeTitle3LineHeight, typeHeadingSize: typeHeadingSize ?? this.typeHeadingSize, typeHeadingLineHeight: typeHeadingLineHeight ?? this.typeHeadingLineHeight, typeBodySize: typeBodySize ?? this.typeBodySize, typeBodyLineHeight: typeBodyLineHeight ?? this.typeBodyLineHeight, typeLabelSize: typeLabelSize ?? this.typeLabelSize, typeLabelLineHeight: typeLabelLineHeight ?? this.typeLabelLineHeight, typeCaptionSize: typeCaptionSize ?? this.typeCaptionSize, typeCaptionLineHeight: typeCaptionLineHeight ?? this.typeCaptionLineHeight, typeHintSize: typeHintSize ?? this.typeHintSize, typeHintLineHeight: typeHintLineHeight ?? this.typeHintLineHeight, typeCodeSize: typeCodeSize ?? this.typeCodeSize, typeCodeLineHeight: typeCodeLineHeight ?? this.typeCodeLineHeight, iconSizeXs: iconSizeXs ?? this.iconSizeXs, iconSizeSm: iconSizeSm ?? this.iconSizeSm, iconSizeMd: iconSizeMd ?? this.iconSizeMd, iconSizeLg: iconSizeLg ?? this.iconSizeLg, iconSizeChip: iconSizeChip ?? this.iconSizeChip, featuredIconSize: featuredIconSize ?? this.featuredIconSize, featuredIconSizeMd: featuredIconSizeMd ?? this.featuredIconSizeMd, featuredIconSizeCompact: featuredIconSizeCompact ?? this.featuredIconSizeCompact, featuredIconSizeXl: featuredIconSizeXl ?? this.featuredIconSizeXl, fieldBorderWidth: fieldBorderWidth ?? this.fieldBorderWidth, fieldWidthDefault: fieldWidthDefault ?? this.fieldWidthDefault, fieldLabelMaxWidth: fieldLabelMaxWidth ?? this.fieldLabelMaxWidth, progressWidthDefault: progressWidthDefault ?? this.progressWidthDefault, widthParagraphMax: widthParagraphMax ?? this.widthParagraphMax, sizeNone: sizeNone ?? this.sizeNone, sizeXxs: sizeXxs ?? this.sizeXxs, sizeXs: sizeXs ?? this.sizeXs, sizeSm: sizeSm ?? this.sizeSm, sizeMd: sizeMd ?? this.sizeMd, sizeLg: sizeLg ?? this.sizeLg, size14: size14 ?? this.size14, sizeXl: sizeXl ?? this.sizeXl, size2xl: size2xl ?? this.size2xl, size3xl: size3xl ?? this.size3xl, size28: size28 ?? this.size28, size4xl: size4xl ?? this.size4xl, size36: size36 ?? this.size36, size5xl: size5xl ?? this.size5xl, size6xl: size6xl ?? this.size6xl, size7xl: size7xl ?? this.size7xl, size8xl: size8xl ?? this.size8xl, size9xl: size9xl ?? this.size9xl, size10xl: size10xl ?? this.size10xl, size11xl: size11xl ?? this.size11xl, tableRowMinHeight: tableRowMinHeight ?? this.tableRowMinHeight, vehicleQSmH: vehicleQSmH ?? this.vehicleQSmH, vehicleCardMediaAppW: vehicleCardMediaAppW ?? this.vehicleCardMediaAppW, vehicleCardMediaAppH: vehicleCardMediaAppH ?? this.vehicleCardMediaAppH, vehicleQLgW: vehicleQLgW ?? this.vehicleQLgW, headerNavHeight: headerNavHeight ?? this.headerNavHeight, headerNavAccountMenuWidth: headerNavAccountMenuWidth ?? this.headerNavAccountMenuWidth, breadcrumbsCurrentMaxWidth: breadcrumbsCurrentMaxWidth ?? this.breadcrumbsCurrentMaxWidth, breadcrumbsMenuMinWidth: breadcrumbsMenuMinWidth ?? this.breadcrumbsMenuMinWidth, commandSearchWidth: commandSearchWidth ?? this.commandSearchWidth, commandSearchHighlightPaddingX: commandSearchHighlightPaddingX ?? this.commandSearchHighlightPaddingX, typeDisplay2xlSize: typeDisplay2xlSize ?? this.typeDisplay2xlSize, typeDisplay2xlLineHeight: typeDisplay2xlLineHeight ?? this.typeDisplay2xlLineHeight, typeDisplayXlSize: typeDisplayXlSize ?? this.typeDisplayXlSize, typeDisplayXlLineHeight: typeDisplayXlLineHeight ?? this.typeDisplayXlLineHeight, typeDisplayLgSize: typeDisplayLgSize ?? this.typeDisplayLgSize, typeDisplayLgLineHeight: typeDisplayLgLineHeight ?? this.typeDisplayLgLineHeight, typeDisplayMdSize: typeDisplayMdSize ?? this.typeDisplayMdSize, typeDisplayMdLineHeight: typeDisplayMdLineHeight ?? this.typeDisplayMdLineHeight, typeBodyLgSize: typeBodyLgSize ?? this.typeBodyLgSize, typeBodyLgLineHeight: typeBodyLgLineHeight ?? this.typeBodyLgLineHeight, otpCellWidth: otpCellWidth ?? this.otpCellWidth);

  @override
  InvPlatform lerp(covariant ThemeExtension<InvPlatform>? other, double t) {
    if (other is! InvPlatform) return this;
    return InvPlatform(radiusNone: lerpDouble(radiusNone, other.radiusNone, t), radiusXxs: lerpDouble(radiusXxs, other.radiusXxs, t), radiusXs: lerpDouble(radiusXs, other.radiusXs, t), radiusSm: lerpDouble(radiusSm, other.radiusSm, t), radiusMd: lerpDouble(radiusMd, other.radiusMd, t), radiusLg: lerpDouble(radiusLg, other.radiusLg, t), radiusXl: lerpDouble(radiusXl, other.radiusXl, t), radius2xl: lerpDouble(radius2xl, other.radius2xl, t), radius3xl: lerpDouble(radius3xl, other.radius3xl, t), radius4xl: lerpDouble(radius4xl, other.radius4xl, t), radiusFull: lerpDouble(radiusFull, other.radiusFull, t), radiusControl: lerpDouble(radiusControl, other.radiusControl, t), radiusField: lerpDouble(radiusField, other.radiusField, t), radiusCard: lerpDouble(radiusCard, other.radiusCard, t), radiusInner: lerpDouble(radiusInner, other.radiusInner, t), radiusOverlay: lerpDouble(radiusOverlay, other.radiusOverlay, t), radiusMenu: lerpDouble(radiusMenu, other.radiusMenu, t), radiusMenuItem: lerpDouble(radiusMenuItem, other.radiusMenuItem, t), radiusBadge: lerpDouble(radiusBadge, other.radiusBadge, t), spaceNone: lerpDouble(spaceNone, other.spaceNone, t), spaceXxs: lerpDouble(spaceXxs, other.spaceXxs, t), spaceXs: lerpDouble(spaceXs, other.spaceXs, t), spaceSm: lerpDouble(spaceSm, other.spaceSm, t), spaceMd: lerpDouble(spaceMd, other.spaceMd, t), spaceMdLg: lerpDouble(spaceMdLg, other.spaceMdLg, t), spaceLgXl: lerpDouble(spaceLgXl, other.spaceLgXl, t), spaceLg: lerpDouble(spaceLg, other.spaceLg, t), spaceXl: lerpDouble(spaceXl, other.spaceXl, t), space2xl: lerpDouble(space2xl, other.space2xl, t), space3xl: lerpDouble(space3xl, other.space3xl, t), space4xl: lerpDouble(space4xl, other.space4xl, t), space5xl: lerpDouble(space5xl, other.space5xl, t), space6xl: lerpDouble(space6xl, other.space6xl, t), space7xl: lerpDouble(space7xl, other.space7xl, t), space8xl: lerpDouble(space8xl, other.space8xl, t), space9xl: lerpDouble(space9xl, other.space9xl, t), space10xl: lerpDouble(space10xl, other.space10xl, t), space11xl: lerpDouble(space11xl, other.space11xl, t), containerPaddingMobile: lerpDouble(containerPaddingMobile, other.containerPaddingMobile, t), containerPaddingDesktop: lerpDouble(containerPaddingDesktop, other.containerPaddingDesktop, t), containerMaxWidthDesktop: lerpDouble(containerMaxWidthDesktop, other.containerMaxWidthDesktop, t), gridColumns: lerpDouble(gridColumns, other.gridColumns, t), gridGutter: lerpDouble(gridGutter, other.gridGutter, t), gridMargin: lerpDouble(gridMargin, other.gridMargin, t), layoutCardPadding: lerpDouble(layoutCardPadding, other.layoutCardPadding, t), layoutListGap: lerpDouble(layoutListGap, other.layoutListGap, t), layoutSectionGap: lerpDouble(layoutSectionGap, other.layoutSectionGap, t), layoutTitleGap: lerpDouble(layoutTitleGap, other.layoutTitleGap, t), layoutEmptyPadding: lerpDouble(layoutEmptyPadding, other.layoutEmptyPadding, t), formFieldGap: lerpDouble(formFieldGap, other.formFieldGap, t), touchMin: lerpDouble(touchMin, other.touchMin, t), controlHeightSm: lerpDouble(controlHeightSm, other.controlHeightSm, t), controlHeightMd: lerpDouble(controlHeightMd, other.controlHeightMd, t), controlHeightMl: lerpDouble(controlHeightMl, other.controlHeightMl, t), controlHeightLg: lerpDouble(controlHeightLg, other.controlHeightLg, t), controlPaddingXSm: lerpDouble(controlPaddingXSm, other.controlPaddingXSm, t), controlPaddingXMd: lerpDouble(controlPaddingXMd, other.controlPaddingXMd, t), controlPaddingXLg: lerpDouble(controlPaddingXLg, other.controlPaddingXLg, t), controlPaddingXIconSm: lerpDouble(controlPaddingXIconSm, other.controlPaddingXIconSm, t), controlPaddingXIconMd: lerpDouble(controlPaddingXIconMd, other.controlPaddingXIconMd, t), controlPaddingXIconLg: lerpDouble(controlPaddingXIconLg, other.controlPaddingXIconLg, t), controlIconGap: lerpDouble(controlIconGap, other.controlIconGap, t), controlLabelInset: lerpDouble(controlLabelInset, other.controlLabelInset, t), tabPaddingX: lerpDouble(tabPaddingX, other.tabPaddingX, t), tabPaddingXIcon: lerpDouble(tabPaddingXIcon, other.tabPaddingXIcon, t), tabGap: lerpDouble(tabGap, other.tabGap, t), navHeight: lerpDouble(navHeight, other.navHeight, t), navOffsetBottom: lerpDouble(navOffsetBottom, other.navOffsetBottom, t), navPaddingX: lerpDouble(navPaddingX, other.navPaddingX, t), navItemPaddingY: lerpDouble(navItemPaddingY, other.navItemPaddingY, t), navScanSize: lerpDouble(navScanSize, other.navScanSize, t), navChildIndent: lerpDouble(navChildIndent, other.navChildIndent, t), chipHeightSm: lerpDouble(chipHeightSm, other.chipHeightSm, t), chipHeightLg: lerpDouble(chipHeightLg, other.chipHeightLg, t), chipFontSizeSm: lerpDouble(chipFontSizeSm, other.chipFontSizeSm, t), chipLineHeightSm: lerpDouble(chipLineHeightSm, other.chipLineHeightSm, t), chipCountInset: lerpDouble(chipCountInset, other.chipCountInset, t), chipCountFontSize: lerpDouble(chipCountFontSize, other.chipCountFontSize, t), chipCountLineHeight: lerpDouble(chipCountLineHeight, other.chipCountLineHeight, t), avatarLabelWidth: lerpDouble(avatarLabelWidth, other.avatarLabelWidth, t), avatarLabelSubtitleSize: lerpDouble(avatarLabelSubtitleSize, other.avatarLabelSubtitleSize, t), avatarLabelSubtitleLineHeight: lerpDouble(avatarLabelSubtitleLineHeight, other.avatarLabelSubtitleLineHeight, t), chipPaddingXSm: lerpDouble(chipPaddingXSm, other.chipPaddingXSm, t), chipPaddingXMd: lerpDouble(chipPaddingXMd, other.chipPaddingXMd, t), chipPaddingXLg: lerpDouble(chipPaddingXLg, other.chipPaddingXLg, t), chipPaddingXIconLg: lerpDouble(chipPaddingXIconLg, other.chipPaddingXIconLg, t), avatarSizeMd: lerpDouble(avatarSizeMd, other.avatarSizeMd, t), avatarStatusSizeMd: lerpDouble(avatarStatusSizeMd, other.avatarStatusSizeMd, t), avatarSizeXxl: lerpDouble(avatarSizeXxl, other.avatarSizeXxl, t), avatarStatusSizeXl: lerpDouble(avatarStatusSizeXl, other.avatarStatusSizeXl, t), avatarEditSizeXl: lerpDouble(avatarEditSizeXl, other.avatarEditSizeXl, t), avatarIconSizeSm: lerpDouble(avatarIconSizeSm, other.avatarIconSizeSm, t), avatarEditIconSizeLg: lerpDouble(avatarEditIconSizeLg, other.avatarEditIconSizeLg, t), avatarSpinnerSizeXxl: lerpDouble(avatarSpinnerSizeXxl, other.avatarSpinnerSizeXxl, t), avatarGroupOverlapSm: lerpDouble(avatarGroupOverlapSm, other.avatarGroupOverlapSm, t), avatarGroupOverlapMd: lerpDouble(avatarGroupOverlapMd, other.avatarGroupOverlapMd, t), avatarGroupOverlapLg: lerpDouble(avatarGroupOverlapLg, other.avatarGroupOverlapLg, t), tooltipMaxWidth: lerpDouble(tooltipMaxWidth, other.tooltipMaxWidth, t), helpSheetTitleLineHeight: lerpDouble(helpSheetTitleLineHeight, other.helpSheetTitleLineHeight, t), uploadActionFontSize: lerpDouble(uploadActionFontSize, other.uploadActionFontSize, t), uploadDisabledOpacity: lerpDouble(uploadDisabledOpacity, other.uploadDisabledOpacity, t), uploadDividerWidth: lerpDouble(uploadDividerWidth, other.uploadDividerWidth, t), uploadAppTapMinHeight: lerpDouble(uploadAppTapMinHeight, other.uploadAppTapMinHeight, t), uploadRequiredGap: lerpDouble(uploadRequiredGap, other.uploadRequiredGap, t), uploadCompactTextMinWidth: lerpDouble(uploadCompactTextMinWidth, other.uploadCompactTextMinWidth, t), uploadMetaOffset: lerpDouble(uploadMetaOffset, other.uploadMetaOffset, t), listRowPaddingX: lerpDouble(listRowPaddingX, other.listRowPaddingX, t), listRowPaddingY: lerpDouble(listRowPaddingY, other.listRowPaddingY, t), listRowGap: lerpDouble(listRowGap, other.listRowGap, t), cardActionGap: lerpDouble(cardActionGap, other.cardActionGap, t), focusWidth: lerpDouble(focusWidth, other.focusWidth, t), focusOffset: lerpDouble(focusOffset, other.focusOffset, t), typeDisplaySize: lerpDouble(typeDisplaySize, other.typeDisplaySize, t), typeDisplayLineHeight: lerpDouble(typeDisplayLineHeight, other.typeDisplayLineHeight, t), typeTitle1Size: lerpDouble(typeTitle1Size, other.typeTitle1Size, t), typeTitle1LineHeight: lerpDouble(typeTitle1LineHeight, other.typeTitle1LineHeight, t), typeTitle2Size: lerpDouble(typeTitle2Size, other.typeTitle2Size, t), typeTitle2LineHeight: lerpDouble(typeTitle2LineHeight, other.typeTitle2LineHeight, t), typeTitle3Size: lerpDouble(typeTitle3Size, other.typeTitle3Size, t), typeTitle3LineHeight: lerpDouble(typeTitle3LineHeight, other.typeTitle3LineHeight, t), typeHeadingSize: lerpDouble(typeHeadingSize, other.typeHeadingSize, t), typeHeadingLineHeight: lerpDouble(typeHeadingLineHeight, other.typeHeadingLineHeight, t), typeBodySize: lerpDouble(typeBodySize, other.typeBodySize, t), typeBodyLineHeight: lerpDouble(typeBodyLineHeight, other.typeBodyLineHeight, t), typeLabelSize: lerpDouble(typeLabelSize, other.typeLabelSize, t), typeLabelLineHeight: lerpDouble(typeLabelLineHeight, other.typeLabelLineHeight, t), typeCaptionSize: lerpDouble(typeCaptionSize, other.typeCaptionSize, t), typeCaptionLineHeight: lerpDouble(typeCaptionLineHeight, other.typeCaptionLineHeight, t), typeHintSize: lerpDouble(typeHintSize, other.typeHintSize, t), typeHintLineHeight: lerpDouble(typeHintLineHeight, other.typeHintLineHeight, t), typeCodeSize: lerpDouble(typeCodeSize, other.typeCodeSize, t), typeCodeLineHeight: lerpDouble(typeCodeLineHeight, other.typeCodeLineHeight, t), iconSizeXs: lerpDouble(iconSizeXs, other.iconSizeXs, t), iconSizeSm: lerpDouble(iconSizeSm, other.iconSizeSm, t), iconSizeMd: lerpDouble(iconSizeMd, other.iconSizeMd, t), iconSizeLg: lerpDouble(iconSizeLg, other.iconSizeLg, t), iconSizeChip: lerpDouble(iconSizeChip, other.iconSizeChip, t), featuredIconSize: lerpDouble(featuredIconSize, other.featuredIconSize, t), featuredIconSizeMd: lerpDouble(featuredIconSizeMd, other.featuredIconSizeMd, t), featuredIconSizeCompact: lerpDouble(featuredIconSizeCompact, other.featuredIconSizeCompact, t), featuredIconSizeXl: lerpDouble(featuredIconSizeXl, other.featuredIconSizeXl, t), fieldBorderWidth: lerpDouble(fieldBorderWidth, other.fieldBorderWidth, t), fieldWidthDefault: lerpDouble(fieldWidthDefault, other.fieldWidthDefault, t), fieldLabelMaxWidth: lerpDouble(fieldLabelMaxWidth, other.fieldLabelMaxWidth, t), progressWidthDefault: lerpDouble(progressWidthDefault, other.progressWidthDefault, t), widthParagraphMax: lerpDouble(widthParagraphMax, other.widthParagraphMax, t), sizeNone: lerpDouble(sizeNone, other.sizeNone, t), sizeXxs: lerpDouble(sizeXxs, other.sizeXxs, t), sizeXs: lerpDouble(sizeXs, other.sizeXs, t), sizeSm: lerpDouble(sizeSm, other.sizeSm, t), sizeMd: lerpDouble(sizeMd, other.sizeMd, t), sizeLg: lerpDouble(sizeLg, other.sizeLg, t), size14: lerpDouble(size14, other.size14, t), sizeXl: lerpDouble(sizeXl, other.sizeXl, t), size2xl: lerpDouble(size2xl, other.size2xl, t), size3xl: lerpDouble(size3xl, other.size3xl, t), size28: lerpDouble(size28, other.size28, t), size4xl: lerpDouble(size4xl, other.size4xl, t), size36: lerpDouble(size36, other.size36, t), size5xl: lerpDouble(size5xl, other.size5xl, t), size6xl: lerpDouble(size6xl, other.size6xl, t), size7xl: lerpDouble(size7xl, other.size7xl, t), size8xl: lerpDouble(size8xl, other.size8xl, t), size9xl: lerpDouble(size9xl, other.size9xl, t), size10xl: lerpDouble(size10xl, other.size10xl, t), size11xl: lerpDouble(size11xl, other.size11xl, t), tableRowMinHeight: lerpDouble(tableRowMinHeight, other.tableRowMinHeight, t), vehicleQSmH: lerpDouble(vehicleQSmH, other.vehicleQSmH, t), vehicleCardMediaAppW: lerpDouble(vehicleCardMediaAppW, other.vehicleCardMediaAppW, t), vehicleCardMediaAppH: lerpDouble(vehicleCardMediaAppH, other.vehicleCardMediaAppH, t), vehicleQLgW: lerpDouble(vehicleQLgW, other.vehicleQLgW, t), headerNavHeight: lerpDouble(headerNavHeight, other.headerNavHeight, t), headerNavAccountMenuWidth: lerpDouble(headerNavAccountMenuWidth, other.headerNavAccountMenuWidth, t), breadcrumbsCurrentMaxWidth: lerpDouble(breadcrumbsCurrentMaxWidth, other.breadcrumbsCurrentMaxWidth, t), breadcrumbsMenuMinWidth: lerpDouble(breadcrumbsMenuMinWidth, other.breadcrumbsMenuMinWidth, t), commandSearchWidth: lerpDouble(commandSearchWidth, other.commandSearchWidth, t), commandSearchHighlightPaddingX: lerpDouble(commandSearchHighlightPaddingX, other.commandSearchHighlightPaddingX, t), typeDisplay2xlSize: lerpDouble(typeDisplay2xlSize, other.typeDisplay2xlSize, t), typeDisplay2xlLineHeight: lerpDouble(typeDisplay2xlLineHeight, other.typeDisplay2xlLineHeight, t), typeDisplayXlSize: lerpDouble(typeDisplayXlSize, other.typeDisplayXlSize, t), typeDisplayXlLineHeight: lerpDouble(typeDisplayXlLineHeight, other.typeDisplayXlLineHeight, t), typeDisplayLgSize: lerpDouble(typeDisplayLgSize, other.typeDisplayLgSize, t), typeDisplayLgLineHeight: lerpDouble(typeDisplayLgLineHeight, other.typeDisplayLgLineHeight, t), typeDisplayMdSize: lerpDouble(typeDisplayMdSize, other.typeDisplayMdSize, t), typeDisplayMdLineHeight: lerpDouble(typeDisplayMdLineHeight, other.typeDisplayMdLineHeight, t), typeBodyLgSize: lerpDouble(typeBodyLgSize, other.typeBodyLgSize, t), typeBodyLgLineHeight: lerpDouble(typeBodyLgLineHeight, other.typeBodyLgLineHeight, t), otpCellWidth: lerpDouble(otpCellWidth, other.otpCellWidth, t));
  }
}

/// Kiểu chữ — dựng từ [InvPlatform] để cỡ chữ đúng nền tảng.
abstract final class InvTypography {
  /// Số rất lớn, màn giới thiệu, Cal Sans (DEC-322)
  static TextStyle display2xl(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplay2xlSize, height: p.typeDisplay2xlLineHeight / p.typeDisplay2xlSize, letterSpacing: p.typeDisplay2xlSize * -0.02);
  /// Số rất lớn, màn giới thiệu (DEC-322)
  static TextStyle displayXl(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplayXlSize, height: p.typeDisplayXlLineHeight / p.typeDisplayXlSize, letterSpacing: p.typeDisplayXlSize * -0.02);
  /// Số lớn, màn giới thiệu (DEC-322)
  static TextStyle displayLg(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplayLgSize, height: p.typeDisplayLgLineHeight / p.typeDisplayLgSize, letterSpacing: p.typeDisplayLgSize * -0.02);
  /// Số lớn trên màn rộng (DEC-322)
  static TextStyle displayMd(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplayMdSize, height: p.typeDisplayMdLineHeight / p.typeDisplayMdSize, letterSpacing: p.typeDisplayMdSize * -0.02);
  /// Số lớn, màn giới thiệu
  static TextStyle display(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeDisplaySize, height: p.typeDisplayLineHeight / p.typeDisplaySize);
  /// Tiêu đề màn
  static TextStyle title1(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle1Size, height: p.typeTitle1LineHeight / p.typeTitle1Size);
  /// Tiêu đề dialog, sheet, khối lớn
  static TextStyle title2(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle2Size, height: p.typeTitle2LineHeight / p.typeTitle2Size);
  /// Tiêu đề khối, thẻ
  static TextStyle title3(InvPlatform p) => TextStyle(fontFamily: 'CalSans', fontWeight: FontWeight.w400, fontSize: p.typeTitle3Size, height: p.typeTitle3LineHeight / p.typeTitle3Size);
  /// Tiêu đề khối nhỏ, biển số, tiêu đề thông báo (DEC-322)
  static TextStyle heading(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeHeadingSize, height: p.typeHeadingLineHeight / p.typeHeadingSize);
  /// Chữ đọc, giá trị
  static TextStyle body(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeBodySize, height: p.typeBodyLineHeight / p.typeBodySize);
  /// Nút, nhãn, tab: một nét 500 (DEC-322)
  static TextStyle label(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w500, fontSize: p.typeLabelSize, height: p.typeLabelLineHeight / p.typeLabelSize);
  /// Thông tin phụ, thời gian
  static TextStyle caption(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize);
  /// Gợi ý dưới ô, chữ lỗi, dòng phụ file: 12/18 (DEC-306, DEC-322)
  static TextStyle hint(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeHintSize, height: p.typeHintLineHeight / p.typeHintSize);
  /// Mã lệnh, mã chứng từ
  static TextStyle code(InvPlatform p) => TextStyle(fontFamily: 'JetBrainsMono', fontWeight: FontWeight.w400, fontSize: p.typeCodeSize, height: p.typeCodeLineHeight / p.typeCodeSize);
  /// Tên cột bảng, nhãn nhóm menu, tiêu đề nhóm nhỏ: chữ xám in hoa, không giãn (DEC-027, DEC-322) · viết hoa: dùng .toUpperCase() ở chữ
  static TextStyle captionCaps(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w500, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize);
  /// Chữ chip trạng thái Soft (DEC-200)
  static TextStyle captionStrong(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeCaptionSize, height: p.typeCaptionLineHeight / p.typeCaptionSize);
  /// Chữ chip, badge, tag cỡ SM (DEC-261)
  static TextStyle chipSm(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeHintSize, height: p.typeHintLineHeight / p.typeHintSize);
  /// Chữ chip đã chọn cỡ SM (Tag Checked) (DEC-261)
  static TextStyle chipSmStrong(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeHintSize, height: p.typeHintLineHeight / p.typeHintSize);
  /// Chữ 16/24 (DEC-322)
  static TextStyle bodyLg(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w400, fontSize: p.typeBodyLgSize, height: p.typeBodyLgLineHeight / p.typeBodyLgSize);
  /// Chữ 16/24 nét 500 (DEC-322)
  static TextStyle bodyLgMedium(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w500, fontSize: p.typeBodyLgSize, height: p.typeBodyLgLineHeight / p.typeBodyLgSize);
  /// Chữ 16/24 nét 600 (DEC-322)
  static TextStyle bodyLgStrong(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w600, fontSize: p.typeBodyLgSize, height: p.typeBodyLgLineHeight / p.typeBodyLgSize);
  /// Trích dẫn trong .prose, không nghiêng (DEC-322)
  static TextStyle proseQuote(InvPlatform p) => TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.w500, fontSize: p.typeTitle2Size, height: p.typeTitle2LineHeight / p.typeTitle2Size);
  /// Mã trong dòng của .prose (DEC-322)
  static TextStyle proseCode(InvPlatform p) => TextStyle(fontFamily: 'JetBrainsMono', fontWeight: FontWeight.w700, fontSize: p.typeBodySize, height: p.typeBodyLineHeight / p.typeBodySize);
}

/// Đổ bóng (effect style Figma).
abstract final class InvShadow {
  /// Thẻ (vai thẻ, DEC-327)
  static const List<BoxShadow> shadowXs = [BoxShadow(color: Color(0x0D000000), offset: Offset(0.0, 1.0), blurRadius: 2.0, spreadRadius: 0.0)];
  /// Thang Untitled, chưa gán vai
  static const List<BoxShadow> shadowSm = [BoxShadow(color: Color(0x1A000000), offset: Offset(0.0, 1.0), blurRadius: 3.0, spreadRadius: 0.0), BoxShadow(color: Color(0x1A000000), offset: Offset(0.0, 1.0), blurRadius: 2.0, spreadRadius: -1.0)];
  /// Thang Untitled, chưa gán vai
  static const List<BoxShadow> shadowMd = [BoxShadow(color: Color(0x1A000000), offset: Offset(0.0, 4.0), blurRadius: 6.0, spreadRadius: -1.0), BoxShadow(color: Color(0x0F000000), offset: Offset(0.0, 2.0), blurRadius: 4.0, spreadRadius: -2.0)];
  /// Menu thả, popover, gợi ý ô tìm (vai menu, DEC-327)
  static const List<BoxShadow> shadowLg = [BoxShadow(color: Color(0x14000000), offset: Offset(0.0, 12.0), blurRadius: 16.0, spreadRadius: -4.0), BoxShadow(color: Color(0x08000000), offset: Offset(0.0, 4.0), blurRadius: 6.0, spreadRadius: -2.0), BoxShadow(color: Color(0x0A000000), offset: Offset(0.0, 2.0), blurRadius: 2.0, spreadRadius: -1.0)];
  /// Dialog, sheet, toast (vai lớp phủ, DEC-327)
  static const List<BoxShadow> shadowXl = [BoxShadow(color: Color(0x14000000), offset: Offset(0.0, 20.0), blurRadius: 24.0, spreadRadius: -4.0), BoxShadow(color: Color(0x08000000), offset: Offset(0.0, 8.0), blurRadius: 8.0, spreadRadius: -4.0), BoxShadow(color: Color(0x0A000000), offset: Offset(0.0, 3.0), blurRadius: 3.0, spreadRadius: -1.5)];
  /// Thang Untitled, chưa gán vai
  static const List<BoxShadow> shadow2xl = [BoxShadow(color: Color(0x2E000000), offset: Offset(0.0, 24.0), blurRadius: 48.0, spreadRadius: -12.0), BoxShadow(color: Color(0x0A000000), offset: Offset(0.0, 4.0), blurRadius: 4.0, spreadRadius: -2.0)];
  /// Thang Untitled, chưa gán vai
  static const List<BoxShadow> shadow3xl = [BoxShadow(color: Color(0x24000000), offset: Offset(0.0, 32.0), blurRadius: 64.0, spreadRadius: -12.0), BoxShadow(color: Color(0x0A000000), offset: Offset(0.0, 5.0), blurRadius: 5.0, spreadRadius: -2.5)];
}

/// Làm mờ nền (DEC-258): dùng với BackdropFilter(filter: ImageFilter.blur(sigmaX: v, sigmaY: v)).
abstract final class InvBlur {
  /// Đầu màn, thanh công cụ dính trên cùng khi cuộn (nền color/bg/primary_blur).
  static const double backdropBlurSm = 8.0;
  /// Thanh điều hướng nổi app (DEC-160), thanh hành động nổi đáy màn (nền color/bg/primary_blur).
  static const double backdropBlurMd = 16.0;
  /// Nền sau dialog, sheet: color/bg/overlay 35% + blur; máy yếu lùi color/bg/overlay_solid.
  static const double backdropBlurLg = 24.0;
  /// Giữ cho đủ thang, chưa dùng trong app nghiệp vụ.
  static const double backdropBlurXl = 40.0;
}

abstract final class InvMotion {
  static const Duration durationFast = Duration(milliseconds: 125);
  static const Duration durationMedium = Duration(milliseconds: 300);
  static const Duration durationSlow = Duration(milliseconds: 500);
  static const Duration durationExit = Duration(milliseconds: 200);
  static const Curve easingStandard = Cubic(0.24, 1, 0.4, 1);
  static const Curve easingExit = Cubic(0.4, 0, 1, 1);
}

class InvMotionPreset {
  final Duration duration;
  final Curve curve;
  final Duration? exitDuration;
  final Curve? exitCurve;
  const InvMotionPreset({required this.duration, required this.curve, this.exitDuration, this.exitCurve});
  /// Số đổi, nội dung sau skeleton (an07, an11)
  static const InvMotionPreset fadeIn = InvMotionPreset(duration: InvMotion.durationFast, curve: InvMotion.easingStandard);
  /// Đĩa dấu kết quả (an02)
  static const InvMotionPreset pop = InvMotionPreset(duration: InvMotion.durationMedium, curve: InvMotion.easingStandard);
  /// Vẽ nét dấu kết quả; đường path có pathLength=1, dấu tích đi từ nét ngắn sang nét dài (an02)
  static const InvMotionPreset draw = InvMotionPreset(duration: InvMotion.durationMedium, curve: InvMotion.easingStandard);
  /// Đổi icon tại chỗ, giữ 1000 rồi về (an05)
  static const InvMotionPreset swap = InvMotionPreset(duration: InvMotion.durationFast, curve: InvMotion.easingStandard);
  /// Dòng vừa đổi, chạy một lần: giữ 1000, phai 500 (an06, an08)
  static const InvMotionPreset flash = InvMotionPreset(duration: Duration(milliseconds: 1500), curve: Curves.linear);
  /// Mở, đóng khối, dòng mới, dải mất mạng (an08, an10, an16). Bật bằng data-open="true"
  static const InvMotionPreset expand = InvMotionPreset(duration: InvMotion.durationMedium, curve: InvMotion.easingStandard, exitDuration: InvMotion.durationExit, exitCurve: InvMotion.easingExit);
  /// Xe trên bản đồ khi có điểm GPS mới (an12)
  static const InvMotionPreset glide = InvMotionPreset(duration: InvMotion.durationMedium, curve: InvMotion.easingStandard);
  /// Cột biểu đồ mọc khi tải, đổi lọc thì đổi ngay (an17)
  static const InvMotionPreset grow = InvMotionPreset(duration: InvMotion.durationMedium, curve: InvMotion.easingStandard);
}

/// Gắn DS v2 vào ThemeData. Đổi khách: truyền brand khác.
ThemeData invTheme({Brightness brightness = Brightness.light, InvBrandColors brand = InvBrandColors.thanChi}) {
  final s = brightness == Brightness.dark ? InvColors.dark : InvColors.light;
  final a = InvAccentColors.from(brightness == Brightness.dark, brand);
  return ThemeData(
    brightness: brightness,
    fontFamily: 'Inter',
    scaffoldBackgroundColor: s.bgSurface,
    extensions: [s, brand, a, InvPlatform.mobile],
  );
}

extension InvThemeX on BuildContext {
  InvColors get invColors => Theme.of(this).extension<InvColors>()!;
  InvBrandColors get invBrand => Theme.of(this).extension<InvBrandColors>()!;
  InvPlatform get invPlatform => Theme.of(this).extension<InvPlatform>()!;
}
