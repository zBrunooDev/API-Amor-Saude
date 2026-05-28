from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import PacienteCreate
from models import Paciente

import crud
from fastapi import HTTPException
from schemas import PacienteUpdate

router = APIRouter()


@router.post("/pacientes", response_model=PacienteCreate)
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


@router.get("/pacientes")
def listar_pacientes(db: Session = Depends(get_db)):
    return crud.get_pacientes(db)


@router.get("/pacientes/por-email")
def listar_pacientes_por_email(email: str, db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes_by_email(db, email)

    if not pacientes:
        raise HTTPException(status_code=404, detail="Nenhum paciente encontrado")
    return pacientes


@router.get("/pacientes/{paciente_id}")
def buscar_paciente(paciente_id: str, db: Session = Depends(get_db)):

    paciente = crud.get_paciente_by_id(db, paciente_id)

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")

    return paciente


@router.put("/pacientes/{paciente_id}")
def atualizar_paciente(
    paciente_id: str, paciente: PacienteUpdate, db: Session = Depends(get_db)
):

    updated_paciente = crud.update_paciente(db, paciente_id, paciente)

    if not updated_paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")

    return updated_paciente


@router.delete("/pacientes/{paciente_id}")
def deletar_paciente(paciente_id: str, db: Session = Depends(get_db)):

    deleted_paciente = crud.delete_paciente(db, paciente_id)

    if not deleted_paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")

    return {"message": "Paciente deletado com sucesso"}
