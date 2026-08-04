def sumar(a: int, b: int, c=0) -> int:
    """Suma tres números enteros, el tercer número es opcional y por defecto es 0"""
    return a + b + c


def main():
    resultado = sumar(1, 2)
    print(f"El resultado de la suma es: {resultado}")

    resultado = sumar(1, 2, 3)
    print(f"El resultado de la suma es: {resultado}")


main()
