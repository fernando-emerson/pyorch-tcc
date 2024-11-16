import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { Task } from '../../core/models/task.model';
import { DashboardStats } from '../../core/models/stat.model';

@Injectable({
  providedIn: 'root',
})
export class DashboardService {
  baseUrl = environment.apiUrl;

  private statsSubject: BehaviorSubject<DashboardStats> =
    new BehaviorSubject<DashboardStats>({
      triggered: 0,
      total_automations: 0,
      saved_hours: 0, // Use `number` para representar o Decimal em TypeScript
      average_time: 0, // Em segundos
      success: 0,
      waiting: 0,
      failures: 0,
      last_execution: undefined,
    });

  private stats$: Observable<DashboardStats> = this.statsSubject.asObservable();

  constructor(private http: HttpClient) {
    this.http
      .get<DashboardStats>(`${this.baseUrl}/dashboard/stats`)
      .subscribe((data) => {
        this.statsSubject.next(data);
      });
  }

  getStats(): Observable<DashboardStats> {
    return this.stats$;
  }
}
