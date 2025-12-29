from sqlalchemy.ext.asyncio import AsyncSession
from app.models.appointment import Appointment

async def create_appointment(db: AsyncSession, appointment: Appointment):
    db.add(appointment)
    await db.commit()
    return appointment
