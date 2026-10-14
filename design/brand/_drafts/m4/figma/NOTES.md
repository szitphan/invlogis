# Figma brand file notes (task 4.1)

- File: [innvie] Invlogis Brand, team innvie (Full seat, student plan)
- URL: https://www.figma.com/design/KPpfeOJ4m0JI33rBnhon3o
- Built 2026-10-14 from the approved kit v1.0 (read only, no repo file changed).

## Pages
1. Cover: 1920x1080, bg-n6-muc-cobalt, instance of Logo/By innvie reverse, title, slogan, v1.0 14/10/2026.
2. Logo: 14 vector components (Logo/*, Symbol/*, Icon/Favicon SVG) imported from SVG, 7 raster icon components (app icon, apple touch, android fg/bg, favicon 16/32/48), gallery, clear space diagram (1 x = 0.52 height), minimum sizes (20px, 6mm, symbol 48px, by innvie 48px, tagline 64px), icon section.
3. Color: variable collection "Brand", modes Light + Dark, 43 variables (15 palette, 13 role, 6 radius, 9 space). Swatches bound to variables, role panels use explicit mode. WCAG ratios computed from the variables (all pass).
4. Type: 15 text styles (Display/*, Body/*, Mono/*, Deck/*) with specimens.
5. Gradients: campaign gradient bar with the 0-56 / 56-70 / 70-100 text rule, 9 backgrounds (1920x1080 JPG as image fills) with contrast numbers from _contrast.json.
6. Applications: 8 Milestone 3 preview images (splash, deck cover, web hero, social post, one-pager, business card, login, landing top) with repo paths.

## Substitutions and gaps
- Fonts: Lexend, Be Vietnam Pro, JetBrains Mono all available in Figma, no substitution.
- Text styles use web px scale (clamp max values) plus deck px; doc (pt) scale is only noted as text, not styles.
- Display styles use Lexend Light (300) as in the guideline specimen; logo wordmark itself is vector (Lexend 340).
- Gradient bar on the Gradients page is drawn horizontally (Figma gradientTransform) with stops from tokens, not at true 115deg; grain not reproduced. The 9 JPG backgrounds are exact.
- Gradient/shadow/glass/border-alpha tokens: border colors are variables (with alpha); shadows and glass not created as effect styles.
- Application images are raster previews, not editable layouts. Cover wordmark lockup is "by innvie" reverse.
- Tagline/by-innvie components are cropped to SVG bounds, so card sizes in the gallery differ.
- Type page: meta column fix applied after the last screenshot (not re-screenshotted).
- Components are not published as a library.

## Figma calls
whoami 1, create_new_file 1, use_figma 13 (1 failed on a bad selector), upload_assets 5 (+ curl POSTs), get_screenshot 6.

## Verification (read-only use_figma, after R5 query)
- Pages: 0:1 Cover (1 child) · 1:2 Logo (1) · 1:3 Color (1) · 1:4 Type (1) · 1:5 Gradients (1) · 1:6 Applications (1). Each page holds one top-level page frame. None missing or empty.
- Collection "Brand": modes Light, Dark; 43 variables.
- Samples (Light / Dark): role/primary #2F43DB / #97A6FF; palette/ink #0E1442 both; palette/cobalt #2F43DB both; palette/peri #97A6FF both; palette/paper #FAF8F4 both.
- Text styles: 15.
- Type page frame 3:214 re-screenshotted after the meta-column fix.
- Note: get_metadata without a page-frame node id lists only pages; use node ids 2:23 (Logo), 3:2 (Color), 3:214 (Type), 3:388 (Gradients), 4:2 (Applications), 4:90 (Cover frame).
