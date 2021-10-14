from pydantic import BaseModel
from typing import List


class CurrentMeasurement(BaseModel):
    from_date: str
    till_date: str
    values: List[dict]


class HistoricMeasurementIndex(BaseModel):
    label: str
    backgroundColor: str
    data: List[float]


class HistoricMeasurement(BaseModel):
    labels: List[str]
    datasets: List[HistoricMeasurementIndex]
