from django import forms
from django.utils import timezone
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_guests', 'date', 'time', 'duration',
                  'special_reqs']
        # Adds custom css classes and maxmimum values (where appropriate) to
        # reservation form fields
        widgets = {
            'number_of_guests': forms.NumberInput(attrs={
                'class': 'small_form_field center-field', 'max': 6}),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'small_form_field',
                    'min': timezone.now().date().isoformat(),  # Today's date
                }),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'small_form_field',
                    'min': '12:00',
                    'max': '22:00',
                }),
            'duration': forms.NumberInput(
                attrs={
                    'class': 'small_form_field center-field',
                    'max': 3,
                }),
            'special_reqs': forms.Textarea(
                attrs={
                    'class': 'form_text_area center-field',
                    'rows': 4,
                    'placeholder': 'Let us know if you have any allergies or '
                    'other special requirements.',
                    'maxlength': 300,
                }),
        }
        # Adds labels to fields requiring additional context
        labels = {
            'duration': 'Booking duration (max 3 hours)',
            'number_of_guests': 'Number of guests (max 6)',
            'special_reqs': 'Special Requirements',
        }

    def clean_time(self):
        time = self.cleaned_data['time']
        import datetime
        min_time = datetime.time(12, 0)
        max_time = datetime.time(22, 0)
        if not (min_time <= time <= max_time):
            from django.core.exceptions import ValidationError
            raise ValidationError(
                "Booking time must be between 12:00 and 22:00.")
        return time
