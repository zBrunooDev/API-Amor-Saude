from sqlalchemy import Column, String
from database import Base


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
    passwordHash = Column(String, index=True)


class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(String, primary_key=True, index=True)
    pacienteId = Column(String, index=True)
    usuarioId = Column(String, index=True)
    data = Column(String, index=True)
    observacoes = Column(String, index=True)
    status = Column(String, index=True)
