"""
# Convertir a POO

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def escribir_archivo(ruta: str, contenido: str) -> None:
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
            logging.debug("✅ Archivo escrito exitosamente")
    except PermissionError:
        logging.error("No hay permisos para escribir.")
    except Exception as error:
        logging.critical("Error inesperado:", repr(error))


def leer_archivo(ruta: str) -> str | None:
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            logging.info("✅ Archivo leído exitosamente")
            return contenido
    except FileNotFoundError:
        logging.error("El archivo no existe")
    except Exception as error:
        logging.critical("Error inesperado", repr(error))


escribir_archivo("17_test.txt", "Python\nDjango\n")
texto = leer_archivo("17_test.txt")
if texto is not None:
    print(texto)
"""
