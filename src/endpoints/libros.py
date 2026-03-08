from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



from src.database.connection import SessionLocal
from src.entities.libro import Libro
from src.schemas.libro_schema import LibroCreate

router = APIRouter(prefix="/libros", tags=["Libros"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_libros(db: Session = Depends(get_db)):
    libros = db.query(Libro).all()
    return libros

@router.get("/{id}")
def obtener_libro(id: int, db: Session = Depends(get_db)):

    libro = db.query(Libro).filter(Libro.id == id).first()

    if not libro:
        return {"mensaje": "Libro no encontrado"}

    return libro

@router.post("/", response_model=dict)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):

    nuevo_libro = Libro(
        titulo=libro.titulo,
        editorial=libro.editorial,
        anio_publicacion=libro.anio_publicacion,
        autor_id=libro.autor_id
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return {"mensaje": "Libro creado correctamente"}

@router.put("/{id}")
def actualizar_libro(id: int, libro: LibroCreate, db: Session = Depends(get_db)):

    libro_db = db.query(Libro).filter(Libro.id == id).first()

    if not libro_db:
        return {"mensaje": "Libro no encontrado"}

    libro_db.titulo = libro.titulo
    libro_db.editorial = libro.editorial
    libro_db.anio_publicacion = libro.anio_publicacion
    libro_db.autor_id = libro.autor_id

    db.commit()

    return {"mensaje": "Libro actualizado correctamente"}

@router.delete("/{id}")
def eliminar_libro(id: int, db: Session = Depends(get_db)):

    libro = db.query(Libro).filter(Libro.id == id).first()

    if not libro:
        return {"mensaje": "Libro no encontrado"}

    db.delete(libro)
    db.commit()

    return {"mensaje": "Libro eliminado correctamente"}