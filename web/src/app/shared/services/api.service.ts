import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Worker } from '../../core/models/worker.model';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getWorkers(): Observable<Worker[]> {
    return this.http.get<Worker[]>(`${this.baseUrl}/workers`);
  }
}
