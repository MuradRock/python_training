from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Enum
from enum import Enum as PyEnum
from uuid import uuid4, UUID
from pydantic import BaseModel


class Base(DeclarativeBase):
    pass

class UserRole(str, PyEnum):
    DOCTOR = "doctor"
    PATIENT = "patient"

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole))
    name: Mapped[str] = mapped_column(String)


class DoctorOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

