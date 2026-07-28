lista = [12, 100, 34]

match lista:
    case []:
        print("La lista está vacía")
    case [x]:
        print(f"La lista tiene un solo elemento: {x}")
    case [x, y]:
        print(f"La lista tiene dos elementos: {x} y {y}")
        print(f"La multiplicación de los elementos es: {x * y}")
    case [x, y, otro]:
        print(f"La lista tiene tres elementos: {x}, {y} y {otro}")
        print(f"La suma de los elementos es: {x + y + otro}")
    case _:
        print("La lista tiene más de tres elementos")
