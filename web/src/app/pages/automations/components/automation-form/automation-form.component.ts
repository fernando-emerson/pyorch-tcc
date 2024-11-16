import { CommonModule } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Worker } from '../../../../core/models/worker.model';
import { WorkersService } from '../../../../shared/services/workers.service';
import { LoadingService } from '../../../../shared/services/loading.service';
import { AutomationsService } from '../../../../shared/services/automations.service';
import { ToastService } from '../../../../shared/services/toast.service';

@Component({
  selector: 'app-automation-form',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './automation-form.component.html',
})
export class AutomationFormComponent implements OnInit {
  form!: FormGroup;
  title!: string;
  workers: Worker[] = [];

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private loadingService: LoadingService,
    private automationService: AutomationsService,
    private toastService: ToastService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.initializeForm();
    this.setTitle();
    this.fillFormIfEditing();
  }

  initializeForm(): void {
    this.form = this.fb.group({
      id: [''],
      name: ['', Validators.required],
      description: [''],
      status: [''],
      file: [null],
    });
  }

  setTitle(): void {
    const path = this.route.snapshot.url[0]?.path || '';
    this.title =
      path == 'cadastrar' ? 'Cadastrar automação' : 'Editar automação';
  }

  fillFormIfEditing(): void {
    const path = this.route.snapshot.url[0]?.path || '';
    const id = this.route.snapshot.paramMap.get('id');
    if (path === 'editar' && id) {
      this.automationService.getAutomationById(id).subscribe((data) => {
        this.form.patchValue(data);
      });
    }
  }

  onSubmit() {
    const path = this.route.snapshot.url[0]?.path || '';
    if (path == 'cadastrar') {
      this.createAutomation();
    } else if (path == 'editar') {
      this.updateAutomation();
    }
    return false;
  }

  createAutomation() {
    const formData = new FormData();
    formData.append('name', this.form.value['name']);
    formData.append('description', this.form.value['description']);
    formData.append('status', this.form.value['status']);
    formData.append('file', this.form.value.file || null);

    this.loadingService.show();
    this.automationService.createAutomation(formData).subscribe((res) => {
      this.loadingService.hide();
      this.toastService.showToast(
        'Automação cadastrada com sucesso!',
        'success'
      );
      this.router.navigate(['automacoes']);
    });
  }

  updateAutomation() {
    this.loadingService.show();
    this.automationService
      .updateAutomation(this.form.value)
      .subscribe((res) => {
        this.loadingService.hide();
        this.toastService.showToast(
          'Automação atualizada com sucesso!',
          'success'
        );
        this.router.navigate(['automacoes']);
      });
  }

  onFileUpload(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      this.form.patchValue({ file: file });
    }
  }
}
