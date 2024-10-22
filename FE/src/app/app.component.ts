import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { WalletConnectComponent } from './wallet-connect/wallet-connect.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, WalletConnectComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'FE';
}
