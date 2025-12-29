from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.availability import Availability

async def get_doctor_availability(db: AsyncSession, doctor_id: int):
    result = await db.execute(
        select(Availability)
        .where(
            Availability.doctor_id == doctor_id,
            Availability.is_booked == False
        )
    )
    return result.scalars().all()
