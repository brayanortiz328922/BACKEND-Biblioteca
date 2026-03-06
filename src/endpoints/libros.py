from fastapi import APIRouter

router = APIRouter()

@router.get("/libros")
def obtener_libros():
    return [
        {"id": 1, "titulo": "Clean Code", "autor": "Robert Martin"},
        {"id": 2, "titulo": "Python Crash Course", "autor": "Eric Matthes"}
    ]