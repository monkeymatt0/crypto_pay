from rest_framework.decorators import api_view
from .serializers import TransactionSerializer

serializer = TransactionSerializer()


# Create your views here.
@api_view(["POST"])
def create_transaction(request):
    return serializer.post(request=request)


@api_view(["GET"])
def get_transaction_status(request, transactionHash):
    return serializer.get(transactionHash)
