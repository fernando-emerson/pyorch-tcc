import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { Task } from '../../core/models/task.model';
import { Log } from '../../core/models/log.model';

@Injectable({
  providedIn: 'root',
})
export class LogsService {
  baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getLogs(): Observable<Log[]> {
    return this.http.get<Log[]>(`${this.baseUrl}/logs/file`);
  }
}
