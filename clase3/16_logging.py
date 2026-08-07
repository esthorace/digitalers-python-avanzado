import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

try:
    with open("15_test.txt", "w") as archivo:
        archivo.write("Python\n")
        archivo.write("Django\n")
        logging.debug("✅ Archivo escrito exitosamente")
except Exception as error:
    logging.critical("Error inesperado:", repr(error))

try:
    with open("15_test.tx", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
        logging.info("✅ Archivo leído exitosamente")
except FileNotFoundError:
    logging.error("El archivo no existe")
except Exception as error:
    logging.critical("Error inesperado", repr(error))
