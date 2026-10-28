#!/usr/bin/env python3
"""Parse s1-colors.md -> _task/s1-primitives.json (hue -> step -> {hex, wcag, default})."""
import re, json

HUES = ['Base','Brand','Red','Orange','Amber','Yellow','Lime','Green','Emerald','Teal',
        'Cyan','Sky','Blue','Indigo','Violet','Purple','Fuchsia','Pink','Rose',
        'Slate','Gray','Zinc','Neutral','Stone','Taupe','Mauve','Mist','Olive']

lines = open('_task/s1-colors.md', encoding='utf-8').read().splitlines()
prim = {}

for ln in lines:
    s = ln.strip()
    m = re.match(r'^([A-Za-z]+)(?:\s*\([^)]*\))?:\s*(.*)$', s)
    if not m:
        continue
    hue, rest = m.group(1), m.group(2)
    if hue not in HUES:
        continue
    d = {}
    # split by '·'
    for tok in rest.split('·'):
        tok = tok.strip()
        if not tok:
            continue
        # step can be number or word (White/Black/Transparent)
        tm = re.match(r'^(?P<step>[A-Za-z]+|\d+)\s+#(?P<hex>[0-9A-Fa-f]{6})(?:\s+\[(?P<wcag>[^\]]*)\])?(?P<pct>\s*0%)?(?P<dot>\s*•)?$', tok)
        if not tm:
            print('UNPARSED token:', repr(tok), 'in line', repr(s))
            continue
        step = tm.group('step')
        d[step] = {
            'hex': '#' + tm.group('hex').upper(),
            'wcag': (tm.group('wcag') or '').strip(),
            'pct': bool(tm.group('pct')),
            'default': bool(tm.group('dot')),
        }
    prim[hue] = d

json.dump(prim, open('_task/s1-primitives.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# verify
total = 0
for hue in HUES:
    if hue not in prim:
        print('MISSING hue:', hue)
        continue
    steps = prim[hue]
    total += len(steps)
    print(f'{hue:10s} {len(steps):3d} steps: ' + ' '.join(sorted(steps, key=lambda x: (x.isdigit(), x))))
print('TOTAL cells:', total)

# expected: Base 3 + 27 dai * 11 = 300
print('Expected: 300 (Base 3 + 27*11=297)')
