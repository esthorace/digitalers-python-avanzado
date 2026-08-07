import logging

from errores import CapturarErrores


class GestorArchivos:
    def __init__(self, nombre: str):
        self.nombre = nombre
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s - %(levelname)s: %(message)s"
        )

    @CapturarErrores()
    def escribir_archivo(self, contenido: str):
        with open(self.nombre, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
            logging.debug(f"✅ Archivo '{self.nombre}' escrito exitosamente")

    @CapturarErrores()
    def leer_archivo(self):
        with open(self.nombre, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            logging.info(f"✅ Archivo {self.nombre} leído exitosamente")
            return contenido


archivo = "19_test.txt"
gestor = GestorArchivos(archivo)
gestor.escribir_archivo("Python\nDjango\n")
texto = gestor.leer_archivo()
if texto is not None:
    print(texto)
