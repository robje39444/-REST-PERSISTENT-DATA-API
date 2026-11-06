# models.py
from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base

class ClinicalData(Base):
    __tablename__ = "clinical_data"

    patient_name = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    problem = Column(String, nullable=False)
    recorded_at = Column(DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        """Return a JSON‑serialisable dict representation."""
        return {
            "patient_name": self.patient_name,
            "weight": self.weight,
            "problem": self.problem,
            "recorded_at": self.recorded_at.isoformat(),
        }