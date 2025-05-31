# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/profile.svg')

    def save(self, *args, **kwargs):
        if self.pk:
            old_profile = UserProfile.objects.get(pk=self.pk)
            if old_profile.avatar and old_profile.avatar.name != 'avatars/profile.svg' and self.avatar != old_profile.avatar:
                default_storage.delete(old_profile.avatar.name)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.avatar and self.avatar.name != 'avatars/profile.svg':
            default_storage.delete(self.avatar.name)
        super().delete(*args, **kwargs)