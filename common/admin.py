from django.contrib import admin
from common.models.indicator import Indicator
from common.models.sensor import (SensorType, Sensor)
from common.models.sensor_indicator import SensorIndicators
from common.models.period import TimePeriod
from common.models.assessment_threshold import AssessmentThreshold

admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Indicator)
admin.site.register(SensorIndicators)
admin.site.register(TimePeriod)
admin.site.register(AssessmentThreshold)
