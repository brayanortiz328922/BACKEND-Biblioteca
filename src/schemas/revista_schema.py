from pydantic import BaseModel

class RevistaBase(BaseModel):
    titulo: str
    numero: int | None = None
    editorial: str | None = None


class RevistaCreate(RevistaBase):
    pass


class Revista(RevistaBase):
    id: int

    class Config:
        from_attributes = True