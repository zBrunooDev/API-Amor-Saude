from sqlalchemy.orm import Session
from models import Paciente
from models import Consulta

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

def create_consulta(db: Session, consulta):

    db_consulta = Consulta(
        id=consulta.id,
        pacienteId=consulta.pacienteId,
        usuarioId=consulta.usuarioId,
        data=consulta.data,
        observacoes=consulta.observacoes,
        status=consulta.status
    )

    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)

    return db_consulta

def get_consultas(db: Session):
    return db.query(Consulta).all()


def get_consulta_by_id(db: Session, consulta_id: str):

    return db.query(Consulta).filter(
        Consulta.id == consulta_id
    ).first()

def delete_consulta(db: Session, consulta_id: str):

    consulta = db.query(Consulta).filter(
        Consulta.id == consulta_id
    ).first()

    if not consulta:
        return None

    db.delete(consulta)
    db.commit()

    return consulta

def get_consultas_by_paciente_id(
    db: Session,
    paciente_id: str
):

    return db.query(Consulta).filter(
        Consulta.pacienteId == paciente_id
    ).all()