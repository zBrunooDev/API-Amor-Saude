from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

from fastapi import Depends, FastAPI

from database import engine, SessionLocal, Base


app = FastAPI()

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, unique=False, index=True)
    cpf = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    cep = Column(String, index=True)
    telefone = Column(String, index=True)
    sexo = Column(String, index=True)


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(String, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, unique=False, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True)
    role = Column(String, index=True)


class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(String, primary_key=True, index=True)
    pacienteId = Column(String, index=True)
    usuarioId = Column(String, index=True)
    data = Column(String, index=True)
    observacoes = Column(String, index=True)
    status = Column(String, index=True)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PacienteCreate(BaseModel):
    id: str
    nome: str
    sobrenome: str
    cpf: str
    email: str
    cep: str
    telefone: str
    sexo: str


@app.post("/pacientes/", response_model=PacienteCreate)
def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):

    db_paciente = Paciente(
        id=paciente.id,
        nome=paciente.nome,
        sobrenome=paciente.sobrenome,
        cpf=paciente.cpf,
        email=paciente.email,
        cep=paciente.cep,
        telefone=paciente.telefone,
        sexo=paciente.sexo,
    )

    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)

    return db_paciente
