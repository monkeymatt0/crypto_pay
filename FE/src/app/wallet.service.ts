import { Injectable } from '@angular/core';
import detectEthereumProvider from '@metamask/detect-provider';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class WalletService {
  provider: any;
  userAddress: string = '';
  connected = new BehaviorSubject<boolean>(false);
  isConnected$ = this.connected.asObservable();

  constructor() {
    this.initMetaMask();
  }

  setConnected(value: boolean) {
    this.connected.next(value);
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
