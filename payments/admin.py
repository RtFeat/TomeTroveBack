from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'user', 'anthology', 'amount', 'status', 'created_at')  # Поля для отображения в списке
    list_filter = ('status', 'created_at', 'user')  # Фильтры в боковой панели
    search_fields = ('payment_id', 'user__username', 'anthology__title')  # Поля для поиска
    list_editable = ('status',)  # Поля, которые можно редактировать прямо в списке
    date_hierarchy = 'created_at'  # Иерархия по датам для навигации
    ordering = ('-created_at',)  # Сортировка по убыванию даты создания

    def get_readonly_fields(self, request, obj=None):
        # Поля, которые нельзя редактировать после создания
        if obj:  # Если объект уже существует
            return ('payment_id', 'user', 'anthology', 'amount', 'created_at')
        return ()

    def has_add_permission(self, request):
        # Запрет на создание транзакций через админку
        return False

    def has_delete_permission(self, request, obj=None):
        # Запрет на удаление транзакций через админку (опционально)
        return True
