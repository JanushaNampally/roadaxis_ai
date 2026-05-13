from django.shortcuts import render
from machines.models import Machine
from bookings.models import Booking
from customers.models import Customer


def dashboard_home(request):

    total_machines = Machine.objects.count()
    total_bookings = Booking.objects.count()
    total_customers = Customer.objects.count()

    available_machines = Machine.objects.filter(
        is_available=True
    ).count()

    recent_bookings = Booking.objects.order_by('-created_at')[:5]

    context = {
        'total_machines': total_machines,
        'total_bookings': total_bookings,
        'total_customers': total_customers,
        'available_machines': available_machines,
        'recent_bookings': recent_bookings,
    }

    return render(request, 'dashboard/dashboard.html', context)