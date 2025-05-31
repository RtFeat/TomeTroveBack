from django.contrib import admin
from .models import Anthology

@admin.register(Anthology)
class AnthologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'price', 'created_at')
    list_filter = ('topic', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
# Register your models here.
