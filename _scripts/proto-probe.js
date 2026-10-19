/* proto-probe.js — đo style thật của 1 màn prototype HTML (/figma-proto-check).
 *
 * proto-figma-diff.py chèn file này vào cuối bản sao prototype rồi mở bằng Chrome headless
 * (--dump-dom). Kết quả ghi vào thẻ pre#__probe dạng JSON, cùng khuôn với
 * .claude/skills/figma-proto-check/references/figma-probe.js để script so được hai bên.
 *
 * Vào thẳng state: prototype tự đọc `#slug?state=<tên>&device=web|app` (quy ước /prototype-html,
 * PROTO_STATES). Probe chỉ gọi dự phòng khi router chưa xử lý.
 */
(function () {
  var WAIT = 1800;

  function parseHash() {
    var h = location.hash.slice(1), q = '', i = h.indexOf('?');
    if (i >= 0) { q = h.slice(i + 1); h = h.slice(0, i); }
    var p = {};
    q.split('&').forEach(function (kv) { if (!kv) return; var a = kv.split('='); p[decodeURIComponent(a[0])] = decodeURIComponent(a[1] || ''); });
    return { slug: h, state: p.state || '', device: p.device || '' };
  }

  function hex(c) {
    var m = /rgba?\(([^)]+)\)/.exec(c || ''); if (!m) return null;
    var v = m[1].split(',').map(function (s) { return parseFloat(s); });
    if (v.length > 3 && v[3] === 0) return null;
    var h2 = function (n) { return ('0' + Math.round(n).toString(16)).slice(-2); };
    return '#' + v.slice(0, 3).map(h2).join('') + (v.length > 3 && v[3] < 0.999 ? h2(v[3] * 255) : '');
  }

  function px(v, fs) {
    if (v === 'normal') return Math.round(fs * 1.2 * 10) / 10;
    var n = parseFloat(v); return isNaN(n) ? null : n;
  }

  function visible(el) {
    var cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return false;
    var r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0;
  }

  function role(el) {
    var t = el.tagName.toLowerCase(), ty = (el.getAttribute('type') || '').toLowerCase();
    if (t === 'input' && (ty === 'checkbox' || ty === 'radio')) return ty;
    if (t === 'input' || t === 'textarea' || t === 'select') return 'input';
    if (t === 'button' || el.getAttribute('role') === 'button') return /\blink\b/.test(el.className) ? 'link' : 'button';
    if (t === 'a') return 'link';
    if (t === 'svg') return 'icon';
    if (t === 'img') return 'image';
    return 'box';
  }

  function shadowOf(v) {
    // "rgba(0, 0, 0, 0.1) 0px 1px 2px 0px, …" → lớp đầu: [màu, x, y, blur, spread]; bỏ inset (viền giả)
    if (!v || v === 'none') return null;
    var layers = v.split(/,(?![^(]*\))/).map(function (s) { return s.trim(); }).filter(function (s) { return s.indexOf('inset') < 0; });
    if (!layers.length) return null;
    var m = /(rgba?\([^)]+\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+([\d.]+)px(?:\s+(-?[\d.]+)px)?/.exec(layers[0]);
    if (!m) return null;
    var c = hex(m[1]); if (!c) return null;
    return [c, parseFloat(m[2]), parseFloat(m[3]), parseFloat(m[4]), parseFloat(m[5] || 0)];
  }

  function iconName(el) {
    var u = el.querySelector('use'); var h = u && (u.getAttribute('href') || u.getAttribute('xlink:href')) || '';
    return h.replace(/^#/, '').replace(/^ic-/, '') || (el.getAttribute('data-icon') || '');
  }

  function run() {
    var want = parseHash();
    var root = document.querySelector('[data-screen].active');
    if (!root && want.slug) root = document.querySelector('[data-screen="' + want.slug + '"]');
    var out = { side: 'proto', slug: want.slug, state: want.state, device: want.device, warnings: [], nodes: [] };
    if (!root) { out.warnings.push('Không thấy màn đang hiện cho #' + want.slug); return out; }
    if (want.state && document.documentElement.dataset.protoState !== want.state)
      out.warnings.push('Prototype chưa báo đã vào state "' + want.state + '" (thiếu PROTO_STATES hoặc router chưa đọc ?state=) — số đo có thể là state mặc định');

    var R = root.getBoundingClientRect();
    out.root = { x: Math.round(R.left), y: Math.round(R.top), w: Math.round(R.width), h: Math.round(R.height), dpr: window.devicePixelRatio || 1 };
    var idx = 0;
    var all = [root].concat([].slice.call(root.querySelectorAll('*')));
    // Toast nằm ngoài khung màn (lớp .toast-host của app) — vẫn đo, toạ độ theo khung màn như Figma.
    [].forEach.call(document.querySelectorAll('.toast-host'), function (h) { if (!root.contains(h)) all = all.concat([h], [].slice.call(h.querySelectorAll('*'))); });
    all.forEach(function (el) {
      if (!visible(el)) return;
      if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') return;   // chỉ đo icon ở thẻ svg ngoài cùng
      var cs = getComputedStyle(el), r = el.getBoundingClientRect(), rl = role(el);
      var rect = { x: Math.round(r.left - R.left), y: Math.round(r.top - R.top), w: Math.round(r.width), h: Math.round(r.height) };
      var parentEl = el.parentElement && el.parentElement.closest('[data-probe-id]');
      var parentId = parentEl ? parentEl.getAttribute('data-probe-id') : null;

      // Khung: có nền/viền, là control, hoặc là khung bố cục có padding / flex / grid (để đo gap).
      var bg = hex(cs.backgroundColor);
      var bw = parseFloat(cs.borderTopWidth) || 0;
      var hasPad = ['Top', 'Right', 'Bottom', 'Left'].some(function (k) { return parseFloat(cs['padding' + k]) > 0; });
      var isBox = el === root || rl !== 'box' || bg || bw > 0 || hasPad || cs.display.indexOf('flex') >= 0 || cs.display.indexOf('grid') >= 0;
      var id = null;
      if (isBox) {
        id = 'p' + (idx++);
        el.setAttribute('data-probe-id', id);
        out.nodes.push({
          id: id, parent: parentId, kind: 'box', role: rl,
          tag: el.tagName.toLowerCase(), cls: String(el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className || '').slice(0, 60),
          rect: rect, fill: bg, stroke: bw > 0 ? hex(cs.borderTopColor) : null, strokeWidth: bw,
          radius: parseFloat(cs.borderTopLeftRadius) || 0,
          padding: [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(function (v) { return parseFloat(v) || 0; }),
          gap: cs.display.indexOf('flex') >= 0 || cs.display.indexOf('grid') >= 0 ? (parseFloat(cs.rowGap) || parseFloat(cs.columnGap) || 0) : null,
          direction: cs.display.indexOf('flex') >= 0 ? (cs.flexDirection.indexOf('column') === 0 ? 'VERTICAL' : 'HORIZONTAL') : null,
          label: (el.getAttribute('aria-label') || '').slice(0, 40),
          shadow: shadowOf(cs.boxShadow),
          icon: rl === 'icon' ? iconName(el) : undefined,
          iconColor: rl === 'icon' ? hex(cs.stroke && cs.stroke !== 'none' ? cs.stroke : cs.color) : undefined
        });
      }

      // Chữ: text node con trực tiếp, đo bằng Range cho sát chữ (giống TEXT node của Figma).
      var own = [].filter.call(el.childNodes, function (n) { return n.nodeType === 3 && n.textContent.trim(); });
      var txt = own.map(function (n) { return n.textContent.trim(); }).join(' ').replace(/\s+/g, ' ');
      var masked = rl === 'input' && (el.getAttribute('type') || '').toLowerCase() === 'password' && el.value;
      if (rl === 'input' && !txt) txt = masked ? new Array(el.value.length + 1).join('•') : (el.value || el.getAttribute('placeholder') || '').trim();
      if (txt) {
        var tr = rect;
        if (rl === 'input') {
          // Ô nhập không có text node: lấy vùng nội dung (trừ padding + viền), dòng chữ canh giữa theo chiều cao.
          var pl = parseFloat(cs.paddingLeft) + (parseFloat(cs.borderLeftWidth) || 0);
          var pr = parseFloat(cs.paddingRight) + (parseFloat(cs.borderRightWidth) || 0);
          var lhIn = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.43;
          tr = { x: rect.x + Math.round(pl), y: rect.y + Math.round((rect.h - lhIn) / 2), w: Math.max(0, rect.w - Math.round(pl + pr)), h: Math.round(lhIn) };
        }
        if (own.length) {
          var rg = document.createRange(); rg.setStartBefore(own[0]); rg.setEndAfter(own[own.length - 1]);
          var b = rg.getBoundingClientRect(); tr = { x: Math.round(b.left - R.left), y: Math.round(b.top - R.top), w: Math.round(b.width), h: Math.round(b.height) };
        }
        var fs = parseFloat(cs.fontSize);
        out.nodes.push({
          id: 't' + (idx++), parent: id || parentId, kind: 'text', text: txt, rect: tr, tag: el.tagName.toLowerCase(),
          placeholder: rl === 'input' && !el.value,
          font: (cs.fontFamily.split(',')[0] || '').replace(/["']/g, '').trim(),
          size: fs, weight: parseInt(cs.fontWeight, 10), lineHeight: px(cs.lineHeight, fs),
          letterSpacing: cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing),
          color: hex(rl === 'input' && !el.value ? getComputedStyle(el, '::placeholder').color : cs.color),
          decoration: cs.textDecorationLine.indexOf('underline') >= 0 ? 'UNDERLINE' : (cs.textDecorationLine.indexOf('line-through') >= 0 ? 'STRIKETHROUGH' : 'NONE'),
          upper: cs.textTransform === 'uppercase'
        });
      }
    });
    return out;
  }

  function hideChrome() {
    // Giấu vỏ prototype (thanh góp ý, FAB, panel mô phỏng) để ảnh chụp chỉ còn màn.
    var stage = document.querySelector('[data-screen].active');
    [].forEach.call(document.body.children, function (c) {
      if (c.id === '__probe') return;
      if (!stage || !c.contains(stage)) c.style.setProperty('visibility', 'hidden', 'important');
    });
    document.querySelectorAll('[class*="cmt-"], .proto-fab, .proto-panel').forEach(function (n) {
      if (!stage || !n.contains(stage)) n.style.setProperty('visibility', 'hidden', 'important');
    });
  }

  function fallbackState(w) {
    if (!w.state || document.documentElement.dataset.protoState === w.state) return;
    try {
      var reg = window.PROTO_STATES && window.PROTO_STATES[w.slug];
      if (reg && typeof reg[w.state] === 'function') { reg[w.state](); document.documentElement.dataset.protoState = w.state; }
    } catch (e) { /* ghi cảnh báo ở run() */ }
  }

  window.addEventListener('load', function () {
    setTimeout(function () {
      fallbackState(parseHash());
      setTimeout(function () {
        hideChrome();
        var pre = document.createElement('pre'); pre.id = '__probe'; pre.style.display = 'none';
        try { pre.textContent = JSON.stringify(run()); } catch (e) { pre.textContent = JSON.stringify({ side: 'proto', error: String(e) }); }
        document.body.appendChild(pre);
      }, 400);
    }, WAIT);
  });
})();
