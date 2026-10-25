import { RouterPath } from './constants/router.constant';
export const routes: Routes = [
  { path: RouterPath.HOME, loadComponent: () => import('./features/home/home.component').then((c) => c.HomeComponent) },
  {
    path: `${RouterPath.ALPHA}/:id`,
    canActivate: [guard],
    loadComponent: () => import('./features/alpha/alpha.component').then((c) => c.AlphaComponent),
    data: { menuId: MenuId.ALPHA },
    children: [{ path: 'child', component: ChildComponent }],
  },
];
