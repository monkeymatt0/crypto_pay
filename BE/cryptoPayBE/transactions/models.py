from django.db import models


# Create your models here.
class Transaction(models.Model):
    tx_hash = models.CharField(
        max_length=66, unique=True
    )  # This one in unique by default the constraint is not have double values in the DB
    sender_address = models.CharField(max_length=42)
    recipient_address = models.CharField(max_length=42)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(max_length=20, default="Pending")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transactions"

    def __str__(self):
        return f"Transaction {self.tx_hash}: {self.status}"
