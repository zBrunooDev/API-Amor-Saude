from sqlalchemy.orm import Session
from models import Paciente, Usuario, Consulta
from schemas import ConsultaCreate


def get_pacientes(db: Session):
    return db.query(Paciente).all()


def get_pacientes_by_email(db: Session, email: str):
    return db.query(Paciente).filter(Paciente.email == email).all()


def get_paciente_by_id(db: Session, paciente_id: str):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()


def update_paciente(db: Session, paciente_id: str, paciente_data):

    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()

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

    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()

    if not paciente:
        return None

    db.delete(paciente)
    db.commit()

    return paciente


def create_consulta(db: Session, consulta: ConsultaCreate):
    db_consulta = Consulta(
        id=consulta.id,
        paciente_id=consulta.paciente_id,  # Muda aqui
        usuario_id=consulta.usuario_id,     # E aqui
        data=consulta.data,
        observacoes=consulta.observacoes,
        status=consulta.status,
        especialidade_medico=consulta.especialidade_medico,  # E aqui
    )
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def get_consultas(db: Session):
    return db.query(Consulta).all()


def get_consulta_by_id(db: Session, consulta_id: str):

    return db.query(Consulta).filter(Consulta.id == consulta_id).first()


def delete_consulta(db: Session, consulta_id: str):

    consulta = db.query(Consulta).filter(Consulta.id == consulta_id).first()

    if not consulta:
        return None

    db.delete(consulta)
    db.commit()

    return consulta


def get_consultas_by_paciente_id(db: Session, paciente_id: str):

    return db.query(Consulta).filter(Consulta.paciente_id == paciente_id).all()


def get_usuarios(db: Session):
    return db.query(Usuario).all()


def get_usuarios_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).all()


def get_usuario_by_id(db: Session, usuario_id: str):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def update_usuario(db: Session, usuario_id: str, usuario_data):

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        return None

    usuario.nome = usuario_data.nome
    usuario.sobrenome = usuario_data.sobrenome
    usuario.cpf = usuario_data.cpf
    usuario.email = usuario_data.email
    usuario.role = usuario_data.role

    db.commit()
    db.refresh(usuario)

    return usuario


def delete_usuario(db: Session, usuario_id: str):

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:
        return None

    db.delete(usuario)
    db.commit()

    return usuario
