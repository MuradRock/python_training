from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.appointment import Appointment
from app.models.availability import Availability
from app.repositories.appointment_repo import create_appointment

async def book_appointment(
    db: AsyncSession,
    patient_id: int,
    availability: Availability
):
    if availability.is_booked:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Slot already booked"
        )

    availability.is_booked = True

    appointment = Appointment(
        doctor_id=availability.doctor_id,
        patient_id=patient_id,
        start_time=availability.start_time,
        end_time=availability.end_time
    )

    return await create_appointment(db, appointment)
