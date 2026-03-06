from fastapi import FastAPI
from src.endpoints.libros import router as libros_router

app = FastAPI()

app.include_router(libros_router)

@app.get("/")
def read_root():
    return {"mensaje": "API biblioteca funcionando"}