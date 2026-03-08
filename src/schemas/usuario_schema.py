from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    email: str | None = None


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int
    class Config:
        from_attributes = True