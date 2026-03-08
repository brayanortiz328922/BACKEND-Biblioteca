from pydantic import BaseModel

class AutorBase(BaseModel):
    nombre: str
    nacionalidad: str | None = None

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    id: int

    class Config:
        from_attributes = True