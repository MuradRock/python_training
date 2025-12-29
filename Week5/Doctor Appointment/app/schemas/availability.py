from datetime import datetime
from pydantic import BaseModel

class AvailabilityOut(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True
