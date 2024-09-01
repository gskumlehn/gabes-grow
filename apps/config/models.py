from django.db import models
from apps.stage.models import StageType

class GrowConfig(models.Model):
    lastUpdate = models.DateTimeField(null=False, blank=False, auto_now=True)
    stageType = models.CharField(max_length=2, choices=StageType.choices, default=StageType.VEGETATIVE,  null=False, blank=False)
    watering = models.BooleanField(null=False, blank=False)
    lights = models.BooleanField(null=False, blank=False, default=False)


