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