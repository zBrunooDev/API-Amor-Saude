from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import UsuarioCreate
from models import Usuario

import crud
from fastapi import HTTPException

router = APIRouter()


@router.post("/usuarios", response_model=UsuarioCreate)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    db_usuario = Usuario(
        id=usuario.id,
        nome=usuario.nome,
        sobrenome=usuario.sobrenome,
        cpf=usuario.cpf,
        email=usuario.email,
        role=usuario.role,
        passwordHash=usuario.passwordHash,
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db)

    if not usuarios:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    return usuarios


@router.get("/usuarios/por-email")
def listar_usuarios_por_email(email: str, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios_by_email(db, email)

    if not usuarios:
        raise HTTPException(status_code=404, detail="Nenhum usuário encontrado")
    return usuarios


@router.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: str, db: Session = Depends(get_db)):

    usuario = crud.get_usuario_by_id(db, usuario_id)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return usuario


@router.put("/usuarios/{usuario_id}")
def atualizar_usuario(
    usuario_id: str, usuario: UsuarioCreate, db: Session = Depends(get_db)
):

    updated_usuario = crud.update_usuario(db, usuario_id, usuario)

    if not updated_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return updated_usuario


@router.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str, db: Session = Depends(get_db)):

    deleted_usuario = crud.delete_usuario(db, usuario_id)

    if not deleted_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {"message": "Usuário deletado com sucesso"}
