from pydantic import BaseModel
from datetime import date

class PeriodicoBase(BaseModel):
    nombre: str
    fecha_publicacion: date | None = None


class PeriodicoCreate(PeriodicoBase):
    pass


class Periodico(PeriodicoBase):
    id: int

    class Config:
        from_attributes = True