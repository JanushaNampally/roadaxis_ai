from django.urls import path
from .views import create_booking, booking_success

urlpatterns = [
path('<int:machine_id>/', create_booking, name='create_booking'),
path('success/', booking_success, name='booking_success'),
]