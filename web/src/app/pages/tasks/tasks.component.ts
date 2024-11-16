import { NgClass } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { BreadcrumbComponent } from '../../shared/breadcrumb/breadcrumb.component';
import { TasksService } from '../../shared/services/tasks.service';
import { Task } from '../../core/models/task.model';

@Component({
  selector: 'app-tasks',
  standalone: true,
  imports: [NgClass, BreadcrumbComponent],
  templateUrl: './tasks.component.html',
})
export class TasksComponent implements OnInit {
  tasks: Task[] = [];

  currentPage: number = 1; // Página atual
  itemsPerPage: number = 10; // Itens por página

  path = [
    { name: 'Fila de tarefas', link: '/tasks', icon: 'fa-solid fa-robot' },
  ];

  constructor(private taskService: TasksService) {}

  ngOnInit(): void {
    this.taskService.getTasks().subscribe((tasks) => {
      this.tasks = tasks;
    });
  }

  get paginatedTasks() {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    return this.tasks.slice(startIndex, startIndex + this.itemsPerPage);
  }

  get numPages() {
    const totalPages = Math.ceil(this.tasks.length / this.itemsPerPage);
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }

  nextPage() {
    if (this.currentPage * this.itemsPerPage < this.tasks.length) {
      this.currentPage++;
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }
}
