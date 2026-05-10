from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import PacienteCreate
from models import Paciente

router = APIRouter()

@router.post("/", response_model=PacienteCreate)
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
