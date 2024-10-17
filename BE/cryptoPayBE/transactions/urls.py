from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_transaction, name="create_transaction"),
    path(
        "status/<str:transactionHash>",
        views.get_transaction_status,
        name="get_transaction_status",
    ),
]
