from __future__ import unicode_literals
from django.db import models

class MwTable(models.Model):
    weather_time = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    temp_max = models.CharField(max_length=20, blank=True, null=True)
    temp_min = models.CharField(max_length=20, blank=True, null=True)
    weather_sky = models.CharField(max_length=20, blank=True, null=True)
    rnst = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mw_table'
        unique_together = (('weather_time', 'dist'),)