from rest_framework import viewsets
from .models import UserQuestion
from .serializers import UserQuestionSerializer

class UserQuestionViewSet(viewsets.ModelViewSet):
    queryset = UserQuestion.objects.all()
    serializer_class = UserQuestionSerializer