import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

export interface Page {
  name: string;
  link: string;
  icon: string;
}

@Component({
  selector: 'app-breadcrumb',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './breadcrumb.component.html',
})
export class BreadcrumbComponent {
  @Input() path: Page[] = [];
}
