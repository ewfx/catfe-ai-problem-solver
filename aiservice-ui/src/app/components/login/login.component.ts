import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  credentials = { username: '', password: '' };
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.credentials).subscribe({
      next: (response) => {
        console.log(response); // Log the response for debugging
        if (response === 'Login successful') {
          this.router.navigate(['/logout']); // Navigate to the logout page
        } else {
          this.errorMessage = 'Unexpected response from the server';
        }
      },
      error: () => {
        this.errorMessage = 'Invalid credentials';
      }
    });
  }
}