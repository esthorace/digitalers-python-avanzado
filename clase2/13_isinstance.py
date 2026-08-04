def sumar(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parámetros deben ser enteros")
    return a + b


resultado = sumar("10", 23)
print(resultado)
