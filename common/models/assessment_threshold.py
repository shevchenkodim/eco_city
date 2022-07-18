from django.db import models
from common.models.indicator import Indicator
from common.models.period import TimePeriod


class AssessmentThreshold(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.PROTECT)
    period = models.ForeignKey(TimePeriod, on_delete=models.PROTECT, related_name="period")
    period_value = models.IntegerField(default=0)
    min_limit = models.FloatField(default=0.00)
    max_limit = models.FloatField(default=0.00)
    max_limit_percent = models.FloatField(default=0.00)
    max_allow_overrun_number = models.FloatField(default=0.00)
    overrun_period = models.ForeignKey(TimePeriod, on_delete=models.PROTECT, related_name="overrun_period")

    class Meta:
        db_table = "assessment_threshold"
