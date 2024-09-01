from django.db import models

class StageType(models.TextChoices):
    VEGETATIVE = "VG", "Vegetative"
    FLOWERING = "FL", "Flowering"
    PRE_HARVEST = "PH", "Pre-harvest"

class Stage(models.Model):
    type = models.CharField(max_length=2, choices=StageType.choices, null=False, blank=False)
    lightOnFor = models.IntegerField(null=False, blank=False, default=18)
    lightOn = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    lightOff = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    phMin = models.DecimalField(max_digits=4, decimal_places=2)
    phMax = models.DecimalField(max_digits=4, decimal_places=2)
    tempMin = models.DecimalField(max_digits=4, decimal_places=2)
    tempMax = models.DecimalField(max_digits=4, decimal_places=2)
    soilHumMin = models.DecimalField(max_digits=4, decimal_places=2)
    soilHumMax = models.DecimalField(max_digits=4, decimal_places=2)
    airHumMin = models.DecimalField(max_digits=4, decimal_places=2)
    airHumMax = models.DecimalField(max_digits=4, decimal_places=2)
