import re, html, sys, glob, os

def extract(path):
    data = open(path, encoding='utf-8').read()
    # isolate main
    m = re.search(r'<main[^>]*>(.*?)</main>', data, re.S)
    if not m:
        m = re.search(r'<body[^>]*>(.*?)</body>', data, re.S)
    body = m.group(1) if m else data
    # drop scripts/styles/svg/nav/footer/code blocks handled separately
    body = re.sub(r'<(script|style|svg|noscript|iframe)[^>]*>.*?</\1>', ' ', body, flags=re.S|re.I)
    # pre blocks -> keep content
    body = re.sub(r'<pre[^>]*>(.*?)</pre>', lambda mm: '\n```\n'+html.unescape(re.sub(r'<[^>]+>','',mm.group(1)))+'\n```\n', body, flags=re.S|re.I)
    # block tags -> newline
    body = re.sub(r'</(h[1-6]|p|li|tr|div|section|ul|ol|table|blockquote)>', '\n', body, flags=re.I)
    body = re.sub(r'<(br|hr)[^>]*/?>', '\n', body, flags=re.I)
    body = re.sub(r'<(h[1-6]|li)[^>]*>', '\n', body, flags=re.I)
    body = re.sub(r'<(td|th)[^>]*>', '\t', body, flags=re.I)
    # strip remaining tags
    body = re.sub(r'<[^>]+>', '', body)
    body = html.unescape(body)
    # collapse whitespace
    lines = [ln.strip() for ln in body.split('\n')]
    out = []
    blank = 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank <= 1:
                out.append('')
            continue
        blank = 0
        out.append(ln)
    return '\n'.join(out).strip()

for f in sorted(glob.glob('raw/docs-*.html')):
    slug = os.path.basename(f)[5:-5]
    txt = extract(f)
    outp = 'raw/docs-%s.txt' % slug
    open(outp, 'w', encoding='utf-8').write(txt)
    print('%-14s %6d bytes -> %s' % (slug, len(txt), outp))
