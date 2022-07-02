from abc import ABC, abstractmethod
from typing import List, Tuple

from common.models.indicator import Indicator
from common.models.sensor import Sensor


class EcoServiceBase(ABC):

    @abstractmethod
    def run_getting_news(self, sensor: Sensor) -> List[Tuple[Indicator, List[Tuple[int, float]]]]:
        pass
