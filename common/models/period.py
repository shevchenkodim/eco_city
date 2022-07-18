from django.db import models


class TimePeriod(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код")
    name = models.CharField(max_length=50, verbose_name="Значення")

    class Meta:
        db_table = "time_period"

