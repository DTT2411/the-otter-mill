from django.test import TestCase
from .forms import ReservationForm


class TestReservationForm(TestCase):

    def test_form_is_valid(self):
        """
        Tests for all valid fields.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '3',
            'date': '2025-07-01',
            'time': '20:30:00',
            'duration': '3',
            'special_reqs': 'None',
        })
        self.assertTrue(reservation_form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid(self):
        """
        Tests for all empty fields.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '',
            'date': '',
            'time': '',
            'duration': '',
            'special_reqs': '',
        })
        self.assertFalse(reservation_form.is_valid(), msg="Form is valid")

    def test_number_of_guests_is_required(self):
        """
        Tests whether empty field for number_of_guests results in invalid form.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '',
            'date': '2025-07-01',
            'time': '20:30:00',
            'duration': '3',
            'special_reqs': 'None',
        })
        self.assertFalse(reservation_form.is_valid(),
                         msg="Empty number_of_guests field is valid")

    def test_date_is_required(self):
        """
        Tests whether empty field for date results in invalid form.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '3',
            'date': '',
            'time': '20:30:00',
            'duration': '3',
            'special_reqs': 'None',
        })
        self.assertFalse(reservation_form.is_valid(),
                         msg="Empty date field is valid")

    def test_time_is_required(self):
        """
        Tests whether empty field for time results in invalid form.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '3',
            'date': '2025-07-01',
            'time': '',
            'duration': '3',
            'special_reqs': 'None',
        })
        self.assertFalse(reservation_form.is_valid(),
                         msg="Empty time field is valid")

    def test_duration_is_required(self):
        """
        Tests whether empty field for duration results in invalid form.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '3',
            'date': '2025-07-01',
            'time': '20:30:00',
            'duration': '',
            'special_reqs': 'None',
        })
        self.assertFalse(reservation_form.is_valid(),
                         msg="Empty number_of_guests field is valid")

    def test_special_reqs_is_not_required(self):
        """
        Tests whether empty field for special_reqs results in valid form.
        """
        reservation_form = ReservationForm({
            'number_of_guests': '3',
            'date': '2025-07-01',
            'time': '20:30:00',
            'duration': '3',
            'special_reqs': '',
        })
        self.assertTrue(reservation_form.is_valid(),
                        msg="Empty number_of_guests field is not valid")
