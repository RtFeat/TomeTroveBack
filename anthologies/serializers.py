from rest_framework import serializers
from .models import Anthology
    
class AnthologySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Anthology
        fields = ['id', 'title', 'image', 'description', 'topic', 'price']