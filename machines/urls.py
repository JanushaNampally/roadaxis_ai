from django.urls import path
from .views import machine_list

urlpatterns = [
    path('', machine_list, name='machine_list'),
]