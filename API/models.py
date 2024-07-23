from django.db import models

# Create your models here.

class Aff(models.Model):
    hewan = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aff'