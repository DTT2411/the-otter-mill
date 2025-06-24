from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('number_of_guests', 'time', 'date', 'duration', 'special_reqs',)