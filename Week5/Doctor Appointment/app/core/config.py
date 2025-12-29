from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   # DATABASE_URL: str = "postgresql+asyncpg://user:pass@db:5432/doctor_db"
    DATABASE_URL: str = "mysql+asyncmy://root:password@localhost:3306/mydb"
    SECRET_KEY: str = "d9f3e2a1c7b84f1e9a6c2d5b7a8e4f0c9b1a2d3e4f5a6b7c8d9e0f1a2b3c4d"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
