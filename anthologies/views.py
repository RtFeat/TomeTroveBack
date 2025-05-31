from django.shortcuts import render
from rest_framework import generics
from .serializers import AnthologySerializer
from .models import Anthology

class AnthologyCreateView(generics.CreateAPIView):
    queryset = Anthology.objects.all()
    serializer_class = AnthologySerializer

class AnthologyListView(generics.ListAPIView):
    queryset = Anthology.objects.all()
    serializer_class = AnthologySerializer

class AnthologyDetailView(generics.RetrieveAPIView):
    queryset = Anthology.objects.all()
    serializer_class = AnthologySerializer
    lookup_field = 'pk'