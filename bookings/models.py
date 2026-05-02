from django.db import models

# Create your models here.
from django.db import models
from machines.models import Machine

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    start_date = models.DateField()
    end_date = models.DateField()

    location = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.machine.name}"