// Component nào thật sự đặt instance của Misc icons, Phương tiện (DEC-337). CHỈ ĐỌC.
// Chạy bằng use_figma, mỗi page một lần gọi: PAGE_ID = DS · Base components 6650:339720, DS · Application components 6766:190506.
// Gộp kết quả vào design-system/components/_figma-uses.json (khoá uses: tên component trên Figma → mã foundation).
const PAGE_ID = '6650:339720';
const SETS = {
  'misc-icon': /^(Featured icon|File type icon|Flag|Bank logo|App logo|QR code|Payment \/|Social \/|_Dot|_Play overlay|Store badge)/i,
  vehicle: /^(Vehicle Image|Tyre Slot|Tyre Layout|Map Marker)/i,
};
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const uses = {}, cache = new Map();
const instances = page.findAllWithCriteria({ types: ['INSTANCE'] });
for (const i of instances) {
  const m = await i.getMainComponentAsync();
  if (!m) continue;
  if (!cache.has(m.id)) {
    const root = m.parent && m.parent.type === 'COMPONENT_SET' ? m.parent.name : m.name;
    cache.set(m.id, Object.keys(SETS).find(k => SETS[k].test(root)) || null);
  }
  const key = cache.get(m.id);
  if (!key) continue;
  let owner = null;
  for (let o = i.parent; o && o.type !== 'PAGE'; o = o.parent)
    if (o.type === 'COMPONENT_SET' || (o.type === 'COMPONENT' && o.parent.type !== 'COMPONENT_SET')) owner = o;
  if (owner) (uses[owner.name] = uses[owner.name] || {})[key] = 1;
}
return { page: page.name, instances: instances.length, uses };
