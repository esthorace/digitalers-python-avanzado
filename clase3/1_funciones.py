from typing import Any


def seleccionar_cadenas(*args: Any) -> list[str]:
    """Selecciona las cadenas de la lista de argumentos"""
    lista_cadenas = []
    for i in args:
        if isinstance(i, str):
            lista_cadenas.append(i)
    return lista_cadenas
    # return [i for i in args if isinstance(i, str)]


def mostrar_lista_cadenas(lista: list[str]) -> None:
    for cadena in lista:
        print(cadena)


def main() -> None:
    lista_cadenas = seleccionar_cadenas(
        "Hola", "Python", 12, True, [], {"nombre": "Juan"}, "Django"
    )
    mostrar_lista_cadenas(lista_cadenas)


main()
