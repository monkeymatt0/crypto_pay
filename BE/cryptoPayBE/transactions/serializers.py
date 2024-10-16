from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        
    def post(self, request):
        serializedTxn = TransactionSerializer(data=request.data)
        if serializedTxn.is_valid():
            serializedTxn.save()
            return Response(serializedTxn.data, status=status.HTTP_201_CREATED)
        return Response(serializedTxn.errors, status=status.HTTP_400_BAD_REQUEST)
