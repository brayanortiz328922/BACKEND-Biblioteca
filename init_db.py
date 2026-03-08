from src.database.connection import engine, Base

import src.entities.autor
import src.entities.libro
import src.entities.usuario
import src.entities.prestamo
import src.entities.periodico
import src.entities.revista

print("Creando tablas en la base de datos...")

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")