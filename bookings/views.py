from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from machines.models import Machine
from customers.models import Customer


def create_booking(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # 🔹 Get or create customer
            customer, created = Customer.objects.get_or_create(
                phone=data['phone'],
                defaults={
                    'name': data['customer_name'],
                    'email': data.get('email'),
                    'location': data.get('location')
                }
            )

            # 🔹 Create booking instance (not saved yet)
            booking = Booking(
                customer=customer,
                machine=machine,
                start_date=data['start_date'],
                end_date=data['end_date'],
                location=data['location'],
                message=data.get('message', '')
            )

            # 🚫 Conflict check (avoid double booking)
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

            # ✅ Save booking
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