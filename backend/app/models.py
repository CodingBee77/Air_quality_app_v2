from pydantic import BaseModel
from typing import List


class CurrentMeasurement(BaseModel):
    from_date: str
    till_date: str
    values: List[dict]


class ChartMeasurement(BaseModel):
    label: str
    backgroundColor: str
    data: List[float]


class HistoricMeasurement(BaseModel):
    labels: List[str]
    datasets: List[ChartMeasurement]


class StandardFactorMeasurement(BaseModel):
    organization_name: str
    pollutant: str
    limit: float
    percent: float
    averaging: str


class StandardFactors:
    factors: List[StandardFactorMeasurement]



