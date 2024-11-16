import { Component, ViewChild } from '@angular/core';
import {
  Directive,
  Inject,
  OnInit,
  PLATFORM_ID,
  TemplateRef,
  ViewContainerRef,
} from '@angular/core';
import { isPlatformServer, isPlatformBrowser } from '@angular/common';

import {
  ApexDataLabels,
  ApexFill,
  ApexGrid,
  ApexStroke,
  ApexTooltip,
  ApexYAxis,
  NgApexchartsModule,
} from 'ng-apexcharts';

import {
  ChartComponent,
  ApexAxisChartSeries,
  ApexChart,
  ApexXAxis,
  ApexTitleSubtitle,
} from 'ng-apexcharts';

export type ChartOptions = {
  series: ApexAxisChartSeries;
  chart: ApexChart;
  xaxis: ApexXAxis;
  title: ApexTitleSubtitle;
  tooltip: ApexTooltip;
  fill: ApexFill;
  dataLabels: ApexDataLabels;
  stroke: ApexStroke;
  grid: ApexGrid;
  yaxis: ApexYAxis;
};

@Component({
  selector: 'app-area-chart',
  standalone: true,
  imports: [NgApexchartsModule],
  templateUrl: './area-chart.component.html',
})
export class AreaChartComponent {
  @ViewChild('chart')
  chart!: ChartComponent;
  public options!: Partial<ChartOptions>;

  test: string = 'fas';

  isBrowser: boolean;

  constructor(@Inject(PLATFORM_ID) platformId: object) {
    this.isBrowser = isPlatformBrowser(platformId);

    this.options = {
      chart: {
        height: '100%',
        width: '100%',
        type: 'area',
        fontFamily: 'Inter, sans-serif',
        dropShadow: {
          enabled: false,
        },
        toolbar: {
          show: false,
        },
      },
      tooltip: {
        enabled: true,
        x: {
          show: false,
        },
      },
      fill: {
        type: 'gradient',
        gradient: {
          opacityFrom: 0.55,
          opacityTo: 0,
          shade: '#1C64F2',
          gradientToColors: ['#1C64F2'],
        },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        width: 6,
      },
      grid: {
        show: false,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: 0,
        },
      },
      series: [
        {
          name: 'New users',
          data: [6500, 6418, 6456, 6526, 6356, 6456],
          color: '#1A56DB',
        },
      ],
      xaxis: {
        categories: [
          '01 February',
          '02 February',
          '03 February',
          '04 February',
          '05 February',
          '06 February',
          '07 February',
        ],
        labels: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
        axisTicks: {
          show: false,
        },
      },
      yaxis: {
        show: false,
      },
    };

    console.log(this.isBrowser);

    if (this.isBrowser) {
      const ApexCharts = require('apexcharts');
      const chart = new ApexCharts(
        document.querySelector('#chart'),
        this.options
      );
      chart.render();
    }
  }
}
