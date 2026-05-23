from sqlalchemy.orm import Session
from models import Paciente

def get_pacientes(db: Session):
    return db.query(Paciente).all()

def get_paciente_by_id(db: Session, paciente_id: str):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def update_paciente(
    db: Session,
    paciente_id: str,
    paciente_data
):
    
    paciente = db.query(Paciente).filter(
        Paciente.id == paciente_id
    ).first()

    if not paciente:
        return None

    paciente.nome = paciente_data.nome
    paciente.sobrenome = paciente_data.sobrenome
    paciente.cpf = paciente_data.cpf
    paciente.email = paciente_data.email
    paciente.cep = paciente_data.cep
    paciente.telefone = paciente_data.telefone
    paciente.sexo = paciente_data.sexo

    db.commit()
    db.refresh(paciente)

    return paciente

def delete_paciente(db: Session, paciente_id: str):

    paciente = db.query(Paciente).filter(
        Paciente.id == paciente_id
    ).first()

    if not paciente:
        return None

    db.delete(paciente)
    db.commit()

    return paciente