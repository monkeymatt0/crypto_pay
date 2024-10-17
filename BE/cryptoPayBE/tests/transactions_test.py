import pytest
from rest_framework.request import Request
from rest_framework.response import Response

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

from .test_logger import logger


@pytest.mark.django_db
def test_create_transaction_201_created(api_client, get_transaction_payload_2xx):
    response = api_client.post(
        "/api/transactions/create/", data=get_transaction_payload_2xx, format="json"
    )
    logger.info(f"{response}")
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_transaction_400_bad_request(api_client, get_transaction_payload_400):
    response = api_client.post(
        "/api/transactions/create/", data=get_transaction_payload_400, format="json"
    )
    logger.info(f"{response}")
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_transaction_status(api_client, get_transaction_payload_2xx):
    api_client.post(
        "/api/transactions/create/", data=get_transaction_payload_2xx, format="json"
    )
    response_OK = api_client.get(
        "/api/transactions/status/0xabc123def4567890abc123def4567890abc123def4567890abc123def4567890",
        format="json",
    )
    response_NOT_FOUND = api_client.get(
        "/api/transactions/status/0xabc123def4567890abc123d777567890abc123def4567890abc123def4567890",
        format="json",
    )
    logger.info(f"{response_OK}")
    assert response_OK.status_code == 200

    logger.info(f"{response_NOT_FOUND}")
    assert response_NOT_FOUND.status_code == 404
