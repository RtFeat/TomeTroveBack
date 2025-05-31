from django.urls import path
from .views import CreatePaymentView, TransactionListView, webhook

urlpatterns = [
    path('api/payment/create/', CreatePaymentView.as_view(), name='payment-create'),
    path('api/transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('api/payment/webhook/', webhook, name='payment-webhook'),
]