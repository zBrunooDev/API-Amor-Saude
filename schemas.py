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
    id: str
    pacienteId: str
    usuarioId: str
    data: str
    observacoes: str
    status: str


class ConsultaCreate(ConsultaBase):
    pass


class ConsultaUpdate(ConsultaBase):
    pass


class UsuarioBase(BaseModel):
    id: str
    nome: str
    sobrenome: str
    email: str
    cpf: str
    role: str
    passwordHash: str


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(UsuarioBase):
    pass
