from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas

from database import get_db

router = APIRouter()

@router.post("/")
def criar_consulta(
    consulta: schemas.ConsultaCreate,
    db: Session = Depends(get_db)
):

    return crud.create_consulta(db, consulta)

@router.get("/")
def listar_consultas(
    db: Session = Depends(get_db)
):

    return crud.get_consultas(db)

@router.get("/paciente/{paciente_id}")
def listar_consultas_por_paciente(
    paciente_id: str,
    db: Session = Depends(get_db)
):

    consultas = crud.get_consultas_by_paciente_id(
        db,
        paciente_id
    )

    return consultas

@router.get("/{consulta_id}")
def buscar_consulta(
    consulta_id: str,
    db: Session = Depends(get_db)
):

    consulta = crud.get_consulta_by_id(
        db,
        consulta_id
    )

    if not consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    return consulta 

@router.delete("/{consulta_id}")
def deletar_consulta(
    consulta_id: str,
    db: Session = Depends(get_db)
):

    deleted_consulta = crud.delete_consulta(
        db,
        consulta_id
    )

    if not deleted_consulta:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada"
        )

    return {
        "message": "Consulta deletada com sucesso"
    }

