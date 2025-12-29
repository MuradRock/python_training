from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.models.availability import Availability
from app.services.appointment_service import book_appointment
from app.api.deps import get_current_user

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("", response_model=AppointmentOut)
async def create_appointment_api(
    data: AppointmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if current_user.role != "PATIENT":
        raise HTTPException(status_code=403, detail="Only patients can book")

    availability = await db.get(Availability, data.availability_id)
    if not availability:
        raise HTTPException(status_code=404, detail="Slot not found")

    return await book_appointment(db, current_user.id, availability)
