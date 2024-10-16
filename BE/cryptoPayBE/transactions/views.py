from rest_framework.decorators import api_view
from .models import Transaction
from .serializers import TransactionSerializer


# Create your views here.
@api_view(["POST"])
def create_transaction(request):
    return TransactionSerializer.post(request)
