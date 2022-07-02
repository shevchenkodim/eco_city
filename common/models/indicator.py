from django.db import models


class Indicator(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Код показника")
    name = models.CharField(max_length=50, unique=True, verbose_name="Назва показника")
    indicator_type = models.CharField(max_length=50, verbose_name="Тип показника")
    type_desc = models.CharField(max_length=50, verbose_name="Опис індикатора")
    unit = models.CharField(max_length=20, verbose_name="Одиниця вимірювання")
    description = models.CharField(max_length=50, verbose_name="Опис")

    class Meta:
        db_table = "indicator"
