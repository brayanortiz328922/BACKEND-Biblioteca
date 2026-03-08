from fastapi import FastAPI
from src.endpoints.libros import router as libros_router
from src.endpoints.autores import router as autores_router
from src.endpoints.usuarios import router as usuarios_router
from src.endpoints.revistas import router as revistas_router
from src.endpoints.periodicos import router as periodicos_router
from src.endpoints.prestamos import router as prestamos_router
# para importar la conexion
from src.database.connection import Base, engine

# para importar las entidades
from src.entities import autor
from src.entities import libro
from src.entities import revista
from src.entities import periodico
from src.entities import usuario
from src.entities import prestamo

app = FastAPI()

# para que las tablas se creen en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(libros_router)
app.include_router(autores_router)
app.include_router(usuarios_router)
app.include_router(revistas_router)
app.include_router(periodicos_router)
app.include_router(prestamos_router)

@app.get("/")
def read_root():
    return {"mensaje": "API biblioteca funcionando"}