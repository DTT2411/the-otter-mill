from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Table(models.Model):

    table_id = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    class Meta:
        ordering = ["-table_id"]


class Reservation(models.Model):
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )
    table = models.OneToOneField(
        Table, on_delete=models.CASCADE, related_name="reserved_table"
    )
    number_of_guests = models.PositiveIntegerField()
    time = models.TimeField()
    date = models.DateField()
    duration = models.PositiveIntegerField()
    special_reqs = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time", "-date"]
