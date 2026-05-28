from pydantic import BaseModel

class PacienteCreate(BaseModel):
    id: str
    nome: str
    sobrenome: str
    cpf: str
    email: str
    cep: str
    telefone: str
    sexo: str

class PacienteUpdate(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    email: str
    cep: str
    telefone: str
    sexo: str

class ConsultaBase(BaseModel):
    pacienteId: str
    usuarioId: str
    data: str
    observacoes: str
    status: str

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(ConsultaBase):
    pass
