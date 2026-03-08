from sqlalchemy import Column, Integer, ForeignKey, Date
from src.database.connection import Base

class Prestamo(Base):

    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materiales.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)