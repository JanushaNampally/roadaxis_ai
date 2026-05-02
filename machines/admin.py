from django.contrib import admin
from .models import Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'machine_type', 'daily_rate', 'is_available')
    list_filter = ('machine_type', 'is_available')
    search_fields = ('name',)