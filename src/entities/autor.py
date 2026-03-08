from sqlalchemy import Column, Integer, String
from src.database.connection import Base

class Autor(Base):
    __tablename__ = "autor"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    nacionalidad = Column(String(100))