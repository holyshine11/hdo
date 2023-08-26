from django.db import models
from django.utils.translation import gettext as _

class Station(models.Model):
    MOILST = models.CharField(max_length=30)
    MOJUSO1 = models.CharField(max_length=100)
    MAPS_X = models.FloatField()
    MAPS_Y = models.FloatField()
    UJONG = models.CharField(max_length=1)
    SMART = models.BooleanField(default=False)
    PRICE = models.IntegerField()