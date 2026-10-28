import json,re,sys
d=json.load(open('tokens.untitled.json'))
s2={}
for c in d['collections']:
    if c['name'].startswith('1. Color modes /') and 'alias' not in c['name']:
        for v in c['variables']:
            s2[v['name'].replace('--color-','')]=v['values']
def norm(x):
    x=x.strip().replace('.','-')
    x=re.sub(r'^base-','',x)
    return {'rgb(0 0 0 / 0-1)':'#000000 10%','rgb(255 255 255)':'white'}.get(x,x)
def res(val,mode,depth=0):
    n=norm(val)
    if depth<4 and n in s2: return res(s2[n][mode],mode,depth+1)
    if depth<4 and ('text-'+n) in s2 and n.startswith('white'): return n
    return n
out=[];miss=[];ok=0
for line in open('_task/s1-semantic.tsv'):
    if line.startswith('#') or not line.strip(): continue
    t,l,dk,u=line.rstrip('\n').split('\t')
    if t not in s2: miss.append(t); continue
    for mode,v1 in (('Light',l),('Dark',dk)):
        raw=s2[t][mode]; v2=res(raw,mode)
        if norm(v1)==v2 or norm(v1)==norm(raw): ok+=1
        else: out.append(f'{t}\t{mode}\tS1={v1}\tS2={raw}' + (f' (→{v2})' if v2!=norm(raw) else ''))
s1names={l.split('\t')[0] for l in open('_task/s1-semantic.tsv') if l.strip() and not l.startswith('#')}
grp=('text-','border-','fg-','bg-')
only2=sorted(k for k in s2 if k.startswith(grp) and k not in s1names)
print(f'khớp {ok} ô; lệch {len(out)}; S1 có mà S2 không: {miss}')
print('\n'.join(out)); print('S2 có mà S1 không:', only2)
