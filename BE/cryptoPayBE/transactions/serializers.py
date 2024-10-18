from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

    def post(self, request) -> Response:
        serializedTxn = TransactionSerializer(data=request.data)
        if serializedTxn.is_valid():
            transaction = serializedTxn.save()
            return Response(serializedTxn.data, status=status.HTTP_201_CREATED)
        return Response(serializedTxn.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, transactionHash) -> Response:
        try:
            transaction = Transaction.objects.get(tx_hash=transactionHash)
        except Transaction.DoesNotExist:
            return Response(
                {"error": "Transaction not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
