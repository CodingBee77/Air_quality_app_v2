from pydantic import BaseModel
from typing import List


class CurrentMeasurement(BaseModel):
    from_date: str
    till_date: str
    values: List[dict]


class IndexMeasurement(BaseModel):
    label: str
    backgroundColor: str
    data: List[float]


class ChartMeasurement(BaseModel):
    labels: List[str]
    datasets: List[IndexMeasurement]


class StandardFactorMeasurement(BaseModel):
    organization_name: str
    pollutant: str
    limit: float
    percent: float


class StandardFactors(BaseModel):
    factors: List[StandardFactorMeasurement]
