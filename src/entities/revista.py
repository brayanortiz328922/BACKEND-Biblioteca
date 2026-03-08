from sqlalchemy import Column, Integer, String
from src.database.connection import Base

class Revista(Base):
    __tablename__ = "revista"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    numero = Column(Integer)
    editorial = Column(String(100))