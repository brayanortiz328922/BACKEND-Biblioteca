from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.prestamo import Prestamo
from src.schemas.prestamo_schema import PrestamoCreate

router = APIRouter(prefix="/prestamos", tags=["Prestamos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_prestamos(db: Session = Depends(get_db)):
    prestamos = db.query(Prestamo).all()
    return prestamos


@router.get("/{id}")
def obtener_prestamo(id: int, db: Session = Depends(get_db)):
    prestamo = db.query(Prestamo).filter(Prestamo.id == id).first()

    if not prestamo:
        return {"mensaje": "Prestamo no encontrado"}

    return prestamo


@router.post("/", response_model=dict)
def crear_prestamo(prestamo: PrestamoCreate, db: Session = Depends(get_db)):

    nuevo_prestamo = Prestamo(
        usuario_id=prestamo.usuario_id,
        libro_id=prestamo.libro_id,
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=prestamo.fecha_devolucion
    )

    db.add(nuevo_prestamo)
    db.commit()
    db.refresh(nuevo_prestamo)

    return {"mensaje": "Prestamo creado correctamente"}


@router.put("/{id}")
def actualizar_prestamo(id: int, prestamo: PrestamoCreate, db: Session = Depends(get_db)):

    prestamo_db = db.query(Prestamo).filter(Prestamo.id == id).first()

    if not prestamo_db:
        return {"mensaje": "Prestamo no encontrado"}

    prestamo_db.usuario_id = prestamo.usuario_id
    prestamo_db.libro_id = prestamo.libro_id
    prestamo_db.fecha_prestamo = prestamo.fecha_prestamo
    prestamo_db.fecha_devolucion = prestamo.fecha_devolucion

    db.commit()

    return {"mensaje": "Prestamo actualizado correctamente"}


@router.delete("/{id}")
def eliminar_prestamo(id: int, db: Session = Depends(get_db)):

    prestamo = db.query(Prestamo).filter(Prestamo.id == id).first()

    if not prestamo:
        return {"mensaje": "Prestamo no encontrado"}

    db.delete(prestamo)
    db.commit()

    return {"mensaje": "Prestamo eliminado correctamente"}