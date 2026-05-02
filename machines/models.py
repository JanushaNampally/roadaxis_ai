from django.db import models

class Machine(models.Model):
    MACHINE_TYPES = [
        ('roller', 'Road Roller'),
        ('excavator', 'Excavator'),
        ('vibrator', 'Vibrator'),
        ('hydraulic', 'Hydraulic Machine'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    machine_type = models.CharField(max_length=50, choices=MACHINE_TYPES)
    description = models.TextField()
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='machines/', blank=True, null=True)

    def __str__(self):
        return self.name