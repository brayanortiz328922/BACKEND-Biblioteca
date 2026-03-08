from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.autor import Autor
from src.schemas.autor_schema import AutorCreate


router = APIRouter(prefix="/autores", tags=["Autores"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_autores(db: Session = Depends(get_db)):
    autores = db.query(Autor).all()
    return autores


@router.get("/{id}")
def obtener_autor(id: int, db: Session = Depends(get_db)):

    autor = db.query(Autor).filter(Autor.id == id).first()

    if not autor:
        return {"mensaje": "Autor no encontrado"}

    return autor


@router.post("/", response_model=dict)
def crear_autor(autor: AutorCreate, db: Session = Depends(get_db)):

    nuevo_autor = Autor(
        nombre=autor.nombre,
        nacionalidad=autor.nacionalidad
    )

    db.add(nuevo_autor)
    db.commit()
    db.refresh(nuevo_autor)

    return {"mensaje": "Autor creado correctamente"}


@router.put("/{id}")
def actualizar_autor(id: int, autor: AutorCreate, db: Session = Depends(get_db)):

    autor_db = db.query(Autor).filter(Autor.id == id).first()

    if not autor_db:
        return {"mensaje": "Autor no encontrado"}

    autor_db.nombre = autor.nombre
    autor_db.nacionalidad = autor.nacionalidad

    db.commit()

    return {"mensaje": "Autor actualizado correctamente"}


@router.delete("/{id}")
def eliminar_autor(id: int, db: Session = Depends(get_db)):

    autor = db.query(Autor).filter(Autor.id == id).first()

    if not autor:
        return {"mensaje": "Autor no encontrado"}

    db.delete(autor)
    db.commit()

    return {"mensaje": "Autor eliminado correctamente"}