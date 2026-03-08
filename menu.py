import requests

BASE_URL = "http://127.0.0.1:8000"


def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Libros")
        print("2. Autores")
        print("3. Usuarios")
        print("4. Revistas")
        print("5. Periodicos")
        print("6. Prestamos")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_entidad("libros")
        elif opcion == "2":
            menu_entidad("autores")
        elif opcion == "3":
            menu_entidad("usuarios")
        elif opcion == "4":
            menu_entidad("revistas")
        elif opcion == "5":
            menu_entidad("periodicos")
        elif opcion == "6":
            menu_entidad("prestamos")
        elif opcion == "0":
            break


def menu_entidad(entidad):
    while True:
        print(f"\n--- {entidad.upper()} ---")
        print("1. Listar")
        print("2. Ver uno")
        print("3. Crear")
        print("4. Actualizar")
        print("5. Eliminar")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            listar(entidad)

        elif opcion == "2":
            id = input("ID: ")
            ver_uno(entidad, id)

        elif opcion == "3":
            crear(entidad)

        elif opcion == "4":
            id = input("ID: ")
            actualizar(entidad, id)

        elif opcion == "5":
            id = input("ID: ")
            eliminar(entidad, id)

        elif opcion == "0":
            break


def listar(entidad):
    r = requests.get(f"{BASE_URL}/{entidad}/")
    print(r.json())


def ver_uno(entidad, id):
    r = requests.get(f"{BASE_URL}/{entidad}/{id}")
    print(r.json())


def crear(entidad):
    datos = {}

    if entidad == "libros":
        datos["titulo"] = input("Titulo: ")
        datos["editorial"] = input("Editorial: ")
        datos["anio_publicacion"] = int(input("Año: "))
        datos["autor_id"] = int(input("Autor ID: "))

    elif entidad == "autores":
        datos["nombre"] = input("Nombre: ")
        datos["nacionalidad"] = input("Nacionalidad: ")

    elif entidad == "usuarios":
        datos["nombre"] = input("Nombre: ")
        datos["email"] = input("Email: ")

    elif entidad == "revistas":
        datos["titulo"] = input("Titulo: ")
        datos["numero"] = int(input("Numero: "))
        datos["editorial"] = input("Editorial: ")

    elif entidad == "periodicos":
        datos["nombre"] = input("Nombre: ")
        datos["fecha_publicacion"] = input("Fecha (YYYY-MM-DD): ")

    elif entidad == "prestamos":
        datos["usuario_id"] = int(input("Usuario ID: "))
        datos["libro_id"] = int(input("Libro ID: "))
        datos["fecha_prestamo"] = input("Fecha prestamo (YYYY-MM-DD): ")
        datos["fecha_devolucion"] = input("Fecha devolucion (YYYY-MM-DD): ")

    r = requests.post(f"{BASE_URL}/{entidad}/", json=datos)
    print(r.json())


def actualizar(entidad, id):
    print("Ingrese los nuevos datos")

    datos = {}

    if entidad == "libros":
        datos["titulo"] = input("Titulo: ")
        datos["editorial"] = input("Editorial: ")
        datos["anio_publicacion"] = int(input("Año: "))
        datos["autor_id"] = int(input("Autor ID: "))

    elif entidad == "autores":
        datos["nombre"] = input("Nombre: ")
        datos["nacionalidad"] = input("Nacionalidad: ")

    elif entidad == "usuarios":
        datos["nombre"] = input("Nombre: ")
        datos["email"] = input("Email: ")

    elif entidad == "revistas":
        datos["titulo"] = input("Titulo: ")
        datos["numero"] = int(input("Numero: "))
        datos["editorial"] = input("Editorial: ")

    elif entidad == "periodicos":
        datos["nombre"] = input("Nombre: ")
        datos["fecha_publicacion"] = input("Fecha (YYYY-MM-DD): ")

    elif entidad == "prestamos":
        datos["usuario_id"] = int(input("Usuario ID: "))
        datos["libro_id"] = int(input("Libro ID: "))
        datos["fecha_prestamo"] = input("Fecha prestamo (YYYY-MM-DD): ")
        datos["fecha_devolucion"] = input("Fecha devolucion (YYYY-MM-DD): ")

    r = requests.put(f"{BASE_URL}/{entidad}/{id}", json=datos)
    print(r.json())


def eliminar(entidad, id):
    r = requests.delete(f"{BASE_URL}/{entidad}/{id}")
    print(r.json())


menu_principal()