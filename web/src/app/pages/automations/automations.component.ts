import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { BreadcrumbComponent } from '../../shared/breadcrumb/breadcrumb.component';
import { ApiService } from '../../shared/services/api.service';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { LoadingService } from '../../shared/services/loading.service';
import { ToastService } from '../../shared/services/toast.service';
import { AutomationsService } from '../../shared/services/automations.service';
import { startupSnapshot } from 'v8';

@Component({
  selector: 'app-automations',
  standalone: true,
  imports: [CommonModule, BreadcrumbComponent, RouterLink],
  templateUrl: './automations.component.html',
})
export class AutomationsComponent implements OnInit {
  selectedItem: any = {};
  mode: string = 'edit';
  automations: any[] = [];
  path = [
    { name: 'Automações', link: '/automacoes', icon: 'fa-solid fa-robot' },
  ];

  constructor(
    private automationsService: AutomationsService,
    private router: Router,
    private route: ActivatedRoute,
    private loadingService: LoadingService,
    private toastService: ToastService
  ) {}

  ngOnInit(): void {
    this.loadAutomations();
  }

  loadAutomations() {
    this.automationsService.getAutomations().subscribe((value) => {
      this.automations = value;
    });
  }

  editItem(item: any) {
    this.selectedItem = item; // Define o item a ser editado
    this.mode = 'edit'; // Modo de edição
    this.router.navigate(['editar', item.id], { relativeTo: this.route });
  }

  deleteAutomation(id: number) {
    this.loadingService.show();
    this.automationsService.deleteAutomation(id).subscribe((res) => {
      this.loadingService.hide();
      this.toastService.showToast('Item removido', 'success');
    });
  }

  execute(id: number) {
    this.loadingService.show();
    this.automationsService.execute(id).subscribe((res) => {
      this.loadingService.hide();
      this.toastService.showToast('Automação enviada para a fila!', 'success');
    });
  }

  openForm() {
    this.router.navigate(['cadastrar'], { relativeTo: this.route });
  }
}
