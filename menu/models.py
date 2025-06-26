from django.db import models
from django.core.validators import MinValueValidator

TYPE = ((0, "Starter"), (1, "Main"), (2, "Dessert"), (3, "Drink"))

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE, default=0)
    price = models.FloatField(validators=[MinValueValidator(0)])
    added_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["type", "name"]

    def __str__(self):
        return f"{self.name} | {self.get_type_display()} | £{self.price}"