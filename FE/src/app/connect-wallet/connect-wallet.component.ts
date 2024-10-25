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
  provider: any;
  userAddress: string = '';

  constructor() {
    this.initMetaMask();
  }

  // This method will detect metamask and use initialize it
  async initMetaMask() {
    this.provider = await detectEthereumProvider();
    if (this.provider) {
      console.log('Metamask detected!!');
    } else {
      console.error('Metamask not detected, please install metamask');
      window.alert(
        'Metamask not found, to properly use the application please install it'
      );
    }
  }

  async listWallets() {
    try {
      if (this.provider) {
        const accounts = await this.provider.request({
          method: 'eth_requestAccounts',
          params: [],
        });
        console.log(accounts);
      }
    } catch (error) {
      console.log(error);
    }
  }

  async connectWallet() {
    try {
      const accounts = await this.provider.request({
        method: 'eth_requestAccounts',
      });
      this.userAddress = accounts[0]; // Here we are connecting to account 0 by default for now later we should be able to @remind : pick an account of my choice
      console.log('Connected account: ', this.userAddress);
    } catch (error) {
      console.error('User rejecteed the request:', error);
    }
  }
}
