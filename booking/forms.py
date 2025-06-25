from django import forms
from .models import Reservation

# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ('number_of_guests', 'time', 'date', 'duration', 'special_reqs',)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'date', 'time', 'duration', 'special_reqs']
        widgets = {
            'number_of_guests': forms.NumberInput(attrs={'class': 'small_form_field'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'small_form_field'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'small_form_field'}),
            'duration': forms.NumberInput(attrs={'class': 'small_form_field'}),
            'special_reqs': forms.Textarea(attrs={'class': 'form_text_area', 'rows': 4}),
        }
        labels = {
            'duration': 'Booking duration (in hours)',
            'number_of_guests': 'Number of Guests (max 4)',
            'special_reqs': 'Special Requests',
        }
        help_texts = {
            'special_reqs': 'Let us know if you have any allergies or other special requirements.',
        }