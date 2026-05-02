from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from machines.models import Machine
from .models import Booking

def create_booking(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.machine = machine

            # 🚫 CHECK DOUBLE BOOKING
            conflict = Booking.objects.filter(
                machine=machine,
                start_date__lte=booking.end_date,
                end_date__gte=booking.start_date,
                status='approved'
            ).exists()

            if conflict:
                return render(request, 'bookings/create_booking.html', {
                    'form': form,
                    'machine': machine,
                    'error': "This machine is already booked for selected dates."
                })

            booking.save()
            return redirect('booking_success')

    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'machine': machine
    })
def booking_success(request):
    return render(request, 'bookings/success.html')