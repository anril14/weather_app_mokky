from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    lat: float
    lon: float
    units: Optional[str] = 'metric'

class ReportBase(BaseModel):
    description: str
    location: Location

class ReportCreate(ReportBase):
    pass

class ReportFull(ReportBase):
    id: int
    created_date: str
    weather: dict
