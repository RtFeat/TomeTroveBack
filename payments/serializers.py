from rest_framework import serializers
from .models import Transaction
from anthologies.models import Anthology
from anthologies.serializers import AnthologySerializer

class TransactionSerializer(serializers.ModelSerializer):
    anthology = AnthologySerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'anthology', 'payment_id', 'amount', 'status', 'created_at']