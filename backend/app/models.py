from pydantic import BaseModel
from typing import List

class CurrentMeasurement(BaseModel):
    from_date: str
    till_date: str
    values: List[dict]