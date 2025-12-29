from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.user_repo import get_all_doctors
from app.models.user import DoctorOut
from app.api.deps import get_current_user

from app.repositories.availability_repo import get_doctor_availability
from app.schemas.availability import AvailabilityOut

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.get("", response_model=list[DoctorOut])
async def list_doctors(
    db: AsyncSession = Depends(get_db),
    _=Depends(get_current_user)
):
    return await get_all_doctors(db)



@router.get("/{doctor_id}/availability", response_model=list[AvailabilityOut])
async def doctor_availability(
    doctor_id: int,
    db: AsyncSession = Depends(get_db),
    _=Depends(get_current_user)
):
    return await get_doctor_availability(db, doctor_id)
