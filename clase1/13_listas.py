# Colección mutable de objetos indexados

lista = [1, 2, 3.4, "hola", True, ("a",)]
print(f"{lista=}")

print(type(lista))

lista_vacia = []
lista_vacia = list()
print(lista_vacia)

# Crear
lista = lista + ["fin"]
print(lista)

lista += ["otra vez fin"]
print(lista)

# Acceder a los elementos de la lista
hola = lista[3]
print(hola)

# Modificar los elementos de la lista
lista[0] = {"clave": "valor"}
print(lista)

# Eliminar elementos de la lista
del lista[-1]
print(lista)
