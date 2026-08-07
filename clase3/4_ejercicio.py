"""
Escribe una función llamada mostrar_perfil que utilice **kwargs
para recibir una cantidad variable de datos en formato clave-valor
y muestre en la consola cada clave junto con su valor en una línea independiente.
Comprueba su funcionamiento llamando a la función una vez con dos datos (como nombre y edad)
y otra vez con tres datos diferentes (como curso, nota y aprobado).
"""


def mostrar_perfil(**kwargs):
    """Muestra el perfil de una persona"""
    for clave, valor in kwargs.items():
        print(f"{clave.upper()}: {valor}")


def main():
    mostrar_perfil(nombre="Juan", edad=30)
    mostrar_perfil(curso="Python", nota=9.5, aprobado=True)
    diccionario = {"nombre": "Juan", "edad": 30}
    mostrar_perfil(**diccionario)


main()
