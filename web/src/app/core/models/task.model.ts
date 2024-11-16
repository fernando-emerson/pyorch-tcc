import { Automation } from './automation.model';

export interface Task {
  id?: number;
  task_id?: string;
  automation?: Automation;
  automation_id: number;
  started_at: Date;
  finished_at: Date;
  status: string;
  message: string;
  priority: string;
  progress: number;
  result?: string;
}
