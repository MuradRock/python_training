from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from app.models.user import Base

class Availability(Base):
    __tablename__ = "availabilities"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    doctor_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)
