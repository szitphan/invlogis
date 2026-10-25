// Chặn assets/runtime-config.js của FE để trỏ API về môi trường đang test.
// FE đọc window.__TRANSPORT_ERP_CONFIG__ { apiUrl, notificationSocketUrl, processesSocketUrl }
// (transport-erp-fe/src/index.html nạp assets/runtime-config.js trước app).
import type { Page } from '@playwright/test';

export async function injectRuntimeConfig(page: Page, apiBase: string): Promise<void> {
  const base = apiBase.replace(/\/+$/, '');
  const body =
    'window.__TRANSPORT_ERP_CONFIG__ = ' +
    JSON.stringify({
      apiUrl: `${base}/api/`,
      notificationSocketUrl: `${base}/hubs/notifications`,
      processesSocketUrl: `${base}/hubs/processes`,
    }) +
    ';';
  await page.route('**/assets/runtime-config.js', (route) =>
    route.fulfill({ status: 200, contentType: 'application/javascript', body }),
  );
}
