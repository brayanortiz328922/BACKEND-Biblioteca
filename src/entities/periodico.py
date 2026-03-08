from sqlalchemy import Column, Integer, String, Date
from src.database.connection import Base

class Periodico(Base):
    __tablename__ = "periodico"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    fecha_publicacion = Column(Date)