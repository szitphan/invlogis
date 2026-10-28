#!/usr/bin/env python3
"""Task C: merge full S1 data (colors/alpha/utility/spacing/widths/containers/radius/effects/typography)
into tokens.untitled.json. Adds S1-only collections (flagged s1_only) + enriches existing brand/transparent."""
import json

prim = json.load(open('_task/s1-primitives.json', encoding='utf-8'))
d = json.load(open('tokens.untitled.json', encoding='utf-8'))

# idempotent: remove previously-added S1-only collections before re-adding
d['collections'] = [c for c in d['collections'] if not c.get('s1_only')]

def mk(name, type_, values, usage='', src=None, **extra):
    v = {'name': name, 'type': type_, 'values': values, 'usage': usage, 'src': src or ['S1']}
    v.update(extra)
    return v

def collection(name, vars_list, note=''):
    c = {'name': name, 'modes': ['Light'], 's1_only': True, 'variables': vars_list}
    if note:
        c['src_note'] = note
    return c

HUES_17 = ['Red','Orange','Amber','Yellow','Lime','Green','Emerald','Teal','Cyan','Sky','Blue',
           'Indigo','Violet','Purple','Fuchsia','Pink','Rose']
HUES_9_GRAY = ['Slate','Gray','Zinc','Neutral','Stone','Taupe','Mauve','Mist','Olive']

# ---------- 1. Primitives / Colors (S1) : 26 dai (17 sac + 9 xam) x 11 + White/Black ----------
prim_vars = []
for hue in HUES_17 + HUES_9_GRAY:
    desc = ('Can be swapped with the default brand color' if hue in HUES_17
            else 'Can be swapped with the default gray color')
    if hue == 'Neutral':
        desc = 'Default gray — xám trung tính, nền tảng của hệ màu'
    for step in ['50','100','200','300','400','500','600','700','800','900','950']:
        v = prim[hue][step]
        extra = {'wcag': v['wcag']}
        if v.get('default'):
            extra['default'] = True
        prim_vars.append(mk(f'--color-{hue.lower()}-{step}', 'color',
                            {'Light': v['hex']}, desc, **extra))
# Base White / Black (Transparent da co trong Base+Component)
prim_vars.append(mk('--color-white', 'color', {'Light': '#FFFFFF'},
                    'Base white', wcag='AAA 21.00'))
prim_vars.append(mk('--color-black', 'color', {'Light': '#000000'},
                    'Base black', wcag='AAA 21.00'))

# enrich existing brand + transparent
for col in d['collections']:
    if col['name'] == '0. Primitives / Brand':
        for v in col['variables']:
            step = v['name'].replace('--color-brand-', '')
            sv = prim['Brand'][step]
            if 'S1' not in v['src']:
                v['src'] = v['src'] + ['S1']
            v['s1'] = {'Light': sv['hex']}
            v['wcag'] = sv['wcag']
            if sv.get('default'):
                v['default'] = True
    if col['name'] == '0. Primitives / Base + Component':
        for v in col['variables']:
            if v['name'] == '--color-transparent' and 'S1' not in v['src']:
                v['src'] = v['src'] + ['S1']

# ---------- 2. Alpha (S1) — 20 ----------
alpha_vars = []
for n in range(10, 101, 10):
    alpha_vars.append(mk(f'--color-alpha-white-{n}', 'color',
                         {'Light': f'white {n}%', 'Dark': f'neutral-950 {n}%'},
                         'Alpha trắng theo bậc 10% (đảo ngược ở dark)'))
for n in range(10, 101, 10):
    alpha_vars.append(mk(f'--color-alpha-black-{n}', 'color',
                         {'Light': f'black {n}%', 'Dark': f'white {n}%'},
                         'Alpha đen theo bậc 10% (đảo ngược ở dark)'))

# ---------- 3. Utility (S1) — 118 ----------
# flip maps
NEUTRAL_DARK = {'50':'900','100':'800','200':'700','300':'700','400':'600','500':'500',
                '600':'400','700':'300','800':'200','900':'100'}
BRAND_DARK = {'50':'950','100':'900','200':'800','300':'700','400':'600','500':'500',
              '600':'400','700':'300','800':'200','900':'100'}
FLIP8_DARK = {'50':'950','100':'900','200':'800','300':'700','400':'600','500':'500',
              '600':'400','700':'300'}
STEPS10 = ['50','100','200','300','400','500','600','700','800','900']
STEPS8 = ['50','100','200','300','400','500','600','700']

util_vars = []
# neutral
for s in STEPS10:
    util_vars.append(mk(f'--color-utility-neutral-{s}', 'color',
                        {'Light': f'neutral.{s}', 'Dark': f'neutral.{NEUTRAL_DARK[s]}'},
                        'Utility neutral (mode-flipped)'))
# brand
for s in STEPS10:
    util_vars.append(mk(f'--color-utility-brand-{s}', 'color',
                        {'Light': f'brand.{s}', 'Dark': f'brand.{BRAND_DARK[s]}'},
                        'Utility brand (mode-flipped)'))
# brand _alt
for s in STEPS10:
    util_vars.append(mk(f'--color-utility-brand-{s}_alt', 'color',
                        {'Light': f'brand.{s}', 'Dark': f'neutral.{NEUTRAL_DARK[s]}'},
                        'Utility brand alt — nền xám thay vì tím ở dark'))
# error/warning/success (S1 = error/warning/success; S2 = red/yellow/green)
for token, hue in [('error','red'), ('warning','yellow'), ('success','green')]:
    for s in STEPS8:
        util_vars.append(mk(f'--color-utility-{token}-{s}', 'color',
                            {'Light': f'{hue}.{s}', 'Dark': f'{hue}.{FLIP8_DARK[s]}'},
                            f'Utility {token} (= {hue}, mode-flipped)'))
# orange/sky/blue/indigo/purple/fuchsia/pink/slate
for hue in ['orange','sky','blue','indigo','purple','fuchsia','pink','slate']:
    for s in STEPS8:
        util_vars.append(mk(f'--color-utility-{hue}-{s}', 'color',
                            {'Light': f'{hue}.{s}', 'Dark': f'{hue}.{FLIP8_DARK[s]}'},
                            f'Utility {hue} (mode-flipped)'))

# ---------- 4. Spacing primitives (S1) — 32 ----------
SPACING_PRIM = [
 ('0','0rem'),('0.5','0.125rem'),('1','0.25rem'),('1.5','0.375rem'),('2','0.5rem'),
 ('3','0.75rem'),('4','1rem'),('5','1.25rem'),('6','1.5rem'),('8','2rem'),('10','2.5rem'),
 ('12','3rem'),('16','4rem'),('20','5rem'),('24','6rem'),('32','8rem'),('40','10rem'),
 ('48','12rem'),('56','14rem'),('64','16rem'),('80','20rem'),('96','24rem'),('120','30rem'),
 ('140','35rem'),('160','40rem'),('180','45rem'),('192','48rem'),('256','64rem'),
 ('320','80rem'),('360','90rem'),('400','100rem'),('480','120rem')]
spacing_prim_vars = [mk(f'--spacing-{n}', 'dimension', {'Light': rem},
                        'Spacing primitive (1 unit = 0.25rem = 4px)') for n, rem in SPACING_PRIM]

# ---------- 5. Spacing semantic (S1) — 17 ----------
SPACING_SEM = [
 ('none','0rem'),('xxs','0.125rem'),('xs','0.25rem'),('sm','0.375rem'),('md','0.5rem'),
 ('lg','0.75rem'),('xl','1rem'),('2xl','1.25rem'),('3xl','1.5rem'),('4xl','2rem'),
 ('5xl','2.5rem'),('6xl','3rem'),('7xl','4rem'),('8xl','5rem'),('9xl','6rem'),
 ('10xl','8rem'),('11xl','10rem')]
spacing_sem_vars = [mk(f'--spacing-{n}', 'dimension', {'Light': rem},
                       'Semantic spacing (gap/padding/margin trong component)') for n, rem in SPACING_SEM]

# ---------- 6. Widths (S1) — 12 ----------
WIDTHS = [
 ('xxs','20rem'),('xs','24rem'),('sm','30rem'),('md','35rem'),('lg','40rem'),('xl','48rem'),
 ('2xl','64rem'),('3xl','80rem'),('4xl','90rem'),('5xl','100rem'),('6xl','120rem')]
width_vars = [mk(f'--width-{n}', 'dimension', {'Light': rem},
                 'Max-width cố định cho section nội dung') for n, rem in WIDTHS]
width_vars.append(mk('--paragraph-max-width', 'dimension', {'Light': '45rem'},
                     'Max-width đoạn văn để độ dài dòng tối ưu (45–85 ký tự)'))

# ---------- 7. Containers (S1) — 3 ----------
cont_vars = [
 mk('--container-padding-mobile', 'dimension', {'Light': '1rem'}, 'Padding container mobile (16px)'),
 mk('--container-padding-desktop', 'dimension', {'Light': '2rem'}, 'Padding container desktop (32px)'),
 mk('--container-max-width-desktop', 'dimension', {'Light': '80rem'}, 'Max-width container desktop (1280px)'),
]

# ---------- 8. Radius (S1) — 11 ----------
RADIUS = [
 ('none','0px'),('xxs','0.125rem'),('xs','0.25rem'),('sm','0.375rem'),('md','0.5rem'),
 ('lg','0.625rem'),('xl','0.75rem'),('2xl','1rem'),('3xl','1.25rem'),('4xl','1.5rem'),('full','9999px')]
radius_vars = [mk(f'--radius-{n}', 'dimension', {'Light': v},
                  'Bo góc (radius)') for n, v in RADIUS]

# ---------- 9. Shadows (S1) — 7 styles / 15 layers ----------
# layers: (x,y,blur,spread,color_var,opacity%)
SHADOWS = {
 'shadow-xs':  [(0,1,2,0,'shadow-xs','5%')],
 'shadow-sm':  [(0,1,2,-1,'shadow-sm_02','10%'),(0,1,3,0,'shadow-sm_01','10%')],
 'shadow-md':  [(0,2,4,-2,'shadow-md_02','6%'),(0,4,6,-1,'shadow-md_01','10%')],
 'shadow-lg':  [(0,2,2,-1,'shadow-lg_03','4%'),(0,4,6,-2,'shadow-lg_02','3%'),(0,12,16,-4,'shadow-lg_01','8%')],
 'shadow-xl':  [(0,3,3,-1.5,'shadow-xl_03','4%'),(0,8,8,-4,'shadow-xl_02','3%'),(0,20,24,-4,'shadow-xl_01','8%')],
 'shadow-2xl': [(0,4,4,-2,'shadow-2xl_02','4%'),(0,24,48,-12,'shadow-2xl_01','18%')],
 'shadow-3xl': [(0,5,5,-2.5,'shadow-3xl_02','4%'),(0,32,64,-12,'shadow-3xl_01','14%')],
}
shadow_vars = []
for name, layers in SHADOWS.items():
    ly = [{'x': x, 'y': y, 'blur': b, 'spread': s,
           'color': f'Colors/Effects/Shadows/{c} (Dark: ? chưa đọc)', 'opacity': o}
          for (x, y, b, s, c, o) in layers]
    shadow_vars.append(mk(f'--{name}', 'effect', {'Light': '#000000'},
                          'Drop shadow (màu = biến, Light = đen + độ mờ)', layers=ly))

# ---------- 10. Focus rings (S1) — 7 ----------
FOCUS = {
 'focus-ring': '0 0 0 4 #9E77ED (focus-ring=brand-500) + 0 0 0 2 #FFFFFF (bg-primary)',
 'focus-ring-error': '0 0 0 4 #EF4444 (focus-ring-error=red-500) + 0 0 0 2 #FFFFFF (bg-primary)',
 'focus-ring-shadow-xs': 'ring 4 brand + gap 2 bg-primary ; 0 1 2 0 shadow-xs #000 5%',
 'focus-ring-shadow-sm': 'ring 4 brand + gap 2 ; 0 1 2 0 shadow-sm_02 10% ; 0 1 3 0 shadow-sm_01 10%',
 'focus-ring-error-shadow-xs': 'ring 4 red + gap 2 ; 0 1 2 0 shadow-xs 5%',
 'focus-ring-shadow-xs-skeuomorphic': 'ring 4 brand + gap 2 ; 0 1 2 0 shadow-xs 5% ; 0 -2 0 0 inner 5% ; 0 0 0 1 inner-border 18%',
 'focus-ring-error-shadow-xs-skeuomorphic': 'ring 4 red + gap 2 ; 0 1 2 0 shadow-xs 5% ; 0 -2 0 0 inner 5% ; 0 0 0 1 inner-border 18%',
}
focus_vars = [mk(f'--{n}', 'effect', {'Light': v}, 'Focus ring (kết hợp shadow)') for n, v in FOCUS.items()]

# ---------- 11. Backdrop blurs (S1) — 4 ----------
BLURS = {'backdrop-blur-sm':'8px','backdrop-blur-md':'16px','backdrop-blur-lg':'24px','backdrop-blur-xl':'40px'}
blur_vars = [mk(f'--{n}', 'effect', {'Light': v}, 'Backdrop blur') for n, v in BLURS.items()]

# ---------- 12. Typography text styles (S1) — 44 ----------
SIZES = [('Display 2xl',72,90,'-2%'),('Display xl',60,72,'-2%'),('Display lg',48,60,'-2%'),
         ('Display md',36,44,'-2%'),('Display sm',30,38,'0%'),('Display xs',24,32,'0%'),
         ('Text xl',20,30,'0%'),('Text lg',18,28,'0%'),('Text md',16,24,'0%'),
         ('Text sm',14,20,'0%'),('Text xs',12,18,'0%')]
WEIGHTS = [('Regular','400'),('Medium','500'),('Semibold','600'),('Bold','700')]
textstyle_vars = []
for name, size, lh, ls in SIZES:
    for wname, wval in WEIGHTS:
        textstyle_vars.append(mk(f'{name} / {wname}', 'typography',
                                 {'size': f'{size}px', 'lineHeight': f'{lh}px', 'weight': wval, 'letterSpacing': ls},
                                 f'Text style ({name}, {wname})'))

# ---------- assemble ----------
new_cols = [
 collection('0. Primitives / Colors (S1)', prim_vars,
            'S1 primitives màu (hex + nhãn WCAG). 26 dải × 11 + White/Black; Brand & Transparent đã hợp nhất vào collection S2 (src thêm S1).'),
 collection('0. Primitives / Alpha (S1)', alpha_vars,
            'S1 Alpha 20 biến theo bậc 10%; S2 chỉ có --color-alpha-white/-black dạng màu đặc.'),
 collection('1. Color modes / Utility (S1)', util_vars,
            'S1 Utility 118 biến. Lệch vs S2 (134): S1 đặt tên utility-error/-warning/-success (S2: red/yellow/green); S2 thừa amber+emerald (16); S1 thiếu 2 hue đó.'),
 collection('0. Primitives / Spacing (S1)', spacing_prim_vars,
            'S1 Spacing primitives 32 bậc (1 unit = 0.25rem = 4px), thuộc _Primitives → Spacing.'),
 collection('3. Spacing / Semantic (S1)', spacing_sem_vars,
            'S1 Spacing semantic 17 biến (collection 3. Spacing).'),
 collection('4. Widths (S1)', width_vars,
            'S1 Widths 11 + paragraph-max-width = 12 (collection 4. Widths).'),
 collection('5. Containers (S1)', cont_vars,
            'S1 Containers 3 (collection 5. Containers).'),
 collection('2. Radius (S1)', radius_vars,
            'S1 Radius 11 biến. ⚠ Lệch vs S3 (10): S1 có xxs + 4xl, không có DEFAULT; thang giá trị khác (S1 sm=6px vs S3 sm=4px…).'),
 collection('7. Effects / Shadows (S1)', shadow_vars,
            'S1 Shadow 7 style / 15 lớp. Màu là biến Colors/Effects/Shadows/*_NN (Dark chưa đọc → ?).'),
 collection('7. Effects / Focus rings (S1)', focus_vars,
            'S1 Focus ring 7 style (ring = spread 4 brand ngoài + spread 2 bg-primary trong).'),
 collection('7. Effects / Backdrop blurs (S1)', blur_vars,
            'S1 Backdrop blur 4 bậc.'),
 collection('6. Typography / Text styles (S1)', textstyle_vars,
            'S1 Text style 44 (11 cỡ × 4 độ đậm). Font Inter cho display + body.'),
]

d['collections'] = d['collections'] + new_cols

json.dump(d, open('tokens.untitled.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
open('tokens.untitled.json', 'a', encoding='utf-8').write('\n')

# summary
tot_s1 = sum(len(c['variables']) for c in new_cols)
print('S1-only collections added:', len(new_cols))
print('S1-only vars:', tot_s1)
for c in new_cols:
    print(f'  {c["name"]:45s} {len(c["variables"]):4d}')
