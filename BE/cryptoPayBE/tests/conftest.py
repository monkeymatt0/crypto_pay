import pytest
from rest_framework.test import APIClient


# This file will contain only fixture
# {
#    Reference data for testing
#    "txHash": "0xabc123def4567890abc123def4567890abc123def4567890abc123def4567890",
#    "senderAddress": "0x1111222233334444555566667777888899990000",
#    "recipientAddress": "0x0000111122223333444455556666777788889999",
#    "amount": "100.12345678",
#    "status": "Pending",
#    "timestamp": "2024-10-15T12:34:56Z"
# }


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def get_transaction_payload_2xx() -> dict:
    return {
        "tx_hash": "0xabc123def4567890abc123def4567890abc123def4567890abc123def4567890",
        "sender_address": "0x1111222233334444555566667777888899990000",
        "recipient_address": "0x0000111122223333444455556666777788889999",
        "amount": "100.12345678",
        "status": "Pending",
        "timestamp": "2024-10-15T12:34:56Z",
    }


@pytest.fixture
def get_transaction_payload_400() -> dict:
    return {
        "tx_hash": "0xabc123def4567890abc123def4567890abc123def4567890abc123def4567890",
        "sender_address": "0x1111222233334444555566667777888899990000",
        "recipient_address": "0x0000111122223333444455556666777788889999",
    }
