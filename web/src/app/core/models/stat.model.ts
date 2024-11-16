export interface DashboardStats {
  triggered: number;
  total_automations: number;
  saved_hours: number; // Use `number` para representar o Decimal em TypeScript
  average_time: number; // Em segundos
  success: number;
  waiting: number;
  failures: number;
  last_execution?: Date;
}
