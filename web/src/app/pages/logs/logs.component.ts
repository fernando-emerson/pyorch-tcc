import { Component, OnInit } from '@angular/core';
import { LogsService } from '../../shared/services/logs.service';
import { Log } from '../../core/models/log.model';
import { BreadcrumbComponent } from '../../shared/breadcrumb/breadcrumb.component';
import { LoadingService } from '../../shared/services/loading.service';
import { NgClass } from '@angular/common';
import { AutomationsService } from '../../shared/services/automations.service';
import { Automation } from '../../core/models/automation.model';

@Component({
  selector: 'app-logs',
  standalone: true,
  imports: [BreadcrumbComponent, NgClass],
  templateUrl: './logs.component.html',
})
export class LogsComponent implements OnInit {
  path = [{ name: 'Logs', link: '/logs', icon: 'fa-solid fa-robot' }];
  currentPage: number = 1; // Página atual
  itemsPerPage: number = 10; // Itens por página

  constructor(
    private logsService: LogsService,
    private loadingService: LoadingService
  ) {}

  logs: Log[] = [];
  automations: Automation[] = [];

  ngOnInit(): void {
    this.loadingService.show();
    this.logsService.getLogs().subscribe((result) => {
      this.loadingService.hide();
      this.logs = result;
    });
  }

  get paginatedlogs() {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    return this.logs.slice(startIndex, startIndex + this.itemsPerPage);
  }

  get numPages() {
    const totalPages = Math.ceil(this.logs.length / this.itemsPerPage);
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }

  nextPage() {
    if (this.currentPage * this.itemsPerPage < this.logs.length) {
      this.currentPage++;
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
    }
  }
}
