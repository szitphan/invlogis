// Kiểm tên node Figma theo luật đặt tên component (DEC-264, design-system/_review/agent-brief-base.md §2d).
// Cách chạy: đọc file này, thay ROOTS bằng id Section của component vừa dựng, dán làm `code` cho
// reqwise figma_write. Chỉ đọc, không sửa gì. Kết quả: { fail: [...], pass } — fail ≠ 0 thì sửa rồi chạy lại.
const ROOTS = ['<sectionId>'];
// Tuỳ chọn (DEC-329 ic15): dán tên icon từ design-system/handoff/icons.json (meanings[].icon) để báo instance icon ngoài bảng nghĩa.
const ICON_MEANINGS = [];

const MAX = { set: 32, section: 32, frame: 40, text: 24, prop: 20, value: 16 };
const ROLE = /^(Title|Subtitle|Group title|Label|Row label|Col label|Description|Value|Caption|Helper|Hint|Note|Text|Placeholder|Error message|Code|Name|Route|Vehicle|Driver|Time|Count)\b/;
const fail = [];
const bad = (n, rule, hint) => fail.push({ id: n.id, type: n.type, name: n.name.slice(0, 80), rule, hint });

async function walk(id, inComponent) {
  const kids = await figma.getChildren(id);
  for (const n of kids) {
    const name = n.name;
    if (n.type === 'COMPONENT_SET' || (n.type === 'COMPONENT' && !/=/.test(name))) {
      if (name.length > MAX.set) bad(n, `component > ${MAX.set}`, 'tên Untitled tiếng Anh, phần con tiền tố _');
    } else if (n.type === 'COMPONENT' && /=/.test(name)) {
      for (const pair of name.split(',')) {
        const [k, v] = pair.split('=').map(s => s.trim());
        if (k.length > MAX.prop) bad(n, `thuộc tính "${k}" > ${MAX.prop}`, 'rút tên thuộc tính');
        if (v && v.length > MAX.value) bad(n, `giá trị "${v}" > ${MAX.value}`, 'rút giá trị (hỏi user: đổi giá trị đụng instance)');
      }
    } else if (n.type === 'SECTION') {
      if (name.length > MAX.section) bad(n, `section > ${MAX.section}`, 'chỉ tên mục');
    } else if (n.type === 'FRAME' || n.type === 'GROUP') {
      if (name.length > MAX.frame) bad(n, `khung > ${MAX.frame}`, 'rút gọn; không ghi mã, không giải thích');
      if (/\bdemo \//i.test(name) || /\/ (Web|Mobile) (1440|393)\b/.test(name)) bad(n, 'khung demo lặp tên component / cỡ', '"<Màn> / Web|Mobile[ / <Trạng thái>]"');
    } else if (n.type === 'TEXT') {
      const byContent = n.characters && name === n.characters;
      if (name.length > MAX.text) bad(n, `layer chữ > ${MAX.text}`, 'đặt theo vai trò: Title, Subtitle, Label, Value, Note…');
      else if (byContent && !ROLE.test(name) && name.length > 12) bad(n, 'layer chữ lấy nội dung làm tên', 'đặt theo vai trò');
    }
    if (ICON_MEANINGS.length && n.type === 'INSTANCE' && /^icon\//.test(name) && !ICON_MEANINGS.includes(name.slice(5))) bad(n, 'icon ngoài bảng nghĩa', 'tra design-system/foundations/icon.md mục 7');
    if (/DEC-\d+|\d+:\d+/.test(name)) bad(n, 'tên chứa mã DEC / mã node', 'chuyển vào description');
    if (n.childCount && n.type !== 'INSTANCE') await walk(n.id, inComponent || n.type === 'COMPONENT');
  }
}
for (const r of ROOTS) await walk(r, false);
return { fail: fail.length, list: fail.slice(0, 200) };
