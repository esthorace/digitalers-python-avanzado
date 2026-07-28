from math import pi

tupla = (1, -2, pi, "cadena", True, ("a", ""), None)

print(tupla)

# Crear de tupla vacía
tupla_vacia = ()
tupla_vacia = tuple()

print(tupla_vacia)

# Crear una tupla con un solo elemento
tupla_un_elemento = (1,)
print(tupla_un_elemento)

# Acceder a los elementos de la tupla
tupla = ("hola", "mundo", "python")
print(tupla[0])

# No puedo modificar los elementos de la tupla
# tupla[0] = "chau"
# print(tupla)

# Operador ir
print("python" in tupla)

# Desempaquetar la tupla
print("Desempaquetando la tupla:")
numeros_primos = (2, 3, 5)
# primero = numeros_primos[0]
# segundo = numeros_primos[1]
# tercero = numeros_primos[2]
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)

# Concatenar tuplas
tupla_1 = (1, 2, 3)
print(id(tupla_1))
tupla_2 = (4, 5, 6)
print(id(tupla_2))
tupla_1 = tupla_1 + tupla_2  # se destruye la tupla_1 y se crea una nueva tupla_1
print(id(tupla_1))
print(tupla_1)

print("Desempaquetando una tupla con *")
numeros_primos = (2, 3, 5, 7, 11, 13)
primero, *medios, ultimo = numeros_primos
print(primero, medios, ultimo)
