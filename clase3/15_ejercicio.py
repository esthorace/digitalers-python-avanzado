"""
A partir del siguiente código, usar with

try:
    archivo = open("15_test.txt", "w")
except Exception as error:
    print("Error", repr(error))
else:
    archivo.write("Python\n")
    archivo.write("Django\n")
finally:
    archivo.close()

try:
    archivo = open("15_test.tx", "r")
except FileNotFoundError:
    print("El archivo no existe")
except Exception as error:
    print("Error", repr(error))
else:
    contenido = archivo.read()
    print(contenido)
finally:
    archivo.close()
"""

try:
    with open("15_test.txt", "w") as archivo:
        archivo.write("Python\n")
        archivo.write("Django\n")
except Exception as error:
    print("Error inesperado:", repr(error))

try:
    with open("15_test.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
except Exception as error:
    print("Error inesperado", repr(error))
