from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'machine', 'start_date', 'status')
    list_filter = ('status',)
    search_fields = ('customer_name', 'phone')