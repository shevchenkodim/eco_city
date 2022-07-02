from typing import List
from pydantic import BaseModel


class KMDADSensorIndicator(BaseModel):
    timestamp: int
    value: float


class KMDADSensor(BaseModel):
    id: str
    sensor: str
    type: str
    type_desc: str
    type_name: str
    unit: str
    value: int
    description: str


class KMDASensorsResult(BaseModel):
    id: int
    sensors: List[KMDADSensor]
