from django.db import models

from common.models.sensor import Sensor
from common.models.indicator import Indicator


class SensorIndicators(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=20)
    time = models.DateTimeField()
    value = models.FloatField()

    class Meta:
        db_table = "sensor_indicator"
        unique_together = ("sensor", "indicator", "timestamp")
        ordering = ["time"]
