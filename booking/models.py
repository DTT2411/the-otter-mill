from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reservation(models.Model):
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )
    number_of_guests = models.IntegerField()
    time = models.TimeField()
    date = models.DateField()
    duration = models.IntegerField()
    special_reqs = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)