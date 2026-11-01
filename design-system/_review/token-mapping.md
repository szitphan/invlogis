---
type: design-review
status: draft
updated: 2026-10-26
links:
  - design-system/foundations/README.md
  - design-system/tokens.json
---

# Ánh xạ token nghĩa sang Apple HIG · Material 3 · Atlassian

> Chỉ để review (DEC-258), không đưa vào mô tả token hay biến Figma. Sinh từ `tokens.json` (khoá `hig`, `m3`, `atlassian`).

| Token | Apple HIG | Material 3 | Atlassian |
|---|---|---|---|
| `color/bg/surface` | systemGroupedBackground | surface-container-low | `elevation.surface.sunken` |
| `color/bg/surface` | secondarySystemGroupedBackground | surface-container-lowest | `elevation.surface` |
| `color/bg/muted` | tertiarySystemFill | surface-container-highest | `color.background.input` |
| `color/bg/hover` | — (iOS không có hover) | lớp trạng thái on-surface 8% | `color.background.neutral.subtle.hovered` |
| `color/bg/selected` | systemFill | secondary-container | `color.background.selected` |
| `color/bg/inverse` | — | inverse-surface | `color.background.inverse.subtle` |
| `color/text/primary` | label | on-surface | `color.text` |
| `color/text/secondary` | secondaryLabel | on-surface-variant | `color.text.subtle` |
| `color/text/tertiary` | tertiaryLabel · placeholderText | on-surface 38% (tắt) | `color.text.subtlest` |
| `color/text/inverse` | — | inverse-on-surface · on-primary | `color.text.inverse` |
| `color/icon/primary` | label | on-surface | `color.icon` |
| `color/icon/secondary` | secondaryLabel | on-surface-variant | `color.icon.subtle` |
| `color/border/default` | separator | outline-variant | `color.border` |
| `color/border/strong` | opaqueSeparator | outline | `color.border.bold` |
| `color/border/input` | separator (đậm) | outline | `color.border.input` |
| `color/border/focus` | tint (vòng focus bàn phím) | secondary (vòng focus) | `color.border.focused` |
| `color/border/danger` | systemRed | error | `color.border.danger` |
| `color/action/primary` | tintColor · accentColor | primary | `color.background.brand.bold` |
| `color/action/primary-hover` | — | primary + lớp on-primary 8% | `color.background.brand.bold.hovered` |
| `color/action/primary-pressed` | — (hệ thống tự làm tối) | primary + lớp on-primary 10% | `color.background.brand.bold.pressed` |
| `color/action/secondary` | secondarySystemFill | secondary-container | `color.background.neutral` |
| `color/action/secondary-hover` | — | secondary-container + lớp 8% | `color.background.neutral.hovered` |
| `color/action/danger` | systemRed | error | `color.text.danger` |
| `color/action/danger-subtle` | systemRed (nhạt) | error-container | `color.background.danger` |
| `color/chip/gray/bg` | systemGray | — (dùng tertiary hoặc tự thêm) | `color.background.accent.gray.subtler` |
| `color/chip/gray/fg` | systemGray | — | `color.text.accent.gray` |
| `color/chip/blue/bg` | systemBlue | — (dùng tertiary hoặc tự thêm) | `color.background.accent.blue.subtler` |
| `color/chip/blue/fg` | systemBlue | — | `color.text.accent.blue` |
| `color/chip/teal/bg` | systemTeal | — (dùng tertiary hoặc tự thêm) | `color.background.accent.teal.subtler` |
| `color/chip/teal/fg` | systemTeal | — | `color.text.accent.teal` |
| `color/chip/purple/bg` | systemPurple | — (dùng tertiary hoặc tự thêm) | `color.background.accent.purple.subtler` |
| `color/chip/purple/fg` | systemPurple | — | `color.text.accent.purple` |
| `color/chip/yellow/bg` | systemYellow | — (dùng tertiary hoặc tự thêm) | `color.background.accent.yellow.subtler` |
| `color/chip/yellow/fg` | systemYellow | — | `color.text.accent.yellow` |
| `color/chip/green/bg` | systemGreen | — (dùng tertiary hoặc tự thêm) | `color.background.accent.green.subtler` |
| `color/chip/green/fg` | systemGreen | — | `color.text.accent.green` |
| `color/chip/red/bg` | systemRed | — (dùng tertiary hoặc tự thêm) | `color.background.accent.red.subtler` |
| `color/chip/red/fg` | systemRed | — | `color.text.accent.red` |
| `color/chip/orange/bg` | systemOrange | — (dùng tertiary hoặc tự thêm) | `color.background.accent.orange.subtler` |
| `color/chip/orange/fg` | systemOrange | — | `color.text.accent.orange` |
| `color/overlay/scrim` | — (hệ thống tự làm mờ) | scrim | `color.blanket` |

Token chưa có ánh xạ (mới ở DEC-258): `color/status/*` 8 vai, `color/shadow/*`, `color/focus/gap`.
