
from django.contrib import admin
from .models import Service, QueueToken


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(QueueToken)
class QueueTokenAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'token_number', 'user',
        'service', 'status', 'created_at'
    )
    list_filter = ('status', 'service', 'created_at')
    search_fields = ('user__username', 'service__name')

