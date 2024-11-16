import { Component } from '@angular/core';
import { ToastService } from '../../services/toast.service';
import { AsyncPipe, NgClass } from '@angular/common';

@Component({
  selector: 'app-toast',
  standalone: true,
  imports: [AsyncPipe, NgClass],
  template: `
    <div class="fixed bottom-5 right-5 space-y-3 w-80">
      @for (toast of $any(toastService.toasts$ | async); track toast) {
      <div
        [ngClass]="{
          'bg-green-500': toast.type === 'success',
          'bg-red-500': toast.type === 'error',
          'bg-yellow-500': toast.type === 'warning',
          'bg-blue-500': toast.type === 'info'
        }"
        class="p-4 rounded-lg text-white shadow-lg flex items-center justify-between mb-3"
      >
        <span>{{ toast.message }}</span>
        <button
          (click)="toastService.removeToast(toast.message)"
          class="ml-auto text-white font-bold"
        >
          ✖
        </button>
      </div>
      }
    </div>
  `,
})
export class ToastComponent {
  constructor(public toastService: ToastService) {}
}
