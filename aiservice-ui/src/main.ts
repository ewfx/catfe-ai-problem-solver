import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app/app.component';
import { RegisterComponent } from './app/components/register/register.component';
import { LoginComponent } from './app/components/login/login.component';
import { LogoutComponent } from './app/components/logout/logout.component';
import { AuthGuard } from './app/guards/auth.guard';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter([
      { path: 'register', component: RegisterComponent },
      { path: 'login', component: LoginComponent },
      { path: 'logout', component: LogoutComponent, canActivate: [AuthGuard] },
      { path: '', redirectTo: '/login', pathMatch: 'full' }
    ]),
    provideHttpClient()
  ]
}).catch((err) => console.error(err));