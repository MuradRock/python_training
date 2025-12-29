from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from uuid import UUID, uuid4
from datetime import datetime
from app.models.user import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    doctor_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    patient_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    start_time: Mapped[datetime] = mapped_column(DateTime)
    end_time: Mapped[datetime] = mapped_column(DateTime)

    __table_args__ = (
        UniqueConstraint("doctor_id", "start_time", "end_time"),
    )
