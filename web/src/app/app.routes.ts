import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AutomationsComponent } from './pages/automations/automations.component';
import { AutomationFormComponent } from './pages/automations/components/automation-form/automation-form.component';
import { TasksComponent } from './pages/tasks/tasks.component';
import { WorkersComponent } from './pages/workers/workers.component';
import { LogsComponent } from './pages/logs/logs.component';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  {
    path: 'automacoes',
    children: [
      { path: '', component: AutomationsComponent },
      { path: 'cadastrar', component: AutomationFormComponent },
      { path: 'editar/:id', component: AutomationFormComponent },
    ],
  },
  { path: 'tasks', component: TasksComponent },
  { path: 'workers', component: WorkersComponent },
  { path: 'logs', component: LogsComponent },
];
