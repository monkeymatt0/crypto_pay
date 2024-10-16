import pytest
import logging
from rest_framework.request import Request
from rest_framework.response import Response

from conftest import get_transaction_payload
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_create_transaction_201(api_client, transaction_payload):
     response = api_client.post('/api/transactions/create/', data=get_transaction_payload(), fromat="json")