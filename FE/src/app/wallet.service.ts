import { Injectable } from '@angular/core';
import detectEthereumProvider from '@metamask/detect-provider';

@Injectable({
  providedIn: 'root',
})
export class WalletService {
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
}
