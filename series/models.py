from django.db import models
from franchises.models import Franchise


class Series(models.Model):
    def __str__(self):
        return f'{self.name} - {self.franchise}'
    name = models.CharField(
        max_length=80, help_text="Series Name")
    franchise = models.ForeignKey(
        Franchise,
        related_name="series",
        on_delete=models.CASCADE
    )
    release_date = models.DateField()
    image_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL to an image of this Labubu variant on the web"
    )
