import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-logout',
  imports: [FormsModule,CommonModule],
  template: `
    <button (click)="logout()">Logout</button>
  `,
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent {
  constructor(private authService: AuthService, private router: Router) {}

  logout() {
    this.authService.logout().subscribe({
      next: () => {
        // Redirect to the login page after successful logout
        this.router.navigate(['/login']);
      },
      error: () => {
        // Handle logout failure (optional)
        console.error('Logout failed. Please try again.');
        this.router.navigate(['/login']);
      }
    });
  }
}