from django.db import models

# Create your models here.
class Datatransport(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)
    station = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    altitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    trayek = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    stationtransit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datatransport'