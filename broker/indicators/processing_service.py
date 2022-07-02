from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import pytz
from broker.eco_base import EcoServiceBase
from broker.kmda.kmda_services import kmda_service
from common.models.sensor import Sensor
from common.models.sensor_indicator import SensorIndicators
from common.tools.optimizations import check_performance_time
from core.settings import TIME_ZONE


class ProcessingService:
    def __init__(self):
        self.services = {}

    def add(self, key: str, service: EcoServiceBase):
        self.services[key] = service

    def _run_process_sensor(self, type_code: str, s: Sensor):
        for ind, rows in self.services[type_code].run_getting_news(s):
            need_to_create = []
            for t, v in rows:
                time = datetime.fromtimestamp(t / 1000, tz=pytz.timezone(TIME_ZONE))
                need_to_create.append(SensorIndicators(sensor=s, indicator=ind, timestamp=t, value=v, time=time))
            SensorIndicators.objects.bulk_create(need_to_create, batch_size=len(need_to_create),
                                                 ignore_conflicts=True)

    @check_performance_time
    def run_for_type(self, type_code: str):
        with ThreadPoolExecutor(max_workers=8) as executor:
            for s in Sensor.objects.filter(sensor_type__code=type_code):
                executor.submit(self._run_process_sensor, type_code, s)


processing_service = ProcessingService()
processing_service.add("kmda", kmda_service)
