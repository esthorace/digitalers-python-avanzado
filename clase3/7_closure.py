from collections.abc import Callable


def crear_multiplicador(n: int) -> Callable[[int], int]:
    def multiplicar(x: int) -> int:
        return x * n

    return multiplicar


triplicar = crear_multiplicador(3)
duplicar = crear_multiplicador(2)

print(triplicar(10))  # 30
print(duplicar(10))  # 20
