import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import detectEthereumProvider from '@metamask/detect-provider';

@Component({
  selector: 'app-wallet-connect',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './wallet-connect.component.html',
  styleUrl: './wallet-connect.component.css',
})
export class WalletConnectComponent {
  connected: boolean = false;
  provider: any;
  userAddress: string = '';
  recipientAddress: string = '';
  transactionHash: string = '';
  amount: string = '';

  constructor() {
    this.initMetaMask();
  }

  // This method will detect metamask and use initialize it
  async initMetaMask() {
    this.provider = detectEthereumProvider();
    if (this.provider) {
      console.log('Metamask detected!!');
    } else {
      console.error('Metamask not detected, please install metamask');
      window.alert(
        'Metamask not found, to properly use the application please install it'
      );
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

  async sendTransaction() {
    const amountInWei = this.convertEthToWei(this.amount);
    const transactionParams = {
      to: '0xReceiverAddressHere',
      from: this.userAddress,
      value: amountInWei,
      gas: '0x5208', // For now this is constant but @remind : retrieve the gas fees directly on the blockchain
    };
  }

  convertEthToWei(ethAmount: string) {
    return BigInt(parseFloat(ethAmount) * Math.pow(10, 18)).toString(16);
  }
}
