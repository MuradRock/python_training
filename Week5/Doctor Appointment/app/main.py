from fastapi import FastAPI
from app.api import auth, appointments
from app.api import doctors, appointments


app = FastAPI()

app.include_router(auth.router)
app.include_router(appointments.router)


app.include_router(doctors.router)
app.include_router(appointments.router)
