# schemas.py
from pydantic import BaseModel, Field
import datetime

class ClinicalDataCreate(BaseModel):
    patient_name: str = Field(..., example="John Doe")
    weight: int = Field(..., ge=0, le=120, example=45)
    problem: str = Field(..., example="Hypertension")

# The read schema includes the auto-generated fields
class ClinicalDataRead(ClinicalDataCreate):
    weight: int
    recorded_at: datetime.datetime