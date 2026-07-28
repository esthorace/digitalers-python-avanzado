# Métodos de las tuplas

serie_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)
print("Serie de Fibonacci:", serie_fibonacci)

# count()
# Devuelve el número de veces que aparece un elemento en la tupla

cantidad_de_ceros = serie_fibonacci.count(0)
print("Cantidad de ceros:", cantidad_de_ceros)

# index()
# Devuelve el índice del primer elemento que aparece en la tupla
valor_a_buscar = 13
indice_del_valor = serie_fibonacci.index(valor_a_buscar)
print("Índice del valor:", indice_del_valor)
