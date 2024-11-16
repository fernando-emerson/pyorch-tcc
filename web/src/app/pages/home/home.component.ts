import { Component, OnInit } from '@angular/core';
import { NgApexchartsModule } from 'ng-apexcharts';
import { AreaChartComponent } from './charts/area-chart/area-chart.component';
import { DashboardService } from '../../shared/services/dashboard.service';
import { DashboardStats } from '../../core/models/stat.model';
import { LoadingService } from '../../shared/services/loading.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [NgApexchartsModule, AreaChartComponent],
  templateUrl: './home.component.html',
})
export class HomeComponent implements OnInit {
  stats?: DashboardStats;

  constructor(
    private dashboardService: DashboardService,
    private loadingService: LoadingService
  ) {}

  ngOnInit(): void {
    this.loadingService.show();
    this.dashboardService.getStats().subscribe((res) => {
      this.loadingService.hide();
      this.stats = res;
    });
  }
}
