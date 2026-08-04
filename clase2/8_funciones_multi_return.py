def poner_mayusculas(texto: str) -> str:
    """Docstrings: Convierte una cadena a mayúsculas"""
    if texto:
        return texto.upper()
    else:
        return "La cadena está vacía"


print(poner_mayusculas("  hola mundo"))
print(poner_mayusculas(""))
