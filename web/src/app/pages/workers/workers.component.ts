import { Component, OnInit } from '@angular/core';
import { BreadcrumbComponent } from '../../shared/breadcrumb/breadcrumb.component';
import { WorkersService } from '../../shared/services/workers.service';
import { Worker } from '../../core/models/worker.model';
import { LoadingService } from '../../shared/services/loading.service';

@Component({
  selector: 'app-workers',
  standalone: true,
  imports: [BreadcrumbComponent],
  templateUrl: './workers.component.html',
})
export class WorkersComponent implements OnInit {
  workers: Worker[] = [];

  path = [{ name: 'Workers', link: '/tasks', icon: 'fa-solid fa-laptop-code' }];

  constructor(
    private workersService: WorkersService,
    private loadingService: LoadingService
  ) {}

  ngOnInit(): void {
    this.loadWorkers();
  }

  loadWorkers() {
    this.loadingService.show();
    this.workersService.getWorkers().subscribe((workers) => {
      this.workers = workers;
      this.loadingService.hide();
    });
  }
}
