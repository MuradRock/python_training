from datetime import datetime
from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    doctor_id: int
    availability_id: int

class AppointmentOut(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True
