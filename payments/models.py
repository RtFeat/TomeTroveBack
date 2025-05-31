from django.db import models
from anthologies.models import Anthology
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    anthology = models.ForeignKey(Anthology, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)  # ID платежа в ЮKassa
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction {self.payment_id} for {self.anthology.title} by {self.user.username}'