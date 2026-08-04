def solicitar_numero(mensaje: str) -> int:
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("El dato debe ser un número")


def introducir_datos() -> tuple[int, int]:
    numero_1 = solicitar_numero("Introduce el primer número: ")
    numero_2 = solicitar_numero("Introduce el segundo número: ")
    return numero_1, numero_2


def dividir(numero_1: int, numero_2: int) -> float | None:
    try:
        resultado = numero_1 / numero_2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None
    return resultado


def main():
    numero_1, numero_2 = introducir_datos()
    resultado = dividir(numero_1, numero_2)
    if resultado is not None:
        print(resultado)


main()
