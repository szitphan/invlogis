// Đăng nhập BE 3 bước theo từng vai, ghi storageState có khoá localStorage của FE.
// Nguồn: transport-erp/bruno/00-auth/*, transport-erp-fe features/login/login.component.ts,
// services/auth.service.ts, features/home/home.component.ts, constants/storage.constant.ts.
import { readFileSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
export const QA_ROOT = resolve(here, '../..');

// Khoá localStorage của FE (StorageKey)
export const StorageKey = {
  ACCESS_TOKEN: 'access_token',
  REFRESH_TOKEN: 'refresh_token',
  DEVICE_IDENTIFIER: 'device_identifier',
  CURRENT_MODULE_CODE: 'current_module_code',
  CURRENT_FACILITY_CONTEXT: 'current_facility_context',
  WORKING_CONTEXT_ID: 'working_context_id',
  CURRENT_WORKING_ORGANIZATION_UNIT_ID: 'current_working_organization_unit_id',
} as const;

export interface EnvConfig {
  apiBase: string;
  webBase: string;
  tenantIdEnv: string;
  webBaseEnv?: string;
}
export interface RoleConfig {
  channel: 'Web' | 'Mobile';
  audience: 'Internal' | 'Partner';
  userEnv: string;
  passEnv: string;
  orgUnitEnv?: string;
  facilityEnv?: string;
}

export function loadEnvFile(): void {
  const p = resolve(QA_ROOT, '.env');
  if (!existsSync(p)) return;
  for (const line of readFileSync(p, 'utf8').split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && process.env[m[1]] === undefined) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
  }
}

export function getEnv(name = process.env.QA_ENV || 'dev'): { name: string; cfg: EnvConfig; tenantId: string; webBase: string } {
  loadEnvFile();
  if (name === 'prod' || name === 'production') throw new Error('QA không được chạy trên prod.');
  const all = JSON.parse(readFileSync(resolve(QA_ROOT, 'config/envs.json'), 'utf8'));
  const cfg: EnvConfig = all[name];
  if (!cfg) throw new Error(`Môi trường "${name}" không có trong config/envs.json`);
  const tenantId = process.env[cfg.tenantIdEnv] || '';
  if (!tenantId) throw new Error(`Thiếu biến môi trường ${cfg.tenantIdEnv}`);
  const webBase = (cfg.webBaseEnv && process.env[cfg.webBaseEnv]) || cfg.webBase;
  return { name, cfg, tenantId, webBase };
}

export function getRole(slug: string): RoleConfig {
  const roles = JSON.parse(readFileSync(resolve(QA_ROOT, 'config/roles.json'), 'utf8'));
  const r = roles[slug];
  if (!r || slug.startsWith('_')) throw new Error(`Vai "${slug}" không có trong config/roles.json`);
  return r;
}

export function storageStatePath(envName: string, role: string): string {
  return resolve(QA_ROOT, '.auth', `${envName}-${role}.json`);
}

async function post(url: string, headers: Record<string, string>, body: unknown): Promise<any> {
  const res = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: JSON.stringify(body) });
  const json: any = await res.json().catch(() => ({}));
  if (!res.ok || json?.isSuccess === false) {
    throw new Error(`POST ${url} -> ${res.status} ${JSON.stringify(json).slice(0, 300)}`);
  }
  return json?.data ?? json;
}

export interface LoginResult {
  accessToken: string;
  refreshToken: string;
  workingOrganizationUnitId?: string;
  workingContextId?: string;
  facilityId?: string;
}

/** Đăng nhập 3 bước. Bước 2 chỉ chạy khi nextStep=WorkingContextSelectionRequired; bước 3 chỉ khi có facility. */
export async function loginRole(roleSlug: string, envName?: string): Promise<LoginResult & { env: string; tenantId: string }> {
  const { name, cfg, tenantId } = getEnv(envName);
  const role = getRole(roleSlug);
  const user = process.env[role.userEnv];
  const pass = process.env[role.passEnv];
  if (!user || !pass) throw new Error(`Thiếu ${role.userEnv} / ${role.passEnv} trong qa/.env`);
  const idn = `${cfg.apiBase.replace(/\/+$/, '')}/api/identity/v1`;
  const base = { 'X-Tenant-Id': tenantId };
  const deviceIdentifier = `qa-${roleSlug}`;

  // Bước 1: login
  const l1 = await post(`${idn}/auth/login`, base, {
    username: user,
    password: pass,
    deviceIdentifier,
    deviceName: 'QA Playwright',
    platform: role.channel === 'Mobile' ? 'android' : 'web',
    channel: role.channel.toLowerCase(), // FE AccessChannel: 'web' | 'mobile'
    appVersion: '',
    rememberMe: false,
  });

  let accessToken: string = l1.accessToken;
  let refreshToken: string = l1.refreshToken;
  let ouId: string | undefined = l1.currentContext?.workingOrganizationUnitId;

  // Bước 2: chọn đơn vị làm việc
  if (String(l1.nextStep).toLowerCase() === 'workingcontextselectionrequired') {
    const options: any[] = l1.workingContextOptions ?? [];
    const wanted = role.orgUnitEnv ? process.env[role.orgUnitEnv] : undefined;
    const opt = (wanted && options.find((o) => String(o.workingOrganizationUnitId) === wanted)) || options[0];
    if (!l1.continuationToken || !opt) throw new Error('Login yêu cầu chọn đơn vị nhưng không có continuationToken/workingContextOptions');
    const l2 = await post(`${idn}/auth/working-organization-unit`, base, {
      temporaryToken: l1.continuationToken,
      workingOrganizationUnitId: String(opt.workingOrganizationUnitId),
    });
    accessToken = l2.accessToken;
    refreshToken = l2.refreshToken;
    ouId = l2.currentContext?.workingOrganizationUnitId ?? String(opt.workingOrganizationUnitId);
  } else if (l1.nextStep && String(l1.nextStep).toLowerCase() !== 'authenticated') {
    throw new Error(`nextStep không hỗ trợ: ${l1.nextStep}`);
  }
  if (!accessToken) throw new Error('Không nhận được accessToken');

  // Bước 3: working context theo facility (để có X-Working-Context-Id)
  let workingContextId: string | undefined;
  const facilityId = role.facilityEnv ? process.env[role.facilityEnv] : undefined;
  if (facilityId) {
    const l3 = await post(
      `${idn}/working-contexts/facility`,
      { ...base, Authorization: `Bearer ${accessToken}` },
      { moduleCode: process.env.QA_MODULE_CODE || 'fuel', facilityId },
    );
    workingContextId = l3.workingContextId;
  }
  return { accessToken, refreshToken, workingOrganizationUnitId: ouId, workingContextId, facilityId, env: name, tenantId };
}

/** Đăng nhập rồi ghi storageState (origin = webBase) trả về đường dẫn file. */
export async function createStorageState(roleSlug: string, envName?: string): Promise<string> {
  const { name, webBase } = getEnv(envName);
  if (!webBase) throw new Error('Chưa có webBase: đặt QA_WEB_BASE trong qa/.env hoặc config/envs.json');
  const r = await loginRole(roleSlug, name);
  const ls: { name: string; value: string }[] = [
    { name: StorageKey.ACCESS_TOKEN, value: r.accessToken },
    { name: StorageKey.REFRESH_TOKEN, value: r.refreshToken },
    { name: StorageKey.DEVICE_IDENTIFIER, value: `qa-${roleSlug}` },
    { name: StorageKey.CURRENT_MODULE_CODE, value: process.env.QA_MODULE_CODE || 'fuel' },
  ];
  if (r.workingOrganizationUnitId) ls.push({ name: StorageKey.CURRENT_WORKING_ORGANIZATION_UNIT_ID, value: r.workingOrganizationUnitId });
  if (r.workingContextId && r.facilityId) {
    ls.push({ name: StorageKey.WORKING_CONTEXT_ID, value: r.workingContextId });
    // Khớp CurrentFacilityContextModel (utils/facility-context.util.ts)
    ls.push({
      name: StorageKey.CURRENT_FACILITY_CONTEXT,
      value: JSON.stringify({ selectionType: 'selected', facilityCount: 1, executionFacilityId: r.facilityId }),
    });
  }
  const state = { cookies: [], origins: [{ origin: new URL(webBase).origin, localStorage: ls }] };
  const file = storageStatePath(name, roleSlug);
  mkdirSync(dirname(file), { recursive: true });
  writeFileSync(file, JSON.stringify(state, null, 2));
  return file;
}
