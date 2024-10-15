from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer


# Create your views here.
@api_view(["POST"])
def create_transaction(request):
    serializedTxn = TransactionSerializer(data=request.data)
    if serializedTxn.is_valid():
        serializedTxn.save()
        return Response(serializedTxn.data, status=status.HTTP_201_CREATED)
    return Response(serializedTxn.errors, status=status.HTTP_400_BAD_REQUEST)
