from pydantic import BaseModel
from datetime import date

class PrestamoBase(BaseModel):
    usuario_id: int
    libro_id: int
    fecha_prestamo: date | None = None
    fecha_devolucion: date | None = None


class PrestamoCreate(PrestamoBase):
    pass


class Prestamo(PrestamoBase):
    id: int

    class Config:
        from_attributes = True