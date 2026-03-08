from pydantic import BaseModel

class LibroBase(BaseModel):
    titulo: str
    editorial: str | None = None
    anio_publicacion: int | None = None
    autor_id: int | None = None


class LibroCreate(LibroBase):
    pass


class Libro(LibroBase):
    id: int

    class Config:
        from_attributes = True