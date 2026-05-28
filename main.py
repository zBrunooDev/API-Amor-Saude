from fastapi import FastAPI

import models
from database import engine
from routers import pacientes
from routers import consultas
from routers import usuarios

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    pacientes.router,
)

app.include_router(
    consultas.router,
)

app.include_router(
    usuarios.router,
)
