// Helper cho ng-zorro-antd 19 (FE Invlogis). Selector đã đối chiếu mã nguồn FE:
// - loading: LoadingService mở overlay CDK chứa <nz-spin> (components/loading)
// - toast: ToastService dùng NzMessage, nội dung có role="status" (thành công) / role="alert" (lỗi)
// - confirm: openConfirmModal (components/confirm-modal) — nút mặc định `nz-button` trong .ant-modal
import { expect, type Locator, type Page } from '@playwright/test';

/** Chờ overlay loading toàn cục biến mất. */
export async function waitForGlobalLoading(page: Page, timeout = 30_000): Promise<void> {
  const spin = page.locator('.cdk-overlay-container nz-spin, .cdk-overlay-container .ant-spin');
  await spin.first().waitFor({ state: 'detached', timeout }).catch(() => {});
}

/** Mở nz-select (theo locator của nó), chọn option theo text trong overlay. */
export async function selectOption(page: Page, select: Locator, optionText: string | RegExp): Promise<void> {
  await select.click();
  const opt = page.locator('.cdk-overlay-container .ant-select-item-option').filter({ hasText: optionText }).first();
  await opt.waitFor({ state: 'visible' });
  await opt.click();
}

/** Chọn ngày trong nz-date-picker: gõ vào input rồi Enter (định dạng theo FE, mặc định dd/MM/yyyy). */
export async function pickDate(page: Page, picker: Locator, value: string): Promise<void> {
  const input = picker.locator('input').first();
  await input.click();
  await input.fill(value);
  await input.press('Enter');
  await page.locator('.cdk-overlay-container .ant-picker-dropdown').first().waitFor({ state: 'hidden' }).catch(() => {});
}

/** Dòng bảng nz-table chứa text. */
export function tableRow(page: Page, rowText: string | RegExp): Locator {
  return page.locator('nz-table tbody tr, .ant-table-tbody tr').filter({ hasText: rowText }).first();
}

/** Bấm nút/hành động trong dòng bảng theo tên hiển thị hoặc aria-label. */
export async function rowAction(page: Page, rowText: string | RegExp, action: string | RegExp): Promise<void> {
  const row = tableRow(page, rowText);
  await row.waitFor({ state: 'visible' });
  const btn = row.getByRole('button', { name: action }).first();
  if (await btn.count()) await btn.click();
  else await row.getByText(action).first().click();
}

/** Xác nhận modal (openConfirmModal / nz-modal): bấm nút primary cuối cùng trong modal đang mở. */
export async function confirmModal(page: Page, okText?: string | RegExp): Promise<void> {
  const modal = page.locator('.ant-modal-wrap:visible .ant-modal, .ant-modal-confirm').last();
  await modal.waitFor({ state: 'visible' });
  const ok = okText ? modal.getByRole('button', { name: okText }) : modal.locator('button').last();
  await ok.click();
  await modal.waitFor({ state: 'hidden' }).catch(() => {});
}

/** Kiểm toast: kind 'success' -> role=status, 'error' -> role=alert. */
export async function expectToast(page: Page, kind: 'success' | 'error', text?: string | RegExp): Promise<void> {
  const role = kind === 'success' ? 'status' : 'alert';
  let toast = page.locator('.ant-message').getByRole(role);
  if (text) toast = toast.filter({ hasText: text });
  await expect(toast.first()).toBeVisible();
}
