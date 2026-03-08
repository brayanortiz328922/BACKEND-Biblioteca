from sqlalchemy import Column, Integer, String
from src.database.connection import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True)
    telefono = Column(String)