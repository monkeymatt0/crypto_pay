import { WalletService } from './../wallet.service';
import { Component } from '@angular/core';
import detectEthereumProvider from '@metamask/detect-provider';

@Component({
  selector: 'app-connect-wallet',
  standalone: true,
  imports: [],
  templateUrl: './connect-wallet.component.html',
  styleUrl: './connect-wallet.component.css',
})
export class ConnectWalletComponent {
  constructor(private walletService: WalletService) {}

  async connectWallet() {
    try {
      const accounts = await this.walletService.provider.request({
        method: 'eth_requestAccounts',
      });
      this.walletService.userAddress = accounts[0];
      console.log('Connected account: ', this.walletService.userAddress);
      console.log('Connected accounts: ', accounts);
    } catch (error) {
      console.error('User rejecteed the request:', error);
    }
  }
}
