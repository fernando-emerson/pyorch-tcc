import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
// import { faCoffee } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './sidebar.component.html',
})
export class SidebarComponent {
  // coffe = faCoffee;
}
