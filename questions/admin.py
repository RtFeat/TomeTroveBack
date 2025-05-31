from django.contrib import admin
from .models import UserQuestion

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'question')
    ordering = ('-created_at',)
# Register your models here.
