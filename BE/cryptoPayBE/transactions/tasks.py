import os
import logging
from celery import shared_task
from web3 import Web3
from .models import Transaction

# Here as url you should insert the test node on your local machine
web3Conn = Web3(Web3.HTTPProvider(os.getenv("DEVELOPMENT_BLOCKCHAIN")))
logger = logging.getLogger(__name__)


@shared_task
def monitor_transactions_status():
    try:
        pendingTransactions = Transaction.objects.get(status="Pending")
        for transaction in pendingTransactions:
            receipt = web3Conn.eth.get_transaction_receipt(transaction.tx_hash)
            if receipt:
                if receipt.status == 1:
                    transaction.status = "Confirmed"
                else:
                    transaction.status = "Failed"
                transaction.save()
    except Transaction.DoesNotExist:
        logger.exception("No transaction in pending state found")
