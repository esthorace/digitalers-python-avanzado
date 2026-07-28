numero = int(input("Ingrese un número: "))


match numero:
    case 1:
        print("El número es 1")
    case 2:
        print("El número es 2")
    case 3:
        print("El número es 3")
    case _:
        print("El número no es 1, 2 o 3")
