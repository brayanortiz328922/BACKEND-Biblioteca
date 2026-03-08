# BACKEND-Biblioteca
Sistema de informacion para una biblioteca
# Sistema de Biblioteca (FastAPI)

API REST desarrollada con **FastAPI** para gestionar un sistema de biblioteca.

Permite realizar operaciones CRUD sobre:

- Libros
- Autores
- Usuarios
- Revistas
- Periódicos
- Préstamos

Además incluye un **menú por consola** que consume la API mediante HTTP.

---

# Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- Pydantic
- Requests
- Uvicorn

---

# Estructura del proyecto


BACKEND-Biblioteca

│

├── app.py

├── menu.py

├── requirements.txt

│

└── src

├── database

├── endpoints

├── entities

└── schemas


---

# Instalación

Crear entorno virtual:


python -m venv venv


Activar entorno virtual:


venv\Scripts\activate


Instalar dependencias:


pip install -r requirements.txt


---

## Inicializar la base de datos

Si necesitas crear las tablas manualmente en la base de datos:


python init_db.py


Este script crea las tablas definidas en las entidades usando SQLAlchemy.


---

# Ejecutar la API


uvicorn app:app --reload


Documentación automática:


http://127.0.0.1:8000/docs


---

# Ejecutar el menú por consola


python menu.py