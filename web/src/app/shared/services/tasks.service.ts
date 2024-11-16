import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { Task } from '../../core/models/task.model';

@Injectable({
  providedIn: 'root',
})
export class TasksService {
  baseUrl = environment.apiUrl;

  private tasksSubject: BehaviorSubject<Task[]> = new BehaviorSubject<Task[]>(
    []
  );

  private tasks$: Observable<Task[]> = this.tasksSubject.asObservable();

  constructor(private http: HttpClient) {
    this.http.get<Task[]>(`${this.baseUrl}/tasks`).subscribe((data) => {
      this.tasksSubject.next(data);
    });
  }

  getTasks(): Observable<Task[]> {
    return this.tasks$;
  }
}
