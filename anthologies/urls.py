from django.urls import path
from .views import AnthologyCreateView, AnthologyListView, AnthologyDetailView

urlpatterns = [
    path('api/anthology/create/', AnthologyCreateView.as_view(), name='anthology-create'),
    path('api/anthology/list/', AnthologyListView.as_view(), name='anthology-list'),
    path('api/anthology/<int:pk>/', AnthologyDetailView.as_view(), name='anthology-detail'),
]