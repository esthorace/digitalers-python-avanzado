"""
RESOLVER CON LISTAS POR COMPRENSION Y SUM

A partir de la siguiente lista:
matriz:

matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

Sumar los elementos de cada lista y agregar el resultado
al final de cada lista. Debe quedar de la siguiente forma:

matriz = [
    [1, 20, 3, 24],
    [4, 3, 2, 9],
    [10, 4, 1, 15],
]
"""

matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

# matriz_nueva = []
# for fila in matriz:
# fila.append(sum(fila))
# matriz_nueva.append(fila)
# matriz_nueva += [fila + [sum(fila)]]

matriz_nueva = [fila + [sum(fila)] for fila in matriz]

print(matriz_nueva)
