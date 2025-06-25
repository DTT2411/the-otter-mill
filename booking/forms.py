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
            'number_of_guests': forms.NumberInput(attrs={'class': 'small_form_field center-field', 'max': 6}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'small_form_field'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'small_form_field'}),
            'duration': forms.NumberInput(attrs={'class': 'small_form_field center-field', 'max': 3}),
            'special_reqs': forms.Textarea(attrs={
                'class': 'form_text_area center-field',
                'rows': 4,
                'placeholder': 'Let us know if you have any allergies or other special requirements.'
            }),
        }
        labels = {
            'duration': 'Booking duration (max 3 hours)',
            'number_of_guests': 'Number of guests (max 6)',
            'special_reqs': 'Special Requirements',
        }
        help_texts = {
            # 'special_reqs': 'Let us know if you have any allergies or other special requirements.',
        }