from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from yookassa import Configuration, Payment, Webhook
import uuid
from anthologies.models import Anthology
from .models import Transaction
from .serializers import TransactionSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class CreatePaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):

        # SETTINGS YOOKASSA
        Configuration.account_id = '1096103'  #Shop ID
        Configuration.secret_key = 'test_PHZQnwRZMheW-pBZH8s8LXZuKTHZrPgCBFj81cYB4pQ'  #Secret Key

        anthology_id = request.data.get('anthology_id')
        try:
            anthology = Anthology.objects.get(id=anthology_id)
        except Anthology.DoesNotExist:
            return JsonResponse({'error': 'Anthology not found'}, status=404)

        # CREATE PAYMENT
        payment = Payment.create({
            'amount': {
                'value': str(anthology.price),
                'currency': 'RUB',
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': 'http://localhost:4200/protected/account/order-list',
            },
            'capture': True,
            'description': f'Оплата за {anthology.title}',
            'metadata': {'anthology_id': anthology_id},
        }, uuid.uuid4().hex)

        # SAVE TRANSACTION
        transaction = Transaction.objects.create(
            user=request.user,
            anthology=anthology,
            payment_id=payment.id,
            amount=anthology.price,
            status='Выполнено',
        )
    
        return JsonResponse({
            'payment_url': payment.confirmation.confirmation_url,
            'transaction_id': transaction.id,
        })

class TransactionListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

@csrf_exempt
def webhook(request):
    event = Webhook.parse(request.body)
    if event.object == 'payment' and event.event == 'payment.succeeded':
        payment_id = event.payment.id
        Transaction.objects.filter(payment_id=payment_id).update(status='succeeded')
    elif event.event == 'payment.canceled':
        payment_id = event.payment.id
        Transaction.objects.filter(payment_id=payment_id).update(status='canceled')
    return HttpResponse(status=200)