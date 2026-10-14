# R5 Figma review: [innvie] Invlogis Brand

File: https://www.figma.com/design/KPpfeOJ4m0JI33rBnhon3o (fileKey KPpfeOJ4m0JI33rBnhon3o). Read only, file not modified.
Reviewed against: `design/brand/invlogis/brand-tokens.json`, `design/brand/invlogis/logo/logo-spec.md`, `design/brand/guideline/brand-guideline.html`.
Scope actually verified: the Cover and Logo pages only (screenshots). The other four pages could not be read (see check 1).

## Checklist

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Six pages exist (Cover, Logo, Color, Type, Gradients, Applications) | FAIL | `get_metadata` (file level) listed only `0:1 Cover` and `1:2 Logo`. Color, Type, Gradients and Applications are not in the response, so they cannot be confirmed. NOTES.md says all six were built, so either the listing is incomplete or the pages are missing. Re-check the file tree in Figma. |
| 2 | Logo variants are vector components, named sensibly | PASS (partial) | Logo page shows 14 named files (`invlogis-primary.svg`, `-reverse`, `-mono-black`, `-mono-white`, `-by-innvie`, `-tagline`, `-stacked`, `-symbol*`, `innvie-logo`, `favicon.svg`). NOTES.md says they are SVG imports. Vector node type not checked (metadata did not return children). |
| 3 | Clear space 1 x = 0.52 height and minimum sizes annotated, match logo-spec | PASS | Clear-space diagram labelled "1 x = 0,52 × chiều cao logo". Min sizes shown: wordmark 20 px / 6 mm, symbol 48 px / 8 mm, lockup by innvie 48 px / 12 mm, tagline lockup 64 px / 16 mm. All match logo-spec §2. |
| 4 | Variable collection "Brand" with Light + Dark modes; 5 values spot-checked | UNVERIFIED | `get_variable_defs` on node 1:2 failed: "You currently have nothing selected". The one call was used, so no values were read. Spot-check values to test later (from brand-tokens.json): `palette.cobalt #2F43DB`, `role.light.bg #FAF8F4`, `role.light.text #0E1442`, `role.dark.bg #0B1033`, `role.dark.primary #97A6FF`. |
| 5 | Swatches bound to variables | UNVERIFIED | Not checked. Needs a selection in Figma, then `get_variable_defs`. |
| 6 | Text styles use Lexend / Be Vietnam Pro / JetBrains Mono; Vietnamese diacritics render | PASS (diacritics only) | Cover and Logo screenshots render "Khai mở cách vận hành mới.", "Quy chuẩn logo", "hướng A · Lụa", "Mốc 2 đã duyệt" with correct diacritics, no tofu. Text style names and font families were not inspected; Type page not readable. |
| 7 | Gradient text-placement rule (0–56% white, 56–70% none, 70–100% ink) | UNVERIFIED | Gradients page not readable. |
| 8 | 9 backgrounds present; r1–r3 marked launch-only | UNVERIFIED | Gradients page not readable. |
| 9 | Applications page shows M3 previews with repo paths | UNVERIFIED | Applications page not readable. |
| 10 | No "Delta", no clipping or overlap in screenshots | PASS (Cover + Logo only) | No "Delta" text on either page. No clipped or overlapping text seen. Gallery captions are small (about 6 px at 1084 px width) but legible. |

Tally: PASS 4 (2, 3, 6, 10, all partial), FAIL 1 (1), UNVERIFIED 5 (4, 5, 7, 8, 9).

## Must fix

1. **Pages 3–6 missing from the file listing (check 1).** Re-check in Figma that Color, Type, Gradients and Applications exist as top-level pages. If they exist, the builder must confirm the file is saved and the page tree is complete.
2. **Variables not verified (checks 4–5).** Re-run the review with a node selected (e.g. a swatch on the Color page), then read `Brand` variables and their Light/Dark modes against brand-tokens.json.
3. **Gradients, Type, Applications not verified (checks 6–9).** Re-run the screenshot calls once those pages are reachable.

## Nice to have

- Enlarge the clear-space "x" markers on the Logo page. They are very small.
- Captions on the gallery are small (about 6 px). Consider a larger caption size for the rendered file.

## Calls used

- Figma `get_metadata`: 1 (file level, returned 2 pages)
- Figma `get_screenshot`: 2 (Cover 0:1, Logo 1:2; 4 pages not screenshotted because they were not listed)
- Figma `get_variable_defs`: 1 (failed, nothing selected)
- Total Figma calls: 4. Nothing written to the Figma file.
