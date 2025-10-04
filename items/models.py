from django.db import models
from series.models import Series


class Item(models.Model):
    def __str__(self):
        return f'{self.variant} - secret: {self.is_secret}'
    variant = models.CharField(
        max_length=50, help_text="Name of Variant. Ex. 'Chestnut Cocoa'")
    is_secret = models.BooleanField(default=False)
    series = models.ForeignKey(
        Series,
        related_name="items",
        on_delete=models.CASCADE
    )