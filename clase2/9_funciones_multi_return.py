def poner_mayusculas(texto: str) -> str | None:
    """Docstrings: Convierte una cadena a mayúsculas"""
    if not texto:
        return
    return texto.upper()


def main():
    entrada = input("Ingrese una cadena: ")
    resultado = poner_mayusculas(entrada)
    if resultado is not None:
        print(f"Resultado: {resultado}")
    else:
        print("La cadena está vacía")


main()
