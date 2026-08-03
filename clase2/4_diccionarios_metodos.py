diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

# get(key, default=None)
# print(diccionario["nombres"])
print(diccionario.get("nombres", "No encontrado"))

# update(dict)
diccionario.update(email="juan@example.com")
diccionario.update({"edad": 31})
print(diccionario)

# pop(key, default=None)
elemento_eliminado = diccionario.pop("email")
print("Elemento eliminado:", elemento_eliminado)
print(diccionario)

# keys()
print(diccionario.keys())
for k in diccionario.keys():
    print("Clave:", k)

# values()
print(diccionario.values())
for v in diccionario.values():
    print("Valor:", v)

# items()
print(diccionario.items())
for k, v in diccionario.items():
    print(f"Clave: {k} - Valor: {v}")
