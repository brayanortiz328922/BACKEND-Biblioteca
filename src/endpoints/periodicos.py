from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.periodico import Periodico
from src.schemas.periodico_schema import PeriodicoCreate

router = APIRouter(prefix="/periodicos", tags=["Periodicos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_periodicos(db: Session = Depends(get_db)):
    periodicos = db.query(Periodico).all()
    return periodicos


@router.get("/{id}")
def obtener_periodico(id: int, db: Session = Depends(get_db)):
    periodico = db.query(Periodico).filter(Periodico.id == id).first()

    if not periodico:
        return {"mensaje": "Periodico no encontrado"}

    return periodico


@router.post("/", response_model=dict)
def crear_periodico(periodico: PeriodicoCreate, db: Session = Depends(get_db)):

    nuevo_periodico = Periodico(
        nombre=periodico.nombre,
        fecha_publicacion=periodico.fecha_publicacion
    )

    db.add(nuevo_periodico)
    db.commit()
    db.refresh(nuevo_periodico)

    return {"mensaje": "Periodico creado correctamente"}


@router.put("/{id}")
def actualizar_periodico(id: int, periodico: PeriodicoCreate, db: Session = Depends(get_db)):

    periodico_db = db.query(Periodico).filter(Periodico.id == id).first()

    if not periodico_db:
        return {"mensaje": "Periodico no encontrado"}

    periodico_db.nombre = periodico.nombre
    periodico_db.fecha_publicacion = periodico.fecha_publicacion

    db.commit()

    return {"mensaje": "Periodico actualizado correctamente"}


@router.delete("/{id}")
def eliminar_periodico(id: int, db: Session = Depends(get_db)):

    periodico = db.query(Periodico).filter(Periodico.id == id).first()

    if not periodico:
        return {"mensaje": "Periodico no encontrado"}

    db.delete(periodico)
    db.commit()

    return {"mensaje": "Periodico eliminado correctamente"}