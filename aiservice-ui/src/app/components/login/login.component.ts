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
  successMessage ='';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
 
    if (!this.credentials.username) {
       this.errorMessage = '';
      this.successMessage =''
      this.errorMessage = 'Username is required';
      return;
    }
  
    if (!this.credentials.password) {
      this.errorMessage = '';
      this.successMessage =''
      this.errorMessage = 'Password is required';
      return;
    }
  
    this.authService.login(this.credentials).subscribe({
      next: (response) => {
        console.log(response);
        this.credentials = { username: '', password: '' };
        if (response === 'Login successful') {
          this.successMessage = 'Login successful';
          this.errorMessage = '';
        } else {
          this.errorMessage = 'Unexpected response from the server';
          this.successMessage = '';
        }
      },
      error: () => {
        this.errorMessage = 'Invalid credentials';
        this.successMessage = '';

      }
    });
  }
}