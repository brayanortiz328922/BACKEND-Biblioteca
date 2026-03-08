from sqlalchemy import Column, Integer, Date, ForeignKey
from src.database.connection import Base

class Prestamo(Base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    libro_id = Column(Integer, ForeignKey("libro.id"))

    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)