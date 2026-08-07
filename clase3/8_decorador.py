# @decorador -> decorador es una función que recibe una función y devuelve una función

from collections.abc import Callable


def decorador_saludo(funcion: Callable) -> Callable:
    def envoltorio():
        print(f"Hola! antes de la función")
        funcion()
        print(f"Chau! después de la función")

    return envoltorio


@decorador_saludo
def saludo():
    print(f"Hola, mundo!")


# d = decorador_saludo(saludo)
# d()
saludo()
