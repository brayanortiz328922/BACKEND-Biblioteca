from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.revista import Revista
from src.schemas.revista_schema import RevistaCreate

router = APIRouter(prefix="/revistas", tags=["Revistas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_revistas(db: Session = Depends(get_db)):
    revistas = db.query(Revista).all()
    return revistas


@router.get("/{id}")
def obtener_revista(id: int, db: Session = Depends(get_db)):
    revista = db.query(Revista).filter(Revista.id == id).first()

    if not revista:
        return {"mensaje": "Revista no encontrada"}

    return revista


@router.post("/", response_model=dict)
def crear_revista(revista: RevistaCreate, db: Session = Depends(get_db)):

    nueva_revista = Revista(
        titulo=revista.titulo,
        numero=revista.numero,
        editorial=revista.editorial
    )

    db.add(nueva_revista)
    db.commit()
    db.refresh(nueva_revista)

    return {"mensaje": "Revista creada correctamente"}


@router.put("/{id}")
def actualizar_revista(id: int, revista: RevistaCreate, db: Session = Depends(get_db)):

    revista_db = db.query(Revista).filter(Revista.id == id).first()

    if not revista_db:
        return {"mensaje": "Revista no encontrada"}

    revista_db.titulo = revista.titulo
    revista_db.numero = revista.numero
    revista_db.editorial = revista.editorial

    db.commit()

    return {"mensaje": "Revista actualizada correctamente"}


@router.delete("/{id}")
def eliminar_revista(id: int, db: Session = Depends(get_db)):

    revista = db.query(Revista).filter(Revista.id == id).first()

    if not revista:
        return {"mensaje": "Revista no encontrada"}

    db.delete(revista)
    db.commit()

    return {"mensaje": "Revista eliminada correctamente"}