from pydantic import BaseModel, Field, ConfigDict


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
    model_config = ConfigDict(populate_by_name=True)
    
    id: str
    paciente_id: str = Field(alias="pacienteId")
    usuario_id: str = Field(alias="UsuarioId")
    data: str
    observacoes: str | None = None
    status: str
    especialidade_medico: str = Field(alias="EspecialidadeMedico")


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
