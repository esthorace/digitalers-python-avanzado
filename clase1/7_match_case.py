dato = {"precio": 1.3}

match dato:
    case int():
        print("El dato es un número entero")
    case float():
        print("El dato es un número decimal")
    case str():
        print("El dato es una cadena de texto")
    case bool():
        print("El dato es un booleano")
    case list():
        print("El dato es una lista")
    case dict():
        print("El dato es un diccionario")
    case _:
        print("No lo sé")
