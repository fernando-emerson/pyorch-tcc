import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { Worker } from '../../core/models/worker.model';

@Injectable({
  providedIn: 'root',
})
export class WorkersService {
  baseUrl = environment.apiUrl;

  private workersSubject: BehaviorSubject<Worker[]> = new BehaviorSubject<
    Worker[]
  >([]);
  private workers$: Observable<Worker[]> = this.workersSubject.asObservable();

  constructor(private http: HttpClient) {
    this.http.get<Worker[]>(`${this.baseUrl}/workers`).subscribe((data) => {
      this.workersSubject.next(data);
    });
  }

  getWorkers(): Observable<Worker[]> {
    return this.workers$;
  }
}
