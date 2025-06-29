from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Reservation, Table


class TestReservationViews(TestCase):
    """
    Tests GET requests for the create, delete and edit reservation views.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="ottermill123",
            email="testuser@test.com"
        )
        self.client.login(username="TestUser", password="ottermill123")
        self.table = Table.objects.create(table_id='1', capacity=6)

    def test_create_reservation(self):
        response = self.client.get(reverse('create_reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/reservation_form.html')

    def test_edit_reservation(self):
        reservation = Reservation.objects.create(
            guest=self.user,
            table=self.table,
            number_of_guests=3,
            date='2025-07-01',
            time='20:30:00',
            duration=3,
            special_reqs='None'
        )
        response = self.client.post(reverse('edit_reservation',
                                            args=[reservation.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_reservation(self):
        reservation = Reservation.objects.create(
            guest=self.user,
            table=self.table,
            number_of_guests=3,
            date='2025-07-01',
            time='20:30:00',
            duration=3,
            special_reqs='None'
        )
        response = self.client.post(reverse('delete_reservation',
                                            args=[reservation.pk]))
        self.assertEqual(response.status_code, 302)
