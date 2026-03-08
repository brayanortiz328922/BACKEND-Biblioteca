from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.connection import Base

class Libro(Base):
    __tablename__ = "libro"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    editorial = Column(String(100))
    anio_publicacion = Column(Integer)

    autor_id = Column(Integer, ForeignKey("autor.id"))