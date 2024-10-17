import pytest
import logging
from rest_framework.request import Request
from rest_framework.response import Response

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

logger = logging.getLogger(__name__)


@pytest.mark.django_db
def test_create_transaction_201(api_client, get_transaction_payload_201):
    response = api_client.post(
        "/api/transactions/create/", data=get_transaction_payload_201, format="json"
    )
    logger.info(f"{response}")
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_transaction_400(api_client, get_transaction_payload_400):
    response = api_client.post(
        "/api/transactions/create/", data=get_transaction_payload_400, format="json"
    )
    logger.info(f"{response}")
    assert response.status_code == 400
