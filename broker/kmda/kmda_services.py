from typing import List, Tuple

import requests

from broker.eco_base import EcoServiceBase
from broker.kmda.entity import KMDASensorsResult
from common.models.indicator import Indicator
from common.models.sensor import Sensor
from core.settings import ECO_KMDA_URL_SENSOR_DATA, ECO_KMDA_URL_SENSORS_INFO

DEVICE_KEY = "device_id"


class KMDAService(EcoServiceBase):
    def __init__(self, sensors_url: str, sensor_data_url: str):
        self.sensors_url = sensors_url
        self.sensor_data_url = sensor_data_url

    def _get_indicators(self, device_id: str) -> KMDASensorsResult:
        return KMDASensorsResult(**requests.get(f"{self.sensors_url}?{DEVICE_KEY}={device_id}").json())

    def _get_indicator_data(self, sensor_id: str, interval: str = "ten_minutes") -> List[Tuple[int, float]]:
        return requests.get(f"{self.sensor_data_url}?sensor_id={sensor_id}&interval={interval}").json()

    def run_getting_news(self, sensor: Sensor) -> List[Tuple[Indicator, List[Tuple[int, float]]]]:
        res = []
        for ind in self._get_indicators(sensor.sensor_id).sensors:
            # get identifier
            ind_db = Indicator.objects.get_or_create(code=ind.sensor, name=ind.type_name, indicator_type=ind.type,
                                                     unit=ind.unit, description=ind.description,
                                                     type_desc=ind.type_name)[0]
            res.append((ind_db, self._get_indicator_data(ind.id)))
        return res


kmda_service = KMDAService(ECO_KMDA_URL_SENSORS_INFO, ECO_KMDA_URL_SENSOR_DATA)
