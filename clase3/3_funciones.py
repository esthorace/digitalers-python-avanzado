def mostrar_caracteristicas(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


def main():
    mostrar_caracteristicas(nombre="Juan", edad=30, ciudad="Madrid")
    # mostrar_caracteristicas(id=1, username="juan123", email="juan123@gmail.com")
    diccionario = {"id": 1, "username": "juan123", "email": "juan123@gmail.com"}
    mostrar_caracteristicas(**diccionario)


main()
