#!/usr/bin/env node
/*
 * dev-scan.mjs — quét TĨNH 3 repo dev (BE .NET · FE Angular · app Flutter) ra JSON cho framework kiểm thử.
 * Không phụ thuộc gói ngoài (Node >= 20). Chỉ ĐỌC repo dev, chỉ GHI vào --out.
 *
 *   node .claude/scripts/dev-scan.mjs --out <dir> [--only be|fe|app]
 *        [--be <path>] [--fe <path>] [--app <path>] [--app-ref origin/tuanvv]
 *
 * Mặc định đường dẫn: ~/Desktop/szit/AI/Projects/invlogis-dev/{transport-erp,transport-erp-fe,driver-portal-flutter}
 *
 * Ra: be-endpoints · be-permissions · be-acs · be-db · be-tests · fe-routes · fe-testids ·
 *     app-routes · app-semantics · jira-keys · summary (.json)
 *
 * Quy ước route BE: ModuleApiRoutePrefixConvention thêm `api/{module}/v{version:apiVersion}` vào
 * controller của assembly có [assembly: ApiModule("x")]; controller host tự khai `api/v{version:apiVersion}/...`.
 *
 * Import-safe: chỉ chạy main() khi được gọi trực tiếp.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

/* ------------------------------------------------------------------ utils */

export const AC_RE_SRC = String.raw`(?<![A-Za-z0-9-])[A-Z]{2,4}(?:-[A-Z0-9]+)+-AC-\d{3}(?![A-Za-z0-9])`;

export function lineStarts(text) {
  const a = [0];
  for (let i = 0; i < text.length; i++) if (text.charCodeAt(i) === 10) a.push(i + 1);
  return a;
}
export function lineOf(starts, idx) {
  let lo = 0, hi = starts.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (starts[mid] <= idx) lo = mid; else hi = mid - 1;
  }
  return lo + 1;
}

/**
 * Che comment + nội dung chuỗi bằng khoảng trắng / 'x' nhưng GIỮ độ dài và xuống dòng, để phân tích cấu trúc
 * (ngoặc, dấu phẩy) trên bản che rồi cắt giá trị thật từ bản gốc cùng chỉ số.
 * lang: 'cs' | 'ts' | 'dart'
 */
export function maskSource(src, lang = 'cs') {
  const n = src.length;
  const out = new Array(n);
  const keep = (c) => (c === '\n' || c === '\r' ? c : ' ');
  const keepX = (c) => (c === '\n' || c === '\r' ? c : 'x');
  let i = 0;
  while (i < n) {
    const c = src[i], d = src[i + 1];
    if (c === '/' && d === '/') {
      while (i < n && src[i] !== '\n') { out[i] = ' '; i++; }
      continue;
    }
    if (c === '/' && d === '*') {
      out[i] = ' '; out[i + 1] = ' '; i += 2;
      while (i < n && !(src[i] === '*' && src[i + 1] === '/')) { out[i] = keep(src[i]); i++; }
      if (i < n) { out[i] = ' '; out[i + 1] = ' '; i += 2; }
      continue;
    }
    if (c === '"' || c === "'" || (c === '`' && lang === 'ts')) {
      // raw / triple-quoted
      let q = 1;
      while (src[i + q] === c) q++;
      const triple = (lang === 'cs' && c === '"' && q >= 3) || (lang === 'dart' && q >= 3 && q < 6);
      if (triple) {
        for (let k = 0; k < q; k++) out[i + k] = c;
        i += q;
        const close = c.repeat(q);
        while (i < n && !src.startsWith(close, i)) { out[i] = keepX(src[i]); i++; }
        if (i < n) { for (let k = 0; k < q; k++) out[i + k] = c; i += q; }
        continue;
      }
      const verbatim = lang === 'cs' && c === '"' && (src[i - 1] === '@' || (src[i - 1] === '$' && src[i - 2] === '@') || (src[i - 1] === '@' && src[i - 2] === '$'));
      const rawDart = lang === 'dart' && (src[i - 1] === 'r');
      out[i] = c; i++;
      while (i < n) {
        const ch = src[i];
        if (verbatim) {
          if (ch === '"' && src[i + 1] === '"') { out[i] = 'x'; out[i + 1] = 'x'; i += 2; continue; }
          if (ch === '"') break;
        } else {
          if (ch === '\\' && !rawDart) { out[i] = 'x'; if (i + 1 < n) out[i + 1] = keepX(src[i + 1]); i += 2; continue; }
          if (ch === c) break;
          if (ch === '\n' && c !== '`') break; // chuỗi đơn dòng bị hở: dừng để khỏi nuốt cả file
        }
        out[i] = keepX(ch); i++;
      }
      if (i < n && src[i] === c) { out[i] = c; i++; }
      continue;
    }
    out[i] = c; i++;
  }
  return out.join('');
}

const OPEN = { '(': ')', '[': ']', '{': '}' };
/** Vị trí ngoặc đóng tương ứng của ngoặc mở tại openIdx (trên bản đã che); -1 nếu hở. */
export function matchClose(masked, openIdx) {
  const o = masked[openIdx], cl = OPEN[o];
  let depth = 0;
  for (let i = openIdx; i < masked.length; i++) {
    const ch = masked[i];
    if (ch === o) depth++;
    else if (ch === cl) { depth--; if (depth === 0) return i; }
  }
  return -1;
}
/** Tách theo dấu phẩy cấp 0 trong [s,e) của bản che; trả mảng [start,end). */
export function splitTop(masked, s, e) {
  const parts = [];
  let depth = 0, from = s;
  for (let i = s; i < e; i++) {
    const ch = masked[i];
    if (ch === '(' || ch === '[' || ch === '{') depth++;
    else if (ch === ')' || ch === ']' || ch === '}') depth--;
    else if (ch === ',' && depth === 0) { parts.push([from, i]); from = i + 1; }
  }
  if (masked.slice(from, e).trim() !== '') parts.push([from, e]);
  return parts;
}

export function walk(dir, filter, skipDirs = ['node_modules', 'bin', 'obj', '.git', 'dist', '.angular']) {
  const out = [];
  const rec = (d) => {
    let ents;
    try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return; }
    for (const e of ents) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) { if (!skipDirs.includes(e.name)) rec(p); }
      else if (filter(p)) out.push(p);
    }
  };
  rec(dir);
  return out.sort();
}
const read = (p) => fs.readFileSync(p, 'utf8');
const rel = (root, p) => path.relative(root, p).split(path.sep).join('/');
const writeJson = (dir, name, obj) => { fs.mkdirSync(dir, { recursive: true }); fs.writeFileSync(path.join(dir, name), JSON.stringify(obj, null, 2) + '\n'); };
function git(repo, args, opts = {}) {
  return execFileSync('git', ['-C', repo, ...args], { encoding: 'utf8', maxBuffer: 1 << 29, stdio: ['ignore', 'pipe', 'pipe'], ...opts });
}
function gitTry(repo, args) { try { return git(repo, args); } catch (e) { return e.stdout ? String(e.stdout) : ''; } }
const bump = (o, k, n = 1) => { o[k] = (o[k] ?? 0) + n; };
const sortObj = (o) => Object.fromEntries(Object.entries(o).sort(([a], [b]) => a.localeCompare(b)));

/* ------------------------------------------------------------------ BE: permissions */

export function parsePermissionFile(file, text, rootRel) {
  const starts = lineStarts(text);
  const masked = maskSource(text, 'cs');
  const classes = [...masked.matchAll(/\bclass\s+(\w+)/g)].map((m) => ({ name: m[1], idx: m.index }));
  const res = [];
  let unresolved = 0;
  for (const m of masked.matchAll(/\bconst\s+string\s+(\w+)\s*=\s*([^;]*);/g)) {
    const valMasked = m[2].trim();
    const origVal = text.slice(m.index + m[0].length - 1 - m[2].length, m.index + m[0].length - 1).trim();
    const lit = origVal.match(/^"((?:[^"\\]|\\.)*)"$/);
    const cls = [...classes].reverse().find((c) => c.idx < m.index)?.name ?? null;
    if (!lit || !/^"x*"$/.test(valMasked)) { unresolved++; continue; }
    res.push({ class: cls, name: m[1], code: lit[1], file: rootRel, line: lineOf(starts, m.index) });
  }
  return { entries: res, unresolved };
}

/* ------------------------------------------------------------------ BE: controllers */

const HTTP_ATTRS = { HttpGet: 'GET', HttpPost: 'POST', HttpPut: 'PUT', HttpPatch: 'PATCH', HttpDelete: 'DELETE', HttpHead: 'HEAD', HttpOptions: 'OPTIONS' };

/** Đọc danh sách attribute ở đầu chunk (đã che). Trả {attrs:[{name,args:[orig...]}], rest}. */
function parseAttributes(masked, orig, s, e) {
  const attrs = [];
  let i = s;
  for (;;) {
    while (i < e && /\s/.test(masked[i])) i++;
    if (masked[i] !== '[') break;
    const close = matchClose(masked, i);
    if (close < 0 || close >= e) break;
    for (const [ps, pe] of splitTop(masked, i + 1, close)) {
      const mm = masked.slice(ps, pe);
      const nm = mm.match(/^\s*([\w.]+)\s*(\(|$)/);
      if (!nm) continue;
      let name = nm[1].split('.').pop().replace(/Attribute$/, '');
      let args = [];
      const po = mm.indexOf('(');
      if (po >= 0) {
        const absOpen = ps + po;
        const absClose = matchClose(masked, absOpen);
        if (absClose > 0) args = splitTop(masked, absOpen + 1, absClose).map(([a, b]) => orig.slice(a, b).trim());
      }
      attrs.push({ name, args });
    }
    i = close + 1;
  }
  return { attrs, restStart: i };
}
const strLit = (s) => { const m = s?.match(/^\$?@?"((?:[^"\\]|\\.)*)"$/s); return m ? m[1] : null; };
const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();

/** Phân tích 1 file .cs, trả danh sách endpoint thô (chưa gắn prefix module). */
export function parseControllerFile(text) {
  const masked = maskSource(text, 'cs');
  const starts = lineStarts(text);
  const out = [];
  const aliases = {};
  for (const m of text.matchAll(/const\s+PermissionLogic\s+(\w+)\s*=\s*PermissionLogic\.(\w+)/g)) aliases[m[1]] = m[2];
  for (const cm of masked.matchAll(/\bclass\s+(\w+)/g)) {
    const className = cm[1];
    const lastTerm = Math.max(masked.lastIndexOf(';', cm.index), masked.lastIndexOf('}', cm.index), masked.lastIndexOf('{', cm.index));
    const { attrs: classAttrs } = parseAttributes(masked, text, lastTerm + 1, cm.index);
    // thân lớp: '{' đầu tiên sau tên lớp ở cấp 0 (bỏ qua primary-ctor và base list)
    let bi = cm.index + cm[0].length;
    let pd = 0;
    for (; bi < masked.length; bi++) {
      const ch = masked[bi];
      if (ch === '(') pd++; else if (ch === ')') pd--; else if (ch === '{' && pd === 0) break; else if (ch === ';' && pd === 0) { bi = -1; break; }
    }
    if (bi < 0 || bi >= masked.length) continue;
    const bodyEnd = matchClose(masked, bi);
    if (bodyEnd < 0) continue;
    const isController = classAttrs.some((a) => a.name === 'ApiController') || /Controller\b/.test(className);
    if (!isController) continue;

    const clsRoute = strLit(classAttrs.find((a) => a.name === 'Route')?.args[0]);
    const clsVersions = classAttrs.filter((a) => a.name === 'ApiVersion').map((a) => strLit(a.args[0])).filter(Boolean);
    const clsModule = strLit(classAttrs.find((a) => a.name === 'ApiModule')?.args[0]);
    const cls = {
      name: className,
      route: clsRoute,
      versions: clsVersions,
      apiModule: clsModule,
      permission: pickPermission(classAttrs, aliases),
      wcr: pickWcr(classAttrs),
      authorize: classAttrs.some((a) => a.name === 'Authorize'),
      anonymous: classAttrs.some((a) => a.name === 'AllowAnonymous'),
    };

    // chia thành member ở cấp 0 của thân lớp
    let i = bi + 1;
    let memberStart = i;
    let paren = 0;
    const members = [];
    while (i < bodyEnd) {
      const ch = masked[i];
      if (ch === '(' || ch === '[') paren++;
      else if (ch === ')' || ch === ']') paren--;
      else if (ch === ';' && paren === 0) { members.push([memberStart, i]); memberStart = i + 1; }
      else if (ch === '{' && paren === 0) {
        const c2 = matchClose(masked, i);
        if (c2 < 0) break;
        members.push([memberStart, c2]);
        i = c2;
        // property initializer sau '}'
        let j = i + 1;
        while (j < bodyEnd && /\s/.test(masked[j])) j++;
        if (masked[j] === '=' && masked[j + 1] !== '>') {
          const semi = masked.indexOf(';', j);
          i = semi > 0 ? semi : j;
        }
        memberStart = i + 1;
      }
      i++;
    }

    for (const [ms, me] of members) {
      const { attrs, restStart } = parseAttributes(masked, text, ms, me);
      const httpAttrs = attrs.filter((a) => HTTP_ATTRS[a.name]);
      if (!httpAttrs.length) continue;
      const sig = masked.slice(restStart, me);
      const sm = sig.match(/(\w+)\s*(?:<[^>(]*>)?\s*\(/);
      if (!sm) continue;
      const actionName = sm[1];
      const nameIdx = restStart + sig.indexOf(sm[0]);
      const methodRoute = strLit(attrs.find((a) => a.name === 'Route')?.args[0]);
      const mapTo = attrs.filter((a) => a.name === 'MapToApiVersion').map((a) => strLit(a.args[0])).filter(Boolean);
      const mp = pickPermission(attrs, aliases);
      const mw = pickWcr(attrs);
      for (const h of httpAttrs) {
        const first = h.args[0];
        const tmpl = first !== undefined && strLit(first) !== null ? strLit(first) : (methodRoute ?? null);
        out.push({
          controllerClass: className,
          actionName,
          method: HTTP_ATTRS[h.name],
          methodTemplate: tmpl,
          classTemplate: cls.route,
          versions: mapTo.length ? mapTo : cls.versions,
          apiModuleAttr: cls.apiModule,
          permission: mp ?? cls.permission,
          permissionFrom: mp ? 'method' : (cls.permission ? 'class' : null),
          workingContext: mw ?? cls.wcr,
          authorize: cls.authorize || attrs.some((a) => a.name === 'Authorize'),
          anonymous: cls.anonymous || attrs.some((a) => a.name === 'AllowAnonymous'),
          line: lineOf(starts, nameIdx),
        });
      }
    }
  }
  return out;
}

function pickPermission(attrs, aliases = {}) {
  const a = attrs.find((x) => x.name === 'HasPermission');
  if (!a) return null;
  let logic = null;
  const refs = [];
  for (const arg of a.args) {
    if (/^PermissionLogic\./.test(arg)) { logic = arg.split('.').pop(); continue; }
    if (aliases[arg]) { logic = aliases[arg]; continue; }
    const lit = strLit(arg);
    refs.push(lit !== null ? { literal: lit } : { ref: arg.replace(/\s+/g, '') });
  }
  return { logic, refs };
}
function pickWcr(attrs) {
  const a = attrs.find((x) => x.name === 'WorkingContextRequirement');
  if (!a) return null;
  return { requirement: (a.args[0] ?? '').split('.').pop() || null, moduleCode: a.args[1] ?? null };
}

export function composeRoute({ prefix, version, classTemplate, methodTemplate }) {
  const isAbs = (t) => typeof t === 'string' && (t.startsWith('/') || t.startsWith('~/'));
  const clean = (t) => (t ?? '').replace(/^~?\//, '');
  let segs;
  if (isAbs(methodTemplate)) segs = [clean(methodTemplate)];
  else if (isAbs(classTemplate)) segs = [clean(classTemplate), methodTemplate ?? ''];
  else segs = [prefix ?? '', classTemplate ?? '', methodTemplate ?? ''];
  // prefix chỉ áp khi route lớp không tuyệt đối (khớp CombineAttributeRouteModel)
  if (isAbs(methodTemplate) || isAbs(classTemplate)) { /* giữ nguyên, không prefix */ }
  let r = segs.filter(Boolean).join('/').replace(/\/{2,}/g, '/');
  const vNum = String(version ?? '1.0').split('.')[0];
  r = r.replace(/\{version:apiVersion\}/g, vNum);
  return '/' + r.replace(/^\/+|\/+$/g, '');
}

function findApiModuleForFile(file, root, cache) {
  let dir = path.dirname(file);
  while (dir.startsWith(root)) {
    if (cache.has(dir)) return cache.get(dir);
    const ai = path.join(dir, 'Properties', 'AssemblyInfo.cs');
    let hit;
    if (fs.existsSync(ai)) {
      const m = read(ai).match(/assembly:\s*ApiModule\(\s*"([^"]+)"/);
      hit = m ? m[1] : null;
    }
    if (hit !== undefined) { cache.set(dir, hit); return hit; }
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return null;
}
function moduleOf(relPath) {
  const m = relPath.match(/^src\/Modules\/([^/]+)\//);
  if (m) return m[1];
  if (relPath.startsWith('src/Host/')) return 'Host';
  if (relPath.startsWith('src/BuildingBlocks/')) return 'BuildingBlocks';
  return 'Other';
}

export function scanBeEndpoints(beRoot, permMap) {
  const files = walk(path.join(beRoot, 'src'), (p) => /Controller\.cs$/.test(p));
  const cache = new Map();
  const endpoints = [];
  const problems = [];
  for (const f of files) {
    const relPath = rel(beRoot, f);
    const raw = parseControllerFile(read(f));
    if (!raw.length) continue;
    const apiModule = findApiModuleForFile(f, beRoot, cache);
    for (const r of raw) {
      const prefixModule = r.apiModuleAttr ?? apiModule;
      const prefix = prefixModule && !(r.classTemplate ?? '').startsWith('/') ? `api/${prefixModule}/v{version:apiVersion}` : '';
      const version = r.versions[0] ?? '1.0';
      const fullRoute = composeRoute({ prefix, version, classTemplate: r.classTemplate, methodTemplate: r.methodTemplate });
      if (!prefix && !/^\/api\//.test(fullRoute)) problems.push({ file: relPath, line: r.line, note: 'route không có tiền tố api/', route: fullRoute });
      const controller = r.controllerClass.replace(/Controller$/, '');
      const perms = (r.permission?.refs ?? []).map((x) => {
        if (x.literal !== undefined) return { ref: null, code: x.literal };
        const hit = permMap.get(x.ref) ?? permMap.get(x.ref.split('.').pop());
        return { ref: x.ref, code: hit?.code ?? null };
      });
      endpoints.push({
        module: moduleOf(relPath),
        apiModule: prefixModule ?? null,
        controller,
        controllerClass: r.controllerClass,
        action: r.actionName,
        operationId: `${controller}_${r.actionName}`,
        httpMethod: r.method,
        route: fullRoute,
        apiVersion: version,
        classTemplate: r.classTemplate,
        methodTemplate: r.methodTemplate,
        permissions: perms,
        permissionLogic: r.permission ? (r.permission.logic ?? (perms.length > 1 ? 'default' : null)) : null,
        permissionFrom: r.permissionFrom,
        workingContext: r.workingContext,
        authorize: r.authorize,
        anonymous: r.anonymous,
        file: relPath,
        line: r.line,
      });
    }
  }
  return { endpoints, problems };
}

export function scanBePermissions(beRoot) {
  const files = walk(path.join(beRoot, 'src'), (p) => /\.cs$/.test(p) && (/[\\/]Permissions[\\/]/.test(p) || /PermissionCodes\.cs$/.test(p)));
  const items = [];
  let unresolved = 0;
  for (const f of files) {
    const { entries, unresolved: u } = parsePermissionFile(f, read(f), rel(beRoot, f));
    unresolved += u;
    for (const e of entries) items.push({ ...e, module: moduleOf(e.file), kind: /EpicCodes|FeatureCodes|Namespace/.test(e.file) ? 'segment' : 'permission' });
  }
  return { items, unresolved };
}

/* ------------------------------------------------------------------ BE: ACs */

export function parseAcDocs(text, fileRel) {
  const lines = text.split(/\r?\n/);
  const acRe = new RegExp(AC_RE_SRC, 'g');
  const defs = [];
  const mentions = [];
  let header = null;
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    if (/^\s*\|/.test(ln)) {
      const cells = ln.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
      if (cells.every((c) => /^:?-{2,}:?$/.test(c))) {
        const prev = lines[i - 1];
        if (prev && /^\s*\|/.test(prev)) header = prev.trim().replace(/^\||\|$/g, '').split('|').map((c) => c.trim());
        continue;
      }
      const first = cells[0].replace(/[`*_]/g, '').trim();
      if (new RegExp(`^${AC_RE_SRC}$`).test(first)) {
        defs.push({ id: first, file: fileRel, line: i + 1, title: cells[1] ?? '', cells: cells.slice(1), header });
        continue;
      }
    } else if (!/^\s*$/.test(ln)) header = header && /^\s*\|/.test(lines[i - 1] ?? '') ? header : null;
    for (const m of ln.matchAll(acRe)) mentions.push({ id: m[0], file: fileRel, line: i + 1 });
  }
  return { defs, mentions };
}

export function scanBeAcs(beRoot) {
  const docFiles = [
    ...walk(path.join(beRoot, 'docs'), (p) => /\.md$/.test(p)),
    ...fs.readdirSync(beRoot).filter((n) => /\.md$/.test(n)).map((n) => path.join(beRoot, n)),
  ];
  const defs = [];
  const mentions = [];
  for (const f of docFiles) {
    const { defs: d, mentions: m } = parseAcDocs(read(f), rel(beRoot, f));
    defs.push(...d);
    mentions.push(...m);
  }
  const testFiles = walk(path.join(beRoot, 'tests'), (p) => /\.cs$/.test(p));
  const testMap = new Map();
  const acRe = new RegExp(AC_RE_SRC, 'g');
  for (const f of testFiles) {
    const t = read(f);
    for (const m of new Set(t.match(acRe) ?? [])) {
      if (!testMap.has(m)) testMap.set(m, []);
      testMap.get(m).push(rel(beRoot, f));
    }
  }
  const byId = new Map();
  for (const d of defs) {
    if (!byId.has(d.id)) byId.set(d.id, { ...d, definedAt: [{ file: d.file, line: d.line }] });
    else byId.get(d.id).definedAt.push({ file: d.file, line: d.line });
  }
  const acs = [...byId.values()].sort((a, b) => a.id.localeCompare(b.id)).map((d) => ({
    id: d.id, file: d.file, line: d.line, title: d.title, cells: d.cells, header: d.header,
    duplicateDefinitions: d.definedAt.length > 1 ? d.definedAt : undefined,
    tests: testMap.get(d.id) ?? [], traced: testMap.has(d.id),
  }));
  const allDocIds = new Set([...mentions.map((m) => m.id), ...defs.map((d) => d.id)]);
  const mentionOnly = [...allDocIds].filter((id) => !byId.has(id)).sort().map((id) => ({
    id, mentions: mentions.filter((m) => m.id === id).slice(0, 5), tests: testMap.get(id) ?? [], traced: testMap.has(id),
  }));
  const testOnly = [...testMap.keys()].filter((id) => !allDocIds.has(id)).sort().map((id) => ({ id, tests: testMap.get(id) }));
  return {
    acs, mentionOnly, testOnly,
    totals: {
      definedUnique: acs.length,
      mentionedInDocsUnique: allDocIds.size,
      tracedByTests: acs.filter((a) => a.traced).length,
      untraced: acs.filter((a) => !a.traced).length,
      idsInTestsNotInDocs: testOnly.length,
    },
  };
}

/* ------------------------------------------------------------------ BE: db snapshots */

export function parseSnapshot(text) {
  const lines = text.split(/\r?\n/);
  const ctx = text.match(/\[DbContext\(typeof\((\w+)\)\)\]/)?.[1] ?? null;
  const defaultSchema = text.match(/\.HasDefaultSchema\("([^"]+)"\)/)?.[1] ?? null;
  const entities = new Map();
  let cur = null;
  let stmt = null;
  for (let i = 0; i < lines.length; i++) {
    const ln = lines[i];
    let m = ln.match(/^\s*modelBuilder\.Entity\("([^"]+)",\s*b\s*=>/);
    if (m) {
      cur = entities.get(m[1]) ?? { fqn: m[1], name: m[1].split('.').pop(), table: null, schema: null, view: null, columns: [], ownedTables: [], line: i + 1 };
      entities.set(m[1], cur);
      stmt = null;
      continue;
    }
    if (!cur) continue;
    m = ln.match(/^\s*b\.Property<([^>]+)>\("([^"]+)"\)/);
    if (m) { stmt = { property: m[2], clr: m[1], column: m[2], dbType: null, required: !m[1].endsWith('?'), maxLength: null, key: false }; cur.columns.push(stmt); }
    if (stmt) {
      let mm;
      if ((mm = ln.match(/\.HasColumnName\("([^"]+)"\)/))) stmt.column = mm[1];
      if ((mm = ln.match(/\.HasColumnType\("([^"]+)"\)/))) stmt.dbType = mm[1];
      if ((mm = ln.match(/\.HasMaxLength\((\d+)\)/))) stmt.maxLength = Number(mm[1]);
      if (/\.IsRequired\(\)/.test(ln)) stmt.required = true;
      if (/;\s*$/.test(ln)) stmt = null;
    }
    if ((m = ln.match(/^\s*b\.ToTable\("([^"]+)"(?:,\s*(?:"([^"]*)"|null|\(string\)null))?/))) { cur.table = m[1]; cur.schema = m[2] ?? defaultSchema; }
    else if ((m = ln.match(/^\s*b\.ToView\("([^"]+)"(?:,\s*(?:"([^"]*)"|null|\(string\)null))?/))) { cur.view = m[1]; cur.schema = m[2] ?? defaultSchema; }
    else if ((m = ln.match(/^\s*b\d+\.ToTable\("([^"]+)"(?:,\s*(?:"([^"]*)"|null|\(string\)null))?/))) cur.ownedTables.push({ table: m[1], schema: m[2] ?? defaultSchema });
    if ((m = ln.match(/^\s*b\.HasKey\(([^)]*)\)/))) {
      const keys = [...m[1].matchAll(/"([^"]+)"/g)].map((x) => x[1]);
      for (const c of cur.columns) if (keys.includes(c.property)) c.key = true;
    }
  }
  return { dbContext: ctx, defaultSchema, entities: [...entities.values()].filter((e) => e.table || e.view || e.ownedTables.length) };
}

export function scanBeDb(beRoot) {
  const files = walk(path.join(beRoot, 'src'), (p) => /ModelSnapshot\.cs$/.test(p));
  const contexts = [];
  for (const f of files) {
    const relPath = rel(beRoot, f);
    const parsed = parseSnapshot(read(f));
    contexts.push({ module: moduleOf(relPath), dbContext: parsed.dbContext, defaultSchema: parsed.defaultSchema, file: relPath, entityCount: parsed.entities.length, entities: parsed.entities });
  }
  return contexts;
}

/* ------------------------------------------------------------------ BE: tests */

export function scanBeTests(beRoot) {
  const root = path.join(beRoot, 'tests');
  const csprojs = walk(root, (p) => /\.csproj$/.test(p));
  const projects = [];
  const traitTotals = {};
  for (const proj of csprojs) {
    const dir = path.dirname(proj);
    const files = walk(dir, (p) => /\.cs$/.test(p));
    const counts = { fact: 0, theory: 0, inlineData: 0, memberData: 0, classData: 0, skipped: 0 };
    const traits = {};
    let withTrait = 0;
    for (const f of files) {
      const t = read(f);
      counts.fact += (t.match(/^[ \t]*\[Fact\b/gm) ?? []).length;
      counts.theory += (t.match(/^[ \t]*\[Theory\b/gm) ?? []).length;
      counts.inlineData += (t.match(/^[ \t]*\[InlineData\b/gm) ?? []).length;
      counts.memberData += (t.match(/^[ \t]*\[MemberData\b/gm) ?? []).length;
      counts.classData += (t.match(/^[ \t]*\[ClassData\b/gm) ?? []).length;
      counts.skipped += (t.match(/\[(?:Fact|Theory)\([^)]*Skip\s*=/g) ?? []).length;
      for (const m of t.matchAll(/\[Trait\(\s*"([^"]*)"\s*,\s*"?([^")]*)"?\s*\)\]/g)) {
        bump(traits, `${m[1]}=${m[2]}`);
        bump(traitTotals, `${m[1]}=${m[2]}`);
        withTrait++;
      }
    }
    projects.push({
      project: path.basename(proj, '.csproj'),
      dir: rel(beRoot, dir),
      kind: rel(beRoot, dir).split('/')[1] ?? null,
      csFiles: files.length,
      ...counts,
      tests: counts.fact + counts.theory,
      traitUsages: withTrait,
      traits: sortObj(traits),
    });
  }
  return {
    projects,
    totals: {
      projects: projects.length,
      fact: projects.reduce((s, p) => s + p.fact, 0),
      theory: projects.reduce((s, p) => s + p.theory, 0),
      testMethods: projects.reduce((s, p) => s + p.tests, 0),
      traitUsages: projects.reduce((s, p) => s + p.traitUsages, 0),
    },
    traits: sortObj(traitTotals),
  };
}

/* ------------------------------------------------------------------ FE */

export function parseEnumsAndConsts(text) {
  const enums = {};
  const consts = {};
  for (const m of text.matchAll(/export\s+(?:const\s+)?enum\s+(\w+)\s*\{([^}]*)\}/g)) {
    const e = {};
    for (const x of m[2].matchAll(/(\w+)\s*=\s*(['"])([^'"]*)\2/g)) e[x[1]] = x[3];
    enums[m[1]] = e;
  }
  for (const m of text.matchAll(/export\s+const\s+(\w+)\s*(?::\s*string)?\s*=\s*(['"])([^'"]*)\2\s*;/g)) consts[m[1]] = m[3];
  return { enums, consts };
}

export function resolveTsExpr(expr, scope) {
  const e = (expr ?? '').trim();
  if (!e) return { value: '', unresolved: false };
  let m = e.match(/^(['"])([^'"]*)\1$/);
  if (m) return { value: m[2], unresolved: false };
  if (e.startsWith('`') && e.endsWith('`')) {
    let un = false;
    const v = e.slice(1, -1).replace(/\$\{([^}]+)\}/g, (_, inner) => { const r = resolveTsExpr(inner, scope); if (r.unresolved) un = true; return r.value; });
    return { value: v, unresolved: un };
  }
  if ((m = e.match(/^(\w+)\.(\w+)$/))) {
    const v = scope.enums[m[1]]?.[m[2]];
    if (v !== undefined) return { value: v, unresolved: false };
  }
  if (/^\w+$/.test(e) && scope.consts[e] !== undefined) return { value: scope.consts[e], unresolved: false };
  if (e.includes('+')) {
    let un = false;
    const v = e.split('+').map((p) => { const r = resolveTsExpr(p, scope); if (r.unresolved) un = true; return r.value; }).join('');
    return { value: v, unresolved: un };
  }
  return { value: e, unresolved: true };
}

function buildTsScope(file, text, cache) {
  const scope = { enums: {}, consts: {} };
  const local = parseEnumsAndConsts(text);
  Object.assign(scope.enums, local.enums);
  Object.assign(scope.consts, local.consts);
  for (const m of text.matchAll(/import\s*\{([^}]+)\}\s*from\s*'(\.[^']+)'/g)) {
    const target = path.resolve(path.dirname(file), m[2]) + '.ts';
    if (!fs.existsSync(target)) continue;
    if (!cache.has(target)) cache.set(target, parseEnumsAndConsts(read(target)));
    const t = cache.get(target);
    for (const spec of m[1].split(',')) {
      const [name, alias] = spec.trim().split(/\s+as\s+/);
      if (!name) continue;
      const a = alias ?? name;
      if (t.enums[name]) scope.enums[a] = t.enums[name];
      if (t.consts[name] !== undefined) scope.consts[a] = t.consts[name];
    }
  }
  return scope;
}

export function parseMenuPermissions(text, permByKey) {
  const masked = maskSource(text, 'ts');
  const out = {};
  for (const m of masked.matchAll(/\[\s*MenuId\.(\w+)\s*\]\s*:\s*\{/g)) {
    const open = m.index + m[0].length - 1;
    const close = matchClose(masked, open);
    if (close < 0) continue;
    const block = masked.slice(open, close + 1);
    const pm = block.match(/\bpermissions\s*:\s*\[/);
    if (!pm) { out[m[1]] = { permissions: undefined, raw: null }; continue; }
    const pOpen = open + pm.index + pm[0].length - 1;
    const pClose = matchClose(masked, pOpen);
    const parts = splitTop(masked, pOpen + 1, pClose).map(([a, b]) => text.slice(a, b).trim());
    out[m[1]] = {
      permissions: parts.map((p) => permByKey[p.split('.').pop()] ?? (strLitTs(p) ?? null)),
      raw: parts,
    };
  }
  return out;
}
const strLitTs = (s) => s.match(/^(['"`])([^'"`$]*)\1$/)?.[2] ?? null;

export function parseRoutesFile(file, text, scope, menuPerms, relPath) {
  const masked = maskSource(text, 'ts');
  const starts = lineStarts(text);
  const results = [];
  const unresolved = [];
  const arrays = [];
  for (const m of masked.matchAll(/(?:export\s+)?const\s+(\w+)\s*:\s*Routes\s*=\s*\[/g)) arrays.push({ name: m[1], open: m.index + m[0].length - 1 });

  const parseArray = (open, parentPath, arrayName, depth) => {
    const close = matchClose(masked, open);
    if (close < 0) return;
    for (const [s, e] of splitTop(masked, open + 1, close)) {
      const seg = masked.slice(s, e);
      const lead = seg.search(/\S/);
      if (lead < 0) continue;
      const abs = s + lead;
      if (masked.startsWith('...', abs)) {
        results.push({ file: relPath, array: arrayName, spread: text.slice(abs + 3, e).trim(), fullPath: null, line: lineOf(starts, abs) });
        continue;
      }
      if (masked[abs] !== '{') continue;
      const oClose = matchClose(masked, abs);
      const props = {};
      for (const [ps, pe] of splitTop(masked, abs + 1, oClose)) {
        const pm = masked.slice(ps, pe).match(/^\s*(\w+)\s*:/);
        if (!pm) continue;
        const vs = ps + pm[0].length;
        props[pm[1]] = { s: vs, e: pe, v: text.slice(vs, pe).trim() };
      }
      let seg1 = null, un = false;
      if (props.path) { const r = resolveTsExpr(props.path.v, scope); seg1 = r.value; un = r.unresolved; if (un) unresolved.push({ file: relPath, expr: props.path.v }); }
      const full = [parentPath, seg1].filter((x) => x !== null && x !== '').join('/');
      const lc = props.loadComponent?.v ?? props.component?.v ?? null;
      let component = null, importPath = null;
      if (props.component) component = props.component.v;
      if (props.loadComponent) {
        importPath = lc.match(/import\(\s*['"]([^'"]+)['"]/)?.[1] ?? null;
        const all = [...lc.matchAll(/=>\s*\w+\.(\w+)/g)];
        component = all.length ? all[all.length - 1][1] : null;
      }
      const dataV = props.data?.v ?? '';
      const menuId = dataV.match(/menuId\s*:\s*(?:\w+\.)?(\w+)/)?.[1] ?? null;
      const guards = ['canActivate', 'canActivateChild', 'canMatch', 'canDeactivate'].flatMap((k) =>
        props[k] ? [...props[k].v.replace(/^\[|\]$/g, '').split(',')].map((x) => x.trim()).filter(Boolean).map((g) => `${k}:${g}`) : []);
      const mp = menuId ? menuPerms[menuId] : undefined;
      const route = {
        file: relPath, array: arrayName,
        path: seg1, fullPath: '/' + full.replace(/\/{2,}/g, '/').replace(/^\/+/, ''),
        pathUnresolved: un || undefined,
        redirectTo: props.redirectTo ? resolveTsExpr(props.redirectTo.v, scope).value : undefined,
        component, importPath,
        lazyChildren: props.loadChildren ? props.loadChildren.v.slice(0, 120) : undefined,
        guards,
        menuId,
        menuPermissions: mp ? (mp.permissions ?? []) : undefined,
        menuPermissionsDeclared: mp ? mp.permissions !== undefined : undefined,
        line: lineOf(starts, abs),
        depth,
      };
      results.push(route);
      if (props.children && props.children.v.startsWith('[')) {
        const co = props.children.s + text.slice(props.children.s, props.children.e).search(/\[/);
        parseArray(co, full, arrayName, depth + 1);
      }
    }
  };
  for (const a of arrays) parseArray(a.open, '', a.name, 0);
  return { routes: results, unresolved };
}

export function scanFe(feRoot) {
  const appDir = path.join(feRoot, 'src', 'app');
  const tsFiles = walk(appDir, (p) => /\.ts$/.test(p) && !/\.spec\.ts$/.test(p));
  // permission codes
  const permFile = path.join(appDir, 'constants', 'permission.constant.ts');
  const permByKey = {};
  if (fs.existsSync(permFile)) for (const m of read(permFile).matchAll(/(\w+)\s*:\s*(['"])([^'"]+)\2/g)) permByKey[m[1]] = m[3];
  // menu permissions
  const menuPerms = {};
  for (const f of tsFiles.filter((p) => /menu\.constant\.ts$/.test(p))) Object.assign(menuPerms, parseMenuPermissions(read(f), permByKey));
  // routes
  const routeFiles = tsFiles.filter((p) => /\.routes\.ts$/.test(p));
  const cache = new Map();
  const routes = [];
  const unresolved = [];
  for (const f of routeFiles) {
    const text = read(f);
    const scope = buildTsScope(f, text, cache);
    const r = parseRoutesFile(f, text, scope, menuPerms, rel(feRoot, f));
    routes.push(...r.routes);
    unresolved.push(...r.unresolved);
  }
  const routerConstants = {};
  for (const f of tsFiles.filter((p) => /router\.constant\.ts$/.test(p))) routerConstants[rel(feRoot, f)] = parseEnumsAndConsts(read(f));

  // test ids
  const markupFiles = walk(appDir, (p) => /\.(html|ts)$/.test(p) && !/\.spec\.ts$/.test(p));
  const groups = {};
  const group = (relToApp) => {
    const parts = relToApp.split('/');
    if (parts[0] === 'features' && parts.length > 2) return `features/${parts[1]}`;
    if (parts[0] === 'app-garages' && parts[1] === 'features' && parts.length > 3) return `app-garages/features/${parts[2]}`;
    if (parts[0] === 'app-garages' && parts.length > 2) return `app-garages/${parts[1]}`;
    return parts.length > 1 ? parts[0] : '(root)';
  };
  for (const f of markupFiles) {
    const t = read(f);
    const testid = (t.match(/data-test-?id/gi) ?? []).length;
    const aria = (t.match(/aria-label/g) ?? []).length;
    const label = (t.match(/label-item/g) ?? []).length;
    if (!testid && !aria && !label && !f.endsWith('.html')) continue;
    const g = group(path.relative(appDir, f).split(path.sep).join('/'));
    groups[g] ??= { dataTestId: 0, ariaLabel: 0, labelItem: 0, htmlFiles: 0 };
    groups[g].dataTestId += testid;
    groups[g].ariaLabel += aria;
    groups[g].labelItem += label;
    if (f.endsWith('.html')) groups[g].htmlFiles++;
  }
  const tot = Object.values(groups).reduce((a, g) => ({ dataTestId: a.dataTestId + g.dataTestId, ariaLabel: a.ariaLabel + g.ariaLabel, labelItem: a.labelItem + g.labelItem, htmlFiles: a.htmlFiles + g.htmlFiles }), { dataTestId: 0, ariaLabel: 0, labelItem: 0, htmlFiles: 0 });
  const e2e = fs.existsSync(path.join(feRoot, 'playwright.config.ts'));
  return {
    routes: { routes, routerConstants, unresolvedPaths: unresolved, menuPermissionKeys: Object.keys(menuPerms).length, routeFiles: routeFiles.map((f) => rel(feRoot, f)) },
    testids: { totals: tot, byFolder: sortObj(groups), playwrightConfigPresent: e2e },
  };
}

/* ------------------------------------------------------------------ APP (Flutter) */

const snake = (s) => s.replace(/([a-z0-9])([A-Z])/g, '$1_$2').toLowerCase();

export function parseDartRouter(text, fileRel) {
  const masked = maskSource(text, 'dart');
  const starts = lineStarts(text);
  // hằng tên route: class X { static const String a = '/p'; }
  const consts = {};
  const classes = [...masked.matchAll(/\bclass\s+(\w+)/g)].map((m) => ({ name: m[1], idx: m.index }));
  for (const m of text.matchAll(/static\s+const\s+String\s+(\w+)\s*=\s*(['"])([^'"]*)\2/g)) {
    const cls = [...classes].reverse().find((c) => c.idx < m.index)?.name;
    if (cls) consts[`${cls}.${m[1]}`] = m[3];
  }
  const imports = [...text.matchAll(/import\s+'([^']+)'/g)].map((m) => m[1]);
  const routes = [];
  for (const m of masked.matchAll(/\bGoRoute\s*\(/g)) {
    const open = m.index + m[0].length - 1;
    const close = matchClose(masked, open);
    if (close < 0) continue;
    const props = {};
    for (const [s, e] of splitTop(masked, open + 1, close)) {
      const pm = masked.slice(s, e).match(/^\s*(\w+)\s*:/);
      if (pm) props[pm[1]] = text.slice(s + pm[0].length, e).trim();
    }
    routes.push({ idx: m.index, props });
  }
  return { consts, imports, routes, starts, fileRel };
}

export function resolveDartExpr(expr, consts) {
  const e = (expr ?? '').trim();
  const lit = e.match(/^(['"])([^'"]*)\1$/);
  if (lit) return lit[2];
  if (/^\w+\.\w+$/.test(e) && consts[e] !== undefined) return consts[e];
  return null;
}

export function pageClassOf(builder) {
  if (!builder) return null;
  const m = builder.match(/(?:return|=>)\s*(?:const\s+)?([A-Z]\w*)\s*\(/) ?? builder.match(/(?:const\s+)?\b([A-Z]\w*Page\w*)\s*\(/);
  return m ? m[1] : null;
}

export function scanApp(appRoot, ref) {
  const gitOk = ref && gitTry(appRoot, ['rev-parse', '--verify', '--quiet', ref]).trim();
  if (!gitOk) return { error: `ref ${ref} không có trong ${appRoot}`, routes: null, semantics: null };
  const listing = gitTry(appRoot, ['ls-tree', '-r', '--name-only', ref]).split('\n').filter(Boolean);
  const dartFiles = listing.filter((p) => /^lib\/.*\.dart$/.test(p));
  const show = (p) => git(appRoot, ['show', `${ref}:${p}`]);
  const routerFiles = listing.filter((p) => /^lib\/.*router.*\.dart$/i.test(p) && /router\//.test(p));
  const parsed = routerFiles.map((f) => parseDartRouter(show(f), f));
  const allConsts = Object.assign({}, ...parsed.map((p) => p.consts));
  const byBase = new Map(dartFiles.map((p) => [path.basename(p), p]));
  const routes = [];
  for (const p of parsed) {
    for (const r of p.routes) {
      const nameExpr = r.props.name ?? null;
      const pathExpr = r.props.path ?? null;
      const pageClass = pageClassOf(r.props.builder ?? r.props.pageBuilder);
      let pageFile = null;
      if (pageClass) {
        const want = `${snake(pageClass)}.dart`;
        const imp = p.imports.find((i) => i.endsWith('/' + want));
        if (imp) {
          const m = imp.match(/^package:[^/]+\/(.*)$/);
          pageFile = m ? `lib/${m[1]}` : imp;
        } else pageFile = byBase.get(want) ?? null;
      }
      routes.push({
        file: p.fileRel,
        line: lineOf(p.starts, r.idx),
        nameExpr, name: resolveDartExpr(nameExpr, allConsts),
        pathExpr, path: resolveDartExpr(pathExpr, allConsts),
        page: pageClass, pageFile,
        usesQueryParams: [...new Set([...(r.props.builder ?? '').matchAll(/queryParameters\[['"]([^'"]+)['"]\]/g)].map((x) => x[1]))],
        usesExtra: /state\.extra/.test(r.props.builder ?? ''),
        group: p.fileRel.split('/').slice(-2, -1)[0],
      });
    }
  }
  const routeConstants = Object.entries(allConsts).map(([k, v]) => ({ key: k, path: v }));
  const shell = parsed.reduce((n, p) => n + (p.routes.length ? 0 : 0), 0);

  // deep link
  const dlOut = gitTry(appRoot, ['grep', '-n', '-I', '-i', '-E', 'deep.?link|uni_links|app_links|getInitialLink|uriLinkStream|AppLinks\\(|handleDeepLink|onMessageOpenedApp|getInitialMessage', ref, '--', 'lib', 'pubspec.yaml', 'android/app/src/main/AndroidManifest.xml', 'ios/Runner/Info.plist']);
  const deepLinkHits = dlOut.split('\n').filter(Boolean).map((ln) => {
    const m = ln.match(new RegExp(`^${ref.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}:([^:]+):(\\d+):(.*)$`));
    return m ? { file: m[1], line: Number(m[2]), text: m[3].trim().slice(0, 200) } : null;
  }).filter(Boolean);
  const dlFiles = [...new Set(deepLinkHits.map((h) => h.file))].filter((f) => /\.dart$/.test(f));
  const destinations = [];
  for (const f of dlFiles) {
    const t = show(f);
    const names = new Set();
    for (const m of t.matchAll(/\b(\w+RouteNames\.\w+)\b/g)) names.add(m[1]);
    for (const m of t.matchAll(/(?:go|push|pushNamed|goNamed|pushReplacement)\(\s*['"](\/[^'"]*)['"]/g)) names.add(m[1]);
    destinations.push({ file: f, references: [...names].map((n) => ({ ref: n, path: n.startsWith('/') ? n : (allConsts[n] ?? null) })) });
  }
  const manifest = gitTry(appRoot, ['show', `${ref}:android/app/src/main/AndroidManifest.xml`]);
  const intentData = [...manifest.matchAll(/<data\b[^>]*android:(?:scheme|host|pathPrefix)[^>]*>/g)].map((m) => m[0].replace(/\s+/g, ' '));

  // semantics
  const modOf = (f) => {
    const m = f.match(/^lib\/modules\/([^/]+)\/([^/]+)\//);
    if (m) return `modules/${m[1]}/${m[2]}`;
    const m2 = f.match(/^lib\/([^/]+)/);
    return m2 ? `lib/${m2[1]}` : '(other)';
  };
  const patterns = {
    semantics: String.raw`\bSemantics\(`,
    identifier: String.raw`\bidentifier\s*:`,
    key: String.raw`\b(ValueKey|ObjectKey|Key)\(`,
    semanticsLabel: String.raw`\bsemanticsLabel\s*:`,
  };
  const perModule = {};
  const totals = {};
  for (const [k, re] of Object.entries(patterns)) {
    const out = gitTry(appRoot, ['grep', '-c', '-I', '-E', re, ref, '--', 'lib']);
    totals[k] = 0;
    for (const ln of out.split('\n').filter(Boolean)) {
      const m = ln.match(/^[^:]+:(lib\/[^:]+):(\d+)$/) ?? ln.match(/^(lib\/[^:]+):(\d+)$/);
      if (!m) continue;
      const mod = modOf(m[1]);
      perModule[mod] ??= { semantics: 0, identifier: 0, key: 0, semanticsLabel: 0, dartFiles: 0 };
      perModule[mod][k] += Number(m[2]);
      totals[k] += Number(m[2]);
    }
  }
  for (const f of dartFiles) { const mod = modOf(f); perModule[mod] ??= { semantics: 0, identifier: 0, key: 0, semanticsLabel: 0, dartFiles: 0 }; perModule[mod].dartFiles++; }

  return {
    ref,
    routes: { ref, routes, routeConstants, routerFiles, deepLinks: { hits: deepLinkHits, destinationsByFile: destinations, androidIntentData: intentData } },
    semantics: { ref, totals, dartFiles: dartFiles.length, byModule: sortObj(perModule), note: '`key` = Key(/ValueKey(/ObjectKey( (không tính GlobalKey); đếm theo dòng khớp, không theo số lần xuất hiện trong dòng' },
    _shell: shell,
  };
}

/* ------------------------------------------------------------------ jira keys */

export function collectJiraKeys(logText) {
  const keys = {};
  for (const ln of logText.split('\n')) {
    if (!ln) continue;
    const [date, ...rest] = ln.split('\t');
    const subject = rest.join('\t');
    const seen = new Set(subject.match(/\bCD-\d+\b/g) ?? []);
    for (const k of seen) {
      const e = (keys[k] ??= { count: 0, first: date, last: date, sample: subject.slice(0, 140) });
      e.count++;
      if (date < e.first) e.first = date;
      if (date > e.last) { e.last = date; }
    }
  }
  return keys;
}
export function mergeJira(perRepo) {
  const merged = {};
  for (const [repo, keys] of Object.entries(perRepo)) {
    for (const [k, v] of Object.entries(keys)) {
      const e = (merged[k] ??= { count: 0, first: v.first, last: v.last, sample: v.sample, repos: {} });
      e.count += v.count;
      if (v.first < e.first) e.first = v.first;
      if (v.last > e.last) e.last = v.last;
      e.repos[repo] = { count: v.count, first: v.first, last: v.last };
    }
  }
  return Object.fromEntries(Object.entries(merged).sort(([a], [b]) => Number(a.slice(3)) - Number(b.slice(3))));
}
function jiraForRepo(repo, ref) {
  const out = gitTry(repo, ['log', ref, '--format=%aI%x09%s']);
  return collectJiraKeys(out);
}

/* ------------------------------------------------------------------ main */

export function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) {
    const t = argv[i];
    if (t.startsWith('--')) {
      const k = t.slice(2);
      const v = argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[++i] : true;
      a[k] = v;
    }
  }
  return a;
}

export function run(opts) {
  const base = path.join(os.homedir(), 'Desktop/szit/AI/Projects/invlogis-dev');
  const be = opts.be || path.join(base, 'transport-erp');
  const fe = opts.fe || path.join(base, 'transport-erp-fe');
  const app = opts.app || path.join(base, 'driver-portal-flutter');
  const appRef = opts['app-ref'] || 'origin/tuanvv';
  const out = path.resolve(opts.out);
  const only = opts.only || null;
  if (only && !['be', 'fe', 'app'].includes(only)) throw new Error('--only phải là be|fe|app');
  const want = (x) => !only || only === x;
  const summaryPath = path.join(out, 'summary.json');
  let summary = {};
  try { summary = JSON.parse(read(summaryPath)); } catch { summary = {}; }
  summary.generatedAt = new Date().toISOString();
  summary.inputs = { ...(summary.inputs ?? {}), ...(want('be') ? { be } : {}), ...(want('fe') ? { fe } : {}), ...(want('app') ? { app, appRef } : {}) };
  const gaps = (summary.parsingGaps = summary.parsingGaps ?? {});
  const jira = {};
  fs.mkdirSync(out, { recursive: true });

  if (want('be')) {
    const perms = scanBePermissions(be);
    const permMap = new Map();
    for (const p of perms.items) { permMap.set(`${p.class}.${p.name}`, p); if (!permMap.has(p.name)) permMap.set(p.name, p); }
    const { endpoints, problems } = scanBeEndpoints(be, permMap);
    const unresolvedPerm = endpoints.flatMap((e) => e.permissions.filter((p) => p.ref && !p.code).map((p) => p.ref));
    writeJson(out, 'be-endpoints.json', { repo: be, count: endpoints.length, endpoints });
    writeJson(out, 'be-permissions.json', { repo: be, count: perms.items.length, unresolvedConstLines: perms.unresolved, permissions: perms.items });
    const acs = scanBeAcs(be);
    writeJson(out, 'be-acs.json', { repo: be, totals: acs.totals, acs: acs.acs, mentionOnly: acs.mentionOnly, testOnly: acs.testOnly });
    const db = scanBeDb(be);
    writeJson(out, 'be-db.json', { repo: be, contexts: db });
    const tests = scanBeTests(be);
    writeJson(out, 'be-tests.json', { repo: be, ...tests });
    const byMod = {};
    const byMethod = {};
    for (const e of endpoints) { bump(byMod, e.module); bump(byMethod, e.httpMethod); }
    summary.be = {
      endpoints: endpoints.length,
      endpointsByModule: sortObj(byMod),
      endpointsByMethod: sortObj(byMethod),
      endpointsWithoutPermission: endpoints.filter((e) => !e.permissions.length).length,
      endpointsAnonymous: endpoints.filter((e) => e.anonymous).length,
      permissionConstants: perms.items.filter((p) => p.kind === 'permission').length,
      acDefinedUnique: acs.totals.definedUnique,
      acMentionedInDocsUnique: acs.totals.mentionedInDocsUnique,
      acTraced: acs.totals.tracedByTests,
      acUntraced: acs.totals.untraced,
      acIdsInTestsNotInDocs: acs.totals.idsInTestsNotInDocs,
      dbContexts: db.length,
      dbEntities: db.reduce((s, c) => s + c.entities.length, 0),
      dbEntitiesWithTable: db.reduce((s, c) => s + c.entities.filter((e) => e.table).length, 0),
      testProjects: tests.totals.projects,
      testMethods: tests.totals.testMethods,
      testFacts: tests.totals.fact,
      testTheories: tests.totals.theory,
      traitUsages: tests.totals.traitUsages,
    };
    gaps.be = {
      permissionRefsUnresolved: [...new Set(unresolvedPerm)].slice(0, 30),
      permissionConstLinesNotLiteral: perms.unresolved,
      routeProblems: problems,
      note: 'Owned-entity (b1.*) cột không liệt kê, chỉ tên bảng ở ownedTables; HasPermission lấy từ attribute (không đọc policy động); operationId = {Controller}_{Action} theo tên method C# (giữ hậu tố Async).',
    };
    jira.be = jiraForRepo(be, 'HEAD');
  }
  if (want('fe')) {
    const r = scanFe(fe);
    writeJson(out, 'fe-routes.json', { repo: fe, count: r.routes.routes.filter((x) => !x.spread).length, ...r.routes });
    writeJson(out, 'fe-testids.json', { repo: fe, ...r.testids });
    summary.fe = {
      routes: r.routes.routes.filter((x) => !x.spread).length,
      routesWithMenuPermission: r.routes.routes.filter((x) => x.menuPermissions?.length).length,
      dataTestId: r.testids.totals.dataTestId,
      ariaLabel: r.testids.totals.ariaLabel,
      labelItem: r.testids.totals.labelItem,
      featureFolders: Object.keys(r.testids.byFolder).length,
    };
    gaps.fe = { unresolvedPathExpressions: r.routes.unresolvedPaths.length, spreads: r.routes.routes.filter((x) => x.spread).map((x) => x.spread), note: 'Route lồng qua loadChildren/spread không bung; route tạo động trong code không thấy.' };
    jira.fe = jiraForRepo(fe, 'HEAD');
  }
  if (want('app')) {
    const r = scanApp(app, appRef);
    if (r.error) { gaps.app = { error: r.error }; summary.app = { error: r.error }; }
    else {
      writeJson(out, 'app-routes.json', { repo: app, ...r.routes, count: r.routes.routes.length });
      writeJson(out, 'app-semantics.json', { repo: app, ...r.semantics });
      summary.app = {
        ref: appRef,
        routes: r.routes.routes.length,
        routesWithResolvedPath: r.routes.routes.filter((x) => x.path).length,
        deepLinkHits: r.routes.deepLinks.hits.length,
        dartFiles: r.semantics.dartFiles,
        semantics: r.semantics.totals.semantics,
        identifier: r.semantics.totals.identifier,
        key: r.semantics.totals.key,
        semanticsLabel: r.semantics.totals.semanticsLabel,
      };
      gaps.app = { routesUnresolvedPath: r.routes.routes.filter((x) => !x.path).length, note: 'Chỉ đọc file trong lib/**/router/; ShellRoute không bung; pageFile suy từ import theo tên snake_case.' };
    }
    jira.app = jiraForRepo(app, appRef);
  }
  if (Object.keys(jira).length) {
    const prev = (() => { try { return JSON.parse(read(path.join(out, 'jira-keys.json'))).perRepo ?? {}; } catch { return {}; } })();
    const perRepo = { ...prev, ...jira };
    const merged = mergeJira(perRepo);
    writeJson(out, 'jira-keys.json', { distinctKeys: Object.keys(merged).length, perRepo, keys: merged });
    summary.jira = { distinctKeys: Object.keys(merged).length, perRepo: Object.fromEntries(Object.entries(perRepo).map(([k, v]) => [k, Object.keys(v).length])) };
  }
  writeJson(out, 'summary.json', summary);
  return summary;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.out || args.out === true || args.help) {
    console.error('Dùng: node .claude/scripts/dev-scan.mjs --out <dir> [--only be|fe|app] [--be P] [--fe P] [--app P] [--app-ref origin/tuanvv]');
    process.exit(args.help ? 0 : 2);
  }
  const s = run(args);
  console.log(JSON.stringify(s, null, 2));
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
