"""
Manejo de excepciones

try:
    # código que puede lanzar una excepción
except:
    # código que se ejecuta si se lanza una excepción
else:
    # (opcional): código que se ejecuta si no se lanza una excepción
finally:
    # (opcional): código que se ejecuta siempre
"""

try:
    numero_1 = int(input("Un número: "))
    numero_2 = int(input("Otro número: "))
    division = numero_1 / numero_2
except ValueError:
    print("Debes ingresar un número")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as mensaje:
    print("Hubo un error:", repr(mensaje))
else:
    print(division)
finally:
    print("👋")
