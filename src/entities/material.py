from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.connection import Base

class Material(Base):

    __tablename__ = "materiales"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    
    # libro, revista, periodico
    tipo = Column(String)  
    anio_publicacion = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autores.id"))