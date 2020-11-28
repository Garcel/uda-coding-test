from django.db import models


class GeoPosition(models.Model):
    """Model representing the coordinates of a terrestrial point."""

    # Fields
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)

    # Methods
    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class Asset(models.Model):
    """Model representing an asset."""

    # Fields
    # Mandatory
    geom = models.OneToOneField(GeoPosition, on_delete=models.CASCADE)
    area = models.IntegerField()

    # Optional
    address = models.CharField(max_length=60, blank=True, null=True)
    garage = models.BooleanField(blank=True, null=True)
    other = models.JSONField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)

    # Methods
    def __str__(self):
        return f'{self.geom}'
