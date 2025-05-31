from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

# Create your models here.

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar']

class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(source='username', required=False)
    avatar = serializers.ImageField(source='profile.avatar', required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'login', 'email', 'password', 'avatar', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'required': False},
            }

    def create(self, validated_date):
        profile_data = validated_date.pop('profile', {})
        user = User.objects.create_user(
            username = validated_date['username'],
            email = validated_date['email'],
            password = validated_date['password']
        ) 
        UserProfile.objects.create(user=user, avatar=profile_data.get('avatar', None))
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        profile, created = UserProfile.objects.get_or_create(user=instance)
        if 'avatar' in profile_data:
            profile.avatar = profile_data['avatar']
            profile.save()
        return instance
    
        
