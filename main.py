from fastapi import FastAPI

import models
from database import engine
from routers import pacientes
from routers import consultas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    pacientes.router,
    prefix="/pacientes",
    tags=["Pacientes"]
)

app.include_router(
    consultas.router,
    prefix="/consultas",
    tags=["Consultas"]
)