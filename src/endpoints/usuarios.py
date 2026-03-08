from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import SessionLocal
from src.entities.usuario import Usuario
from src.schemas.usuario_schema import UsuarioCreate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios


@router.get("/{id}")
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        return {"mensaje": "Usuario no encontrado"}

    return usuario


@router.post("/", response_model=dict)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario creado correctamente"}


@router.put("/{id}")
def actualizar_usuario(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):

    usuario_db = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario_db:
        return {"mensaje": "Usuario no encontrado"}

    usuario_db.nombre = usuario.nombre
    usuario_db.email = usuario.email

    db.commit()

    return {"mensaje": "Usuario actualizado correctamente"}


@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if not usuario:
        return {"mensaje": "Usuario no encontrado"}

    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado correctamente"}