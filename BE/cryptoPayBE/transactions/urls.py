from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path("create/", views.create_transaction, name="create_transaction"),
]
