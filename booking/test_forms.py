from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_form_is_valid(self):
        reservation_form = ReservationForm(
            {'number_of_guests': '3'},
            {'date': '2025-07-01'},
            {'time': '20:30:00'},
            {'duration': '3'},
            {'special_reqs': 'None'},
        )
        self.assertTrue(reservation_form.is_valid(), msg="Form is not valid")
