from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    # Extra fields (NOT in Booking model)
    customer_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'})
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email (optional)'})
    )

    class Meta:
        model = Booking
        # exclude fields handled manually
        exclude = ['machine', 'status', 'customer', 'created_at']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Project location'}),
            'message': forms.Textarea(attrs={'placeholder': 'Additional details'}),
        }