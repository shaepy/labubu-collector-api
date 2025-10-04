from django.db import models
from items.models import Item


class Collection(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(
        max_length=60, help_text="User Collection Name")
    # reference to multiple collectibles
    collectibles = models.ManyToManyField(
        Item,
        related_name="collections"
    )
    # TODO-ST : reference to a user in the future
