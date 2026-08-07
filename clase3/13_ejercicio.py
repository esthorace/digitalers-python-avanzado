"""
A partir del siguiente código, crear un bloque
try-except para que muestre "el archivo no existe"

archivo = open("13_test.txt", "w")
archivo.write("Python\n")
archivo.write("Django\n")
archivo.close()

archivo = open("13_test.tx", "r")
contenido = archivo.read()
archivo.close()
print(contenido)
"""

try:
    archivo = open("13_test.txt", "w")
except Exception as error:
    print("Error", repr(error))
else:
    archivo.write("Python\n")
    archivo.write("Django\n")
finally:
    archivo.close()

try:
    archivo = open("13_test.tx", "r")
except FileNotFoundError:
    print("El archivo no existe")
except Exception as error:
    print("Error", repr(error))
else:
    contenido = archivo.read()
    print(contenido)
finally:
    archivo.close()
