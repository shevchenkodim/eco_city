from django.db import models


class SensorType(models.Model):
    code = models.CharField(max_length=100, unique=True, verbose_name="Код")
    name = models.CharField(max_length=100, verbose_name="Значення")

    class Meta:
        db_table = "sensor_type"


class Sensor(models.Model):
    sensor_id = models.CharField(max_length=100, unique=True, verbose_name="Унікальний ідентифікатор")
    sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE, verbose_name="Тип")

    class Meta:
        db_table = "sensor"
