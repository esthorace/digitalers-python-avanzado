"""
Crear una función que reciba argumentos indeterminados que
sean alturas de personas, crear una lista y ordenarla de menor a mayor
y devolver la lista ordenada
Usar isinstance para validar que los argumentos sean de tipo numerico
"""


def ordenar_alturas(*alturas: float) -> list[float]:
    alturas_validas = []
    for altura in alturas:
        if isinstance(altura, float):
            alturas_validas.append(altura)
    alturas_validas.sort()
    return alturas_validas


def main():
    alturas = ordenar_alturas(1.75, 1.80, 1.70, 1.65, 1.60)
    print(alturas)


main()
