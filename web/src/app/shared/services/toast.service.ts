import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

interface Toast {
  id: number;
  message: string;
  type: 'success' | 'error' | 'warning' | 'info';
}

@Injectable({
  providedIn: 'root',
})
export class ToastService {
  private toastsSubject = new BehaviorSubject<Toast[]>([]);
  public toasts$ = this.toastsSubject.asObservable();
  private currentId = 0;

  showToast(
    message: string,
    type: Toast['type'] = 'info',
    duration: number = 6000
  ) {
    const newToast: Toast = { id: this.currentId++, message, type };
    const currentToasts = this.toastsSubject.value;

    // Adiciona a nova toast
    this.toastsSubject.next([...currentToasts, newToast]);

    // Remove a toast automaticamente após o tempo definido
    setTimeout(() => {
      this.removeToast(newToast.id);
    }, duration);
  }

  removeToast(id: number) {
    const updatedToasts = this.toastsSubject.value.filter(
      (toast) => toast.id !== id
    );
    this.toastsSubject.next(updatedToasts);
  }
}
