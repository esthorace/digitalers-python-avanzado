# Métodos de las listas

serie_fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
print("Serie de Fibonacci:", serie_fibonacci)

# append(): agrega un elemento al final de la lista
numero_siguiente = serie_fibonacci[-1] + serie_fibonacci[-2]
serie_fibonacci.append(numero_siguiente)
print("append():", serie_fibonacci)

# extend(): extiende la lista con los elementos de otra lista
mas_numeros = [233, 377, 610]
serie_fibonacci.extend(mas_numeros)
print("extend():", serie_fibonacci)

# insert()
indice = 0
serie_fibonacci.insert(indice, "INICIO")
print("insert():", serie_fibonacci)

# remove(): elimina el primer elemento que coincide con el valor
serie_fibonacci.remove("INICIO")
print("remove():", serie_fibonacci)

# pop(indice): elimina el elemento en el índice especificado, si no se especifica, elimina el último elemento
ultimo_elemento = serie_fibonacci.pop()
print("pop():", serie_fibonacci, ultimo_elemento)

# sort(): ordena la lista
letras = ["c", "a", "b"]
letras.sort()
print("sort():", letras)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort(reverse=True)
print("sort(reverse=True):", numeros)
