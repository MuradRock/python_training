from fastapi import HTTPException
from app.repositories.user_repo import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User

async def register_user(db, data):
    if await get_user_by_email(db, data.email):
        raise HTTPException(400, "User already exists")

    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        role=data.role,
        name=data.name
    )
    await create_user(db, user)
    return user

async def login_user(db, email, password):
    user = await get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    return create_access_token(str(user.id), user.role)
