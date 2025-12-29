from fastapi import APIRouter, Depends
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import register_user, login_user
from app.core.database import get_db

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(data: RegisterRequest, db=Depends(get_db)):
    return await register_user(db, data)

@router.post("/login")
async def login(data: LoginRequest, db=Depends(get_db)):
    return {"access_token": await login_user(db, data.email, data.password)}
