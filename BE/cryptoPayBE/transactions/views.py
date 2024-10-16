from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer

serializer = TransactionSerializer()

# Create your views here.
@api_view(["POST"])
def create_transaction(request):
    return serializer.post(request=request)
