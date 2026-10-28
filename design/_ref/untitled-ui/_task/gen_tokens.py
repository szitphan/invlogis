import re, json

css = open('raw/theme.css', encoding='utf-8').read()

def extract_block(text, start_pat):
    m = re.search(start_pat, text)
    i = m.end(); depth = 1; j = i
    while j < len(text):
        c = text[j]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return text[i:j]
        j += 1
    return text[i:]

theme_body = extract_block(css, r'@theme\s*\{')
dark_body  = extract_block(css, r'\.dark-mode\s*\{')

def parse(body):
    out = {}
    for m in re.finditer(r'(--[\w-]+)\s*:\s*(.*?);', body, re.S):
        name, val = m.group(1), re.sub(r'\s+', ' ', m.group(2)).strip()
        out[name] = val
    return out

light = parse(theme_body)
dark  = parse(dark_body)

# normalize value to alias (resolve var(--x) -> x, keep literal rgb as-is)
def alias(v):
    m = re.match(r'var\(--([\w-]+)\)$', v)
    if m: return m.group(1)
    return v

def alias_name(v):
    # produce friendly alias like neutral.700 from --color-neutral-700
    m = re.match(r'var\(--color-([\w-]+)\)$', v)
    if m: return m.group(1).replace('-', '.')
    m2 = re.match(r'var\(--([\w-]+)\)$', v)
    if m2: return m2.group(1)
    return v

def group_of(name):
    order = ['--color-utility-','--color-text-','--color-border-','--color-fg-','--color-bg-',
             '--color-brand-','--color-alpha-','--color-',
             '--shadow-','--drop-shadow-','--font-','--text-color-','--text-',
             '--breakpoint-','--max-width-','--animate-',
             '--background-color-','--border-color-','--ring-color-','--outline-color-']
    for p in order:
        if name.startswith(p):
            return p
    return '--other-'

groups = {}
for n, v in light.items():
    g = group_of(n)
    groups.setdefault(g, []).append((n, v))

def usage_for(n, g):
    if g == '--color-utility-':
        return 'Utility color step (mode-flipped)'
    if g in ('--text-color-','--background-color-','--border-color-','--ring-color-','--outline-color-'):
        return 'Tailwind property-color alias'
    if g == '--color-text-':
        return ''
    if g == '--color-border-': return ''
    if g == '--color-fg-': return ''
    if g == '--color-bg-': return ''
    if g == '--shadow-': return ''
    if g == '--text-': return ''
    return ''

collections = []
group_order = ['--color-brand-','--color-alpha-','--color-',
               '--color-utility-','--color-text-','--color-border-','--color-fg-','--color-bg-',
               '--text-color-','--background-color-','--border-color-','--ring-color-','--outline-color-',
               '--font-','--text-','--breakpoint-','--max-width-',
               '--shadow-','--drop-shadow-','--animate-']

def gname(g):
    return {
        '--color-brand-':'0. Primitives / Brand','--color-alpha-':'0. Primitives / Alpha','--color-':'0. Primitives / Base + Component',
        '--color-utility-':'1. Color modes / Utility','--color-text-':'1. Color modes / Text','--color-border-':'1. Color modes / Border',
        '--color-fg-':'1. Color modes / Foreground','--color-bg-':'1. Color modes / Background',
        '--text-color-':'1. Color modes / Text (property alias)','--background-color-':'1. Color modes / Background (property alias)',
        '--border-color-':'1. Color modes / Border (property alias)','--ring-color-':'1. Color modes / Ring (property alias)',
        '--outline-color-':'1. Color modes / Outline (property alias)',
        '--font-':'6. Typography / Font family','--text-':'6. Typography / Text scale',
        '--breakpoint-':'5. Containers / Breakpoints','--max-width-':'5. Containers / Max width',
        '--shadow-':'7. Effects / Shadows','--drop-shadow-':'7. Effects / Drop shadows','--animate-':'7. Effects / Animations',
    }[g]

for g in group_order:
    if g not in groups: continue
    vars_list = []
    for n, v in sorted(groups[g]):
        entry = {
            "name": n,
            "type": "color" if g.startswith('--color-') or g in ('--text-color-','--background-color-','--border-color-','--ring-color-','--outline-color-') else "dimension",
            "values": {"Light": alias_name(v)},
            "usage": usage_for(n, g),
            "src": ["S2"],
        }
        if n in dark:
            entry["values"]["Dark"] = alias_name(dark[n])
        else:
            entry["values"]["Dark"] = entry["values"]["Light"]  # mode-independent
        vars_list.append(entry)
    collections.append({"name": gname(g), "modes": ["Light","Dark"] if any(n in dark for n,_ in groups[g]) else ["Light"],
                        "variables": vars_list})

data = {
    "source": {
        "figma": "QERVV4a2Fpa1FmsZ5LGW3S",
        "repo": "untitleduico/react@1d410cb8facde8d50869e7bbb5f3d048e2267466",
        "read_at": "2026-10-26",
    },
    "collections": collections,
}

json.dump(data, open('tokens.untitled.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# summary
print("light vars:", len(light), " dark overrides:", len(dark))
total = sum(len(v) for v in groups.values())
print("grouped total:", total)
for g in group_order:
    if g in groups:
        nd = sum(1 for n,_ in groups[g] if n in dark)
        print(f"  {gname(g):55s} {len(groups[g]):4d} vars (dark: {nd})")
