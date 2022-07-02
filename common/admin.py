from django.contrib import admin

from common.models.indicator import Indicator
from common.models.sensor import SensorType, Sensor
from common.models.sensor_indicator import SensorIndicators

admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(Indicator)
admin.site.register(SensorIndicators)

