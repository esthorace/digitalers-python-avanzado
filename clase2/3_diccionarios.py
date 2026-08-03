from pprint import pprint

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

pprint(diccionario)

diccionario_vacio = {}
diccionario_vacio = dict()
print(diccionario_vacio)

# Acceder a los valores del diccionario
print(diccionario["nombre"])
print(diccionario["edad"])

# Crear
diccionario["email"] = "juan@example.com"
pprint(diccionario)

# Actualizar un valor
diccionario["edad"] = 31
pprint(diccionario)

# Eliminar un valor
del diccionario["email"]
pprint(diccionario)


# Desempacar un diccionario
datos_civiles = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}

datos_estudios = {
    "universidad": "Universidad de Madrid",
    "carrera": "Ingeniería Informática",
    "promedio": 8.5,
}

datos_completos = {**datos_civiles, **datos_estudios}
pprint(datos_completos)
