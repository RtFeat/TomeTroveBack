from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserQuestionViewSet

router = DefaultRouter()
router.register(r'', UserQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]