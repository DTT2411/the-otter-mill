from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


# Create your models here.

class Table(models.Model):

    table_id = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    class Meta:
        ordering = ["-table_id"]

    def __str__(self):
        return f"Table {self.table_id} | {self.capacity}-person table"


class Reservation(models.Model):
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="reserved_table"
    )
    number_of_guests = models.PositiveIntegerField(validators=[MaxValueValidator(6)])
    time = models.TimeField()
    date = models.DateField()
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(3)])
    special_reqs = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time", "-date"]

    def __str__(self):
        return f"Time: {self.time} | Date: {self.date} | Guest: {self.guest.username} | Table: {self.table.table_id}"
    
