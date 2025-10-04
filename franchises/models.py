from django.db import models


class Franchise(models.Model):
    def __str__(self):
        return f'{self.name}'
    name = models.CharField(
        max_length=60, help_text="Franchise. Ex 'Labubu - The Monsters'")
    brand = models.CharField(max_length=40, help_text="ex. POPMART")
