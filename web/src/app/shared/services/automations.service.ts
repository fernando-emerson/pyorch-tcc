import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { Worker } from '../../core/models/worker.model';
import { Automation } from '../../core/models/automation.model';

@Injectable({
  providedIn: 'root',
})
export class AutomationsService {
  baseUrl = environment.apiUrl;

  private automationsSubject: BehaviorSubject<Automation[]> =
    new BehaviorSubject<Automation[]>([]);

  private automations$: Observable<Automation[]> =
    this.automationsSubject.asObservable();

  constructor(private http: HttpClient) {
    this.http
      .get<Automation[]>(`${this.baseUrl}/automations`)
      .subscribe((data) => {
        this.automationsSubject.next(data);
      });
  }

  getAutomations(): Observable<Automation[]> {
    return this.automations$;
  }

  createAutomation(form: any): Observable<any> {
    const headers = new HttpHeaders({ enctype: 'multipart/form-data' });
    return this.http
      .post<Automation>(`${this.baseUrl}/automations`, form, {
        headers: headers,
      })
      .pipe(
        tap((created) => {
          this.automationsSubject.next([
            ...this.automationsSubject.getValue(),
            created,
          ]);
        })
      );
  }

  deleteAutomation(id: number) {
    return this.http.delete<any>(`${this.baseUrl}/automations/${id}`).pipe(
      tap((_) => {
        const updated = this.automationsSubject
          .getValue()
          .filter((item) => item.id !== id);
        this.automationsSubject.next(updated);
      })
    );
  }

  getAutomationById(id: string) {
    return this.http.get<Automation>(`${this.baseUrl}/automations/${id}`);
  }

  updateAutomation(automation: Automation) {
    console.log(automation);
    return this.http
      .put<Automation>(`${this.baseUrl}/automations`, automation)
      .pipe(
        tap((updated) => {
          this.automationsSubject.next([
            ...this.automationsSubject.getValue(),
            updated,
          ]);
        })
      );
  }

  execute(id: number) {
    return this.http.post<any>(`${this.baseUrl}/automations/execute/${id}`, {});
  }
}
